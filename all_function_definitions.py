
def find_user_details():

    global user_data

    #find name
    name = input("What is your name:")

    #find gender
    while True:
        gender = input("What is your gender (M/F): ")
        if gender.upper()[0] == 'F':
            gender = 'F'
            break
        elif gender.upper()[0] == 'M':
            gender = 'M'
            break
        else:
            print("That is not a valid input. Please try again.")
            continue
    
    #find age
    while True:
        age = input("What is your age?")
        try:
            age = int(age)
            if age < 0:
                print("That is not valid input. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not valid input. Please try again")
            continue
    

    #find marital_status
    marital_flag = True
    separated_flag = True

    while marital_flag:
        marital_status = input("Are you currently married/divorced/widowed/single (M/D/W/S):")
        if marital_status.upper()[0] == 'M':
            while separated_flag:
                separated_check = input("If you are married, are you separated from your spouse (Y/N): ")
                if separated_check.upper()[0] == 'Y':
                    marital_status = 'SP'
                    marital_flag = False
                    separated_flag = False
                elif separated_check.upper()[0] == 'N':
                    marital_status = 'M'
                    marital_flag = False
                    separated_flag = False
                else:
                    print("That is not a valid input. Please try again.")
                    continue 
        elif marital_status.upper()[0] in ['D','W','S']:
            marital_status = marital_status.upper()[0]
            break
        else:
            print("That is not a valid input. Please try again.")
            continue

    
   #find number of children
    children_presence_flag = True
    children_count_flag = True

    while children_presence_flag:
        children_presence = input("Do you have any children? (Y/N)")
        if children_presence.upper()[0] == 'Y':
            while children_count_flag:
                children_count = input("How many children do you have?")
                try:
                    children_count = int(children_count)
                    if children_count <0:
                        print("That is not valid input. Please try again")
                        continue
                    else:
                        children_presence_flag = False
                        children_count_flag = False
                except ValueError:
                    print("That is not valid input. Please try again")
                    continue
        elif children_presence.upper()[0] == 'N':
            children_count = 0
            children_presence_flag = False
            children_count_flag = False
        else:
            print("That is not a valid input. Please try again.")
            continue

    #find employment status
    while True:
        employment_status = input("Are you currently employed/self-employed/BOTH employed AND self-employed/unenmployed? (E/S/D/U) ")
        if employment_status.upper()[0] in ['E','S','D','U']:
            employment_status = employment_status.upper()[0]
            break
        else:
            print("That is not a valid input. Please try again.")
            continue

    #find if SG citizen/PR
    while True:
        citizenship_status = input("Are you a Singapore citizen or permanent resident? (Y/N) ")
        if citizenship_status.upper()[0] == 'Y':
            citizenship_status = 'Y'
            break
        elif citizenship_status.upper()[0] == 'N':
            citizenship_status = 'N'
            break
        else:
            print("That is not a valid input. Please try again.")
            continue

    user_data = [name,gender,age,marital_status,children_count,employment_status,citizenship_status]
    return user_data

################################################################################################3

