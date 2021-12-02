import os
from typing import Dict

import matplotlib as mpl
import matplotlib.scale
import matplotlib.pyplot as plt


def apply_rc_styles(rc_files: Dict[str, str]):
    mpl.rc_file_defaults()
    for rc_file in rc_files.values():
        mpl.rc_file(rc_file, use_default_template=False)

