count = input()

for i in range(int(count)):
    word = input()
    res_odd = ""
    res_even = ""
    for j in range(len(word)):
        if(j % 2 == 0):
            res_even += word[j]
        else:
            res_odd += word[j]
    print(res_even + " " + res_odd)