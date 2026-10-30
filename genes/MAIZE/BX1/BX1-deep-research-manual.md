# BX1 (P42390; Benzoxazineless 1) - manual literature research

No deep-research API was available; this summary was compiled manually from cached
publications (publications/PMID_*.md), PubMed searches and the UniProt record
(searched 2026-10-28).

## Identity

- UniProt P42390 (Swiss-Prot, TRPA_MAIZE), 347 aa, "Indole-3-glycerol phosphate lyase,
  chloroplastic"; gene Bx1 (benzoxazineless1), chromosome 4, Zm00001eb165610,
  NCBI GeneID 542117, MaizeGDB 102199.
- One of four maize TrpA (tryptophan synthase alpha) homologs: BX1, IGL, ZmTSAlike and
  ZmTSA [PMID:18430213 "Four TSA homologs are present: BX1, IGL, ZmTSAlike [17], and ZmTSA
  (this work)."].
- First isolated as an abundant pith transcript with homology to TrpA that complements an
  E. coli trpA mutant [PMID:7766899 "the cDNA clone can complement an E. coli trpA
  mutant"]. This complementation shows that the protein can supply indole/alpha activity in
  E. coli; it does not show a role in maize tryptophan synthesis.

## Family and sequence features

- TrpA family: Pfam PF00290, NCBIfam TIGR00262, HAMAP MF_00131, PROSITE PS00167,
  PANTHER PTHR43406 (subfamily SF7 "INDOLE-3-GLYCEROL PHOSPHATE LYASE, CHLOROPLASTIC").
- N-terminal chloroplast transit peptide, residues 1-53 (UniProt, ECO:0000255). In the
  supplementary alignment of PMID:18430213, the BX1 transit peptide is stated to have been
  determined experimentally [PMID:18430213 "for BX1 it was determined experimentally"].
  Exon 1 of Bx1 encodes the transit peptide [PMID:11106389 "In the case of Bx1 ( 11 ) and
  TSA of A. thaliana ( 19 ), exon 1 encodes a transit peptide."].
- Crystal structures 1RD5 and 1TJR (mature protein). The structure resembles the active
  conformation of bacterial TSA: loop alphaL6 closed and the catalytic glutamate in the
  active conformation, which explains the high activity of BX1 without a beta subunit
  [PMID:16120446 "the faster catalytic rate of BX1 may be due to a stabilization of the
  active conformation"].

## Enzyme activity

- Frey et al. 1997 (PMID:9235894, abstract only): "Bx1 encodes a tryptophan synthase alpha
  homolog that catalyzes the formation of indole for the production of secondary
  metabolites rather than tryptophan, thereby defining the branch point from primary to
  secondary metabolism."
- UniProt kinetic data from PMID:9235894: KM 0.013 mM for indole-3-glycerol phosphate,
  kcat 0.02 s-1 per UniProt note. PMID:18430213 Table 1, citing ref. 18 (Frey 1997), lists
  BX1 with KM 13 uM and kcat 2.8 s-1; PMID:11106389 states that IGL kcat of 2.3 s-1 "is
  similar for both enzymes". The UniProt kcat value (0.02 s-1) is therefore probably a
  transcription error for 2.8 s-1 (see notes).
- BX1 activity does not need the beta subunit [PMID:11106389 "In contrast, BX1 activity is
  independent of TSB ( 10 )."].
- BX1 is monomeric in gel filtration and does not bind ZmTSB1 [PMID:18430213 "No
  interaction of ZmTSB1 with ZmTSAlike, BX1, or IGL was detectable."]. UniProt's SUBUNIT
  line describes a homodimer for the lyase activity, based on a crystal structure (Ref.4).
- BX1 is absent from the native leaf tryptophan synthase complex [PMID:18430213
  "ZmTSAlike, BX1, and IGL were not detectable in the native tryptophan synthase complex in
  leaves."].

## Biological role

- First (branch-point) step of benzoxazinoid (DIBOA/DIMBOA) biosynthesis; Bx1-Bx5 are
  clustered on chromosome 4 [PMID:9235894 "Five genes, Bx1 through Bx5, are required for
  DIBOA biosynthesis in maize."]. Indole made by BX1 is hydroxylated by the P450s BX2-BX5.
- BX1 is the main source of benzoxazinoids under developmental control; IGL is
  stress-inducible [PMID:21730199 "The Bx1 gene is under developmental control and is
  mainly responsible for BX production, whereas the Igl gene is inducible by stress
  signals, such as wounding, herbivory, or jasmonates."].
- Bx1 is transcribed mainly in seedlings [PMID:18430213 "In contrast, Bx1 is predominantly
  transcribed in seedlings"].
- bx1 mutants are viable and have no growth defects, and tryptophan in maize is made mainly
  by the ZmTSA/ZmTSB complex [PMID:18430213 "We propose that, despite the availability of
  the highly active monomers BX1 and IGL, in maize tryptophan is predominantly synthesized
  through a tryptophan synthase complex containing ZmTSA and ZmTSB1 or ZmTSB2,
  respectively."]. A minor contribution of BX1 + TSB dimers to tryptophan via indole
  salvage is left open [PMID:18430213 "It remains open, whether a mechanism involving BX1
  monomer and TSB dimer contributes significantly to the total metabolic flux towards
  tryptophan."].
- Emission of volatile indole after herbivore elicitor treatment is IGL-dependent, not
  BX1-dependent [PMID:11106389 "Emission of Volatile Indole Is Independent of a Functional
  Bx1 Gene."].
- Phenotypes of bx1 mutants (downstream consequences of benzoxazinoid loss): more aphid
  growth and reduced penetration resistance to Setosphaeria turcica (PMID:21730199); loss
  of local induced resistance to Spodoptera littoralis (PMID:27538820). These are
  consequences of metabolite deficiency, not activities of BX1.
- Evolution: BX1 arose by duplication and neofunctionalisation of TSA [PMID:19577780 "The
  branchpoint from the primary metabolism (Bx1 gene) can be traced back to duplication and
  functionalisation of the alpha-subunit of tryptophan synthase (TSA)."].

## Localization

- Chloroplast: transit peptide (above); YFP fusions of the maize indole-3-glycerol
  phosphate lyases (BX1, TSA, IGL) localized to chloroplasts [PMID:33458870 "Fusions of
  yellow fluorescent protein with maize IGPS enzymes and indole-3-glycerolphosphate lyases
  were all localized in chloroplasts."].
- Upstream enzyme channelling: IGPS1 interacts with BX1 and IGL in BiFC
  [PMID:33458870 "IGPS1 interacted strongly with BX1 and IGL"].
- BX1 activity is recovered in soluble leaf extracts as a monomer [PMID:18430213 "BX1
  monomer activity was observed in leaf extracts (Figure 4)"].
- Sequence features of the UniProt record (P42390): a single chloroplast transit
  peptide (1-53) and no transmembrane segment or second thylakoid-targeting signal are
  annotated, consistent with a soluble stromal enzyme.
