#decorators function always accept a function
#decorators has an inner function

def shuffle_value(func):
    def wrapper(no1,no2):
        if (no1<no2):
            (no1,no2)=(no2,no1)
        return func (no1,no2)
    return wrapper()

@shuffle_value
def div (num1,num2):
    return num1/num2


@shuffle_value
def sub(num1,num2):
    return num1-num2
