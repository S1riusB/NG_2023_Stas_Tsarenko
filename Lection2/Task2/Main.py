create_list = input("Enter your list: ")
finish_list = create_list.split()

def is_number(element):
    try:
        float(element)
        return True
    except ValueError:
        return False

numbers = [element for element in finish_list if is_number(element)]

print("Numbers in list:", numbers)