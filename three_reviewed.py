digits = input('Enter digits separated by a comma ')
numbers = [float(i) for i in digits.split(",")]
result = max([a * b for a, b in zip(numbers, numbers[1:])])
print(f'maximum is {result}')
