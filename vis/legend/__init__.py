from typing import Any, Dict, List


from matplotlib.axes import Axes
from matplotlib.lines import Line2D


def set_legend(axes: Axes, lines: List[Line2D], legend_cfg: Dict[str, Any]):
    axes.legend(handles=lines, **legend_cfg)

