#!/usr/bin/env python3
import sys, os
import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv
import glob

files_r = glob.glob('../results/comparison_Lfng_human_gastruloids/GOterms_ReprChiLfng/GO_vsReprChiLfng_hcl*tsv')

dfs_r = {int(f.rsplit('hcl')[-1].rsplit('.')[0]): read_csv(f, sep = '\t', skiprows=91) for f in files_r}

### Study on reproducible genes background
cols = ['GO','enrichment', 'name', 'ratio_in_study','p_uncorrected','p_fdr_bh','study_items']
ontologies = ['BP', 'MF', 'CC']
for ont in ontologies:
    for cl in dfs_r:
        idxs = [idx for idx in dfs_r[cl].index if dfs_r[cl].loc[idx,'NS']==ont]
        adf = dfs_r[cl].loc[idxs,cols]
        adf = adf[adf['p_fdr_bh'] <= 0.3]
        print(cl)
        print(adf)
        print()


###
files_r = glob.glob('../results/comparison_Lfng_human_gastruloids/GOterms_ReprSBLfng/GO_vsReprSBLfng_hcl*tsv')

dfs_r = {int(f.rsplit('hcl')[-1].rsplit('.')[0]): read_csv(f, sep = '\t', skiprows=91) for f in files_r}

### Study on reproducible genes background
cols = ['GO','enrichment', 'name', 'ratio_in_study','p_uncorrected','p_fdr_bh','study_items']
ontologies = ['BP', 'MF', 'CC']
for ont in ontologies:
    for cl in dfs_r:
        idxs = [idx for idx in dfs_r[cl].index if dfs_r[cl].loc[idx,'NS']==ont]
        adf = dfs_r[cl].loc[idxs,cols]
        adf = adf[adf['p_fdr_bh'] <= 0.3]
        print(cl)
        print(adf)
        print()


