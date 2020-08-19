#!/usr/bin/python
import sys
import numpy as np

# input user and the resource
num_user = input("Please input the num of users: ")
num_res = input("Please input the num of resource: ")
print("Resources owned by the system: ")
total_resource = []
res = input()
data = res.replace(" ", "")
input_list = data.split(",")
total_resource = list(map(int, input_list))
#print(sys_res)
u_resource = []
print("Input the resource they need: ")
for u in range(int(num_user)):
    row = sys.stdin.readline().strip()
    if row == '':
        break
    row_list = list(map(int, row.split(",")))
    u_resource.append(row_list)
#print(u_resource)


# Find dominant resource
dom_res = []
for u in range(int(num_user)):
    max = 0
    for r in range(int(num_res)):
        dr = float(u_resource[u][r] / total_resource[r])
        if dr >= max:
            max = dr
    dom_res.append(max)
#print(dom_res)


# compute resource allocation
domain_equ = []
if len(dom_res) == 2:              
    domain_equ.append(dom_res[0])
    domain_equ.append(-dom_res[1])
#print(domain_equ)
equation = []
right = []
for r in range(int(num_res)):
    temp_equ = []
    data = []
    for u in range(int(num_user)):
        temp_equ.append(u_resource[u][r])
    equation.append(temp_equ)
    data.append(total_resource[r])
    data.append(0)
    right.append(data)
#equation.append(domain_equ)
#print(equation)
#print(right)
y = []
for r in range(int(num_res)):
    temp = []
    temp.append(equation[r])
    temp.append(domain_equ)
    A = np.array(temp)
    b = np.array(right[r])
    #print(temp)
    #print(right[r])
    x = np.linalg.solve(A,b)
    lis = x.tolist()
    y.append(lis)
print("the tasks allocated to each user are:", min(y))
