import pandas as pd

def make_run_lumi(df):
    return [f'{r}:{l}' for r,l in zip(df['Run'].tolist(), df['Lumi'].tolist())]

command = "/cvmfs/cms.cern.ch/common/dasgoclient"

inputs = [
    {
        'name': 'JpsiEERun2016H', 
        'run_lumi': make_run_lumi(pd.read_csv('../csv/JpsiEERun2016H.csv')),
        'dataset': '/DoubleEG/Run2016H-UL2016_MiniAODv2-v1/MINIAOD'
    }
]

for i in inputs:

    name = i['name']
    dasfile = open(f'dasfile_{name}.sh', 'w')

    run_lumi = i['run_lumi']
    dataset = i['dataset']

    # Use a set to get rid of duplicates
    run_lumi = list(set(run_lumi))
    
    for rel in run_lumi:

        run = rel.split(':')[0]
        lumi = rel.split(':')[1]
        query = f'{command} -query="file dataset={dataset} run={run} lumi={lumi}"\n'
        dasfile.write(query)

    dasfile.close()

