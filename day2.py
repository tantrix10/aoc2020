with open('data.txt') as file:
    data = file.read()

nums = [int(num) for num in data.split('\n') if num != '']

while nums:
    tot = 2020 - nums.pop()
    diff = []
    for num in nums:
        if num in diff:
            print((2020-tot)+(tot-num)+num,(2020-tot)*(tot-num)*num)
            break
        else:
            diff.append((tot-num))

