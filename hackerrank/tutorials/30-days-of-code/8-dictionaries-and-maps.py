count = input()
data = {}

for i in range(int(count)):
    tmp = input().split(' ')
    data[tmp[0]] = tmp[1]
    
for i in range(int(count)):
    case = input()
    if case in data:
        print(case + '=' + data[case])
    else:
        print("Not found")