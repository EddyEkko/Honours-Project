C2OverlapData$HvL = C2OverlapData$`logFC (fibrosis: fibrosis_high vs fibrosis_low)`
C2OverlapData$MvL = C2OverlapData$`logFC (fibrosis: fibrosis_med vs fibrosis_low)`
C2OverlapData$HvM = C2OverlapData$`logFC (fibrosis: fibrosis_high vs fibrosis_med)`



boxplot(C2OverlapData$HvL, C2OverlapData$MvL,C2OverlapData$HvM, xlab = 'Experimental Condition', ylab = 'Log(Fold Change)',main = "Cluster 2 Overlap LogFC")

