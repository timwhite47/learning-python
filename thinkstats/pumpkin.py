import thinkstats
import math

class Pumpkin(object):
    def __init__(self, size):
        self.size = size

class Patch(object):
    def __init__(self, pumpkins):
        self.pumpkins = pumpkins

    def mean_size(self):
        return thinkstats.Mean(self.sizes())

    def size_variance(self):
        return thinkstats.Var(self.sizes())

    def sizes(self):
        return map(lambda pumpkin: pumpkin.size, self.pumpkins)

sizes = [1,1,1,3,3,591]
pumpkins = map(lambda size: Pumpkin(size), sizes)
patch = Patch(pumpkins)
mean= patch.mean_size()
var = patch.size_variance()

print "Mean Size"
print mean

print

print "Variance:"
print var

print

print "Standard Deviation"
print math.sqrt(var)
