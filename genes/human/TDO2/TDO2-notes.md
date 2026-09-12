# TDO2 (human) — gene review notes

UniProt: P48775 (T23O_HUMAN). Gene: TDO2 (HGNC:11708). 406 aa. Chromosome 4.

## Core identity and function

TDO2 encodes **tryptophan 2,3-dioxygenase** (TDO; EC 1.13.11.11), a **heme-dependent
dioxygenase** that catalyzes the oxidative cleavage of the pyrrole ring of L-tryptophan,
converting L-tryptophan + O2 to N-formyl-L-kynurenine. This is the **first and
rate-limiting, committed step of the kynurenine pathway** of tryptophan catabolism, which
routes ~95% of dietary tryptophan and ultimately supplies de novo NAD+ biosynthesis.

- UniProt FUNCTION: "Heme-dependent dioxygenase that catalyzes the oxidative cleavage of
  the L-tryptophan (L-Trp) pyrrole ring and converts L-tryptophan to N-formyl-L-kynurenine.
  Catalyzes the oxidative cleavage of the indole moiety."
  [file:human/TDO2/TDO2-uniprot.txt]
- CATALYTIC ACTIVITY: "L-tryptophan + O2 = N-formyl-L-kynurenine; ... EC=1.13.11.11"
  (Rhea:RHEA:24536). [file:human/TDO2/TDO2-uniprot.txt]
- COFACTOR: "Name=heme ... Note=Binds 1 heme group per subunit." His328 is the axial
  (proximal) heme iron ligand. [file:human/TDO2/TDO2-uniprot.txt]
- PATHWAY: "Amino-acid degradation; L-tryptophan degradation via kynurenine pathway;
  L-kynurenine from L-tryptophan: step 1/2." [file:human/TDO2/TDO2-uniprot.txt]
- SUBUNIT: "Homotetramer. Dimer of dimers." [file:human/TDO2/TDO2-uniprot.txt]

