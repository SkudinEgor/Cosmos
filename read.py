def myread(f):
    c = open("username.txt", "r")
    v = c.readlines()
    for r in range(len(v)):
        if v[r] == F"{f}\n":
            return True
    return False

def myadd(j):
    a = open("username.txt", "a")
    b = a.write(F"{j}\n")
