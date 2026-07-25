# TUSC3 (Q13454) — gene review notes

## Summary / core biology

TUSC3 (Tumor suppressor candidate 3; N33; also called Magnesium uptake/transporter TUSC3)
is an accessory subunit of the **STT3B-containing oligosaccharyltransferase (OST-B) complex**
in the endoplasmic reticulum membrane. It is a multi-pass membrane protein with a lumenal
**thioredoxin-like domain** bearing a redox-active CXXC motif (Cys99–Cys102). It is the
close paralog of MAGT1 and the metazoan orthologue of yeast Ost3/Ost6.

- UniProt authoritative function statement: "Acts as accessory component of the
  N-oligosaccharyl transferase (OST) complex ... Involved in N-glycosylation of
  STT3B-dependent substrates. Specifically required for the glycosylation of a subset of
  acceptor sites that are near cysteine residues; in this function seems to act redundantly
  with MAGT1. In its oxidized form proposed to form transient mixed disulfides with a
  glycoprotein substrate to facilitate access of STT3B to the unmodified acceptor site.
  Also has oxidoreductase-independent functions in the STT3B-containing OST complex possibly
  involving substrate recognition. Could indirectly play a role in Mg(2+) transport."
  [file:human/TUSC3/TUSC3-uniprot.txt]
- UniProt SUBUNIT: "Accessory component of the STT3B-containing form of the
  oligosaccharyltransferase (OST) complex. OST exists in two different complex forms which
  contain common core subunits RPN1, RPN2, OST48, OST4, DAD1 and TMEM258, either STT3A or
  STT3B as catalytic subunits ... The association of TUSC3 or MAGT1 with the STT3B-containing
  complex seems to be mutually exclusvice." [file:human/TUSC3/TUSC3-uniprot.txt]
- UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane; Multi-pass membrane protein."
  [file:human/TUSC3/TUSC3-uniprot.txt]
- UniProt PATHWAY: "Protein modification; protein glycosylation." [file:human/TUSC3/TUSC3-uniprot.txt]
- UniProt DOMAIN 59..187 "Thioredoxin"; DISULFID 99..102 "Redox-active"; MUTAGEN C99/C102 ->S
  "Reduces N-glycosylation of cysteine-proximal acceptor sites" [file:human/TUSC3/TUSC3-uniprot.txt]
- UniProt SIMILARITY: "Belongs to the OST3/OST6 family." [file:human/TUSC3/TUSC3-uniprot.txt]
- ComplexPortal: CPX-8738 "Oligosaccharyltransferase complex B, TUSC3 variant."
  [file:human/TUSC3/TUSC3-uniprot.txt]

## Mechanistic evidence — oxidoreductase activity (core MF)

PMID:25135935 (Cherepanova, Shrimal, Gilmore 2014, J Cell Biol; full text available) is the
key mechanistic paper. It studies MagT1 but directly tests TUSC3 by complementation:

- "MagT1, an ER-localized thioredoxin homologue, is a subunit of the STT3B isoform of the
  oligosaccharyltransferase (OST). The lumenally oriented active site CVVC motif in MagT1 is
  required for glycosylation of STT3B-dependent acceptor sites" [PMID:25135935]
- "The predominant form of MagT1 in vivo is oxidized, which is consistent with transient
  formation of mixed disulfides between MagT1 and a glycoprotein substrate to facilitate
  access of STT3B to unmodified acceptor sites." [PMID:25135935]
- "MagT1-depleted cells were fully complemented by expression of TUSC3, which is indicative
  of functional redundancy between MagT1 and TUSC3." [PMID:25135935]
- "Human MagT1 and TUSC3 are 73% identical in sequence in the mature region of the protein
  and have thioredoxin CXXC motifs..." [PMID:25135935]
- "Mutants that lacked both active site cysteine residues (e.g., MagT1 m1) were not able to
  fully restore glycosylation of pCatCΔ234-HA, which indicates that the CXXC motif is
  necessary for MagT1 and TUSC3 activity." [PMID:25135935]

The redox chemistry: the oxidized CXXC forms a mixed disulfide with a substrate free thiol;
the reduced form can react with a substrate disulfide — i.e. protein-disulfide
oxidoreductase / thioredoxin-type activity (GO:0015035 protein-disulfide reductase activity).

## Structural evidence

