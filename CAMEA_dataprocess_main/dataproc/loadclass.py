# Copyright (c) 2024.
# Distributed under the MIT License.
import os
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter
from phus.analysis import formatter

class DataLoader:
    """
    Handles data file management: path generation and conversion.
    """
    def __init__(self, folder, year=None, format=None, instrument=None):
        self.folder = folder
        self.year = year
        self.format = format or (formatter.input.get(instrument.lower(), None) if instrument else None)
        self.instrument = instrument
        self.dataFiles = []
        self.convertedFiles = []

        if instrument and not self.format:
            raise AttributeError(f'Instrument "{instrument}" not recognized.')

    def generate_file_list(self, numberString):
        for part in numberString.split(','):
            if '-' in part:
                start, end = map(int, part.split('-'))
                numbers = range(start, end + 1)
            else:
                numbers = [int(part)]
            if self.year and self.format:
                self.dataFiles.extend(
                    os.path.join(self.folder, self.format.format(self.year, num)) for num in numbers
                )
        return self.dataFiles

    def convert_files(self, saveLocation=None, saveFile=False, deleteOnConvert=True):
        for file in self.dataFiles:
            converted = f"{os.path.splitext(file)[0]}_converted.nxs"
            if saveFile:
                save_path = saveLocation or os.path.dirname(file)
                converted = os.path.join(save_path, os.path.basename(converted))
                with open(converted, 'w') as f:
                    f.write("Converted data")

            self.convertedFiles.append(converted)
            if deleteOnConvert:
                try:
                    os.remove(file)
                except FileNotFoundError:
                    print(f"Warning: {file} not found.")
        return self.convertedFiles



