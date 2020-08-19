#!/usr/bin/python
import sys


# input user and the resource they asked
num_res = input("Please input the num of resource: ")
num_user = input("Please input the num of users: ")
print("Input the resource they need: ")
u_resource = []
for u in range(int(num_user)):
    row = sys.stdin.readline().strip()
    if row == '':
        break
    row_list = list(map(int, row.split(",")))
    u_resource.append(row_list)
# input machined and their resource
num_mach = input("Please input the num of machines: ")
print("Input the resource they have on each machine: ")
m_resource = []
for m in range(int(num_mach)):
    row = sys.stdin.readline().strip()
    if row == '':
        break
    row_list = list(map(int, row.split(",")))
    m_resource.append(row_list)

#input their relationship
print("Input the relationship (user, machine): ")
relationship = []
while True:
    row = sys.stdin.readline().strip()
    if row == '':
        break
    row_list = list(map(int, row.split(",")))
    relationship.append(row_list)

flag = int(num_user)
result = [0 for i in range(int(num_user))]
while flag > 0:
    flag -= 1
    total_task = []
    total = [0 for i in range(int(num_user))]
    for u in range(int(num_user)):
        tasks = []
        for m in range(int(num_mach)):
            min_task = 100
            min_mach = 0
            for r in range(int(num_res)):
                if u_resource[u][r] != 0:
                    t = m_resource[m][r] / u_resource[u][r]
                if min_task > t:
                    min_task = t
                    min_mach = m
            tasks.append(min_task)
            total[u] += min_task
        total_task.append(tasks)
#    print(total_task)
#    print("total = ", total)


    share = [0 for i in range(int(num_user))]
    for u,m in relationship:
        share[u-1] += total_task[u-1][m-1]
    task_share1 = [(share[u]/total[u]) for u in range(int(num_user))]

    for u in range(int(num_user)):
        if task_share1[u] == 0:
            task_share1[u] = 100
    print("share", share)
    print(task_share1)

    min_share_user = task_share1.index(min(task_share1))
    result[min_share_user] = share[min_share_user]
    print("result", result)
    
    #########################
    min_share_user += 1                 # change from index to user number
    for user,mach in relationship:
        if user == min_share_user:
            relationship.remove([user,mach])
            ma = mach
    for user,mach in relationship:
        if mach == ma:
            relationship.remove([user,mach])
    m_resource[ma - 1] = [0 for i in range(int(num_res))]
    u_resource[min_share_user - 1] = [0 for i in range(int(num_res))]


