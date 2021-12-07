import argparse
import os
import pyjson5
from typing import Any, Dict

import pandas as pd
import matplotlib.pyplot as plt

from vis.bar import draw_bar
from vis.msic import apply_rc_styles
from vis.axes import set_axes


def scale_curve(data: pd.DataFrame, column: str, scale_val: float = 100):
    data[column] *= scale_val


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
    bar_cfg = cfg["bar"]
    data = pd.read_csv(bar_cfg["data_fp"])
    bar_cfg["data"] = data

    # set style sheets
    apply_rc_styles(cfg["style"])
    fig, axes = plt.subplots()
    # set axes
    draw_cfg = cfg["draw"]
    set_axes(axes, draw_cfg["axes"])

    draw_bar(
        axes=axes,
        bar_cfg=bar_cfg,
        draw_cfg=cfg["draw"]
    )

    rotate_x = cfg["draw"]["axes"]["rotate_x"]
    if rotate_x is not None:
        plt.xticks(rotation=rotate_x)

    fig.savefig(save_fp)
    plt.show()
    plt.close()

