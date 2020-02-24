INPUT_String = eval(input())
Final = []


Flag = INPUT_String[0][-1]

Final.append(INPUT_String[0])

INPUT_String = INPUT_String[1:]


for j in INPUT_String:
    for i in INPUT_String :
        if Flag == i[0] and i not in Final :
            Final.append(i)
            Flag = i[-1]


print(Final)