PMID:24685145 (Mohorko et al. 2014, Structure; abstract via PubMed) crystallized the lumenal
N33/Tusc3 thioredoxin domain (PDB 4M8G/4M90/4M91/4M92, res 44–194): "N33/Tusc3 possesses a
membrane-anchored N-terminal thioredoxin domain located in the ER lumen that may form
transient mixed disulfide complexes with OST substrates ... a defined peptide-binding groove
adjacent to the active site ... N33/Tusc3 increases glycosylation efficiency for a subset of
human glycoproteins by slowing glycoprotein folding." (According to PubMed;
[DOI](https://doi.org/10.1016/j.str.2014.02.013)). Cited in UniProt as the source of the
redox-active 99..102 disulfide and proposed function.

## OST complex membership

- PMID:31831667 (Ramírez, Kowal, Locher 2019, Science; abstract only): cryo-EM of human OST-A
  and OST-B. Establishes two distinct complexes; OST-B contains the MAGT1/TUSC3 subunit and
  is posttranslocational. ComplexPortal used this as the basis for TUSC3 OST-complex IPI/IDA
  and ER-membrane NAS annotations.
- PMID:15835887 (Shibatani et al. 2005, Biochemistry; abstract only): proteomic analysis of
  mammalian OST subcomplexes; this is the original HGNC-UCL IDA for OST complex membership
  (it identified DC2/KCP2; TUSC3 was among OST-associated proteins). Established mammalian OST
  heterogeneity.
- PMID:12887896 (Kelleher et al. 2003, Mol Cell; abstract only): identified that mammals
  express two Ost3p homologs (TUSC3/MAGT1) assembled into OST complexes with distinct
  enzymatic activity. UniProt reference [6] for OST identification + tissue specificity.
- PMID:26864433 (Cherepanova & Gilmore 2016, Sci Rep; full text): CRISPR MagT1/TUSC3 double
  knockout HEK293 cells. "The absence of both oxidoreductase subunits (MagT1(−/−) TUSC3(−/−)),
  or elimination of STT3B, causes a dramatic reduction in SHBG glycosylation." Directly tests
  the requirement of TUSC3+MagT1 for STT3B-dependent glycosylation in vivo. Basis of the IMP
  protein-N-linked-glycosylation annotation.

## Disease / process

- MRT7 (autosomal recessive intellectual disability): PMID:18455129 (Molinari et al. 2008)
  and PMID:18452889 (Garshasbi et al. 2008). Biallelic loss-of-function TUSC3 variants cause
  non-syndromic AR intellectual disability. UniProt DISEASE. Note the "cognition" IMP
  (GO:0050890) derives from the human-genetics disease phenotype (patients), not a direct
  molecular assay.
  - Molinari abstract: "a 1 bp insertion, c.787_788insC, resulting in a premature stop codon
    ... leading to mRNA decay ... fine regulation of OTase activity is essential for normal
    cognitive-function development" [PMID:18455129]. Note: patient fibroblasts showed normal
    bulk N-glycosylation — consistent with MAGT1 redundancy.

## Magnesium transport — treat carefully

PMID:19717468 (Zhou & Clapham 2009, PNAS; abstract only): yeast complementation screen
identified MagT1 and TUSC3 as mediators of Mg2+ influx; morpholino knockdown in zebrafish
causes developmental arrest rescued by excess Mg2+. This is the experimental basis for the
Mg2+-transport annotations (IMP GO:0015693; plasma-membrane NAS; Reactome TAS).

However, the field has largely reinterpreted this: the established, mechanistically supported
function of TUSC3 is the ER OST-B oxidoreductase. PMID:25135935 explicitly notes the
incompatibility: "Direct roles for MagT1 in both N-linked glycosylation and magnesium uptake
are incompatible unless one invokes both a dual localization (RER and plasma membrane) and a
dual activity (oxidoreductase and Mg+2 channel)" and shows MagT1/TUSC3 are ER-resident, not
plasma-membrane, with low cell-surface biotinylation. The Mg2+ effect is plausibly an
indirect consequence of hypoglycosylation of Mg2+ transporters/channels. UniProt hedges:
"Could indirectly play a role in Mg(2+) transport (PubMed:19717468)."

Curation decisions for Mg2+ annotations: the IMP (experimental, GO:0015693) is retained as
KEEP_AS_NON_CORE (do not remove experimental). The plasma-membrane locations (NAS/TAS) and
Mg-transporter-activity (IEA/TAS) are over-annotations of the true ER OST role — marked
MARK_AS_OVER_ANNOTATED (or REMOVE for the clearly-wrong ARBA IEA MF). IBA Mg2+-transmembrane
transport comes from a different PANTHER family (PTN000976171, note the WITH/FROM is
Drosophila FBgn0032015) and is over-annotated.

## Isoforms

Two isoforms (Q13454-1 displayed; Q13454-2 differs only at C-terminus DLDFE->FLIK, VSP_003776).
No isoform-specific function reported; annotations are not isoform-restricted.

## Curation plan (core functions)

- MF: GO:0015035 protein-disulfide reductase activity (thioredoxin-like oxidoreductase;
  CXXC/mixed-disulfide mechanism) — via PMID:25135935 + UniProt mutagenesis + PMID:24685145.
- MF (contributes_to): GO:0004579 dolichyl-diphosphooligosaccharide-protein glycotransferase
  activity — TUSC3 is an accessory subunit contributing to the OST-B catalytic reaction.
- CC/in_complex: GO:0160227 oligosaccharyltransferase complex B (OST-B; STT3B-specific).
- BP: GO:0006487 protein N-linked glycosylation.
- Location: GO:0005789 endoplasmic reticulum membrane.
