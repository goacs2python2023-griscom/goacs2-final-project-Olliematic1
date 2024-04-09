#Whats up guys today we're gonna be making a visualization for a huge amount of data about air quality in NYC!
from bokeh.layouts import row, column
from bokeh.plotting import figure, show
#First we gotta import stuff
f = open("Air_Quality.csv", "r")
#open our data file
particlenames = []
#create list
for line in f:
    line = line.strip()
    line = line.split(",")
    if line[2] not in particlenames:
        preventbreak = [line[2]]
        particlenames.append(preventbreak)
    for i in range(len(particlenames)):
        if particlenames[i][0] == line[2]:
            date = line[9].split("/")
            days_since_2005 = (int(date[2]) - 2005) * 365
            days_since_2005 += ((int(date[1]) - 1) * 30)
            days_since_2005 += ((int(date[0]) - 1))
            particlenames[i].append((line[9], line[10]))
#alright guys now we have this super long list of particles, dates and times!
# Now we do Quicksort because we have a huge list!!
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        arr = arr[1:]
        pivot = arr[0]
        left = [x for x in arr[1:][0] if x < pivot]
        right = [x for x in arr[1:][0] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)
sortedparticlelist = []
for i in range(len(particlenames)):
    sortedlist = quicksort(particlenames[i])
    sortedparticlelist.append(sortedlist)
    print(i)