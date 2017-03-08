import Pmf

d = {
    7: 8,
    12: 8,
    17: 14,
    22: 4,
    27: 6,
    32: 12,
    37: 8,
    42: 3,
    47: 2
}

def UnbiasedPmf(pmf, invert=False):
    new_pmf = pmf.Copy()

    for x, p in pmf.Items():
        if invert:
            new_pmf.Mult(x, x)
        else:
            new_pmf.Mult(x, 1.0/x)

    new_pmf.Normalize()

    return new_pmf

def ClassSize():
    print "Class Sizes"

    print 

    pmf = Pmf.MakePmfFromDict(d)
    unbiased = UnbiasedPmf(pmf, True)
    biased = UnbiasedPmf(pmf)

    print "Unbiased"
    for x,p in unbiased.Items():
        print x,p

    print

    print "Biased"
    for x,p in biased.Items():
        print x,p

if __name__ == '__main__':
    ClassSize()
