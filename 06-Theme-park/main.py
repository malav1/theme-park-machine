from time import sleep
from datetime import date

#int input error function for products question
def option_int_input(prompt):
    not_valid = True
    while not_valid:
        try:
            int_value = int(input(prompt))
            if int_value<1 or int_value>4:
                print("\033[31mYour number must be between 1 and 10\033[0m")
            else:
                not_valid=False
        except ValueError:
            print("\033[31mYou can ONLY use numbers!\033[0m")
    return int_value

#int input error function for checkout
def checkout_int_input(prompt):
    not_valid = True
    while not_valid:
        try:
            int_value = int(input(prompt))
            if int_value!=10 and int_value!=20:
                print("\033[31mthe payment must be either a £10 note or £20 note\033[0m")
            else:
                not_valid=False
        except ValueError:
            print("\033[31mYou can ONLY use numbers!\033[0m")
    return int_value

#int input error func
def int_input(prompt):
    not_valid = True
    while not_valid:
        try:
            int_value = int(input(prompt))
            not_valid = False
        except ValueError:
            print("\033[31mYou can ONLY use numbers!\033[0m")
    return int_value

def y_n_input(prompt):
    loop=True
    while loop:
        user_answer=input(prompt).lower()
        if user_answer=='y' or user_answer=='n':
            loop=False
        else:
            print("\033[31mError. Please format your answer as Y or N\033[0m")
    return user_answer

# Provide a welcome message. centered
# Display the entrance ticket prices
sleep(1)
print("""
          🎢WELCOME TO COPINGTON ADVENTURE THEME PARK🎢
                    ------------------
                        ~PRODUCTS~
                        ---------
                      1️⃣ Adult Tickets 
                      2️⃣ Child Tickets 
                   3️⃣ Senior Citizen Tickets 
                      4️⃣ Parking Pass 

""")

sleep(1)

#assigning initial values to vars which will be calculated in the end
adult_tix=0
child_tix=0
senior_tix=0
parking_tix=0

#asking user to pick product and create while loop to keep coming back to the main menu
#how many adult, child, senior and parking passes they want
continue_products=True
continue_proceeding=True

#empty list to append user's purchases to which can be altered at checkout. position 0 is for adult tickets, 1 for children, 2 for seniors and 3 for parking,4 for wristbands
users_purchases=[[],[],[],[],[]]
while continue_products:
    user_choice=option_int_input("\nWould you like to add product 1️⃣ , 2️⃣ , 3️⃣ or 4️⃣ to your basket?: ")
    if user_choice==1:
        adult_tix=int_input("\n🎟️ ADULT TICKETS-£40\nHow many \033[4mAdult Tickets\033[0m would you like?: ")
        #creating while loop incase user inputs incorrect format
        users_purchases[0].append(adult_tix)
        continue_proceeding=True
        while continue_proceeding:
            #asking user if they want to go back to purchase more tickets or checkout
            proceeding=input("\nWould you like to go back to \033[4mproducts\033[0m or proceed to \033[4mcheckout\033[0m?: ").lower()
            if proceeding=="checkout":
                continue_proceeding=False
                continue_products=False
            elif proceeding=="products":
                continue_proceeding=False
            else:
                print("\033[31mInvalid. Please enter either 'products' or 'checkout'\033[0m")
        
   
    elif user_choice==2:
        child_tix=int_input("\n🎟️ CHILD TICKETS-£20\nHow many \033[4mChild Tickets \033[0mwould you like?: ")
        users_purchases[1].append(child_tix)
        continue_proceeding=True
        while continue_proceeding:
            proceeding=input("\nWould you like to go back to \033[4mproducts\033[0m or proceed to \033[4mcheckout\033[0m?: ").lower()
            if proceeding=="checkout":
                continue_products=False
                continue_proceeding=False
            elif proceeding=="products":
                continue_proceeding=False
            else:
               print("\033[31mInvalid. Please enter either 'products' or 'checkout'\033[0m")

    elif user_choice==3:
        senior_tix=int_input("\n🎟️ SENIOR CITIZEN TICKETS-£35\nHow many \033[4mSenior Citizen Tickets\033[0m would you like?: ")
        users_purchases[2].append(senior_tix)
        continue_proceeding=True
        while continue_proceeding:
            proceeding=input("\nWould you like to go back to \033[4mproducts\033[0m or proceed to \033[4mcheckout\033[0m?: ").lower()
            if proceeding=="checkout":
                continue_products=False
                continue_proceeding=False
            elif proceeding=="products":
                continue_proceeding=False
            else:
                print("\033[31mInvalid. Please enter either 'products' or 'checkout'\033[0m")
   
    elif user_choice==4:
        parking_tix=int_input("\n🅿️ PARKING PASS-£5\nHow many \033[4mParking Passes\033[0m would you like?: ")
        users_purchases[3].append(parking_tix)
        continue_proceeding=True
        while continue_proceeding:
            proceeding=input("\nWould you like to go back to \033[4mproducts\033[0m or proceed to \033[4mcheckout\033[0m?: ").lower()
            if proceeding=="checkout":
                continue_products=False
                continue_proceeding=False
            elif proceeding=="products":
                continue_proceeding=False
            else:
                print("\033[31mInvalid. Please enter either 'products' or 'checkout'\033[0m")
