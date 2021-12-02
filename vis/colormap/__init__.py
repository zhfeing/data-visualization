from typing import List


DESCREATE_COLOR = {
    "Color4Line": ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"],
    "ColorLines": [
        "#515151", "#F14040", "#1A6FDF", "#37AD6B", "#B177DE", "#CC9900", "#00CBCC", "#7D4E4E",
        "#8E8E00", "#FB6501", "#6699CC", "#6FB802"
    ],
    "Color4Bar": ["#FDC897", "#9DD79D", "#C2B2D6", "#FFFFA2", "#9ABBF3", "#FEB8F9", "#B2B791", "#B6E4EB"]
}


def get_colors(name: str) -> List[str]:
    return DESCREATE_COLOR[name]

