import csv
import operator
from sklearn.decomposition import PCA

f = open('genome-data.txt', 'rb')
reader = csv.reader(f, delimiter=' ')
genomeRows = [];
totalColumns = 0;

print "Parsing CSV...";
for row in reader:
    # print row
    genomeRows.append(row);
    totalColumns = len(row);
f.close();

print "Counting genes..."
# Figure out the mode in each row
modeTracking = [None]*(totalColumns-3);
#Initialize count tracking
for i in range(3, totalColumns):
    modeTracking[i - 3] = {'A':0,'T':0,'C':0,'G':0,'0':0};
# Accumulate
for i in range(0, len(genomeRows)):
    row = genomeRows[i];
    for j in range(0, totalColumns - 3):
        currentGene = row[j + 3];
        currentModeTracking = modeTracking[j];
        currentModeTracking[currentGene]+=1;
# Calculate mode for each column
print "Calculating mode...";
modes = [None]*(totalColumns - 3);
for j in range(0, totalColumns - 3):
    currentModeTracking = modeTracking[j];
    modes[j] = max(currentModeTracking.iteritems(), key=operator.itemgetter(1))[0];

print modes;

print "Calculating mode matrix...";
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

#for row in matrix:
    #print row;

print "Running PCA...";
pca = PCA(n_components=2);
result = pca.fit_transform(matrix);
# print(pca)
#print(result)

