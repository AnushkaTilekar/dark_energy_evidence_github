# This .py file inputs an array of redshift values (z), plus two optional numbers (H0, Om0),
# describing "what recipe of universe" to assume.
# Then, the program mentioned in this file builds a mathematical model of an expanding universe 
# using Python's "astropy" library (or "Package")'s ready-made cosmology tools, then asks that 
# model- "At each of these redshifts, how far away would the supernova with the given redshift 
# value be in the universe from the observer (or telescope) that recorded this redshift value
# for it, according to a universe that includes dark energy?". Then this program file 
# calculates an array of predicted distance modulus values (with units), one for each 
# input redshift value, representing what a universe with dark energy predicts. 
# Further, this program converts these distance modulus 'values with physical units' into 
# 'values without any physical units (i.e. pure numbers)' for convenience, and returns these 
# distance modulus values without any physical units (i.e. pure numbers) as output of this file. 
# This output would then be used in one of the other files within this package, 
# called "graphs.py", to compare against our real data (i.e. the dataset obtained from the 
# user in the data_loader.py file) and the naive straight line (i.e. plotted line obtained on 
# our data by the absence of dark energy) - which is calculated in the file "without_dark_energy.py" 
# in this package.



# NOTE: We are not actually currently going to use the Python's numpy module directly anywhere 
# in this file's code. We have iported it here only for the purpose of the docstring's math 
# explanations. Although this import is currently unnecessary/unused, Author have kept here for now
# due plans to use it later in later code expansions and file updates. But if the user wants, they
# can remove this code line for now.
import numpy as np



# This line imports Python's "astropy" library's (or "Package's") "FlatLambdaCDM" class of the 
# "cosmology" module (or "subpackage"). 
# astropy's cosmology-->FlatLambdaCDM is a ready-made mathematical model representing exactly the 
# kind of universe we want to discuss in this package - flat (not curved), and containing-
# (i) matter (baryonic),  
# (ii) "CDM" meaning "cold dark matter", and
# (iii) a cosmological constant style dark energy (represented by the Greek letter Λ ("Lambda").
# Astropy already has done a wonderful job building and testing this specific kind of universe's 
# model, the specific kind that we want and move ahead with. 
# Now, in our package, we are going to plug-in our specific required parameters into this model 
# constructed by the astropy's cosmology-->FlatLambdaCDM class, to manipulate the template model 
# provided by astropy's cosmology-->FlatLambdaCDM class further, so as to test it for our specific
# requirements.
from astropy.cosmology import FlatLambdaCDM




