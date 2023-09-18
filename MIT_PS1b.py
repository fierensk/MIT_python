#gathering initial numbers for salary, down payment, and total cost
annual_salary = input("Enter your annual salary: ")
salary_savings = input("Enter the percent of your salary to save, as a decimal: ")
total_cost = input("Enter the cost of your dream home: ")

#doing calculations for current savings
portion_down_payment = .25
down_payment = float(total_cost) * portion_down_payment
current_savings = 0
r = 0.04
ROI = 0
months = 0
monthly_salary = float(annual_salary) / 12.0
monthly_salary_saved = monthly_salary * float(salary_savings)


while current_savings <= down_payment:
    #add monthly salary savings
    current_savings += monthly_salary_saved
    
    #mult by ROI
    ROI = current_savings * r / 12

    #add ROI to savings
    current_savings+= ROI

    #incremement months
    months+=1

print("Number of months:" + str(months))