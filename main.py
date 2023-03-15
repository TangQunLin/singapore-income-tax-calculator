
#import functions that gathers basic user info
from all_function_definitions import find_user_details

#import functions that is used to calculate assessable income
from all_function_definitions import find_net_employment_income 
from all_function_definitions import find_trade_income
from all_function_definitions import find_other_income # run regardless of employment status
from all_function_definitions import find_approved_donations #run regardless of employment status


#user_data = [name,gender,age,marital_status,children_count,employment_status,citizenship_status]
user_data = find_user_details()


if user_data[5] =='E': #user is employed
    results_employment = find_net_employment_income()
    net_employment_income = results_employment[1]
    employment_income = results_employment[0]
    other_income = find_other_income()
    approved_donations = find_approved_donations()
    trade_income = 0
    assessable_income = net_employment_income + trade_income + other_income - approved_donations
elif user_data[5] == 'S': #user is self-employed
    trade_income = find_trade_income()
    other_income = find_other_income()
    approved_donations = find_approved_donations()
    net_employment_income = 0
    employment_income = 0
    assessable_income = net_employment_income + trade_income + other_income - approved_donations
elif user_data[5] == 'D': #user is both employed and self-employed
    results_employment = find_net_employment_income()
    net_employment_income = results_employment[1]
    employment_income = results_employment[0]
    trade_income = find_trade_income()
    other_income = find_other_income()
    approved_donations = find_approved_donations()
    assessable_income = net_employment_income + trade_income + other_income - approved_donations
else: #user is unemployed
    other_income = find_other_income()
    approved_donations = find_approved_donations()
    net_employment_income = 0
    employment_income = 0
    trade_income = 0
    assessable_income = net_employment_income + trade_income + other_income - approved_donations

#ensure assessable income is not negative
if assessable_income < 0:
    assessable_income = 0
else:
    pass


#for personal reliefs
#import functions that run depending on user_data information
from all_function_definitions import find_earned_income_relief
from all_function_definitions import find_spouse_handicapped_relief
from all_function_definitions import find_qualifying_handicapped_child_relief
from all_function_definitions import find_grandparent_caregiver_relief
from all_function_definitions import find_working_mother_child_relief
from all_function_definitions import find_foreign_domestic_worker_levy_relief

#for personal reliefs
#import functions that run regardless of user_data information
from all_function_definitions import find_parent_handicapped_parent_relief
from all_function_definitions import find_handicapped_brother_sister_relief
from all_function_definitions import find_cpf_relief_cap
from all_function_definitions import find_course_fees_relief
from all_function_definitions import find_cpf_cash_topup_relief
from all_function_definitions import find_srs_relief
from all_function_definitions import find_ns_relief

#for personal reliefs
#import function that depends on CPF for input
from all_function_definitions import find_life_insurance_relief



#user is not unemployed
if user_data[5] in ['E','S','D']:
    earned_income_relief = find_earned_income_relief(net_employment_income,trade_income)
else:
    earned_income_relief = 0

#user has a spouse
if user_data[3] in ['M','SP']:
    spouse_handicapped_relief = find_spouse_handicapped_relief()
else:
    spouse_handicapped_relief = 0

#user has children
if user_data[4] > 0:
    results_child = find_qualifying_handicapped_child_relief()
    total_relief_available_under_qcr_hcr = results_child[0]
    child_order = results_child[1]
else:
    total_relief_available_under_qcr_hcr = 0

#user is a working mother who is either married/widowed/separated
if user_data[1] == 'F' and user_data[3] != 'S' and user_data[4] > 0:
    grandparent_caregiver_relief = find_grandparent_caregiver_relief()
else:
    grandparent_caregiver_relief = 0 

#user is a working mother who is either married/widowed/separated and has children claimable under QCR
if user_data[1] == 'F' and user_data[3] != 'S' and total_relief_available_under_qcr_hcr > 0:
    working_mother_child_relief = find_working_mother_child_relief(child_order,net_employment_income, trade_income)
else:
    working_mother_child_relief = 0

#user is a married female or has children claimable under QCR (if not married)
if user_data[1] == 'F' and (user_data[3] == 'M' or (user_data[3] in ['D','W','SP'] and total_relief_available_under_qcr_hcr > 0)):
    foreign_domestic_worker_levy_relief = find_foreign_domestic_worker_levy_relief()
else:
    foreign_domestic_worker_levy_relief = 0


#run for all users regardless of status
total_relief_available_under_phpr = find_parent_handicapped_parent_relief()
handicapped_brother_sister_relief = find_handicapped_brother_sister_relief()
cpf_relief = find_cpf_relief_cap(employment_income, trade_income)
course_fees_relief = find_course_fees_relief()
cpf_cash_topup_relief = find_cpf_cash_topup_relief()
srs_relief = find_srs_relief()
ns_man_relief = find_ns_relief()

#this relief relies on output from CPF relief, so it must run AFTERWARDS
if user_data[5] in ['E','S','D']:
    life_insurance_relief = find_life_insurance_relief()
else:
    life_insurance_relief = 0


#sum up all personal reliefs (14 in total)
personal_reliefs = (earned_income_relief
                    +spouse_handicapped_relief
                    +total_relief_available_under_qcr_hcr
                    +working_mother_child_relief
                    +total_relief_available_under_phpr
                    +grandparent_caregiver_relief
                    +handicapped_brother_sister_relief
                    +cpf_relief
                    +life_insurance_relief
                    +course_fees_relief
                    +foreign_domestic_worker_levy_relief
                    +cpf_cash_topup_relief
                    +srs_relief
                    +ns_man_relief)

