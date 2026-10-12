"""Render the dismech<->AIGR alignment audit as a markdown project page."""
import sys

import yaml


def load(path):
    """Return (provenance, entries, review-independent flag names) for a report."""
    d = yaml.safe_load(open(path))
    # Both committed reports are now produced by the current script, so the old leniency
    # here - added when the all-slices report could not be regenerated from this branch -
    # is gone: a missing key is a superseded report and the callers exit on it.
    if isinstance(d, dict):
        prov = dict(d.get("provenance") or {})
        # Carried on the provenance mapping so the renderer reads the groups the run
        # recorded rather than a copy of them kept here.
        # Keyed on presence, not truthiness: an empty map is a run that matched no pairs,
        # which is a different fact from a report that predates the key. Gating on
        # truthiness made the two indistinguishable and left the empty-case branch below
        # unreachable, so a legitimate empty run was told its script was superseded.
        if "flag_groups" in d:
            prov["_flag_groups"] = d["flag_groups"]
        if "term_aspects" in d:
            prov["_term_aspects"] = d["term_aspects"]
        return (prov, d.get("entries") or [],
                tuple(d.get("review_independent_flags") or ()))
    return {}, d, ()


PROV, rep, _INDEP = load(sys.argv[1])
out = sys.argv[2]
# Optional third argument: a second report over the same scope, whose counts the
# provenance section compares against this one's. Passing it is what makes the
# branch-local comparison a measurement; without it the comparison is simply not printed,
# which is the right behaviour once every slice has merged and there is nothing to compare.
ALT_PATH = sys.argv[3] if len(sys.argv) > 3 else None
ALT_PROV, ALT_REP, ALT_INDEP = load(ALT_PATH) if ALT_PATH else ({}, [], ())


def flag_counts(entries):
    """Flag -> occurrences over every gene row, and the row total."""
    c, n = {}, 0
    for e in entries:
        for g in e.get("genes") or []:
            n += 1
            for f in g.get("flags") or []:
                c[f] = c.get(f, 0) + 1
    return c, n


def flag_rows(entries, flag):
    """The set of (entry, gene) rows carrying `flag`.

    The comparison the steady branch needs. Counts are not identity: two runs can report
    the same number of occurrences over wholly different rows, which is exactly what
    PARTIAL_COVERAGE does here - 14 against 14, with 9 rows shared and 5 distinct on each
    side. Any explanation attached to a steady *count* inherits that ambiguity, so the
    page compares the row sets and says which case it is.
    """
    return {(e.get("entry"), g.get("gene"))
            for e in entries for g in e.get("genes", []) if flag in (g.get("flags") or ())}


