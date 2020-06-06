name = 'tome'
def fun():
    global name
    name = "jerry"
    print(f"fun={name}")

print(name)
fun()