# This graphs.py file takes the numbers/arrays already computed elsewhere in this package, i,e, 
# the z, mu from real data; slope, intercept from the no-dark-energy fit; 
# z_grid, predicted_mu_with_dark_energy from the dark-energy model, and plus a filename to save to, as Input.

# Then, this graphs.py file draws two kinds of graphs using a Python plotting library called "matplotlib", 
# and saves each graph as an .png image file on the user's machine's local disk, 
# while also trying to show it on-screen interactively for the user,
# and also prints to the terminal the location of this saved .png file, 
# telling the user where to find it.



import matplotlib.pyplot as plt

# To access matplotlib.get_backend()
import matplotlib

import os




# -----------------------------------------------------------------------------------------
# Function-1 :

def plot_hubble_diagram(z, mu, slope, intercept, z_grid, predicted_mu_with_dark_energy, save_path="hubble_diagram.png", figure_size=(8, 6), point_size=5, point_transparency=0.4, label_fontsize=12, title_fontsize=14, legend_fontsize=13):
    """
    Plot the real supernova data received from the user against the 
    "Without dark energy" Model, and "With dark energy" Model.

    Displays the plot interactively, and also automatically saves a copy to local machine folder.
    The path of the saved plot file is printed to the console so the user knows where to locate 
    it on their machine.

    Input: real redshift/distance-modulus data, the fitted line's slope and intercept, a smooth grid of redshift values, and the dark-energy model's predicted distance modulus at each grid point.

    Args:
        z (array): Redshift values from the real data obtained from the user.
        mu (array): Distance modulus values from the real dataset obtained from the user.
        slope (float): Slope of the "Without dark energy Model" line.
        intercept (float): The intercept obtained from calculations for the "Without dark energy Model" line.
        z_grid (array): z_grid is a set of evenly-spaced redshift values spanning from the lowest to highest redshift in the user provided dataset. It exists purely so the two model curves (straight line and ΛCDM) can be drawn as smooth continuous lines across the whole plot, rather than only at the exact redshifts of user's real supernovae dataset.
        predicted_mu_with_dark_energy (array): The distance modulus that the "With-dark-energy Model" predicts at each redshift value in z_grid. This is what gets drawn as the blue curve.
        save_path (str, optional): Defined by user, decides where to save the generated plot image file on the user's machine. Default is "hubble_diagram.png" in the user's current working directory.

    Processing: Plots all three as an overlay on one chart, saves the result as an image file, and attempts to display it on-screen.

    Output: Nothing is returned. A .png image file is saved to save_path, and a confirmation message is printed to the console.
    
    """

    plt.figure(figsize=figure_size)


    # s = controls the size of each plotted dot (in points²). Larger number = bigger dots. With ~1,800 supernovae, small dots (like s=5) avoid the plot turning into an unreadable solid blob.
    # alpha = controls transparency, from 0 (fully invisible) to 1 (fully solid). A value like 0.4 makes overlapping points show as darker patches, which helps you visually see where data is dense versus sparse — useful with lots of points sitting close together.
    plt.scatter(z, mu, s=point_size, alpha=point_transparency, label="Real supernova dataset provided by user")

    Without_dark_energy_Model_line = slope*z_grid + intercept

    plt.plot(z_grid, Without_dark_energy_Model_line, color='red', label='Without dark energy Model (Straight Line)')
    plt.plot(z_grid, predicted_mu_with_dark_energy, color='blue', label="With dark energy Model (ΛCDM)")

    plt.xlabel("Redshift (z)", fontsize=label_fontsize)
    plt.ylabel("Distance modulus (mu)", fontsize=label_fontsize)
    plt.title("Hubble Diagram for the user provided dataset: \n Evidence for Dark Energy in the user provided dataset", fontsize=title_fontsize)
    plt.legend(fontsize=legend_fontsize)

    # Save the calculated plot figure first (always)
    abs_save_path = os.path.abspath(save_path)

    # dpi ("dots per inch") = controls the image's resolution/sharpness. Higher = crisper image, but larger file size. 150 is a reasonable middle ground; 300 is common for print-quality/publication figures.
    # bbox_inches="tight" = tells matplotlib to trim excess blank space around the edges of the saved image, so labels/titles don't get awkwardly cut off or leave huge empty margins.
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    
    print(f"✅ The Hubble Diagram calculated for your provided dataset is now saved at location: {abs_save_path}")

    # Then display this calculated Hubble diagram image for the user provided dataset to the user,
    # while also taking into account the possibility of fallback in case of headless environments on the user machine:
    # Now, because plt.show() doesn't reliably raise an exception in headless environments,
    # If there is no GUI available on the user's machine, inform the user:
    # 'agg' is the non-interactive backend used in headless environments
    if matplotlib.get_backend().lower() == 'agg':
        print(f"ℹ️ Kindly note, the calculated Hubble plot image for your provided dataset cannot be displayed in this current environment as the Plot Display is not available in this environment. But please do not worry. This calculated Hubble Plot image file for your provided dataset is now automatically saved on your this machine at this location: {abs_save_path} ")
        print("😄 Congratulations once again for your success on this project so far! Keep going. I am confident that you can soon take this project to your desired completion stage. I believe in you. 😄👍💯🏆✨")
        # Close the figure to free memory
        plt.close()    

    # Displays the plot only if an interactive backend is available.
    else:
        print("🎉🥳Yayy! You did it! Congratulations on your progress in this project so far. Here is the calculated Hubble Diagram plot file for your given dataset-")
        plt.show(block=False)
        plt.pause(0.5)
        print("🏆 I am confident that you can soon take this project to your desired completion stage. I believe in you. Congratulations once again 😄👍👍✨💯 💯")






