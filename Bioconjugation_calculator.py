from Bioconjugation_functions import  bio_cys_calculator, bio_lys_calculator, in_situ, help_tool
from excel_modifier import excel_modifier
from predictions import pred_lys, pred_cys

print("Welcome, this is the Bioconjugation calculator!")
#entries = int(input("How many entries to perform?: "))
print("Define the amino acidic residue for the conjugation... if you don't know, type 'help' 😉.")

residues = ["lys", "cys", "help"]
options = ["yes", "no"]

#for entry in range(entries):
while True:
    residue = input("> ").lower()
    if residue == residues[2]:
        help_tool()
    elif residue == residues[1]:
        print("Very well!")
        file_name = bio_cys_calculator()
        break
    elif residue == residues[0]:
        print("in situ activation ?")
        while True:
            method = input("> ").lower()
            if method == options[1]:
                print("good choice!")
                file_name = bio_lys_calculator()
                break
            if method == options[0]:
                print("Ok!")
                file_name = in_situ()
                break
            else:
                print("Type 'yes' or 'no'")
        break
    else:
        print("type 'lys' or 'cys'")
file_path = file_name
mod = excel_modifier(file_path)
if residue == residues[0]:
    prediction_lys = pred_lys()
    print(prediction_lys)
if residue == residues[1]:
    prediction_cys = pred_cys()
    print(prediction_cys)

print("Good luck!")



