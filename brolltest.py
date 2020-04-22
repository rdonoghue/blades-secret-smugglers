import random


def bladesroll(poolsize, showroll=1, difficulty=0):
	roll1 = []
	rollsnapshot = 0
	if (difficulty == 1 and poolsize <=1):
		roll1.append(1)
	else:
		if poolsize > 0:
			for x in range(0, poolsize):
				dieroll = random.randint(1, 6)
				roll1.append(dieroll)
			roll1 = sorted(roll1, reverse=True)
			if difficulty == 1:
				roll1.pop(0)



## Gotta Deal with zero pools
		else:
			for x in range(0, 2):
				dieroll = random.randint(1, 6)
				roll1.append(dieroll)
			roll1 = sorted(myroll)
			if roll1[1]==6:
				roll1[1] = 0


	rollsnapshot = roll1
	bestroll = roll1.pop(0)
	if len(roll1) > 0:
		if roll1[0] == 6:
			bestroll += 1
	if showroll:
		print(rollsnapshot, " - ", bestroll)



	##	print ("Best: ", bestroll)
	##	print ("Rest: ", myroll)


	return rollsnapshot, bestroll



def samplingroll(pool, samplesize=10):
	rollcount = 1
	fail = 0
	mixed = 0
	success = 0
	crit = 0
	while rollcount <= samplesize:
		diceroll, bestresult = bladesroll(pool)
		if (bestresult == 1) or (bestresult == 2) or (bestresult == 3):
			fail += 1
		elif (bestresult == 4) or (bestresult == 5):
			mixed += 1
		elif bestresult == 6:
			success += 1
		elif bestresult > 6:
			crit += 1
		rollcount += 1
	return fail, mixed, success, crit, pool, samplesize


def getbladesresults(poolsize, samplesize, output=1):
	fail, mixed, success, crit, poolsize, samplesize = samplingroll(poolsize, samplesize)
	failpercent = round(fail / samplesize * 100, 2)
	mixedpercent = round(mixed / samplesize * 100, 2)
	succpercent = round(success / samplesize * 100, 2)
	critpercent = round(crit / samplesize * 100, 2)
	if output == 1:
		print(samplesize, " rolls of ", poolsize, " dice.")
		print("-----------------------------------------")
		print("Failure:       ", f'{fail:10}', " - ", failpercent, "%")
		print("Mixed Results: ", f'{mixed:10}', " - ", mixedpercent, "%")
		print("Successes:     ", f'{success:10}', " - ", succpercent, "%")
		print("Crits:         ", f'{crit:10}', " - ", critpercent, "%")
		print()
	elif output == 2:
		print("%r,%r,%r,%r,%r,%r" % (samplesize, poolsize, failpercent, mixedpercent, succpercent, critpercent))
	return failpercent, mixedpercent, succpercent, critpercent


## print("%r:%r" % (len(diceroll), diceroll))
howbig = 10
for dicerolled in range(3,4):
	f, m, s, c = getbladesresults(dicerolled, howbig, 1)


