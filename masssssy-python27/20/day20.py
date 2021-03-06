import re
def main():
    inputfile = open("input")
    inputdata = inputfile.read()
    inputfile.close()

    splitData = inputdata.split("\n")

    startsEnds = []
    for item in splitData:
    	split = item.split("-")
    	startsEnds.append([int(split[0]), int(split[1])])

    sortedList = sorted(startsEnds, key=lambda x: x[0])

    #take lowest start, remove all that ends before this ones end
    found = False
    while found == False:
    	lowest = sortedList.pop(0)
    	#blocked until at least lowests end
    	blockedUntil = int(lowest[1])

    	#remove all that have their highest block lower than blockedUntil
    	for item in sortedList:
    		if int(item[1]) < int(blockedUntil):
    			sortedList.remove(item)

    	test = int(sortedList[0][0]) - int(blockedUntil)
    	if(test > 1):
    		found = True
    		
    		print blockedUntil +1

if __name__ == "__main__":
    main()
   