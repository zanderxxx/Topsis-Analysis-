EXPOSURE_THRESHOLD = 20

AVG_DURATION_ANOMALY_THRESHOLD = 1000

EXCLUDE_SCREENS = [
    "scene-download",
    "scene-overview-firstscreen scene-first",
    "scene-0 scene-first"
]

EXCLUDE_LAST_SCREEN = True

TOPSIS_WEIGHTS = {
    "平均曝光时长": 0.7,
    "退出率": 0.3
}
