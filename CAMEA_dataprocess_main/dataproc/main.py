# Copyright (c) 2024.
# Distributed under the MIT License.

import argparse
from dataproc.loadclass import DataLoader
from dataproc.cutclass import DataProcessor
from dataproc.fitting import fit_gaussian, gaussian
from dataproc.visualization import visualize_results


def main():

    parser = argparse.ArgumentParser(description="Run data processing and fitting.")
    parser.add_argument("--file", type=str, required=True, help="Path to the input data file.")
    #parser.add_argument("--E_min", type=float, required=True, help="Minimum energy for the cut.")
    #parser.add_argument("--E_max", type=float, required=True, help="Maximum energy for the cut.")
    #parser.add_argument("--q", type=float, required=True, help="Momentum transfer (q) for the cut.")
    #parser.add_argument("--min_pixel", type=int, required=True, help="Minimum pixel count.")
    args = parser.parse_args() # ho to use in terminal:python main.py --file "data2.csv" --E_min 5 --E_max 10 --q 0.2 --min_pixel 20

    # Load data
    data_loader = DataLoader()
    data = data_loader.load(args.file)

    # Process and fit data
    processor = DataProcessor(data)
    x, y = processor.cut_1D_energy(args.E_min, args.E_max, args.q, args.min_pixel)

    # Perform Gaussian fitting
    popt, FWHM, FWHM_error = fit_gaussian(x, y)

    # Visualize results interactively
    if popt is not None:
        visualize_results(x, y, popt)
    else:
        print("Fitting failed. No visualization will be displayed.")


if __name__ == "__main__":
    main()

