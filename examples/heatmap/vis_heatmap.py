import argparse
import os
from typing import Any, Dict

import pyjson5
import h5py
import pandas as pd
import matplotlib.pyplot as plt

from vis.heatmap import draw_heatmap
from vis.msic import apply_rc_styles
from vis.axes import set_axes


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--save-path", type=str)
    parser.add_argument("--config-fp", type=str)
    args = parser.parse_args()

    with open(args.config_fp, "r") as f:
        cfg: Dict[str, Any] = pyjson5.load(f)

    # initialization
    save_fp = cfg["save_fp"]
    save_path = os.path.dirname(save_fp)
    os.makedirs(save_path, exist_ok=True)

    # read data files
    heatmap = cfg["heatmap"]
    with h5py.File(heatmap["data_fp"]) as data_file:
        heatmap["data"] = data_file[heatmap["name"]][:]

    # set style sheets
    apply_rc_styles(cfg["style"])
    fig, axes = plt.subplots()
    # set axes
    draw_cfg = cfg["draw"]
    set_axes(axes, draw_cfg["axes"])

    draw_heatmap(
        fig=fig,
        axes=axes,
        heatmap_cfg=heatmap,
        draw_cfg=draw_cfg
    )
    fig.savefig(save_fp)
    plt.show()
    plt.close()

