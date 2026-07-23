import numpy as np

from dark_energy_evidence_package.data_loader import load_supernova_data
from dark_energy_evidence_package.without_dark_energy import fit_no_dark_energy_line
from dark_energy_evidence_package.with_dark_energy import predict_distance_modulus_with_dark_energy_presence
from dark_energy_evidence_package.graphs import plot_hubble_diagram, plot_residuals

z, mu, mu_err = load_supernova_data('downloaded_dataset_files/our_new_custom_DES_SN5yr_dataset.csv')

slope, intercept = fit_no_dark_energy_line(z, mu)

z_grid = np.linspace(z.min(), z.max(), len(z))

dark_energy_mu = predict_distance_modulus_with_dark_energy_presence(z_grid)

plot_hubble_diagram(z, mu, slope, intercept, z_grid, dark_energy_mu, save_path="testing_day2_hubble_diagram.png")
plot_residuals(z, mu, slope, intercept, save_path="testing_day2_residuals.png")

print("Done. Succesfully produced and saved testing_day2_hubble_diagram.png and testing_day2_residuals.png")

import matplotlib.pyplot as plt
plt.show()