def alt_comparison():
    """The second report's flag counts against this one's, derived rather than quoted.

    Nothing is printed without a second report, so once every slice has merged and there
    is no second tree to compare, the paragraph disappears instead of going stale. The
    previous version of this section hardcoded six numbers in this file, which made the
    one artifact added to support the disclosure the one artifact nobody could check.
    """
    if not ALT_REP:
        return []
    here, n_here = flag_counts(rep)
    there, n_there = flag_counts(ALT_REP)
    if n_here != n_there:
        # The comparison's whole premise is that the two runs cover the same rows, so a
        # mismatch is a bug in the scope or the trees, not something to paper over.
        sys.exit(f"report row counts differ ({n_here} vs {n_there}); the two runs do not "
                 "cover the same scope and cannot be compared flag by flag")
    # No fallback copy of the audit's set: a second copy here is the drift the export was
    # added to prevent, moved from prose into code. A report without the field cannot be
    # compared, and saying so is stricter and matches how MODULE_REASONS fails.
    if not ALT_INDEP:
        sys.exit("the second report has no review_independent_flags; it was produced by a "
                 "superseded align_audit.py and cannot be compared - re-run the audit")
    # The exact check the presence tests below were a proxy for: same script, same report
    # semantics. Two reports from different script versions cannot be compared flag by flag.
    if not (PROV.get("audit_sha256") and ALT_PROV.get("audit_sha256")):
        # Required, not optional: a conditional check lets a report without the field fall
        # back on the presence proxies, when the other three fields are hard requirements.
        sys.exit("a report carries no audit_sha256; it was produced by a superseded "
                 "align_audit.py and the two cannot be shown to come from one script")
    if PROV["audit_sha256"] != ALT_PROV["audit_sha256"]:
        sys.exit(f"the two reports were produced by different align_audit.py versions "
                 f"({PROV['audit_sha256']} vs {ALT_PROV['audit_sha256']}); their flags are "
                 "not necessarily comparable - re-run both from one script")
    if _INDEP and set(_INDEP) != set(ALT_INDEP):
        # Otherwise two reports could disagree about which flags are review-independent and
        # the identity guard below would silently be checking the wrong set.
        sys.exit("the two reports disagree about which flags are review-independent "
                 f"({sorted(set(_INDEP) ^ set(ALT_INDEP))}); they come from different "
                 "align_audit.py versions and cannot be compared")
    indep = ALT_INDEP
    # Enforced, not asserted: these are the flags decided before the gene review is read,
    # so they must be identical between two runs over the same dismech tree. If one moves,
    # the difference is not the review set and the explanation below would be wrong.
    moved = [f for f in indep if here.get(f, 0) != there.get(f, 0)]
    if moved:
        sys.exit("flags that do not read a gene review differ between the two reports "
                 f"({', '.join(moved)}); the difference between the runs is not the review "
                 "set, so the explanation on the page would be false")
    rose = sorted(f for f in set(here) | set(there)
                  if there.get(f, 0) > here.get(f, 0) and f not in indep)
    fell = sorted(f for f in set(here) | set(there)
                  if there.get(f, 0) < here.get(f, 0) and f not in indep)

    def pairs(fs):
        return ", ".join(f"`{f}` {there.get(f, 0)} against {here.get(f, 0)}" for f in fs)

    tree = ALT_PROV.get("aigr_tree") or ALT_PROV.get("aigr_branch") or "a second tree"
    mods_here = (PROV.get("module_accessions") or {}).get("modules_read")
    mods_there = (ALT_PROV.get("module_accessions") or {}).get("modules_read")
    # Each risen flag is explained by the group it belongs to, read from the report rather
    # than inferred by subtraction. The previous version split the rises into "module
    # flags" and "everything else", and told the reader everything else counted *absent*
    # reviews - wrong for AIGR_NOT_COMPLETE and NO_CORE_FUNCTION_TERMS, which fire where a
    # review was found, and so wrong for 85 of 87 rows in the run it was written against.
    groups = ALT_PROV.get("_flag_groups")
    if "_flag_groups" not in ALT_PROV:
        sys.exit("the second report has no flag_groups; it was produced by a superseded "
                 "align_audit.py and its risen flags cannot be explained - re-run the audit")
    if not groups:
        # Present but empty is a separate failure from absent, and unlike term_aspects it is
        # never legitimate: without the groups every risen flag falls through to "cause not
        # established", which would read as a finding rather than as a broken input.
        sys.exit("the second report's flag_groups is empty; every risen flag would be reported "
                 "as unexplained rather than grouped - re-run the audit")
    if "_term_aspects" not in ALT_PROV:
        # Not read for the cross-aspect figures, which come from the primary report, but a
        # second report missing it is a superseded one and the two are then not comparable.
        sys.exit("the second report has no term_aspects; it was produced by a superseded "
                 "align_audit.py - re-run the audit")
    absent = tuple(groups.get("review_absent") or ())
    thin = tuple(groups.get("review_present_thin") or ())
    modular = tuple(groups.get("module_sourced") or ())
    rose_absent = [f for f in rose if f in absent]
    rose_thin = [f for f in rose if f in thin]
    rose_mod = [f for f in rose if f in modular]
    rose_other = [f for f in rose if f not in absent + thin + modular]

    def names(fs):
        return ", ".join(f"`{f}`" for f in fs)

    out = [
        f"The audit also runs over {tree}, and comparing the two runs shows which flags are",
        "artifacts of the missing slices rather than findings. Both cover the same",
        f"{n_here} gene rows. Flags that fall: {pairs(fell)}. Flags that rise: {pairs(rose)}.",
        "",
        f"The falls - {names(fell)} - are the absent reviews: a row with no review is skipped by",
        "every later test, so it cannot be found partial, shared-node-only, or outside a module.",
    ]
    # A module flag can fall for the review reason (its row was skipped) but could also fall
    # because modules were added, and this sentence cannot tell those apart - so it says so
    # rather than asserting the review cause for a flag whose source is the module files.
    fell_mod = [f for f in fell if f in modular]
    if fell_mod:
        out += ["", f"That reading is exact for the alignment flags. {names(fell_mod)} is"
                    " module-sourced, so it falls here because the rows carrying it were skipped"
                    " for want of a review - but a module flag can also fall because modules were"
                    " added, and this comparison does not distinguish the two."]
    out += ["", "The rises have three different causes, and only one of them is that absence."]
    if rose_absent:
        out += ["", f"- {names(rose_absent)} counts rows with no review at all. This is the only"
                    " risen flag the missing slices raise directly."]
    if rose_thin:
        verb = "fire" if len(rose_thin) > 1 else "fires"
        out += ["", f"- {names(rose_thin)} {verb} where a review **was** found and is thin: a stub"
                    " status, or no core-function terms to compare against. These count stub"
                    " reviews present on the second tree, not reviews missing from it - a"
                    " different claim, and the larger share of the movement."]
    if rose_mod:
        _mw = {1: "The one module flag is", 2: "Both module flags are"}.get(
            len(modular), f"All {len(modular)} module flags are")
        line = (f"- {names(rose_mod)} cannot have either cause. {_mw} computed"
                " only once a review has been found, so a missing review **removes** one rather"
                " than adding it. The driver is the module files:")
        if mods_here and mods_there:
            line += (f" the second run reads {mods_there} modules against {mods_here} here, so"
                     " fewer are available to cover a gene's aligned terms.")
        # Nesting is a set question, not a count question: 448 < 451 is equally consistent
        # with the smaller tree being a subset. Derived from the recorded module lists, and
        # simply not claimed when a report does not carry them.
        here_mods = set(PROV.get("modules") or ())
        there_mods = set(ALT_PROV.get("modules") or ())
        if here_mods and there_mods:
            only_there = sorted(there_mods - here_mods)
            only_here = sorted(here_mods - there_mods)
            if only_there and only_here:
                line += (f" The two sets are not nested either way: {len(only_here)} modules are"
                         f" here and not there, and {len(only_there)} there and not here"
                         f" (e.g. `{only_here[0]}` and `{only_there[0]}`).")
            elif only_here:
                line += (f" The second set is a strict subset: {len(only_here)} modules are here"
                         f" and not there (e.g. `{only_here[0]}`), and none the other way.")
            elif only_there:
                line += (f" This set is the strict subset: {len(only_there)} modules are there and"
                         f" not here (e.g. `{only_there[0]}`).")
            else:
                line += " The two runs read the same module set, so the counts above must differ for another reason."
        else:
            line += (" Whether the two module sets are nested is not derivable here, since at"
                     " least one report does not record which modules it read.")
        out += ["", line]
    if rose_other:
        # Not silently folded into one of the groups above: an unclassified flag would
        # otherwise inherit whichever explanation it happened to land next to.
        out += ["", f"- {names(rose_other)} is not in any group this page knows how to explain;"
                    " its cause has not been established here."]
    steady = sorted(f for f in set(here) | set(there)
                    if f not in indep and here.get(f, 0) == there.get(f, 0) and here.get(f, 0))
    if steady:
        steady_mod = [f for f in steady if f in modular]
        steady_rev = [f for f in steady if f not in modular]
        verb = "are" if len(steady) > 1 else "is"
        out += ["", f"{names(steady)} {verb} identical in **total** in both runs while depending"
                    " on a review, so they appear in neither list above. An equal total is not an"
                    " equal set of rows, and the difference matters here, so each is compared row"
                    " by row below rather than read off the count."]
        # Counts only say the totals match. Whether the same rows carry the flag is a
        # different question, asked here rather than inferred - and asked before any
        # interpretation is offered, because "a stable property of the dismech side" is not
        # even available as a reading for a flag whose rows moved.
        same_rows, moved_rows = [], []
        for f in steady:
            (same_rows if flag_rows(rep, f) == flag_rows(ALT_REP, f) else moved_rows).append(f)
        if same_rows:
            out += ["", f"{names(same_rows)} {'are' if len(same_rows) > 1 else 'is'} identical row"
                        " for row as well: the same (entry, gene) rows carry the flag on each"
                        " tree."]
            _sr = [f for f in same_rows if f in steady_rev]
            if _sr:
                out += [f"For {names(_sr)} that is either a stable property of the dismech side or"
                        " a path these two runs do not separate; this comparison cannot tell"
                        " which."]
        for f in moved_rows:
            a_, b_ = flag_rows(rep, f), flag_rows(ALT_REP, f)
            shared, only_a, only_b = a_ & b_, sorted(a_ - b_), sorted(b_ - a_)

            def _show(rows):
                # A gene can hold two rows in one entry or sit in two entries, so a bare
                # symbol list would print the same name twice with nothing to tell the rows
                # apart. The entry is added only where the symbol repeats.
                dup = {g for g in (g for _, g in rows) if [x for _, x in rows].count(g) > 1}
                return ", ".join(f"{g} ({e})" if g in dup else g for e, g in rows[:5])

            out += ["", f"`{f}` has the same total in both runs over **different rows**:"
                        f" {len(shared)} shared, {len(only_a)} only here"
                        f" ({_show(only_a)}"
                        + (", ..." if len(only_a) > 5 else "") + ") and"
                        f" {len(only_b)} only in the second run"
                        f" ({_show(only_b)}"
                        + (", ..." if len(only_b) > 5 else "") + "). The equal count is a"
                        " coincidence of two populations, so nothing about stability follows"
                        " from it."
                        + (" Being module-sourced, that is what a differing module set does: a"
                           " row drops out where its covering module is absent and another"
                           " appears where one is." if f in modular else "")]
        if steady_mod and not moved_rows:
            # Only sayable once the row sets have been compared, which is why it is here
            # rather than attached to the count.
            out += [f"{names(steady_mod)} is module-sourced, so a count stable across two"
                    " different module sets would otherwise prove nothing; here the rows are"
                    " the same ones, which does mean their covering modules are present in both"
                    " trees."]
    out += [
        "",
        "The flags decided before any review is read are identical in both runs",
        f"({', '.join('`%s` %d' % (f, here.get(f, 0)) for f in indep)}), which is what separates",
        "missing inputs from the script behaving differently - and that identity is enforced",
        "rather than stated: the generator exits if one of those counts moves, or if the two runs",
        "do not cover the same rows. So a second run tests that the audit works; only the",
        "all-slices tree gives the figures this table reports.",
        "",
    ]
    return out

