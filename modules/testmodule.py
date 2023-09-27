import modules.mymodule as mx
import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)

y = dir(mx)
print(y)

mx.greeting("Mariana")

a = mx.person1["age"]
print("Age person1: ", a)