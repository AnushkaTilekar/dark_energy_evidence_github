# In this file we input two arrays of numbers, redhsift 'z' and the distance modulus 'mu' values,
# which we already loaded using the "load_supernova_data()" function in the "data_loader.py" file.
# And alsong with these two parameters, we are also giving one optional number as input parameter,
# called "max_redshift_for_nearby_fit" - defaulting to 0.1, that controls how much "nearby" counts as nearby in our program.
# This "max_redshift_for_nearby_fit" parameter is customisable to each user.
# Then this program picks out only the supernovae close enough to us by selecting redshift values 
# from the initial user input dataset (the .csv file) such that redshift z ≤ max_redshift_for_nearby_fit, 
# and then fits a straight line through just those points.
# Then this fitting gives us two numbers as the output - the "slope", and the "intercept", 
# of that best-fit line. Together, these two numbers fully describe "Hubble's simple law",
# for the initial user input dataset (the .csv file)
# The line equation here is : mu = slope × z + intercept.



# numpy is a Python library for working with arrays of numbers efficiently 
# (much faster than plain Python lists for math). 
# And 'np' is just its universal nickname.
import numpy as np



# "def" - defines a function in Python. 
# "fit_no_dark_energy_line" - is the function's name. 
# "z" and "mu" - are the two required input arrays taken form the initial user input dataset (the .csv file) 
# in the "data_loader.py" file. 
# max_redshift_for_nearby_fit=0.1 is a parameter with a default value - meaning if whoever calls this function doesn't specify a max_redshift_for_nearby_fit,
# it automatically uses 0.1. This is Python's way of making an argument optional.
def fit_no_dark_energy_line(z, mu, max_redshift_for_nearby_fit=0.1):
    """
    Fit a linear (No dark energy existence) relation to the low-redshift data.

    At low redshift, distance modulus 'mu', is approximately linear in redhsift.
    This produces Hubble's original 1929 approach:
    Fit only the nearby supernovae, where the linear approximation holds,
    so it can be extrapolated to compare against more distant data.

    Args:
        z (array): Redshift values.
        mu (array): Distance modulus values.
        max_redshift_for_nearby_fit (float): Only fit data with z <= max_redshift_for_nearby_fit. Default 0.1.
    
    Returns:
        tuple: Pairs in the form of (slope, intercept) - of the best-fit line,
        mu = slope*z + intercept.

    Raises:
        ValueError: If fewer than 2 data points fall below max_redshift_for_nearby_fit.

    """


    
    # Now we place a "z <= max_redshift_for_nearby_fit" condition which doesn't just compare two single numbers
    # - since "z" is a whole array of redshift values, this comparison happens to every value 
    # in the array at once, producing a new array of "True"/"False" values, one for each supernova 
    # - "True" - if that supernova's redshift is small enough to count as "nearby," 
    # - "False" - otherwise. 
    # We call this "True"/"False" array as "is_low_redshift" - becaue we want to indicate that, 
    # it's later used to "is_low_redshift out" (hide/exclude) the values we don't want, 
    # and keeping only the ones marked as "True".
    is_low_redshift = z <= max_redshift_for_nearby_fit

    
    
    
    # Now, since "True" counts as 1, and "False" counts as 0, when we sum them, "np.sum(is_low_redshift)" would count
    # how many supernovae passed the nearby test. 
    # So this checks: "Do we have at least 2 nearby supernovae?"
    # (- Because we need at least 2 points to draw any line at all - one point alone doesn't define a slope.)
    # So we write this logic as -
    if np.sum(is_low_redshift) < 2:
        
        # Now only if the above mentioned condition "np.sum(is_low_redshift) < 2" is true for th euser given data 
        # (i.e., only if there's not enough nearby data to work with.), 
        # we tell our program to run this next block of code. -
        # The "raise" is a Python inbuilt keyword that stops our currently runing "fit_no_dark_energy_line()" function immediately,
        # and reports an error to the user, rather than continuing on with broken/incomplete data. 
        # The "ValueError()" is a built-in Python category of error, meaning "something about the value/input you gave me is wrong."
        # And then gives the user the Error message we have written below.
        raise ValueError(
            f"Error Message: Only {np.sum(is_low_redshift)} data point(s) available in your input .csv file with redhsift z <= {max_redshift_for_nearby_fit};"
            "need at least 2 to fit a line."
            f"Solution: Kindly edit or change your input .csv file to contain at least 2 data ponints with redhsift z <= {max_redshift_for_nearby_fit}. And try again."
            "You can do this. I believe in you."
            f"Kindly also note that, currently you have currently also set max_redshift_for_nearby_fit value used in the condition redshift 'z <= max_redshift_for_nearby_fit' which is used in this package as {max_redshift_for_nearby_fit}."
            "And it's default value in this package code is set to 0.1. If that seems like a mistake, please feel free to change your custom set max_redshift_for_nearby_fit value."
            "You can do this. I believe in you."
        )
    
    

    
    
    # Now this is the actual fitting step. Breaking it down:
    # (i) "z[is_low_redshift]" - uses the "True"/"False" is_low_redshift to select only the redshift values marked as "True" (i.e., only the nearby ones). This is the "masking" action the earlier variable's name "is_low_redshift" refers to.
    # (ii) "mu[is_low_redshift]" - similarly, this uses the "True"/"False" is_low_redshift to select only the nearby distance modulus values.
    # (iii) "np.polyfit(x_values, y_values, deg=1)" - This is numpy's built-in function for fitting a polynomial of a chosen degree to data. 
    # deg=1 specifically means "degree 1," i.e., a straight line (y = mx + b)
    # deg=2 (a parabola) or higher. 
    # Now this returns the two numbers that define that best-fit line.
    # So we immediately unpack the two returned numbers into two clearly named variables, using standard mathematical terms -
    # (i) "slope"-  for "how steep the line is" and 
    # (ii) "intercept" - for "where the line crosses the y-axis" 
    slope, intercept = np.polyfit(z[is_low_redshift], mu[is_low_redshift], deg=1)
    
    
    # Then we send both of these numbers back out to whichever variable or funciton called this "fit_no_dark_energy_line()" function.
    return slope, intercept
