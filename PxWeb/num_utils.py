import numpy as np

def log_scale_thresholds(data, num_bins=5):
    """
    Logarithmic scaling is useful when the data has a wide range of values.
    It compresses the data into a smaller range, making it easier to visualize.
    
    @param data: The data to be log scaled.
    @type data: list
    @param num_bins: The number of bins to split the data into.
    @type num_bins: int
    @return: The log scaled thresholds
    """
    
    log_data = np.log10(data)
    log_min, log_max = np.min(log_data), np.max(log_data)
    log_bins = np.linspace(log_min, log_max, num_bins + 1)
    return np.power(10, log_bins)


def quantile_thresholds(data, num_bins=5):
    """
    Quantiles split your data into equal-sized groups, ensuring that each range contains roughly the same number of data points.

    How to apply:

    Divide the data into n quantiles (e.g., quartiles, deciles).
    Use these quantiles as thresholds.
    Advantages:

    Works well for skewed data or varying distributions.
    Adjusts dynamically to the data range.
    
    @param data: The data to be split into quantiles.
    @type data: list
    @param num_bins: The number of quantiles to split the data into.
    @type num_bins: int
    @return: The quantile thresholds.
    """
    
    return np.quantile(data, q=np.linspace(0, 1, num_bins + 1))
    
    

def __round_to(base: float, strategy: str, val: float) -> float:
    """
    Rounds a number to the specified base using the given strategy.
    
    @param base: The base to round to.
    @type base: float
    @param strategy: The rounding strategy.
    @type strategy: str
    @param val: The value to be rounded.
    @type val: float
    @return: The rounded value.
    """
    if strategy == 'nearest':
        rounded_val = base * np.round(float(val) / base)
        return int(rounded_val) if rounded_val.is_integer() else float(rounded_val)
    elif strategy == 'floor':
        rounded_val = base * np.floor(float(val) / base)
        return int(rounded_val) if rounded_val.is_integer() else float(rounded_val)
    elif strategy == 'ceiling':
        rounded_val = base * np.ceil(float(val) / base)
        return int(rounded_val) if rounded_val.is_integer() else float(rounded_val)
    else:
        raise ValueError("Invalid rounding strategy")


def progressive_round(val: float, base: float = None, strategy: str = "nearest") -> float:
    """
    Scales and rounds a number based on its value.
    
    @param val: The value to be scaled and rounded.
    @type val: float
    @param base: The base to round to.
    @type base: float or None
    @param strategy: The rounding strategy.
    @type strategy: "nearest" or "floor" or "ceiling"
    @return: The rounded value.
    """
    

    scales = [ # (upper_limit, base)
        (1, 0.25),
        (2, 0.5),
        (5, 1),
        (10, 2.5),
        (20, 5),
        (50, 10),
        (100, 25),
        (500, 100),
        (1000, 250),
        (5000, 1000),
        (10000, 2500),
        (50000, 10000),
        (100000, 25000),
        (500000, 100000),
        (1000000, 250000),
        (5000000, 1000000),
        (10000000, 2500000),
        (50000000, 10000000),
        (100000000, 25000000),
        (500000000, 100000000),
        (1000000000, 250000000),
        (float('inf'), 1000000000)  # For values greater than 1 billion
    ]
    
    for upper_limit, base in scales:
        if abs(val) <= upper_limit:
            return __round_to(base, strategy, val)
