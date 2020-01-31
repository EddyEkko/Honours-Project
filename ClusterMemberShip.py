import pandas as pd

MOCompleteIC = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MatrisomeOnly-Completev2\MOCompleteItemConsensus.csv") #dataframe containing the cluster membership of every item for every attempted k value

ThreeClusters = MOCompleteIC.loc[MOCompleteIC['k'] == 3] #segments the original dataframe into 'cluster memberships when k = 3'


MostRepresentative = ThreeClusters.loc[ThreeClusters['itemConsensus'] >= 0.7] #creates a new dataframe, of only those items with an item consensus > 0.8 - the cluster members most similar to other members of the same cluster


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
    
print('Cluster 1: ' + str(GOCluster1))
print()
print('Cluster 2: ' + str(GOCluster2))
print()
print('Cluster 3: ' + str(GOCluster3))


