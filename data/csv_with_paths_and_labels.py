#You should run this inside folder with datasets.

import os
import os.path
import pandas as pd

df = pd.DataFrame(columns=['path', 'label', 'dataset'])
rows_list = []
def formDict(pathToFile):
    path = pathToFile
    label = pathToFile.rsplit('/')[-2]
    dataset = pathToFile.split('/')[1]
    rows_list.append({ 'path': path, 'label': label, 'dataset': dataset} )

for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(".jpg")]:
        formDict(os.path.join(dirpath, filename))
df = pd.DataFrame(rows_list)


df = df.loc[df['label'] != 'asl_alphabet_test'] #There are some badly sorted folder with single image per class. So I decided just to wipe out those pictures. 
#df = df.loc[df['label'] != '.ipynb_checkpoints']  # During working on this project my Jupyter left some files inside folders. 


df.to_csv('data.csv')