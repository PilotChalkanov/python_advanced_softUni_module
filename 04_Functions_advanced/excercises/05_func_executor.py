def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2
def func_executor(*args):
    list_output = []
    for func,func_arg in args:
        list_output.append(func(*func_arg))
    return list_output


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))