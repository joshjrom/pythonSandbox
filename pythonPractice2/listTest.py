alph = ["Stella", 1, 3, "Phone"]
alpha = ("Stella", 1, 3, "Phone")
days = ["Monday", "Tuesday", "Wednesday"]
months = ["January", "February", "March"]
years = [2020, 2021, 2022]

def something(arg):
    for i in arg:
        print(i)


def triple_list(a_list1, a_list2, a_list3):
    for i in a_list1:
        print(i)
    for i in a_list2:
        print(i)
    for i in a_list3:
        print(i)


def fouple_list(f_list1, f_list2, f_list3, f_list4):
    for item in f_list1:
        print(item[0])
    for item in f_list2:
        print(item[0])
    for item in f_list3:
        print(item[0])
    for item in f_list4:
        print(item[0])

fouple_list(days, days, days, days)
        