# -----------------------------------------------------------------------------------------
# Function-2 :

def plot_residuals(z, mu, slope, intercept, save_path="residuals.png", figure_size=(8, 6), point_size=5, point_transparency=0.4, label_fontsize=12, title_fontsize=14, legend_fontsize=13):
    """
    Plot how far the real dataset deviates from the "Without dark energy Model" prediction.

    Displays the plot interactively, and also automatically saves a copy to local machine folder.
    The path of the saved plot file is printed to the console so the user knows where to locate 
    it on their machine.

    Input: real redshift/distance-modulus data, the fitted line's slope and intercept, a smooth grid of redshift values, and the dark-energy model's predicted distance modulus at each grid point.

    Args:
        z (array): Redshift values from the real data obtained from the user.
        mu (array): Distance modulus values from the real dataset obtained from the user.
        slope (float): Slope of the "Without dark energy Model" line.
        intercept (float): The intercept obtained from calculations for the "Without dark energy Model" line.
        save_path (str, optional): Defined by user, decides where to save the generated plot image file on the user's machine. Default is "residuals.png" in the user's current working directory.
    

    Processing: Plots all three as an overlay on one chart, saves the result as an image file, and attempts to display it on-screen.

    Output: Nothing is returned. A .png image file is saved to save_path, and a confirmation message is printed to the console.
    
    """

    Without_dark_energy_Model_prediction = slope*z + intercept

    # Here, "mu" is simply the real, measured data from user provided dataset - it has nothing to do with "the With-dark-energy-Model."
    residuals = mu - Without_dark_energy_Model_prediction

    plt.figure(figsize=figure_size)
    plt.scatter(z, residuals, s=point_size, alpha=point_transparency, label="Residuals \n [= (Real data from user provided dataset) \n - (Predicted data of Without-dark-energy-Model)]")

    # Zero Residuals Line (Indicating the residuals if the user provided dataset would have perfectly matched to Without-dark-energy-Model)
    plt.axhline(0, color='gray', linestyle='-', label="'Without-dark-energy' Model \n (Flattened to zero in this residual space \n because subtracted from itself)")

    plt.xlabel("Redshift(z)", fontsize=label_fontsize)
    plt.ylabel("Residuals \n [= (Real mu from user provided dataset) \n - (Without dark energy Model prediction)]", fontsize=label_fontsize)
    plt.title("Residuals: \n Indicating how much the user provided Real Dataset deviates \n from the 'Without-dark-energy' Model", fontsize=title_fontsize)
    plt.legend(fontsize=legend_fontsize)
    
    # Save the calculated plot figure first (always)
    abs_save_path = os.path.abspath(save_path)

    # dpi ("dots per inch") = controls the image's resolution/sharpness. Higher = crisper image, but larger file size. 150 is a reasonable middle ground; 300 is common for print-quality/publication figures.
    # bbox_inches="tight" = tells matplotlib to trim excess blank space around the edges of the saved image, so labels/titles don't get awkwardly cut off or leave huge empty margins.
    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    
    print(f"✅ The Residuals plot calculated for your provided dataset is now saved at location: {abs_save_path}")

    # Then display this calculated Residuals plot image for the user provided dataset to the user,
    # while also taking into account the possibility of fallback in case of headless environments on the user machine:
    # Now because plt.show() doesn't reliably raise an exception in headless environments,
    # If there is no GUI available on the user's machine, inform the user:
    # 'agg' is the non-interactive backend used in headless environments
    if matplotlib.get_backend().lower() == 'agg':
        print(f"ℹ️ Kindly note, the calculated Residuals plot image for your provided dataset cannot be displayed in this current environment as the Plot Display is not available in this environment. But please do not worry. This calculated Hubble Plot image file for your provided dataset is now automatically saved on your this machine at this location: {abs_save_path} ")
        print("😄 Congratulations once again for your success on this project so far! Keep going. I am confident that you can soon take this project to your desired completion stage. I believe in you. 😄👍💯🏆✨")
        # Close the figure to free memory
        plt.close()

    # Displays the plot only if an interactive backend is available
    else:
        print("🎉🥳Yayy! You did it! Congratulations on your progress in this project so far. Here is the calculated Residuals plot file for your given dataset-")
        plt.show(block=False)
        plt.pause(0.5)
        print("🏆 I am confident that you can soon take this project to your desired completion stage. I believe in you. Congratulations once again 😄👍👍✨💯 💯")
    


