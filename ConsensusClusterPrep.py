import pandas as pd

MatrisomeOnly = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\MatrisomeOnlyAnovaZ.csv") #imports the data as a dataframe
AllProteins = pd.read_csv(r"C:\Users\user\Documents\pdf\bioinfo\AllProteinsAnovaZ.csv")

MatrisomeOnlyReady = MatrisomeOnly.set_index('Gene name (unique)') #sets the gene name as the index for each row
AllProteinsReady= AllProteins.set_index('Gene name (unique)')

MatrisomeOnlyReady.to_csv(r'C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\MatrisomeOnly.csv')
AllProteinsReady.to_csv(r'C:\Users\user\Documents\pdf\bioinfo\ConsensusClustering\AllProteins.csv')