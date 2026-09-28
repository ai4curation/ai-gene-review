# KITLG (Stem Cell Factor / KIT ligand) — curation notes

UniProt: P21583 (SCF_HUMAN). Gene: KITLG (HGNC:6343). Synonyms: MGF, SCF, Steel factor,
c-Kit ligand, mast cell growth factor. Taxon: Homo sapiens (NCBITaxon:9606).

## Identity and molecular nature

KITLG is the single physiological ligand for the class-III receptor tyrosine kinase KIT
(CD117). It is not an enzyme or a transporter; it is a secreted/membrane four-helix-bundle
cytokine. It belongs to the SCF family (Pfam PF02404; InterPro IPR003452; 4-helix
cytokine-like core IPR009079). [UniProt P21583 SIMILARITY, DOMAIN]

The protein is synthesized as a type-I single-pass transmembrane precursor (signal 1-25,
extracellular 26-214, TM 215-237, cytoplasmic 238-273). A soluble form (sKITLG, residues
26-190) is produced by proteolytic cleavage of the extracellular domain. [UniProt P21583
FT/PTM: "A soluble form (sKITLG) is produced by proteolytic processing of isoform 1 in the
extracellular domain"]

Three isoforms exist by alternative splicing. Isoform 1 (SCF248) retains the protease-sensitive
exon-6-encoded region and is efficiently shed to give soluble SCF; isoform 2 (SCF220) lacks
that region (VSP_006022, del 174-202) and remains predominantly membrane-bound. [UniProt
P21583 ALTERNATIVE PRODUCTS]. Osteoblasts express the exon-6-omitted (membrane-associated)
form: [PMID:10049787 "Sequencing osteoblast SCF cDNAs showed that exon 6 was omitted. mRNAs
without exon 6 produce membrane-associated SCF isoforms in rodents"].

## Molecular function

SCF is biologically active as a non-covalent homodimer; the dimer binds two KIT ectodomains,
bringing two receptors together and triggering trans-autophosphorylation. This is established
at atomic resolution: [PMID:17662946 "The structures show that KIT dimerization is driven by
SCF binding whose sole role is to bring two KIT molecules together."]. The KITLG:KIT complex
is a heterotetramer (two KITLG + two KIT). [UniProt P21583 SUBUNIT: "Heterotetramer with KIT,
binding two KIT molecules; thereby mediates KIT dimerization and subsequent activation by
autophosphorylation"].

Core molecular activities:
- **stem cell factor receptor binding** (GO:0005173) — KIT-specific ligand/receptor binding.
  Functional expression of recombinant SCF was demonstrated by [PMID:2208279 "truncated forms
  of the rat and human proteins have been expressed in E. coli and mammalian cells and have
  been shown to possess biological activity"]. Structural basis: PMID:17662946.
- **cytokine activity** (GO:0005125) — SCF is a hematopoietic cytokine/growth factor that
  augments progenitor proliferation and synergizes with CSFs. [PMID:2208279 "SCF is able to
  augment the proliferation of both myeloid and lymphoid hematopoietic progenitors in bone
  marrow cultures. SCF exhibits potent synergistic activities in conjunction with
  colony-stimulating factors"].

Downstream (KIT-intrinsic, not KITLG-intrinsic): PI3K–AKT, RAS–RAF–MEK–ERK/MAPK, PLCγ,
JAK/STAT. [UniProt P21583 FUNCTION]. These are receptor-side activities; KITLG's job is
receptor engagement and dimerization.

## Localization

KITLG functions extracellularly, either tethered to the producing cell's plasma membrane
(juxtacrine) or as the shed soluble ectodomain (paracrine/secreted).
- Cell membrane / plasma membrane (single-pass type I membrane protein). [UniProt P21583
  SUBCELLULAR LOCATION]. Directly shown by immunofluorescence: [PMID:26522471 "Both FLAG-tagged
  wild-type and p.Leu104Val KITLG were detected in the cytoplasm and at the cell membrane, as
  well as in lamellipodia and filipodia"].
- Cytoplasm, lamellipodium, filopodium — same IDA source PMID:26522471 (quote above).
- Secreted (soluble KIT ligand). [UniProt P21583 SUBCELLULAR LOCATION: Soluble KIT ligand:
  Secreted]; extracellular region annotations via Reactome.
- A DCUA variant (p.His67_Cys68delinsArg) abolishes membrane localization: [PMID:26522471
  "the p.His67_Cys68delinsArg transmembrane isoform of KITLG is not detectable at the cell
  membrane"], and a WS2 variant (p.Leu104Val) reduces the soluble form: [PMID:26522471 "in
  culture media of transfected cells, the p.Leu104Val soluble isoform of KITLG was reduced"].

## Biological processes

- **Hematopoiesis / positive regulation of hematopoietic progenitor differentiation and
  proliferation**: SCF augments myeloid and lymphoid progenitor proliferation and synergizes
  with CSFs. [PMID:2208279 (quote above)]. Embryonic/fetal hemopoiesis annotation via
  PMID:21149635 (DFLAT). SCF is a core niche cytokine for KIT+ HSPCs. [deep-research falcon:
  "supports KIT-positive hematopoietic stem and progenitor-cell survival, retention,
  maintenance, proliferation, lineage differentiation"].
- **Positive regulation of cell population proliferation**: growth-factor activity on KIT+
  cells (mast cells, melanocytes, germ cells, hematopoietic progenitors). PMID:2208279;
  IBA (GO_REF:0000033); IDA PMID:9722506.
- **Male gonad development / gametogenesis**: KITL (KITLG) is a Sertoli-cell product in the
  human fetal testis whose expression rises through the second trimester. [PMID:17848411
  "Transcripts encoding Sertoli (KITL, FGF9, SOX9, FSHR, WT1) ... cell-specific products
  increased per testis through the second trimester"]. This is an IEP (expression pattern)
  annotation — supports a developmental role, appropriate as non-core.
- **Melanogenesis / pigmentation**: KITLG variation underlies the SHEP7 pigmentation locus,
  familial progressive hyperpigmentation (FPHH), and Waardenburg syndrome 2F. A gain-of-function
  FPHH variant (p.Asn36Ser) increases melanin content. [UniProt P21583 DISEASE/VARIANT;
  PMID:19375057]. (No GOA melanogenesis process term in this set.)
- **Ovarian follicle development** (IEA, ortholog transfer) — KIT/KITL signaling supports
  ovarian follicle/oocyte survival; consistent with reproductive role but electronic only.

## Disease

FPHH (MIM:145250), congenital unilateral/asymmetric deafness DCUA (MIM:616697), Waardenburg
syndrome 2F (MIM:619947); pigmentation variation locus SHEP7; blond-hair enhancer SNP
rs12821256. [UniProt P21583 DISEASE, POLYMORPHISM]. The deafness/pigmentation phenotypes reflect
the requirement for KIT/KITLG signaling in melanocyte-lineage cells, including inner-ear
melanocytes.

## Annotation-review reasoning summary

- Two `GO:0005173 stem cell factor receptor binding` rows (IEA GO_REF:0000120; TAS PMID:2208279):
  both ACCEPT — this is the defining molecular function.
- `GO:0005125 cytokine activity` (IEA): ACCEPT — SCF is a bona fide cytokine.
- `GO:0005515 protein binding` (IPI, with KIT P10721, PMID:17662946): MODIFY → the paper and
  the interactant identify this specifically as KIT/stem cell factor receptor binding
  (GO:0005173); per curation policy, replace uninformative "protein binding" with the specific
  MF rather than MARK_AS_OVER_ANNOTATED.
- Localization IDA rows from PMID:26522471 (cytoplasm, plasma membrane, lamellipodium,
  filopodium): ACCEPT (directly observed). The single-pass membrane and secreted forms are
  the functional locations; cytoplasm/lamellipodium/filopodium ACCEPT but non-core.
- `GO:0005576 extracellular region` (many TAS Reactome duplicates + one IEA): ACCEPT the location
  (soluble/secreted SCF is genuinely extracellular). Keep as one representative accepted;
  duplicates are fine per guidelines.
- `GO:0005886 plasma membrane` (IBA is_active_in; IDA; IEA; NAS; TAS): ACCEPT — membrane-bound
  SCF signals from the plasma membrane. IBA node PTN002611905.
- `GO:0005856 cytoskeleton` (IEA subcell mapping): KEEP_AS_NON_CORE / MODIFY — this is derived
  from the cytoplasm/cytoskeleton subcellular-location keyword; weakly supported, not a
  functional site. Marked non-core.
- `GO:0016020 membrane` (IEA): ACCEPT but redundant/general parent of plasma membrane.
- Process terms: positive regulation of cell proliferation (IBA/IDA/IEA), positive regulation
  of hematopoietic progenitor cell differentiation (TAS), embryonic hemopoiesis (IDA),
  signal transduction (IEA), male gonad development (IEP), ovarian follicle development (IEA),
  developmental process involved in reproduction (IEA), animal organ development (IEA),
  cell adhesion (IEA InterPro).
- `GO:0007155 cell adhesion` (IEA from InterPro IPR003452): membrane-bound SCF does contribute
  to cell-cell adhesion/retention of KIT+ cells, but this InterPro2GO mapping is broad; KEEP as
  non-core / mark over-annotated is borderline. Kept as non-core with caveat.
- `GO:0048513 animal organ development` and `GO:0003006 developmental process involved in
  reproduction` (ARBA IEA): very general ARBA electronic terms; KEEP_AS_NON_CORE (too general
  to be core but not wrong).

No NEW terms proposed: the melanogenesis/pigmentation role, while strong in the disease data,
is a downstream consequence of KIT activation in melanocytes — the entity performing melanin
synthesis is the melanocyte's tyrosinase machinery, not KITLG. KITLG's participation is via
its receptor-binding/cytokine activity, already captured. Adding a melanogenesis process term
to the ligand would fail the participation test (KITLG does not catalyze or structurally
contribute to melanin synthesis). Comparator: other KIT-pathway ligands/growth factors are not
annotated to melanin biosynthetic process on the ligand side.
