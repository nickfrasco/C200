
dict = {"0":"Do you have abdominal pain", 
        "1":"Do you have nausea", 
        "2":"Do you have vomiting", 
        "3":"Do you have fever", 
        "4":"Do you have loss of apetite", 
        "5":"Appendecitis", 
        "6":"No Appendecitis"}
#answer = input("Do you have abdominal pain 1/0: ")
#answer2 = input("Do you have nausea 1/0: ")
#answer3 = input("Do you have vomiting 1/0: ")
#answer4 = input("Do you have fever 1/0: ")
#answer5 = input("Do you have loss of apetite 1/0: ")
count = 0
def doctor():
    count = 0
    #while count < 3:  
    if input("Do you have abdominal pain 1/0: ") == "1" or "0" and count < 3:
        count += 1
        if input("Do you have nausea 1/0: ") == "1" or "0" and count < 3:
            count += 1
            if input("Do you have vomiting 1/0: ") =="1" or "0" and count < 3:
                count += 1
                if input("Do you have fever 1/0: ") == "1" or "0" and count < 3:
                    count += 1
                    if input("Do you have loss of apetite 1/0: ") == "1" or "0" and count < 3:
                        count += 1
                        print("Appendicitis")
        
                    else:
                        print("No Appendicitis")
                else:
                    print("No Appendicitis")
            else:
                print("No Appendicitis")


print(doctor())

        
    


