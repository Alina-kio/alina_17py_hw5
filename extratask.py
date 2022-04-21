# ExtraTask:
# Дан массив целых чисел nums, отсортированных в порядке возрастания, и целое число target, напишите функцию для поиска target в nums. 
# Если target существует, верните его индекс. В противном случае возвращайтесь -1.



nums = [9,45,22,87,12,54,32,76,12]
nums.sort()
print(nums)
for i in nums:
    target = int(input('Enter num: '))
    if target in nums:
        print(nums.index(target))
    else:
        print(-1)