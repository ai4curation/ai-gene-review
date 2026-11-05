# Cupriavidus necator GabD (Q9RBF6)

## 2026-10-26 source-based review

The exact published clone is Q9RBF6, linked by UniProt and the primary sequence deposit AF175740/AAF19796.1 to PMID:10564790 and strain SHF3. This is not silently replaced by an H16 genome paralog. The closest named H16 GabD1 sequence Q0K2K1 has 472/483 position-wise identities, not identity; other H16 GabD sequences are more divergent. The deposited clone remains the reviewed entity.

The accessible primary abstract reports a transposon-associated 4HB-leaky phenotype, cloning and heterologous expression, and the relationship of gabD to GABA-degradation genes. The exact protein also has SSADH-specific NCBIfam TIGR01780 and CDD ALDH_F5_SSADH_GabD classifications. Together these support cofactor-general succinate-semialdehyde oxidation (GO0009013). The two originally broad oxidoreductase rows are refined to that existing term. GABA catabolism is retained as a conserved catalytic pathway inference: the enzyme oxidizes a downstream intermediate, rather than merely being required or consumed. No separate target-specific GABA growth assay is asserted.

The primary abstract describes resemblance to NADP-dependent enzymes and separately reports a second NAD-dependent SSADH in the organism. This is not evidence that the cloned GabD is that second enzyme. The NAD-only TreeGrafter row remains source-limited UNDECIDED pending cloned-enzyme acceptor details; absence of NAD activity is not asserted. The broader GO0009013 term does not require an assertion of equally efficient use of both acceptors.

The cytosol TreeGrafter row is also explicitly source-limited: the available abstract and record establish a bacterial metabolic SSADH but not a target-specific localization measurement. Soluble-family membership is not reported as a native localization assay, and the word mitochondrial in the official PTHR43353 label is not imported into bacterial biology. No evolutionary loss, secretion or organelle claim is inferred.

Normal PMID retrieval, the repository full-text provider chain, and ordinary publisher attempts did not recover the full 1999 paper. The strain's precise genealogy and cofactor details require source follow-up; these are not falsely declared unknown to science. Actual Falcon/fallback research failed authentication. FEBA retrieval was attempted but no mapped/reachable CUPNE source was available. No research report was fabricated. All six original ordered annotation payloads and both raw-file hashes are preserved, with no NEW annotation. Baseline and actual acquisition logs are in `.cache/module-audit-logs/hydroxybutyrate-*`.

## Curated cofactor evidence recovered during the same review

The normally cached BRENDA EC1.2.1.79 page explicitly links Q9RBF6/reference 288054 (PMID:10564790) to both acceptors: specific activities 132.1 with NADP and 14.9 with NAD, in micromol/min/mg at pH 11.0 and 30°C. The NAD row is therefore ACCEPT, and all three broad activity rows refine to both GO:0036243 and GO:0004777. This supersedes the preliminary source-limited NAD judgment above without claiming access to the primary Methods. No NEW is required. The much lower NAD activity is not absence, and the alkaline assay ratio does not establish native cofactor flux. BRENDA also reports no substrate-specific gabD induction by 4HB or GABA; this does not contradict catalytic pathway participation. An apparent molecular-weight transcription error elsewhere on the database page is not used.


## PR #5591 source and cofactor follow-up — 2026-10-26

Verified live QuickGO ancestry: both NAD-specific GO:0004777 and NADP-specific GO:0036243 descend from GO:0009013 and the two broader oxidoreductase terms used here. Both core activities remain supported by the exact Q9RBF6 BRENDA extraction tied to PMID:10564790; the primary cache remains abstract-only. NAD activity around 11% of NADP activity at high pH is an assay comparison, not native flux or exclusivity. The module now explicitly depicts the NADP branch, matching that gene core, while this review preserves the additional NAD branch. All original annotation payloads, qualifiers, actions and raw UniProt/GOA bytes are preserved. No NEW annotation was added. Independent bounded consultation agreed that NAD capacity does not imply NADP exclusion. Focused validation, source checks, renders and preservation checks are recorded in the PR #5591 follow-up report.

## 2026-11-02 — cytosol compartment, and one core for a dual-acceptor enzyme

### The cytosol row

What GO:0005829 claims here is modest. Live QuickGO gives it as "The part of the
cytoplasm that does not contain organelles but which does contain other
particulate matter, such as protein complexes", which for an organism without
organelles is the soluble interior of the cell. Three independent lines agree on
that compartment: there is no signal peptide and no transmembrane segment
anywhere in the FT block of the record; succinate semialdehyde is generated
intracellularly, by 4HB oxidation and by GABA transamination, and the
gab-cluster enzymes that supply it are cytoplasmic; and the characterized
enterobacterial enzymes of the same reaction, GabD and Sad (see
`genes/ECOLI/sad`), are cytoplasmic.

What is still missing is a location measurement on the SHF3 clone itself. Family
membership is *not* used as a localization assay, and the "mitochondrial"
wording of the PTHR43353 label is still not imported into bacterial biology. So
the row is kept at the resolution the evidence supports but marked non-core, and
the suggested question asking for an independent source stays open;
`core_functions` continues to assert no location. The earlier UNDECIDED verdict
was recording the same gap, and resolving it this way does not close it.

### One core function instead of two

Both acceptors are measured on this exact clone, 132.1 micromol/min/mg with NADP
against 14.9 with NAD at pH 11.0 and 30°C, so NADP is the major branch and NAD,
at about 11%, the minor one. That is one active site running one reaction with
either cofactor, and GO has a term for exactly that: the QuickGO definition of
GO:0009013 is the reaction with NAD(P)+.

This review previously refined the GO:0009013 row away into GO:0036243 and
GO:0004777 and carried two core functions, one per acceptor. That is withdrawn.
Asserting both children says what the parent already says, and it reports one
reaction as two evolved functions. The GO:0009013 row is now ACCEPT and is the
single core; the two broad oxidoreductase rows refine to it; the NAD-specific
child is kept as its own row, marked non-core at its measured weight; and the
NADP preference is recorded in the core description rather than in the choice of
term. The same convention now runs through `genes/ECOLI/sad` (where the
preference is reversed), the Pseudomonas Sad candidates (where it is unresolved),
the PTHR43217 and PTHR43353 family reviews, and every SSA-oxidation annoton of
the `bacterial_4_hydroxybutyrate_oxidation` module. No evidence changed; only
the number of terms used to state it.
