from typing import Any, Dict, List, Tuple

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from vis.msic import apply_rc_styles
from vis.axes import set_axes
from vis.legend import set_legend


def draw_lines(
    curve_cfg: List[Dict[str, Any]],
    style_cfg: Dict[str, str],
    draw_cfg: Dict[str, Any]
) -> Tuple[Figure, Axes]:
    """
    Configuration of one curve:
        "data": pd.DataFrame
        "label": name for the line
        "x_axis": column name for x axis
        "y_axis": column name for y axis
    """
    apply_rc_styles(style_cfg)

    fig, axes = plt.subplots()

    # set axes
    set_axes(axes, draw_cfg["axes"])

    lines: List[Line2D] = list()
    for curve in curve_cfg:
        line = axes.plot(
            curve["x_axis"],
            curve["y_axis"],
            data=curve["data"],
            label=curve["label"],
            color=curve["color"]
        )
        lines.extend(line)

    set_legend(axes, lines, draw_cfg["legend"])

    return fig, axes
