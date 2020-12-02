with open('day2_data.txt') as file:
    data = file.read()

rows = [row for row in data.split('\n') if row != '']

total = 0

for row in rows:
    key, pw = row.split(':')
    key_range, key_value = key.split(' ')
    key_min, key_max = [int(val) for val in key_range.split('-')]
    tot = pw.count(key_value)
    test1 = pw[key_min] == key_value
    test2 = pw[key_max] == key_value
    if (test1 ^ test2) and (test1 or test2):
        total += 1
print(total)