# Recorded justifications for flags that are deliberate, keyed (entry, gene) or (entry, None).
NOTES = {
    ("Inborn_Disorder_of_Bile_Acid_Synthesis", None): "Grouping-like entry; genes are carried by its subtypes.",
    ("Triglyceride_Storage_Disease_Type_1", None): "Historical OMIM:190420 phenotype; no gene has been reported (ABHD5 content lives in Dorfman_Chanarin_Disease).",
    ("Vitamin_D-Dependent_Rickets_Type_2B", None): "Genetic basis unknown; HNRNPC is modelled as a mechanism actor, not a causal gene.",
}
# Keyed by gene symbol. Every principal row carrying a module flag must appear here, or
# the run fails: the page claims each such gene has a stated reason, so that claim is
# enforced rather than asserted. A key may name several genes separated by " / ".
MODULE_REASONS = {
    "TRMT10C": "RNase P partners (HSD17B10, PRORP, ELAC2) lack completed reviews.",
    "ANGPTL3": "No LPL / plasma triglyceride clearance module; LPL review still DRAFT.",
    "CTNS": "Lysosomal cystine export is a single step.",
    "SLC26A1": "Epithelial oxalate/sulfate transport has no coherent multi-part module yet; SLC26A1's oxalate role is contested.",
    "SLC26A6": "As SLC26A1; a two-part oxalate-transport module is possible later.",
    "DMP1": "No module contains DMP1 as a part. It is named in the notes of fgf23_klotho_phosphate_homeostasis as regulatory context, which this audit deliberately does not count as membership, and its mechanism is undefined.",
    "SLC10A7": "Single gene with unknown transported substrate.",
    "DNAJC30": "Complex I N-module repair is not assembly; no repair module exists.",
    "LCT": "Brush-border disaccharide digestion: only LCT has a completed review (SI, MGAM, TREH missing).",
    "HNF1A / HNF4A": "Transcription factors whose hyperinsulinism and MODY roles act through many target genes; no beta-cell transcriptional-network module exists yet.",
    "SLC16A1": "Disease mechanism is ectopic beta-cell expression of a transporter whose normal role (lactate/pyruvate transport) belongs to no beta-cell pathway; a monocarboxylate-transport module would not include the disease mechanism.",
    "SIM1": "Transcription factor needed for paraventricular hypothalamic neuron development and function; it acts on, rather than within, the leptin_melanocortin_signaling module, whose parts are the ligand, processing and receptor steps.",
    "MT-TL1 / MT-TQ / MT-TH / MT-TK / MT-TC / MT-TS1 / MT-TS2 / MT-TV / MT-TW / MT-TM": "No mitochondrial translation module exists; in mitochondrial_trna_charging_and_initiator_formylation a tRNA would appear only as a synthetase substrate, which the substrate guidance excludes, and module parts are UniProt proteins.",
    "UCP2": "Causal role disputed (relationship DISPUTED); its transported substrate is itself contested.",
    "AIFM1": "The aligned function is the mitochondrial disulfide relay (CHCHD4 anchoring); no module covers the relay. AIFM1 is a part of apoptotic_execution_phase, whose AIFM1 annoton carries DNA binding, nucleus and positive regulation of apoptotic process: a different AIFM1 activity, and not the encephalomyopathy mechanism.",
    "APOB": "The aligned term is GO:0034379 very-low-density lipoprotein particle assembly, and there is no VLDL-assembly module. APOB is a part of chylomicron_assembly_secretion, whose scope is GO:0034378 chylomicron assembly, and of ldl_receptor_mediated_endocytosis, which is about the receptor taking the particle up. GO:0034378 and GO:0034379 are siblings, not one inside the other, so the hepatic VLDL step is genuinely unmodelled. APOB's other row, the LDL-receptor-binding one, is covered.",
    "NUBPL": "The aligned term is GO:0016226 iron-sulfur cluster assembly. NUBPL is a part of complex_i_assembly_factors, whose scope is GO:0032981 mitochondrial respiratory chain complex I assembly: NUBPL delivers an Fe-S cluster to the assembling complex, and the cluster's own assembly is a different process that no module covers.",
    "NDUFA1": "A limitation of the coverage test rather than a modelling gap, and left flagged rather than waived. The module is the right one; the cause is an asymmetry in how the two sides may say the same thing. The dismech node binds GO:0008137 NADH dehydrogenase (ubiquinone) activity, which the review carries as contributes_to_molecular_function, so the row aligns. complex_i_accessory_subunits says the identical relation the GO-idiomatic way, giving its NDUFA1 annoton GO:0005198 structural molecule activity as part of complex I, and GO:0005198 does not relate to GO:0008137 by is_a/part_of ancestry: a structural role and the activity it supports are different branches of molecular function. Coverage accepts a contributes-to term from the review but has no way to read the module\'s structural-plus-part_of idiom as the same claim. (The module also declares GO:0006120 as its process scope, which ancestry does not reach from GO:0008137 either - but that is a fact about this particular pair, not about the aspects: is_a/part_of does cross between molecular function and biological process, and MT-ND1 in this same table aligns GO:0008137 to GO:1902600 by doing so. Either way the aspect question is not what decides this row.)",
}
# Read from the run rather than kept here: a hardcoded pair went stale the moment the audit
# added PARTIAL_COVERAGE to module_sourced, leaving alt_comparison reading the triple while
# the reasons enforcement and the "(not covering)" marker read the pair.
MODULE_FLAGS = tuple((PROV.get("_flag_groups") or {}).get("module_sourced") or ())
if not MODULE_FLAGS:
    sys.exit("the report records no module_sourced flag group; it was produced by a "
             "superseded align_audit.py - re-run the audit")
# Which module flags oblige a hand-written reason. PARTIAL_COVERAGE does not, and the page
# now says so rather than leaving it to be inferred from the constant: the other two are
# verdicts about a module ("none contains this gene", "one does and misses its function")
# that only a reader of the module can justify, whereas PARTIAL_COVERAGE reports which
# aligned terms no module term reached, and the row prints them. The distinction is
# obligation, not importance.
REASON_REQUIRING_MODULE_FLAGS = tuple(
    (PROV.get("_flag_groups") or {}).get("module_sourced_reason_required") or ())
