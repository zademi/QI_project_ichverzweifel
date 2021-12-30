import math as m

#define all variables, ec = e_cor and es = e_sec
ec = es = m.pow(10, (-6))
QX = 0.053
QZ = 0.047

#define all the functions
def l(n):
    return n * (1 - h(QX + mu(n))) - leak(n) - m.log((2/(pow(es, 2) * ec)), 2)

def mu(n):
    return m.sqrt(((2 * (n + 1))/(pow(n, 2))) * m.log((4/es)))

def h(x):
    return -x * m.log(x, 2) - (1 - x) * m.log((1 - x), 2)

def leak(n):
    return n * h(QZ) + 7.747 * m.sqrt(n) * m.sqrt(m.log((8/ec**2), 2)) + m.log((2 + (8/ec**2)), 2) + m.log((1/ec), 2)

#start with inital guess n=10000, because starting with n=1 gives negative roots and leads two different datatypes (float and complex)
n = 10000

#with the while loop the n is being incremented by 1 if the the length l(n) is smaller or equal to 0
#once we reach l(n) equal to 0, n is being incremented one last time and then the solution is printed.
#The smallest n for which the key length l(n) is positive is n=28515
while l(n) <= 0:
    n += 1

print(n)
