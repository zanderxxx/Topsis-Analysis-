import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler

from .config import TOPSIS_WEIGHTS


def calculate_topsis(df):

    topsis_df = df.copy()

    metrics = [
        "平均曝光时长",
        "退出率"
    ]

    scaler = MinMaxScaler()

    normalized = scaler.fit_transform(
        topsis_df[metrics]
    )

    norm_df = pd.DataFrame(
        normalized,
        columns=metrics
    )

    # 退出率为负向指标
    norm_df["退出率"] = 1 - norm_df["退出率"]

    # 加权
    for col in metrics:
        norm_df[col] *= TOPSIS_WEIGHTS[col]

    ideal_best = norm_df.max()
    ideal_worst = norm_df.min()

    dist_best = np.sqrt(
        ((norm_df - ideal_best) ** 2).sum(axis=1)
    )

    dist_worst = np.sqrt(
        ((norm_df - ideal_worst) ** 2).sum(axis=1)
    )

    scores = (
        dist_worst /
        (dist_best + dist_worst)
    )

    topsis_df["TOPSIS关注度得分"] = scores.round(4)

    topsis_df = topsis_df.sort_values(
        by="TOPSIS关注度得分",
        ascending=False
    )

    topsis_df["关注度排名"] = range(
        1,
        len(topsis_df) + 1
    )

    return topsis_df
