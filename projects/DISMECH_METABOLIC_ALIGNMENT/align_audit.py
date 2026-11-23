"""Audit dismech metabolic entries against ai-gene-review core functions and modules.

For each in-scope disorder and each gene bound in its genetic records, compare the GO
terms on pathograph nodes naming that gene with the gene's AIGR core-function terms
(exact, or related through is_a/part_of ancestry), and find AIGR modules that contain
the gene's UniProt accession. Emits a YAML report with a provenance block.

Usage, from the ai-gene-review root with a dismech checkout beside it:

    # The all-slices run. AIGR_DIR is a tree holding every themed slice of #4690; AIGR_TREE
    # records how it was built, since a bare directory path says nothing once it is gone,
    # and AIGR_REVISION/AIGR_REF record the revision when that tree is not itself a checkout.
    DISMECH_DIR=../dismech AIGR_DIR=<all-slices tree> \
    AIGR_TREE="origin/main with the ten themed slice branches of #4690 merged" \
    uv run python projects/DISMECH_METABOLIC_ALIGNMENT/align_audit.py \
        projects/DISMECH_METABOLIC_ALIGNMENT/scope.yaml \
        projects/DISMECH_METABOLIC_ALIGNMENT/report.yaml

    # The branch-local run, whose only purpose is to be compared against the one above.
    DISMECH_DIR=../dismech AIGR_TREE="this branch alone" \
    uv run python projects/DISMECH_METABOLIC_ALIGNMENT/align_audit.py \
        projects/DISMECH_METABOLIC_ALIGNMENT/scope.yaml \
        projects/DISMECH_METABOLIC_ALIGNMENT/report-branch-local.yaml

    # Both reports are passed to the renderer. The third argument is what makes the
    # comparison section a measurement; with two arguments that section is not printed,
    # so the two-argument form does NOT reproduce the committed page.
    uv run python projects/DISMECH_METABOLIC_ALIGNMENT/make_page.py \
        projects/DISMECH_METABOLIC_ALIGNMENT/report.yaml \
        projects/DISMECH_METABOLIC_ALIGNMENT.md \
        projects/DISMECH_METABOLIC_ALIGNMENT/report-branch-local.yaml

Five properties of the comparison are deliberate, and are stated on the generated page
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
* A node's MF and BP terms are compared against **one pooled set** of the review's core
  molecular functions and ``directly_involved_in`` processes (``core = a["mf"] | a["bp"]``),
  so a node activity term can be satisfied by a core process and the reverse. That pooling
  matters because ``is_a``/``part_of`` ancestry **does** cross between the MF and BP
  aspects: GO asserts ``part_of`` from transporter activities to the transport processes
  they carry out, so e.g. ``GO:0015184`` L-cystine transmembrane transporter activity
  reaches ``GO:0015811`` L-cystine transport, and ``GO:0008137`` reaches ``GO:1902600``.
  Alignments of that shape are real agreement, not artefacts, but they are weaker than a
  same-aspect match and the page says so. Where a particular cross-aspect edge is simply
  absent -- ``GO:0008137`` does not reach ``GO:0006120`` -- that is a fact about the pair,
  not about the aspects.
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
  disulfide relay is the case the second flag exists to catch. Coverage is tested against
  every term anywhere in a module, so a large module satisfies it easily; which aligned
  term matched which module term is recorded in ``covering_pairs``, so an earned coverage
  can be told from one won on a remote ancestor.

Module membership and module GO terms are read from the module structure
(``module.parts[].node.annotons[]``, including protein-complex ``active_units``), not by
regex over the file text, so an accession mentioned only in ``notes`` or in evidence
does not count as membership.
"""
import csv
import datetime
import glob
import hashlib
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


_ASPECT_ROOTS = {"GO:0003674": "MF", "GO:0008150": "BP", "GO:0005575": "CC"}
_aspect_cache = {}
# Collected and re-raised at the end, as anc() does. Swallowing these emptied
# term_aspects, and an empty map made the page print "no matched pair crosses the
# aspects" as a finding - a lookup failure rendering as a result.
_aspect_failures = []
# Terms that resolved but sat under no aspect root, or under several.
_aspect_unresolved = []


