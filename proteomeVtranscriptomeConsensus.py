import pandas as pd

#first retrieve cluster membership assignments for the proteomic data, then do the same for the transcriptomic data and measure their similarity

MOCompleteIC = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MatrisomeOnly-Completev2\MOCompleteItemConsensus.csv") #dataframe containing the cluster membership of every item for every attempted k value

ThreeClusters = MOCompleteIC.loc[MOCompleteIC['k'] == 3] #segments the original dataframe into 'cluster memberships when k = 3'


MostRepresentative = ThreeClusters.loc[ThreeClusters['itemConsensus'] >= 0.80] #creates a new dataframe, of only those items with an item consensus > 0.8 - the cluster members most similar to other members of the same cluster
# 0.8 is the highest possible item Consensus where Cluster1 retains any members

Cluster1Best = MostRepresentative.loc[MostRepresentative['cluster'] == 1]

Cluster2Best = MostRepresentative.loc[MostRepresentative['cluster'] == 2]

Cluster3Best = MostRepresentative.loc[MostRepresentative['cluster'] == 3]

GOCluster1 = []
GOCluster2 = []
GOCluster3 = []

for x in Cluster1Best['item']:
    GOCluster1.append(x)
    
for x in Cluster2Best['item']:
    GOCluster2.append(x)
    
for x in Cluster3Best['item']:
    GOCluster3.append(x)
    
#--------------------------------------

DECompleteIC = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\MatrisomeOverlaps\DEMatrisomeCompleteItemConsensus.csv") 

DE3C = DECompleteIC.loc[DECompleteIC['k'] == 3] #segments the original dataframe into 'cluster memberships when k = 3'


DEMR = DE3C.loc[DE3C['itemConsensus'] >= 0.80] #creates a new dataframe, of only those items with an item consensus > 0.8 - the cluster members most similar to other members of the same cluster
# 0.8 is the highest possible item Consensus where Cluster1 retains any members

DEC1Best = DEMR.loc[DEMR['cluster'] == 1]

DEC2Best = DEMR.loc[DEMR['cluster'] == 2]

DEC3Best = DEMR.loc[DEMR['cluster'] == 3]

DECluster1 = []
DECluster2 = []
DECluster3 = []

for x in DEC1Best['item']:
    DECluster1.append(x)
    
for x in DEC2Best['item']:
    DECluster2.append(x)
    
for x in DEC3Best['item']:
    DECluster3.append(x)

#the above retrieves the cluster assignments for the DE data
#-------------------

MOC1vDEC1consensus = []
MOC1vDEC2consensus = []
MOC1vDEC3consensus = []

for x in GOCluster1:
    if x.upper() in DECluster1:
        MOC1vDEC1consensus.append(x.upper())
    if x.upper() in DECluster2:
        MOC1vDEC2consensus.append(x.upper())
    if x.upper() in DECluster3:
        MOC1vDEC3consensus.append(x.upper())
        
print('MOC1 v DEC1 = ' + str(len(MOC1vDEC1consensus)) + '/' + str(len(GOCluster1)))
print('MOC1 v DEC2 = ' + str(len(MOC1vDEC2consensus)) + '/' + str(len(GOCluster1)))
print('MOC1 v DEC3 = ' + str(len(MOC1vDEC3consensus)) + '/' + str(len(GOCluster1)))
print()

MOC2vDEC1consensus = []
MOC2vDEC2consensus = []
MOC2vDEC3consensus = []

for x in GOCluster2:
    if x.upper() in DECluster1:
        MOC2vDEC1consensus.append(x.upper())
    if x.upper() in DECluster2:
        MOC2vDEC2consensus.append(x.upper())
    if x.upper() in DECluster3:
        MOC2vDEC3consensus.append(x.upper())
        
print('MOC2 v DEC1 = ' + str(len(MOC2vDEC1consensus)) + '/' + str(len(GOCluster2)))
print('MOC2 v DEC2 = ' + str(len(MOC2vDEC2consensus)) + '/' + str(len(GOCluster2)))
print('MOC2 v DEC3 = ' + str(len(MOC2vDEC3consensus)) + '/' + str(len(GOCluster2)))
print()

print(len(DECluster1))
print(len(DECluster2))

