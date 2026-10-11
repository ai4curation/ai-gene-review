"""Audit dismech metabolic entries against ai-gene-review core functions and modules.

For each in-scope disorder and each gene bound in its genetic records, compare the GO
terms on pathograph nodes naming that gene with the gene's AIGR core-function terms
(exact, or related through is_a/part_of ancestry), and find AIGR modules that contain
the gene's UniProt accession. Emits a YAML report with a provenance block.

Usage, from the ai-gene-review root with a dismech checkout beside it:

    DISMECH_DIR=../dismech uv run python projects/DISMECH_METABOLIC_ALIGNMENT/align_audit.py \
        projects/DISMECH_METABOLIC_ALIGNMENT/scope.yaml \
        projects/DISMECH_METABOLIC_ALIGNMENT/report.yaml
    python3 projects/DISMECH_METABOLIC_ALIGNMENT/make_page.py \
        projects/DISMECH_METABOLIC_ALIGNMENT/report.yaml \
        projects/DISMECH_METABOLIC_ALIGNMENT.md

Two properties of the comparison are deliberate, and are stated on the generated page
because they make this a weak consistency test rather than a strong one:

* ``related()`` is **symmetric** and **unbounded in distance**. It holds when either
  term is an is_a/part_of ancestor of the other, at any depth, so a dismech node bound
  to something broad aligns with a specific core function and the reverse, and two terms
  many levels apart still align. The report records which core term each node term
  matched (``aligned_pairs``) so the distance behind a match can be judged per row.
* A dismech pathophysiology node binds its GO terms at **node level**, and a node may name
  several genes. dismech has no per-gene attribution inside a node, so every term on a
  shared node is read for every gene on it. The report records which of a gene's node terms
  came *only* from a shared node (``shared_node_terms``), so a row whose verdict could rest
  on a co-named partner's activity is visible rather than assumed clean. The
  GLUD1/HADH hyperinsulinism node, which carries both glutamate dehydrogenase activity and
  enzyme inhibitor activity, is the case this field exists to expose.
* ``contributes_to_molecular_function`` is compared **alongside** core molecular function,
  not folded into it: a subunit that contributes to a complex-level activity without
  enabling it is doing the thing the dismech node describes, so excluding it would lose
  real agreement. But the two are different claims, so a node term matching only a
  contributes-to function is recorded in ``aligned_via_contributes_to``, and a row whose
  whole alignment rests on one is flagged ``ALIGNED_CONTRIBUTES_ONLY``.
* Module **membership** says the gene is in some module; it does not say the module is
  about the function the row aligned on. The two are reported separately:
  ``NO_MODULE_MEMBERSHIP`` means no module contains the accession, and
  ``MODULE_NOT_COVERING`` means one does but no annoton for this gene, in any of them,
  carries a GO term related to the aligned terms. AIFM1 sitting in
  ``apoptotic_execution_phase`` while the aligned function is the mitochondrial
  disulfide relay is the case the second flag exists to catch.

Module membership and module GO terms are read from the module structure
(``module.parts[].node.annotons[]``, including protein-complex ``active_units``), not by
regex over the file text, so an accession mentioned only in ``notes`` or in evidence
does not count as membership.
"""
import csv
import datetime
import glob
import json
import os
import re
import subprocess
import sys

import yaml
from oaklib import get_adapter

DM = os.environ.get("DISMECH_DIR", "../dismech")
AG = os.environ.get("AIGR_DIR", ".")
_scope_path = sys.argv[1]
with open(_scope_path) as fh:
    SCOPE = json.load(fh) if _scope_path.endswith(".json") else yaml.safe_load(fh)
OUT = sys.argv[2]

GO_ADAPTER = os.environ.get("GO_ADAPTER", "sqlite:obo:go")
go = get_adapter(GO_ADAPTER)
PRED = ["rdfs:subClassOf", "BFO:0000050"]
_anc = {}
_anc_failures = []


def anc(t):
    """Ancestor closure of a GO term.

    A lookup failure is recorded rather than silently swallowed: if the adapter were
    unavailable, every comparison would degrade to exact match and the page would be
    quietly wrong, so the run aborts at the end if anything failed to resolve.
    """
    if t not in _anc:
        try:
            _anc[t] = set(go.ancestors(t, predicates=PRED, reflexive=True))
        except Exception as exc:  # noqa: BLE001 - recorded, then re-raised in aggregate
            _anc_failures.append((t, f"{type(exc).__name__}: {exc}"))
            _anc[t] = {t}
    return _anc[t]


