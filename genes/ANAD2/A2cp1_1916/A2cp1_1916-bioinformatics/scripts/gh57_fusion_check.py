"""Are GH57/DUF3536 proteins fused to TreY? Follow-up on run gh57-synteny.

In kbase.ke_pangenome eggNOG-mapper output, some DUF3536+Glyco_hydro_57 clusters carry the
TreY KO (K06044) and CAZy GH13. A real TreY fusion would be ~1.5-2x longer than the
~800-aa GH57/DUF3536 protein and would carry a TreY (GH13 Alpha-amylase) domain. This compares
bakta protein lengths and products of K06044-tagged vs untagged DUF3536 clusters, and checks
whether tagged clusters still have a separate treY gene within +-5 genes (from gh57-synteny).
Inputs: --synteny-dir (out/out of the gh57-synteny run). Outputs to $BERIL_RUN_DIR.
"""
import os, sys, json, argparse
sys.path.insert(0, os.path.join(os.environ.get("BERIL_CORE", ""), "tools"))
from berdl_notebook_utils.setup_spark_session import get_spark_session
from pyspark.sql import functions as F
import pandas as pd

ap = argparse.ArgumentParser(); ap.add_argument("--synteny-dir", required=True); a = ap.parse_args()
OUT = os.environ.get("BERIL_RUN_DIR", "/tmp/gh57_fus"); os.makedirs(OUT, exist_ok=True)
spark = get_spark_session()
cl = pd.read_csv(os.path.join(a.synteny_dir, "duf3536_clusters.tsv"), sep="\t")
cl["trey_ko"] = cl["ko"].fillna("").str.contains("K06044")
ids = cl["cluster"].tolist()
bak = spark.table("kbase.ke_pangenome.bakta_annotations").filter(F.col("gene_cluster_id").isin(ids)) \
    .select(F.col("gene_cluster_id").alias("cluster"), "length", "product", "kegg_orthology_id").toPandas()
egg = spark.table("kbase.ke_pangenome.eggnog_mapper_annotations").filter(F.col("query_name").isin(ids)) \
    .select(F.col("query_name").alias("cluster"), "seed_ortholog", "max_annot_lvl").toPandas()
m = cl.merge(bak, on="cluster", how="left").merge(egg, on="cluster", how="left")
m.to_csv(os.path.join(OUT, "duf3536_clusters_lengths.tsv"), sep="\t", index=False)
summ = {}
for k, g in m.groupby("trey_ko"):
    L = g["length"].dropna()
    summ[f"trey_ko={k}"] = {"n": int(len(g)), "len_median": float(L.median()), "len_p10": float(L.quantile(.1)),
                            "len_p90": float(L.quantile(.9)), "n_len_ge_1200": int((L >= 1200).sum()),
                            "top_products": g["product"].value_counts().head(5).to_dict(),
                            "bakta_K06044": int(g["kegg_orthology_id"].fillna("").str.contains("K06044").sum()),
                            "top_seed_orthologs": g["seed_ortholog"].value_counts().head(5).to_dict()}
fl = pd.read_csv(os.path.join(a.synteny_dir, "per_target_gene_flags.tsv"), sep="\t")
fl["trey_ko"] = fl["self_ko"].fillna("").str.contains("K06044")
summ["synteny_by_trey_ko"] = {str(k): {"n_genes": int(len(g)), "separate_treY_within5": int(g["treY_nb"].sum()),
                                       "treZ_within5": int(g["treZ_nb"].sum())} for k, g in fl.groupby("trey_ko")}
summ["trey_ko_tagged_by_phylum"] = fl[fl.trey_ko]["phylum"].value_counts().head(10).to_dict()
json.dump(summ, open(os.path.join(OUT, "results.json"), "w"), indent=1, default=str)
print(json.dumps(summ, indent=1, default=str))
