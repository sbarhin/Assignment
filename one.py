string = input("Enter to preferred string: ")


def compare_string(string):
    if string == string[::-1]:
        return True
    else:
        return False


# def compare_string(string):
#     return string == string[::-1]

print(compare_string(string))
