import pandas as pd
#import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import os

print('Start processing 2 components ATP\n')
for r in ["1990", "2000", "2010", "2020", "2021", "all"]:
    data = pd.read_csv("../data/preprocessed/pca/atp_players_statistics_" + r + ".csv")
    restr = data.filter(items=['ace', 'df', '1stWon', '2ndWon', 'bpSaved', 'bpLost'])

    # Normalize
    data_std = preprocessing.StandardScaler().fit_transform(restr)

    #Compute PCA
    pca = PCA(n_components=2).fit_transform(data_std)

    att=['Y1','Y2']
    restr_pca = pd.DataFrame(columns=att)
    for i,j in zip(att,range(6)):
        restr_pca[i] = pca[:,j]
    restr_pca.to_csv('../data/preprocessed/radar/atp_pca_' + r +'.csv',index=False)

    dataFull = pd.read_csv('../data/preprocessed/pca/atp_players_statistics_'+ r +'.csv').join(pd.read_csv('../data/preprocessed/radar/atp_pca_'+ r +'.csv'))
    dataFull.to_csv('../data/preprocessed/radar/atp_dataFullPCA_'+ r +'.csv', index=False)

print('Done.')

print('Start processing 2 components WTA\n')
for r in ["2010", "2020", "2021", "all"]:
    data = pd.read_csv("../data/preprocessed/pca/wta_players_statistics_"+ r +".csv")
    restr = data.filter(items=['ace', 'df', '1stWon', '2ndWon', 'bpSaved', 'bpLost'])

    # Normalize
    data_std = preprocessing.StandardScaler().fit_transform(restr)

    #Compute PCA
    pca = PCA(n_components=2).fit_transform(data_std)

    att=['Y1','Y2']
    restr_pca = pd.DataFrame(columns=att)
    for i,j in zip(att,range(6)):
        restr_pca[i] = pca[:,j]
    restr_pca.to_csv('../data/preprocessed/radar/wta_pca_'+ r +'.csv',index=False)

    dataFull = pd.read_csv('../data/preprocessed/pca/wta_players_statistics_'+ r +'.csv').join(pd.read_csv('../data/preprocessed/radar/wta_pca_'+ r +'.csv'))
    dataFull.to_csv('../data/preprocessed/radar/wta_dataFullPCA_'+ r +'.csv', index=False)

print('Done.')
