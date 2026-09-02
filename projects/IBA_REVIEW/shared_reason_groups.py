"""Count identical `review.reason` strings shared across annotations.

Exists because the "a shared reason is suspicious only under a corrective action"
paragraph in projects/IBA_REVIEW.md quotes figures that a reader cannot re-derive with
grep: `reason` is usually a folded block scalar, so line-wise tools see fragments, not
values. Every figure in that paragraph should come from this script.

PREDICATE (one, stated here, applied to every figure):
  * group annotations by the EXACT `review.reason` string, across all files in the glob
  * a group qualifies when its rows span >=3 distinct GO term ids
  * counts reported are of ANNOTATION ROWS, not of distinct terms

The threshold is on TERMS, not rows, and that is the whole point: a reason applied three
times to one term under three evidence codes is one judgement recorded three times, not
boilerplate. Spanning >=3 distinct terms means the same sentence is being asked to
justify verdicts on genuinely different annotations. A row threshold would be dead code
here -- >=3 distinct terms already implies >=3 rows -- so there isn't one.

No minimum reason length is applied. Terse tags ("Stale ISO transfer.") count like any
other string; filtering them out is a tuning knob that makes figures irreproducible
unless the cutoff travels with them.

Usage:  python3 projects/IBA_REVIEW/shared_reason_groups.py [glob ...] [--action ACTION] [--list]
Defaults to genes/mouse/*/*-ai-review.yaml.
  --action REMOVE   restrict to rows whose review.action is REMOVE (the scoped figure)
  --list            print each qualifying group: rows, genes, and the reason's first line
  --classify-labels ignore the grouping entirely and print the propagation_review
                    source_label split instead (self / third-party, provenanced or not),
                    which projects/IBA_REVIEW.md quotes. It lives here because the
                    predicate went wrong once while it existed only as prose: matching the
                    gene_symbol anywhere in the label filed five cross-species ortholog
                    labels ("rat Casp3", "Drosophila Nf1") as self-labels.

Exits 2 if the glob matches no files, the self-test fails, or --action names something the
corpus has no rows for. That last case matters more than it looks: a typo ("remove",
"REMOVED") silently filters to nothing, and "0 groups over 0 rows" reads as a clean corpus
rather than as a mistyped flag. A vacuous pass in a tool whose whole output is figures other
people quote is the failure this script exists to prevent, so it is an error, not a zero.

Otherwise exits 0. This is a measurement tool, not a checker -- it has no notion of a finding.
"""
import glob
import re
import sys
from collections import Counter, defaultdict

import yaml

DEFAULT_GLOB = "genes/mouse/*/*-ai-review.yaml"
SCHEMA = "src/ai_gene_review/schema/gene_review.yaml"
MIN_TERMS = 3


def collect(paths, action=None):
    """Return ({reason: [(gene, term_id), ...]}, actions_seen) for rows carrying a reason.

    actions_seen covers every reasoned row in the glob regardless of the filter, so the
    caller can tell "no rows have this action" apart from "no rows qualified".
    """
    groups = defaultdict(list)
    actions_seen = set()
    for path in paths:
        with open(path) as handle:
            doc = yaml.safe_load(handle) or {}
        gene = doc.get("gene_symbol") or path.split("/")[-2]
        for ann in doc.get("existing_annotations") or []:
            review = ann.get("review") or {}
            reason = review.get("reason")
            if not reason:
                continue
            actions_seen.add(review.get("action"))
            if action is not None and review.get("action") != action:
                continue
            groups[reason].append((gene, (ann.get("term") or {}).get("id")))
    return groups, actions_seen


MOD_PREFIXES = ('MGI:', 'RGD:', 'SGD:', 'FB:', 'WB:', 'ZFIN:', 'TAIR:', 'PomBase:',
                'dictyBase:', 'CGD:', 'Xenbase:')
