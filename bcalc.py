import string
def result(result):
    print("result:", result)
while True :



    Fnum = (input("Enter a number (or a letter to exit) :"))
    if Fnum.isalpha():
        break

    else:
        Fnum = int(Fnum)
        op = (input("Enter an operation    :"))
        Lnum = int(input("Enter another number    :"))
        print(Fnum,op,Lnum)
        if op == "+":
            result( Fnum + Lnum)
        elif op == "-":
            result(Fnum - Lnum)
        elif op == "*":
            result(Fnum * Lnum)
        elif op == "/":
            result(Fnum / Lnum)
