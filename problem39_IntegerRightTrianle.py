# Euler Problem 39:
# If p is the perimeter of a right triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.
#
#    {20,48,52}, {24, 45, 51}, {30,40,50}
#
# For which value of p <1000, is the number of solutions maximised?
#
# Solution:
# -------------------------------
# Iterate over perimeter values. A little analysis reveals that all perimiters
# of integral right triangles will be even. Next we can parameterize c = p-a-b
# and can rewrite the Pythagorean theorem as a^2+b^2=(p-a-b)^2. Expanding,
# simplifying and solving for b we obtain: b=\frac{p(p-2a)}{2(p-a)}. A last
# criteria we can use to limit the search space is a+b > c. With this we only
# need to investigate values of a up to \frac{p}{2+\sqrt{2}}


import time as T

def findMaxRightTriangles(maxP):
    st= T.time()
    maxTri = 0
    Perim = 0
    for p in range(maxP//4*2,maxP+1,2):
        tri=0
        for a in range(2,int(p/(2+2**.5))+1):
            if p*(p-2*a) % (2*(p-a)) == 0:
                tri += 1
                if tri > maxTri:
                    maxTri = tri
                    Perim = p
        tt= T.time() - st
    print "The perimeter that gives the max number of integral right triangles is:", Perim, "with", maxTri, "integral right triangle solutions"
    print "This program took:", tt, "seconds to run"

if __name__ == "__main__":
    import sys
    findMaxRightTriangles(int(sys.argv[1]))



