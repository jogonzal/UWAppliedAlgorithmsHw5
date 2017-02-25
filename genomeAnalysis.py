import csv
import operator

f = open('genome-data.txt', 'rb')
reader = csv.reader(f, delimiter=' ')
genomeRows = [];
totalColumns = 0;
for row in reader:
    # print row
    genomeRows.append(row);
    totalColumns = len(row);
f.close();

# Figure out the mode in each row
modeTracking = [];
#Initialize count tracking
for i in range(3, totalColumns):
    modeTracking.append({'A':0,'T':0,'C':0,'G':0,'0':0});
# Accumulate
for i in range(0, len(genomeRows)):
    row = genomeRows[i];
    for j in range(0, totalColumns - 3):
        currentGene = row[j + 3];
        currentModeTracking = modeTracking[j];
        currentModeTracking[currentGene]+=1;
# Calculate mode for each column
modes = [];
for j in range(0, totalColumns - 3):
    currentModeTracking = modeTracking[j];
    modes.append(max(currentModeTracking.iteritems(), key=operator.itemgetter(1))[0]);

print modes;

matrix = [None] * len(genomeRows);
for i in range(0, len(genomeRows)):
    row = genomeRows[i];
    matrixRow = [0] * len(modes);
    for j in range(0, totalColumns - 3):
        currentGene = row[j + 3];
        if (currentGene == modes[j]):
            matrixRow[j] = 1;
        else:
            matrixRow[j] = 0;
    matrix[i] = matrixRow;

for row in matrix:
    print row;