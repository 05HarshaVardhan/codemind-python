x, y, z = [float(s) for s in input().split()]

a = x*((1+y/100)**z)
print("%.2f"%a)