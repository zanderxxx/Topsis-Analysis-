import pandas as pd

from .cleaning import clean_data
from .aggregation import aggregate_data
from .topsis import calculate_topsis
from .report import export_report


def run_pipeline(
    input_excel,
    output_excel
):

    print("读取 Excel...")

    df = pd.read_excel(input_excel)

    print("数据清洗...")

    clean_df, log_df = clean_data(df)

    screen_order = (
        clean_df["每一屏名称"]
        .drop_duplicates()
        .tolist()
    )

    print("聚合计算...")

    group_df = aggregate_data(clean_df)

    print("TOPSIS 分析...")

    result_df = calculate_topsis(group_df)

    print("导出报告...")

    export_report(
        result_df,
        log_df,
        output_excel,
        screen_order
    )

    print("分析完成")

    return result_df
