# CRBN (Cereblon) — Gene Review Notes

UniProt: Q96SW2 (CRBN_HUMAN), 442 aa. HGNC:30185. Gene on chromosome 3.

## Summary of function

CRBN (cereblon) is the substrate-recognition (substrate-receptor) subunit of a CRL4
cullin-RING E3 ubiquitin ligase, the DCX/CRL4(CRBN) complex composed of DDB1, CUL4A or
CUL4B, RBX1 and CRBN. It recruits substrate proteins for ubiquitination and subsequent
proteasomal degradation [PMID:20223979, PMID:25108355, PMID:26909574]. Structurally it has
an N-terminal Lon-protease-like domain (no protease activity; the ATP-binding/catalytic
residues are absent — UniProt CAUTION) and a C-terminal thalidomide-binding domain (CULT
domain) that coordinates a structural Zn2+ ion and binds thalidomide-class drugs. DDB1 is
bound via the N-terminal region [PMID:25108355].

## E3 ligase / substrate receptor role (core)

- CRBN forms a DCX (DDB1-CUL4-X-box) / CRL4(CRBN) E3 ubiquitin ligase with DDB1, CUL4A and
  RBX1 [PMID:20223979 "CRBN forms an E3 ubiquitin ligase complex with damaged DNA binding
  protein 1 (DDB1) and Cul4A"]. ComplexPortal records both CUL4A (CPX-2759) and CUL4B
  (CPX-2762) variants (UniProt DR lines), supporting part_of both Cul4A-RING and Cul4B-RING
  E3 ubiquitin ligase complex.
- The complex is "important for limb outgrowth and expression of the fibroblast growth
  factor Fgf8 in zebrafish and chicks" [PMID:20223979]. Thalidomide binding inhibits the
  associated ligase activity, the basis of teratogenicity [PMID:20223979].
- Endogenous substrates ubiquitinated/degraded by CRL4(CRBN) include MEIS2, GLUL (glutamine
  synthetase), ILF2 (UniProt FUNCTION summary; PMID:26990986, PMID:33009960). These support
  protein ubiquitination and proteasome-mediated ubiquitin-dependent protein catabolic
  process (involved_in).

## IMiD / molecular-glue neosubstrate biology (drug-induced, not endogenous)

- Thalidomide, lenalidomide, pomalidomide (IMiDs) bind the CRBN CULT/thalidomide-binding
  domain [PMID:25108355 "These drugs directly bind Cereblon (CRBN)"; binding residues
  His378/His380/Trp386, Zn at 323/326/391/394 from UniProt FT]. Drug binding reprograms
  ("molecular glue") substrate specificity to recruit neosubstrates such as IKZF1 (Ikaros),
  IKZF3 (Aiolos), and CK1α (CSNK1A1) for ubiquitination/degradation
  [PMID:25108355; PMID:26131937 "lenalidomide induces the ubiquitination of casein kinase
  1A1 (CK1α) by the E3 ubiquitin ligase CUL4-RBX1-DDB1-CRBN"; PMID:26909574 "CK1α binding
  to CRL4(CRBN) is strictly dependent on the presence of an IMiD"].
- CK1α and IKZF1 recruitment is STRICTLY IMiD-dependent [PMID:26909574] — so neosubstrate
  recruitment is a pharmacological gain-of-function, not the endogenous function. Provenance
  for the molecular-glue mechanism is the IMiD literature; endogenous human substrate
  capture is sparse.
- The CK1α/CSNK1A1 IPI interaction in GOA (PMID:26131937, PMID:26909574) is the
  IMiD-induced (lenalidomide) drug-bound interaction.

## Wnt signaling

- PMID:34489457 reports that Wnt promotes CRBN-dependent degradation of CK1α (a negative
  regulator of Wnt) in an IMiD-INDEPENDENT manner; CRBN is required for physiological Wnt
  signaling, and modulation in zebrafish and Drosophila yields Wnt phenotypes
  [PMID:34489457 "CRBN is required for physiological Wnt signaling ... modulation of CRBN in
  zebrafish and Drosophila yields Wnt-driven phenotypes"]. This supports positive regulation
  of Wnt signaling pathway (IMP, source FlyBase). The IBA transfer to the same term derives
  from the same lineage of evidence (fly FBgn0037780). Reasonable to keep as a non-core
  regulatory process.

## Ion-channel / neuronal roles (endogenous, mostly non-core, largely from rodent orthologs)

- CRBN negatively regulates the large-conductance Ca2+-activated K+ (BK) channel via
  interaction with KCNT1, maintaining presynaptic glutamate release, memory and learning
  [UniProt FUNCTION; PMID:18414909; PMID:29530986]. The MRT2 p.R419X truncation dysregulates
  BK channel expression. These underlie the IEA-by-orthology terms transmembrane transporter
  binding (GO:0044325), negative regulation of monoatomic ion transmembrane transport
  (GO:0034766), and the behavior terms (locomotory exploration behavior GO:0035641) — all
  transferred from rat (Q56AP7) or mouse (Q8C7D2) orthologs. Endogenous but peripheral to
  the core E3-adaptor function; keep as non-core where literature supports, mark broad
  ortholog transfers as over-annotation where weak.

## Subcellular location

- Cytoplasm and nucleus [PMID:20223979, IDA]. Also peripheral membrane protein (by
  similarity), consistent with membrane/perinuclear IEA. Cytosol TAS from Reactome
  (R-HSA-9681169, "CRBN binds IMiDs").

## Disease

- Autosomal recessive intellectual developmental disorder 2 (MRT2); variants p.R419X
  (truncation) and C391R [PMID:15557513, PMID:28143899]. CRBN is highly expressed in brain.

## Interactome / protein binding annotations

- Multiple GO:0005515 "protein binding" IPI annotations come from high-throughput
  binary/affinity interactome screens: PMID:25416956 (HuRI/Rolland — RBPMS, PAK5),
  PMID:31515488 (Fragoza — PAK5), PMID:32296183 (HuRI/Luck — MISP), PMID:32814053 (Haenig —
  KLF11, COL26A1), PMID:35271311 (OpenCell — DDB1). These are generic "protein binding"
  with no specific informative MF; per curation guidance, bare protein binding should be
  marked as over-annotated. The DDB1 interaction (PMID:35271311; also PMID:20223979 IPI with
  DDB1 Q16531) is biologically meaningful (defines complex membership) but the GO term used
  is still uninformative "protein binding"; the meaningful content is captured by the
  Cul4-RING complex part_of annotations and the substrate-adaptor MF.

## Proposed MF term

- The current annotation set has NO molecular function term capturing CRBN's actual role.
  GO:1990756 "ubiquitin-like ligase-substrate adaptor activity" is the precise MF for the
  substrate-receptor function and is proposed as a new term.

## Caution / non-function

- Lon N-terminal domain present but NO protease activity (ATP-binding and catalytic domains
  absent) — UniProt CAUTION. Do not annotate peptidase activity.
