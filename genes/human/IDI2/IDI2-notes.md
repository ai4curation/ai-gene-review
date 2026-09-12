# IDI2 (human) review notes

UniProt: Q9BXS1 (IDI2_HUMAN), 227 aa, EC 5.3.3.2. HGNC:23487. Gene on chromosome 10.
Reviewed here against `IDI2-uniprot.txt`, `IDI2-goa.tsv`, the cached primary paper
`publications/PMID_17202134.md` (abstract-only, `full_text_available: false`), the two
IntAct interactome papers, and `reactome/R-HSA-191382.md`. No deep-research file used or
created.

## Core biology (grounded)

- **Molecular function**: Isopentenyl-diphosphate delta-isomerase (type-2 isozyme,
  paralog of IDI1). Catalyzes the reversible 1,3-allylic rearrangement
  IPP <=> DMAPP.
  - UniProt FUNCTION: [file:human/IDI2/IDI2-uniprot.txt "Catalyzes the 1,3-allylic rearrangement of the homoallylic ... isopentenyl (IPP) to its highly electrophilic allylic isomer, dimethylallyl diphosphate (DMAPP)"]
  - Rhea/EC: [file:human/IDI2/IDI2-uniprot.txt "Reaction=isopentenyl diphosphate = dimethylallyl diphosphate;" ... "EC=5.3.3.2 {ECO:0000269|PubMed:17202134}"]
  - Direct assay: [PMID:17202134 "IDI2 has the ability to catalyze the isomerization of [(14)C]IPP to [(14)C]DMAPP."]; kinetics [PMID:17202134 "K(IPP)(m) value of 22.8 microm IPP"], pH optimum 8.0.
  - Functional complementation: [PMID:17202134 "Expression constructs of human IDI2 in Saccharomyces cerevisiae can complement isomerase function in an idi1-deficient yeast strain."]
- **Cofactor**: Mg2+ (binds 1 per subunit). [file:human/IDI2/IDI2-uniprot.txt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420"]
- **Pathway**: Isoprenoid biosynthesis; DMAPP biosynthesis; DMAPP from IPP: step 1/1.
  [file:human/IDI2/IDI2-uniprot.txt "PATHWAY: Isoprenoid biosynthesis; dimethylallyl diphosphate biosynthesis; dimethylallyl diphosphate from isopentenyl diphosphate: step 1/1."] Also mapped to UniPathway UPA00059/UER00104.
- **Location**: Peroxisome (experimental), with C-terminal PTS1-type microbody-targeting
  motif (residues 225..227).
  - [file:human/IDI2/IDI2-uniprot.txt "SUBCELLULAR LOCATION: Peroxisome {ECO:0000269|PubMed:17202134}."]
  - [file:human/IDI2/IDI2-uniprot.txt "MOTIF           225..227" ... "Microbody targeting signal"]
  - [PMID:17202134 "Both isozymes, IDI1 and IDI2 are localized to the peroxisome by a PTS1-dependent pathway."]
  - Reactome models the isomerase step as cytosolic and notes peroxisomal function is
    unclear: [file:human/IDI2/... reactome/R-HSA-191382.md "IPP isomerase may also be located in human peroxisomes but its function there is not clear."] The GOA cytosol annotation (TAS, Reactome:R-HSA-191382) is retained as non-core.
- **Tissue specificity**: Skeletal-muscle-specific in humans (distinguishes IDI2 from
  ubiquitous IDI1). [file:human/IDI2/IDI2-uniprot.txt "TISSUE SPECIFICITY: Muscle-specific expression."]; HPA "Tissue enriched (skeletal)".
- **Regulation**: Independent of IDI1, possibly via PPARalpha. [PMID:17202134 "IDI2 is regulated independently from IDI1, by a mechanism that may involve PPARalpha."]
- **Fold/family**: Nudix hydrolase domain (49..199); belongs to the IPP isomerase type 1
  family. PDB 2PNY (1.81 A). Active-site His86 and Glu148 (by similarity).

## Annotation review summary

15 GOA annotations reviewed.

- **ACCEPT (8)**: GO:0004452 x3 (IBA, IEA, IDA -- core MF); GO:0005777 peroxisome x3
  (IBA is_active_in, IEA located_in, IDA located_in -- core CC, experimentally supported);
  GO:0008299 isoprenoid biosynthetic process (IEA and IDA -- core BP); GO:0050992 DMAPP
  biosynthetic process (IEA/UniPathway -- precise core BP).
- **KEEP_AS_NON_CORE (3)**: GO:0009240 IPP biosynthetic process (IBA -- imprecise family
  term, real process is DMAPP biosynthesis); GO:0046490 IPP metabolic process (IDA --
  general parent of the isomerase step); GO:0005829 cytosol (TAS/Reactome -- genuine
  alternate location).
- **MODIFY (1)**: GO:0016860 intramolecular oxidoreductase activity (IEA/ARBA). Verified
  in local go.db that GO:0004452 is a descendant (GO:0004452 -> GO:0016863 "intramolecular
  oxidoreductase activity, transposing C=C bonds" -> GO:0016860 -> GO:0016853 isomerase
  activity). Correct but over-general; propose replacement with GO:0004452. (Not REMOVE --
  it is a true ancestor, just imprecise.)
- **MARK_AS_OVER_ANNOTATED (2)**: GO:0005515 protein binding x2 (IPI, PMID:28514442 BioPlex
  AP-MS; PMID:32296183 HuRI Y2H). Both support the same high-throughput binary interaction
  IDI2-LDB1 (Q86U70-2) recorded in the UniProt INTERACTION block. Bare "protein binding" is
  uninformative and no functional role is established. Per policy, IPI protein binding is
  marked over-annotated, not removed.

## Notes / caveats

- The two interactome papers (PMID:28514442, PMID:32296183) are cached with full text but
  do not name IDI2/Q9BXS1/LDB1 in the cached markdown (interaction data live in their
  supplementary tables). The interaction itself is corroborated by the UniProt INTERACTION
  record, so `supporting_text` for those annotations is anchored to the UniProt file rather
  than to the paper bodies.
- Evidence base for IDI2 is thinner than IDI1: the single functional primary paper is
  PMID:17202134. Where GOA process terms are broader than the demonstrated reaction, they
  are kept as non-core rather than accepted as core.

## Core functions (synthesis)

- MF: isopentenyl-diphosphate delta-isomerase activity (GO:0004452)
- BP: dimethylallyl diphosphate biosynthetic process (GO:0050992); isoprenoid biosynthetic
  process (GO:0008299)
- CC: peroxisome (GO:0005777); cytosol (GO:0005829)
- Substrates: isopentenyl diphosphate (CHEBI:128769); prenyl diphosphate (CHEBI:57623)
