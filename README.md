# cms-masterclass-scripts
Scripts for preparation of the CMS masterclass

## Input

The input four-lepton events come from the analysis found [here](https://gitlab-p4n.aip.de/lucas.karwatzki/DPG_HEP_HiggsTo4L_PUNCH). 
There, I have modified the analysis code to output the selected event information to the csv files found here.

## Usage

```
virtualenv qn
source qn/bin/activate
pip install -r requirements.txt
jupyter lab
```

* `fourlepton.ipynb` reads the information from the csv files into a pandas dataframe
* `invariantmass.ipynb` reads the information from the csv files into a pandas dataframe and plots the invariant mass
* `dasfiles.py` generates the DAS queries for the equivalent miniaod files; the .sh files have to be run on lxplus to generate the resulting file lists (be sure to run `voms-proxy-init --voms cms`)
