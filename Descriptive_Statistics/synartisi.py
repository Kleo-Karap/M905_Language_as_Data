# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:47:39 2023

@author: kleop
"""

from scipy.stats import skew

def interpret_skewness(data):
    """
    Returns a string describing the skewness of a distribution.
    """
    skewness = skew(data)
    if -0.5 <= skewness <= 0.5:
        return "The data are fairly symmetrical."
    elif (-1 <= skewness < -0.5) or (0.5 < skewness <= 1):
        return "The data are moderately skewed."
    else:
        return "The data are highly skewed."