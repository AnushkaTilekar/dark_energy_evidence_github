# What this file does: 
# loads our real DES supernova data, fits the "no dark energy" straight line to the nearby ones, and prints out what it found.

# Output of this file: 
# nothing is being saved anywhere - just printed text in our terminal, for us to visually check "did this work correctly?"


from dark_energy_evidence_package.data_loader import load_supernova_data
from dark_energy_evidence_package.without_dark_energy import fit_no_dark_energy_line

z, mu, mu_err = load_supernova_data('downloaded_dataset_files/our_new_custom_DES_SN5yr_dataset.csv')
print(f'From the given input .csv file, Loaded {len(z)} supernovae, with redshfit z range: {z.min():.3f} to {z.max():.3f}')

slope, intercept = fit_no_dark_energy_line(z, mu)

print("Line equation used: mu = slope*z + intercept")
print("Here, for the given input .csv dataset, we have-")
print(f'mu = {slope:.2f}*z + {intercept:.2f}')
print(f"Therefore, for the given input .csv dataset, slope = {slope:.2f} and intercept = {intercept:.2f} ")


