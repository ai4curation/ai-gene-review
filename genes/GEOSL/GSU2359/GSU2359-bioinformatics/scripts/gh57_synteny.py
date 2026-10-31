"""Gene-neighbourhood survey of GH57/DUF3536 (COG1449-like) proteins in the BERDL pangenome.

Question: is the GH57+DUF3536 protein family (Q74AJ5/GSU2359, B8J768/A2cp1_1916) conserved
next to the TreY/TreZ (glycogen -> trehalose) genes across genomes, and is it ever fused to TreY?

Targets  = gene clusters in kbase.ke_pangenome whose eggNOG-mapper PFAMs include DUF3536.
Sampling = one genome per GTDB species (lowest genome_id carrying a target), all target
           genes in that genome.
Neighbours = genes within +-K on the same contig (prodigal gene_id = <contig>_<index>),
           annotated with eggNOG-mapper KEGG_ko / Preferred_name / PFAMs of their cluster.
Also reports the specific neighbourhoods of the dashboard genes.
Outputs to $BERIL_RUN_DIR/out.
"""
import os, sys, json, re
sys.path.insert(0, os.path.join(os.environ.get("BERIL_CORE", ""), "tools"))
from berdl_notebook_utils.setup_spark_session import get_spark_session
from pyspark.sql import functions as F
try:
    from run_tables import pin
except Exception:
    pin = None

K = int(os.environ.get("GH57_K", "5"))
OUT = os.path.join(os.environ.get("BERIL_RUN_DIR", "/tmp/gh57_run"), "out")
os.makedirs(OUT, exist_ok=True)
spark = get_spark_session()
P = "kbase.ke_pangenome."
TABLES = [P + t for t in ["gene_cluster", "gene_genecluster_junction", "gene",
                          "eggnog_mapper_annotations", "gtdb_taxonomy_r214v1"]]
if pin:
    pin(spark, TABLES)

# marker KOs for alpha-glucan / trehalose genes
MARK = {
    "treY": "K06044", "treZ": "K01236", "treS": "K05343", "glgX": "K02438",
    "malQ": "K00705", "glgB": "K00700", "glgE": "K16147", "glgA": "K00703",
    "glgC": "K00975", "mak": "K16146", "otsA": "K00697", "otsB": "K01087",
    "glgP": "K00688", "amyA": "K01176", "treT": "K13057", "pulA": "K01200",
}
DASH = {"DPAK01000005.1_6": "GSU2359 (G. sulfurreducens)", "NC_011891.1_1918": "A2cp1_1916 (A. dehalogenans 2CP-1)"}

egg = spark.table(P + "eggnog_mapper_annotations").select(
    F.col("query_name").alias("cluster"), F.col("Preferred_name").alias("egg_name"),
    F.col("Description").alias("egg_desc"), F.col("PFAMs").alias("pfams"),
    F.col("KEGG_ko").alias("ko"), F.col("CAZy").alias("cazy"))
tgt = egg.filter(F.col("pfams").contains("DUF3536")).cache()
tgtp = tgt.toPandas()
tgtp.to_csv(f"{OUT}/duf3536_clusters.tsv", sep="\t", index=False)
print("DUF3536 clusters", len(tgtp), flush=True)

# fusion check 1: domain combinations among DUF3536 clusters
combo = tgtp.groupby("pfams").size().sort_values(ascending=False)
combo.to_csv(f"{OUT}/duf3536_pfam_combos.tsv", sep="\t", header=["n_clusters"])
# fusion check 2: TreY-KO clusters that also carry GH57/DUF3536 domains
treyc = egg.filter(F.col("ko").contains(MARK["treY"])).toPandas()
treyc["has_gh57"] = treyc["pfams"].fillna("").str.contains("Glyco_hydro_57")
treyc["has_duf3536"] = treyc["pfams"].fillna("").str.contains("DUF3536")
treyc.groupby(["pfams"]).size().sort_values(ascending=False).to_csv(
    f"{OUT}/treY_pfam_combos.tsv", sep="\t", header=["n_clusters"])
fus = treyc[treyc.has_gh57 | treyc.has_duf3536]
fus.to_csv(f"{OUT}/treY_gh57_fusions.tsv", sep="\t", index=False)

junc = spark.table(P + "gene_genecluster_junction")
gene = spark.table(P + "gene").select("gene_id", "genome_id")
gc = spark.table(P + "gene_cluster").select(F.col("gene_cluster_id").alias("cluster"), "gtdb_species_clade_id")
tg = tgt.select("cluster").join(gc, "cluster")
mem = junc.withColumnRenamed("gene_cluster_id", "cluster").join(F.broadcast(tg), "cluster") \
          .join(gene, "gene_id").cache()
print("target member genes", mem.count(), flush=True)
rep = mem.groupBy("gtdb_species_clade_id").agg(F.min("genome_id").alias("genome_id"))
mem1 = mem.join(rep, ["gtdb_species_clade_id", "genome_id"])
# always include dashboard genes' genomes
dash_genomes = mem.filter(F.col("gene_id").isin(list(DASH))).select("gtdb_species_clade_id", "genome_id")
mem1 = mem1.unionByName(mem.join(dash_genomes, ["gtdb_species_clade_id", "genome_id"])).distinct()
mem1 = mem1.withColumn("contig", F.regexp_extract("gene_id", r"^(.*)_(\d+)$", 1)) \
           .withColumn("idx", F.regexp_extract("gene_id", r"^(.*)_(\d+)$", 2).cast("int")).cache()