if not REASON_REQUIRING_MODULE_FLAGS:
    sys.exit("the report records no module_sourced_reason_required flag group; it was "
             "produced by a superseded align_audit.py - re-run the audit")
# Flags that qualify a row rather than mark it defective. PARTIAL_ALIGNMENT,
# ALIGNED_CONTRIBUTES_ONLY and ALIGNED_ON_SHARED_NODE_ONLY are counted and reported
# individually below rather than folded into one "clean" figure, because each is a way
# the test can be weaker than the row looks.
QUALIFYING = ("PARTIAL_ALIGNMENT", "ALIGNED_CONTRIBUTES_ONLY",
              "ALIGNED_ON_SHARED_NODE_ONLY", "PARTIAL_COVERAGE")
# Read from the run, not built here from MODULE_FLAGS: deriving it made "soft" the
# default for any module flag the audit added later, so a flag marking a real
# contradiction would have been absorbed into the clean count with nothing failing.
SOFT = tuple((PROV.get("_flag_groups") or {}).get("soft") or ())
if not SOFT:
    sys.exit("the report records no soft flag group; it was produced by a superseded "
             "align_audit.py - re-run the audit")
# The page names these three in prose, so a run whose soft set stopped containing them
# would print a sentence its own figures contradict.
_missing_soft = [f for f in ("ALIGNED_NONCORE", "ALIGNED_PROPOSED") + QUALIFYING
                 if f not in SOFT]
if _missing_soft:
    sys.exit(f"the report's soft flag group omits {', '.join(_missing_soft)}, which this "
             "page describes as tolerated by the clean count - re-run the audit or amend "
             "the prose")

# Flag glossary, keyed on the flag name. Checked against the flags the run actually
# emitted rather than hand-maintained beside them: PARTIAL_COVERAGE was published on 14
# rows and defined nowhere, because the previous legend was prose carrying its own
# arithmetic ("the last seven are informational") that counted an older vocabulary.
FLAG_GLOSS = {
    "UNTYPED": "the dismech genetic record carries no relationship type",
    "NO_ORIGIN": "the dismech genetic record carries no variant origin",
    "GENE_ON_NO_NODE": "no pathophysiology node names the gene",
    "NO_GO_ON_GENE_NODES": "no node naming the gene carries a GO term",
    "NO_AIGR_REVIEW": "no ai-gene-review review exists for the gene",
    "AIGR_NOT_COMPLETE": "a review exists but its status is not COMPLETE",
    "NO_CORE_FUNCTION_TERMS": "a review exists but has no core-function GO term to compare against",
    "NO_GO_ALIGNMENT": "no node term matches a core function, an annotation the review keeps, or a term it proposes",
    "ALIGNED_NONCORE": "node terms match only annotations the review keeps as non-core",
    "ALIGNED_PROPOSED": "node terms match only terms the review proposes as NEW, which are not yet annotations",
    "PARTIAL_ALIGNMENT": "some node terms aligned and others matched nothing in the review",
    "ALIGNED_CONTRIBUTES_ONLY": "every aligned term matched only a contributes-to function, not an enabled one",
    "ALIGNED_ON_SHARED_NODE_ONLY": "every aligned term came from a node the gene shares with another gene",
    "NO_MODULE_MEMBERSHIP": "no module contains the gene's accession",
    "MODULE_NOT_COVERING": "a module contains it, but no annoton term there relates to the aligned terms",
    "PARTIAL_COVERAGE": "a module covers some aligned terms and no module term reaches the rest",
}


def flag_legend():
    """The whole glossary as bullets, grouped, enforcing that every emitted flag is defined.

    Prints every entry rather than only the emitted ones. Filtering to what the primary
    report emits was a regression: it dropped the definitions of four flags the page's own
    prose names, NO_GO_ALIGNMENT among them - the headline negative result - so the fix for
    one undefined flag left four more undefined. A flag the run does not emit is still a
    flag a reader meets in the text, and the glossary is small enough to print whole.

    Enforcement runs the other way and over both reports, since a flag emitted by either
    would be published without a definition.
    """
    emitted = {f for src in (rep, ALT_REP) for e in src for g in e.get("genes") or []
               for f in g.get("flags") or []}
    missing = sorted(emitted - set(FLAG_GLOSS))
    if missing:
        sys.exit(f"flags emitted by a run with no entry in FLAG_GLOSS: {', '.join(missing)}; "
                 "they would be published in the table and the summary with no definition")
    # Ordered by the groups the comparison section argues from, not alphabetically, so the
    # legend carries the same structure as the explanation.
    groups = PROV.get("_flag_groups") or {}
    order, seen = [], set()
    for key in ("review_independent", "review_absent", "review_present_thin", "module_sourced"):
        for f in groups.get(key) or []:
            if f in FLAG_GLOSS and f not in seen:
                order.append(f); seen.add(f)
    order += [f for f in sorted(FLAG_GLOSS) if f not in seen]
    out = []
    for f in order:
        mark = " *(qualifying)*" if f in QUALIFYING else ""
        # "either" is only true when there are two runs. With one report ALT_REP is empty,
        # so the claim would cover a run this page has not read - and the branch-local
        # report does emit NO_CORE_FUNCTION_TERMS, which such a page would deny.
        _scope = "either run" if ALT_PATH else "this run"
        note = "" if f in emitted else f" - not emitted by {_scope}"
        out.append(f"- `{f}`{mark} - {FLAG_GLOSS[f]}{note}")
    return out


lines = [
    "---",
    "title: dismech metabolic disorders aligned with ai-gene-review",
    "maturity: IN_PROGRESS",
    "description: Per-entry check that dismech metabolic disease mechanisms agree with ai-gene-review core functions and modules",
    "species: [human]",
]

from collections import Counter

# Suggestion from review: ALIGNED_ON_SHARED_NODE_ONLY fires on a large minority of rows, so
# the page says how many of them align on a term the review asserts in its own right. An
# identical node/core term means the shared node is not what earned the match.
def _shared_node_split(entries):
    """Rows flagged shared-node-only, split by how much of the row is self-identical.

    Two figures, because they license different claims. `some` counts a row with at
    least one node term identical to a core term; `all` counts a row where every
    aligned term is. The inference "the shared node is not doing the work" holds for
    the identical terms only, so a row in `some` but not `all` still has partner-derived
    matches carrying part of its verdict.
    """
    tot = some = every = 0
    for e in entries:
        for g in e.get("genes") or []:
            if g.get("relationship") not in (None, "CAUSATIVE"):
                continue
            if "ALIGNED_ON_SHARED_NODE_ONLY" not in (g.get("flags") or []):
                continue
            tot += 1
            pairs_ = (g.get("aligned_pairs") or {}).items()
            hits = [t in (v if isinstance(v, list) else [v]) for t, v in pairs_]
            if any(hits):
                some += 1
            if hits and all(hits):
                every += 1
    return tot, some, every


