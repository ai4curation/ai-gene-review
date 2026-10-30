# kefA (PP_5067, Q88CW3): notes

Dashboard protein: [NZ_LGRH01000055.1_2](https://gene-annotate-dashboard.kbase.us/review/NZ_LGRH01000055.1_2) (*P. putida*, tier A).
The review is filed on the KT2440 reference-proteome entry Q88CW3, which is 98.8% identical to it (1089/1102, global alignment). The exact-sequence UniProt entries are deleted.

## Conclusion

PP_5067 is an MscK-type mechanosensitive channel. The assignment is by orthology only: no experiment has been done on the *P. putida* protein.
- **Homology.** It is 43.1% identical to *E. coli* MscK (P77338) over its full length (1077 aligned pairs). It is in PANTHER PTHR30347:SF1 (MscK) and NCBIfam PRK11281.
- **Topology.** DeepTMHMM predicts a 1-24 N-terminal signal or anchor, a ~465-residue extracytoplasmic region and 11 TM helices. All 11 map in order onto the 11 UniProt TM helices of *E. coli* MscK. The C-terminus is cytoplasmic and MscS-like.
  - This matches the MscK cryo-EM architecture: a periplasmic domain, an 11-helix TM domain and a cytoplasmic domain, assembled as a heptamer (PMID:36371466).
  - Whether the N-terminal segment is cleaved, as DeepTMHMM and SignalP predict, is untested.
- **Conserved residues.** MscK W914 (the periplasmic Trp gate) is conserved as W897, and the gating-sensitive G922 as G905.
- **What E. coli MscK does.**
  - It gates under membrane tension, but only with high external K+, NH4+, Rb+ or Cs+. It has a slight anion preference and is not K+-selective (PMID:12374733).
  - It has no major role in downshock survival (PMID:10202137).
  - The kefA2 allele disturbs K+ pools in high-K+ medium (PMID:11985727).
  - The C-terminal MscS-like part alone can rescue downshock (PMID:12505982).
  - "K+ efflux" in the UniProt name is historical, and the protein is unrelated to KefB/KefC.

Analysis: `kefA-bioinformatics/` (BERIL run `20261030T211325Z-kefa-homology-topology`).

## Dashboard verdict: supported for the channel, overreach on "polymyxin B tolerance"

On the dashboard scale, the recommended verdict is **overreach**, but only for the phenotype clause. Equivalently, it is "partially supported".

Suggested annotation: *MscK-family mechanosensitive ion channel (K+-dependent gating by homology to E. coli MscK); physiological role unknown.*

GO terms (PredictionReview `kefA-dashboard-predictions-review.yaml`):
- GO:0008381 mechanosensitive monoatomic ion channel activity: **CNN** (already IEA in GOA).
- GO:0034220 monoatomic ion transmembrane transport: **CNN** (already IEA in GOA).

## Polymyxin B: what the evidence actually is

- **One homolog.** The phenotypes come from *P. simiae* WCS417 at 76% identity.
- **One compound.** All 11 experiments use polymyxin B, at 0.002 and 0.003 mg/ml in R2A, with fitness -2.77 to -1.34 and t -4.8 to -10.1.
- **The defects are consistent, but they are one condition type in one organism.**
- **No other evidence.** The dashboard evidence has no KT2440 data, no cofitness, and no paper linking MscK to polymyxin.
- **The other homologs differ.** *P. stutzeri* RCH2 (61.6%) shows nickel sensitivity, and *Klebsiella* (44%) a positive D-alanine phenotype.
- **Not checked.** The Fitness Browser returned HTTP 403, so it was not possible to check whether KT2440 PP_5067 or the *P. simiae* gene has phenotypes in other conditions, or whether the polymyxin phenotype is specific.
- **Interpretation.** A membrane-tension channel affecting tolerance to a membrane-disrupting cationic peptide is plausible. It is a lead, not a property, and is not annotated here.

## Caveats

- The dashboard's PaperBLAST "MscL-like" KT2440 summary is a loose label. The protein is MscS-family, as the call itself noted.
- No KT2440 fitness data was available: `just fetch-fitness` failed, and fit.genomics.lbl.gov returned 403.
- `validate-predictions` writes `reports/prediction-evidence.json`, a shared report file outside this folder.
