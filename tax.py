

def calculate_tax(salaries):
    employee_salaries=[]
    
    for salary in salaries:
        

        employee_salary=0
        if salary <=5000:
            employee_salary +=salary
        elif salary <=12000:
            employee_salary +=5000
            salary -=5000
            tax_five_percent= salary * 5/100
            salary -=tax_five_percent
            employee_salary +=salary
        elif salary <=100000:
            employee_salary +=5000
            salary -=5000
            tax_five_percent= 7000 * 5/100
            employee_salary +=7000 - tax_five_percent
            salary -=7000
            tax_ten_percent= salary * 10/100
            employee_salary +=salary - tax_ten_percent
        else:
            employee_salary +=5000
            salary -=5000
            tax_five_percent= 7000 * 5/100
            employee_salary +=7000 - tax_five_percent
            salary -=7000
            tax_ten_percent= 88000 * 10/100
            employee_salary +=88000 - tax_ten_percent
            salary -=88000
            tax_twenty_percent= salary * 20/100
            employee_salary +=salary - tax_twenty_percent
        employee_salary=int(employee_salary) if employee_salary.is_integer() else employee_salary
        employee_salaries.append(employee_salary)
    return employee_salaries






def main():
    t=int(input())
    for _ in range(t):
        N=int(input())
        salaries=[]
        for i in range(N):
            salaries.append(int(input()))
        employee_salaries=calculate_tax(salaries)
        for salary in employee_salaries:
            print(salary)


if __name__ =="__main__":
    main()