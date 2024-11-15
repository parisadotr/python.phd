# -*- coding: utf-8 -*-
import argparse
import matplotlib.pyplot as plt
from dataproc.bin.loadclass import DataLoader
from dataproc.bin.cutclass import DataProcessor

def entry_point():
    """
    Entry point for the dataproc command-line script.
    """
    # Argument parser for command-line inputs
    parser = argparse.ArgumentParser(description="Run data processing and visualization.")
    parser.add_argument("--file", type=str, required=True, help="Path to the input data file (CSV format).")
    parser.add_argument("--cut_type", type=str, choices=["energy", "q"], required=True, help="Type of cut to perform: 'energy' or 'q'.")
    parser.add_argument("--params", type=str, required=True, help="Parameters for the cut. For energy: 'E_min,E_max,q,minPixel'. For q: 'q_min,q_max,E,minPixel'.")
    parser.add_argument("--output", type=str, default="output_plot.png", help="Path to save the output plot.")
    args = parser.parse_args()
    # Parse parameters
    params = [float(p) if '.' in p else int(p) for p in args.params.split(",")]

    # Load data
    data_loader = DataLoader()
    data = data_loader.load(args.file)

    # Initialize DataProcessor
    processor = DataProcessor(data)
  
    # Perform the cut and plot
    if args.cut_type == "energy":
        x, y = processor.cut_1D_energy(E_min=params[0], E_max=params[1], q=params[2], minPixel=params[3])
        xlabel = "Energy"
    elif args.cut_type == "q":
        x, y = processor.cut_1D_q(q_min=params[0], q_max=params[1], E=params[2], minPixel=params[3])
        xlabel = "q"

    # Plot the results
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"Cut along {xlabel}")
    plt.xlabel(xlabel)
    plt.ylabel("Intensity")
    plt.title(f"Cut along {xlabel}")
    plt.legend()
    plt.grid(True)
    plt.savefig(args.output)
    print(f"Plot saved to {args.output}")
