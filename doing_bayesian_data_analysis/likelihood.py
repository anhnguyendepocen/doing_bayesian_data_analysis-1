"""
Likelihood functions.
"""


def bernoulli_likelihood(theta, flips, heads):
    """
    Likelihood function based on Bernoulli distribution.

    Parameters
    ----------
    theta : float
        Probability of heads.
    flips : int
        Number of flips.
    heads : int
        Number of heads.

    Returns
    -------
    float
        Likelihood value.
    """
    return theta ** heads * (1 - theta) ** (flips - heads)
