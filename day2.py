with open('day2_data.txt') as file:
    data = file.read()

rows = [row for row in data.split('\n') if row != '']

total = 0

for row in rows:
    key, pw = row.split(':')
    key_range, key_value = key.split(' ')
    key_min, key_max = [int(val) for val in key_range.split('-')]
    tot = pw.count(key_value)
    if key_min <= tot <= key_max:
        total += 1
print(total)