def aspect(t):
    """GO aspect of a term, by is_a ancestry to the three roots.

    Recorded per term in the report so the page can derive which matched pairs cross
    between molecular function and biological process. The page used to name three
    examples in hardcoded prose; one of them stopped being cross-aspect when the input
    tree changed, which is the same staleness the figures had.
    """
    if t not in _aspect_cache:
        try:
            up = set(go.ancestors(t, predicates=["rdfs:subClassOf"], reflexive=True))
        except Exception as exc:  # noqa: BLE001 - recorded, then re-raised in aggregate
            _aspect_failures.append((t, f"{type(exc).__name__}: {exc}"))
            up = set()
        hit = [v for k, v in _ASPECT_ROOTS.items() if k in up]
        if up and len(hit) != 1:
            # Resolved, but to no aspect root or to several. Recorded rather than dropped:
            # this was the residue of the old "absence is recorded, not raised" docstring,
            # and a term with no aspect silently leaves term_aspects.
            _aspect_unresolved.append((t, sorted(hit)))
        _aspect_cache[t] = hit[0] if len(hit) == 1 else None
    return _aspect_cache[t]


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


# Flags grouped by *why* they fire, exported so the page can explain a count that moves
# between two runs instead of inferring a cause from the flag's name. The groups are not
# a taxonomy of severity; they are the three places a flag is appended relative to the
# gene-review lookup, which is what decides whether a changed review set can move it.
#
# Deciding this by subtraction ("everything that is not a module flag counts absent
# reviews") was wrong for 85 of 87 rows in one run: AIGR_NOT_COMPLETE and
# NO_CORE_FUNCTION_TERMS both fire where a review *was* found, so they count stub reviews
# present rather than reviews absent.
#
# Decided before the review lookup, so identical between two runs over the same dismech
# tree whatever reviews are present.
REVIEW_INDEPENDENT_FLAGS = ("GENE_ON_NO_NODE", "NO_GO_ON_GENE_NODES", "NO_ORIGIN", "UNTYPED")
# Fires only where no review was found. This is the one flag that counts absence.
REVIEW_ABSENT_FLAGS = ("NO_AIGR_REVIEW",)
# Fires only where a review *was* found and is thin: a stub status, or no comparable
# terms to align against. A rise here means more stub reviews present, not more absent.
REVIEW_PRESENT_THIN_FLAGS = ("AIGR_NOT_COMPLETE", "NO_CORE_FUNCTION_TERMS")
# Computed from the module files, inside the branch where a review was found. A missing
# review removes these rather than adding them, so a rise can only come from the modules.
MODULE_SOURCED_FLAGS = ("NO_MODULE_MEMBERSHIP", "MODULE_NOT_COVERING", "PARTIAL_COVERAGE")
# Which module flags oblige a hand-written reason on the page. Declared here rather than
# derived there by excluding a hardcoded name: the page's enforcement and this list have to
# move together, and a module flag added here without a decision about its reason should
# not silently inherit one. PARTIAL_COVERAGE is out because the row prints the terms no
# module reached, so the reason is in the table; the other two are verdicts about a module
# that only a reader of it can justify. The distinction is obligation, not importance.
REASON_REQUIRING_MODULE_FLAGS = ("NO_MODULE_MEMBERSHIP", "MODULE_NOT_COVERING")
# Flags the page's "clean" count tolerates: ones that qualify a row rather than say the
# alignment failed. Declared, not derived, because deriving it from MODULE_SOURCED_FLAGS
# made "soft" the default for any module flag added later - including one that would mark
# a real contradiction, which would then be absorbed into the clean figure with nothing
# failing. A new flag is hard until it is named here.
SOFT_FLAGS = MODULE_SOURCED_FLAGS + (
    "ALIGNED_NONCORE", "ALIGNED_PROPOSED",
    "PARTIAL_ALIGNMENT", "ALIGNED_CONTRIBUTES_ONLY", "ALIGNED_ON_SHARED_NODE_ONLY",
)
# Everything else is an alignment verdict, computed from the review's terms.
FLAG_GROUPS = dict(
    review_independent=list(REVIEW_INDEPENDENT_FLAGS),
    review_absent=list(REVIEW_ABSENT_FLAGS),
    review_present_thin=list(REVIEW_PRESENT_THIN_FLAGS),
    module_sourced=list(MODULE_SOURCED_FLAGS),
    module_sourced_reason_required=list(REASON_REQUIRING_MODULE_FLAGS),
    soft=list(SOFT_FLAGS),
)
assert set(REASON_REQUIRING_MODULE_FLAGS) <= set(MODULE_SOURCED_FLAGS)
assert set(MODULE_SOURCED_FLAGS) <= set(SOFT_FLAGS)

