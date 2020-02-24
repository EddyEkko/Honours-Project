#the purpose of this script is to get clusters ready for various kinds of gene ontology/pathway analysis
import pandas as pd

MOCompleteCluster1File =open( r"C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MOCompleteCluster1.txt",'a')

MOCompleteIC = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MatrisomeOnly-Completev2\MOCompleteItemConsensus.csv")

ThreeClusters = MOCompleteIC.loc[MOCompleteIC['k'] == 3]

MostRepresentative = ThreeClusters.loc[ThreeClusters['itemConsensus'] >= 0.8]

Cluster1Best = MostRepresentative.loc[MostRepresentative['cluster'] == 1]

for x in Cluster1Best['item']:
    MOCompleteCluster1File.write(x)
    MOCompleteCluster1File.write('\n')
    
MOCompleteCluster2File =open( r"C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MOCompleteCluster2.txt",'a')

MostRepresentative = ThreeClusters.loc[ThreeClusters['itemConsensus'] >= 0.8]

Cluster2Best = MostRepresentative.loc[MostRepresentative['cluster'] == 2]

for x in Cluster2Best['item']:
    MOCompleteCluster2File.write(x)
    MOCompleteCluster2File.write('\n')
    