# Args and Kwargs


# args Section
# Returns the tuple
def add(*args):
    total =0
    for i in args:
        total +=i
    return total

print(add(1,3))
print(add(4,5,10))
print((add(3,5,12,5)))


# Section **kwargs
# Returns the Dictionary

def details(**kwargs):
    print(f"Following are the entered values: \nThis is the kwargs: {kwargs}")
    for key, values in kwargs.items():
        print(f"Key: {key} value: {values}")

details(name = "vicky", age =59, address = "XYX area 445340")

