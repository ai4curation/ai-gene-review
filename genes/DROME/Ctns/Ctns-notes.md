# Ctns (Q9VCR7) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used.

### Identity
- Q9VCR7 is the reviewed Swiss-Prot canonical entry for FlyBase FBgn0039045 (Ctns, CG17119),
  397 aa, signal peptide 1..24, seven TM helices, two PQ-loop repeats (Pfam PF04193 x2,
  NCBIfam TIGR00951). Not a fragment, isoform or alternative gene model.
- PANTHER PTHR13131:SF5 (CYSTINOSIN), the same subfamily as human CTNS (O60931), mouse Ctns,
  worm ctns-1, yeast ERS1 and YCL002C, Arabidopsis At5g40670 (interpro/panther/PTHR13131/PTHR13131-entries.csv).
  The family review interpro/panther/PTHR13131/PTHR13131-review.yaml also places Q9VCR7 in SF5: no disagreement.

### Evidence
- Fly: endogenous tagging places dCTNS on fat-body lysosomes; knockout accumulates cystine; fasting
  cysteine falls; cysteamine (cystinosin-independent lysosomal cystine export) or low-dose cysteine rescues
  starvation sensitivity [PMID:35175796 "The role of dCTNS during starvation was dependent on its cystine transport function"].
  TORC1 reactivation and autophagy loss in mutants are downstream of cysteine/CoA supply, so no TORC1
  or autophagy process terms are proposed.
- Human ortholog in the same subfamily: H+-driven lysosomal cystine export shown directly
  [PMID:11689434 "We conclude that cystinosin represents a novel H(+)-driven transporter that is responsible for cystine export from lysosomes"].
  Proton coupling has not been tested for the fly protein.

### Changes from the earlier review
- FlyBase ISS rows (GO:0015171, GO:0003333; PMID:17443808) give Eaat1 (FBgn0026439) as the similarity
  partner. Eaat1 is SLC1 (PF00375, PTHR11958), unrelated to cystinosin
  (Ctns-bioinformatics/RESULTS-rereview.md, compare_iss_donor_families.py). The terms are true but
  broad, so MODIFY to the cystine terms, with a WRONG_WITH_FROM source defect for FlyBase.
- Lysosomal membrane IMP from PMID:35175796 is really a direct localization assay (IDA); recorded as
  a PROBABLE WRONG_EVIDENCE_CODE source defect, annotation accepted.
- GO:0015811 L-cystine transport (ISS) and GO:0034486 vacuolar transmembrane transport (IBA) changed
  from ACCEPT/KEEP_AS_NON_CORE to MODIFY -> GO:1904919, since they are correct but general ancestors
  of a term the gene already carries.
- Description rewritten; core function now cites the human transport assay and the subfamily check.
- Status set to COMPLETE.

### Relative
- Human CTNS (O60931), same PANTHER subfamily SF5 and in the IBA donor set; complete review at
  genes/human/CTNS/CTNS-ai-review.yaml (status COMPLETE).
- No module in modules/ covers lysosomal cystine export.
