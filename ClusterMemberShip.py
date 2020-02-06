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


OGMOdata = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\MOBoxPlotting.csv")


Cluster1Data = OGMOdata[OGMOdata['Gene name (unique)'].isin(GOCluster1)]


Cluster1Data['Control'] = (Cluster1Data['3dOO'] + Cluster1Data['3dOO.1'] + Cluster1Data['3dOO.2'] + Cluster1Data['3dOO.3'] + Cluster1Data['3dOO.4'])/5
Cluster1Data['Injury'] = (Cluster1Data['3dCCl4'] + Cluster1Data['3dCCl4.1'] + Cluster1Data['3dCCl4.2'] + Cluster1Data['3dCCl4.3'] + Cluster1Data['3dCCl4.4'])/5
Cluster1Data['Recovery'] = (Cluster1Data['1mCCl4'] + Cluster1Data['1mCCl4.1']  + Cluster1Data['1mCCl4.2']  + Cluster1Data['1mCCl4.3']  + Cluster1Data['1mCCl4.4'])/5 

Cluster1Final = Cluster1Data[['Gene name (unique)','Control','Injury','Recovery']]

Cluster1Final = Cluster1Final.set_index('Gene name (unique)')

Cluster1Final.to_csv(r'C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MOCompleteCluster1Final.csv')

# --------------------
Cluster2Data = OGMOdata[OGMOdata['Gene name (unique)'].isin(GOCluster2)]


Cluster2Data['Control'] = (Cluster2Data['3dOO'] + Cluster2Data['3dOO.1'] + Cluster2Data['3dOO.2'] + Cluster2Data['3dOO.3'] + Cluster2Data['3dOO.4'])/5
Cluster2Data['Injury'] = (Cluster2Data['3dCCl4'] + Cluster2Data['3dCCl4.1'] + Cluster2Data['3dCCl4.2'] + Cluster2Data['3dCCl4.3'] + Cluster2Data['3dCCl4.4'])/5
Cluster2Data['Recovery'] = (Cluster2Data['1mCCl4'] + Cluster2Data['1mCCl4.1']  + Cluster2Data['1mCCl4.2']  + Cluster2Data['1mCCl4.3']  + Cluster2Data['1mCCl4.4'])/5 

Cluster2Final = Cluster2Data[['Gene name (unique)','Control','Injury','Recovery']]

Cluster2Final = Cluster2Final.set_index('Gene name (unique)')

Cluster2Final.to_csv(r'C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MOCompleteCluster2Final.csv')


#----------------------

Cluster3Data = OGMOdata[OGMOdata['Gene name (unique)'].isin(GOCluster3)]


Cluster3Data['Control'] = (Cluster3Data['3dOO'] + Cluster3Data['3dOO.1'] + Cluster3Data['3dOO.2'] + Cluster3Data['3dOO.3'] + Cluster3Data['3dOO.4'])/5
Cluster3Data['Injury'] = (Cluster3Data['3dCCl4'] + Cluster3Data['3dCCl4.1'] + Cluster3Data['3dCCl4.2'] + Cluster3Data['3dCCl4.3'] + Cluster3Data['3dCCl4.4'])/5
Cluster3Data['Recovery'] = (Cluster3Data['1mCCl4'] + Cluster3Data['1mCCl4.1']  + Cluster3Data['1mCCl4.2']  + Cluster3Data['1mCCl4.3']  + Cluster3Data['1mCCl4.4'])/5 

Cluster3Final = Cluster3Data[['Gene name (unique)','Control','Injury','Recovery']]

Cluster3Final = Cluster3Final.set_index('Gene name (unique)')

Cluster3Final.to_csv(r'C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MOCompleteCluster3Final.csv')

# export this data to R, and use it to make box plots. 
# only the most cluster representative items in each cluster are used in the box plots, in order to make any trends easier to see. 
