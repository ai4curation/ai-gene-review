import csv
import pathlib
import re
import collections

R = pathlib.Path.cwd()
P = R / "projects/PROTNLM_EVALUATION"
out = []
paths = collections.defaultdict(list)
for p in (R / "genes").glob("*/*/*-ai-review.yaml"):
    m = re.search(r"^id:\s*[\"\']?([^\s\"\']+)", p.read_text(), re.M)
    if m:
        paths[m[1].replace("UniProtKB:", "")].append(str(p.relative_to(R)))


def add(src, cohort, species=None, role="prediction_target"):
    for r in csv.DictReader((P / src).open()):
        a = r["accession"]
        ps = paths[a]
        sp = species or r.get("species") or (ps[0].split("/")[1] if ps else "")
        gene = r.get("gene_symbol") or (ps[0].split("/")[2] if ps else a)
        out.append(
            dict(
                cohort=cohort,
                role=role,
                accession=a,
                species=sp,
                gene_symbol=gene,
                gene_review=";".join(ps),
                cohort_source=str((P / src).relative_to(R)),
            )
        )


add("argo_protnlm_50.csv", "ARGO50")
add("mammal-benchmark/horse40.csv", "HORSE40", "HORSE")
for r in list(out):
    if r["cohort"] != "HORSE40":
        continue
    p = R / "genes/human" / r["gene_symbol"] / (r["gene_symbol"] + "-ai-review.yaml")
    if p.exists():
        import yaml

        a = yaml.safe_load(p.read_text())["id"]
        out.append(
            dict(
                cohort="HORSE40_HUMAN_PAIR",
                role="paired_reference",
                accession=a,
                species="human",
                gene_symbol=r["gene_symbol"],
                gene_review=str(p.relative_to(R)),
                cohort_source=r["cohort_source"],
            )
        )
add("fly-benchmark/functional-cohort.csv", "FLY41", "DROME")
add("fly-benchmark/location-keyword-tier.csv", "FLY_LOCATION_KEYWORD", "DROME")
add("fly-benchmark/next20/cohort.csv", "FLY_NEXT20", "DROME")
add("pombe-benchmark/functional-cohort.csv", "POMBE20", "SCHPO")
add("pombe-benchmark/remaining/cohort.csv", "POMBE_REMAINING8", "SCHPO")
add("neurospora-benchmark/review-cohort.csv", "NEUROSPORA20", "NEUCR")
add("mod-evolution-benchmark/cohort.csv", "MOD_EVOLUTION20")
with (P / "family-curation/scope.csv").open("w") as f:
    w = csv.DictWriter(f, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
print(
    "Rows",
    len(out),
    "unique accessions",
    len({r["accession"] for r in out}),
    "cohorts",
    collections.Counter(r["cohort"] for r in out),
)
print("Missing species", [r for r in out if not r["species"]])
