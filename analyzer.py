import json

file = open('Streaming_History_Audio_DATE.json')

data = json.load(file)

templist1=[]

for i in data:
	tempitem = (i.get("master_metadata_track_name"))
	templist1.append(tempitem)

#print(templist1)

file.close()

templist2 = []

for i in templist1:
	if templist2.count(i) != 1:
		templist2.append(i)

outputlist=[]

for i in templist2:
	tempitem = {
		"song": i,
		"listens": templist1.count(i)
	}
	outputlist.append(tempitem)

def sortbylistens(e):
	return e["listens"]

outputlist.sort(key=sortbylistens)

totallistens=0

for i in outputlist:
	totallistens=totallistens+i["listens"]

with open("outputfile.txt", "w") as f:
	for i in outputlist:
		tempstring = ""
		tempstring = tempstring+str(i)+'\n'
		f.write(tempstring)
	f.write("Total Songs:\t"+str(len(outputlist))+'\n')
	f.write("Total Songs with Repeats:\t"+str(totallistens)+'\n')
