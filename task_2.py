lst = []
var = ""
while var != "Поработали, и хватит":
    var = input()
    lst.append(var)
    if var == "Поработали, и хватит":
        break
for v in lst[-1]:
    print(lst)

def check_variable(v):
    if str(v).isdigit():
        print("Ошибка")
check_variable(v)