import pylab

a, b = -2*pylab.pi, 2*pylab.pi
n = 101
dx = (b-a)/(n-1)

xs = [a + i * dx for i in range(n) ]
ys1 = [ pylab.sin(x) for x in xs ]
ys2 = [ pylab.cos(x) for x in xs ]

pylab.plot(xs,ys1)
pylab.plot(xs,ys2)

pylab.show()