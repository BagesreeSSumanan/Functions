
def factorial(num):
    factorial = 1
    for i in range(2,num+1):
        factorial *= i
    print("factorial of number",num , "is",factorial)


def powerOfnumber(num, power):
    if power == 0:
        return 1   
    else:
        return num * powerOfnumber(num, power - 1) 

def student_data(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

   
factorial(5)
print("3 ^ 2 is", powerOfnumber(3, 2))
student_data(student_id=1,student_name="Hari",student_class ="10th",student_avgMark="98")

