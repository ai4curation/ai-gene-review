# VC_1624 (Q9KRL3) curation notes

## 2026-11-02 (module curation: bacterial_carboxyspermidine_biosynthesis)

Fetched with `just fetch-gene VIBCH Q9KRL3 --alias VC_1624`. UniProt gives no
gene name, so the ordered locus name is used as the symbol, following other
VIBCH folders (e.g. VC_1087).

Deep research: no gene-level provider deep-research file was generated in this
session. The module-level OpenScientist report
(`modules/bacterial_carboxyspermidine_biosynthesis-deep-research-openscientist.md`)
was used for retrieval; all claims below were checked against the cached
primary paper.

Evidence (full text of PMID:19196710 cached and read):

- Identity of the enzyme: [PMID:19196710 "Both the carboxynorspermidine and sym
  -norspermidine peaks were absent in the ΔVC1624 mutant (result not shown),
  confirming VC1624 as the functional CANSDH"]; complementation restored
  norspermidine.
- Both products depend on it: [PMID:19196710 "Deletion of either VC1624
  (putative CANSDH) or VC1623 (CANSDC) abolished sym -norspermidine and
  spermidine accumulation"].
- Putrescine use in vivo: [PMID:19196710 "when the CANSDH enzyme is in excess,
  it increasingly uses putrescine as a substrate and forms carboxyspermidine,
  which is then converted to spermidine by CANSDC"].
- Phenotype: growth reduced 50-60% and biofilm severely reduced, rescued by
  norspermidine. Biofilm is a downstream effect of the norspermidine signal, so
  no biofilm process annotation is proposed for the enzyme.

Decisions:

- GO:0102143 IEA: ACCEPT (core). The GO definition explicitly includes the
  carboxyspermidine reaction ("Also converts carboxyspermidine to putrescine").
- NEW IMP: GO:0045312 nor-spermidine biosynthetic process and GO:0008295
  spermidine biosynthetic process. The enzyme catalyses the committed
  condensation step, so it does work in both processes.
- No in vitro kinetics exist for VC_1624 itself; recorded as a knowledge gap.


## 2026-11-05 complete gene-level comparative audit

Re-read every existing annotation, core function, raw UniProt record, relevant
provider report and primary literature. Original annotation payloads and raw
UniProt/GOA snapshots were preserved; no new annotation rows were added. Five
authored NEW rows across the four-gene baseline remain inherited proposals, not
new proposals from this audit. Default Falcon research was attempted with
`just deep-research ORGANISM GENE --provider falcon`; it failed with HTTP 403
authentication. No provider report was fabricated or overwritten. Manual findings
are recorded here; the command logs are in the ignored module-audit cache.

QuickGO on 2026-11-05 confirmed active GO:0102143 includes both carboxynorspermidine
and carboxyspermidine dehydrogenase reactions, and GO:0102144 is obsolete as the
same activity. Searches for carboxyspermidine/carboxynorspermidine decarboxylase
and carboxypolyamine returned no specific decarboxylase term. The existing NTR
name was retained; no GO or PTN identifier was invented. PANTHER official names
were checked in panther.obo, and exact protein/subfamily assignments against the
unchanged UniProt records (PTHR43796:SF2 for the dehydrogenases; PTHR43727:SF1 for
the decarboxylases).

The comparative literature requires a substrate-specific reading. The B. fragilis
and C. leptum enzymes have measured putrescine/DAP kinetics, but these are not
measurements of this target [PMID:37437886, "These data suggest that both enzymes
can use putrescine or DAP and thus produce carboxyspermidine or
carboxynorspermidine."]. Agmatine was not tested in those comparisons. The 2025
reconstruction shows that related pairs can make tetramines or use agmatine;
those functions are not transferred here [PMID:40074085, "The ASA-dependent
pathway consisting of CASDH/CASDC homologs has diversified during evolution
to produce norspermidine (29), N1-aminopropylagmatine (37), and as we have shown
here, spermidine and Spm/Tspm."]. Physiological product identity, reconstructed
pathway activity and isolated-enzyme turnover are distinct evidence.

The 2009 deletions/complementations used C6709, not the N16961 reference strain.
These are same-species locus assignments, not claims of an N16961 experiment
[PMID:19196710, "Wild-type V. cholerae strain C6709 cells grown in M9 minimal
medium"]. Purified CANSDC specificity, including lack of meso-diaminopimelate
activity and 20-fold substrate preference, was measured in the V. vulnificus
ortholog; it is not a direct Q9KRL4 assay. No blanket absence of experimental
support is inferred from these strain distinctions.

PMID:37878710 explicitly synthesized VC1624 and used purified V. cholerae
CANSDH with DAP/ASA/NADPH to provide carboxynorspermidine in a coupled CAPADC
assay. Thus biochemical activity is supported; the narrower outstanding gap
is comparative steady-state kinetics and physiological flux partition. This
corrects any implication in the earlier notes that no in vitro characterization
exists [PMID:37878710, "the genes encoding CASDH from A. tumefaciens (Atu4170)
and CANSDH from V. cholerae (VC1624)"]. The two inherited NEW process assertions
remain supported by catalytic participation and C6709 genetics. No additional
biofilm, virulence, CAPA or tetramine assertion is justified.


## PR #6089 requested revisions — 2026-11-06

Removed the misplaced CANSDC/Q9KRL4 specificity caveat from all three reasons. Q9KRL3 is CANSDH: its own evidence combines C6709 native genetics/metabolites with purified VC1624 substrate generation in PMID37878710. Quantitative synthase substrate preference remains unmeasured. Both inherited NEW process proposals and the original MF decision are unchanged. Machine annotation payloads, inherited NEW assertions and raw UniProt/GOA files were preserved; no new annotation rows were added. Existing research/provider records were not refreshed.
