# L99 TOPSIS Attention Analysis

## 安装 Skill

本项目包含 Roo Code skill（`.roo/skills/l99-topsis-analysis/`），有以下几种安装方式：

### 方式一：克隆项目（自动获得 skill）

```bash
git clone git@github.com:zanderxxx/-Topsis-.git
cd -Topsis-
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

用 VS Code + Roo Code 打开项目目录后，`.roo/skills/` 中的 skill 会被自动识别加载。

### 方式二：安装为用户级全局 skill

如果想在任何项目中都能使用此 skill，将 skill 目录复制到全局位置：

```bash
cp -r .roo/skills/l99-topsis-analysis ~/.agents/skills/
```

### 方式三：打包为 .skill 文件分发

```bash
cd .roo/skills
zip -r l99-topsis-analysis.skill l99-topsis-analysis/
```

将生成的 `l99-topsis-analysis.skill` 文件发给对方，对方将其解压到 `~/.agents/skills/` 即可。

---

## 功能

- Excel 数据读取
- 数据清洗
- 异常值修正
- 多日期聚合
- 平均曝光时长计算
- 退出率计算
- TOPSIS 关注度分析
- Excel 结果导出

---

## 安装依赖

```bash
pip install -r requirements.txt
```

---

## 运行

```bash
python main.py
```

---

## 输出

生成：

```text
L99_TOPSIS_Analysis_Result.xlsx
```