SELF_MARKER = re.compile(r"this gene|the review target itself|the target's own", re.I)
NEGATION = re.compile(r'\bnot\s+(?:the\s+target|[a-z-]+\s+\S)', re.I)
# Every species word the corpus uses in a source_label. The TARGET organism's own words
# are removed per call, so "rat Casp3" is third-party in genes/mouse and a self-label in
# genes/rat. Written from the labels that exist, not from a taxonomy: a species the corpus
# has not yet named is simply not matched, which fails toward self rather than away.
SPECIES_WORDS = ('mouse', 'rat', 'human', 'Drosophila', 'zebrafish', 'budding-yeast',
                 'fission-yeast', 'fly', 'worm', 'chicken', 'bovine', 'Xenopus',
                 'Arabidopsis', 'yeast', r'S\. cerevisiae', r'S\. pombe', r'C\. elegans',
                 r'E\. coli', 'Dictyostelium', 'cerevisiae', 'pombe', 'elegans')
# genes/<organism>/ -> every word a label may use for THAT organism. Several directories
# have more than one: genes/yeast labels say "budding-yeast" and "S. cerevisiae" as well
# as "yeast", and treating only the directory name as its own word filed those foreign.
ORGANISM_WORDS = {
    'mouse': ('mouse',), 'rat': ('rat',), 'human': ('human',),
    'worm': ('worm', r'C\. elegans', 'elegans'),
    'yeast': ('yeast', 'budding-yeast', r'S\. cerevisiae', 'cerevisiae'),
    'SCHPO': ('fission-yeast', r'S\. pombe', 'pombe'),
    'DICDI': ('Dictyostelium',), 'ECOLI': (r'E\. coli', 'coli'),
}
PROVENANCE_VERBS = re.compile(
    r'\bresolv|\bcorroborat|asserted from external knowledge', re.I)


def is_self_label(label, gene_symbol, organism='mouse'):
    """True when the label names the review target itself, so nothing needs establishing.

    Deliberately NOT "the symbol appears in the label". That looser test admitted
    "rat Casp3" in Casp3, "Drosophila Nf1" in Nf1, and an Fbxo2 label whose whole
    content is "not mouse Fbxo2" -- every one a claim about a DIFFERENT gene, and
    exactly the class the provenance rule exists for. A self-label carries an explicit
    marker, or IS the symbol (optionally prefixed with the TARGET organism's own word,
    optionally with a trailing parenthetical), with no foreign-species qualifier and no
    negation.

    The two guards are load-bearing only against a label that ALSO carries a self-marker
    -- "rat Casp3 (this gene)" and "not mouse Bcl2 (this gene)" -- because the equality
    test rejects every other negative case on its own. The self-test pins them there,
    since a guard no arm requires is one refactor from vanishing silently.

    organism is the genes/<organism>/ directory, so this works outside genes/mouse: on a
    rat review "rat Casp3" is the self-label and "mouse Casp3" is the foreign one.
    """
    own = ORGANISM_WORDS.get(organism, (organism,))
    own_lower = {w.replace('\\', '').lower() for w in own}
    foreign_words = [w for w in SPECIES_WORDS if w.replace('\\', '').lower() not in own_lower]
    foreign = re.compile(r'(?<!\w)(' + '|'.join(foreign_words) + r')(?!\w)', re.I)
    if NEGATION.search(label) or foreign.search(label):
        return False
    if SELF_MARKER.search(label):
        return True
    bare = re.sub(r'\s*\(.*\)\s*$', '', label.strip()).lower()
    return bare == gene_symbol.lower() or bare in {f"{w} {gene_symbol}".lower()
                                                   for w in own_lower}


def organism_from_path(path):
    """The genes/<organism>/ directory for a review path, or None if there isn't one.

    None rather than a "mouse" default: defaulting is the hardcoding this predicate was
    just generalised out of, and it would be silent. The caller turns None into exit 2.
    Takes the LAST "genes" segment, so an absolute path with an earlier one still works.
    """
    parts = path.split("/")
    if "genes" not in parts:
        return None
    idx = len(parts) - 1 - parts[::-1].index("genes")
    return parts[idx + 1] if idx + 1 < len(parts) else None


