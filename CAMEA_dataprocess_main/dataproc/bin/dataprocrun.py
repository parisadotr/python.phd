# Copyright (c) 2024.
# Distributed under the MIT License.

import matplotlib.pyplot as plt
from dataproc.loadclass import DataLoader
from dataproc.cutclass import DataProcessor
from dataproc.fitting import fit_gaussian

def entry_point():
    """
    Asks the user for parameters to perform an energy cut.
    """
    # Ask the user for the type of cut
    print("Welcome to the CAMEA Data Cutting Script!")
    cut_type = input("What type of cutting do you need? (energy): ").strip().lower()

    # Collect parameters for the energy cut
    file_path = input("Enter the path to the data file (CSV format): ").strip()
    try:
        E_min = float(input("Enter the minimum energy (E_min): ").strip())
        E_max = float(input("Enter the maximum energy (E_max): ").strip())
        q_value = float(input("Enter the fixed q value: ").strip())
        min_pixel = int(input("Enter the minimum pixel count (minPixel): ").strip())
    except ValueError:
        print("Invalid input.")
        return

    # Perform the energy cut
    try:
        data_loader = DataLoader()
        data = data_loader.load(file_path)

        processor = DataProcessor(data)
        x, y = processor.cut_1D_energy(E_min=E_min, E_max=E_max, q=q_value, minPixel=min_pixel)

        # Plot the results
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, label="Cut along Energy")
        plt.xlabel("Energy")
        plt.ylabel("Intensity")
        plt.title("Energy Cut")
        plt.legend()
        plt.grid(True)
    except Exception as e:
        print("An error occurred")


if __name__ == "__main__":
    entry_point()


def run_fitting(x, y):
    popt, FWHM, FWHM_error = fit_gaussian(x, y)
    print(f"FWHM: {FWHM}, Error: {FWHM_error}")
    return popt

