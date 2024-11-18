import numpy as np

def log_scale(datavalues):
    """
    Applies a log transformation to the data values.
    
    @param datavalues: The data values.
    @type datavalues: list
    @return: The data values with log base 10 transformation applied.
    """
    return [np.log10(value) for value in datavalues]


def inverse_log_scale(datavalues):
    """
    Applies an inverse log transformation to the data values.
    
    @param datavalues: The data values.
    @type datavalues: list
    @return: The data values with inverse log base 10 transformation applied.
    """
    return [np.pow(10, value) for value in datavalues]

    
def get_split_points(min, max, splits):
    """
    Finds n number of even splitting points in the given range.
    
    @param min: The minimum value of the range.
    @type min: float
    @param max: The maximum value of the range.
    @type max: float
    @param splits: The number of splits to be made.
    @type splits: int
    @return: The splitting points.
    """
    return np.linspace(min, max, splits)
    
def progressive_rounding(values) -> list:
    rounded = []
    for v in values:
        magnitude = np.log10(np.abs(v))
        d = None
        
        if magnitude < 1:
            d = 0
        elif magnitude < 2:
            d = 1
        elif magnitude < 4:
            d = 2
        elif magnitude < 7:
            d = 3
        else:
            d = 4
                
        rounded.append(int(v * 10**-d) * 10**d)
        
    return rounded
        