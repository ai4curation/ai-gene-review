# THG1L (Q9NWX6) — Gene Review Notes

Human tRNA(His) guanylyltransferase homolog. HGNC:26053. Gene ID 54974. Chr 5.
Synonyms: ICF45 (Interphase Cytoplasmic Foci protein 45), IHG-1 (Induced in High Glucose-1).
298 aa; PANTHER PTHR12729; Pfam PF04446 (Thg1) + PF14413 (Thg1C).

## Deep research status
- `falcon` (Edison) provider returned HTTP 402 Payment Required — unavailable.
- `perplexity` provider not present in installed `deep-research-client` build.
- `asta` provider ran and produced `THG1L-deep-research-asta.md`, but it is **retrieval-only
  and entirely off-target** (generic genome-annotation / database papers; none about THG1L).
  Not used as evidence. Review below is grounded in the UniProt record, GOA, and the cached
  primary literature.

## Core biology

### 1. Canonical enzyme: tRNA(His) guanylyltransferase (EC 2.7.7.79)
- Adds a single guanylate (G-1) to the 5' end of tRNA(His) after transcription and RNase P
  cleavage, via an unusual **3'-5' nucleotidyl addition** (opposite direction to all canonical
  polymerases). G-1 is required for tRNA(His) identity/aminoacylation and translational fidelity.
- Human THG1 (hTHG1) crystal structure solved at 2.3 Å; despite no sequence similarity it shares
  active-site architecture with 5'-3' DNA polymerases and adenylyl/guanylyl cyclases and uses a
  **two-metal-ion (Mg2+) mechanism** [PMID:21059936 "The 2.3-Å crystal structure of human THG1
  (hTHG1) reported here shows that, despite the lack of sequence similarity, hTHG1 shares
  unexpected structural homology with canonical 5′-3′ DNA polymerases and adenylyl/guanylyl
  cyclases, two enzyme families known to use a two-metal-ion mechanism for catalysis."].
- Reaction consumes ATP to activate the monophosphorylated tRNA 5'-end before GMP addition
  [PMID:21059936 "The 3′-5′ addition reaction catalyzed by Thg1 requires consumption of an
  additional ATP to activate a monophosphorylated 5′-end for addition of the first nucleotide."].
- Biochemistry/structure (from full text; curator-read): homotetramer; binds 2 Mg2+ per subunit;
  binds GTP and ATP; extensive active-site mutagenesis (D58A −99.5%, D105A / H181A / N227A loss,
  T127A abolishes oligomerization + activity). Supports MF annotations: GO:0008193 tRNA
  guanylyltransferase activity (IDA), GO:0000287 magnesium ion binding (IDA), GO:0005524 ATP
  binding (IDA), GO:0005525 GTP binding (IDA), GO:0000049 tRNA binding (TAS), GO:0051289 protein
  homotetramerization (IPI), GO:1990234 transferase complex (part_of the homotetramer).
- Note: UniProt names it "**Probable** tRNA(His) guanylyltransferase" — the enzymatic activity is
  demonstrated in vitro, but the in vivo tRNA(His) substrate role in human is inferred/less
  established than in yeast (where Thg1 is essential). Thg1-family enzymes also perform 5'-end
  tRNA repair (3'-5' addition to 5'-truncated tRNAs), relevant to a mitochondrial tRNA role.

### 2. Moonlighting function: mitofusin GEF → mitochondrial fusion
- IHG-1 (= THG1L) forms complexes with mitofusins MFN1 and MFN2 and enhances GTP binding by MFN2,
  acting as a **guanine nucleotide exchange factor (GEF)** [PMID:25008184 "IHG-1 forms complexes
  with known mediators of mitochondrial fusion-mitofusins (Mfns) 1 and 2-and enhances the
  GTP-binding capacity of Mfn2, suggesting that IHG-1 acts as a guanine nucleotide exchange
  factor."].
- Overexpression increases mitochondrial fusion and protects from ROS-induced apoptosis;
  knockdown reduces respiratory capacity, ATP production and fusion [PMID:25008184 "inhibition of
  endogenous IHG-1 expression results in reduced mitochondrial respiratory capacity, ATP
  production, and mitochondrial fusion. Conversely, overexpression of IHG-1 leads to increased
  mitochondrial fusion and also protects cells from reactive oxygen species-induced apoptosis."].
- Mitochondrial localization is required for the MFN interaction/fusion effect [PMID:25008184
  "IHG-1 must be localized to mitochondria to interact with Mfn1 and Mfn2, and this interaction is
  necessary for increased IHG-1-mediated mitochondrial fusion."].
- Supports: GO:0005085 GEF activity (IDA), GO:0008053 mitochondrial fusion (IDA), GO:1990046
  stress-induced mitochondrial fusion (IDA), GO:0006979 response to oxidative stress (IDA),
  GO:0005741 mitochondrial outer membrane, GO:0005739 mitochondrion.

### Localization
- Cytoplasm (original ICF45 characterization, PMID:15459185) and mitochondrion / mitochondrial
  outer membrane (PMID:25008184; HTP mito proteome PMID:34800366). Both cytosolic and
  mitochondrial pools consistent with dual tRNA + mitochondrial-fusion roles.

### Disease
- Biallelic THG1L variants cause **SCAR28** (autosomal recessive spinocerebellar ataxia 28;
  MIM:618800): motor delay, gait ataxia, dysarthria. The p.Val55Ala variant decreases
  mitochondrial fusion [UniProt VAR_083901; PMID:27307223, PMID:31168944] — links disease to the
  mitochondrial-fusion function rather than (only) the tRNA role.

## Protein-binding / interactome annotations (uninformative; non-core)
- GO:0005515 protein binding (IPI): TERF1/TRF1 (PMID:21044950 telomere complementation screen),
  SDCBP (PMID:25416956 HuRI), LNX1/NTAQ1/PLEKHF2 (PMID:32296183 HuRI), plus MFN1/MFN2 partners
  captured in PMID:25008184. All high-throughput or partner-listing; "protein binding" is
  uninformative per curation guidelines → keep as non-core.
- GO:0042802 identical protein binding (IPI, self Q9NWX6-Q9NWX6): PMID:21059936, 21516116,
  25416956 — the self-interaction is real and reflects the established homotetramer.

## Proposed core functions
1. tRNA(His) guanylyltransferase activity (GO:0008193) — ancestral/biochemically-demonstrated MF.
2. Guanyl-nucleotide exchange factor activity for mitofusins (GO:0005085) driving mitochondrial
   fusion (GO:0008053) — experimentally-demonstrated moonlighting function; disease-relevant.
