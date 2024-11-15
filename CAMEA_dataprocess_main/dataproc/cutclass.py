# -*- coding: utf-8 -*-
# Copyright (c) 2024.
# Distributed under the MIT License.
import os
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from phus.analysis import formatter

class DataProcessor:
    """
    Processes data: performs cuts along q and energy.

    Parameters:
        data (DataFrame): Input data containing 'Energy', 'q', 'Intensity', and 'PixelCount' columns.

    Methods:
        cut_1D_energy(E_min, E_max, q, minPixel):
            Cuts data along energy values at a fixed q point.

        cut_1D_q(q_min, q_max, E, minPixel):
            Cuts data along q values at a fixed energy.
    """

    def __init__(self, data):
        self.data = data

    def cut_1D_energy(self, E_min, E_max, q, minPixel):

        """  Cuts data along energy values at a fixed q point.  """

        # Filter data based on energy range, fixed q, and minimum pixel count
        cut_data = self.data[(self.data['Energy'] >= E_min) &
                             (self.data['Energy'] <= E_max) &
                             (self.data['q'] == q)].copy()
        cut_data = cut_data[cut_data['PixelCount'] >= minPixel]

        # Extract energy and intensity values
        x = cut_data["Energy"]
        y = cut_data["Intensity"]
        return x, y

    def cut_1D_q(self, q_min, q_max, E, minPixel):

        """ Cuts data along q values at a fixed energy. """

        # Filter data by fixed energy and q range
        cut_data = self.data[(self.data['Energy'] == E) &
                             (self.data['q'] >= q_min) &
                             (self.data['q'] <= q_max)].copy()
        cut_data = cut_data[cut_data['PixelCount'] >= minPixel]

        # Extract q and intensity values
        x = cut_data["q"]
        y = cut_data["Intensity"]
        return x, y
