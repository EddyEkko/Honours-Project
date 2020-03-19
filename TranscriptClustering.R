library(ConsensusClusterPlus)

d = read.csv(file = 'OverlapData.csv',sep = ',',row.names = 1)

m = data.matrix(d)
m[1:3,1:3]
n = t(m)
n[1:3,1:3]

title=tempdir()

results = ConsensusClusterPlus(n,maxK=12,reps=500,pItem=0.8,pFeature=1,
                               ,clusterAlg="hc",innerLinkage = 'complete',finalLinkage='complete',distance="euclidean",seed=1262118388.71279,plot="png")
results[[2]][["consensusMatrix"]][1:5,1:5]

#consensusTree = hclust object
results[[2]][["consensusTree"]]
#reports the cluster method used (e.g average, complete, centroid) as well as the number of objects analyzed

icl = calcICL(results,plot='png')
write.csv(icl[["itemConsensus"]], file = "TranscriptsCompleteItemConsensus.csv", row.names=FALSE)
write.csv(icl[["clusterConsensus"]], file = "TranscriptsCompleteClusterConsensus.csv", row.names=FALSE)

#current issues = the dataset is literally so big your laptop doesn't have enough RAM to run the analysis