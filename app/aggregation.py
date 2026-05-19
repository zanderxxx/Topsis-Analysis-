
def aggregate_data(df):

    screen_col = "每一屏名称"
    duration_col = "每一屏的曝光时长"
    exposure_user_col = "每一屏的曝光人数"

    group_df = (
        df.groupby(screen_col, as_index=False)
        .agg({
            "每一屏的曝光次数": "sum",
            exposure_user_col: "sum",
            duration_col: "sum",
            "最后一屏的退出人数": "sum"
        })
    )

    # 平均曝光时长
    group_df["平均曝光时长"] = (
        group_df[duration_col] /
        group_df[exposure_user_col]
    )

    # 退出率
    group_df["退出率"] = (
        group_df["最后一屏的退出人数"] /
        group_df[exposure_user_col]
    )

    return group_df
