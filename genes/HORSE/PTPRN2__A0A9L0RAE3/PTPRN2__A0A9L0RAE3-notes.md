# PTPRN2 (horse, A0A9L0RAE3) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: canonical horse PTPRN2 model (UP000002281 gene-centric canonical, Ensembl ENSECAT00000125162 of
ENSECAG00000012762). This review does not use ProtNLM2 output.

### Deep research

`just deep-research-falcon HORSE A0A9L0RAE3 --alias PTPRN2__A0A9L0RAE3 --fallback perplexity-lite`
failed: falcon (Edison) raised "Failed to authenticate", and the perplexity-lite fallback returned
HTTP 401 insufficient_quota. No deep-research file was produced. The review relies on the cached
primary literature already used for human PTPRN2 (genes/human/PTPRN2) and on the sequence analysis
below.

### Evolutionary grounding

- PANTHER PTHR46106:SF5, same subfamily as human Q92932, mouse P80560 and rat Q63475; PTPRN (IA-2) is
  in SF1. Identity to human 74.5% overall, 96.2% over the PTP-like domain, 60.8% over the luminal
  precursor region (see PTPRN2__A0A9L0RAE3-bioinformatics/RESULTS.md).
- Catalytic Cys (horse Cys984 = human Cys945), P-loop VHCSDGAGRSG, WPD-loop Asp, Q-loop Gln,
  tyrosine-based internalization motif and C-terminal leucine-based sorting signal are all conserved.
- IBA nodes: PTN000439769 (family node; granule, synapse, regulation of secretion) and PTN000439772
  (vertebrate node; insulin secretion). Seed identities checked against UniProt cross-references:
  MGI:107418 = Ptprn2, MGI:102765 = Ptprn, RGD:61904 = Ptprn2, RGD:620777 = Ptprn.
- No experimental GO annotation exists for horse PTPRN2; everything is inferred.

### Key literature (orthologs)

- Rat phogrin: [PMID:20097759 "phogrin is able to dephosphorylate specific inositol phospholipids,
  including phosphatidylinositol (PI) 3-phosphate and PI 4,5-diphosphate but not PI 3,4,5-trisphosphate."]
  and [PMID:20097759 "The PIPase activity of phogrin depended on the catalytic site cysteine and
  correlated with effects on glucose-stimulated insulin secretion."]
- Human: [PMID:26620550 "PTPRN2 belongs to the protein tyrosine phosphatase family, but does not exhibit
  activity against phosphoprotein substrates due to several critical amino acid variations in the PTP
  domain (Magistrelli et al, 1996)."]
- Mouse knockout: [PMID:15220191 "The IA-2beta(-/-) mice, in contrast to wild-type controls, showed mild
  glucose intolerance and impaired glucose-stimulated insulin secretion."];
  [PMID:21732083 "Islets from single and DKO mice all showed a significant decrease in insulin content,
  insulin secretion and the number and half-life of DCV"]
- Mouse brain: [PMID:19361477 "IA-2beta, but not IA-2, co-purifies with fractions rich in synaptic
  vesicles (SV)"]. Neurotransmitter release defects are from the double knockout; PAINT did not place
  neurotransmitter secretion on the family node, so it is not added here.

### Decisions

- PTP activity and protein Tyr/Ser/Thr phosphatase activity (IEA): REMOVE (subfamily is inactive on
  phosphoproteins; horse retains the same residues).
- Hydrolase activity: MODIFY to phosphatidylinositol phosphate phosphatase activity (GO:0052866).
- Secretory granule (IBA, IEA): MODIFY to dense core granule membrane.
- Synapse (IBA, IEA) and transport vesicle membrane: MODIFY to synaptic vesicle membrane (checked via
  OLS4 hierarchicalAncestors that GO:0030672 is under transport vesicle membrane and synapse; GO:0032127
  is under secretory granule but not transport vesicle membrane).
- Insulin secretion (IBA, vertebrate node) and regulation of secretion (IBA, family node): ACCEPT.
- Signaling receptor complex (Ensembl Compara from human IDA PMID:23382219): UNDECIDED, as for the
  human donor row; cached full text does not mention PTPRN2.
- No NEW annotations proposed.
