add = lambda x, y: x + y


result = add(3, 7)
print(result)

max_num = lambda nums: max(nums)


result = max_num([1, 5, 3, 9, 2])
print(result)

concat = lambda str1, str2: str1 + str2


result = concat('hello', 'world')
print(result)

starts_with_a = lambda word: word.lower().startswith('a')


result1 = starts_with_a('apple')
result2 = starts_with_a('banana')

print(result1)  
print(result2)  