def _dirty(repo, path=None):
    """True/False for uncommitted changes, or None when git could not answer.

    Tri-state on purpose. bool(_git(...)) made a git failure indistinguishable from a
    clean tree, so an erroring git recorded "clean" and the page's dirtiness clause
    disappeared - a reader then takes the absence as "the revisions name what ran", which
    is the assertion these fields exist to withhold. Same shape as aspect() swallowing a
    lookup failure: the failure renders as a result.
    """
    out = _git(repo, "status", "--porcelain", *(["--", path] if path else []))
    return None if out is None else bool(out)


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
    # AIGR_TREE says how a non-checkout tree was built, because the directory path alone
    # is often a scratch directory that no longer exists when the report is read. Without
    # it the provenance records where the bytes sat rather than what they were.
    aigr_tree=os.environ.get("AIGR_TREE") or None,
    aigr_dir=AG,
    # Which version of this script produced the report. Without it two reports from
    # different script versions are indistinguishable from their provenance, which is how
    # a report predating a field could sit beside one carrying it with nothing to say so.
    audit_revision=_git(AG, "log", "-1", "--format=%h", "--",
                        os.path.relpath(os.path.abspath(__file__), AG)) or None,
    audit_sha256=hashlib.sha256(open(__file__, "rb").read()).hexdigest()[:12],
    # Whether either tree had uncommitted changes when the run was made. Without this a
    # recorded revision can name a tree that is not what ran, which was true of both
    # committed reports: the script was edited after the commit the revision names.
    audit_dirty=_dirty(AG, os.path.relpath(os.path.abspath(__file__), AG)),
    aigr_dirty=_dirty(AG),
    dismech_dirty=_dirty(DM),
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
    mf, mf_contributes, bp = set(), set(), set()
    for cf in d.get("core_functions") or []:
        # Kept apart: enabling an activity and contributing to a complex that has it are
        # different claims, and a row that aligns only on the weaker one says so.
        for k, dest in (("molecular_function", mf),
                        ("contributes_to_molecular_function", mf_contributes)):
            v = cf.get(k)
            if isinstance(v, dict) and v.get("id"):
                dest.add(v["id"])
        for k, dest in (("directly_involved_in", bp),):
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
                     mf=mf, mf_contributes=mf_contributes, bp=bp,
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
# Separate key, since this is a list rather than a count and a reader scanning the
# provenance block wants the counts without 450 stems in the middle of them.
PROVENANCE["modules"] = sorted(mod_terms)

# Parsed with the csv module rather than split(","): a quoted label containing a comma
# would shift every later field and silently yield the wrong symbol.
hgnc_sym = {}
with open(f"{DM}/cache/hgnc/terms.csv", newline="") as fh:
    for row in csv.reader(fh):
        if len(row) >= 2:
            hgnc_sym[row[0].lower()] = row[1]


# HGNC symbols whose AIGR review folder uses a newer symbol than the dismech HGNC cache
# reports. Checked below against the folders actually present, so an entry that has become
# wrong fails the run instead of quietly sending the row to NO_AIGR_REVIEW.
HGNC_RENAMES = {"TMEM251": "LYSET"}

# gid values the dismech HGNC cache cannot resolve to a symbol.
_symbol_failures = []


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
        if gid not in hgnc_sym:
            # Collected and re-raised at the end, as anc() and aspect() are. Falling back
            # to the raw CURIE made an unresolvable id read as NO_AIGR_REVIEW - a lookup
            # failure rendering as a curation gap, which is the one way this table can be
            # wrong without looking wrong.
            _symbol_failures.append((gid, name))
            continue
        sym = hgnc_sym[gid]
        sym = HGNC_RENAMES.get(sym, sym)
        node_mf, node_bp, nodes = set(), set(), []
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
            here.discard(None)
            if len({x for x in ng if x}) > 1:
                shared_terms |= here
                shared_nodes.append(n.get("name"))
            else:
                sole_terms |= here
        node_mf.discard(None); node_bp.discard(None)
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
                        # Which retained non-core term each one matched. aligned_pairs does
                        # this for core matches; without the same record here the page can
                        # name the matched term in prose and nothing can check it.
                        g["aligned_noncore_pairs"] = {
                            t: sorted(k for k in a["kept"] if related(t, k)) for t in noncore}
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
                # Which module term earned the coverage is recorded too, symmetrically
                # with aligned_pairs: coverage tests the aligned terms against every term
                # anywhere in a module, so a large module satisfies it easily, and without
                # the pair a reader cannot tell a relevant match from a remote ancestor.
                covering, covering_pairs = [], {}
                for m in mods:
                    hits = sorted({(t, mt) for t in g["aligned_terms"]
                                   for mt in mod_terms.get(m, ()) if related(t, mt)})
                    if hits:
                        covering.append(m)
                        covering_pairs[m] = [[t, mt] for t, mt in hits]
                g["covering_modules"] = covering
                if covering_pairs:
                    g["covering_pairs"] = covering_pairs
                if not covering:
                    flags.append("MODULE_NOT_COVERING")
                else:
                    # Coverage is existential over (aligned term x module term): one match
                    # anywhere in any module passes the row. So record which aligned terms
                    # no module term reached, and flag a row that is only partly covered -
                    # the same distinction PARTIAL_ALIGNMENT draws for the review side.
                    covered_terms = {pr[0] for v in covering_pairs.values() for pr in v}
                    uncovered = sorted(set(g["aligned_terms"]) - covered_terms)
                    if uncovered:
                        g["uncovered_aligned_terms"] = uncovered
                        flags.append("PARTIAL_COVERAGE")
        g["flags"] = flags
        entry["genes"].append(g)
    report.append(entry)

