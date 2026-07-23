# This test runs this package's all contents 
# (or in fancy words, A.K.A. "full pipeline"), on the real,
# included DES supernova dataset, and checks that every step
# completes without crashing and is producing non-broken 
# output values.

# Input: The real dES dataset lready included in the folder 
#           called "downloaded_dataset_files/" within this
#           github repository.
# What this file does: This file first loads this input data,
#                       fits the no-dark-energy-line to it,
#                       then computes the WITH-dark-energy 
#                       model prediction for this data, and
#                       in the obtained calculated prediction
#                       output checks that nothing is "NaN" or
#                       "infinite" or "obviously wrong in 
#                       scinetific sense".
# Output: pytest reports this test as either "PASSED" or "FAILED".

import numpy as np

from dark_energy_evidence_package.data_loader import load_supernova_data
from dark_energy_evidence_package.without_dark_energy import fit_no_dark_energy_line
from dark_energy_evidence_package.with_dark_energy import predict_distance_modulus_with_dark_energy_presence

# The following mentioned dataset is explicitly used to test this version of this package,
# unless the user explictly mentions some other dataset and it's location.
DEFAULT_TEST_DATASET_PATH = 'downloaded_dataset_files/our_new_custom_DES_SN5yr_dataset.csv'


def test_full_pipeline_runs_on_real_data_without_crashing():
    """
    Load real supernova data, fit the no-dark-energy line on 
    this data, and also predict the WITH-dark-energy-Model for 
    this data
    -- checking at each of these 3 steps that the program 
    completes successfully without crashes and gives out 
    sensible results i.e., results that are not NaN/infinite 
    values, at each of these 3 steps.

    By default, this program currently runs on the real 
    DES-SN5YR dataset included in the github repository of 
    this package 
    (a file named "our_new_custom_DES_SN5yr_dataset.csv" 
    which is located at the folder location: 
    "dark_energy_evidence_github/downloaded_dataset_files/").
    However, if user would like to run this test program by 
    using a different dataset, they can easily do so by simply 
    changing the DEFAULT_TEST_DATASET_PATH variable defined 
    just above this function, in which they can explicitly 
    menition the name and the path to the dataset that they 
    would like to test this file for.
    """

    z, mu, mu_err = load_supernova_data(DEFAULT_TEST_DATASET_PATH)
    print(f"Loaded {len(z)} supernovae form the dataset located at: {DEFAULT_TEST_DATASET_PATH}")

    # check the data loaded is not empty and has mathcing lengths
    assert len(z) > 0
    assert len (z) == len(mu) == len(mu_err)
    print("Confirmed: 'z', 'mu', and 'mu_err', all have matching lengths.")

    slope, intercept = fit_no_dark_energy_line(z, mu)
    print(f"Fitted the no-dark-energy line on the real data, found: slope={slope:.2f}, intercept={intercept:.2f}")

    # Check the fit produced real, finite numbers -- not NaN or infinity
    assert np.isfinite(slope)
    assert np.isfinite(intercept)
    print("Confirmed: The calcualted Slope and the Intercept after fitting the np-dark-energy-line on the real dataset, are Real, and Finite numbers.")

    z_grid = np.linspace(z.min(), z.max(), len(z))
    predicted_mu_with_dark_energy = predict_distance_modulus_with_dark_energy_presence(z_grid)

    # Check every predicted value is finite, and the array is the coorect length (one prediction per z_grid point)
    assert np.all(np.isfinite(predicted_mu_with_dark_energy))
    assert len(predicted_mu_with_dark_energy) == len(z_grid)






