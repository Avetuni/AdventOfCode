cal_list = open('input.txt').read().split()

alphabet = []
for letters in 'abcdefghijklmnopqrstuvwxyz':
    alphabet.append(letters)

digits = {'one' : 'o1ne', 'two' : 't2wo', 'three' : 'th3ree',
'four' : 'fo4ur', 'five' : 'fi5ve', 'six' : 's6ix',
'seven' : 'se7ven', 'eight' : 'eig8ht', 'nine' : 'ni9ne'}

for x in range(len(cal_list)):
    for dig in digits:
        cal_list[x] = cal_list[x].replace(dig, digits[dig])
    for char in alphabet:
        cal_list[x] = cal_list[x].replace(char, '')

numerical_list = []

for x in range(len(cal_list)):
    numerical_list.append(int(cal_list[x][0] + cal_list[x][-1]))

print(sum(numerical_list))