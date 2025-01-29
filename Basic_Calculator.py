def Answer(num1,num2,operation):
    ans=0
    match(operation):
        case '+':
            ans=num1+num2
        case '-':
            ans=num1-num2
        case '*':
            ans=num1*num2
        case '/':
            ans=num1/num2
    if ans==int(ans): return int(ans)
    else: return ans
def calculate():
    try:
        operations=['+','-','*','/']
        print(f">Please use the available operations as,\n{",".join(operations)}\nFor exiting the calculator , just enter exit")
        operation = input(f">Enter the operation:")
        num1=int(input(">Enter the first number:"))
        num2=int(input(">Enter the second number:"))
        while operation in operations:
            if num2==0:
                raise ZeroDivisionError
            elif operation not in operations:
                raise ValueError
            print(f">The answer is:{Answer(num1,num2,operation)}")
            operation = input(f">Enter the operation:")
            if operation.lower()=="exit": break
            num1=int(input(">Enter the first number:"))
            num2=int(input(">Enter the second number:"))
    except ValueError:
        print(">Please enter a valid number!!!")
    except:
        print(">Sorry an error occured.")

if __name__=="__main__":
    calculate()
