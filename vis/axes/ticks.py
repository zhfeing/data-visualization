import math
from typing import Callable, Dict, Any, List

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from matplotlib.axis import XAxis, YAxis


def _set_ticks(tick_fn: Callable, major_cfg: Dict[str, Any], minor_cfg: Dict[str, Any]):
    # set major ticks
    if major_cfg is not None:
        major_ticks = _get_ticks(
            min=major_cfg["min"],
            max=major_cfg["max"],
            step=major_cfg["step"]
        )
        tick_fn(
            ticks=major_ticks,
            labels=major_cfg["labels"],
            minor=False
        )
    # set minor ticks
    if minor_cfg is not None:
        # set major ticks
        minor_ticks = _get_ticks(
            min=minor_cfg["min"],
            max=minor_cfg["max"],
            step=minor_cfg["step"]
        )
        tick_fn(
            ticks=minor_ticks,
            labels=minor_cfg["labels"],
            minor=True
        )


def _get_ticks(min: float, max: float, step: float) -> np.ndarray:
    num = math.floor((max - min) / step) + 1
    ticks = np.linspace(min, max, num)
    return ticks


def _set_tick_formatters(axes: plt.Axes, x_cfg: Dict[str, Any], y_cfg: Dict[str, Any]):
    # set x ticks
    x_axis: XAxis = axes.get_xaxis()

    if x_cfg["major"] is not None and x_cfg["major"]["format"] is not None:
        x_axis.set_major_formatter(StrMethodFormatter(x_cfg["major"]["format"]))
    if x_cfg["minor"] is not None and x_cfg["minor"]["format"] is not None:
        x_axis.set_minor_formatter(StrMethodFormatter(x_cfg["minor"]["format"]))
    # set y ticks
    y_axis: YAxis = axes.get_yaxis()

    if y_cfg["major"] is not None and y_cfg["major"]["format"] is not None:
        y_axis.set_major_formatter(StrMethodFormatter(y_cfg["major"]["format"]))
    if y_cfg["minor"] is not None and y_cfg["minor"]["format"] is not None:
        y_axis.set_minor_formatter(StrMethodFormatter(y_cfg["minor"]["format"]))


def set_ticks(axes: plt.Axes, x_cfg: Dict[str, Any], y_cfg: Dict[str, Any]):
    _set_ticks(axes.set_xticks, x_cfg["major"], x_cfg["minor"])
    _set_ticks(axes.set_yticks, y_cfg["major"], y_cfg["minor"])
    _set_tick_formatters(axes, x_cfg, y_cfg)

