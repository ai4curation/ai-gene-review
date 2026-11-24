"""Pearson correlation of fitness profiles among PP_2042, PP_2043, PP_0765, PP_0766
from fitness_putida_pairs.tsv (output of analyze_pair.py)."""
import sys, json
import pandas as pd
here = sys.argv[1]
df = pd.read_csv(f"{here}/fitness_putida_pairs.tsv", sep="\t")
w = df.pivot(index="expName", columns="locusId", values="fit")
c = w.corr().round(3)
print(c)
out = {"n_experiments": int(len(w)), "pearson": c.to_dict()}
json.dump(out, open(sys.argv[2], "w"), indent=1)
