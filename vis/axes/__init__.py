from typing import Dict, Any

from matplotlib.axes import Axes

from . import scale
from .ticks import set_tick_pos
from .formatter import set_tick_formatter


def set_axes(axes: Axes, axes_cfg: Dict[str, Any], tick_kwargs: Dict[str, Any] = dict()):
    # axes scale
    x_scale = scale.get_axes_scale(axes, axes_cfg["x_scale"])
    y_scale = scale.get_axes_scale(axes, axes_cfg["y_scale"])
    # set limit
    if axes_cfg["x_limit"] is not None:
        axes.set_xlim(axes_cfg["x_limit"])
    if axes_cfg["y_limit"] is not None:
        axes.set_ylim(axes_cfg["y_limit"])
    # axes title
    axes.set(
        xscale=x_scale,
        yscale=y_scale,
        title=axes_cfg["title"],
        xlabel=axes_cfg["x_label"],
        ylabel=axes_cfg["y_label"],
    )
    ticks_cfg = axes_cfg["ticker"]
    set_tick_formatter(axes, ticks_cfg["formatter"])
    set_tick_pos(axes, ticks_cfg["ticks"])