def classify_labels(paths):
    """Return (self_rows, third_provenanced, third_bare) for labelled MOD sources."""
    selfs, prov, bare, unresolved = [], [], [], []
    for path in paths:
        with open(path) as handle:
            doc = yaml.safe_load(handle) or {}
        gene = doc.get("gene_symbol") or path.split("/")[-2]
        organism = organism_from_path(path)
        if organism is None:
            unresolved.append(path)
            continue
        for ann in doc.get("existing_annotations") or []:
            block = (ann.get("review") or {}).get("propagation_review") or {}
            for src in block.get("source_entities") or []:
                sid, label = src.get("source_id", ""), src.get("source_label")
                if not label or not sid.startswith(MOD_PREFIXES):
                    continue
                row = (gene, sid, label)
                if is_self_label(label, gene, organism):
                    selfs.append(row)
                elif PROVENANCE_VERBS.search(src.get("comment") or ""):
                    prov.append(row)
                else:
                    bare.append(row)
    if unresolved:
        raise SystemExit(
            f"cannot tell which organism {len(unresolved)} path(s) belong to - no "
            f"'genes/<organism>/' segment, e.g. {unresolved[0]}. Pass a glob rooted at "
            f"the repository, not one relative to genes/.")
    return selfs, prov, bare


def _known_actions():
    """ActionEnum's permissible values, read from the schema. Empty set if unreadable.

    Read rather than hardcoded so a new action does not turn this tool into a liar; an
    unreadable schema degrades to the corpus-derived check below rather than failing.
    """
    try:
        with open(SCHEMA) as handle:
            schema = yaml.safe_load(handle) or {}
    except OSError:
        return set()
    enum = (schema.get("enums") or {}).get("ActionEnum") or {}
    return set((enum.get("permissible_values") or {}).keys())


def qualifying(groups):
    """Apply the predicate. Returns {reason: rows} for groups that qualify."""
    return {
        reason: rows
        for reason, rows in groups.items()
        if len({term for _gene, term in rows}) >= MIN_TERMS
    }


def action_error(action, actions_seen, known):
    """Message explaining why `action` cannot be measured, or None if it can.

    Split out of main() so the self-test can reach it: a guard with no anchor is one
    refactor away from vanishing while the suite still reports green.
    """
    if action is None or action in actions_seen:
        return None
    if known and action not in known:
        return (f"--action {action!r} is not an ActionEnum value. "
                f"Known: {', '.join(sorted(known))}")
    present = ', '.join(sorted(a for a in actions_seen if a))
    return f"--action {action!r} matches no reasoned row. Present: {present}"


