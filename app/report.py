import pandas as pd
from pathlib import Path


def export_report(
    result_df,
    log_df,
    output_excel
):

    # -------------------------
    # Excel 输出
    # -------------------------
    with pd.ExcelWriter(
        output_excel,
        engine="openpyxl"
    ) as writer:

        result_df.to_excel(
            writer,
            index=False,
            sheet_name="TOPSIS关注度排名"
        )

        log_df.to_excel(
            writer,
            index=False,
            sheet_name="异常修正日志"
        )

    # -------------------------
    # JSON 输出
    # -------------------------
    json_path = (
        Path(output_excel)
        .with_suffix(".json")
    )

    result_df.to_json(
        json_path,
        orient="records",
        force_ascii=False,
        indent=2
    )

    print(f"JSON 已导出: {json_path}")
