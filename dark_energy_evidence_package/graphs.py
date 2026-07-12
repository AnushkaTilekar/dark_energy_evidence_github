import matplotlib.pyplot as plt
import os




# -----------------------------------------------------------------------------------------
# Function-1 :

def plot_hubble_diagram(z, mu, slope, intercept, z_grid, dark_energy_mu, save_path="hubble_diagram.png"):
    """
    Plot the real supernova data received from the user against the 
    No dark energy model, and With dark energy model.

    Displays the plot interactively, and also automatically saves a copy to local machine folder.
    The path of the saved plot file is printed to the console so the user knows where to locate 
    it on their machine.

    Args:
        z (array): Redshift values from the real data obtained from the user.
        mu (array): Distance modulus values from the real dataset obained from the user.
        slope (float): Slope of the "Without dark energy Model" line.
        intercept (float): The intercept obtained from calculations for the "Without dark energy Model" line.
        z-grid (array): A smooth range of redshift values, used to draw both model curves across the full plot.
        dark_energy_mu (array): Predicted distance modulus (form the With dark energy model) at each value in z_grid.
        save_path (str, optional): Defined by user, decides where to save the generated plot image file on the user's machine. Default is "hubble_diagram.png" in the user's current working directory.
    
    """

    plt.figure(figsize=(8,6))
    plt.scatter(z, mu, s=5, alpha=0.4, label="Real supernova dataset provided by user")

    Without_dark_energy_Model_line = slope*z_grid + intercept

    plt.plot(z_grid, Without_dark_energy_Model_line, color='red', label='No dark energy Model (Straight Line)')
    plt.plot(z_grid, dark_energy_mu, color='blue', label="With dark energy Model (ΛCDM)")

    plt.xlabel("Redshift (z)")
    plt.ylabel("Distance modulus (mu)")
    plt.title("Hubble Diagram for the user provided dataset: Evidence for Dark Energy in the user provided dataset")
    plt.legend()

    # Save the calculated plot figure first (always)
    abs_save_path = os.path.abspath(save_path)
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print(f"✅ The Hubble Diagram calculated for your provided dataset is now saved at location: {abs_save_path}")

    # Then display this calculated Hubble diagram image for the user provided dataset to the user,
    # while also taking into account the possibility of fallback in case of headless environments on the user machine:
    try:
        print("🎉🥳Yayy! You did it! Congratulation on your progress in this project so far. Here is the calcualted Hubble Diagram plot file for your given dataset-")
        plt.show()
        print("🏆 I am confident that you can soon take this project to your desired completion stage. I believe in you. Congratulations once again 😄👍👍✨💯 💯")
    except Exception:
        # If there is no GUI available on the user's machine, inform the user:
        print(f"ℹ️ Kindly note, the calculated Hubble plot image for your provided dataset cannot be displayed in this current environment as the Plot Display is not available in this environment. But please do not worry. This calcualted Hubble Plot image file for your provided dataset is now automatically saved on your this machine ath this location: {abs_save_path} ")
        print("😄 Congratulations once again for your success on this project so far! Keep going. I am confident that you can soon take this project to your desired completion stage. I believe in you. 😄👍💯🏆✨")

    # Close the figure to free memory
    plt.close()



# -----------------------------------------------------------------------------------------
# Function-2 :

def plot_residuals(z, mu, slope, intercept, save_path="residuals.png"):
    """
    Plot how far the real dataset deviates from the "Without dark energy Model" prdiction.

    Displays the plot interactively, and also automatically saves a copy to local machine folder.
    The path of the saved plot file is printed to the console so the user knows where to locate 
    it on their machine.

    Args:
        z (array): Redshift values from the real data obtained from the user.
        mu (array): Distance modulus values from the real dataset obained from the user.
        slope (float): Slope of the "Without dark energy Model" line.
        intercept (float): The intercept obtained from calculations for the "Without dark energy Model" line.
        save_path (str, optional): Defined by user, decides where to save the generated plot image file on the user's machine. Default is "residuals.png" in the user's current working directory.
    
    """

    Without_dark_energy_Model_prediction = slope*z + intercept
    residuals = mu - Without_dark_energy_Model_prediction

    plt.figure(figsize=(8,6))
    plt.scatter(z, residuals, s=5, alpha=0.4)
    plt.axhline(0, color='gray', linestyle='-')

    plt.xlabel("Redshift(z)")
    plt.ylabel("Residuals ((Real mu from your provided dataset) - (Without dark energy Model prediction))")
    plt.title("Residuals: Where Real Data Deviates form the Simple Line")

    # Save the calculated plot figure first (always)
    abs_save_path = os.path.abspath(save_path)
    plt.savefig(save_path, dpi=150, bbox_inches="tight")
    print(f"✅ The Residuals plot calculated for your provided dataset is now saved at location: {abs_save_path}")

    # Then display this calculated Residuals plot image for the user provided dataset to the user,
    # while also taking into account the possibility of fallback in case of headless environments on the user machine:
    try:
        print("🎉🥳Yayy! You did it! Congratulation on your progress in this project so far. Here is the calcualted Residuals plot file for your given dataset-")
        plt.show()
        print("🏆 I am confident that you can soon take this project to your desired completion stage. I believe in you. Congratulations once again 😄👍👍✨💯 💯")
    except Exception:
        # If there is no GUI available on the user's machine, inform the user:
        print(f"ℹ️ Kindly note, the calculated Residuals plot image for your provided dataset cannot be displayed in this current environment as the Plot Display is not available in this environment. But please do not worry. This calcualted Hubble Plot image file for your provided dataset is now automatically saved on your this machine ath this location: {abs_save_path} ")
        print("😄 Congratulations once again for your success on this project so far! Keep going. I am confident that you can soon take this project to your desired completion stage. I believe in you. 😄👍💯🏆✨")

    # Close the figure to free memory
    plt.close()













