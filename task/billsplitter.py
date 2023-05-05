import random

def input_positive_int():
    num = input()
    try:
        num = int(num)
    except TypeError:
        print()
        print('No one is joining for the party')
        exit()
    else:
        if num < 1:
            print()
            print('No one is joining for the party')
            exit()
        else:
            print()
            return num


print('Enter the number of friends joining (including you):')
num = input_positive_int()
people = {}
print('Enter the name of every friend (including you), each on a new line:')
for i in range(num):
    people[input()] = 0

print()
print('Enter the total bill value:')
bill = input_positive_int()

print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
want_lucky = input()
print()
if want_lucky == 'Yes':
    lucky_man = random.choice(list(people))
    print(lucky_man, 'is the lucky one!')
    num -= 1
else:
    print('No one is going to be lucky')
    lucky_man = ''

for name in people:
    if name != lucky_man:
        people[name] = round(bill / num, 2)

print()
print(people)
