import os

# Define the list of file names with a pattern similar to what the user requested
file_names = [
    "ImportantProject_final.py", "ImportantProject_final2.py", "ImportantProject_final3.py", 
    "ImportantProject_finalfinal.py", "ImportantProject_finalfinal2.py", "ImportantProject_v1.py",
    "ImportantProject_v2.py", "ImportantProject_v3.py", "ImportantProject_v4.py", "ImportantProject_v5.py",
    "ImportantProject_final_v1.py", "ImportantProject_final_v2.py", "ImportantProject_final_v3.py",
    "ImportantProject_ultimate.py", "ImportantProject_ultimate_v2.py", "ImportantProject_superfinal.py",
    "ImportantProject_superfinal2.py", "ImportantProject_latest.py", "ImportantProject_latest_v1.py",
    "ImportantProject_final_final_final.py", "ImportantProject_final_v4.py", "ImportantProject_v6.py",
    "ImportantProject_finalfinalfinal.py", "ImportantProject_revised.py", "ImportantProject_final_v5.py",
    "ImportantProject_final_edition.py", "ImportantProject_v7.py", "ImportantProject_revised_v2.py",
    "ImportantProject_superultimate.py", "ImportantProject_last_final.py", "ImportantProject_final_v6.py",
    "ImportantProject_final_edit.py", "ImportantProject_edition_final.py", "ImportantProject_final_v7.py",
    "ImportantProject_finalfinal_v3.py", "ImportantProject_superfinal_v3.py", "ImportantProject_latest_v2.py",
    "ImportantProject_ultimate_final.py", "ImportantProject_final_v8.py", "ImportantProject_superfinal_final.py",
    "ImportantProject_final_final_v4.py", "ImportantProject_final_v9.py", "ImportantProject_latest_final.py",
    "ImportantProject_final_last_version.py", "ImportantProject_v8.py", "ImportantProject_final_final_v5.py",
    "ImportantProject_ultimate_final_v2.py", "ImportantProject_latest_edit.py", "ImportantProject_final_edition_v2.py",
    "ImportantProject_superfinal_final2.py"
]

Worsefile_names = [
    # Simulation files with unique dates
    "simulation_01_01_2024.py", "simulation_15_01_2024.py", "simulation_01_02_2024.py",
    "simulation_15_02_2024.py", "simulation_01_03_2024.py", "simulation_15_03_2024.py",
    "simulation_01_04_2024.py", "simulation_15_04_2024.py", "simulation_01_05_2024.py",
    "simulation_15_05_2024.py",

    # Degradation files with unique dates
    "degradation_02_01_2024.py", "degradation_16_01_2024.py", "degradation_02_02_2024.py",
    "degradation_16_02_2024.py", "degradation_02_03_2024.py", "degradation_16_03_2024.py",
    "degradation_02_04_2024.py", "degradation_16_04_2024.py", "degradation_02_05_2024.py",
    "degradation_16_05_2024.py"
]


# Create each file
for file_name in file_names:
    open('badVersionControl/'+file_name, 'w').close()

file_names


for file_name in Worsefile_names:
    open('worseVersionControl/'+file_name, 'w').close()

Worsefile_names