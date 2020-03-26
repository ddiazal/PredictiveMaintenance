import os
import glob
import time
import pandas as pd

print(os.getcwd())
os.chdir("C:\\Users\\DanielDíazAlmeida\\Documents\\FiltersData\\Data")

print(os.getcwd())

extension = "csv"
all_filenames = [i for i in glob.glob("*.{}".format(extension))]

#%%
cols2use = ["ESN",
           "AVL",
           "Vehículo",
           "Fecha Servidor",
           "Fecha AVL",
           "RPM",
           "Pedal",
           "F. de Carga",
           "Potencia",
           "Estado Motor",
           "Engine Torque Mode ()",
           "Actual Percent Torque (%)",
           "Actual Speed (RPM)",
           "Accelerator position (%)",
           "Percent Load At Current Speed (%)",
           "Fuel rate (L/h)",
           "Barometric Pressure (PSI)",
           "IMP-LB (PSI)",
           "IMT-LBF (F)",
           "EGT-AV (F)",
           "Battery potential (V)",
           "Coolant temperature (F)",
           "Fuel Temperature (F)",
           "Engine Oil Temperature (F)",
           "Injector Metering (PSI)",
           "Injector Timing (PSI)",
           "Pre-filter Oil Pressure (PSI)",
           "Instantaneous Estimated Brake Power (HP)",
           "IMT-LBR (F)",
           "IMT-RBF (F)",
           "IMT-RBR (F)",
           "IMP-RB (PSI)",
           "IMP-RB (MCRS) (PSI)",
           "Oil Differential Pressure (PSI)",
           "Ecu temperature (F)",
           "EGT-01 (F)",
           "EGT-02 (F)",
           "EGT-03 (F)",
           "EGT-04 (F)",
           "EGT-05 (F)",
           "EGT-06 (F)",
           "EGT-07 (F)",
           "EGT-08 (F)",
           "EGT-09 (F)",
           "EGT-10 (F)",
           "EGT-11 (F)",
           "EGT-12 (F)",
           "EGT-13 (F)",
           "EGT-14 (F)",
           "EGT-15 (F)",
           "EGT-16 (F)",
           "Crankcase Pressure (HPI) (in-H2O)",
           "Engine Oil Level (%)",
           "Post Oil Filter (PSI)",
           "Rifle Oil Pressure (PSI)",
           "Coolant Pressure (PSI)",
           "Ambient Temperature (F)",
           "EGT-17 (F)",
           "EGT-18 (F)",
           "IMT-LBM (F)",
           "IMT-RBM (F)",
           "Remote accelerator pedal position (%)",
           "Engine Pre-filter Oil Pressure (Extended Range) (PSI)",
           "Post Oil Filter (Extended Range) (PSI)",
           "Engine Operating State (bit)",
           "Engine Turbocharger 1 Compressor Inlet Pressure (kPa)",
           "Engine Protection System has Shutdown Engine (bit)",
           "Engine Protection System Approaching Shutdown (bit)",
           "Engine Protection System Timer State (bit)",
           "Engine Oil Filter Differential Pressure (Extended Range) (PSI)",
           "Engine Oil Priming Pump Control (bit)",
           "Engine Controlled Shutdown Request (bit)",
           "Engine Emergency (Immediate) Shutdown Indication (bit)",
           "Power (HP)"]
#%%
start = time.time()
# Combine all files in the list
combined_csv = pd.concat(
    [pd.read_csv(f, sep=';', usecols=cols2use, thousands='.', decimal=',') for f in all_filenames])

# Export to csv
os.chdir("C:\\Users\\DanielDíazAlmeida\\Desktop\\filtersDataRepository\\PredictiveMaintenance")
combined_csv.to_csv("combinedFilters_csv.csv", index=False, encoding='utf-8-sig')
end = time.time()
print(end - start)

filters_df = pd.read_csv("combinedFilters_csv.csv", sep=',')
print(filters_df.head())