if _anc_failures:
    for t, exc in _anc_failures[:10]:
        print(f"ancestor lookup failed: {t}: {exc}", file=sys.stderr)
    sys.exit(f"{len(_anc_failures)} GO ancestor lookups failed; every comparison would "
             "degrade to exact match, so no report was written.")

# The flag groups travel in the report so make_page names them from the run rather than
# from prose that can drift out of step with the code.
# Aspect of every term that appears in a matched pair, so the page can derive the
# cross-aspect matches rather than naming examples that can stop being true.
_paired = {t for e in report for g in e.get("genes", [])
           for pair in [(g.get("aligned_pairs") or {})]
           for t, v in pair.items()
           for t in [t] + (v if isinstance(v, list) else [v])}
TERM_ASPECTS = {t: aspect(t) for t in sorted(_paired) if aspect(t)}

if _symbol_failures:
    for gid, ent in _symbol_failures[:5]:
        print(f"unresolvable HGNC id: {gid} ({ent})", file=sys.stderr)
    sys.exit(f"{len(_symbol_failures)} HGNC id(s) did not resolve to a symbol in "
             f"{DM}/cache/hgnc/terms.csv, e.g. {_symbol_failures[:3]}; each would have "
             "read as NO_AIGR_REVIEW, so no report was written.")

# A rename entry is wrong once the old symbol has a review folder of its own: the map
# would then redirect a real review somewhere else. The new symbol having no folder is
# *not* an error - it means that gene is not reviewed in this tree, which is an ordinary
# NO_AIGR_REVIEW. Requiring it broke the run over any tree predating the review, which is
# exactly the second tree this audit is compared against.
_rename_bad = [f"{o}->{n}: {o} now has its own review folder"
               for o, n in HGNC_RENAMES.items() if os.path.isdir(f"{AG}/genes/human/{o}")]
if _rename_bad:
    sys.exit("HGNC_RENAMES is out of step with the review folders: " + "; ".join(_rename_bad))

if _aspect_failures:
    sys.exit(f"GO aspect lookups failed for {len(_aspect_failures)} terms, e.g. "
             f"{_aspect_failures[:3]}; the cross-aspect figures would read as an absence "
             "rather than as a failure")
# Not fatal: a term under no aspect root is a fact about the ontology, not a failed
# lookup. Written unconditionally, including as an empty list, so that "this run resolved
# every term" and "this report predates the field" are different states on the page -
# writing it only when non-empty made an absent key mean both.
PROVENANCE["aspect_unresolved"] = [t for t, _ in _aspect_unresolved]
if _aspect_unresolved:
    print("terms with no single GO aspect root:", _aspect_unresolved[:5],
          f"({len(_aspect_unresolved)} total)")

yaml.safe_dump(dict(provenance=PROVENANCE,
                    review_independent_flags=list(REVIEW_INDEPENDENT_FLAGS),
                    flag_groups=FLAG_GROUPS,
                    term_aspects=TERM_ASPECTS,
                    entries=report),
               open(OUT, "w"), sort_keys=False, width=120)
from collections import Counter

c = Counter(fl for e in report for g in e.get("genes", []) for fl in g["flags"])
print("provenance", PROVENANCE)
print("entries", len(report), "gene-rows", sum(len(e.get("genes", [])) for e in report))
print(dict(c))
print("entries with problem:", [(e["entry"], e["problem"]) for e in report if e.get("problem")])
