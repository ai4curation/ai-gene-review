# BACSU/rnhC evidence review — 2026-11-06

RnhC is RNase HIII, a magnesium-dependent ribonuclease that cleaves RNA paired to DNA. It resolves longer RNA-DNA hybrids, including R loops, and internally incises RNA primers during Okazaki fragment processing, facilitating subsequent PolA-dependent repair in reconstituted reactions. Metal availability affects its substrate preference; single-ribonucleotide incision is measurable in vitro but inefficient under physiological metal conditions compared with RnhB.

## Identity and source boundaries

Normal fetch preceded curation. Seed documents, all original row payloads and raw hashes are in `.cache/module-audit-logs/chromosomal-replication-20261106/bacillus-maturation-baseline.json`. Official strain 168 identities and unique full-length PY79 sequence matches are documented in [the sequence audit](../fenA/fenA-source-analysis/README.md). The 2023 paper amplified wild-type genes from PY79 and sequenced cloned plasmids. Exact protein sequence identity supports transfer of chemistry; PY79 mutant phenotypes remain PY79 observations.

PMID:30670546 directly reconstructs RnhC/PolA processing and FenA/YpcP nuclease action on model substrates. Its cached text is abstract-only after normal refetch; online full text was inspected for Fig. 2 and construct methods. PMID:37146086 has cached full text, purified full-length proteins, active-site mutants, substrate comparisons and complementation. PMID:17905985 establishes alternative 5-prime nuclease dependence genetically; synthetic lethality does not assign gap filling. PMID:42133467 is comparative synthesis: its proposed PolC gap-filling assignment is explicitly a hypothesis, not a direct measurement. PMID:42286923 is a primary live-cell fusion tracking study, with no direct resolution of which polymerase fills native gaps; the main text does not name the parental strain, so no strain-specific kinetics or stable replisome location is transferred.

## Mechanistic decisions

FenA performs the dominant measured flap/primer-nuclease activity. RnhC can shorten RNA internally, facilitating PolA processing; PolA can extend DNA and remove remaining RNA. These are alternative or overlapping contributions, not a universal AND requirement. The 2019 efficient RnhC/PolA reaction and 2023 FenA-dominant model use different substrates/assays and need not contradict one another. Polymerase activity and native allocation of gap-filling flux are separate claims.

RnhC-specific review distinguishes HIII from the H2 complex and treats single-rNMP incision as a metal-dependent capability of unresolved native RER significance (PMID:29084857). Longer-hybrid/R-loop processing is supported by biochemical activity and genome-wide hybrid measurements (PMID:37494439). PolA 3-prime proofreading is excluded by the Bacillus catalytic-residue evidence, while its double-strand-break-specific BP remains UNDECIDED rather than rejecting a phylogenetic inference from incomplete target evidence.

## Annotation proposal checks and research provenance

The only authored NEW row is RnhC Okazaki processing: RnhC itself cleaves primer RNA, the process belongs to the DNA-metabolic branch, and same-role primer-removal comparators were queried in QuickGO. FenA P54161 has GO0033567; E. coli PolA P00582 lacks that exact term and carries broader replication terms. Rad27 P26793 and human FEN1 P39748 have the distinct primer-removal term GO0043137, which is not a descendant of GO0033567 in current is_a/part_of ancestry. The observed convention supports catalytic participants while showing heterogeneous process granularity, rather than implying a universal missing annotation. Existing PolA replication rows are refined to this process; its flap activity is represented as a replacement of broad catalytic activity, avoiding duplicate NEW rows. No DNA polymerase activity is assigned to FenA or RnhC. No gene-specific source is inferred from a GOA file.

A genuine normal Falcon attempt failed with HTTP 403 authentication; the unaltered log is `falcon-BACSU-rnhC-maturation.log` in the audit directory. No provider report was fabricated. These notes are manual research.
