# Given an integer "n" and an array "a" of length "n". apply the following
# array "a" mutates to array "b" of length n
# for each "i" from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1]
# if some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. for eg
# b[0] should be equal to 0 + a[0] + a[1]

# n = 5 a = [4, 0, 1, -2, 3]
# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = -2 + 3 + 0 = 1
# b = [4, 5, -1, 2, 1]
value_of_n = int(input("Enter your preferred number: "))
new = input("Input list of array with length same as n: ")
if value_of_n != len(new) or value_of_n > len(new):
    print("Length of a is not equal to value of n.")
    new = input("Input 'a' again: ")
new_ = new.split(",")
print(new_)

a = []
for i in new_:
    a.append(float(i))
print(a)


def mutate_array(array, length):
    b = []
    for index, item in enumerate(array):
        if index == 0:
            a_ = 0 + array[index] + array[index + 1]
            b.append(a_)

        elif index == length - 1:
            a_ = array[index - 1] + array[index] + 0
            b.append(a_)

        else:
            a_ = array[index - 1] + array[index] + array[index + 1]
            b.append(a_)

    return b


print(mutate_array(a, value_of_n))
