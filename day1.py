with open('data.txt') as file:
    data = file.read()

nums = [int(num) for num in data.split('\n') if num != '']
diff = []

for num in nums:
    if num in diff:
        print( (2020-num)*num)
    else:
        diff.append(2020-num)
