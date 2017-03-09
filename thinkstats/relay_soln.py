import relay
import Pmf
import myplot

class RelayPmf(object):
    """docstring for RelayPmf."""
    def __init__(self):
        results = relay.ReadResults()
        speeds = relay.GetSpeeds(results)
        self.speeds = speeds
        self.pmf = Pmf.MakePmfFromList(speeds)

    def BiasedPmf(self, speed):
        new_pmf = self.pmf.Copy()

        for other_speed,p in new_pmf.Items():
            diff = abs(other_speed - speed)
            new_pmf.Mult(other_speed, diff)

        new_pmf.Normalize()

        return new_pmf

if __name__ == '__main__':
    r = RelayPmf()
    biased = r.BiasedPmf(7.5)

    print "Variance", biased.Var()
    print "Mean", biased.Mean()

    myplot.Clf()
    myplot.Hist(biased)
    myplot.Save(root='observed_speeds',
                title='PMF of running speed',
                xlabel='speed (mph)',
                ylabel='probability')