def find_net_employment_income():

    global employment_income

    while True: #To find employment income
        employment_income = input("What is your employment income (Rounded to nearest whole number): ")
        try:
            employment_income = int(employment_income) #input validation to ensure only integers allowed
            if employment_income < 0: #input validation to ensure no negative integers
                print("Employment income has a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
                
    while True: #To find employment expense
        employment_expense = input("What is your employment expense (Rounded to nearest whole number): ")
        try:
            employment_expense = int(employment_expense) #input validation to ensure only integers allowed
            if employment_expense < 0: #input validation to ensure no negative integers
                print("Employment expense has a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
            
    net_employment_income = max(0,employment_income - employment_expense) #To ensure that net employment income cannot be less than 0
    
    return employment_income,net_employment_income

################################################################################################################

def find_trade_income():


    while True: #To find trade income
        trade_income = input("What is your trade income (Rounded to nearest whole number): ")
        try:
            trade_income = int(trade_income) #User input validation to ensure only integers allowed           
            if trade_income<0: #input validation to ensure no negative integers
                print("Trade income has a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
    return trade_income

################################################################################################################

def find_other_income():

    
    while True: #To find dividend income
        dividend_income = input("What is your dividend income (Rounded to nearest whole number): ")
        try:
            dividend_income = int(dividend_income) #User input validation to ensure only integers allowed
            if dividend_income < 0: #input validation to ensure no negative integers
                print("Dividend income has a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
            
    while True: #To find interest income
        interest_income = input("What is your interest income (Rounded to nearest whole number): ")
        try:
            interest_income = int(interest_income) #User input validation to ensure only integers allowed
            if interest_income < 0: #input validation to ensure no negative integers
                print("Interest income has a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
            
    while True: #To find rental income
        rental_income = input("What is your rental income (Rounded to nearest whole number): ")
        try:
            rental_income = int(rental_income) #User input validation to ensure only integers allowed
            if rental_income < 0: #input validation to ensure no negative integers
                print("Rental income has a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
            
    while True: #To find royalties
        royalties_income = input("What is your income from royalties (Rounded to nearest whole number): ")
        try:
            royalties_income = int(royalties_income) #User input validation to ensure only integers allowed
            if royalties_income < 0: #input validation to ensure no negative integers
                print("Income from royalties has a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
    
    while True: #To find other gains of an income nature
        other_gains_income = input("What are your other gains/profits of an income nature (Rounded to nearest whole number): ")
        try:
            other_gains_income = int(other_gains_income) #User input validation to ensure only integers allowed
            if other_gains_income < 0: #input validation to ensure no negative integers
                print("Gains/profits of an income nature has a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
            
    other_income = dividend_income + interest_income + rental_income + royalties_income + other_gains_income
    return other_income

################################################################################################################

def find_approved_donations():

    

    while True: #To cash donations
        cash_donation = input("How much are your cash donations to an IPC (Rounded to nearest whole number): ")
        try:
            cash_donation = int(cash_donation) #User input validation to ensure only integers allowed
            if cash_donation < 0: #input validation to ensure no negative integers
                print("Cash donation have a minimum value of 0. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again.")
            
    approved_donations = round(cash_donation * 2.5) #Approved donations to be deductible at 2.5 times, rounded off and convert into integer
    return approved_donations

################################################################################################################

def find_earned_income_relief(net_employment_income,trade_income):

    


    earned_income = net_employment_income + trade_income
    
    flag1 = None


    if earned_income > 0:
        earned_income_status = True
        flag1 = True
    elif earned_income == 0: #If no earned income, skip remaining questions
        earned_income_status = False
        disability = None
        flag1 = False 
            

    while flag1: #To find if user has permanent physical or mental disability
        disability = input("Do you have a permanent physical or mental disability that severely affects your ability to work (Y/N): ")
        if disability.upper()[0] == 'Y':
            disability = True
            flag1 = False
        elif disability.upper()[0] == 'N':
            disability = False
            flag1 = False
        else:
            print("That is not a valid input. Please try again.")
            continue 

    if user_data[2] < 55 and earned_income_status == True and disability == False:
        if earned_income < 1000:
            earned_income_relief = earned_income
        else:
            earned_income_relief = 1000
    elif user_data[2] >= 55 and user_data[2] <= 60 and earned_income_status == True and disability == False:
        if earned_income < 6000:
            earned_income_relief = earned_income
        else:
            earned_income_relief = 6000
    elif user_data[2] >= 60 and earned_income_status == True and disability == False:
        if earned_income < 8000:
            earned_income_relief = earned_income
        else:
            earned_income_relief = 8000
    elif user_data[2] < 55 and earned_income_status == True and disability == True:
        if earned_income < 4000: 
            earned_income_relief = earned_income
        else:
            earned_income_relief = 4000
    elif user_data[2] >= 55 and user_data[2] <= 60 and earned_income_status == True and disability == True:
        if earned_income < 10000:
            earned_income_relief = earned_income
        else:
            earned_income_relief = 10000
    elif user_data[2] >= 60 and earned_income_status == True and disability == True:
        if earned_income < 12000:
            earned_income_relief = earned_income
        else:
            earned_income_relief = 12000
    else:
        earned_income_relief = 0 #not eligible for the relief

    earned_income_relief = round(earned_income_relief)

    return earned_income_relief
    
################################################################################################################
 
def find_spouse_handicapped_relief():    

    flag1 = True
    flag2 = None
    flag3 = None

    while flag1: #To find if user has a spouse
        spouse = input("Do you have a spouse living with/supported by you (Y/N): ")
        if spouse.upper()[0] == 'Y':
            spouse = True
            flag2 = True
            flag1 = False
        elif spouse.upper() == 'N': 
            spouse = False
            spouse_income = False
            spouse_disability = False
            flag1 = False
            flag2 = False
            flag3 = False
        else:
            print("That is not a valid input. Please try again.")
            continue
        

    while flag2:
        spouse_income = input("Does your spouse have an annual income exceeding $4,000 (Y/N): ") #If user has a spouse, ask if spouse has annual income > $4,000
        if spouse_income.upper()[0] == 'Y':
            spouse_income = False
            flag3 = True
            flag2 = False
        elif spouse_income.upper()[0] == 'N':
            spouse_income = True
            flag3 = True
            flag2 = False
        else:
            print("That is not a valid input. Please try again.")
            continue
                
                
    while flag3:
        spouse_disability = input("Does your spouse have a permanent physical or mental disability that severely affects his/her ability to work (Y/N): ") #If user has a spouse, ask if spouse is disabled
        if spouse_disability.upper()[0] == 'Y':
            spouse_disability = True
            flag3 = False
        elif spouse_disability.upper()[0] == 'N':
            spouse_disability = False 
            flag3 = False                    
        else:
            print("That is not a valid input. Please try again.")
            continue


    if spouse == True and (spouse_income == True or spouse_income == False) and spouse_disability == True:
        spouse_handicapped_relief =  5500
    elif spouse == True and spouse_income == True and spouse_disability == False:
        spouse_handicapped_relief =  2000
    else:
        spouse_handicapped_relief = 0

    spouse_handicapped_relief = round(spouse_handicapped_relief)

    return spouse_handicapped_relief
    
################################################################################################################

def find_qualifying_handicapped_child_relief():
        
        
    eligible_handicapped_child_headcount = 0 #initial headcount is 0
    eligible_nonhandicapped_child_headcount = 0 #initial headcount is 0
    global child_order


    #this is a dictionary whereby each key = child order (E.g. 1,2,3) , and the values = amount claimable for each child (E.g. 4000,7500)
    #used in WMCR where child order is relevant for $50,000 cap per child
    child_order= {} 

    #for each child under children_count
    for number in range(1,user_data[4]+1):
        
        child_disability = input(f"Does your child_{number} have a permanent physical or mental disability that severely affects his/her ability to work (Y/N): ") #If user has a child, ask if child is disabled
        if child_disability.upper()[0] == 'Y': #If child is disabled, skip questions on child income,age and education because eligible for HCR
            eligible_handicapped_child_headcount += 1 #add to headcount
            child_order[number] = 7500
            continue #If child is disabled, skip remaining questions and move to next child because eligible for HCR
        elif child_disability.upper()[0] == 'N':
            child_income = input(f"Does your child_{number} have an annual income exceeding $4,000. This includes allowances and salaries from NS/internship/school attachment/part-time employment. It does not include scholarships, bursaries and similar allowances (Y/N): ") #If user has a child, ask if child has annual income > $4,000
            if child_income.upper()[0] == 'Y':
                child_order[number] = 0
                continue #If child has income more than $4,000, skip remaining questions and move to next child because not eligible for relief
            elif child_income.upper()[0] == 'N':
                child_age_education = input(f"Is your child_{number} below 16 years old OR studying full-time at any university or other educational institution (Y/N): ") #If user has a child, ask if child has annual income > $4,000
                if child_age_education.upper()[0] == 'Y':
                    eligible_nonhandicapped_child_headcount += 1 #add to headcount
                    child_order[number] = 4000
                    continue
                elif child_age_education.upper()[0] == 'N': #If child is above 16 or not studying, 
                    child_order[number] = 0
                    continue
                else:
                    print("That is not a valid input. Please try again.")
                    continue
            else:
                print("That is not a valid input. Please try again.")
                continue      
        else:
            print("That is not a valid input. Please try again.")
            continue

    total_relief_available_under_qcr_hcr = round(eligible_nonhandicapped_child_headcount * 4000 + eligible_handicapped_child_headcount * 7500)
    return total_relief_available_under_qcr_hcr,child_order

################################################################################################################

def find_grandparent_caregiver_relief():

    
    while True:
        child_status = input("Do you have a parent/parent-in-law/grandparent/grandparent-in-law who is (a) not working and (b) staying in Singapore and looking after any of your (ci) children who is a Singapore Citizen age 12 and below ;or (cii) unmarried handicapped children who is a Singapore Citizen: (Y/N) ")
        if child_status.upper()[0] == 'Y':
            grandparent_caregiver_relief = 3000
            break
        elif child_status.upper()[0] == 'N':
            grandparent_caregiver_relief = 0
            break
        else:
            print("That is not a valid input. Please try again.")
        continue

    return grandparent_caregiver_relief

################################################################################################################
 
def find_working_mother_child_relief(child_order,net_employment_income, trade_income):

    wmcr_child_order = {}

    #for each key-value pair in child_order, create a new dictionary whereby key = child order (same as dictionary child_order, but values = amount claimable under WMCR)
    #WMCR claimable on the child only if the child is eligible for QHCR, therefore value cannot be 0 if child is claimable under WMCR
    for key,value in child_order.items():
        if key == 1 and value != 0:
            wmcr_child_order[key] = 0.15 * (net_employment_income + trade_income)
        if key == 2 and value != 0:
            wmcr_child_order[key] = 0.20 * (net_employment_income + trade_income)
        if key >=3 and value != 0:
            wmcr_child_order[key] = 0.25 * (net_employment_income + trade_income)


    for key in wmcr_child_order.keys():
        if child_order[key] + wmcr_child_order[key] > 50000:
            wmcr_child_order[key] = 50000 - child_order[key]
        else:
            pass


    working_mother_child_relief = round(sum(wmcr_child_order.values()))

    print(child_order)
    print(wmcr_child_order)

    return working_mother_child_relief
    
################################################################################################################

def find_foreign_domestic_worker_levy_relief():


    flag1 = True

    while flag1:
        employ_foreign_domestic_worker_status = input("Did you or your husband employ a foreign domestic worker: (Y/N) ")
        if employ_foreign_domestic_worker_status.upper()[0] == 'Y':
            employ_foreign_domestic_worker_status = True
            levy_paid = input('How much foreign domestic worker levy was paid in the year. If you employed more than one domestic helper, please choose the domestic worker that you paid the highest total levy for in the year: ')
            try:
                levy_paid = int(levy_paid)
                if levy_paid <0:
                    print("Foreign domestic worker levy has a minimum value of 0. Please try again")
                    continue
                else:
                    flag1 = False
            except ValueError:
                print("That is not a valid input. Please try again.")            
        elif employ_foreign_domestic_worker_status.upper()[0] == 'N':
            employ_foreign_domestic_worker_status = False 
            levy_paid = 0
            flag1 = False           
        else:
            print("That is not a valid input. Please try again.")
            continue

    
    if employ_foreign_domestic_worker_status == True and levy_paid > 0:
        foreign_domestic_worker_levy_relief = levy_paid * 2
    else:
        foreign_domestic_worker_levy_relief = 0

    foreign_domestic_worker_levy_relief = round(foreign_domestic_worker_levy_relief)
    return foreign_domestic_worker_levy_relief

################################################################################################################

def find_parent_handicapped_parent_relief():
    
    flag1 = True
    flag2 = True


    while flag1:
        dependant = input("Do you have a parent/parent-in-law/grandparent/grandparent-in-law supported by you (Y/N): ")
        if dependant.upper()[0] == 'Y':
            dependant = True       
            while flag2:
                total_dependant_headcount = input("How many of such dependants do you have: ")
                try:
                    total_dependant_headcount = int(total_dependant_headcount) #User input validation to ensure only integers allowed
                    if total_dependant_headcount < 0 or total_dependant_headcount > 2: #input validation to ensure no negative integers
                        print("Total dependants cannot be less than 0. You can only claim for up to 2 dependants. Please try again.")
                        continue
                    else:
                        flag1 = False #total_dependant_headcount has suitable input (integer and more than 0) therefore set all flags to False to break out of all loops-->subsequently calculate eligibility for each child
                        flag2 = False
                except ValueError:
                    print("That is not a valid input. Please try again.")
                    continue                         
        elif dependant.upper()[0] == 'N': #If user does not have a dependant, skip questions on child age,education,income and disability 
            dependant = False
            total_dependant_headcount = 0
            eligible_nonhandicapped_dependant_staying_headcount = 0
            eligible_nonhandicapped_dependant_not_staying_headcount = 0
            eligible_handicapped_dependant_staying_headcount = 0
            eligible_handicapped_dependant_not_staying_headcount = 0
            break
        else:
            print("That is not a valid input. Please try again.")
            continue    

    #The portion below is to calculate eligibiity of EACH dependant

    eligible_nonhandicapped_dependant_staying_headcount = 0
    eligible_nonhandicapped_dependant_not_staying_headcount = 0
    eligible_handicapped_dependant_staying_headcount = 0
    eligible_handicapped_dependant_not_staying_headcount = 0

    for number in range(total_dependant_headcount):
        
        stay_with_user = input(f"Does your dependant_{number+1} stay with you (Y/N): ")
        if stay_with_user.upper()[0] == 'Y': #stays with user
            dependant_disability = input(f"Does your dependant_{number+1} have a permanent physical or mental disability that severely affects his/her ability to work (Y/N): ") #If user has a dependant, ask if dependant is disabled
            if dependant_disability.upper()[0] == 'Y': 
                eligible_handicapped_dependant_staying_headcount += 1
                continue #If dependant is disabled, skip remaining questions and move to next dependant because eligible for HCR
            elif dependant_disability.upper()[0] == 'N':
                dependant_income = input(f"Does your dependant_{number+1} have an annual income exceeding $4,000 (Y/N): ") #If user has a dependant, ask if dependant has annual income > $4,000
                if dependant_income.upper()[0] == 'Y':
                    continue #If dependant has income more than $4,000, skip remaining questions and move to next dependant because not eligible for relief
                elif dependant_income.upper()[0] == 'N':
                    eligible_nonhandicapped_dependant_staying_headcount += 1
                else:
                    print("That is not a valid input. Please try again.")
                    continue      
            else:
                print("That is not a valid input. Please try again.")
                continue
        elif stay_with_user.upper()[0] == 'N': #does not stay with user
            dependant_disability = input(f"Does your dependant_{number+1} have a permanent physical or mental disability that severely affects his/her ability to work (Y/N): ") #If user has a dependant, ask if dependant is disabled
            if dependant_disability.upper()[0] == 'Y': 
                eligible_handicapped_dependant_not_staying_headcount += 1
                continue #If dependant is disabled, skip remaining questions and move to next dependant because eligible for HCR
            elif dependant_disability.upper()[0] == 'N':
                dependant_income = input(f"Does your dependant_{number+1} have an annual income exceeding $4,000 (Y/N): ") #If user has a dependant, ask if dependant has annual income > $4,000
                if dependant_income.upper()[0] == 'Y':
                    continue #If dependant has income more than $4,000, skip remaining questions and move to next dependant because not eligible for relief
                elif dependant_income.upper()[0] == 'N':
                    eligible_nonhandicapped_dependant_not_staying_headcount += 1
                else:
                    print("That is not a valid input. Please try again.")
                    continue      
            else:
                print("That is not a valid input. Please try again.")
                continue
        else:
            print("That is not a valid input. Please try again.")
            continue 


    total_relief_available_under_phpr = round(eligible_nonhandicapped_dependant_staying_headcount * 9000 + eligible_nonhandicapped_dependant_not_staying_headcount * 5500 + eligible_handicapped_dependant_staying_headcount * 14000 + eligible_handicapped_dependant_not_staying_headcount * 10000)
    return total_relief_available_under_phpr

################################################################################################################

def find_handicapped_brother_sister_relief():


    flag1 = True
    flag2 = True

    while flag1:
        handicapped_sibling_status = input("Do you have handicapped siblings/siblings-in-law supported by you (Y/N): ")
        if handicapped_sibling_status.upper()[0] == 'Y':
            handicapped_sibling_status = True
            while flag2:
                handicapped_sibling_headcount = input("How many of such siblings/siblings-in-law do you have: ")
                try:
                    handicapped_sibling_headcount = int(handicapped_sibling_headcount)
                    if handicapped_sibling_headcount <0:
                        print("Total siblings/siblings-in-law cannot be less than 0. Please try again")
                        continue
                    else:
                        flag1 = False
                        flag2 = False
                except:
                    print("That is not a valid input. Please try again.")
                    continue
        elif handicapped_sibling_status.upper()[0] == 'N':
            handicapped_sibling_status = False
            break
        else:
            print("That is not a valid input. Please try again.")
            continue

    if handicapped_sibling_status == True:
        handicapped_brother_sister_relief = handicapped_sibling_headcount * 5500
    elif handicapped_sibling_status == False:
        handicapped_brother_sister_relief = 0

    handicapped_brother_sister_relief = round(handicapped_brother_sister_relief)
    return handicapped_brother_sister_relief

################################################################################################################     

def find_cpf_relief_cap(net_employment_income,trade_income):

    #flag1 is for ordinary wage (For employed users only)
    #flag2 is for months worked in the YA (For employed users only)
    #flag3 is for additional wage (For employed users only)
    #flag4 is for voluntary medisave contributions (For employed users only)
    #flag5 is for compulsory MediSave contributions and voluntary CPF contributions (For self-employed users only)
    #flag6 is for voluntary CPF contributions (For self-employed users only)
    
    global voluntary_medisave_contribution
    global self_employed_compulsory_medisave_contribution 
    global self_employed_voluntary_cpf_contribution
    global employee_cpf_contributions
    global employer_cpf_contributions



    if user_data[5] == 'E' : #employed
        flag1 = True
        flag2 = True
        flag3 = True
        flag4 = True
        flag5 = False
        
    elif user_data[5] == 'D': #dual employment status
        flag1 = True
        flag2 = True
        flag3 = True
        flag4 = True
        flag5 = True
    elif user_data[5] == 'S': #self-employed
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        flag5 = True
    elif user_data[5] == 'U': #unemployed
        flag1 = False
        flag2 = False
        flag3 = False
        flag4 = False
        flag5 = False


    while flag1:
        ordinary_wage = input("As an employed individual, what is your ordinary wage PER MONTH? Ordinary wages are wages due or granted for employment. They include allowances (e.g. food allowance and overtime payments) earned by an employee in the month. Ordinary wages must be paid before the due date for payment of CPF contributions for that month.")
        try:
            ordinary_wage = int(ordinary_wage)
            if ordinary_wage < 0:
                print("That is not a valid input. Ordinary wage cannot be less than 0")
                continue
            else:
                flag1 = False
                flag2 = True
                flag3 = True
        except ValueError:
            print("That is not a valid input. please enter a whole number.")
            continue
    
    while flag2:
        months_worked = input("How many months were you employed in the year of assessment?")
        try:
            months_worked = int(months_worked)
            if months_worked <= 0 or months_worked >12:
                print("That is not a valid input. Please enter a number greater than 0 and less than/equals to 12. ")
                continue
            else:
                flag1 = False
                flag2 = False
                flag3 = True
        except:
            print("That is not a valid input. please enter a whole number.")
            continue              


    while flag3:
        additional_wage = input("As an employed individual, what is your additional wage FOR THE ENTIRE YEAR? Additional wages are wage supplements which are not granted wholly and exclusively for the month. These include your annual bonus and leave pay. ")
        try:
            additional_wage = int(additional_wage)
            if additional_wage < 0:
                print("That is not a valid input. Ordinary wage cannot be less than 0")
                continue
            else:
                flag1 = False
                flag2 = False
                flag3 = False
        except ValueError:
            print("That is not a valid input. please enter a whole number.")
            continue


    #To find applicable cpf contribution rate (Based on YA22)
    if user_data[2] <= 55:
        employee_contribution_rate = 0.20
        employer_contribution_rate = 0.17
        cpf_contribution_cap = 0.37 * 102000
    elif user_data[2] > 55 and user_data[2] <=60:
        employee_contribution_rate = 0.14
        employer_contribution_rate = 0.14
        cpf_contribution_cap = 0.28 * 102000
    elif user_data[2] > 60 and user_data[2] <= 65:
        employee_contribution_rate = 0.085
        employer_contribution_rate = 0.1
        cpf_contribution_cap = 0.185 * 102000
    elif user_data[2] > 65 and user_data[2] <=70:
        employee_contribution_rate = 0.06
        employer_contribution_rate = 0.08
        cpf_contribution_cap = 0.14 * 102000
    else:
        employee_contribution_rate = 0.05
        employer_contribution_rate = 0.75
        cpf_contribution_cap = 0.125 * 102000


    if net_employment_income > 0: #To find actual ow and aw subjected to CPF
        total_ow = ordinary_wage * months_worked

        ow_ceiling = 6000 * months_worked
        ow_subjected_to_cpf = min(total_ow,ow_ceiling)

        aw_ceiling = 102000 - ow_subjected_to_cpf
        aw_subjected_to_cpf = min(additional_wage,aw_ceiling)

        total_contribution_rate = employee_contribution_rate + employer_contribution_rate
        employer_cpf_contributions = employer_contribution_rate * (ow_subjected_to_cpf+ aw_subjected_to_cpf)
        employee_cpf_contributions = employee_contribution_rate * (ow_subjected_to_cpf+ aw_subjected_to_cpf)
        employer_employee_cpf_contributions = total_contribution_rate * (ow_subjected_to_cpf+ aw_subjected_to_cpf)
    else:
        pass

    
    while flag4:
        voluntary_medisave_contribution = input("As an employed individual, how much voluntary contributions to your MediSave Account have you made?")
        try:
            voluntary_medisave_contribution = int(voluntary_medisave_contribution)
            if voluntary_medisave_contribution < 0:
                print("That is not valid input. Minimum value is 0. Please try again")
                continue
            else:               
                flag4 = False
                flag6 = False
        except ValueError:
            print("That is not valid input. Minimum value is 0. Please try again")
            continue

    #to cap the allowable voluntary medisave contributions for employed users
    max_voluntary_medisave_allowable = min(37740 - employer_employee_cpf_contributions,voluntary_medisave_contribution)
    voluntary_medisave_contribution = max_voluntary_medisave_allowable


    while flag5:
        self_employed_compulsory_medisave_contribution = input("As a self-employed individual, how much compulsory MediSave contributions have you made?")
        try:
            self_employed_compulsory_medisave_contribution = int(self_employed_compulsory_medisave_contribution)
            if self_employed_compulsory_medisave_contribution < 0:
                print("That is not valid input. Minimum value is 0. Please try again")
                continue
            else:
                flag5 = False
                flag6 = True
        except ValueError:
            print("That is not valid input. Minimum value is 0. Please try again")
            continue
        
        
    while flag6:
        self_employed_voluntary_cpf_contribution = input("As a self-employed individual, how much voluntary CPF contributions have you made?")
        try:
            self_employed_voluntary_cpf_contribution = int(self_employed_voluntary_cpf_contribution)
            if self_employed_voluntary_cpf_contribution < 0:
                print("That is not valid input. Minimum value is 0. Please try again")
                continue
            else:
                flag6 = False
        except ValueError:
            print("That is not valid input. Minimum value is 0. Please try again")
            continue


    
    if user_data[5] == 'E': #employee
        cpf_relief_cap = min(cpf_contribution_cap,employer_employee_cpf_contributions+voluntary_medisave_contribution)
        cpf_relief = min(cpf_relief_cap, employee_cpf_contributions + voluntary_medisave_contribution)
    elif user_data[5] == 'S': #self-employed
        cpf_relief_cap = min(37740,0.37*trade_income,self_employed_voluntary_cpf_contribution+self_employed_compulsory_medisave_contribution)
        cpf_relief = cpf_relief_cap
    elif user_data[5] == 'D': #employed and self-employed
        cpf_relief_cap = min(37740,0.37*trade_income, employer_employee_cpf_contributions+voluntary_medisave_contribution+self_employed_voluntary_cpf_contribution+self_employed_compulsory_medisave_contribution)
        cpf_relief = min(cpf_relief_cap,employee_cpf_contributions + voluntary_medisave_contribution+self_employed_voluntary_cpf_contribution+self_employed_compulsory_medisave_contribution)

    cpf_relief = round(cpf_relief)
    return cpf_relief
        
################################################################################################################ 

def find_life_insurance_relief():


    flag1 = True
    flag2 = False
    flag3 = False


    if user_data[5] == 'E': #User only has employment income
        total_contributions = employee_cpf_contributions+voluntary_medisave_contribution
    elif user_data[5] == 'S' > 0: #User only has trade income
        total_contributions = self_employed_compulsory_medisave_contribution  + self_employed_voluntary_cpf_contribution
    elif user_data[5] == 'D': #User has dual employment status
        total_contributions = employee_cpf_contributions+voluntary_medisave_contribution+self_employed_voluntary_cpf_contribution+self_employed_compulsory_medisave_contribution
        
    if total_contributions <5000:
        flag1 = True
    else:
        flag1 = False

    while flag1:
        insurance_premium_paid_status = input("Have you paid insurance premiums on your own life insurance policy or your wife's life insurance policy (for married men) (Y/N): ")
        if insurance_premium_paid_status.upper()[0] == 'Y':
            flag1 = False
            flag2 = True
        elif insurance_premium_paid_status.upper()[0] == 'N':
            flag1= False
            flag2 = False
            flag3 = False       
            life_insurance_relief = 0  
        else:
            print("That is not a valid input. Please try again.")
            continue
    
    while flag2:
        insured_value = input("What is the insured value of your own/your wife's life. Please round off to nearest number")
        try:
            insured_value = int(insured_value)
            if insured_value < 0:
                print("That is not a valid input. Please try again")
                continue
            else:
                flag2 = False
                flag3 = True
        except ValueError:
            print("That is not a valid input. Please try again")
            continue
    
    while flag3:
        insurance_premium_paid = input("How much insurance premiums have you paid in the year. Please round off to nearest number")
        try:
            insurance_premium_paid = int(insurance_premium_paid)
            if insurance_premium_paid < 0:
                print("That is not a valid input. Please try again")
                continue
            else:
                flag3 = False
                break
        except ValueError:
            print("That is not a valid input. Please try again")
            continue

    if total_contributions >= 5000:
        life_insurance_relief = 0
    elif total_contributions < 5000 and insurance_premium_paid_status.upper()[0] == 'Y':
        life_insurance_relief = round(min(5000-total_contributions,min(0.07 * insured_value,insurance_premium_paid)))

    life_insurance_relief = round(life_insurance_relief)
    return life_insurance_relief

################################################################################################################ 

def find_course_fees_relief():


    flag1 = True
    flag2 = True

    while flag1:
        course_fee_status = input("Have you attended any course of study, seminar or conference in 2021 for the (a) purpose of gaining an approved academic, professional or vocational* qualification or (b) relevant to your current employment, trade, business, profession or vocation or (c) any course, seminar or conference between 1 Jan 2019 to 31 Dec 2020 that is relevant to your new employment, trade, business, profession or vocation in 2021. (Y/N)  ")
        if course_fee_status.upper()[0] == 'Y':
            flag2 = True
            flag1 = False
        elif course_fee_status.upper()[0] == 'N':
            flag2 = False
            flag1 = False
            course_fee_incurred = 0
        else:
            print("That is not a valid input. Please enter either Y or N")
            continue

        
    while flag2:
        course_fee_incurred = input("How much actual course fees have you incurred by yourself. Any amount paid or reimbursed by your employer or any other organisations (including the use of SkillsFuture Credit) cannot be claimed as Course Fees Relief. ")
        try:
            course_fee_incurred = int(course_fee_incurred)
            if course_fee_incurred < 0:
                print("That is not a valid input. Please enter either Y or N")
                continue
            else:
                flag2 = False                       
        except ValueError:
            print("That is not a valid input. Please enter either Y or N")
            continue

    if course_fee_incurred > 5500:
        course_fees_relief = 5500
    elif course_fee_incurred < 5500:
        course_fees_relief = course_fee_incurred

    course_fees_relief = round(course_fees_relief)
    return course_fees_relief

################################################################################################################ 

def find_cpf_cash_topup_relief():


    flag1 = True #Ask if user made ANY top-ups
    flag2 = None #Ask if user made top-ups to self
    flag3 = None #Ask if user made top-ups to parents/parent-in-law/Grandparents/Grandparents-in-law/Handicapped spouse/Handicapped siblings
    flag4 = None #Ask if user made top-ups to non-handicapped spouse or non-handicapped siblings

    while flag1:
        cpf_cash_topup_status = input("Have you made cash topups under the CPF Retirement Sum Topping-up Scheme? (Y/N)")
        if cpf_cash_topup_status.upper()[0] == 'Y':
            cpf_cash_topup_status = True
            flag2 = True
            flag1 = False
        elif cpf_cash_topup_status.upper()[0] == 'N':
            cpf_cash_topup_status = False
            cpf_self_cash_topup = 0
            cpf_parents_grandparents_handicappedspouse_handicappedsiblings_cash_topup = 0
            cpf_nonhandicappedspouse_nonhandicappedsiblings_cash_topup = 0
            flag2 = False
            flag1 = False
        else:
            print("That is not a valid input. Please try again")
            continue
    
    while flag2:
        cpf_self_cash_topup = input("How much cash top-ups have you made to self? (rounded to whole number) Enter 0 if you did not make top-ups to self")
        try:
            cpf_self_cash_topup = int(cpf_self_cash_topup)
            if cpf_self_cash_topup < 0:
                print("That is not a valid input. Please try again")
                continue
            else:
                flag3 = True
                flag2 = False
        except ValueError:
            print("That is not a valid input. Please try again")
            continue

    while flag3:
        cpf_parents_grandparents_handicappedspouse_handicappedsiblings_cash_topup = input("How much cash top-ups have you made to parents/parent-in-law/Grandparents/Grandparents-in-law/Handicapped spouse/Handicapped siblings? (rounded to whole number) Enter 0 if you did not make top-ups to these family members")
        try:
            cpf_parents_grandparents_handicappedspouse_handicappedsiblings_cash_topup = int(cpf_parents_grandparents_handicappedspouse_handicappedsiblings_cash_topup)
            if cpf_parents_grandparents_handicappedspouse_handicappedsiblings_cash_topup < 0:
                print("That is not a valid input. Please try again")
                continue
            else:
                flag4 = True
                flag3 = False
        except ValueError:
            print("That is not a valid input. Please try again")
            continue

    while flag4:
        cpf_nonhandicappedspouse_nonhandicappedsiblings_cash_topup = input("If you have a nonhandicapped spouse/siblings with annual income less than $4000, how much cash top-ups have you made to these family members. Enter 0 if you did not make top-ups to these family members or if their annual income is more than $4000")
        try:
            cpf_nonhandicappedspouse_nonhandicappedsiblings_cash_topup = int(cpf_nonhandicappedspouse_nonhandicappedsiblings_cash_topup)
            if cpf_nonhandicappedspouse_nonhandicappedsiblings_cash_topup < 0:
                print("That is not a valid input. Please try again")
                continue
            else:
                flag4 = False    
        except ValueError:
            print("That is not a valid input. Please try again")
            continue


    if cpf_self_cash_topup > 7000:
        cpf_self_cash_topup = 7000 #maximum 7000 for self
    elif cpf_self_cash_topup <= 7000:
        pass

    if cpf_parents_grandparents_handicappedspouse_handicappedsiblings_cash_topup + cpf_nonhandicappedspouse_nonhandicappedsiblings_cash_topup > 7000:
        cpf_others_cash_topup = 7000 #maximum 7000 for family members
    elif cpf_parents_grandparents_handicappedspouse_handicappedsiblings_cash_topup + cpf_nonhandicappedspouse_nonhandicappedsiblings_cash_topup <= 7000:
        cpf_others_cash_topup = cpf_parents_grandparents_handicappedspouse_handicappedsiblings_cash_topup + cpf_nonhandicappedspouse_nonhandicappedsiblings_cash_topup

    cpf_cash_topup_relief = cpf_self_cash_topup + cpf_others_cash_topup

    cpf_cash_topup_relief = round(cpf_cash_topup_relief)
    return cpf_cash_topup_relief

################################################################################################################ 

def find_srs_relief():


    flag1 = True #Ask user if there is SRS account
    flag2 = None #Ask for amount contributed by user or by user's employer (on behalf of user)


    while flag1:
        srs_account_status = input("Do you have an Supplementary Retirement Scheme (SRS) account? (Y/N)")
        if srs_account_status.upper()[0] == "Y":
            srs_account_status = True
            flag2 = True
            flag1 = False
        elif srs_account_status.upper()[0] == "N":
            srs_account_status = False
            srs_relief = 0
            srs_contribution = 0
            flag2 = False
            flag1 = False
            return 0
        else:
            print("That is not a valid input. Please try again")
            continue



    while flag2:
        srs_contribution = input("How much have you and/or your employer (on your behalf) contributed in the year? (rounded to whole number) ")
        try:
            srs_contribution = int(srs_contribution)
            if srs_contribution < 0:
                print("That is not a valid input. Please try again")
                continue
            else:
                flag2 = False
        except ValueError:
            print("That is not a valid input. Please try again")
            continue


    if user_data[6] == True:
        srs_capped = 15300
    elif user_data[6] == False:
        srs_capped = 35700
    else:
        srs_capped = 0 

    if srs_contribution < srs_capped:
        srs_relief = srs_contribution
    else:
        srs_relief = srs_capped

    srs_relief = round(srs_relief)
    return srs_relief

################################################################################################################ 

def find_ns_relief():


    flag1 = True #Ask user for NS self relief
    flag2 = None #Ask user for NS parent/wife relief
    flag3 = None #Ask NS self eligible user about whether user performed NS activities in the preceding year
    flag4 = None #Ask NS self eligible user about whether user is a key command and staff appointment holder


    while flag1:   
        ns_self_status = input("Have you completed full-time National Service? (Y/N)")
        if ns_self_status.upper()[0] == 'Y':
            ns_self_status = True
            flag2 = True
            flag3 = True
            flag4 = True
            flag1 = False
        elif ns_self_status.upper()[0] == 'N':
            ns_self_status = False
            flag2 = True
            flag3 = False
            flag4 = False
            flag1 = False
        else:
            print("That is not a valid input. Please try again")
            continue



    while flag2:
        ns_wife_parent_status = input("Do you have a husband/child who is eligible for NSman Self Relief? (Y/N)")
        if ns_wife_parent_status.upper()[0] == 'Y':
            ns_wife_parent_status = True
            flag2 = False
        elif ns_wife_parent_status.upper()[0] == 'N':
            ns_wife_parent_status = False
            flag2 = False
        else:
            print("That is not a valid input. Please try again")
            continue

    while flag3:
        ns_activities_status = input("Did you perform NS activities in the preceding year? (Y/N)")
        if ns_activities_status.upper()[0] == 'Y':
            ns_activities_status = True
            flag3 = False
        elif ns_activities_status.upper()[0] == 'N':
            ns_activities_status = False
            flag3 = False
        else:
            print("That is not a valid input. Please try again")
            continue
        
    while flag4:
        ns_appointment_holder_status = input("Are you a NS key command and staff appointment holder? (Y/N)")
        if ns_appointment_holder_status.upper()[0] == 'Y':
            ns_appointment_holder_status = True
            flag4 = False
        elif ns_appointment_holder_status.upper()[0] == 'N':
            ns_appointment_holder_status = False
            flag4 = False
        else:
            print("That is not a valid input. Please try again")
            continue

    if ns_self_status == False and ns_wife_parent_status == True: #User only eligible for NS wife/parent relief
        ns_man_relief = 750
    elif ns_self_status == False and ns_wife_parent_status == False: #User not eligible for any NS relief
        ns_man_relief = 0
    
    #User is eligible for NS (self) relief
    if ns_self_status == True and ns_activities_status == True and ns_appointment_holder_status == True:
        ns_man_relief = 5000
    elif ns_self_status == True and ns_activities_status == True and ns_appointment_holder_status == False:
        ns_man_relief = 3000
    elif ns_self_status == True and ns_activities_status == False and ns_appointment_holder_status == True:
        ns_man_relief = 3500
    elif ns_self_status == True and ns_activities_status == False and ns_appointment_holder_status == False:
        ns_man_relief = 1500

    #If user if eligible for both NS(self) and NS(wife/parent) relief, take the one that is higher
    if ns_self_status == True and ns_wife_parent_status == True:
        ns_man_relief = max(ns_man_relief,750)

    ns_man_relief = round(ns_man_relief)
    return ns_man_relief

################################################################################################################

def find_parenthood_tax_rebate(tax_payable_on_chargeable_income):


    while True:
        unutilised_parenthood_tax_rebate = input("How much unutilised Parenthood Tax Rebate do you have? Enter 0 if you do not have any untilised PTR or are not eligible for PTR")
        try:
            unutilised_parenthood_tax_rebate = int(unutilised_parenthood_tax_rebate)
            if unutilised_parenthood_tax_rebate < 0:
                print("That is not a valid input. Please try again")
                continue
            else:
                break
        except ValueError:
            print("That is not a valid input. Please try again")
            continue
    
    #amount of parenthood tax rebate used cannot be more than the tax payable
    if unutilised_parenthood_tax_rebate > tax_payable_on_chargeable_income:
        parenthood_tax_rebate = tax_payable_on_chargeable_income
    elif unutilised_parenthood_tax_rebate <= tax_payable_on_chargeable_income:
        parenthood_tax_rebate = unutilised_parenthood_tax_rebate

    parenthood_tax_rebate = round(parenthood_tax_rebate)
    return parenthood_tax_rebate

################################################################################################################