n_shared, n_shared_exact, n_shared_all = _shared_node_split(rep)
def cross_aspect_rows(entries, aspects):
    """Matched pairs whose two terms sit in different GO aspects.

    Derived rather than named. The page used to cite three examples in prose; when the
    input tree changed, one of them (SLC16A1) stopped being cross-aspect and the sentence
    became false while reading exactly as before. A pair counts only where both aspects
    are known and differ, and a row is only listed where it has no same-aspect pair of
    its own, since otherwise the crossing is not what earned the row.
    """
    sole, any_ = [], 0
    for e in entries:
        for g in e.get("genes") or []:
            crossings, same = [], False
            for t, v in (g.get("aligned_pairs") or {}).items():
                for c in (v if isinstance(v, list) else [v]):
                    a, b = aspects.get(t), aspects.get(c)
                    if a and b and a != b:
                        crossings.append((t, c, a, b))
                    elif a and b:
                        same = True
            if crossings:
                any_ += 1
                if not same:
                    sole.append((g["gene"], crossings[0]))
    return sole, any_


TERM_ASPECTS = PROV.get("_term_aspects")
if TERM_ASPECTS == {}:
    # An empty map is what a run with no matched pairs legitimately produces, which is a
    # different thing from a report that predates the field.
    print("note: the report records term_aspects as empty, so this run matched no pairs")
if TERM_ASPECTS is None:
    # Without aspects the cross-aspect figures are zero, and zero renders as "no matched
    # pair crosses the aspects" - a lookup failure or an old report printing as a finding.
    sys.exit("the report has no term_aspects key at all; it was produced by a superseded "
             "align_audit.py and the cross-aspect figures would read as an absence rather "
             "than as missing data - re-run the audit")
_n_all_rows = sum(1 for e in rep for g in e.get('genes') or [])
_ca_sole, _ca_any = cross_aspect_rows(rep, TERM_ASPECTS)
if _ca_sole:
    _g, (_t, _c, _a, _b) = _ca_sole[0]
    _cross_aspect_sentence = (
        f"{_ca_any} rows of all {_n_all_rows} - not only the principal ones - carry at least one such"
        f" pair, and on {len(_ca_sole)} of them the row has no"
        f" same-aspect pair at all, so the crossing is what earns the verdict - {_g} matches"
        f" `{_t}` ({_a}) to `{_c}` ({_b}).")
elif _ca_any:
    _cross_aspect_sentence = (
        f"{_ca_any} rows of all {_n_all_rows} carry at least one such pair, though every one also has a"
        " same-aspect pair, so on this run the crossing never decides a row by itself.")
else:
    _cross_aspect_sentence = (
        "On this run no matched pair crosses the aspects, so nothing here depends on it.")

# The audit records terms it could place under no single aspect root. They are a gap in the
# figures above - a pair involving one is neither crossing nor same-aspect - so the page
# states them rather than leaving the count to read as complete. Written unconditionally by
# the audit, so an absent key is a superseded report and an empty list is a clean run.
_unres = PROV.get("aspect_unresolved")
if _unres is None:
    sys.exit("the report has no aspect_unresolved key; it was produced by a superseded "
             "align_audit.py and the cross-aspect figures would read as covering every term")
if _unres:
    _cross_aspect_sentence += (
        f" {len(_unres)} term(s) sit under no single aspect root and are outside both figures"
        f" ({', '.join('`%s`' % t for t in _unres[:5])}"
        + (", ..." if len(_unres) > 5 else "") + ").")

# Whitelist, so a renamed or new dismech relationship value does not silently become
# principal and inflate the clean count.
PRINCIPAL_RELATIONSHIPS = (None, "CAUSATIVE")
principal = lambda g: g.get("relationship") in PRINCIPAL_RELATIONSHIPS
# Scale of the third membership/coverage state, derived rather than written, for the bullet below.
_n_partial_cov = sum(1 for e in rep for g in e.get("genes", [])
                     if principal(g) and "PARTIAL_COVERAGE" in g["flags"])

# Only genes the audit actually matched to a review. Listing every symbol in the report
# would count modifier and susceptibility genes with no review (SAR1A, APOA5, SH2B1,
# NCOA1, TYK2) toward this project's gene coverage in the all-projects table, and
# `resolve_frontmatter_gene_links` leaves an unresolvable symbol silently unlinked.
reviewed_genes = sorted({g["gene"] for e in rep for g in e.get("genes", [])
                         if g.get("aigr_status")})
