# Pnkd (rat, D3ZXB0) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: D3ZXB0 is the rat Pnkd canonical product (RGD:2300155, ENSRNOG00000014806,
reference proteome, PE1). It is the relative of the ProtNLM2 benchmark product B4F7D2
(genes/rat/Pnkd/), an alternative splice product of the same gene. No ProtNLM2 file or
prediction-evidence folder was opened for this review.

### Data and provenance
- `just fetch-gene rat D3ZXB0 --alias Pnkd__D3ZXB0`: 22 GOA rows, all IEA or RGD ISO
  (GO_REF:0000121). **There is no experimental GO annotation made in rat.**
- Deep research: `just deep-research-falcon rat Pnkd__D3ZXB0 --fallback perplexity-lite`
  failed twice (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401
  insufficient_quota). No deep-research file exists for this folder; the review uses the
  cached primary literature directly.
- Publications cached/read: PMID:21487022 (full text), PMID:25730884 (full text),
  PMID:19124534, PMID:15496428, PMID:22214848, PMID:28199844, PMID:15188056 (abstracts),
  PMID:22418241 (full text, rat cardiomyocytes).

### Evolutionary grounding
- UniProt D3ZXB0 cross-reference: PANTHER PTHR11935:SF116 (HYDROLASE PNKD-RELATED); PANTHER
  19.0 rat classification lists the same gene (RGD=2300155, represented by F1M1E4) in SF116,
  together with mouse Q69ZP3 and human Q8N490. So the experimentally studied mouse and human
  proteins are the 1:1 orthologs in the same subfamily; transfer of PNKD-specific functions
  is justified at the gene level. HAGH (glyoxalase II) is a different subfamily.
- PAINT (interpro/panther/PTHR11935/PTHR11935-paint.tsv): GO:0016790 thiolester hydrolase
  activity at the root PTN004322580 (reaches PNKD); GO:0004416 hydroxyacylglutathione
  hydrolase activity at PTN000232795, which does not reach PNKD (human and mouse PNKD lack
  the GO:0004416 IBA); GO:0006749 glutathione metabolic process only on the HAGH node
  PTN002631193; mitochondrion GO:0005739 at PTN000940186, seeded only by human Q8N490
  (Eumetazoa). The omission of GO:0004416 and of glyoxalase-pathway process terms for the
  PNKD branch is treated as a deliberate curator decision.
- Bioinformatics (Pnkd__D3ZXB0-bioinformatics/RESULTS-d3zxb0.md): D3ZXB0 (424 aa) is
  421/424 identical to mouse Q69ZP3-3, i.e. the long isoform carrying the 39-residue exon
  (80-118, AIGFPCGILFFVL...) that in MR-1S follows the shared exon 1. It is 382 identical
  residues with mouse PNKD-L (Q69ZP3-1). The N-terminal 79 residues, including A7, A9 and
  A33 (the disease positions in the MTS), and all seven Zn(2+) ligands (human 172/174/176/
  177/229/253/291 -> rat 211/213/215/216/268/292/330) are conserved. The extra exon gives
  the most hydrophobic window (Kyte-Doolittle 2.18, residues 74-92), matching the Phobius
  TM call.
- D3ZXB0 lacks the MR-1S-specific C-terminal tail and lacks the alternative N-terminus of
  MR-1M; isoform-specific annotations from those products (COX assembly from MR-1S; ER/Golgi
  from MR-1M) do not transfer cleanly to this product.

### Experimental knowledge (all in other species or with exogenous constructs)
- Enzyme: human PNKD-L hydrolyses S-D-lactoylglutathione at a very low rate and fails to
  rescue HAGH-null flies [PMID:21487022 "PNKD-L has extremely low but consistent SLG
  hydrolysis activity"; "further supporting the idea that PNKD-L does not use SLG as an in
  vivo substrate"]. Lower glutathione in Pnkd KO mouse cortex.
- Synapse: mouse Pnkd-L co-IPs RIM1/RIM2 from cortex, localizes to presynaptic terminals,
  and overexpressed PNKD suppresses SV exocytosis in cultured rat hippocampal neurons
  (exogenous construct, not endogenous rat protein) [PMID:25730884 "Overexpressed PNKD
  protein suppresses release, and mutant PNKD protein is less effective than wild-type at
  inhibiting exocytosis."]. KO mice: reduced RIM1/2, impaired synaptic strength.
- Localization dispute: plasma membrane for PNKD-L [PMID:15496428; PMID:21487022] vs
  mitochondrial with cleaved 39-aa MTS for MR-1L and MR-1S [PMID:19124534].
- Mutant knock-in/transgenic mice: dopamine dysregulation, dystonia-like phenotype
  [PMID:22214848] — phenotypes of dominant disease alleles; I do not treat them as process
  participation.
- MR-1S as COX assembly factor with PET100/PET117 [PMID:28199844] — short isoform.
- Rat studies (PMID:22418241 etc.): mostly overexpression of human MR-1(S) in neonatal rat
  cardiomyocytes, plus siRNA against rat MR-1; isoform-ambiguous, cardiac hypertrophy
  phenotypes; low weight for D3ZXB0 function.

### Decisions summary
- GO:0004416 IEA -> MODIFY to GO:0016790 (PAINT placement + biochemistry).
- GO:0051596 IEA -> REMOVE.
- Mitochondrion (IEA, ISO x2) -> ACCEPT (MTS conserved; PAINT IBD; Ghezzi 2009).
- Cytoplasm (IEA, ISO) -> MODIFY to mitochondrion.
- Plasma membrane (IEA, ISO) -> KEEP_AS_NON_CORE (disputed).
- Membrane (IEA, ISO) -> MODIFY to plasma membrane / mitochondrial inner membrane.
- ER, Golgi (ISO) -> MARK_AS_OVER_ANNOTATED (MR-1M-specific).
- Presynaptic cytosol (IEA, ISO) -> ACCEPT.
- Negative regulation of neurotransmitter secretion (IEA, ISO x2) -> ACCEPT (core).
- COX IV assembly (ISO from MR-1S) -> MARK_AS_OVER_ANNOTATED for this product.
- Dopaminergic transmission / dopamine metabolism / posture (ISO of mouse mutant IMP) ->
  MARK_AS_OVER_ANNOTATED.