#personal reliefs capped at $80,000
if personal_reliefs < 0:
    personal_reliefs = 0
elif personal_reliefs > 80000:
    personal_reliefs = 80000

#rounding to whole number
personal_reliefs = round(personal_reliefs)

#compute chargeable income which cannot be less than 0
chargeable_income = max(0,assessable_income - personal_reliefs)

#apply tax rates on chargeable income
if chargeable_income <= 20000:
    tax_payable_on_chargeable_income = 0
elif chargeable_income > 20000 and chargeable_income <= 30000:
    tax_payable_on_chargeable_income = (chargeable_income - 20000) * 0.02
elif chargeable_income > 30000 and chargeable_income <= 40000:
    tax_payable_on_chargeable_income = 200 + (chargeable_income - 30000) * 0.035
elif chargeable_income > 40000 and chargeable_income <= 80000:
    tax_payable_on_chargeable_income = 550 + (chargeable_income - 40000) * 0.07
elif chargeable_income > 80000 and chargeable_income <= 120000:
    tax_payable_on_chargeable_income = 3350 + (chargeable_income-80000) * 0.115
elif chargeable_income > 120000 and chargeable_income <= 160000:
    tax_payable_on_chargeable_income = 7950 + (chargeable_income - 120000) * 0.15
elif chargeable_income > 160000 and chargeable_income <= 200000:
    tax_payable_on_chargeable_income = 13950 + (chargeable_income - 160000) * 0.18
elif chargeable_income > 200000 and chargeable_income <= 240000:
    tax_payable_on_chargeable_income = 21150 + (chargeable_income - 200000) * 0.19
elif chargeable_income > 240000 and chargeable_income <= 280000:
    tax_payable_on_chargeable_income = 28750 + (chargeable_income - 240000) * 0.195
elif chargeable_income > 280000 and chargeable_income <= 320000:
    tax_payable_on_chargeable_income = 36550 + (chargeable_income - 280000) * 0.2
elif chargeable_income > 320000:
    tax_payable_on_chargeable_income = 44550 + (chargeable_income - 320000) * 0.22

#rounding to 2dp
tax_payable_on_chargeable_income = round(tax_payable_on_chargeable_income,2)

#import function for parenthood tax rebate
from all_function_definitions import find_parenthood_tax_rebate

parenthood_tax_rebate = find_parenthood_tax_rebate(tax_payable_on_chargeable_income)

#compute net tax payable
net_tax_payable = tax_payable_on_chargeable_income - parenthood_tax_rebate

#ensure net tax payable cannot be negative
if net_tax_payable < 0:
    net_tax_payable = 0

#rounding to 2dp
net_tax_payable = round(net_tax_payable,2)

#print full tax computation for user
print()
print()
print()
print()
print()
print()
print()
print()
print()
print(f"{user_data[0].upper()}'S PROFILE")
print("-------------------------------------------------------------------------------------------------")
print(f"Gender: {user_data[1]}")
print(f"Age: {user_data[2]}")
print(f"Marital status: {user_data[3]}")
print(f"Number of children: {user_data[4]}")
print(f"Employment status: {user_data[5]}")
print(f"Citizenship: {user_data[6]}")
print()
print()
print(f"TAX COMPUTATION FOR {user_data[0].upper()}")
print("-------------------------------------------------------------------------------------------------")
print()
print(f"Net employment income ___________________________________________ {net_employment_income}")
print(f"Trade income_____________________________________________________ {trade_income}")
print(f"Other income_____________________________________________________ {other_income}")
print()
print(f"Total income_____________________________________________________ {net_employment_income + trade_income + other_income}")
print()
print(f"Less: Approved Donations_________________________________________ ({approved_donations})")
print()
print(f"Assessable income________________________________________________ {assessable_income}")
print()
print("Less: Personal reliefs")
print(f"Earned Income Relief_____________________________________________({earned_income_relief})")
print(f"Spouse/Handicapped Spouse Relief_________________________________({spouse_handicapped_relief})")
print(f"Qualifying/Handicapped Child Relief______________________________({total_relief_available_under_qcr_hcr})")
print(f"Working Mother's Child Relief____________________________________({working_mother_child_relief})")
print(f"Parent/Handicapped Parent Relief_________________________________({total_relief_available_under_phpr})")
print(f"Grandparent Caregiver Relief_____________________________________({grandparent_caregiver_relief})")
print(f"Handicapped Brother/Sister Relief________________________________({handicapped_brother_sister_relief})")
print(f"CPF/Provident Fund Relief________________________________________({cpf_relief})")
print(f"Life Insurance Relief____________________________________________({life_insurance_relief})")
print(f"Course Fees Relief_______________________________________________({course_fees_relief})")
print(f"Foreign Domestic Worker Levy Relief______________________________({foreign_domestic_worker_levy_relief})")
print(f"CPF Cash Top-up Relief (Self,Dependant and Medisave account)_____({cpf_cash_topup_relief})")
print(f"Supplementary Retirement Scheme (SRS) Relief_____________________({srs_relief})")
print(f"NSman (Self/Wife/Parent) Relief__________________________________({ns_man_relief})")
print()
print(f"Total personal reliefs___________________________________________({personal_reliefs})")
print()
print(f"Chargeable income________________________________________________ {chargeable_income}")
print()
print(f"Tax payable on Chargeable Income_________________________________ {tax_payable_on_chargeable_income}")
print()
print(f"Less: Parenthood Tax Rebate______________________________________({parenthood_tax_rebate})")
print()
print(f"Net tax payable__________________________________________________ {net_tax_payable}")
print()
print()
print()