def _self_test():
    """Assert the predicate bites, on constructed input.

    Each arm can fail on its own: loosening MIN_TERMS admits the one-term group,
    tightening it rejects the three-term group, and counting distinct terms rather
    than rows changes the reported number for the qualifying group. The two-row arm
    is the inflation case a rows-based threshold would wave through.
    """
    three_terms = {"r": [("G", "GO:1"), ("G", "GO:2"), ("G", "GO:3")]}
    one_term = {"r": [("G", "GO:1"), ("G", "GO:1"), ("G", "GO:1")]}
    two_terms = {"r": [("G", "GO:1"), ("G", "GO:2"), ("G", "GO:2")]}
    if not qualifying(three_terms):
        return "three rows over three terms should qualify"
    if qualifying(one_term):
        return "three rows on one term should NOT qualify (one judgement, thrice)"
    if qualifying(two_terms):
        return "three rows over only two terms should NOT qualify"
    if len(qualifying(three_terms)["r"]) != 3:
        return "qualifying() must report ROW count, not distinct-term count"

    if not is_self_label("mouse Ccnb1 (this gene)", "Ccnb1"):
        return "an explicit self-marker must count as a self-label"
    if not is_self_label("Grb2", "Grb2"):
        return "a bare symbol must count as a self-label"
    if not is_self_label("mouse Ccne1 (cyclin E1)", "Ccne1"):
        return "a mouse-prefixed symbol with a parenthetical must count as a self-label"
    if is_self_label("rat Casp3", "Casp3"):
        return "a cross-species ortholog must NOT count as a self-label"
    if is_self_label("Drosophila Nf1 (Neurofibromin 1)", "Nf1"):
        return "a fly ortholog must NOT count as a self-label"
    if is_self_label("a mouse F-box family member; not mouse Fbxo2", "Fbxo2"):
        return "a label saying it is NOT the target must NOT count as a self-label"
    if is_self_label("budding-yeast CLB5", "Ccnb1"):
        return "a bare FOREIGN symbol must NOT count as a self-label"
    if is_self_label("zebrafish ednraa", "Ednra"):
        return "a substring-like foreign symbol must NOT count as a self-label"
    # These two arms are the only ones the guards are load-bearing for: each label also
    # carries a self-marker, so without its guard SELF_MARKER would win.
    if is_self_label("rat Casp3 (this gene)", "Casp3"):
        return "a foreign-species qualifier must beat a self-marker (OTHER_SPECIES guard)"
    if is_self_label("not mouse Bcl2 (this gene)", "Bcl2"):
        return "a negation must beat a self-marker (NEGATION guard)"
    # And the predicate must follow the organism, since the section targets the ISO backlog.
    if not is_self_label("rat Casp3", "Casp3", "rat"):
        return "on a rat review, 'rat Casp3' IS the self-label"
    if is_self_label("mouse Casp3", "Casp3", "rat"):
        return "on a rat review, 'mouse Casp3' is the foreign one"

    # An organism directory can own more than one word, and the corpus uses all of them.
    if not is_self_label("budding-yeast CLB5", "CLB5", "yeast"):
        return "'budding-yeast' is one of genes/yeast's own words"
    if not is_self_label("MIM1 (S. cerevisiae), the target's own experimental annotation",
                         "MIM1", "yeast"):
        return "a self-marker phrased 'the target's own' must count, with its own species"

    # The hardest case: a FOREIGN ortholog whose symbol is the same word as the target's.
    # The parenthetical strip removes the species, leaving bare equality to say "self".
    if is_self_label("mim1 (S. pombe, UniProtKB:Q9C1W7)", "MIM1", "yeast"):
        return "a same-symbol ortholog in another species must NOT count as a self-label"
    if is_self_label("ATG12 (Saccharomyces cerevisiae)", "ATG12", "human"):
        return "a same-symbol yeast ortholog in a human file must NOT count as a self-label"

    if organism_from_path("genes/yeast/MIM1/MIM1-ai-review.yaml") != "yeast":
        return "organism_from_path must read the segment after genes/"
    if organism_from_path("/a/genes/b/genes/rat/Casp3/Casp3-ai-review.yaml") != "rat":
        return "organism_from_path must take the LAST genes/ segment"
    if organism_from_path("yeast/MIM1/MIM1-ai-review.yaml") is not None:
        return "a path with no genes/ segment must be unresolvable, not defaulted"

    seen, known = {"REMOVE"}, {"REMOVE", "ACCEPT"}
    if action_error("REMOVE", seen, known) is not None:
        return "an action present in the corpus must be measurable"
    if action_error(None, seen, known) is not None:
        return "no --action must be measurable"
    if "not an ActionEnum value" not in (action_error("remove", seen, known) or ""):
        return "a typo'd action must be rejected as not an ActionEnum value"
    if "matches no reasoned row" not in (action_error("ACCEPT", seen, known) or ""):
        return "a valid action with no rows must be rejected, not reported as zero"
    if action_error("ACCEPT", seen, set()) is None:
        return "an unreadable schema must still reject an action with no rows"

    if parse_argv(["--action", "REMOVE", "--list", "g/*.yaml"]) != (["g/*.yaml"], "REMOVE", True, False):
        return "parse_argv must return patterns, action and --list as given"
    if parse_argv([]) != ([], None, False, False):
        return "an empty argv must parse to no patterns and no action"
    if not isinstance(parse_argv(["--action"]), str):
        return "a trailing --action must be an error, not a whole-corpus run"
    if not isinstance(parse_argv(["--action", "  "]), str):
        return "a blank --action value must be an error, not a whole-corpus run"
    if not isinstance(parse_argv(["--action="]), str):
        return "an empty --action= must be an error, not a whole-corpus run"
    if not isinstance(parse_argv(["--nope"]), str):
        return "an unrecognized flag must be an error"
    return None


