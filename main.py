import os
import subprocess

def run_gamess(input_file):
    version = "2023.R1.intel"  # GAMESS version
    ncpus = 1  # Number of CPUs
    
    gamess_bat = r"C:\Users\Public\gamess-64\rungms.bat"  # Path to rungms.bat script
    logfile = os.path.splitext(input_file)[0] + ".out"  # Use input file name for logfile
    
    command = [gamess_bat, input_file, version, str(ncpus)]
    command_str = " ".join(command) + " > " + logfile
    
    subprocess.run(command_str, shell=True, cwd=os.path.dirname(gamess_bat))

if __name__ == "__main__":
    folder_path = r"C:\Project\"  # Folder containing input files
    input_files = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) if file_name.endswith(".inp")]

    # Run GAMESS calculations
    for input_file in input_files:
        run_gamess(input_file)
