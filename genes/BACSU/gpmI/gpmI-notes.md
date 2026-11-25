# gpmI (P39773, BSU33910) notes

## Session 2026-11-13

Deep research: `just deep-research BACSU gpmI --provider falcon` was tried once and
failed (the deep-research client could not be resolved in this offline environment).
No provider deep-research file exists; the review rests on the cached publications and
the UniProt record listed below.

Literature checked (cached in `publications/`): PMID:9830105 (abstract only),
PMID:8021172 (abstract only). PMID:17218307 (phosphoproteome) was not fetched; it is
cited only through UniProt for the Ser62 phosphorylation.

### Identity

- UniProt P39773 GPMI_BACSU, gene gpmI (synonym pgm), BSU33910, 511 aa, B. subtilis 168.
- PANTHER PTHR31637 (2,3-BISPHOSPHOGLYCERATE-INDEPENDENT PHOSPHOGLYCERATE MUTASE),
  subfamily PTHR31637:SF0. Reference protein of the family review
  `interpro/panther/PTHR31637/PTHR31637-review.yaml`.
- Family/domain: TIGR01307 pgm_bpd_ind; Pfam PF06415 iPGM_N and PF01676 Metalloenzyme;
  alkaline phosphatase superfamily fold; HAMAP MF_01038.

### Function

- Cofactor-independent (2,3-BPG-independent) phosphoglycerate mutase; Mn2+-dependent.
  [PMID:8021172 "B. subtilis PGM, which is DPG independent, is very similar to a
  DPG-independent PGM from a plant species but differs from the latter in the absolute
  requirement of B. subtilis PGM for Mn2+"]
- Activity requires Mn2+ and is very pH sensitive. [PMID:9830105 "The enzymatic activity
  of phosphoglycerate mutase (Pgm) from three gram-positive endospore-forming bacteria
  (Bacillus subtilis, Clostridium perfringens, and Sporosarcina ureae) requires Mn2+ and
  is very sensitive to pH"]
- Mn2+ converts an inactive apoenzyme into a catalytically competent form.
  [PMID:9830105 "These findings suggest that Mn2+ binds to catalytically inactive Pgm and
  converts it to a catalytically competent form"]
- Mechanism (HAMAP-inferred): phosphoserine intermediate at Ser62, two Mn ions bound by
  Asp12, Ser62, Asp403, His407, Asp444, His445, His462 (UniProt FT lines, ECO:0000255).
  Ser62 was also found phosphorylated in the phosphoproteome (UniProt FT MOD_RES,
  ECO:0000269 PubMed:17218307), consistent with the catalytic phosphoenzyme.

### Physiology

- Gene is in the pgk-tpi-pgm-eno glycolytic operon. [PMID:8021172 "the operon includes
  pgk (coding for phosphoglycerate kinase) followed by tpi, pgm, and eno"]
- pgm eno double inactivation gives very slow growth and asporogeny. [PMID:8021172
  "Inactivation of pgm plus eno in B. subtilis resulted in extremely slow growth either on
  plates or in liquid"; "these mutants were asporogenous with or without malate
  supplementation"]
- Sporulation link is about regulation OF the enzyme: forespore acidification is proposed
  to inhibit Pgm so that 3-phosphoglycerate accumulates in the spore. [PMID:9830105 "The
  extreme pH sensitivity of the Mn(2+)-dependent Pgms supports a model in which this
  enzyme is inhibited during sporulation by acidification of the forespore, thus allowing
  accumulation of the spore's large depot of 3-phosphoglyceric acid"]. This does not show
  that Pgm regulates sporulation; the GO:0043937 rows are therefore marked as
  over-annotated.

### Annotation decisions (summary)

- Phosphoglycerate mutase activity (IBA, IDA, IEA): ACCEPT, core.
- Manganese ion binding (IBA, IDA, IEA): ACCEPT; metal ion binding MODIFY to Mn binding.
- Catalytic activity: MODIFY to phosphoglycerate mutase activity.
- Cytosol IBA: ACCEPT; cytoplasm IEA: MODIFY to cytosol.
- Carbohydrate metabolic process IBA and glucose catabolic process IEA: MODIFY to
  glycolytic process (GO:0006096); glycolytic process IEA: ACCEPT.
- Regulation of sporulation (IDA, IEA): MARK_AS_OVER_ANNOTATED.