def parse_argv(argv):
    """Return (patterns, action, show, classify) or a str explaining why argv is unusable.

    A pure function for the same reason action_error() is one: an inline guard has
    nothing to anchor it, so a refactor can drop it while the self-test stays green.
    The two guards that matter here both turn a mistyped flag into a silent
    whole-corpus run: "--action" as the last token, and an empty value.
    """
    action, show, classify, patterns = None, False, False, []
    rest = list(argv)
    while rest:
        arg = rest.pop(0)
        if arg == "--list":
            show = True
        elif arg == "--classify-labels":
            classify = True
        elif arg == "--action":
            if not rest:
                return "--action needs a value, e.g. --action REMOVE"
            action = rest.pop(0)
        elif arg.startswith("--action="):
            action = arg.split("=", 1)[1]
        elif arg.startswith("--"):
            return f"unrecognized flag: {arg}"
        else:
            patterns.append(arg)
    if action is not None and not action.strip():
        return "--action: empty value. Give an action, e.g. --action REMOVE"
    return patterns, action, show, classify


def main(argv):
    failure = _self_test()
    if failure:
        print(f"self-test failed: {failure}")
        return 2

    parsed = parse_argv(argv)
    if isinstance(parsed, str):
        print(parsed)
        return 2
    patterns, action, show, classify = parsed

    paths = sorted({p for pattern in (patterns or [DEFAULT_GLOB]) for p in glob.glob(pattern)})
    if not paths:
        print(f"no files matched: {' '.join(patterns or [DEFAULT_GLOB])}")
        return 2

    if classify:
        selfs, prov, bare = classify_labels(paths)
        total = len(selfs) + len(prov) + len(bare)
        print(f"{len(paths)} files, {total} labelled MOD sources: {len(selfs)} self, "
              f"{len(prov) + len(bare)} third-party ({len(prov)} with a provenance verb, "
              f"{len(bare)} without)")
        if show:
            by_gene = Counter(g for g, _s, _l in bare)
            print("  third-party without provenance, by gene: "
                  + ", ".join(f"{g} {n}" for g, n in sorted(by_gene.items(), key=lambda kv: (-kv[1], kv[0]))))
            for g, sid, lab in bare:
                print(f"    {g:12} {sid:22} {lab[:60]}")
        return 0

    raw, actions_seen = collect(paths, action)
    problem = action_error(action, actions_seen, _known_actions())
    if problem:
        print(f"{problem} ({len(paths)} files)")
        return 2
    groups = qualifying(raw)
    rows = sum(len(v) for v in groups.values())
    largest = max((len(v) for v in groups.values()), default=0)
    scope = f"action={action}" if action else "all actions"
    print(f"{len(paths)} files, {scope}: {len(groups)} groups over {rows} rows, "
          f"largest {largest} rows")
    if show:
        for reason, members in sorted(groups.items(), key=lambda kv: -len(kv[1])):
            genes = sorted({gene for gene, _term in members})
            print(f"  {len(members):4d}  {','.join(genes)}  :: {reason.splitlines()[0][:70]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
