import pandas as pd

# 600 Z
# 1000 J/psi
# 600 Y

df = pd.concat(
    [
        #pd.read_csv('../csv/DoubleElectronRun2016H.csv').iloc[:300],
        pd.read_csv('../csv/DoubleMuonRun2016H.csv').iloc[-300:],
        #pd.read_csv('../csv/JpsiEERun2016H.csv').iloc[:500],
        #pd.read_csv('../csv/JpsiMuMuRun2016H.csv').iloc[:500],
        #pd.read_csv('../csv/UpsilonEERun2016H.csv').iloc[:300],
        #pd.read_csv('../csv/UpsilonMuMuRun2016H.csv').iloc[:300]
    ]
)

df = df.drop_duplicates(subset=['Event'], keep='first')

run_event_file = open('run_event_Zmumu.txt', 'w')

run_event_list = [f'{r}:{e}' for r,e in zip(df['Run'].tolist(), df['Event'].tolist())]

for rel in run_event_list:
    run_event_file.write(f'{rel}\n')

run_event_file.close()
    
