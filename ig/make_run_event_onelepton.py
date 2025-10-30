import pandas as pd

df = pd.concat(
    [
        #pd.read_csv('../csv/SingleMuonRun2016H.csv'),
        #pd.read_csv('../csv/SingleElectronRun2016G.csv'),
        #pd.read_csv('../csv/Wenu_plus.csv'),
        #pd.read_csv('../csv/Wmunu_plus.csv'),
        #pd.read_csv('../csv/Wenu_minus.csv'),
        pd.read_csv('../csv/Wmunu_minus.csv')
    ]
)

df = df.drop_duplicates(subset=['Event'], keep='first')

run_event_file = open('run_event_Wmunu_minus.txt', 'w')

run_event_list = [f'{r}:{e}' for r,e in zip(df['Run'].tolist(), df['Event'].tolist())]

for rel in run_event_list:
    run_event_file.write(f'{rel}\n')

run_event_file.close()
    
