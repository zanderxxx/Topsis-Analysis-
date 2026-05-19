"""
L99 TOPSIS 分析命令行入口
用法: python scripts/run_analysis.py <输入Excel路径> [输出Excel路径]
"""

import sys
import os

# 将项目根目录加入 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.pipeline import run_pipeline


def main():
    if len(sys.argv) < 2:
        print("用法: python scripts/run_analysis.py <输入Excel路径> [输出Excel路径]")
        print("示例: python scripts/run_analysis.py data.xlsx result.xlsx")
        sys.exit(1)

    input_excel = sys.argv[1]

    if len(sys.argv) >= 3:
        output_excel = sys.argv[2]
    else:
        # 默认输出到输入文件同目录
        input_dir = os.path.dirname(os.path.abspath(input_excel))
        output_excel = os.path.join(input_dir, "L99_TOPSIS_Analysis_Result.xlsx")

    if not os.path.exists(input_excel):
        print(f"错误: 输入文件不存在 - {input_excel}")
        sys.exit(1)

    print(f"输入文件: {input_excel}")
    print(f"输出文件: {output_excel}")
    print("-" * 50)

    result = run_pipeline(input_excel, output_excel)

    print("\n" + "=" * 50)
    print("TOPSIS 关注度排名 Top 10:")
    print("=" * 50)
    print(result.head(10).to_string(index=False))
    print(f"\n结果已保存至: {output_excel}")


if __name__ == "__main__":
    main()
