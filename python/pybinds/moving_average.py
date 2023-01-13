from typing import List


def python_moving_average(v: List[float], window: int) -> List[float]:
    """Moving average implemented in python

    with a given window calculate the average of the window and append it
    This function slides over the list

    Args:
        v: list of floats
        window: size of window

    Returns:
        moving average of v
    """
    moving_average = list()
    for i in range((len(v) - window + 1)):
        slice = sum(v[i : (i + window)])
        slice_average = slice / window
        moving_average.append(slice_average)

    return moving_average
