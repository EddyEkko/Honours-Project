import pandas as pd


DEgenes = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\transcriptomic data\fibrosis_de.csv")

DEGenesReady = DEgenes[['gene_name','logFC (fibrosis: fibrosis_high vs fibrosis_low)','logFC (fibrosis: fibrosis_med vs fibrosis_low)','logFC (fibrosis: fibrosis_high vs fibrosis_med)']]

DEGenesReady.to_csv(r"C:\Users\user\Documents\pdf\bioinfo\transcriptomic data\DEGenesReady.csv") 

DEnames = DEGenesReady['gene_name'].tolist() #exports the gene names of the DE dataset as a list


# new goal - add the Cluster 1 and Cluster 2 Overlap files together, and then run Consensus Clustering on them.
# this should produce a situation where two clusters is the optimum solution (if there really is a strong correlation between transcriptomic and proteomic behavior)
#use all members of both Clusters - not just the Members with the highest item consensus scores.

MOCompleteIC = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MatrisomeOnly-Completev2\MOCompleteItemConsensus.csv") #dataframe containing the cluster membership of every item for every attempted k value

ThreeClusters = MOCompleteIC.loc[MOCompleteIC['k'] == 3] #segments the original dataframe into 'cluster memberships when k = 3'

MostRepresentative = ThreeClusters.loc[ThreeClusters['itemConsensus'] >= 0.80] #sets a cutoff value, preventing overlap between clusters

Cluster1 = MostRepresentative.loc[MostRepresentative['cluster'] == 1] 

Cluster2 = MostRepresentative.loc[MostRepresentative['cluster'] == 2]

C1 = []
for x in Cluster1['item']:
    C1.append(x)
    
C2 = []
for x in Cluster2['item']:
    C2.append(x)
    
C2overlaps = []
for x in C2:
    if x.upper() in DEnames:
        C2overlaps.append(x.upper())


C1overlaps = []
for x in C1:
    if x.upper() in DEnames:
        C1overlaps.append(x.upper())

#print(C1overlaps[0:10])
#print(C2overlaps[0:10]) 

C2OverlapData = DEGenesReady[DEGenesReady['gene_name'].isin(C2overlaps)]
C2OverlapData = C2OverlapData.set_index('gene_name')


C1OverlapData = DEGenesReady[DEGenesReady['gene_name'].isin(C1overlaps)]
C1OverlapData = C1OverlapData.set_index('gene_name')


OverlapData = C1OverlapData.append(C2OverlapData)


OverlapData.to_csv(r"C:\Users\user\Documents\pdf\bioinfo\transcriptomic data\OverlapData.csv")