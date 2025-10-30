import pandas as pd

edf = pd.read_csv('SingleElectronRun2016G.csv')
mdf = pd.read_csv('SingleMuonRun2016H.csv')

# We want to split the two dataframes by charge and
# export a file each for both electrons and muons

wep = edf[edf['Q'] == 1]
wem = edf[edf['Q'] == -1]

wmp = mdf[mdf['Q'] == 1]
wmm = mdf[mdf['Q'] == -1]

wep.to_csv(
    'Wenu_plus.csv',
    index=False
)

wem.to_csv(
    'Wenu_minus.csv',
    index=False
)

wmp.to_csv(
    'Wmunu_plus.csv',
    index=False
)

wmm.to_csv(
    'Wmunu_minus.csv',
    index=False
)