def related(a, b):
    """True when a and b are the same term, or either is an ancestor of the other.

    Symmetric and distance-unbounded; see the module docstring.
    """
    return a == b or b in anc(a) or a in anc(b)


def _git(repo, *args):
    try:
        return subprocess.run(["git", "-C", repo, *args], capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return None


def _go_version():
    """GO release of the adapter actually in use, read from the ontology itself."""
    try:
        for v in go.ontology_versions("go"):
            if v:
                return v
    except Exception:
        pass
    try:  # sqlite adapters: owl:versionInfo on the ontology document
        import sqlite3
        path = GO_ADAPTER.split(":", 1)[1]
        if path.startswith("obo:"):
            path = os.path.expanduser(f"~/.data/oaklib/{path[4:]}.db")
        rows = sqlite3.connect(path).execute(
            "select value from statements where predicate = 'owl:versionInfo' "
            "and subject like '%go%' limit 1").fetchall()
        if rows:
            return rows[0][0]
    except Exception:
        pass
    return None


PROVENANCE = dict(
    run_date=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    go_adapter=GO_ADAPTER,
    go_version=_go_version(),
    dismech_revision=_git(DM, "rev-parse", "HEAD"),
    dismech_describe=_git(DM, "log", "-1", "--format=%h %cs %s"),
    # AIGR_REVISION / AIGR_REF let the audit record which tree it read when AIGR_DIR is
    # not itself a checkout. The reviews and modules this audit compares are spread over
    # the ten themed branches split out of #4690, so the run behind the committed page
    # reads a tree materialised from the combined branch rather than one worktree.
    aigr_revision=os.environ.get("AIGR_REVISION") or _git(AG, "rev-parse", "HEAD"),
    aigr_branch=os.environ.get("AIGR_REF") or _git(AG, "rev-parse", "--abbrev-ref", "HEAD"),
    aigr_dir=AG,
    scope_entries=len(SCOPE),
)
# Filled in after the modules are read, so the claim that reading module files as text
# overcounts parts is reproducible from a run rather than quoted from a one-off count.
MODULE_COUNTS = {}

# AIGR: symbol -> (uniprot, status, core term sets)
aigr = {}
for p in glob.glob(f"{AG}/genes/human/*/*-ai-review.yaml"):
    sym = os.path.basename(os.path.dirname(p))
    try:
        d = yaml.safe_load(open(p))
    except Exception:
        continue
    mf, mf_contributes, bp, cc = set(), set(), set(), set()
    for cf in d.get("core_functions") or []:
        # Kept apart: enabling an activity and contributing to a complex that has it are
        # different claims, and a row that aligns only on the weaker one says so.
        for k, dest in (("molecular_function", mf),
                        ("contributes_to_molecular_function", mf_contributes)):
            v = cf.get(k)
            if isinstance(v, dict) and v.get("id"):
                dest.add(v["id"])
        for k, dest in (("directly_involved_in", bp), ("locations", cc), ("in_complex", cc)):
            v = cf.get(k) or []
            if isinstance(v, dict):
                v = [v]
            for x in v:
                if isinstance(x, dict) and x.get("id"):
                    dest.add(x["id"])
    # Terms the review keeps as existing annotations but does not treat as core: used to
    # tell "consistent with a non-core function" from "no match". NEW is held separately,
    # because a NEW term is proposed by the review, not an annotation the review keeps.
    kept, proposed = set(), set()
    for a in d.get("existing_annotations") or []:
        act = ((a.get("review") or {}).get("action") or "")
        tid_ = (a.get("term") or {}).get("id")
        if not tid_ or a.get("negated"):
            continue
        if act in ("ACCEPT", "KEEP_AS_NON_CORE"):
            kept.add(tid_)
        elif act == "NEW":
            proposed.add(tid_)
    aigr[sym] = dict(uniprot=d.get("id"), status=d.get("status"),
                     mf=mf, mf_contributes=mf_contributes, bp=bp, cc=cc,
                     kept=kept, proposed=proposed)


def _annoton_terms(an):
    """GO term ids a module annoton asserts (its function, processes and locations).

    `ModuleAnnoton` carries exactly `function`, `processes` and `locations`; it has no
    `inputs`/`outputs`, and `ProteinComplexDescriptor` has only `active_units`. Earlier
    versions also read `inputs`, `outputs` and a complex's `components`, none of which
    exist in the schema, so those branches never fired.
    """
    out = set()
    f = an.get("function")
    if isinstance(f, dict):
        out.add((f.get("term") or {}).get("id"))
    for k in ("processes", "locations"):
        for x in an.get(k) or []:
            if isinstance(x, dict):
                out.add((x.get("term") or {}).get("id"))
    pc = (an.get("participant") or {}).get("protein_complex") or {}
    for sub in pc.get("active_units") or []:
        if isinstance(sub, dict):
            out |= _annoton_terms(sub)
    out.discard(None)
    return {t for t in out if str(t).startswith("GO:")}


def _participant_curies(part):
    """Every identifier CURIE a module participant names, across all selector shapes.

    `FAMILY` is the most common selector in this corpus, and it names its proteins as
    `family.representative_members[].term`, not as a `gene_product`. Reading only
    `gene_product` would miss most parts: LIPA is a representative member of
    PANTHER:PTHR11005:SF26 in ldl_receptor_mediated_endocytosis, so it would read as
    belonging to no module at all. A `PROTEIN_COMPLEX` selector nests a participant per
    subunit, each typically a FAMILY, which is how ABCG5 and ABCG8 are named.

    This returns raw CURIEs and leaves the UniProtKB filtering to the caller, so that
    the recursion cannot strip a prefix the next level up is still matching on.
    """
    out = set()
    if not isinstance(part, dict):
        return out
    # Every `ParticipantSelector` slot that names a protein identity. `homolog_of` is a
    # `GeneDescriptor` like `ortholog_of`, so omitting it would make a gene named only
    # that way read as a member of nothing.
    for key in ("gene_product", "gene", "ortholog_of", "homolog_of"):
        v = part.get(key)
        if isinstance(v, dict):
            out.add((v.get("term") or {}).get("id"))
    fam = part.get("family") or {}
    for mem in fam.get("representative_members") or []:
        if isinstance(mem, dict):
            out.add((mem.get("term") or {}).get("id"))
    pc = part.get("protein_complex") or {}
    for sub in pc.get("active_units") or []:
        if isinstance(sub, dict):
            out |= _participant_curies(sub.get("participant") or sub)
    out.discard(None)
    return out


def _annoton_accessions(an):
    """UniProt accessions a module annoton's participant names."""
    return {c.split(":", 1)[1] for c in _participant_curies(an.get("participant") or {})
            if str(c).startswith("UniProtKB:")}


def _walk_annotons(obj):
    """Every annoton anywhere in a module, however deeply nested.

    A node may hold `annotons`, nested `parts`, or `variant_sets` whose variants hold
    their own annotons (FBP1 is reached only through a variant set, and the glucose
    release step only through nested parts). Walking just `parts[].node.annotons` would
    silently drop those genes and report them as belonging to no module.
    """
    if isinstance(obj, dict):
        for an in obj.get("annotons") or []:
            if isinstance(an, dict):
                yield an
        for key in ("parts", "variant_sets", "variants", "nodes"):
            for sub in obj.get(key) or []:
                yield from _walk_annotons(sub)
        node = obj.get("node")
        if isinstance(node, dict):
            yield from _walk_annotons(node)
    elif isinstance(obj, list):
        for sub in obj:
            yield from _walk_annotons(sub)


# accession -> set of module names it is a part of, and module name -> all its GO terms.
# Coverage is judged against the module's whole term set rather than against the gene's
# own annoton: asking whether this module is about the aligned function is the useful
# question, and the narrower test produced false positives wherever a module asserts a
# subunit's role with a different term from the one the dismech node used (MT-ND1 as
# ubiquinone binding, NDUFS7 as NADH dehydrogenase activity, against complex I nodes
# bound to NADH:ubiquinone oxidoreductase activity and 4Fe-4S cluster binding).
def _concept_terms(obj):
    """GO terms declared as `concepts` anywhere in a module.

    A module states its scope as process-level concepts, at module level and on each
    node, while its annotons carry the molecular functions of individual parts. Reading
    annotons alone therefore misses what the module is *about*: peroxisome-lifecycle's
    annotons carry PTS-binding, ubiquitin-ligase and ATPase activities, and only its
    concepts carry peroxisome organization and protein import into the peroxisome
    matrix, which are the terms the dismech PEX nodes use.
    """
    out = set()
    if isinstance(obj, dict):
        for c in obj.get("concepts") or []:
            if isinstance(c, dict):
                out.add((c.get("term") or {}).get("id"))
        for v in obj.values():
            if isinstance(v, (dict, list)):
                out |= _concept_terms(v)
    elif isinstance(obj, list):
        for v in obj:
            out |= _concept_terms(v)
    out.discard(None)
    return {t for t in out if str(t).startswith("GO:")}


mod_by_acc = {}
mod_terms = {}
# Per-module counts of accessions reached structurally against accessions appearing
# anywhere in the file text, so the gap between the two is a measured figure.
_ACC_RE = re.compile(r"UniProtKB:([A-Z0-9]+)")
structural_accs = textual_accs = 0
for p in glob.glob(f"{AG}/modules/*.yaml"):
    mname = os.path.basename(p)[:-5]
    try:
        md = yaml.safe_load(open(p))
    except Exception:
        continue
    mod = md.get("module") or {}
    terms, accs = _concept_terms(mod), set()
    for an in _walk_annotons(mod):
        terms |= _annoton_terms(an)
        accs |= _annoton_accessions(an)
    mod_terms[mname] = terms
    for acc in accs:
        mod_by_acc.setdefault(acc, set()).add(mname)
    structural_accs += len(accs)
    textual_accs += len(set(_ACC_RE.findall(open(p).read())))  # unique, as accs is

MODULE_COUNTS = dict(modules_read=len(mod_terms),
                     accessions_as_parts=structural_accs,
                     accessions_in_file_text=textual_accs)
PROVENANCE["module_accessions"] = MODULE_COUNTS

# Parsed with the csv module rather than split(","): a quoted label containing a comma
# would shift every later field and silently yield the wrong symbol.
hgnc_sym = {}
with open(f"{DM}/cache/hgnc/terms.csv", newline="") as fh:
    for row in csv.reader(fh):
        if len(row) >= 2:
            hgnc_sym[row[0].lower()] = row[1]


def tid(x):
    if isinstance(x, dict):
        t = x.get("term") or {}
        return t.get("id")
    return None


report = []
for name in SCOPE:
    f = f"{DM}/kb/disorders/{name}.yaml"
    if not os.path.exists(f):
        report.append(dict(entry=name, problem="FILE_MISSING"))
        continue
    d = yaml.safe_load(open(f))
    genes = []
    for r in d.get("genetic") or []:
        gid = tid(r.get("gene_term"))
        if gid and gid.lower().startswith("hgnc:"):
            genes.append((gid.lower(), r.get("relationship_type"), r.get("variant_origin")))
    entry = dict(entry=name, genes=[])
    if not genes:
        entry["problem"] = "NO_GENE_RECORD"
    for gid, rel, origin in genes:
        sym = hgnc_sym.get(gid, gid)
        sym = {"TMEM251": "LYSET"}.get(sym, sym)  # HGNC rename; AIGR folder uses current symbol
        node_mf, node_bp, node_cc, nodes = set(), set(), set(), []
        # A node binds its GO terms at node level and may name several genes, and dismech
        # has no per-gene attribution inside a node. So terms on a shared node are read
        # for every gene on it, and the two provenances are tracked apart: `shared_terms`
        # minus `sole_terms` is the set this gene holds *only* because a partner was
        # named on the same node.
        sole_terms, shared_terms, shared_nodes = set(), set(), []
        for n in d.get("pathophysiology") or []:
            ng = [(tid(g) or "").lower() for g in n.get("genes") or []]
            if isinstance(n.get("gene"), dict):
                ng.append((tid(n["gene"]) or "").lower())
            gc = n.get("genetic_context") or {}
            for k in ("gene", "gene_term"):
                if isinstance(gc.get(k), dict):
                    ng.append((tid(gc[k]) or "").lower())
            if gid not in ng:
                continue
            nodes.append(n.get("name"))
            here = set()
            for x in n.get("molecular_functions") or []:
                node_mf.add(tid(x)); here.add(tid(x))
            for x in n.get("biological_processes") or []:
                node_bp.add(tid(x)); here.add(tid(x))
            for k in ("cellular_components", "locations"):
                for x in n.get(k) or []:
                    node_cc.add(tid(x))
            here.discard(None)
            if len({x for x in ng if x}) > 1:
                shared_terms |= here
                shared_nodes.append(n.get("name"))
            else:
                sole_terms |= here
        node_mf.discard(None); node_bp.discard(None); node_cc.discard(None)
        a = aigr.get(sym)
        g = dict(gene=sym, hgnc=gid, relationship=rel, origin=origin, nodes=len(nodes))
        flags = []
        if rel is None:
            flags.append("UNTYPED")
        if origin is None:
            flags.append("NO_ORIGIN")
        if not nodes:
            flags.append("GENE_ON_NO_NODE")
        if not node_mf and not node_bp:
            flags.append("NO_GO_ON_GENE_NODES")
        if a is None:
            flags.append("NO_AIGR_REVIEW")
        else:
            g["aigr_status"] = a["status"]
            if a["status"] != "COMPLETE":
                flags.append("AIGR_NOT_COMPLETE")
            core = a["mf"] | a["bp"]
            contributes = a["mf_contributes"]
            comparable = core | contributes
            dm = node_mf | node_bp
            # Node terms this gene holds only because a partner shares one of its nodes.
            only_shared = sorted((shared_terms - sole_terms) & dm)
            if only_shared:
                g["shared_node_terms"] = only_shared
                g["shared_nodes"] = sorted({n for n in shared_nodes if n})
            if dm and not comparable:
                # Nothing to compare against. Without a flag this row would print "ok".
                flags.append("NO_CORE_FUNCTION_TERMS")
            if dm and comparable:
                pairs, contrib_only = {}, []
                for t in sorted(dm):
                    hits = sorted(c for c in core if related(t, c))
                    if hits:
                        pairs[t] = hits
                        continue
                    # Falls back to contributes-to, and says so: a subunit contributing
                    # to a complex-level activity is doing what the node describes, but
                    # it is a weaker claim than enabling the activity itself.
                    chits = sorted(c for c in contributes if related(t, c))
                    if chits:
                        pairs[t] = chits
                        contrib_only.append(t)
                aligned = sorted(pairs)
                g["aligned_terms"] = aligned
                # Which core term each node term matched, so the unbounded ancestry
                # distance behind a match is visible rather than assumed small.
                if pairs:
                    g["aligned_pairs"] = {t: (v[0] if len(v) == 1 else v) for t, v in pairs.items()}
                if contrib_only:
                    g["aligned_via_contributes_to"] = sorted(contrib_only)
                    if len(contrib_only) == len(aligned):
                        flags.append("ALIGNED_CONTRIBUTES_ONLY")
                if aligned and set(aligned) <= set(only_shared):
                    # Every term this row aligned on came from a node it shares with
                    # another gene, so the verdict may rest on a partner's activity.
                    flags.append("ALIGNED_ON_SHARED_NODE_ONLY")
                if not aligned:
                    noncore = sorted(t for t in dm if any(related(t, k) for k in a["kept"]))
                    prop = sorted(t for t in dm if any(related(t, k) for k in a["proposed"]))
                    if noncore:
                        g["aligned_noncore_terms"] = noncore
                        flags.append("ALIGNED_NONCORE")
                    elif prop:
                        g["aligned_proposed_terms"] = prop
                        flags.append("ALIGNED_PROPOSED")
                    else:
                        flags.append("NO_GO_ALIGNMENT")
                g["dismech_only"] = sorted(dm - set(aligned))
                if aligned and g["dismech_only"]:
                    # Agreement is partial: dismech models something the review's core
                    # functions do not cover. Flagged so a partly-matching row cannot
                    # read as a fully clean one.
                    flags.append("PARTIAL_ALIGNMENT")
            mods = sorted(mod_by_acc.get(a["uniprot"], ()))
            g["modules"] = mods
            if not mods:
                flags.append("NO_MODULE_MEMBERSHIP")
            elif g.get("aligned_terms"):
                # Membership is not coverage: the gene may be in a module about a
                # different one of its functions than the one this row aligned on.
                covering = sorted(m for m in mods if any(
                    related(t, mt) for t in g["aligned_terms"] for mt in mod_terms.get(m, ())))
                g["covering_modules"] = covering
                if not covering:
                    flags.append("MODULE_NOT_COVERING")
        g["flags"] = flags
        entry["genes"].append(g)
    report.append(entry)

if _anc_failures:
    for t, exc in _anc_failures[:10]:
        print(f"ancestor lookup failed: {t}: {exc}", file=sys.stderr)
    sys.exit(f"{len(_anc_failures)} GO ancestor lookups failed; every comparison would "
             "degrade to exact match, so no report was written.")

yaml.safe_dump(dict(provenance=PROVENANCE, entries=report),
               open(OUT, "w"), sort_keys=False, width=120)
from collections import Counter

c = Counter(fl for e in report for g in e.get("genes", []) for fl in g["flags"])
print("provenance", PROVENANCE)
print("entries", len(report), "gene-rows", sum(len(e.get("genes", [])) for e in report))
print(dict(c))
print("entries with problem:", [(e["entry"], e["problem"]) for e in report if e.get("problem")])
