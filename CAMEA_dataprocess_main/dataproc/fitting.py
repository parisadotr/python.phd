
# Copyright (c) 2024.
# Distributed under the MIT License.
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from dataproc.core import calculate_fwhm, gaussian


def gaussian(x, a, x0, sigma):
    """
    Gaussian function.

    Parameters:
        x (array): Independent variable.
        a (float): Amplitude.
        x0 (float): Center of peak.
        sigma (float): Standard deviation.
    """
    return a * np.exp(-(x - x0) ** 2 / (2 * sigma ** 2))


def fit_gaussian(x, y):
    """
    Fits a Gaussian function to the given data and prints FWHM and its error.
    
    """
    # Initial guess for fitting parameters: amplitude, peak position, and sigma
    amplitude_guess = np.max(y)
    peak_position_guess = x[np.argmax(y)]
    sigma_guess = (x[-1] - x[0]) / 10  # Approximate guess for width

    p0 = [amplitude_guess, peak_position_guess, sigma_guess]

    # Perform the Gaussian fit
    popt, pcov = curve_fit(gaussian, x, y, p0=p0)

    # Extract fitted parameters and their errors
    a, x0, sigma = popt
    perr = np.sqrt(np.diag(pcov))  # Parameter errors

    # Calculate FWHM and its error
    FWHM = calculate_fwhm(sigma)
    FWHM_error = 2 * np.sqrt(2 * np.log(2)) * perr[2]

    # Print results
    print("Fitted Gaussian parameters:")
    print(f"  Amplitude (a): {a:.3f}")
    print(f"  Peak position (x0): {x0:.3f}")
    print(f"  Standard deviation (sigma): {sigma:.3f}")
    print(f"FWHM: {FWHM:.3f} ± {FWHM_error:.3f}")

    return popt, FWHM, FWHM_error

    



# Example usage
if __name__ == "__main__":
    # Generate example data
    x = np.linspace(-10, 10, 100)
    y = gaussian(x, a=10, x0=2, sigma=3) + np.random.normal(0, 0.5, size=x.size)
# Fit Gaussian and calculate FWHM
    popt, FWHM, FWHM_error = fit_gaussian(x, y)

    # Plot the data and the fitted Gaussian
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, label="Data", color="blue", s=10)
    plt.plot(x, gaussian(x, *popt), label="Fitted Gaussian", color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Gaussian Fit")
    plt.show()
