from math import *
print(" This program will solve a simultaneous equation with 2 variables ")
print("Equations should be in the form of:")
print("ax+by=c")
print("AND")
print("dx+ey=f")
print("Enter values of a, b and c when prompted below:")
var_a =input("Enter value of a :")
var_b =input("Enter value of b :")
var_c =input("Enter value of c :")
print("Enter values of d, e and f when prompted below:")
var_d =input("Enter value of d :")
var_e =input("Enter value of e :")
var_f =input("Enter value of f :")
var_a = float(var_a)
var_b = float(var_b)
var_c = float(var_c)
var_d = float(var_d)
var_e = float(var_e)
var_f = float(var_f)
ans_x = (((var_e*var_c)-(var_b*var_f))/((var_a*var_e)-(var_b*var_d)))
ans_y = (((var_d*var_c)-(var_a*var_f))/((var_d*var_b)-(var_e*var_a)))
print("x = " + str(int(ans_x)))
print("y = " + str(int(ans_y)))
print("\n\n\nGoodbye !!")
