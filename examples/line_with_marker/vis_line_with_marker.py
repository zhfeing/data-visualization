import argparse
import os
import pyjson5
from typing import Any, Dict

import pandas as pd
import matplotlib.pyplot as plt

from vis.vis_line import draw_lines
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
    curves = cfg["curves"]
    for curve in curves:
        data = pd.read_csv(curve["data_fp"])
        scale_curve(data, column=curve["y_axis"], scale_val=curve["scale"])
        curve["data"] = data

    # set style sheets
    apply_rc_styles(cfg["style"])
    fig, axes = plt.subplots()
    # set axes
    draw_cfg = cfg["draw"]
    set_axes(axes, draw_cfg["axes"])

    draw_lines(
        axes=axes,
        curve_cfg=curves,
        draw_cfg=draw_cfg
    )
    fig.savefig(save_fp)
    plt.show()
    plt.close()

