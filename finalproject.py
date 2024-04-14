#Whats up guys today we're gonna be making a visualization for a huge amount of data about air quality in NYC!
from bokeh.layouts import row, column
from bokeh.plotting import figure, show
#First we gotta import stuff
def main():
    #open our data file
    f = open("Air_Quality.csv", "r")
    #create list
    particlenames = []
    #this will come up later
    variable = False
    # first line is bad, so skip!!
    next(f)
    #Now comes the hard part
    #In this code we will be using a 3D list
    #We have our overall list, then inside we have our lists of each particle, and inside we have the (x,y) tuples
    #Structure is [["Name of particle 1", (x,y), (x,y)...], ["Name of particle 2", (x,y), (x,y) ...] ...]
    for line in f:
        line = line.strip()
        line = line.split(",")
        #go through particlenames
        #not too innefficient because its only 10 long, its the overall list
        for i in range(len(particlenames)):
            if particlenames[i][0] == line[2]:
                #date is in month, day, year, and can't be organized so we change it
                #to days since Jan 1st, 2005, because thats the earliest date.
                date = line[9].split("/")
                #just in case theres an error make sure the length is 3!!
                if len(date) == 3:
                    days_since_2005 = (int(date[-1]) - 2005) * 365
                    days_since_2005 += ((int(date[-2]) - 1) * 30)
                    days_since_2005 += ((int(date[-3]) - 1))
                    #change str to float, and append!
                    particlenames[i].append((days_since_2005, float(line[10])))
                #ok so that sneaky variable we had before comes into play
                #its so that if we already appended it we dont double append
                variable = True
        # so we can't do something normal here like "if line[2] not in particlenames"
        # because of the way the list works, the names aren't in their own list
        # so I could make them their own list but thats innefficient so I did this!
        if not variable:
            date = line[9].split("/")
                #just in case theres an error make sure the length is 3!!
            if len(date) == 3:
                days_since_2005 = (int(date[-1]) - 2005) * 365
                days_since_2005 += ((int(date[-2]) - 1) * 30)
                days_since_2005 += ((int(date[-3]) - 1))
            else:
                days_since_2005 = 0
            #some weird errors were happening
            #some of the data is mislabeled I think so we'll do this!
            try:
                particlenames.append([line[2], (days_since_2005, float(line[10]))])
            except:
                pass
        variable = False

    #alright guys now we have this super long list of particles, dates and times!

    #time to sort stuff
    sortedparticlelist = []
    for i in range(len(particlenames)):
        #essentially we're just sorting every list in the big list individually
        #(python sorted() automatically sorts by the first number in a tuple)
        #but we're excluding the first thing because its the particle name
        #then adding it back to the first slot
        sortedparticlelist.append(sorted(particlenames[i][1:]))
        sortedparticlelist[i].insert(0, particlenames[i][0])


    #now we need to put everything into a format that bokeh likes so here we go!
    xvals = [[]]
    yvals = [[]]
    for i in range(len(sortedparticlelist)):
        for l in range(len(sortedparticlelist[i][1:])):
            #appending the first number in each tuple to x, second number to y
            xvals[i].append(sortedparticlelist[i][l][0])
            yvals[i].append(sortedparticlelist[i][l][1])
        xvals.append([])
        yvals.append([])

    #now they are in two 2D lists that should match up with each other
    #[[no2(x,y)]]
    f1 = figure(title = sortedparticlelist[0][0])
    f1.circle(xvals[0], yvals[0], size = 5, color = "blue")
    f1.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f2 = figure(title = sortedparticlelist[1][0])
    f2.circle(xvals[1], yvals[1], size = 5, color = "blue")
    f2.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f3 = figure(title = sortedparticlelist[2][0])
    f3.circle(xvals[2], yvals[2], size = 5, color = "blue")
    f3.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f4 = figure(title = sortedparticlelist[3][0])
    f4.circle(xvals[3], yvals[3], size = 5, color = "blue")
    f4.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f5 = figure(title = sortedparticlelist[4][0])
    f5.circle(xvals[4], yvals[4], size = 5, color = "blue")
    f5.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f6 = figure(title = sortedparticlelist[5][0])
    f6.circle(xvals[5], yvals[5], size = 5, color = "blue")
    f6.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f7 = figure(title = sortedparticlelist[6][0])
    f7.circle(xvals[6], yvals[6], size = 5, color = "blue")
    f7.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f8 = figure(title = sortedparticlelist[7][0])
    f8.circle(xvals[7], yvals[7], size = 5, color = "blue")
    f8.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f9 = figure(title = sortedparticlelist[8][0])
    f9.circle(xvals[8], yvals[8], size = 5, color = "blue")
    f9.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f10 = figure(title = sortedparticlelist[9][0])
    f10.circle(xvals[9], yvals[9], size = 5, color = "blue")
    f10.xaxis.axis_label = 'Days Since Jan 1, 2005'
    f11 = figure(title = sortedparticlelist[10][0])
    f11.circle(xvals[10], yvals[10], size = 5, color = "blue")
    f11.xaxis.axis_label = 'Days Since Jan 1, 2005'
    show(row(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11))
main()