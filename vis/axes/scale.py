import copy
from typing import Dict, Any, Union

import matplotlib.scale as mpl_scale
import matplotlib.pyplot as plt


SCALES = {
    "linear": mpl_scale.LinearScale,
    "log": mpl_scale.LogScale
}


def get_axes_scale(axes: plt.Axes, scale_cfg: Dict[str, Any] = None) -> mpl_scale.ScaleBase:
    if scale_cfg is None:
        return "linear"
    scale_cfg = copy.deepcopy(scale_cfg)
    name = scale_cfg.pop("name")
    scale_fn = SCALES[name](axis=axes, **scale_cfg)
    return scale_fn
