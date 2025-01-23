import json
import os
import re

#converting the JSON into python dictionery
with open('Python-task.json', 'r') as file:
    data_dict = json.load(file)
#Using flag for the first iteratio, to put the first value as the min.
flag= 1
hotel_dict = {}
tax_string= ""
#Iteratin on all the rooms types and finding the cheapest
for room_type,price in data_dict["assignment_results"][0]["shown_price"].items():
        if flag:
            # putting the first value as the min price for comparing it afterwards
            min_price =(room_type,price)
            flag= 0
        else:
             #comparing beteween the room prices
            if float(price)< float(min_price[1]):
               min_price= (room_type,price)
#Pulling the tax values
tax_string = data_dict["assignment_results"][0]['ext_data']['taxes']
#Extracting only the numbers by searching the text pattern.
numbers = re.findall(r'\d+\.\d+', tax_string)
#Taking the number of guets value
number_of_guests =data_dict["assignment_results"][0]['number_of_guests']
#Calculating the total tax('TAX' and "City Tax")
total_tax = sum([float(num) for num in numbers])

for room_type,price  in data_dict["assignment_results"][0]['net_price'].items():
    hotel_dict[room_type] = float(price)+total_tax
#Writing all the results into txt file.
with open("Hotels-HW.txt", 'w') as file:
     #Clearing the file from data
    file.truncate()
    file.write("The cheapest shown price is: " + str(min_price[1]) + "\n")
    file.write("The cheapest room type is: " + min_price[0] + ", " + 'Number of guests: ' + str(number_of_guests) + ", " + 'The Price is: ' + str(min_price[1]) + "\n")
    file.write("Net Price with taxes:\n")
    for key, value in hotel_dict.items():
        file.write(f'{key}: {value:.2f}\n')
#opening the file
os.startfile("Hotels-HW.txt")
