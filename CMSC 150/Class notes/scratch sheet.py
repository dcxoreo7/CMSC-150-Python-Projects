import arcade


def f(a,b):
    f = a + b
    return f()

if f(30,40) == 70:
    print("Passed")
else:
    print("Failed")

f(3889,798)