"""KT2440 gene neighbourhoods (Fitness Browser gene table, BERDL) around the two
DUF1302/DUF1329 pairs and the STRING partners PP_2018/PP_2019 and PP_2810-PP_2813.
Also: pairwise cofitness (FB cofit table) between PP_2042/PP_2043 and those partners."""
import sys, json
from berdl_notebook_utils.setup_spark_session import get_spark_session
spark = get_spark_session()
out = {}
windows = {"PP_2042": (2036, 2050), "PP_0765": (760, 770), "PP_2018": (2014, 2022), "PP_2811": (2806, 2816)}
for k, (a, b) in windows.items():
    ids = ",".join(f"'PP_{i:04d}'" for i in range(a, b + 1))
    df = spark.sql(f"SELECT sysName, CAST(begin AS INT) b, CAST(end AS INT) e, strand, desc FROM kescience.fitnessbrowser.gene "
                   f"WHERE orgId='Putida' AND sysName IN ({ids}) ORDER BY b").toPandas()
    out[k] = df.to_dict(orient="records")
    print("==", k); print(df.to_string())
part = "('PP_2018','PP_2019','PP_2810','PP_2811','PP_2812','PP_2813','PP_3201','PP_5590','PP_2042','PP_2043','PP_0765','PP_0766')"
c = spark.sql(f"SELECT locusId, hitId, CAST(rank AS INT) rank, CAST(cofit AS DOUBLE) cofit FROM kescience.fitnessbrowser.cofit "
              f"WHERE orgId='Putida' AND locusId IN ('PP_2042','PP_2043') AND hitId IN {part} ORDER BY locusId, hitId").toPandas()
out["cofit_pp2042_pp2043_vs_partners"] = c.to_dict(orient="records")
print(c.to_string())
f = spark.sql(f"SELECT locusId, MIN(CAST(fit AS DOUBLE)) minfit, MAX(CAST(fit AS DOUBLE)) maxfit, COUNT(*) n FROM kescience.fitnessbrowser.genefitness "
              f"WHERE orgId='Putida' AND locusId IN {part} GROUP BY locusId ORDER BY locusId").toPandas()
out["fit_range_partners"] = f.to_dict(orient="records")
print(f.to_string())
json.dump(out, open(sys.argv[1], "w"), indent=1, default=str)
