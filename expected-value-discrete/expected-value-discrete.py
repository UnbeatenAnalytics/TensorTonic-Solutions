import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here,
    if len(x) == len(p):
        prob_sums = np.sum(p)
        tolerance = 1e-6
        if not np.isclose(prob_sums, 1.0, atol=tolerance, rtol=0):
            raise ValueError('Probability Does not sum to 1')
        else:
            return float(np.dot(x,p))
    else:
        raise ValueError('Lengths are not equal.')
