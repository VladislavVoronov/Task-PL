print('Путь к файлу:')
fn = input()

with open(fn, 'r') as f:
    nums = f.readlines()

numbers = [int(num) for num in nums]

numbers.sort()
median = len(numbers) // 2
result = 0

for i in numbers:
    result += abs(i - numbers[median])

print(result)
