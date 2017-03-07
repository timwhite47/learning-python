import first
import Pmf
import risk
import matplotlib.pyplot as pyplot

l = filter(lambda x: x.prglength > 37, first.OtherChildren())
live_pmf = Pmf.MakePmfFromList(map(lambda x: risk.PregnancyValue(x), l))
vals, freqs = live_pmf.Render()
rectangles = pyplot.bar(vals, freqs)
pyplot.show()
