import survey
table = survey.Pregnancies()
table.ReadRecords()

def first_child(record):
	return (record.birthord == 1) and (record.outcome == 1)

def not_first_child(record):
	return (record.birthord != 1) and (record.outcome == 1)

def live_birth(record):
	return record.outcome == 1

def avg_prg_length(data):
	prglengths = map(lambda x: x.prglength, data)
	s = sum(prglengths)
	return float(s) / len(data)

def FirstChildren():
	return filter(first_child, table.records)

def OtherChildren():
	return filter(not_first_child, table.records)

def LiveBirths():
	return filter(live_birth, table.records)

first_children = FirstChildren()
other_children = OtherChildren()

avg_frist = avg_prg_length(first_children)
avg_others = avg_prg_length(other_children)

# print "Live First Birth: "
# print len(first_children)
# print avg_frist
#
# print
#
# print "Other Live Births"
# print len(other_children)
# print avg_others
#
# print
#
# print "Difference"
# print (avg_frist - avg_others) * 7
