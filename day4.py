with open('day4_data.txt', 'r') as dat:
    data = dat.read()

pas_secs = [row for row in data.split('\n\n') if row !='']
pas_lines = [row.split('\n') for row in pas_secs]
just_passes = []

comp = set(['byr', 'iyr','eyr', 'hgt','hcl','ecl','pid'])
total = 0
total_2 = 0
for row in pas_lines:
    temp = []
    for item in row:
        temp.extend(item.split(' '))
    try:
        temp.remove('')
    except:
        pass

    temp = {
        item.split(':')[0] : item.split(':')[1]
            for item in temp if item.split(':')[0] != 'cid'
    }
    if set(temp.keys()) == comp:
        total += 1

print(f"Part 1 answer: {total}")

