def simple_generator(func):
    def wrapper(user):
        print("Something is happening before the function is being called!")
        result = func(user)
        print("Something has happened after the function has been called!")
        return result
        
    return wrapper



@simple_generator
def greeting(user):
    return f"Welcome: {user}"

result = greeting(input("Enter Username: "))
print(f"Result: {result}")