from typing import Any, Dict, Tuple

import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from vis.colormap import get_colormaps
from vis.msic import colorbar


def draw_heatmap(
    fig: Figure,
    axes: Axes,
    heatmap_cfg: Dict[str, Any],
    draw_cfg: Dict[str, Any]
) -> Tuple[Figure, Axes]:
    """
    Configuration of heatmap:
        "data": np.ndarray
    """
    cmap = None
    if draw_cfg["colormap"] is not None:
        cmap = get_colormaps(draw_cfg["colormap"])

    data: np.ndarray = heatmap_cfg["data"]
    # draw heatmap
    heatmap = axes.imshow(
        data,
        cmap=cmap
    )
    colorbar_cfg = draw_cfg["color_bar"]
    if colorbar_cfg is not None:
        colorbar(heatmap, axes, bar_axes_cfg=colorbar_cfg["axes"])

