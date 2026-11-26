"""Append a compact batch file of curated RHEA->GO calls to rhea2go.sssom.yaml.

Batch file: YAML list of [rhea_id, pred, go_id, comment]; pred is exact | broad (GO term broader) | none
(no GO term at all; go_id is then the best broader term or null). Validates that each GO id is a live
molecular_function term in go-edit.obo and that the reaction is not already in the SSSOM file, and takes
labels from go-edit.obo and the RHEA equation table.

usage: batch_to_sssom.py BATCH.yaml GO_EDIT_OBO DATA_DIR SSSOM.yaml "Section title"
"""
import sys, re, yaml, csv
sys.path.insert(0, sys.argv[0].rsplit("/",1)[0])
from rheago_lib import parse_obo, load_rhea
batch, obo, D, ss, title = sys.argv[1:6]
T = parse_obo(obo); eq, _ = load_rhea(D)
REL = parse_obo(f"{D}/go-basic.obo")  # labels from the released GO, which the term validator uses
def label(go): return REL[go]["name"] if go in REL else T[go]["name"]
have = set(re.findall(r"subject_id: RHEA:(\d+)", open(ss).read()))
P = {"exact": ("skos:exactMatch", "exact match"), "broad": ("skos:broadMatch", "broad match")}
def q(s): return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
out, errs = [f"\n# ===== {title} =====\n"], []
for rid, pred, go, comment in yaml.safe_load(open(batch)):
    rid = str(rid)
    if rid in have: errs.append(f"RHEA:{rid} already in SSSOM"); continue
    if rid not in eq: errs.append(f"RHEA:{rid} not a known reaction"); continue
    t = T.get(go) if go else None
    if go and (not t or t["obs"] or t["ns"] != "molecular_function"):
        errs.append(f"RHEA:{rid} -> {go}: not a live MF term"); continue
    have.add(rid)
    if pred == "none":
        out.append(f"""- subject_id: RHEA:{rid}
  subject_label: {q(eq[rid])}
  predicate_id: skos:exactMatch
  object_id: sssom:NoTermFound
  mapping_justification: semapv:ManualMappingCuration
  comment: {q(comment + (f' Best current broader term: {go} {label(go)}.' if go else ''))}
""")
        if go:
            pred = "broad"
        else:
            continue
    p, pl = P[pred]
    out.append(f"""- subject_id: RHEA:{rid}
  subject_label: {q(eq[rid])}
  predicate_id: {p}
  predicate_label: {pl}
  object_id: {go}
  object_label: {q(label(go))}
  mapping_justification: semapv:ManualMappingCuration
  comment: {q(comment)}
""")
if errs:
    print("\n".join(errs)); sys.exit(1)
open(ss, "a").write("".join(out)); print("appended", len(out) - 1)
