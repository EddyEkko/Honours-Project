import pandas as pd

DEgenes = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\transcriptomic data\fibrosis_de.csv")

DEGenesReady2 = DEgenes[['gene_name','logFC (fibrosis: fibrosis_high vs fibrosis_low)','logFC (fibrosis: fibrosis_med vs fibrosis_low)','logFC (fibrosis: fibrosis_high vs fibrosis_med)']]

Resolvable = pd.read_csv(r'C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MOCompleteCluster2Final.csv')

C2genes = Resolvable['Gene name (unique)'].tolist()

DeGenes = DEGenesReady2['gene_name'].tolist()

#print(len(DeGenes))

C2overlaps = []
for x in C2genes:
    if x.upper() in DeGenes:
        C2overlaps.append(x.upper())
print('Cluster 2 Overlaps: ' + str(C2overlaps))


Augmented = pd.read_csv(r'C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MOCompleteCluster1Final.csv')
C1genes = Augmented['Gene name (unique)'].tolist()


C1overlaps = []
for x in C1genes:
    if x.upper() in DeGenes:
        C1overlaps.append(x.upper())
print('Cluster 1 Overlaps: ' + str(C1overlaps))

#new goal - find some way to pull out the DE gene Fold changes for each Overlap genes, and store them in a new dataset for each Cluster

C2OverlapData = DEGenesReady2[DEGenesReady2['gene_name'].isin(C2overlaps)]
print(C2OverlapData.head())

C2OverlapReady = C2OverlapData[['gene_name','logFC (fibrosis: fibrosis_high vs fibrosis_low)','logFC (fibrosis: fibrosis_med vs fibrosis_low)','logFC (fibrosis: fibrosis_high vs fibrosis_med)']]

C2OverlapReady = C2OverlapReady.set_index('gene_name')

C2OverlapReady.to_csv(r"C:\Users\user\Documents\pdf\bioinfo\transcriptomic data\C2OverlapData.csv")

#-------

C1OverlapData = DEGenesReady2[DEGenesReady2['gene_name'].isin(C1overlaps)]
print(C1OverlapData.head())

C1OverlapReady = C1OverlapData[['gene_name','logFC (fibrosis: fibrosis_high vs fibrosis_low)','logFC (fibrosis: fibrosis_med vs fibrosis_low)','logFC (fibrosis: fibrosis_high vs fibrosis_med)']]

C1OverlapReady = C1OverlapReady.set_index('gene_name')

C1OverlapReady.to_csv(r"C:\Users\user\Documents\pdf\bioinfo\transcriptomic data\C1OverlapData.csv")