lines += [
    "genes: [" + ", ".join(reviewed_genes) + "]",
    "---",
    "",
    "# dismech metabolic disorders aligned with ai-gene-review",
    "",
    "This page records, for every dismech metabolic disorder in scope, whether the causal gene's",
    "dysfunction as modelled in the dismech pathograph agrees with the gene's normal function in its",
    "ai-gene-review review, and whether the gene sits in an ai-gene-review module.",
    "",
    "**Scope.** dismech entries with Harrison's chapter `ENDOCRINOLOGY_METABOLISM` or a metabolic",
    "`category`, excluding primarily endocrine-gland, autoimmune, complex, neoplastic and gynecologic",
    "conditions, plus two entries created in this work (Mitchell syndrome, SLC26A1-related hypersulfaturia).",
    "",
    "**Method.** For each gene bound in an entry's `genetic` records, the GO molecular functions and",
    "biological processes on the pathograph nodes naming that gene are compared with the gene's",
    "ai-gene-review core functions. The audit script (`align_audit.py`), the page generator",
    "(`make_page.py`), the entry list (`scope.yaml`) and the committed report of the run behind this",
    "table (`report.yaml`) are in the `projects/DISMECH_METABOLIC_ALIGNMENT/` directory of the",
    "repository.",
    "",
    "**What \"aligned\" does and does not claim.** Four properties of the test make it a weak",
    "check, and any of them can turn a row green that a curator would not:",
    "",
    "- The relation is **symmetric** and **unbounded in distance**. A node term counts as aligned",
    "  when either it or the core term is an is_a/part_of ancestor of the other, at any depth. So a",
    "  dismech node bound to something broad aligns with a specific core function, and the reverse,",
    "  and two terms many levels apart still align. The table therefore prints the core term each",
    "  node term matched (`node->core`, or the term alone where the two are identical), so the",
    "  distance behind a match is visible per row. `DMP1 | GO:0005509` (calcium ion binding) is the",
    "  clearest row where the verdict carries little information; reading a row as agreement means",
    "  reading its pair.",
    "- A dismech node binds its GO terms **at node level**, and a node may name several genes.",
    "  dismech has no per-gene attribution inside a node, so every term on a shared node is read",
    "  for every gene on it, and a row can align on a co-named partner's activity. The column",
    "  marks such a term `s`, and `ALIGNED_ON_SHARED_NODE_ONLY` fires where *every* term a row",
    "  aligned on came from a shared node. The hyperinsulinism node naming both GLUD1 and HADH,",
    "  which carries glutamate dehydrogenase activity and enzyme inhibitor activity together, is",
    "  the case to read: each gene is credited with both, and here that happens to be right in",
    "  both directions (HADH does inhibit GLUD1), which is exactly why it needs marking rather",
    "  than trusting. The flag is conservative by construction and fires on a large minority of",
    f"  rows, so read it with this alongside: of the {n_shared} principal rows it fires on,",
    f"  {n_shared_all} align **only** on node terms identical to one of the gene's own core",
    "  functions, so the review asserts each of those activities in its own right and the shared",
    f"  node earned none of the match. A further {n_shared_exact - n_shared_all} have at least one",
    "  such identical term but not all of them, so part of the verdict still rests on a",
    f"  partner-derived term, and {n_shared - n_shared_exact} have none at all. GLUD1 and its",
    "  `GO:0004353` are of the first shape. Only the identical terms license reading the flag as",
    "  harmless, which is why the three figures are given separately rather than summed.",
    "- `contributes_to_molecular_function` is compared **alongside** core molecular function. A",
    "  subunit that contributes to a complex-level activity without enabling it is doing what the",
    "  dismech node describes, so excluding it would lose real agreement; but it is a weaker claim,",
    "  so a term matched only that way is marked `c` and `ALIGNED_CONTRIBUTES_ONLY` fires where a",
    "  row's whole alignment rests on one.",
    "- Module **membership** is not module **coverage**. Membership says the gene is a part of some",
    "  module; coverage says a module is about the function the row aligned on, which is a different",
    "  and stronger claim. They are flagged separately in three states: `NO_MODULE_MEMBERSHIP` means",
    "  no module contains the gene; `MODULE_NOT_COVERING` means one does but no term anywhere in any",
    "  of those modules is related to the aligned terms, and such a module is marked",
    f"  `(not covering)` in the Modules column; and `PARTIAL_COVERAGE` ({_n_partial_cov} principal",
    "  rows) means a module covers some of the aligned terms while no module term reaches the rest,",
    "  which the Modules column names term by term after `- uncovered:`. The third state is not a",
    "  defect to fix: a module is scoped to a process, so it will often reach the aligned term that",
    "  names that process and not a second term naming a different activity of the same gene.",
    "  AIFM1 is the row `MODULE_NOT_COVERING` exists to catch: it sits",
    "  in `apoptotic_execution_phase`, whose AIFM1 annoton carries DNA binding, nucleus and",
    "  positive regulation of apoptotic process, while the aligned function is the mitochondrial",
    "  disulfide relay. No module covers the relay.",
    "",
    "Coverage reads the module's declared `concepts`, at module level and per node, as well as its",
    "annotons' terms: a module states its scope as processes while its annotons carry the molecular",
    "functions of individual parts, so annotons alone miss what the module is about. One limitation",
    "survives that and is left visible rather than waived: coverage is asymmetric about complex",
    "membership. It accepts a `contributes_to_molecular_function` term from the review, but cannot",
    "read a module's GO-idiomatic way of saying the same thing - a subunit given `GO:0005198`",
    "structural molecule activity as part of the complex - as the same claim, because a structural",
    "role and the activity it supports are unrelated branches of molecular function. NDUFA1 is the",
    "row where that decides the verdict.",
    "",
    "An earlier version of this page also claimed that is_a/part_of ancestry cannot cross between",
    "molecular function and biological process. That is false, and rows of this table disprove it:",
    "GO asserts `part_of` from transporter activities to the transport processes they carry out.",
    _cross_aspect_sentence,
    "What is true is narrower, and is a fact about one pair rather than about the aspects:",
    "`GO:0008137` does not reach `GO:0006120`. Two things follow. Cross-aspect `part_of` is a",
    "real source of",
    "alignment in this table, not an artefact - and since node MF and BP terms are compared against",
    "one pooled set of the review's core molecular functions and `directly_involved_in` processes,",
    "a node activity term can be satisfied by a core process and the reverse. Such a match is",
    "genuine agreement but weaker than a same-aspect one, and `aligned_pairs` records which core",
    "term each node term matched so a reader can see which shape any given row is.",
    "",
    "Membership is read from the module structure (`parts[].node.annotons[]`, following the",
    "participant whichever selector it uses - `gene_product`, `gene`, `ortholog_of`, `homolog_of`,",
    "a `FAMILY` participant's `representative_members`, and a protein complex's `active_units`) and",
    "following nested parts and variant sets, so a gene named only in a module's notes or evidence",
    "does not count as a part. The run records both counts in its provenance below, so the gap",
    "between reading the structure and reading the file text is a measured figure rather than a",
    "quoted one.",
    "",
    "Flags, with the qualifying ones marked - a qualifying flag says the verdict is weaker than",
    "`ok` would suggest, so those are counted separately below rather than absorbed into one",
    "clean figure:",
    "",
] + flag_legend() + [
    "",
]
if PROV:
    lines += [
        "**Provenance of this run.** The table is generated, so it is only as current as the inputs it",
        "was generated from, and those inputs live in two repositories.",
        "",
        f"- run date: `{PROV.get('run_date') or 'unrecorded'}`",
        f"- dismech revision: `{PROV.get('dismech_revision') or 'unrecorded'}`"
        + (f" ({PROV['dismech_describe']})" if PROV.get("dismech_describe") else ""),
        f"- ai-gene-review revision: `{PROV.get('aigr_revision') or 'unrecorded'}`"
        + (f" (branch `{PROV['aigr_branch']}`)" if PROV.get("aigr_branch") else ""),
        f"- GO release: `{PROV.get('go_version') or 'unrecorded'}`, adapter `{PROV.get('go_adapter') or 'unrecorded'}`",
    ]
    _ad = PROV.get("audit_revision") or "unrecorded"
    _ah = PROV.get("audit_sha256") or "unrecorded"
    _DIRT_NAMES = {"audit_dirty": "the audit script itself",
                   "aigr_dirty": "the ai-gene-review tree",
                   "dismech_dirty": "the dismech tree"}
    # Three states, not two. None means git could not answer, and treating it as False -
    # which `if PROV.get(k)` did - published an unanswerable tree as a clean one, which is
    # the assertion the audit-side fix was made to stop. Rendered separately.
    _dirt = [v for k, v in _DIRT_NAMES.items() if PROV.get(k) is True]
    _unknown = [v for k, v in _DIRT_NAMES.items() if PROV.get(k) is None]
    lines.append(
        f"- audit script: `{_ah}` (sha256 of `align_audit.py`), last committed at `{_ad}`"
        + ("; unrecorded because the project directory has no history in the tree that was"
           " read, which is the case for a scratch tree the script was copied into, so the"
           " sha256 is the identifier to use" if _ad == "unrecorded" else "")
        + (f"; **uncommitted changes at run time in: {', '.join(_dirt)}**, so the revisions"
           " above name commits that are not exactly what ran" if _dirt else "")
        + (f"; **git could not be asked about: {', '.join(_unknown)}**, so whether the revisions"
           " above name what ran is not established either way" if _unknown else "")
    )
    if PROV.get("aigr_tree"):
        lines.append(f"- ai-gene-review tree: {PROV['aigr_tree']}")
    _ma = PROV.get("module_accessions") or {}
    if _ma:
        lines.append(
            f"- modules read: `{_ma.get('modules_read')}`; UniProt accessions reached as parts:"
            f" `{_ma.get('accessions_as_parts')}`, against `{_ma.get('accessions_in_file_text')}`"
            " matching the accession pattern anywhere in the module file text. Both are sums over"
            " modules of that module's distinct accessions, so a protein in several modules counts"
            " once per module; the difference is accessions mentioned in notes or evidence of a"
            " module they are not a part of, which this audit does not count as membership."
        )
    lines += [
        "",
        "Many of the gene reviews and modules this table asserts `COMPLETE` for are added by the ten",
        "themed PRs split out of #4690, so reproducing these rows needs a tree holding all of them.",
    ]
    if PROV.get("aigr_tree"):
        lines.append(f"The run above read {PROV['aigr_tree']}.")
    else:
        # No guessing from aigr_dir. The previous version inferred "this was a scratch
        # directory" from the path not starting with /home, which asserted two things the
        # provenance does not record and was false for any ordinary checkout.
        lines.append(
            "That run's provenance records no `aigr_tree`, so it does not say how its tree was"
            " built - only the revision and directory above. Set `AIGR_TREE` when running the"
            " audit over a tree that is not a plain checkout."
        )
    lines.append("")
    lines += alt_comparison()


