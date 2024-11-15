# Copyright (c) 2024.
# Distributed under the MIT License.
import matplotlib.pyplot as plt

def plot_raw_data(x, y):
    """
    Plots the raw data.

        """
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color="blue", s=10, label="Raw Data")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Raw Data")

def plot_fitted_data(x, y, popt, fit_function):
    """
    Plots the data with the fitted curve.
       
        popt (array): Optimized parameters from the fitting function.
        fit_function (callable): The function used for fitting.
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color="blue", s=10, label="Data")
    plt.plot(x, fit_function(x, *popt), color="red", label="Fitted Curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Data with Fitted Curve")
 
 def visualize_results(x, y, popt):
    """
    Visualizes the raw data, fitted curve, and residuals.

    """
    plot_raw_data(x, y)
    plot_fitted_data(x, y, popt, gaussian)
    
 