print("sampled target genes", mem1.count(), flush=True)

offs = spark.range(-K, K + 1).withColumnRenamed("id", "off")
nb = mem1.select(F.col("gene_id").alias("tgene"), "gtdb_species_clade_id", "genome_id", "contig", "idx") \
         .crossJoin(F.broadcast(offs)) \
         .withColumn("ngene", F.concat_ws("_", F.col("contig"), (F.col("idx") + F.col("off")).cast("string")))
ng = nb.select(F.col("ngene").alias("gene_id")).distinct()
nj = junc.join(F.broadcast(ng), "gene_id").withColumnRenamed("gene_id", "ngene") \
         .withColumnRenamed("gene_cluster_id", "cluster")
nb = nb.join(nj, "ngene").join(egg, "cluster", "left")
tax = spark.table(P + "gtdb_taxonomy_r214v1")
taxcols = [c for c in ["genome_id", "phylum", "class", "order", "family", "genus", "species"] if c in tax.columns]
nb = nb.join(F.broadcast(tax.select(*taxcols)), "genome_id", "left")
nbp = nb.toPandas()
nbp.to_csv(f"{OUT}/neighbourhoods_long.tsv", sep="\t", index=False)
print("neighbour rows", len(nbp), flush=True)

import pandas as pd
def flag(df, ko):
    return df["ko"].fillna("").str.contains(ko)
rows = []
for tgene, d in nbp.groupby("tgene"):
    r = {"tgene": tgene}
    for c in taxcols[1:]:
        r[c] = d[c].iloc[0] if c in d else None
    r["species_clade"] = d["gtdb_species_clade_id"].iloc[0]
    me = d[d.off == 0]
    r["self_pfams"] = me["pfams"].iloc[0] if len(me) else None
    r["self_ko"] = me["ko"].iloc[0] if len(me) else None
    others = d[d.off != 0]
    for name, ko in MARK.items():
        hit = others[flag(others, ko)]
        r[name] = ",".join(str(int(o)) for o in sorted(hit.off)) if len(hit) else ""
    # self fusion with a marker
    for name, ko in MARK.items():
        if len(me) and ko in str(me["ko"].iloc[0]):
            r["self_fused_" + name] = True
    rows.append(r)
per = pd.DataFrame(rows)
per.to_csv(f"{OUT}/per_target_gene.tsv", sep="\t", index=False)

def has(col, within=K):
    return per[col].fillna("").apply(lambda s: any(abs(int(x)) <= within for x in s.split(",") if x))
summ = {"K": K, "n_duf3536_clusters": int(len(tgtp)),
        "n_sampled_species": int(per.species_clade.nunique()), "n_sampled_target_genes": int(len(per)),
        "n_trey_ko_clusters": int(len(treyc)), "n_trey_clusters_with_gh57_or_duf3536": int(len(fus))}
sp = per.copy()
for name in MARK:
    sp[name + "_nb"] = has(name)
sp["treY_and_treZ"] = sp["treY_nb"] & sp["treZ_nb"]
sp["treY_or_treZ"] = sp["treY_nb"] | sp["treZ_nb"]
sp["any_glucan_marker"] = sp[[m + "_nb" for m in MARK]].any(axis=1)
sp["treY_adjacent"] = has("treY", 1)
sp["treZ_adjacent"] = has("treZ", 1)
sp["treY_within2"] = has("treY", 2)
# species-level: species counts as positive if any sampled target gene in it is positive
byspec = sp.groupby("species_clade")[[m + "_nb" for m in MARK] + ["treY_and_treZ", "treY_or_treZ",
          "any_glucan_marker", "treY_adjacent", "treZ_adjacent", "treY_within2"]].any()
summ["species_fraction"] = {c: round(float(byspec[c].mean()), 4) for c in byspec.columns}
summ["species_count"] = {c: int(byspec[c].sum()) for c in byspec.columns}
if "phylum" in sp:
    ph = sp.groupby("phylum").agg(n_genes=("tgene", "size"), treY=("treY_nb", "sum"),
                                  treZ=("treZ_nb", "sum"), both=("treY_and_treZ", "sum"))
    ph.sort_values("n_genes", ascending=False).to_csv(f"{OUT}/by_phylum.tsv", sep="\t")
sp.to_csv(f"{OUT}/per_target_gene_flags.tsv", sep="\t", index=False)
# dashboard genes' neighbourhoods
dn = nbp[nbp.tgene.isin(list(DASH))].sort_values(["tgene", "off"])
dn[["tgene", "off", "ngene", "cluster", "egg_name", "ko", "pfams", "egg_desc"]].to_csv(
    f"{OUT}/dashboard_gene_neighbourhoods.tsv", sep="\t", index=False)
summ["dashboard_neighbourhoods_found"] = sorted(dn.tgene.unique().tolist())
json.dump(summ, open(os.path.join(os.path.dirname(OUT), "results.json"), "w"), indent=1)
print(json.dumps(summ, indent=1))
if pin:
    pin(spark, TABLES)
