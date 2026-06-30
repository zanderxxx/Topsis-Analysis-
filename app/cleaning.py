import pandas as pd

from .config import (
    EXPOSURE_THRESHOLD,
    AVG_DURATION_ANOMALY_THRESHOLD,
    EXCLUDE_SCREENS
)


def clean_data(df):

    screen_col = "每一屏名称"
    duration_col = "每一屏的曝光时长"
    exposure_user_col = "每一屏的曝光人数"

    possible_date_cols = [
        c for c in df.columns
        if "日期" in c or "date" in c.lower()
    ]

    date_col = possible_date_cols[0]

    clean_df = df.copy()

    # 确保曝光时长列为浮点类型，避免修正时类型冲突
    clean_df[duration_col] = clean_df[duration_col].astype(float)

    # 剔除曝光人数过低数据
    clean_df = clean_df[
        clean_df[exposure_user_col] >= EXPOSURE_THRESHOLD
    ].copy()

    # 按屏幕命名片段剔除特殊页面，不再用每日期最后一行推断最后屏
    exclude_mask = clean_df[screen_col].astype(str).apply(
        lambda screen: any(
            excluded_screen in screen
            for excluded_screen in EXCLUDE_SCREENS
        )
    )

    clean_df = clean_df[
        ~exclude_mask
    ].copy()

    adjustment_logs = []

    # 异常值修正
    for screen in clean_df[screen_col].unique():

        screen_df = (
            clean_df[
                clean_df[screen_col] == screen
            ]
            .copy()
            .sort_values(by=date_col)
        )

        screen_df["daily_avg_duration"] = (
            screen_df[duration_col] /
            screen_df[exposure_user_col]
        )

        anomaly_rows = screen_df[
            screen_df["daily_avg_duration"] >
            AVG_DURATION_ANOMALY_THRESHOLD
        ]

        for idx in anomaly_rows.index:

            pos = screen_df.index.get_loc(idx)

            if pos == 0 or pos == len(screen_df) - 1:
                continue

            prev_idx = screen_df.index[pos - 1]
            next_idx = screen_df.index[pos + 1]

            prev_val = clean_df.loc[
                prev_idx,
                duration_col
            ]

            next_val = clean_df.loc[
                next_idx,
                duration_col
            ]

            corrected_val = (
                prev_val + next_val
            ) / 2

            clean_df.loc[
                idx,
                duration_col
            ] = corrected_val

            adjustment_logs.append({
                "每一屏名称": screen,
                "异常日期": str(
                    clean_df.loc[idx, date_col]
                ),
                "原曝光时长": clean_df.loc[
                    idx,
                    duration_col
                ],
                "修正后曝光时长": corrected_val
            })

    log_df = pd.DataFrame(adjustment_logs)

    return clean_df, log_df