def aligned_cell(g):
    """Node term with the core term it matched, so an unbounded match is visible.

    Every match is shown where a node term relates to more than one core term: picking
    one would show the alphabetically smallest GO id, which need not be the nearest.
    A term matched only through `contributes_to_molecular_function` is marked, and so is
    one held only because another gene shares the node it came from.
    """
    pairs = g.get("aligned_pairs") or {}
    terms = g.get("aligned_terms") or []
    if not terms:
        return "-"
    contrib = set(g.get("aligned_via_contributes_to") or [])
    shared = set(g.get("shared_node_terms") or [])
    cells = []
    for t in terms:
        c = pairs.get(t)
        cs = c if isinstance(c, list) else [c]
        cs = [x for x in cs if x is not None]
        if not cs or cs == [t]:
            cell = t
        else:
            cell = f"{t}&rarr;" + "/".join(cs)
        marks = ("c" if t in contrib else "") + ("s" if t in shared else "")
        cells.append(cell + (f" <sup>{marks}</sup>" if marks else ""))
    return " ".join(cells)


def unaligned_cell(g):
    """Node terms that matched no core function: the half that shows disagreement."""
    terms = g.get("dismech_only") or []
    if not terms:
        return "-"
    shared = set(g.get("shared_node_terms") or [])
    return " ".join(t + " <sup>s</sup>" if t in shared else t for t in terms)


def modules_cell(g):
    """Modules the gene is a part of, linked, marking a non-covering one only when flagged.

    `(not covering)` used to print on any module outside `covering_modules`, including on
    rows carrying no flag, where it only means the gene's other module is about its other
    function. Marking it only where `MODULE_NOT_COVERING` fires keeps it to the rows the
    page has a stated reason for.
    """
    mods = g.get("modules") or []
    if not mods:
        return "-"
    pairs_ = g.get("covering_pairs") or {}

    def link(m):
        # Which module term earned the coverage, as the Aligned column shows which core
        # term earned the alignment. Coverage is tested against every term anywhere in a
        # module, so without the pair a reader cannot tell a relevant match from a remote
        # ancestor of one.
        cell = f"[{m}](../modules/{m}.html)"
        hits = pairs_.get(m) or []
        if hits:
            # Formatted here rather than in the report, so the uncovered set is derived
            # from the pairs themselves instead of by re-parsing a display string.
            shown = [f"{t}->{mt}" for t, mt in hits[:2]]
            cell += " (" + ", ".join(shown) + (", ..." if len(hits) > 2 else "") + ")"
        return cell

    cov = g.get("covering_modules") or []
    flags_ = g.get("flags") or []
    out = " ".join(link(m) if m in cov or "MODULE_NOT_COVERING" not in flags_
                   else f"[{m}](../modules/{m}.html) (not covering)" for m in mods)
    if "PARTIAL_COVERAGE" in flags_:
        # Coverage is existential, so a covered row can still leave aligned terms that no
        # module term reached. Named here rather than left to the flag alone.
        unc = g.get("uncovered_aligned_terms") or []
        out += " - uncovered: " + " ".join(unc[:3]) + (" ..." if len(unc) > 3 else "")
    return out


c = Counter(f for e in rep for g in e.get("genes", []) if principal(g) for f in g["flags"])
n_rows = sum(1 for e in rep for g in e.get("genes", []) if principal(g))
n_clean = sum(1 for e in rep for g in e.get("genes", [])
              if principal(g) and not [f for f in g["flags"] if f not in SOFT])
n_partial = sum(1 for e in rep for g in e.get("genes", [])
                if principal(g) and "PARTIAL_ALIGNMENT" in g["flags"])
n_full = sum(1 for e in rep for g in e.get("genes", [])
             if principal(g) and g.get("aligned_terms") and not g.get("dismech_only"))
n_untyped = sum(1 for e in rep for g in e.get("genes", [])
                if principal(g) and g.get("relationship") is None)
# The whitelist admits untyped rows defensively, but saying "causative and untyped" when a
# run holds none of the latter describes the predicate rather than the table.
_principal_desc = (f"causative and untyped; {n_untyped} untyped" if n_untyped
                   else "all causative in this run; the predicate also admits untyped")
