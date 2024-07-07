import random
import string
name=input("Enter the name of the user: ")
print(name)
length_of_password=int(input("Enter the desired length of the password: "))
upper_case_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case_letters="abcdefghijkuplmnopqrstuvwxyz"
numerical_values="0123456789"
symbols="!#$%^&*()_+{}[]"
combine=lower_case_letters+upper_case_letters+numerical_values+symbols
print(length_of_password)
user_password="".join(random.sample(combine,length_of_password))
print(user_password)