#!/usr/bin/python3
""" Function: find_peak """


def find_peak(ls):
    """
    This function finds a peak element in a given list of numbers.
    A peak element is an element that is greater than its adjacent elements.
    Args:
    - ls: a list of numbers
    Returns:
    - the peak element, if one exists, otherwise None
    """
    if not ls:
        return None
    left = 0
    right = len(ls) - 1
    while left < right:
        mid = (left + right) // 2
        if ls[mid] < ls[mid+1]:
            left = mid + 1
        else:
            right = mid
    return ls[left]