lines += [
    f"**Summary.** {len(rep)} entries; {n_rows} principal gene rows ({_principal_desc});",
    f"{n_clean} carry no flag other than a module flag or one of the qualifying flags - none"
    " carries `NO_GO_ALIGNMENT`, `NO_CORE_FUNCTION_TERMS`, `NO_GO_ON_GENE_NODES` or"
    " `GENE_ON_NO_NODE`. That count also tolerates `ALIGNED_NONCORE` and `ALIGNED_PROPOSED`,"
    " which say a row aligned only against a retained non-core or a proposed term rather than"
    " a core function; no principal row in this run carries either."
    + (" Flag counts on principal rows: " + ", ".join(f"`{k}` {v}" for k, v in sorted(c.items()))
       # Only worth saying when the provenance section printed all-row counts to compare with.
       + (". These are principal rows only, so they are smaller than the all-row counts in the"
          " provenance section above wherever a flag also falls on a modifier, susceptibility"
          " or disputed row." if ALT_REP else ".")
       if c else " No principal row carries a flag."),
    "",
    f"**Agreement is partial on many rows, and the table shows both halves.** {n_full} principal",
    f"rows align every GO term their dismech nodes carry; {n_partial} align some and leave others",
    "matching nothing in the gene review. A partial row is usually not a defect in either",
    "repository - it is dismech modelling a step of the disease mechanism that is not part of the",
    "gene's normal function, which is what the two resources are each for. `LCT` is the clearest",
    "case: the row aligns `GO:0000016` lactase activity and leaves `GO:0006366` transcription by",
    "RNA polymerase II unaligned, because the hypolactasia mechanism is the enhancer that switches",
    "the gene off, and transcribing its own gene is not a function of lactase. Reading such a row",
    "as full agreement would be wrong in the other direction, so the unaligned terms are printed",
    "rather than dropped.",
    "",
    "Polygenic entries (Type I diabetes) and modifier/susceptibility genes are",
    "listed but were not required to align: their genes are risk loci or modifiers, not the",
    "normal-function owners of a single pathway step.",
    "",
    "In the GO-term columns, <sup>c</sup> marks a term matched only through the review's",
    "`contributes_to_molecular_function`, and <sup>s</sup> a term the gene holds only because",
    "another gene is named on the same dismech node. Where a node term relates to several core",
    "terms, all of them are shown separated by `/`.",
    "",
    "| Entry | Gene | Relationship | AIGR | Aligned GO terms (node&rarr;core) | Unaligned node terms | Modules | Flags |",
    "|---|---|---|---|---|---|---|---|",
]
for e in rep:
    if not e.get("genes"):
        lines.append(f"| {e['entry']} | - | - | - | - | - | - | {e.get('problem','')}: {NOTES.get((e['entry'], None), '')} |")
        continue
    for g in e["genes"]:
        flags = ", ".join(g["flags"]) or "ok"
        lines.append(
            f"| {e['entry']} | {g['gene']} | {g.get('relationship') or '-'} | {g.get('aigr_status') or '-'} | "
            f"{aligned_cell(g)} | {unaligned_cell(g)} | {modules_cell(g)} | {flags} |"
        )
lines += [
    "",
    "## Notes on remaining flags",
    "",
    "- **No causative row carries `NO_GO_ALIGNMENT`**, which is the flag that would mark a real",
    "  contradiction: every causative gene has at least one node term matching a core function.",
    "  The flags causative rows do carry say something weaker. The three module flags",
    "  (`NO_MODULE_MEMBERSHIP`, `MODULE_NOT_COVERING`, `PARTIAL_COVERAGE`) are about what is",
    "  modelled elsewhere in ai-gene-review, not about this gene's function.",
    "  `PARTIAL_ALIGNMENT` marks non-overlap rather than conflict - dismech modelling a step the",
    "  gene's normal function does not include - and `ALIGNED_CONTRIBUTES_ONLY` and",
    "  `ALIGNED_ON_SHARED_NODE_ONLY` mark a match that rests on a weaker relation than the row",
    "  looks. `ALIGNED_NONCORE` falls only on UCP2, a DISPUTED gene that was never required to",
    "  align, as do the `NO_AIGR_REVIEW` and `AIGR_NOT_COMPLETE` rows.",
    "- **MELAS mtDNA genes**: MT-ND1, MT-ND5 and MT-ND6 have reviews and are parts of",
    "  mitochondrial_complex_i_core, aligning with the dismech complex I node (NADH:ubiquinone",
    "  oxidoreductase activity, DECREASED). The ten mt-tRNA genes (MT-TL1, MT-TQ, MT-TH, MT-TK,",
    "  MT-TC, MT-TS1, MT-TS2, MT-TV, MT-TW, MT-TM) have ncRNA reviews (RNAcentral ids) whose core",
    "  function, triplet codon-amino acid adaptor activity in mitochondrial translation, matches",
    "  the dismech translation-defect nodes.",
    "- **UCP2** (DISPUTED): dismech binds regulation of insulin secretion (GO:0050796), which",
    "  is the parent of a UCP2 annotation the review keeps as non-core (GO:0061179), so the row",
    "  is `ALIGNED_NONCORE`. dismech deliberately binds no UCP2",
    "  activity, because its causal role in hyperinsulinism and its transported substrate",
    "  are both disputed.",
    "- **TMEM251** is the dismech/HGNC-build label for the gene now named LYSET; it is matched to",
    "  the LYSET review.",
    "- **Type I diabetes risk loci** (PTPN22, IL2RA, CTLA4, IFIH1, BACH2, TNFAIP3, EGR2, IRF4, IKZF1,",
    "  TYK2) are SUSCEPTIBILITY records with no single pathway step; several ai-gene-review entries",
    "  for them are still drafts from other projects.",
]
# Which module flag each named gene actually carries, and whether its row is principal,
# so the list cannot read as "these causative genes are all in a module that misses their
# function" when most of them are in no module at all and one is not causative.
flag_by_gene, principal_genes = {}, set()
for e in rep:
    for g in e.get("genes", []):
        for f in g["flags"]:
            if f in REASON_REQUIRING_MODULE_FLAGS:
                flag_by_gene.setdefault(g["gene"], set()).add(f)
        if principal(g):
            principal_genes.add(g["gene"])

lines += ["", "## Genes with a module flag, and why", "",
          "`NO_MODULE_MEMBERSHIP` means no module contains the gene; `MODULE_NOT_COVERING` means",
          "one does but nothing in it is about the function the row aligned on. Rows that are not",
          "causative are marked, since they were never required to align. `PARTIAL_COVERAGE` is",
          "the third module flag and is deliberately absent from this list: it reports which of a",
          "row's aligned terms a module reached and which it did not, so the covering pairs and the",
          "`- uncovered:` list in the Modules column already say everything a hand-written reason",
          "could, and the generator",
          "does not require one. The distinction is obligation, not importance.", ""]
for k, v in MODULE_REASONS.items():
    names = [n.strip() for n in k.split("/")]
    fl = sorted({f for n in names for f in flag_by_gene.get(n, ())})
    tag = ", ".join(f"`{f}`" for f in fl) or "`no module flag on this run`"
    if names and not any(n in principal_genes for n in names):
        tag += ", not causative"
    lines.append(f"- **{k}** ({tag}): {v}")

# Enforce the claim above in both directions: every principal row carrying a module flag
# must have a reason, and every reason must still name a gene that carries one. The
# unused side used to compare against every gene in the report, so a reason that had
# stopped applying lingered silently.
covered = {g.strip() for key in MODULE_REASONS for g in key.split("/")}
missing = sorted({g["gene"] for e in rep for g in e.get("genes", [])
                  if principal(g)
                  and [f for f in g["flags"] if f in REASON_REQUIRING_MODULE_FLAGS]} - covered)
if missing:
    sys.exit("MODULE_REASONS has no entry for principal rows flagged "
             f"{'/'.join(REASON_REQUIRING_MODULE_FLAGS)}: {', '.join(missing)}")
unused = sorted(covered - set(flag_by_gene))
if unused:
    sys.exit("MODULE_REASONS names genes that carry no module flag on this run, so the "
             f"stated reason no longer applies: {', '.join(unused)}")

open(out, "w").write("\n".join(lines) + "\n")
print("wrote", out, n_rows, n_clean)
