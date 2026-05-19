from app.pipeline import run_pipeline


if __name__ == "__main__":

    input_excel = "/Users/xiezhidong/Desktop/L99产品介绍页用户行为数据（4月份）.xlsx"

    output_excel = "/Users/xiezhidong/Desktop/L99_TOPSIS_Analysis_Result.xlsx"

    result = run_pipeline(
        input_excel,
        output_excel
    )

    print(result.head(10))
