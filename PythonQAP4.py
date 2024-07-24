# Title:       Python QAP 4
# Description: A program for One Stop Insurance Company to 
#              enter and calculate policy information for customers.
# Author:      Noah Whiffen - SD12
# Date:        July 18th, 2024 - July 23rd, 2024

# Import required libraries.

import datetime
import sys
import time
# Program constants and variables.

PROVINCES = ["NL", "NS", "NB", "PE", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
PAYMENTOPTIONS = ["Full", "Monthly", "Down Payment"]
custClaims = [("14567", "2022-08-09", "$8200.00"), ("14568", "2019-04-14", "$7400.00"), ("14569", "2017-12-18", "$2200.00")]
file = "customers.dat"
f = "const.dat"
invDate = datetime.datetime.now()
monthlyPayments = 0
downPayment = 0
extraCosts = 0
firstPayment = None

# Declare program functions.

def paymentDate(invDate):
    if invDate.month == 12:
        firstPayment = invDate.replace(year = invDate.year + 1, month = 1, day = 1)
        return firstPayment
    else:
        firstPayment = invDate.replace(month = invDate.month + 1, day = 1)
        return firstPayment

# From the url: https://handhikayp.medium.com/creating-terminal-progress-bar-using-python-without-external-library-b51dd907129c
def progressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):
    # Generate and display a progress bar with % complete at the end.
 
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

