import pandas as pd

df = pd.concat(
    [
        pd.read_csv('csv/DoubleEG_2016G.csv'),
        pd.read_csv('csv/DoubleEG_2016H.csv'),
        pd.read_csv('csv/DoubleMu_2016G.csv'),
        pd.read_csv('csv/DoubleMu_2016H.csv')
    ]
)

df = df.drop_duplicates(subset=['Event'], keep='first')

run_event_file = open('run_event.txt', 'w')

run_event_list = [f'{r}:{e}' for r,e in zip(df['Run'].tolist(), df['Event'].tolist())]

for rel in run_event_list:
    run_event_file.write(f'"{rel}"\n')

run_event_file.close()
    
