"""Derive the dismech entries in scope: Mendelian, eye-restricted vision disorders.

Usage, from the ai-gene-review root with a dismech checkout beside it:

    DISMECH_DIR=../dismech uv run python projects/DISMECH_VISION_ALIGNMENT/build_scope.py

Writes scope.yaml (the flat entry list the audit reads) and scope_decisions.yaml (every
candidate with its decision and reason) next to this script. MONDO and HPO are read from
OBO files, downloaded once into the git-ignored .cache/obo/.

The rule, applied mechanically before the hand decisions in scope_overrides.yaml:

  A. the entry's category is Mendelian, Genetic or unset;
  B. its disease_term is under MONDO:0024458 "disorder of visual system";
  C. it has at least one germline causal gene record (CAUSATIVE or untyped);
  D. it is not a disorder of eye movement or of the eyelids and adnexa;
  E. it is eye-restricted: MONDO does not class it under MONDO:0002254 "syndromic
     disease", and at least 80% of its HPO-bound phenotypes are under HP:0000478
     "Abnormality of the eye".

Phenotype share is a proxy for "non-syndromic", so the borderline entries are decided by
hand, each with a reason. An entry is NONSYNDROMIC, MIXED (a non-syndromic disease whose
entry also carries a recognised syndromic arm) or EXCLUDED.
"""
import collections
import glob
import os
import sys
import urllib.request

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
DM = os.environ.get("DISMECH_DIR", "../dismech")
CACHE = os.environ.get("OBO_CACHE", ".cache/obo")
SOURCES = {"mondo.obo": "https://purl.obolibrary.org/obo/mondo.obo",
           "hp.obo": "https://purl.obolibrary.org/obo/hp.obo"}
VISUAL, SYNDROMIC, HP_EYE, HP_PHENOTYPE = "MONDO:0024458", "MONDO:0002254", "HP:0000478", "HP:0000118"
THRESHOLD = 0.8
Loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


def obo(name):
    """is_a parents, labels and data-version of an OBO file, fetched once."""
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        os.makedirs(CACHE, exist_ok=True)
        req = urllib.request.Request(SOURCES[name], headers={"User-Agent": "curl/8"})
        with urllib.request.urlopen(req, timeout=600) as r, open(path, "wb") as fh:
            fh.write(r.read())
    parents, label, version, cur, term = collections.defaultdict(set), {}, None, None, False
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith("data-version:"):
                version = line.split(":", 1)[1].strip()
            elif line.startswith("["):
                term, cur = line == "[Term]", None
            elif term and line.startswith("id: "):
                cur = line[4:].strip()
            elif term and cur and line.startswith("name: "):
                label[cur] = line[6:]
            elif term and cur and line.startswith("is_a: "):
                parents[cur].add(line[6:].split(" ! ")[0].split(" {")[0].strip())
    return parents, label, version


def ancestors(parents, t, memo={}):
    key = (id(parents), t)
    if key not in memo:
        seen, stack = set(), [t]
        while stack:
            for p in parents.get(stack.pop(), ()):
                if p not in seen:
                    seen.add(p)
                    stack.append(p)
        memo[key] = seen
    return memo[key]


def term_id(x):
    return ((x or {}).get("term") or {}).get("id") if isinstance(x, dict) else None


def main():
    mondo, mondo_label, mondo_version = obo("mondo.obo")
    hp, _, hp_version = obo("hp.obo")
    ov = yaml.load(open(os.path.join(HERE, "scope_overrides.yaml")), Loader=Loader)
    extra, motility = ov["admit_outside_visual_branch"], set(ov["motility_or_adnexal"])
    force_in, force_out = ov["force_in"], ov["force_out"]
    decisions = []
    for path in sorted(glob.glob(os.path.join(DM, "kb/disorders/*.yaml"))):
        slug = os.path.basename(path)[:-5]
        d = yaml.load(open(path), Loader=Loader)
        if not isinstance(d, dict):
            continue
        category, mid = d.get("category"), term_id(d.get("disease_term"))
        anc = ancestors(mondo, mid) | {mid} if mid in mondo_label else set()
        if category not in ("Mendelian", "Genetic", None) and slug not in extra:
            continue
        if VISUAL not in anc and slug not in extra:
            continue
        phen = [term_id(p.get("phenotype_term")) for p in d.get("phenotypes") or []]
        phen = [t for t in phen if t and HP_PHENOTYPE in ancestors(hp, t) | {t}]
        eye = [t for t in phen if HP_EYE in ancestors(hp, t) | {t}]
        genes = sorted({(g.get("gene_term") or {}).get("term", {}).get("label")
                        for g in d.get("genetic") or []
                        if g.get("relationship_type") in ("CAUSATIVE", None)
                        and g.get("variant_origin") in (None, "GERMLINE")
                        and str(term_id(g.get("gene_term")) or "").lower().startswith("hgnc:")} - {None})
        rec = dict(entry=slug, mondo=mid, label=mondo_label.get(mid), category=category,
                   eye_phenotypes=len(eye), phenotypes=len(phen), causal_genes=genes)
        share = len(eye) / len(phen) if phen else None
        if slug in motility:
            rec.update(decision="EXCLUDED", reason="disorder of eye movement or of the eyelids and adnexa")
        elif slug in force_out:
            rec.update(decision="EXCLUDED", reason=force_out[slug])
        elif slug in force_in:
            rec.update(decision=force_in[slug]["class"], reason=force_in[slug]["reason"])
        elif not genes:
            rec.update(decision="EXCLUDED", reason="no germline causal gene record")
        elif SYNDROMIC in anc:
            rec.update(decision="EXCLUDED", reason="MONDO classes it as a syndromic disease")
        elif share is None:
            rec.update(decision="EXCLUDED", reason="no HPO-bound phenotype to judge from")
        elif share >= THRESHOLD:
            rec.update(decision="NONSYNDROMIC", reason="eye-restricted by phenotype share"
                       + (f"; {extra[slug]}" if slug in extra else ""))
        else:
            rec.update(decision="EXCLUDED",
                       reason=f"extra-ocular features: {len(phen) - len(eye)} of {len(phen)} phenotypes")
        decisions.append(rec)
    unknown = (set(force_in) | set(force_out) | set(extra) | motility) - {r["entry"] for r in decisions}
    if unknown:
        sys.exit(f"scope_overrides.yaml names entries the rule never reached: {sorted(unknown)}")
    included = [r["entry"] for r in decisions if r["decision"] != "EXCLUDED"]
    head = dict(mondo_version=mondo_version, hp_version=hp_version, threshold=THRESHOLD,
                visual_root=VISUAL, syndromic_root=SYNDROMIC, hp_eye_root=HP_EYE)
    with open(os.path.join(HERE, "scope_decisions.yaml"), "w") as fh:
        yaml.safe_dump(dict(inputs=head, decisions=decisions), fh, sort_keys=False, width=110)
    with open(os.path.join(HERE, "scope.yaml"), "w") as fh:
        fh.write("# dismech entries in scope for the vision-disorder alignment; one per line.\n"
                 "# Generated by build_scope.py from the rule and scope_overrides.yaml; do not edit by hand.\n")
        yaml.safe_dump(included, fh, default_flow_style=False)
    counts = collections.Counter(r["decision"] for r in decisions)
    print(dict(counts), "in scope:", len(included),
          "distinct causal genes:", len({g for r in decisions if r["decision"] != "EXCLUDED" for g in r["causal_genes"]}))


if __name__ == "__main__":
    main()
