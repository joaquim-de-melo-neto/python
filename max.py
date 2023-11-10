# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def max(n1:int, n2:int):
    # Use a breakpoint in the code line below to debug your script.
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return 'sao iguais'


# Press the green button in the gutter to run the script.

n1 = input('digite o primeiro numero ')
n2 = input('digite o segundo numero ')
print(max(n1, n2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
