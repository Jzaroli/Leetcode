nums = [1, 4, 9, 3, 20, 41, 6, 7, 8]
target = 1000
flag = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f'{nums[i]} + {nums[j]} make up the {target}')
        elif nums[i] + nums[j] != target and not flag:
            print('target was not found')
            flag = True
