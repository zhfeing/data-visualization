from typing import Dict, Any

from matplotlib.axes import Axes

from . import parse
from .ticks import set_ticks


def set_axes(axes: Axes, axes_cfg: Dict[str, Any]):
    # axes scale
    x_scale = parse.scale(axes, axes_cfg["x_scale"])
    y_scale = parse.scale(axes, axes_cfg["y_scale"])
    # axes title
    axes.set(
        xlim=axes_cfg["x_limit"],
        ylim=axes_cfg["y_limit"],
        xscale=x_scale,
        yscale=y_scale,
        title=axes_cfg["title"],
        xlabel=axes_cfg["x_label"],
        ylabel=axes_cfg["y_label"],
    )
    set_ticks(axes, axes_cfg["x_ticks"], axes_cfg["y_ticks"])

