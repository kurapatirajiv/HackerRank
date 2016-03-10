# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle
import math

def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def dot(a, b):
    return sum([a[x]*b[x] for x in range(3)])
#Square root of sum of squares of individual items |X||Y| means integral Multiplication 
def mod(a):
    return sum([a[x]**2 for x in range(3)])**0.5

a, b, c, d = (list(map(float, input().split())) for _ in range(4))

ab = list([b[x]-a[x] for x in range(3)])
bc = list([c[x]-b[x] for x in range(3)])
cd = list([d[x]-c[x] for x in range(3)])

X = cross(ab, bc)
Y = cross(bc, cd)

cosPhi = dot(X,Y)/(mod(X)*mod(Y))
#Inverse is taken because the actual formula contains a negative sign
PhiRad = math.acos(cosPhi)
PhiDeg = math.degrees(PhiRad)

print(round(PhiDeg,2))