# "def" - defines a function in Python. 
# "predict_distance_modulus_with_dark_energy_presence" - is the function's name. 
# "z", "H0", and "Om0" - are the three required inputs.
# The "z" array is taken form the initial user input dataset (the .csv file) in the "data_loader.py" file. 
# "H0=67.66" and "Om0=0.3096" are parameters with a default value - meaning if whoever calls this 
# function, doesn't specify a Hubble constant (H0) value and Total Matter Fraction  in the universe
# (Om0) value, this function automatically uses 67.66 and 0.3096 as their respective values.
# This is Python's way of making an argument optional for the user.
def predict_distance_modulus_with_dark_energy_presence(z, H0=67.66, Om0=0.3096):
    """
    Predict the distance modulus assuming a universe containing dark energy.

    Uses astropy's built-in FlatLambdaCDM cosmology model to compute the distane
    modulus expected at each input redshift, for a flat universe containing matter 
    (ordinary + dark) and dark energy, with an expansion rate set by H0.
    This model assumes dark energy behaves as a cosmological constant 
    (with the equation of state parameter for dark energy being defined here as w=-1),
    which is consistent with the Lambda-CDM picture.

    NOTE: Om0 here represents the "total" matter density, including both- ordinary
    (i.e. baryonic) matter, and dark matter, combined. these two are not separated here 
    in the Friedmann Equations because, they affect the expansion history of the universe
    universe identically by the mathematics of the above considered assumptions.
    The remaining density  of the universe, i.e. (1-Om0), is assumed to be dark energy here,
    since a flat universe requires all density components to sum to 1.

    The default values here are derived from the same cosmological parameters
    used in this author's other CAMB-based project:
    (i) H0 = 67.66,
    (ii) ombh2 = 0.02242,
    (iii) omch2 = 0.11933.
    Converting these values to fractional densities (i.e. dividing by h^2, where
    h = H0/100) would give us:
    Om0 = (ombh2 + omch2) / h^2 ~= 0.3096.

    Args:
        z (array): Redshift values at which we want to compute predictions.
        H0 (float): Hubble constant, in km/s/Mpc. Default is 67.66.
        Om0 (float): Present-day total matter density fraction (0 to 1), 
            including both ordinary (baryonic) and dark matter. Default 0.3096.

    Returns:
        array: Predicted distance modulus at each given input redshift value. 

    """





    # This line constructs an actual cosmology model as an "object" - for our convenience to be 
    # easy to call and reuse later. 
    # This line is "building a specific, complete recipe for a universe" using our chosen H0 and 
    # Om0 values, and stores that whole ready-to-use recipe in a variable called, 
    # "our_custom_cosmology_model".
    our_custom_cosmology_model = FlatLambdaCDM(H0=H0, Om0=Om0)




    
    # Python's "astropy" library, has a built-in method called, "distmod()", in its cosmology 
    # module's (i.e. "subpackage's") "FlatLambdaCDM" class.
    # The "distmod(z)" function tells our cosmology model, currently called, 
    # "our_custom_cosmology_model", to calculate the distance modulus at each specified 
    # redshift value 'z' form the input redshift array. Remember, the redshift 'z' array being 
    # used here is take from the user's input dataset in the data_loader.py file.
    # Now, astropy is very careful about tracking physical units like "this number is in 
    # magnitudes", etc.
    # Here, astropy stores the result of calculated distance magnitude in units of "--". 
    # Hence, we store it in the variable called "predicted_mu_with_units".
    # Numbers stored with units, this is useful for us further in the package while creating and 
    # displaying plots, in the file "graphs.py" to be precise, and also for keeping a check on 
    # dimensional correctness in our mathematical calculations.
    # Here,
    # mu => "distance modulus"
    predicted_mu_with_units = our_custom_cosmology_model.distmod(z)


    # But also, further in the package, in our calculations, we would need to use these obtained 
    # distance modulus numbers without their units - i.e. in pure number form - for some 
    # mathematical procedures.
    # Hence, we now we use "value()" function, which is a built-in function of the Python's 
    # astropy library.
    # This .value at the end strips away the extra unit-tracking information which astropy had 
    # attached internally above leaving us with plain numbers for the obtained distance modulus 
    # values for each given redshift value.
    # Here,
    # mu => "distance modulus"
    predicted_mu_without_units = predicted_mu_with_units.value


    

    # This line sends the above obtained array of predicted distance modulus values (as pure numbers)
    # back out to whichever variable or funciton called this 
    # "predict_distance_modulus_with_dark_energy()" function.
    # Here,
    # mu => "distance modulus"
    return predicted_mu_without_units



# -----------------------------------------------------------------------------------------------------

# Kindly NOTE :-
# In this file, dark matter isn't "missing"- it's already inside Om0. 
# In the standard ΛCDM model(and in astropy's FlatLambdaCDM), 
# Om0 represents total matter density - dark matter and ordinary (baryonic) matter combined, 
# not just ordinary matter alone. 
# This is for a specific physical reason: for the purposes of how the universe's expansion evolves 
# over time, dark matter and ordinary matter behave identically (both are "pressureless," meaning 
# their density just dilutes as the universe expands, following the same mathematical rule). 
# Since they affect the expansion history in exactly the same way, the standard Friedmann equations 
# (and therefore astropy) don't need to track them as two separate terms - they're combined into 
# one Om0 in the astropy's FlatLambdaCDM.
# So in FlatLambdaCDM(H0, Om0):
# Om0 = dark matter + ordinary matter, combined 
# (typically ≈0.3, of which the ordinary/baryonic piece is only about 0.05 
# and dark matter is the other ≈0.25 
# - but the code here is made unaware of that split).
# The remaining (1 - Om0) = dark energy 
# (since the model assumes a flat universe, these two must add to 1).
# This means here, dark matter isn't neglected, it's baked into Om0 by definition. 
# Thus, in this code, "Om0 includes both ordinary matter and dark matter, along with dark energy".
# And, FlatLambdaCDM in astropy already assumes w = -1 internally 
# - it's baked into the model choice, not a separate parameter that user needs to set.