value = input("Enter your preferred list of numbers separated by a comma: ")
value_ = value.split(",")
# print(value_)


new = []
for i in value_:
    new.append(float(i))
# print(new)

# [1, 2, 3, 4, 5]
prods = []


def max_product(array):
    for index, item in enumerate(array):
        if index != len(new) - 1:
            product = item * array[index + 1]
            prods.append(product)
    return max(prods)


print(max_product(new))
