from typing import Any, Dict, Tuple

import pandas as pd
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from vis.colormap import get_colors


def draw_bar(
    axes: Axes,
    bar_cfg: Dict[str, Any],
    draw_cfg: Dict[str, Any]
) -> Tuple[Figure, Axes]:
    """
    Configuration of bar:
        "data": pd.DataFrame
        "x_axis": column name for x axis
        "y_axis": column name for y axis
    """
    # set color, !color will overrite colormap!
    color = None
    if draw_cfg["colormap"] is not None:
        color = get_colors(draw_cfg["colormap"])
    if draw_cfg["color"] is not None:
        color = draw_cfg["color"]
    # set error bar
    data: pd.DataFrame = bar_cfg["data"]
    y_err = None
    if bar_cfg["error"] is not None:
        err_cfg = bar_cfg["error"]
        y_err = data[err_cfg["err_pos"]]
        if err_cfg["err_neg"] is not None:
            y_err = data[[err_cfg["err_neg"], err_cfg["err_pos"]]].to_numpy().T

    # draw bar plot
    bar_container = axes.bar(
        bar_cfg["x_axis"],
        bar_cfg["y_axis"],
        yerr=y_err,
        data=data,
        error_kw=draw_cfg["error_bar"],
        color=color,
        **draw_cfg["bar"]
    )

    if draw_cfg["bar_label"] is not None:
        axes.bar_label(bar_container, **draw_cfg["bar_label"])