print()

#calculating number of people      
#calculating the total number of purchases of each type of product
users_ps_total = list(map(sum, users_purchases))
#then slicing the purchases that are only tickets for memebers of user's party
people_only_list=users_ps_total[:3]
total_people=sum(people_only_list)

#starting checkout section
print("""\n\n\n\n             
                      --------------    
                        ~CHECKOUT~
                         --------
""")

 #asking if they want wristband at checkout
wristband_loop=True
while wristband_loop:
    wristband_question=y_n_input("\nYou also have the product to purchase \033[4mwristbands\033[0m which are required for our top 5 🤩mega-thriller🤩 rides. They cost £10 each. Would you like to purchase any? Y/N: ").lower()

    if wristband_question=='y':
        wristband_loop=True
        wristband=int_input("How many would you like to purchase?: ")
        users_ps_total[4]=users_ps_total[4]+wristband
        while wristband>total_people:
             wristband=int_input("\033[31mError. The maxixmum  number of wristbands you can purchase is "+str(total_people)+"\n\033[0mHow many would you like to purchase?: ")
        wristband_price=wristband*10
        wristband_loop=False  

    elif wristband_question=='n':
        wristband_loop=False


#asking if they want to ammend their basket
#while loop to keep asking if they want to change the basket until they are satisfied. when N is entered, amend basket mode is exited and checkout proceeds.
amend=True
while amend:
    amend_basket=y_n_input("\nWould you like to amend your basket? Y/N: ").lower()
    if amend_basket=='y':
        #while loop to keep erroring if invalid value inputted which is not add or remove
        invalid=True
        while invalid:
            add_or_remove=input("\nWould you like to \033[4madd\033[0m or \033[4mremove\033[0m products?: ").lower()
            if add_or_remove =='add':
                invalid=False
                #while loop to keep erroring if invalid value inputted which is not any of the products advertised
                invalid_product=True
                while invalid_product:
                    adding_product=input("\nWould you like to add \033[4mAdult\033[0m Tickets, \033[4mChild\033[0m Tickets, \033[4mSenior\033[0m Tickets, \033[4mWristband\033[0m or \033[4mParking\033[0m Passes?: ").lower()
                    if adding_product=='adult':
                        adult_add=int_input("\nHow many Adult Tickets would you like to add?: ")
                        users_ps_total[0]=users_ps_total[0]+adult_add
                        invalid_product=False
                    elif adding_product=='child':
                        child_add=int_input("\nHow many Child Tickets would you like to add?: ")
                        users_ps_total[1]=users_ps_total[1]+child_add
                        invalid_product=False
                    elif adding_product=='senior':
                        senior_add=int_input("\nHow many Senior Tickets would you like to add?: ")
                        users_ps_total[2]=users_ps_total[2]+senior_add
                        invalid_product=False
                    elif adding_product=='parking':
                        parking_add=int_input("\nHow many Parking Passes would you like to add?: ")
                        users_ps_total[3]=users_ps_total[3]+parking_add
                        invalid_product=False
                    elif adding_product=='wristband':
                        #continuing to ensure wristbands dont exceed party number
                        people_only_list_checkout=users_ps_total[:3]
                        total_people_checkout=sum(people_only_list_checkout)
                        wristband_add=int_input("\nHow many Wristbands would you like to add?: ")
                        #number of already accumulated wristbands
                        remaining_wristbands=total_people_checkout-users_ps_total[4]
                        while wristband_add>remaining_wristbands:
                            wristband_add=int_input("\033[31mError. The maxixmum  number of wristbands you can purchase in total is "+str(total_people_checkout)+"\n\033[0mHow many would you like to add?: ")
                        users_ps_total[4]=users_ps_total[4]+wristband_add
                    else:
                        print("\033[31mError. Please enter adult, child, senior, parking or wristband.\033[0m")

            elif add_or_remove =='remove':
                invalid=False
                invalid_product2=True
                while invalid_product2:
                    removing_product=input("\nWould you like to remove \033[4mAdult\033[0m Tickets, \033[4mChild\033[0m Tickets, \033[4mSenior\033[0m Tickets or \033[4mParking\033[0m Passes?: ").lower()
                    if removing_product=='adult':
                        adult_remove=int_input("\nHow many Adult Tickets would you like to remove?: ")
                        users_ps_total[0]=users_ps_total[0]-adult_remove
                        invalid_product2=False
                    elif removing_product=='child':
                        child_remove=int_input("\nHow many Child Tickets would you like to remove?: ")
                        users_ps_total[1]=users_ps_total[1]-child_remove
                        invalid_product2=False
                    elif removing_product=='senior':
                        senior_remove=int_input("\nHow many Senior Tickets would you like to remove?: ")
                        users_ps_total[2]=users_ps_total[2]-senior_remove
                        invalid_product2=False
                    elif removing_product=='parking':
                        parking_remove=int_input("\nHow many Parking Passes would you like to remove?: ")
                        users_ps_total[3]=users_ps_total[3]-adult_remove
                        invalid_product2=False
                    elif removing_product=='wristband':
                        wristband_remove=int_input("\nHow many Wristbands would you like to remove?: ")
                        users_ps_total[4]=users_ps_total[4]-adult_remove
                        invalid_product2=False
            else:
                print("\033[31mInvalid. Please enter either 'add' or 'remove'\033[0m")
    elif amend_basket=='n':
        amend=False


