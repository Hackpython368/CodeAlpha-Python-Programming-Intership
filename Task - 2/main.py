import csv 
import datetime

stock = {
    "ABC In." : 45.63,
    "Reliance Industry": 102.34,
    "Jio" : 40
}

while True:

    c_name = input("Enter the company name :")
    quantity = int(input("Enter the quantity of the stock :"))

    total_cost = stock[c_name] * quantity

    today_data = datetime.date.today()

    data = []
    with open("stock.csv","a") as f:
        writer = csv.writer(f,lineterminator="\n")
        data.append([today_data,c_name,quantity,f"{total_cost:.2f}"])
        writer.writerows(data)

    print("Do you want add more stock? [Y for Yes| N for No]")
    ans = input()
    if ans == "Y" or ans == "y" :
        continue
    else:
        break

