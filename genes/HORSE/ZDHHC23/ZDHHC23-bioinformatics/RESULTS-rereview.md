# ZDHHC23 horse gene models: re-review comparison (2026-10-20)

Script: `compare_models_rereview.py` (stdlib only; fetches UniProt FASTA live). Output: `results-rereview.json`.
Ensembl gene and transcript structure was read from the Ensembl REST API (`lookup/id/ENSECAG00000014382?expand=1`).

## Gene model identity

A0A9L0T4E4 is the translation of ENSECAT00000105517, which Ensembl flags as the canonical transcript of horse gene ENSECAG00000014382 (ZDHHC23, chromosome 19). The same gene has six other unreviewed UniProt models (A0A3Q2KPV4, F7CNX6, A0A5F5Q1C7, A0A9L0RVS6, A0A9L0R7E2, A0A9L0SCZ1). No horse ZDHHC23 entry is Swiss-Prot reviewed. All models with a PANTHER cross-reference are placed in PTHR22883:SF475 (PALMITOYLTRANSFERASE ZDHHC23), the same subfamily as reviewed human Q8IYP9, mouse Q5Y5T3 and rat Q76IC6.

## Shared core

A0A9L0T4E4 has the DHHC motif at 280-283, so its predicted active-site cysteine is C283. That position corresponds to human C289 and rat C283. Every model except A0A9L0RVS6 (397 aa) carries the full region from the N-terminal cytoplasmic segment through the last transmembrane segment, ending at the conserved anchor LCGLIVDT (residue 399 in A0A9L0T4E4). A0A9L0RVS6 has a frameshifted tail and is missing the last transmembrane segments.

## C-terminal tail diverges between models

The models differ after the LCGLIVDT anchor because they use different last exons:

| Protein | Length | Tail after LCGLIVDT | Ends -EDIV |
|---|---|---|---|
| A0A9L0T4E4 (horse, benchmark) | 448 | AGADCSPGASAAGPRLHGEWRQICQSLWLFRGGLVTYDWSSLPDCTFHF | no |
| A0A3Q2KPV4 / A0A9L0R7E2 / A0A9L0SCZ1 (horse) | 435/426/419 | GQYNRGFLRNWHQFSTLGAHPFHHPAEDIV | yes |
| F7CNX6 (horse) | 417 | GASTLVTMAGRGEQTPLC | no |
| A0A5F5Q1C7 (horse) | 410 | GLPGW | no |
| Q76IC6 (rat, reviewed) | 429 | GQYNRGFLRNWLQFSTLGTRTVHTPAEDIV | yes |
| Q5Y5T3 (mouse, reviewed) | 425 | GQYNRGFLRNWLQFSTLGTHTVHTPAEDIV | yes |
| Q8IYP9 (human, reviewed canonical) | 409 | GLLG | no |

In A0A9L0T4E4, exon 5 splices at its donor (chr19:46759456) to a distal 3' exon (chr19:46755009-46755651, CDS end 46755503), which encodes the 49-residue tail shown above. In the -EDIV models (for example ENSECAT00000051286), the reading frame instead continues past that donor (CDS end 46759364). The -EDIV tail is conserved between horse and rodents, and the rat -EDIV tail is the mapped PDZ-binding motif that binds NOS1 (rat Q76IC6 REGION 426..429, PMID:15105416). The A0A9L0T4E4 tail does not resemble any reviewed ortholog tail tested here.

## Interpretation

- A0A9L0T4E4 is a complete-core ZDHHC23 product. It keeps the full DHHC cysteine-rich domain (C283) and the transmembrane architecture, so the subfamily-level S-palmitoyltransferase function can be transferred.
- Its C-terminal tail comes from an alternative last exon and has no -EDIV PDZ-binding motif. The NOS1 PDZ interaction from rat should not be transferred to this model.
- The reviewed human canonical isoform (GLLG tail) also has no -EDIV motif, so the tail is variable even among reviewed orthologs. The KCNMA1 evidence (PMID:22399288) comes from an siRNA screen in HEK293 cells, which depletes the endogenous human enzyme, and from overexpression of ZDHHC23 constructs "described previously". The cached text does not say which tail those constructs carry, so this analysis cannot test whether KCNMA1 S0-S1 palmitoylation depends on the tail. Catalysis by DHHC enzymes resides in the DHHC cysteine-rich domain, which A0A9L0T4E4 retains.
- This analysis does not test whether the A0A9L0T4E4 tail is expressed in horse tissues. No RNA-seq or transcript-support level was examined.
