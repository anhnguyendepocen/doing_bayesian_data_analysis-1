"""
Functions for highest density interval (HDI) calculation.
"""
import numpy as np
import sklearn
from pymc3.stats import hpd


def calc_hdi(hist, bins, size, random_state=None):
    """
    Estimate HDI from histogram of probability.

    Data is sampled with the given probability and
    HDI is calculated with pymc3.stats.hpd

    Parameters
    ----------
    hist : list of float
        Histogram of probability.
    bins : list of float
        Bins of the histogram.
    size : int
        Number of samples to generate.
    random_state : int, RandomState instance or None, optional (default=None)
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used
        by `np.random`.

    Returns
    -------
    hdi_x : [float, float]
        HDI range.
    hdi_y : float
        Probability value corresponding to the HDI.
    """
    rng = sklearn.utils.check_random_state(random_state)
    samples = rng.choice(bins, size=size, p=hist)
    hdi_x = [float(x + np.diff(bins[:2])) for x in hpd(samples)]
    hdi_y = np.mean([
        hist[np.argwhere(np.abs(bins - x) < 1e-6).ravel()[0] + 1]
        for x in hdi_x
    ])
    return hdi_x, hdi_y
