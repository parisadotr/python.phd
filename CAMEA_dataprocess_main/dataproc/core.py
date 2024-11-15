# Copyright (c) 2024.
# Distributed under the MIT License.

import numpy as np

# Common Utilities
def normalize_data(data):
    """
    Normalizes data to have a maximum value of 1.
    """
    return data / np.max(data)


def gaussian(x, a, x0, sigma):
    """
    Gaussian function.
    """
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))

def calculate_fwhm(sigma):
    """Calculates the FWHM for a Gaussian."""
    return 2 * np.sqrt(2 * np.log(2)) * sigma

# Error Handling
def raise_error(message):
    """Standardized error raising."""
    raise ValueError(f"Error: {message}")
