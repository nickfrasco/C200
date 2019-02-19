 #This is the bank as a dictionary.
#The key is the type and value is the number of pints.
# bank["O+"] == 2
bank = {"A+":4, "A-":2, "O-":0, "O+":2, "B+":5, "B-":2, "AB+":4, "AB-":2}

#1 Parameters donor's blood type donor_blood_type
#Return a string of the types that can accept the blood
#If the donor_blood_type is unknown, then return "Unkown"
def red_blood_compability(donor_blood_type):
    if "O-" in donor_blood_type:
        red_blood_compability = ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"]
        return red_blood_compability

    elif "O+" in donor_blood_type:
        red_blood_compability = ["O+", "A+", "B+", "AB+"]
        return red_blood_compability

    elif "A-" in donor_blood_type:
        red_blood_compability = ["O-", "O+", "A-", "A+"]
        return red_blood_compability

    elif "A+" in donor_blood_type:
        red_blood_compability = ["A+", "AB+"]
        return red_blood_compability
    
    elif "B-" in donor_blood_type:
        red_blood_compatability = ["B-", "B+", "AB-", "AB+"]
        return red_blood_compability 
    
    elif "B+" in donor_blood_type:
        red_blood_compatability = ["B+", "AB+"]
        return red_blood_compability
    
    elif "AB-" in donor_blood_type:
        red_blood_compatability = ["AB-", "AB+"]
        return red_blood_compability
    
    elif "AB+" in donor_blood_type:
        red_blood_compability = ["AB+"]
        return red_blood_compability

    else:
        red_blood_compability = "Unknown"
        return red_blood_compability

# Show the current bank
# This is a dictionary
def show_bank():
    print(bank)

#2 Parameters donor blood type is donor, recipient's type is recipient, and pints is the 
# number of pints that donor will give to recipient using the bank.
# Return True if the blood bank has enough pints to give 
# and remove the amount of pints used from the bank
# Return False if either the recipient can't recieve the type or there's not enough blood
def transfusion(donor, recipient, pints):
    if "O-" in donor:
        transfusion = False
        return transfusion

    elif "O+" in donor and "O+,A+,B+,AB+" in recipient:
        bank["O+"] = (pints - bank["O+"])
        if bank["O+"] < 0:
            transfusion = "True"
        else:
            transfusion = "false"
        return transfusion
     
    elif "A-" in donor and "O-,O+,A-,A+" in recipient:
        bank["A-"] = (pints - bank["A-"])
        if bank["A-"] < 0:
            transfusion = "True"
        else:
            transfusion = "false"
        return transfusion
        
    elif "A+" in donor and "A+" or "AB+" in recipient:
        bank["A+"] = (pints - bank["A+"])
        if bank["A+"] < 0:
            transfusion = "True"
        else:
            transfusion = "false"
        return transfusion

    elif "B-" in donor and "B-" or "B+" or "AB-" or "AB+" in recipient:
        bank["B-"] = (pints - bank["B-"])
        if bank["B-"] < 0:
            transfusion = "True"
        else:
            transfusion = "false"
        return transfusion

    elif "B+" in donor and "B+" or "AB+" in recipient:
        bank["B+"] = (pints - bank["B+"])
        if bank["B+"] < 0:
            transfusion = "True"
        else:
            transfusion = "false"
        return transfusion

    elif "AB-" in donor and "AB-" or "AB+" in recipient:
        bank["AB-"] = (pints - bank["AB-"])
        if bank["AB-"] < 0:
            transfusion = "True"
        else:
            transfusion = "false"
        return transfusion

    elif "AB+" in donor and "AB+" in recipient:
        bank["AB+"] == (pints - bank["AB+"])
        if bank["AB+"] < 0:
            transfusion = "True"
        else:
            transfusion = "false"
        return transfusion

print(red_blood_compability("A+"))
print(red_blood_compability("O-"))
print(red_blood_compability("C+"))


show_bank()
print(transfusion("A+","AB+",1))
show_bank()
print(transfusion("A-", "O-",1))
show_bank()
print(transfusion("A-", "B+",1))
show_bank()
print(transfusion("AB-", "AB+",3))
