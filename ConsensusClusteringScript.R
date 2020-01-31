library(ConsensusClusterPlus)

d = read.csv(file = 'AllProteins.csv',sep = ',',row.names = 1)

m = data.matrix(d)
m[1:5,1:5]
n = t(m)
n[1:5,1:5]
#in gene/protein analysis the genes are the items, and the concenrations measured are the features
#this analysis wants the items to be columns, and the rows to be features, so the data set has to be transposed.

title=tempdir()

#consensusMatrix = the consensus matrix
#The top five rows and coulmns of results for k = 2
results = ConsensusClusterPlus(n,maxK=12,reps=500,pItem=0.8,pFeature=1,
                               ,clusterAlg="hc",innerLinkage = 'ward.D',finalLinkage='ward.D',distance="euclidean",seed=1262118388.71279,plot="png")
results[[2]][["consensusMatrix"]][1:5,1:5]
 
#consensusTree = hclust object
results[[2]][["consensusTree"]]
#reports the cluster method used (e.g average, complete, centroid) as well as the number of objects analyzed

icl = calcICL(results,plot='png')
write.csv(icl[["itemConsensus"]], file = "AllProteinWardItemConsensus.csv", row.names=FALSE)
write.csv(icl[["clusterConsensus"]], file = "AllProteinWardClusterConsensus.csv", row.names=FALSE)


#default cluster method is average
#use the innerLinkage option in ClusterConsensusPlus to change the cluster method
#make FinalLinkage the same as InnerLinkage 

#intially got confused and had the Experimental Conditions (e.g 3doo_2) as my items and the proteins as my features.
#corrected this mistake by transposing the data, and used the new, correct matrix to generate the v2 files.

#for the MatrisomeOnlyDatasets, the consensus clustering was done with 1000 reps.
#this made analyzing the AllProteins dataset take far too long, so for them only 500 reps were used.

#for this data, the distance method has to be 'euclidean' or the whole analysis will fail
#next step = figure out how to give the output folder a specific name

#for some reason k has to be between 1 and 12.