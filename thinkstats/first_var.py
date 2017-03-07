import survey
import thinkstats
import math

table = survey.Pregnancies()
table.ReadRecords()

def first_child(record):
	return (record.birthord == 1) and (record.outcome == 1)

def not_first_child(record):
	return (record.birthord != 1) and (record.outcome == 1)

def avg_prg_length(data):
    prglengths = map(lambda x: x.prglength, data)
    return thinkstats.Mean(prglengths)

def variance(data):
    prglengths = map(lambda x: x.prglength, data)
    return thinkstats.Var(prglengths)

def standard_deviation(data):
    v = variance(data)
    return math.sqrt(v)


first_children = filter(first_child, table.records)
other_children = filter(not_first_child, table.records)

avg_frist = avg_prg_length(first_children)
avg_others = avg_prg_length(other_children)

print "Live First Birth: "
print len(first_children)
print avg_frist

print

print "Other Live Births"
print len(other_children)
print avg_others

print

print "Difference"
print (avg_frist - avg_others) * 7

print

print "Standard Deviation"
print "\t - First"
print standard_deviation(first_children)

print "\t - Other"
print standard_deviation(other_children)
