def validation1(func):
    def wrapper(name,age):
        #age=kwargs ["age"]
        #health=kwargs ["health_issues"]
        if age>60 :
            return func (age  )
        else:
            print("not allowed")
    return wrapper


@validation1
def vaccination_portal(name,age):
    print("request id allowed location ekm")
vaccination_portal ("ahesj",25)
#vaccination_portal (name="ram",age=25,address="address",health_issues=True )