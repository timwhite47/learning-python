import matplotlib.pyplot as pyplot
import Pmf

hist = Pmf.MakeHistFromList([1,2,2,3,5])
vals, freqs = hist.Render()
rectangles = pyplot.bar(vals, freqs)
pyplot.show()