def saveData():
    with open('customers.dat', 'a') as file:
        file.write(f"{POLICY_NUM},")
        file.write(f"{firstName},")
        file.write(f"{lastName},")
        file.write(f"{address},")
        file.write(f"{city},")
        file.write(f"{province},")
        file.write(f"{postalCode},")
        file.write(f"{phoneNum},")
        file.write(f"{insuredCars},")
        file.write(f"{extraLiability},")
        file.write(f"{glassIns},")
        file.write(f"{loanerCar},")
        file.write(f"{paymentPlan},")
        file.write(f"{invDate}\n")

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
    print()
    print("--------------------------------------------------")
    while True:
        firstName = input("Enter customer's first name (done to quit): ").title()
        if firstName.lower() == "done":
            sys.exit()
        else:
            break
    lastName = input("Enter customer's last name: ").title()
    address = input("Enter customer's street address: ")
    city = input("Enter customer's city: ").title()
    while True:
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
    while True:
        paymentPlan = input("Which payment plan would the customer like to use? (Full, Monthly, Down Payment): ").title()
        if paymentPlan in PAYMENTOPTIONS:
            if paymentPlan == "Down Payment":
                downPayment = float(input("Enter amount of down payment: "))
                break
            elif paymentPlan == "Monthly" or paymentPlan == "Full":
                break
            else:
                print("Please enter one of the options listed.")

    while True:
        claimNum = input("Enter customer's claim number: ")
        if claimNum.lower() == "done":
            sys.exit()           
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
    while True:
        claimDate = input("Enter date of claim (YYYY-MM-DD): ")
        if len(claimDate) == 10:
            if claimDate[:4].isdigit() and claimDate[4] == "-":
                if claimDate[5:7].isdigit() and claimDate[7] == "-":
                    if claimDate[8:].isdigit():
                        break
        print("Please enter date in required format. (YYYY-MM-DD)")
    while True:
        claimAmount = input("Enter amount of claim: ")
        if claimAmount.isdigit():
            break
        else:
            print("Amount must be a dollar value.")
    custClaims.append((claimNum, claimDate, claimAmount))

    # Perform required calculations.
    insuredCars = int(insuredCars) # This needed to go here instead of in the inputs as the .isidigit() wouldn't work.
    insPremium = BASE_PREMIUM + (insuredCars - 1) + (BASE_PREMIUM * DISCOUNT)
    
    if extraLiability == "Y":
        extraCosts += insuredCars * LI_CHARGES
    if glassIns == "Y":
        extraCosts += insuredCars * GLASS_CHARGES
    if loanerCar == "Y":
        extraCosts += insuredCars * LOANER_CHARGES
    
    totalInsPremium = insPremium + extraCosts
    hst = totalInsPremium * HST_RATE
    totalCost = totalInsPremium + hst

    if paymentPlan == "Full":
        monthlyPayments = 0
    if paymentPlan == "Down Payment":
        monthlyPayments = (totalCost - downPayment + PROCESSING_FEE)/8
    if paymentPlan == "Monthly":
        monthlyPayments = (totalCost + PROCESSING_FEE)/8

    # String manipulation & formatting.

    fullNameDSP = f"{firstName:<s} {lastName:<s}"
    phoneNumDSP = "(" + phoneNum[:3] + ")" + phoneNum[3:6] + "-" + phoneNum[6:]
    addressDSP = f"{address:<20s}"
    cityDSP = f"{city:<17s}"
    invDateFormat = invDate.strftime("%Y-%m-%d")
    insPremiumDSP = f"${insPremium:>.2f}"
    insuredCarsDSP = f"{insuredCars:>d}"
    claimAmount = float(claimAmount)
    claimAmountDSP = f"${claimAmount:>.2f}"
    hstDSP = f"${hst:>.2f}"
    totalCostDSP = f"${totalCost:>.2f}"
    extraCostsDSP = f"${extraCosts:>.2f}"
    monthlyPaymentsDSP = f"${monthlyPayments:>.2f}"
    downPaymentDSP = f"${downPayment:>.2f}"

    extraLiabilityDSP = ""
    glassInsDSP = ""
    loanerCarDSP = ""
    if extraLiability == "Y":
        extraLiabilityDSP = LI_CHARGES
        extraLiabilityDSP = f"${LI_CHARGES:>.2f}"
    else:
        extraLiabilityDSP = "None"
    if glassIns == "Y":
        glassInsDSP = GLASS_CHARGES
        glassInsDSP = f"${GLASS_CHARGES:>.2f}"
    else:
        glassInsDSP = "None"
    if loanerCar == "Y":
        loanerCarDSP = LOANER_CHARGES
        loanerCarDSP = f"${LOANER_CHARGES:>.2F}"
    else:
        loanerCarDSP = "None"

    # Progress bar to simulate work.

    totalIterations = 15
    Message = "Saving Data ..."
    
    for i in range(totalIterations + 1):
        time.sleep(0.1)
        progressBar(i, totalIterations, prefix=Message, suffix='Complete', length=50)
    
    POLICY_NUM += 1
    
    paymentDate(invDate)
    
    # Append customer info to a file.
    
    saveData()
    print("Information has been saved.")
    
    # Output values in a receipt.

    print()
    print("----------------------------------------------------------------------")
    print("                     One Stop Insurance Company")
    print("----------------------------------------------------------------------")
    print("                          CUSTOMER DETAILS")
    print(f"Policy #: {POLICY_NUM}                        Date:     {invDateFormat}")
    print(f"Name:     {fullNameDSP}                Address:  {addressDSP}")
    print(f"Phone:    {phoneNumDSP}                         {city},    {province}")
    print(f"                                                {postalCode}")
    print("                          COVERAGE DETAILS       ")
    print("----------------------------------------------------------------------")
    print(f"Insured vehicles: {insuredCarsDSP}                             Extra Liability: {extraLiabilityDSP}")
    print(f"Loaner Car:       {loanerCarDSP}                          Glass Coverage:  {glassInsDSP}")
    print("                                              --------------------------")
    print("                           PAYMENT DETAILS")
    print("------------------------------------------------------------------------")
    print(f"Premium Charges: {insPremiumDSP}                      Monthly Payment: {monthlyPaymentsDSP}")
    print(f"Taxes:           {hstDSP}                       Extra Costs:     {extraCostsDSP}")
    print(f"Total:           {totalCostDSP}                      Down Payment:    {downPaymentDSP}")
    print("                                              --------------------------")
    if firstPayment == None:
        print()
    else:
        print(f"First Payment on: {firstPayment}")
    print()
    print("              Claim #       Claim Date      Amount")
    print("              --------------------------------------")
    
    for claim in custClaims:
        claimNum = claim[0]
        claimDate = claim[1]
        claimAmount = claim[2]
        print(f"              {claimNum:<s}         {claimDate:<s}   {claimAmountDSP}")

        
    # Prompt for user to generate another invoice if needed.
    cont = input("Would you like to make another invoice? (Y/N)").upper()
    if cont == "N":
        break
    elif cont == "Y":
        continue
    else:
        print("Please enter Y or N.")