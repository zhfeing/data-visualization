from typing import Any, Dict

import matplotlib as mpl
from matplotlib.axes import Axes
from mpl_toolkits.axes_grid1 import make_axes_locatable


def apply_rc_styles(rc_files: Dict[str, str]):
    mpl.rc_file_defaults()
    for rc_file in rc_files.values():
        mpl.rc_file(rc_file, use_default_template=False)


def colorbar(mappable, axes: Axes, bar_axes_cfg: Dict[str, Any]):
    fig = axes.get_figure()
    divider = make_axes_locatable(axes)
    cax = divider.append_axes(**bar_axes_cfg)
    fig.colorbar(mappable, cax=cax)

