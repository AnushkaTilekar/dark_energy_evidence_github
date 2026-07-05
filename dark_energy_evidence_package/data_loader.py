# The program in this file is designed to open the .csv file located at the filepath given by the user as input,
# without reading any of the file contents first just check that the file contains the 3 columns we require to run 
# this package further, namely - the redshift values 'z', the distance modulus values 'mu', 
# and the distance modulus error values 'mu_err', 
# and then pulls only the contents of those 3 columns out into three separate arrays of numbers.
# And then, these three separate arrays of numbers - the redshift values, the distance modulus values,
# and the distance modulus error values - will be readily used for the rest of our package to do fitting/plotting.


# numpy is a Python library for working with arrays of numbers efficiently (much faster than plain Python lists for math). 
# And 'np' is just its universal nickname.
import numpy as np



# 'def' means "define a function" - a reusable block of code. 
# 'load_supernova_data' is the function's name. 
# 'csv_input_filepath' is the function's input parameter 
# - a placeholder name for whatever value someone passes in when they call this function.
def load_supernova_data(csv_input_filepath):
    """
        Load supernova redshift and distance modulus data.

    Expects a .CSV file as input with a header row, 
    and (at minimum) columns named - 
    'z' (i.e. the redhsift),
    'mu' (i.e. the distance modulus), and 
    'mu_err' (i.e. the distance modulus uncertainty).

    - This format is intentionally kept generic enough to be able  
    to accept the real survey catalogues, e.g., DES-SN5YR, Pantheon+, etc.,
    or even the mock/simulated data from any other observatories.

    Args:
        csv_input_filepath (str): Path to the input .CSV data file. 
        -  Not the file's contents yet, just where to find it.

    Returns:
        tuple: (z, mu, mu_err) - three 1-D numpy arrays containing the
            redshift values, distance modulus values, and distance
            modulus uncertainty values, respectively.
    
    Raises:
        ValueError: If the mentioned input file is lacking or missing any of
        the required columns.

    """


    # 'np.genfromtxt()' function reads a text file into a numpy array. Breaking down its three arguments: 
    # (i) 'csv_input_filepath' - the file to read (whatever was passed in)
    # (ii) 'delimiter = ',''  - This tells it values are separated by commas (since it's a .CSV i.e. "comma-separated values")
    # (iii) 'names = True'  - This tells it the first row is a header row (column names), 
    # and to remember those names so you can access columns by name (like parsed_table['z']) instead of by position number
    # We store the result in a variable called 'parsed_table' - this is a table-like numpy array with named columns.
    parsed_table = np.genfromtxt(csv_input_filepath, delimiter=',', names=True)


    # Then we create a "tuple" i.e. a type of unchangeable list) of the three column names which our function absolutely needs to find
    # in order to be able to run this package.
    required_cols = ('z', 'mu', 'mu_err')

    
    # Now here is a compact way of writing a loop in Python. 
    # In plain English we are telling this program: 
    # "Go through each name in the "required_cols" tuple, one at a time (call the current one c), 
    # and keep only the ones that are NOT found in the array called 'parsed_table' 's actual column names." 
    # Ad the "parsed_table.dtype.names" is numpy's way of storing "what are this table's column names" 
    # - so this line is checking each required column against what's actually present in the user given input .csv file,
    # and collecting any essential column names that are missing, into a new list called "missing".
    missing = [c for c in required_cols if c not in parsed_table.dtype.names]



    # Now only if the above mentioned "missing" list has anything in it (i.e., only if it isn't empty), 
    # we tell our program to run this next block of code. -
    # The "raise" is a Python inbuilt keyword that stops our currently runing "load_supernova_data()" function immediately,
    # and reports an error to the user, rather than continuing on with broken/incomplete data. 
    # The "ValueError()" is a built-in Python category of error, meaning "something about the value/input you gave me is wrong."
    # And then gives the user the Error message we have written below.
    if missing:
        raise ValueError(
            f"Error Message: The given input .csv file is missing required column(s): {missing}."
            f"This program expects a .csv file as input having columns: {required_cols} in it."
            "Thank you."
            "Solution: Kindly add the above mentioned columns in the .csv file that you are trying to give as input to this program, and then try again."
            "You can do this. I believe in you."
        )
    
    
    
    # "parsed_table['z']" - pulls out just the column named 'z' from the table.
    # "np.asarray(..., dtype=float)" - makes sure it's a proper numpy array of decimal numbers (not, say, text or some other odd type). 
    # And we do this for all three needed columns, storing each in its own clearly-named variable.
    z = np.asarray(parsed_table['z'], dtype=float)
    mu = np.asarray(parsed_table['mu'], dtype=float)
    mu_err = np.asarray(parsed_table['mu_err'], dtype=float)

    
    # Then we send all three arrays back out to whichever variable or funciton called this "load_supernova_data()" function.
    return z, mu, mu_err

