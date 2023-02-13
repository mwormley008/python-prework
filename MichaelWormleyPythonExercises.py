# Question 1
def hello_name(user_name):  
    print(f"hello_{user_name.upper()}!")

hello_name("Worm") 

# Question 2
def first_odds():
    for i in range(1,100,2):
        print(i)

first_odds()

# Question 3
def max_num_in_list(a_list):
    print(max(a_list))
    return max(a_list)

#max_num_in_list([1,2,3])

# Question 4
def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

#print(is_leap_year(500))       

# Question 5
def is_consecutive(a_list):
    if sorted(a_list) == a_list:
        for i in range(1, len(a_list)):
            if a_list[i] == a_list[i-1] + 1:
                continue
            else:
                return False
        return True
print(is_consecutive([1,2,3]))
print(is_consecutive([1,3]))