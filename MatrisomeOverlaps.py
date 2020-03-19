import pandas as pd

DEgenes = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\transcriptomic data\fibrosis_de.csv")

DEGenesReady = DEgenes[['gene_name','logFC (fibrosis: fibrosis_high vs fibrosis_low)','logFC (fibrosis: fibrosis_med vs fibrosis_low)','logFC (fibrosis: fibrosis_high vs fibrosis_med)']]
#get rid of all the variables in the DE transcript data that aren't needed.

MatrisomeOnly = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\MatrisomeOnlyAnovaZ.csv")
MOgenes = MatrisomeOnly['Gene name (unique)'].tolist()

DEList = DEGenesReady['gene_name'].tolist()

MatrisomeOverlaps = []
for x in MOgenes:
    if x.upper() in DEList:
        MatrisomeOverlaps.append(x.upper())
        
print('Total number of Matrisome Proteins = ' + str(len(MOgenes)))
print()
print('Total number of Overlaps = ' + str(len(MatrisomeOverlaps)))
# result = 166 Matrisome Proteins, of which 158 also appear in the DE data-set

DEMatrisomeProteins = DEGenesReady[DEGenesReady['gene_name'].isin(MatrisomeOverlaps)]
DEMatrisomeProteins = DEMatrisomeProteins.set_index('gene_name')

#FinalLength = DEMatrisomeProteins['gene_name'].tolist()
#no longer works after gene_name has been set to the index.

#print('Length of Final Dataset = ' + str(len(FinalLength)))
#result = 158 elements (proteins) in the final dataset - just as planned.

DEMatrisomeProteins.to_csv(r'C:\Users\user\Documents\pdf\bioinfo\MatrisomeOverlaps\DEMatrisomeProteins.csv')
        
        
        