TDO is [PMID:27762317 "the first and rate-limiting step of the kynurenine pathway for L-Trp
catabolism"]; "The majority of dietary Trp (~95%) is metabolized in the liver through this
pathway to produce NAD+" [PMID:27762317]. TDO is [PMID:28285122 "mainly expressed in the
liver, has high substrate specificity for L-tryptophan, and its activity is increased by the
substrate"], contrasting with the immune enzyme IDO1 which has widespread tissue distribution,
less substrate specificity, and inflammation-induced activity [PMID:28285122]. In mouse
knockout models, TDO was estimated [PMID:28285122 "to account for 75% of tryptophan
oxidation"].

## Structure / catalysis

- Crystal structure of human TDO in ternary complex with L-Trp and O2, and binary complex
  with product N-formylkynurenine (NFK): [PMID:27762317 "we report the crystal structure of
  human TDO (hTDO) in a ternary complex with the substrates L-Trp and O2 and in a binary
  complex with the product N-formylkynurenine (NFK)"]. Reaction "initiated by a direct
  attack of O2 on the C2 atom of the L-Trp indole ring." Proximal ligand: "the proximal
  His328 ligand coming from the C-terminal region of helix αJ."
- Apo (heme-free) hTDO structure at 2.90 Å; tetramer, active-site architecture conserved;
  mutational studies confirmed eight residues critical for L-Trp oxidation
  [PMID:25066423 abstract]. Key active-site mutants (Y42A, Y45A, F72A, H76A, F140A, R144A,
  S151A, H328A) reduce/abolish activity (UniProt MUTAGEN, ECO:0000269|PubMed:25066423).
- Homotetramer / dimer of dimers confirmed by gel filtration; disease variant Met108Ile
  "is predominately a homotetramer as reported for the native human enzyme" [PMID:28285122].
- Exo (non-catalytic) L-Trp binding site ~42 Å from active site regulates cellular stability:
  L-Trp binding to this exo site "retards the degradation of hTDO through the
  ubiquitin-dependent proteasomal pathway" [PMID:27762317]. This is the molecular basis for
  substrate-induced stabilization / short half-life of TDO.

## Localization

Cytosolic enzyme. Reactome: "Cytosolic tryptophan 2,3-dioxygenase (TDO) tetramer catalyzes
the conversion of L-tryptophan and oxygen to formylkynurenine" [Reactome:R-HSA-71188].
Enzyme assayed directly from **liver cytosol** across species [PMID:29959909 "liver cytosol
contained sufficient active TDO2"]. GO cytosol annotations: IDA (PMID:29959909, FlyBase),
TAS (Reactome), IEA (orthology). Consistent — cytosol accepted as core CC.

## Regulation / physiology

- Hepatic; induced by substrate (tryptophan), by histidine, and by **glucocorticoids**
  [Reactome:R-HSA-71188 "induced by metabolites such as tryptophan and histidine, and by
  glucocorticoids"]. Comings et al. reported a glucocorticoid-response-like element in the
  TDO2 promoter [PMID:8666386, sequence paper].
- Disease: **Hypertryptophanemia (HYPTRP, MIM:600627)**, autosomal recessive, first human
  case with compound heterozygous TDO2 variants (Met108Ile + a frameshift) established by
  [PMID:28285122]. Biochemical phenotype (persistent hypertryptophanemia + hyperserotoninemia)
  reported as benign/without significant clinical consequences in that case.

## Ensembl-projected IEA BP annotations (rat ortholog P21643)

`response to ethanol` (GO:0045471), `response to cortisol` (GO:0051414), `response to
dexamethasone` (GO:0071548), `response to nitroglycerin` (GO:1904842). These are
electronically transferred from the rat ortholog via Ensembl Compara (GO_REF:0000107,
ECO:0000265). Cortisol/dexamethasone responses are biologically plausible (TDO is a classic
glucocorticoid-inducible hepatic enzyme; see Reactome and the glucocorticoid-response element
in PMID:8666386) — kept as non-core regulatory/stimulus-response terms. `response to ethanol`
and `response to nitroglycerin` are narrow rat-specific transcriptional-response observations,
kept as non-core. None are core molecular functions.

## Molecular-function / binding IEA annotations to scrutinize

- `amino acid binding` (GO:0016597, IEA Ensembl from rat): substrate L-Trp is an amino acid;
  this is a generic parent capturing substrate binding. Kept as non-core (the specific
  catalytic MF GO:0004833 already entails L-Trp binding).
- `oxygen binding` (GO:0019825, in UniProt DR but not in current GOA TSV): O2 is a
  co-substrate; captured by catalytic activity. (Not present as a separate row in the GOA
  TSV under review, so no annotation entry needed.)
- `metal ion binding` (GO:0046872, IEA InterPro/UniProtKB-KW): TDO binds heme iron; the
  informative term is `heme binding` (GO:0020037, well supported by IDA). `metal ion binding`
  is a redundant generic parent — MARK_AS_OVER_ANNOTATED.

## Protein-binding IPI annotations (over-annotation)

All `protein binding` (GO:0005515) IPI rows derive from high-throughput interactome / Y2H /
affinity-capture screens (PMID:16189514, 24722188, 25416956, 25910212, 28514442, 31515488,
32296183, 32814053, 33961781). Partners (AHCYL1, ASMTL, CALR, CDH1, DLST, DPM1, EIF4E, LNX1,
MOB1A/3C, NEK7, NGB, NMNAT1, NR1D1, PICK1, PM20D2, SDCBP/2, ZFYVE26, etc.) are heterogeneous
and do not define a specific characterized molecular function for this cytosolic metabolic
enzyme. Per policy, bare `protein binding` IPI is MARK_AS_OVER_ANNOTATED (not removed).
`identical protein binding` (GO:0042802, IPI self) reflects the well-established homotetramer
and is retained as non-core supporting evidence for oligomerization (the informative term is
`protein homotetramerization`, GO:0051289, IDA).

## Core functions (summary)

1. MF: L-tryptophan 2,3-dioxygenase activity (GO:0004833) — heme-dependent; well supported
   by IDA/EXP (PMID:25066423, 27762317, 28285122).
2. MF: heme binding (GO:0020037) — cofactor; IDA (PMID:27762317, 28285122).
3. BP: L-tryptophan catabolic process (GO:0006569) — kynurenine pathway; IDA (PMID:27762317).
   Contributes to 'de novo' NAD+ biosynthesis from L-tryptophan (GO:0034354).
   [GO:0019441 "L-tryptophan catabolic process to L-kynurenine" is OBSOLETE — do not use.]
4. CC: cytosol (GO:0005829) — IDA/TAS.

## Action tally rationale

- ACCEPT: catalytic MF (GO:0004833) IDA/EXP/TAS/IBA; heme binding (GO:0020037) IDA/IBA;
  L-tryptophan catabolic process (GO:0006569) IDA/IBA; cytosol (GO:0005829) IDA/TAS;
  protein homotetramerization (GO:0051289) IDA.
- ACCEPT (IEA, correct): GO:0004833 IEA, GO:0006569 IEA, GO:0020037 IEA, cytosol IEA.
- KEEP_AS_NON_CORE: identical protein binding (self/homotetramer); amino acid binding;
  response to cortisol; response to dexamethasone; response to ethanol; response to
  nitroglycerin.
- MARK_AS_OVER_ANNOTATED: metal ion binding (redundant generic parent of heme binding);
  all bare `protein binding` IPI (high-throughput interactome).
</content>
</invoke>
