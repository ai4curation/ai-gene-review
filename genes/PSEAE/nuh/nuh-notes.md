# nuh (PA0143, Q9I6Y9) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I6Y9 --alias nuh` (accession fetch). Accession Q9I6Y9
(unreviewed, PE4) matches the worklist. No deep-research keys; literature from the cached seed
paper (PMID:15995202, abstract-only; PMC1169536 full text not retrievable) and the UniProt
record.

## Identity

- Inosine-uridine-preferring nucleoside hydrolase (IU-NH), Pfam IU_nuc_hydro, PTHR12304:SF4
  (uridine nucleosidase subfamily). 350 aa with a predicted Sec signal peptide (SignalP
  1-30), so the mature protein (31-350) is likely exported/periplasmic rather than cytosolic.
  UniProt SubName "Nonspecific ribonucleoside hydrolase" (imported, ECO:0000313 — not used as
  evidence).

## Literature

- Nuh degrades adenosine; required for growth on adenosine as sole carbon source; used as a
  LasR reporter (Nuh- phenotype)
  [PMID:15995202 "lasR mutants did not grow on adenosine as the sole carbon source because a key degradative enzyme, nucleoside hydrolase (Nuh), is positively controlled by LasR"];
  [PMID:15995202 "five consecutive cycles of 48 h of incubation sufficed to enrich for about 10% of spontaneous mutants with a Nuh(-) phenotype"].

## Annotation decisions

- Purine nucleosidase activity (IBA, IMP): ACCEPT core. Purine nucleoside catabolic process
  (IBA): ACCEPT core.
- Purine nucleotide metabolic process (IMP, GO:0006163, PseudoCAP): MODIFY -> GO:0006152
  purine nucleoside catabolic process, with a PSEUDOCAP WRONG_TERM / REPOINT defect
  (PROBABLE). Nuh acts on adenosine, a nucleoSIDE, not a nucleoTIDE; GO:0006163 is the wrong
  branch and GO:0006152 is already asserted by IBA.
- Hydrolase, hydrolyzing N-glycosyl compounds (IEA, GO:0016799): TOO_GENERAL (GO:0008477 is
  its is_a descendant).
- Uridine nucleosidase activity (IBA, IEA, GO:0045437) and uridine catabolic process (IBA,
  GO:0006218): KEEP_AS_NON_CORE. Plausible for a nonspecific IU-NH (PTHR12304:SF4), but the
  only experimental substrate for this gene is adenosine; kept as inferred non-core activity.
- Cytosol (IBA, is_active_in, GO:0005829): MARK_AS_OVER_ANNOTATED with a propagation_review.
  The IBD is seeded only by two cytosolic Arabidopsis enzymes; nuh has a Sec signal peptide,
  so it is exported, probably periplasmic. Compartment does not transfer. Flagged, not removed,
  because the signal peptide is a single computational line.
- Action counts: ACCEPT 3, MODIFY 1, TOO_GENERAL 1, KEEP_AS_NON_CORE 3,
  MARK_AS_OVER_ANNOTATED 1. Defects: PSEUDOCAP 1.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000266727 | GO:0008477 purine nucleosidase activity | 5 | 140 (76 taxa) | GO:0008477, IMP, PMID:15995202 | SOUND | Nuh is the nucleoside hydrolase that degrades adenosine (a purine ribonucleoside); loss of adenosine utilization identifies the activity. Genetic (growth) evidence, not a direct assay, but sufficient to identify the function. | Leishmania major nonspecific nucleoside hydrolase Q4QDN1 (IDA GO:0008477 PMID:10409664, same PTHR12304:SF4), Arabidopsis AT1G05620 and AT2G36310, E. coli RihC P22564 | Yes; grounded in the Leishmania IDA purine nucleosidase and plant seeds |

The GO:0008477 IBD at PTN000266727 (PTHR12304 IU-NH clade, 140 leaves in 76 taxa) is grounded
in an IDA purine nucleosidase of nuh's own PANTHER subfamily (Q4QDN1), so the IBD stands and
the node term suits the clade; no GO_CENTRAL defect on the activity IBD. A separate concern is
the cytosol IBD at the same node, seeded only by cytosolic plant enzymes: it does not fit
signal-peptide-bearing bacterial members (recorded as a propagation_review on the cytosol row,
not a defect, since compartment is genuinely not conserved across this broad clade).
