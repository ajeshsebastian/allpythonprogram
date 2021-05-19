def admin_required(func):
    def wrapper(use,pin1):
        if use!="admin":
            raise Exception ("yor are not allowed")
        else:
            return func (use ,pin1)
    return wrapper

@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin


def delete_account(user,acno):
    return str(acno)+"deleted"

print(change_pin ("admin",1000))