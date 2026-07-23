# This test file checks that the function named,
# "fit_no_dark_energy_line()", within this package, correctly
# recovers a known straight line's slope and intercept,
# when given some fake, self-generated data points as input,
# for which we already know the correct answer (i.e. output)
# in advance.

# Input : Nothing from external source. This file
#                       is designed to genrate it's own fake data
#                       as input.
# What this file does: This file creates a perfect straight line
#                       with a chosen slope and intercept, runs 
#                       the funciton named "fit_no_dark_energy_line()"
#                       from this package, on it, and checks the
#                       recovered values (or output) matches with
#                       what we already know via physical/mechanical
#                       mathematical calculations.
# Output: pytest rpeorts this test as either "PASSED" or "FAILED".



import numpy as np
from dark_energy_evidence_package.without_dark_energy import fit_no_dark_energy_line


def test_fit_no_dark_energy_line_recovers_correct_slope_and_intercept():
    """
    Check that the line fit correctly finds the exact slope/intercept we used 
    to generate fake data, as we already know the correct answer.
    """

    # Define some input values of our choice as fake/
    # self-generated observation data points.
    true_slope = 5.0
    true_intercept = 10.0

    # Generate redshift values as our fake input dataset
    # (Here, we are considering 
    # max_redshift_for_nearby_fit = 0.1 -- as default)
    z = np.linspace(0.01, 0.09, 20)

    # Generate perfectly clean 'mu' values that lie exactly on 
    # our above chosen line.
    mu = true_slope * z + true_intercept

    # Run the actual function from th epackage that we want to 
    # test on this above generated and defined synthetic data 
    # points.
    recovered_slope, recovered_intercept = fit_no_dark_energy_line(z, mu)

    # Check the recovered values are very close to the true ones.
    # We use np.isclose() rather than exact equality (==),
    # because floating-point math can introduce tiny 
    # rounding erros.
    assert np.isclose(recovered_slope, true_slope)
    assert np.isclose(recovered_intercept, true_intercept)


