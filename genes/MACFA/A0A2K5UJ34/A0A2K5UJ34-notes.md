# A0A2K5UJ34 (Macaca fascicularis TTC39C) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

### Identity
- A0A2K5UJ34 (545 aa, TrEMBL, PE 3) is macaque TTC39C. It equals human TTC39C (Q8N584, 583 aa)
  residues 39-583 with 2 substitutions (99.6% identity); the Ensembl model starts at the human
  internal Met39 and lacks residues 1-38 (Q8N584 1-22 annotated disordered; Pfam PF10300 on
  Q8N584 spans 35-498, TPR repeats 315-348, 353-386, 485-518). So it is an N-terminally truncated
  alternative gene model, not a domain-lacking fragment
  [file:MACFA/A0A2K5UJ34/A0A2K5UJ34-bioinformatics/RESULTS-rereview.md "Ungapped identity over the 545 aligned residues is 0.9963"].
- No reviewed or longer macaque TTC39C entry exists in UniProt (only A0A2K5UJ40, 75 aa), so the
  "same-gene canonical" relative rule does not apply; the closest canonical product is human
  TTC39C Q8N584.

### Phylogenetic placement
- PANTHER PTHR31859:SF1 (TTC39C), shared with human/mouse/rat/zebrafish TTC39C; fungal IML2-like
  proteins are also in SF1 in the entries table, but the PAINT cilium node is Eumetazoa (taxon:6072).
- PAINT (PTHR31859-paint.tsv): cilium assembly IBD at PTN001275223 (Eumetazoa) and otolith
  morphogenesis IBD at PTN002840059 (Euteleostomi), both seeded only by zebrafish ttc39c
  (ZDB-GENE-050522-194). The zebrafish IMP to determination of heart left/right asymmetry was NOT
  propagated; treated as a deliberate decision.
- TTC39B (LXR degradation scaffold) is SF4; its function is not transferred.

### Literature
- Xu et al. 2015 [PMID:25860617], full text now cached (re-fetched from PMC during this review):
  ttc39c morphants have fewer/shorter KV cilia ["both the number and length of the KV cilia were significantly reduced in the ttc morphants"],
  paralysed pronephric cilia (5.6 Hz vs 42.2 Hz), abnormal otoliths and randomized heart tubes;
  body curvature rescued by MO-resistant mRNA. TTC39C "showed weak association with IFT144 and IFT139,
  two subunits of IFT-A". Localization unknown: "the antibody did not work for immunostaining".
- The falcon deep research's C. elegans localization (Pir et al. 2024, "TTC39A/C") cannot be tied to
  SF1; the only reviewed worm family member (ttc-39B, Q09266) is SF9. Dropped as support for a
  ciliary location.

### Decisions (changes from previous review)
- GO:0032474 otolith morphogenesis (IEA TreeGrafter): MARK_AS_OVER_ANNOTATED -> REMOVE. Downstream
  morphant organismal phenotype; the paper states otolith formation requires cilia motility;
  primates have otoconia.
- GO:0060271 cilium assembly (IEA TreeGrafter): ACCEPT retained, now grounded on PAINT node + SF1
  membership + full-text cellular phenotype and IFT-A association (single MO study caveat).
- Core function: removed MF GO:0030674 protein-macromolecule adaptor activity (no evidence beyond
  a weak co-IP) and location GO:0005929 cilium (no vertebrate localization; worm orthology not
  established). Kept directly_involved_in cilium assembly.
- Description rewritten: removed worm localization and TTC39B-derived claims as function of this gene.

### Relative
- Zebrafish ttc39c (Q1LXE6, DANRE), same subfamily SF1 and the sole PAINT seed; no review in repo.
- Family review interpro/panther/PTHR31859/PTHR31859-review.yaml places A0A2K5UJ34 in SF1 (agrees).
  No modules reference TTC39 or PTHR31859.
