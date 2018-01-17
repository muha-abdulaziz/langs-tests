admins = ("Ahmed", "Zaid")

def get():
    return admins[:]

print(get())

def check(name):
    s = get()[:]
    # if name in s:
    #     return True
    # return False
    if name in s:
        s.remove(name)
    return s

a = check("Ahmed")
print(a)

print(get())