import copy
from typing import Callable, Dict, Any, Optional

import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter
import matplotlib.ticker as m_ticker
from matplotlib.axis import XAxis, YAxis


__FORMATTERS__ = {
    # No labels on the ticks.
    "null": m_ticker.NullFormatter,
    # Set the strings manually for the labels.
    "fixed": m_ticker.FixedFormatter,
    # Use string format method.
    "str_method": m_ticker.StrMethodFormatter,
    # Use an old-style sprintf format string.
    "format_str": m_ticker.FormatStrFormatter,
    # Default formatter for scalars: autopick the format string.
    "scalar": m_ticker.ScalarFormatter,
    # Formatter for log axes.
    "log": m_ticker.LogFormatter,
    # Format values for log axis using exponent = log_base(value).
    "log_exp": m_ticker.LogFormatterExponent,
    # Format values for log axis using exponent = log_base(value) using Math text.
    "log_math": m_ticker.LogFormatterMathtext,
    # Format values for log axis using scientific notation.
    "log_sci": m_ticker.LogFormatterSciNotation,
    # Probability formatter.
    "logit": m_ticker.LogitFormatter,
    # Format labels in engineering notation.
    "eng": m_ticker.EngFormatter,
    # Format labels as a percentage.
    "percent": m_ticker.PercentFormatter,
}


def _get_formatter(config: Dict[str, Any] = None):
    if config is None:
        return None
    config = copy.deepcopy(config)
    name = config.pop("name")
    return __FORMATTERS__[name](**config)


def set_tick_formatter(
    axes: plt.Axes,
    config: Dict[str, Any],
    pre_define_formatter: Dict[str, Formatter] = None
):
    """
    pre_define_formatter: must contains: "x_major", "x_minor", "y_major", "y_minor"
    """
    x_axis: XAxis = axes.get_xaxis()
    y_axis: YAxis = axes.get_yaxis()
    # load pre-defined formatters
    if pre_define_formatter is not None:
        x_major = pre_define_formatter["x_major"]
        x_minor = pre_define_formatter["x_minor"]
        y_major = pre_define_formatter["y_major"]
        y_minor = pre_define_formatter["y_minor"]
    else:
        x_major = _get_formatter(config["x_major"])
        x_minor = _get_formatter(config["x_minor"])
        y_major = _get_formatter(config["y_major"])
        y_minor = _get_formatter(config["y_minor"])

    def set_formatter(setter: Callable, formatter: Optional[Formatter] = None):
        if formatter is not None:
            setter(formatter)

    set_formatter(x_axis.set_major_formatter, x_major)
    set_formatter(x_axis.set_minor_formatter, x_minor)
    set_formatter(y_axis.set_major_formatter, y_major)
    set_formatter(y_axis.set_minor_formatter, y_minor)

