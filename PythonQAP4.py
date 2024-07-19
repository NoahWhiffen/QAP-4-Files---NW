# Title:       Python QAP 4
# Description: A program for One Stop Insurance Company to 
#              enter and calculate policy information for customers.
# Author:      Noah Whiffen - SD12
# Date:        July 18th, 2024 - 

# Import required libraries.

import datetime
import sys

# All program constants.

PROVINCES = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
PAYMENTOPTIONS = ["Full", "Monthly", "Down Payment"]
extraCosts = 0
monthlyPayments = 0
downPayment = 0

# Declare program functions.

def monthFromToday():
    pass

# From the url: https://handhikayp.medium.com/creating-terminal-progress-bar-using-python-without-external-library-b51dd907129c
def progressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()


# Main program starts here.

while True:
    # Parse values from file and apply them to constants
    with open('const.dat', 'r') as f:
        consts = f.readlines()
        POLICY_NUM = int(consts[0].strip())
        BASE_PREMIUM = float(consts[1].strip())
        DISCOUNT = float(consts[2].strip())
        LI_CHARGES = float(consts[3].strip())
        GLASS_CHARGES = float(consts[4].strip())
        LOANER_CHARGES = float(consts[5].strip())
        HST_RATE = float(consts[6].strip())
        PROCESSING_FEE = float(consts[7].strip()) 

    # User inputs with validations 
    
    claimNum = input("Enter customer's claim number (done to quit): ")
    if claimNum == "done":
        exit
    elif claimNum.isalpha():
        print("Please enter a number.")
    else:
        break
    claimNum = input("Enter customer's claim number (done to quit): ")
    if claimNum == "done":
        exit
    elif claimNum.isalpha():
        print("Please enter a number.")
    else:
        break
    firstName = input("Enter customer's first name: ").title()
    lastName = input("Enter customer's last name: ").title()
    address = input("Enter customer's street address:")
    city = input("Enter customer's city").title()
    province = input("Enter customer's province (XX): ").upper()
    if province in PROVINCES:
        break
    else:
        print("Please enter a valid province.")
    while True:
        postalCode = input("Enter customer's postal code (X1X1X1): ")
        if len(postalCode) == 6:
            if postalCode[0].isalpha() and postalCode[2].isalpha() and postalCode[4].isalpha():
                if postalCode[1].isdigit() and postalCode[3].isdigit() and postalCode[5].isdigit():
                    break
        else:
            print("Please enter a valid postal code.")
    while True:
        phoneNum = input("Enter customer's phone number (XXXXXXXXXX): ")
        if len(phoneNum) == 10 and phoneNum.isdigit():
            break
        else:
            print("Phone number must be 10 digits.")
    while True:
        insuredCars = input("How many cars does the customer have insured?: ")
        if insuredCars.isdigit():
            break
        else:
            print("Input must be a number.")
    while True:
        extraLiability = input("Does customer want extra coverage up to $1000000? (Y/N): ").upper()
        if extraLiability == "Y" or extraLiability == "N":
            break
        else:
            print("Please enter Y or N.")
    while True:
        glassIns = input("Does customer want glass insurance? (Y/N): ").upper()
        if glassIns == "Y" or glassIns == "N":
            break
        else:
            print("Please enter Y or N.")
    while True:
        loanerCar = input("Does customer want a loaner car?: ").upper()
        if loanerCar == "Y" or loanerCar == "N":
            break
        else:
            print("Please enter Y or N.")
        paymentPlan = input("Which payment plan would the customer like to use? (Full, Monthly, Down Payment): ").title()
        if paymentPlan == "Down Payment":
            downPayment = input("Enter amount of down payment: ") 
    
    # Perform required calculations.

    totalInsPremium = insPremium + extraCosts
    hst = totalInsPremium * HST_RATE
    totalCost = totalInsPremium + hst

    insPremium = BASE_PREMIUM + (BASE_PREMIUM * DISCOUNT)
    
    if extraLiability == "Y":
        extraCosts += LI_CHARGES
    if glassIns == "Y":
        extraCosts += GLASS_CHARGES
    if loanerCar == "Y":
        extraCosts += LOANER_CHARGES
 
    if paymentPlan == "Full":
        monthlyPayments = 0
    if paymentPlan == "Down Payment":
        monthlyPayments = (totalCost - downPayment + PROCESSING_FEE)/8
    if paymentPlan == "Monthly":
        monthlyPayments = (totalCost + PROCESSING_FEE)/8

    invDate = datetime.datetime.now()
    monthFromToday()
    
    # Append policy data to a file.
    with open('customers.dat', 'a') as file:
        file.write(f"{POLICY_NUM}")
        file.write(f"{firstName}")
        file.write(f"{lastName}")
        file.write(f"{address}")
        file.write(f"{city}")
        file.write(f"{province}")
        file.write(f"{postalCode}")
        file.write(f"{phoneNum}")
        file.write(f"{insuredCars}")
        file.write(f"{extraLiability}")
        file.write(f"{glassIns}")
        file.write(f"{loanerCar}")
        file.write(f"{paymentPlan}")
        file.write(f"{invDate}")

        POLICY_NUM += 1
    
    # String manipulation for display on the receipt.

    fullName = f"{firstName:<20s} {lastName:<20s}"
    phoneNumDSP = "(" + phoneNum[:3] + ")" + phoneNum[3:6] + "-" + phoneNum[6:]
    extraLiabilityDSP = ""
    glassInsDSP = ""
    loanerCarDSP = ""
    if extraLiability == "Y":
        extraLiabilityDSP = LI_CHARGES
    else:
        extraLiabilityDSP = "NONE"
    if glassIns == "Y":
        glassInsDSP = GLASS_CHARGES
    else:
        glassInsDSP = "NONE"
    if loanerCar == "Y":
        loanerCarDSP = LOANER_CHARGES
    else:
        loanerCarDSP = "NONE"

    # Output values in a receipt.

    print()
    print("-------------------------------------------------------------------")
    print("                     One Stop Insurance Company")
    print("                           1-777-777-7777")
    print("-------------------------------------------------------------------")
    print(f"Name:  {fullName}                        Address: {address:15s}")
    print(f"Phone: {phoneNumDSP}                              {city:12s} {province:2s}")
    print(f"                                                  {postalCode}")
    print("-------------------------------------------------------------------")
    print(f"Insured vehicles: {insuredCars}          Extra Liability: {extraLiabilityDSP}")
    print(f"Loaner Car:       {loanerCarDSP}         Glass Coverage:  {glassInsDSP}")
    print()
    print("-------------------------------------------------------------------")
    print(f"Premium Charges: {insPremium}            Monthly Payment: {monthlyPayments}")
    print(f"                                         Extra Costs:     {extraCosts}")
    print(f"                                         Taxes:           {hst}")
    print(f"Total Cost: {totalCost}                  Down Payment:    {downPayment}")
    print("-------------------------------------------------------------------")

