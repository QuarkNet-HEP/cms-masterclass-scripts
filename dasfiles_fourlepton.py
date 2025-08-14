import pandas as pd

def make_run_event_lumi(df):
    return [f'{r}:{e}:{l}' for r,e,l in zip(df['Run'].tolist(), df['Event'].tolist(), df['Lumi'].tolist())]


command = "/cvmfs/cms.cern.ch/common/dasgoclient"

inputs = [
    {
        'name': 'DoubleEG_2016G', 
        'run_event_lumi': make_run_event_lumi(pd.read_csv('csv/DoubleEG_2016G.csv')),
        'dataset': '/DoubleEG/Run2016G-UL2016_MiniAODv2-v1/MINIAOD'
    },
    {
        'name': 'DoubleEG_2016H',
        'run_event_lumi': make_run_event_lumi(pd.read_csv('csv/DoubleEG_2016H.csv')),
        'dataset': '/DoubleEG/Run2016H-UL2016_MiniAODv2-v1/MINIAOD',
    },
    {
        'name': 'DoubleMu_2016G',
        'run_event_lumi': make_run_event_lumi(pd.read_csv('csv/DoubleMu_2016G.csv')),
        'dataset': '/DoubleMuon/Run2016G-UL2016_MiniAODv2-v1/MINIAOD',
    },
    {
        'name': 'DoubleMu_2016H',
        'run_event_lumi': make_run_event_lumi(pd.read_csv('csv/DoubleMu_2016H.csv')),
        'dataset': '/DoubleMuon/Run2016H-UL2016_MiniAODv2-v2/MINIAOD',
    }
]


for i in inputs:

    name = i['name']
    dasfile = open(f'dasfile_{name}.sh', 'w')

    run_event_lumi = i['run_event_lumi']
    dataset = i['dataset']

    for rel in run_event_lumi:

        run = rel.split(':')[0]
        lumi = rel.split(':')[2]
        query = f'{command} -query="file dataset={dataset} run={run} lumi={lumi}"\n'
        dasfile.write(query)

    dasfile.close()

