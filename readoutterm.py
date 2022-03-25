from calendar import c
import os
import subprocess

cmd = "more /Users/bcarpena/_Projects/ROP/statementofwork/training.csv | wc -l"
os.system(cmd)

returned_text = subprocess.check_output("more /Users/bcarpena/_Projects/ROP/statementofwork/training.csv | wc -l", shell=True, universal_newlines=True)
print("Output #### ")
print(returned_text)

returned_text = subprocess.check_output("uptime", shell=True, universal_newlines=True)
print("Output #### ")
print(returned_text)
