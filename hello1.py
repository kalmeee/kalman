import sys

def hiname(name):
    print("Hello", name)

if len(sys.argv) > 1:
    name = sys.argv[1]
    hiname(name)
else: print("Hello World!")
