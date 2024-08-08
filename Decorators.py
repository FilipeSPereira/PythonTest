def announce (f):
    def wrapper():
        print(f"About to run the function...")
        f()
        print(f"Done with th function.")
    return wrapper
    
@announce
def hello():
        print("Hello, world!")

hello()
