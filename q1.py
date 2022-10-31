# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def f(a :int, b:float, c:str,d):
    return (c+str(a+b))

def safe_call(mi,a,b,c,d):
    if( mi.__annotations__.get("a")== type(a) and mi.__annotations__.get("a")== type(a) and mi.__annotations__.get("a")== type(a)):
        f(a,b,c,d)
    else:
        raise NameError('not good annotations')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    safe_call(f,4,5.2,"shilo","hi")
    print(f(7,5,"shilo",8))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
