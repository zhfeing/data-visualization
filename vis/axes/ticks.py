import copy
import math
from typing import Dict, Any, List

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axis import Axis, XAxis, YAxis


class Ticks:
    def __init__(self):
        self.ticks = None
        self.labels = None

    def get_ticks(self) -> List[float]:
        return self.ticks

    def get_tick_labels(self) -> List[str]:
        return self.labels


class ManualTicks(Ticks):
    def __init__(self, ticks: List[float], labels: List[str] = None):
        super().__init__()
        self.ticks = ticks
        self.labels = labels


class LinearTicks(Ticks):
    def __init__(self, start: float, end: float, step: float) -> None:
        super().__init__()
        num = math.floor((end - start) / step) + 1
        self.ticks = np.linspace(start, end, num)


__TICKS__ = {
    "manual": ManualTicks,
    "linear": LinearTicks,
}


def _get_ticks(config: Dict[str, Any]) -> Ticks:
    if config is None:
        return None
    config = copy.deepcopy(config)
    name = config.pop("name")
    return __TICKS__[name](**config)


def set_tick_pos(
    axes: plt.Axes,
    tick_cfg: Dict[str, Any]
):
    x_axis: XAxis = axes.get_xaxis()
    y_axis: YAxis = axes.get_yaxis()
    # load ticks
    x_major = _get_ticks(tick_cfg["x_major"])
    x_minor = _get_ticks(tick_cfg["x_minor"])
    y_major = _get_ticks(tick_cfg["y_major"])
    y_minor = _get_ticks(tick_cfg["y_minor"])

    def set_ticks(axis: Axis, major_ticks: Ticks = None, minor_ticks: Ticks = None):
        if major_ticks is not None:
            ticks = major_ticks.get_ticks()
            labels = major_ticks.get_tick_labels()
            axis.set_ticks(
                ticks=ticks,
                labels=labels,
                minor=False
            )
        if minor_ticks is not None:
            ticks = minor_ticks.get_ticks()
            labels = minor_ticks.get_tick_labels()
            axis.set_ticks(
                ticks=ticks,
                labels=labels,
                minor=True
            )

    set_ticks(x_axis, x_major, x_minor)
    set_ticks(y_axis, y_major, y_minor)


