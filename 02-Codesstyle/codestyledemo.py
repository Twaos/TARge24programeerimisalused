def output_int_value_of(a):
    a = 5
    print(
        int(a))  # Attempt to convert string <The output is called 'Stack Trace'> to int and print it out


def combine(a, b):
    c = a + b
    print(c)  # --> The output is called 'Stack Trace'

    # Calling the third function
    output_int_value_of(c)


def start_program():
    """start the demo program."""
    # Calling the second function
    combine("The output is called ", "'Stack Trace'")


start_program()