#adding the tickets for each product and multiplying by price
total_price_adult=users_ps_total[0]*40
total_price_child=users_ps_total[1]*20
total_price_senior=users_ps_total[2]*35
total_price_parking=users_ps_total[3]*5
total_price_wristband=users_ps_total[4]*10

#calculating the total price
total_cost=total_price_adult+total_price_child+total_price_senior+total_price_parking+total_price_wristband

print("Your total to pay is £",total_cost)
# Ask for the lead booker surname (for the ticket)
wrong_name=True
while wrong_name:
    name=input("\n\nPlease enter a surname for this booking: ").capitalize()
    if name.isalpha()==False:
        #ensuring the name is not numeric
        print("\033[31mInvalid. Please enter a name.\033[0m")
    else:
        wrong_name=False

# Ask for payment (the machine only accepts £10 and £20 notes, each note entered will need to be counted)
print("💳 PAYMENT NOTE: this machine only accepts £10 and £20 notes\n")
continue_total_cost=True
while total_cost>0:
    inserted_payment=checkout_int_input("Please enter the amount you will be inserting: ")
    total_cost-=inserted_payment
    #avoiding saying you have to pay £-10 if user inserts too much
    if total_cost>0:
        print("You have",total_cost,"left to pay\n")
# Display change (if any)
    elif total_cost<0:
        print("Please collect your £",str(total_cost*-1),"change")
       


# Thank the customer for their purchase
print("""\n\n\n\n\n
                   -------------------------------------
                         ~THANK YOU FOR YOUR CUSTOM~
                           -----------------------
\n\n\n\n""")

# Print a ticket (display lead booker surname, tickets purchased, wristbands purchased, today’s date*)
today=date.today()
print(f"""
------------------------------
      ONE ADULT ADMISSION
      DATE:{today}
      lead booker:{name}
------------------------------
"""*users_ps_total[0])

print(f"""
------------------------------
      ONE CHILD ADMISSION
      DATE:{today}
      lead booker:{name}
------------------------------
"""*users_ps_total[1])
print(f"""
------------------------------
      ONE SENIOR CITIZEN ADMISSION
      DATE:{today}
      lead booker:{name}
------------------------------
"""*users_ps_total[2])
print(f"""
+====================+
      PARKING PASS
      DATE:{today}
+====================+
"""*users_ps_total[3])
print(f"""
--------------------------------------------
               PLACE ON WRIST
              DATE:{today}
--------------------------------------------
"""*users_ps_total[4])


















