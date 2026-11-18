"""Extract structured review fields beyond actions, for the deep-dive figures.

Outputs (paper/data/):
  predictions.tsv      one row per reviewed computational prediction (*-predictions-review.yaml)
  propagation.tsv      one row per annotation carrying a propagation_review block
  source_defects.tsv   one row per source_defects item on an annotation
  ref_reviews.tsv      one row per reference with a reference_review block
  history.tsv          one row per gene history record (agent, model, date)
"""
import csv, glob, os, sys
from concurrent.futures import ProcessPoolExecutor
import yaml

Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "paper", "data")

def load(path):
    try:
        with open(path) as fh:
            d = yaml.load(fh, Loader=Loader)
        return d if isinstance(d, dict) else None
    except Exception:
        return None

def org_of(path):
    return os.path.relpath(path, ROOT).split(os.sep)[1]

def review(path):
    d = load(path)
    out = {"propagation": [], "source_defects": [], "ref_reviews": []}
    if not d:
        return out
    org, gene = org_of(path), d.get("gene_symbol")
    for a in d.get("existing_annotations") or []:
        if not isinstance(a, dict):
            continue
        r = a.get("review") or {}
        t = a.get("term") or {}
        base = {"organism": org, "gene": gene, "term_id": t.get("id"), "evidence_type": a.get("evidence_type"),
                "reference": a.get("original_reference_id"), "action": r.get("action")}
        pr = r.get("propagation_review")
        if isinstance(pr, dict):
            fm = pr.get("failure_modes") or []
            out["propagation"].append({**base, "root_cause": pr.get("root_cause"),
                                       "failure_modes": "|".join(map(str, fm)) if isinstance(fm, list) else str(fm)})
        for sd in r.get("source_defects") or []:
            if isinstance(sd, dict):
                out["source_defects"].append({**base, "defect_type": sd.get("defect_type"), "resource": sd.get("resource"),
                                              "requested_change": sd.get("requested_change"), "confidence": sd.get("confidence"),
                                              "cause": sd.get("cause")})
    for ref in d.get("references") or []:
        rr = (ref or {}).get("reference_review") if isinstance(ref, dict) else None
        if isinstance(rr, dict):
            rid = ref.get("id") or ""
            out["ref_reviews"].append({"organism": org, "gene": gene, "ref_id": rid, "ref_type": rid.split(":")[0],
                                       "relevance": rr.get("relevance"), "correctness": rr.get("correctness")})
    return out

def predictions(path):
    d = load(path)
    rows = []
    if not d:
        return rows
    for p in d.get("predictions") or []:
        if not isinstance(p, dict):
            continue
        r = p.get("review") or {}
        rows.append({"organism": org_of(path), "gene": d.get("gene_symbol"), "file": os.path.basename(path),
                     "source_method": p.get("source_method"), "source_version": p.get("source_version"),
                     "term_type": p.get("predicted_term_type"), "assessment": r.get("assessment"),
                     "error_type": r.get("error_type")})
    return rows

def history(path):
    d = load(path)
    if not d:
        return None
    s = d.get("session") or {}
    actors = [x for x in s.get("actors") or [] if isinstance(x, dict) and x.get("type") == "ai_agent"]
    a = actors[0] if actors else {}
    ev = [e.get("type") for e in d.get("events") or [] if isinstance(e, dict)]
    t = d.get("target") or {}
    return {"organism": t.get("organism"), "slug": t.get("slug"), "timestamp": s.get("timestamp"),
            "agent_tool": a.get("agent_tool") or a.get("name"), "model": a.get("model"),
            "backfilled": "backfill" in os.path.basename(path).lower() or bool(d.get("backfilled")),
            "events": "|".join(map(str, ev))}

def write(name, rows):
    if not rows:
        print(f"{name}: no rows", file=sys.stderr); return
    keys = list(dict.fromkeys(k for r in rows for k in r))
    with open(os.path.join(OUT, name), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=keys, delimiter="\t"); w.writeheader(); w.writerows(rows)
    print(f"{name}: {len(rows)} rows", file=sys.stderr)

def main():
    os.makedirs(OUT, exist_ok=True)
    revs = sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-ai-review.yaml")))
    preds = sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*predictions-review.yaml")))
    hist = sorted(glob.glob(os.path.join(ROOT, "history", "genes", "*", "*", "*.yaml")))
    agg = {"propagation": [], "source_defects": [], "ref_reviews": []}
    with ProcessPoolExecutor() as ex:
        for out in ex.map(review, revs, chunksize=50):
            for k in agg:
                agg[k].extend(out[k])
        P = [r for rows in ex.map(predictions, preds, chunksize=20) for r in rows]
        H = [r for r in ex.map(history, hist, chunksize=100) if r]
    for k, v in agg.items():
        write(f"{k}.tsv", v)
    write("predictions.tsv", P); write("history.tsv", H)

if __name__ == "__main__":
    main()
