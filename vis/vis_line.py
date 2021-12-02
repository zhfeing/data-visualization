from typing import Any, Dict, List

from matplotlib.axes import Axes
from matplotlib.lines import Line2D

from vis.legend import set_legend
from vis.colormap import get_colors


def draw_lines(
    axes: Axes,
    curve_cfg: List[Dict[str, Any]],
    draw_cfg: Dict[str, Any]
):
    """
    Configuration of one curve:
        "data": pd.DataFrame
        "label": name for the line
        "x_axis": column name for x axis
        "y_axis": column name for y axis
    """
    # set color, !color will overrite colormap!
    color: List[str] = list()
    if draw_cfg["colormap"] is not None:
        color = get_colors(draw_cfg["colormap"])
    if draw_cfg["color"] is not None:
        color = draw_cfg["color"]
    assert len(color) >= len(curve_cfg), "color is not enough"

    lines: List[Line2D] = list()
    for i, curve in enumerate(curve_cfg):
        line = axes.plot(
            curve["x_axis"],
            curve["y_axis"],
            data=curve["data"],
            label=curve["label"],
            color=color[i]
        )
        lines.extend(line)

    set_legend(axes, lines, draw_cfg["legend"])

