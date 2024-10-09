import os
from Art import bid_logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(bid_logo)

bid_data={}
ask= "yes"
final_bit_amount=0
while ask=="yes":
    name=str(input("Enter your name: "))
    bit_amount=int(input("Enter your bid: $"))
    bid_data[name]=bit_amount
    ask=input("Do you want enter more:(yes/no): ").lower()


for i in bid_data:
    if bid_data[i]>=final_bit_amount:
        final_bit_amount= bid_data[i]
        winner_name= i
    else:
        final_bit_amount=final_bit_amount

clear()




print(f"The higest bid was made by '{winner_name}' of amount '${final_bit_amount}'\n!!!!!!!!!!!! WINNER !!!!!!!!!!!")