import pylab

a, b = -2*pylab.pi, 2*pylab.pi #從-2pi到2pi
n = 100
dx = (b-a)/(n-1) #x軸增量

xs = [a + i * dx for i in range(n) ]
ys1 = [ pylab.sin(x) for x in xs ] #sin部份
ys2 = [ pylab.cos(x) for x in xs ] #cos部份

pylab.plot(xs,ys1, color=(0,1,0,0.5)) #x和y都是list，數量要搭配
pylab.plot(xs,ys2,color=(1,0,0,1))

pylab.title("my graph")
pylab.xlabel("x name")
pylab.ylabel("y name")
pylab.axis((-5,5,-2,2))

#pylab.axis('off')

pylab.show()