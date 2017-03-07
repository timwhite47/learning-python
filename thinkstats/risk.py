import first
import Pmf

def IsOnTime(prglength):
    return prglength in [38, 39, 40]

def IsLate(prglength):
    return prglength > 40

def IsEarly(prglength):
    return prglength < 38

def PregnancyValue(record):
    prglength = record.prglength
    if IsOnTime(prglength):
        return 1
    elif IsEarly(prglength):
        return 0
    elif IsLate(prglength):
        return 2
    print prglength

def ProbLate(pmf):
    return pmf.Prob(2)

def ProbEarly(pmf):
    return pmf.Prob(0)

def ProbOnTime(pmf):
    return pmf.Prob(1)


f = first.FirstChildren()
o = first.OtherChildren()
l = first.LiveBirths()

first_pmf = Pmf.MakePmfFromList(map(lambda x: PregnancyValue(x), f))
other_pmf = Pmf.MakePmfFromList(map(lambda x: PregnancyValue(x), o))
live_pmf = Pmf.MakePmfFromList(map(lambda x: PregnancyValue(x), l))

for name, pmf in [("First", first_pmf),("Other", other_pmf),("All Live Births", live_pmf)]:
    print name
    print ProbEarly(pmf)
    print ProbOnTime(pmf)
    print ProbLate(pmf)
    print
