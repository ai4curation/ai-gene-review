# kitlga (Danio rerio) — curation notes

UniProt: Q56JH6 (Kit ligand a). ZFIN: ZDB-GENE-070424-1. Synonyms: kitla.
Taxon: NCBITaxon:7955. 272 aa, single-pass type I membrane protein, SCF family,
four-helix cytokine-like core (IPR009079), SCF domain (IPR003452 / PF02404).

## 1. Identity and teleost-duplication context

Zebrafish retained two co-orthologs of mammalian KITLG/Kitl (stem cell factor, SCF)
following the teleost whole-genome duplication: **kitlga** (this gene, historical alias
*kitla*, on chromosome 25) and **kitlgb** (*kitlb*, on chromosome 4). The receptors
duplicated in parallel (kita, kitb).

- Phylogeny places both zebrafish genes as co-orthologs of tetrapod Kitl, with the
  duplication occurring in the teleost lineage: [PMID:17257055 "We conclude that zebrafish kitla and kitlb are co-orthologous to mammalian Kitl"] and [PMID:17257055 "it appears that the two zebrafish copies arose from a duplication event in the teleost lineage after the divergence from the tetrapod lineage but before the teleost radiation"].
- The paralogs diverged strongly in sequence (kitla ~29% identical / 43% similar to
  mouse Kitl) and in splice-form structure: kitla retained exon 6 (nine exons matching
  the nine murine exons), whereas kitlb lost the exon-6-homologous sequence
  [PMID:17257055 "kitla contains nine exons, each aligning with the nine murine exons ... kitlb has retained only eight exons ... suggesting that kitlb is missing sequence homologous to mouse exon 6"].
- **Subfunctionalization / pigmentation-role partitioning:** kitlga is the paralog that
  retains the ancestral melanocyte (pigment) role; kitlgb does NOT substitute for it.
  MO knockdown of kitla, but not kitlb, phenocopies the kita-null allele
  [PMID:17257055 "kitla morphants, but not kitlb morphants, phenocopy the null allele of kita, with defects for both melanocyte migration and survival"], and only kitla interacts
  genetically with a sensitized kita allele [PMID:17257055 "kitla morpholino, but not kitlb morpholino, interacts genetically with a sensitized allele of kita, confirming that kitla is the functional ligand to kita"]. kitlb is not required for embryonic
  melanocyte migration or survival [PMID:17257055 "MO knockdowns of kitlb indicate that it is not required for either embryonic melanocyte migration or survival"].
- The deep-research report adds (from non-cached primary literature) that the ligand
  systems are receptor-specialized (Kitlga→Kita, Kitlgb→Kitb) and that embryonic
  HSC-specification is instead assigned mainly to Kitlgb–Kitb, so mammalian-KITLG or
  kitlgb roles should not be transferred wholesale to Q56JH6 (deep-research falcon,
  hultman2007 / yao2013 / mahony2018).

## 2. Core molecular function — Kita ligand (SCF-family cytokine)

kitlga is a **signaling cytokine ligand, not an enzyme/transporter/structural protein**.
Its defining molecular function is to bind and activate the Kita receptor tyrosine
kinase (the zebrafish KIT-a ortholog), i.e. stem cell factor receptor binding /
cytokine/growth-factor activity.

- Functional-ligand conclusion: [PMID:17257055 "we conclude that kitla is the functional kita ligand in zebrafish embryonic melanocyte development and that kitla promotes all of the kita-dependent functions in embryonic melanocyte development"].
- Growth-factor (mitogenic) activity in vivo: kitla overexpression causes
  kita-dependent hyperpigmentation through increased melanocyte number and size
  [PMID:17257055 "overexpression of kitla results in a hyperpigmented embryo with an increase in the number and size of melanocytes"] and this requires kita
  [PMID:17257055 "This hyperpigmentation is dependent on kita function"].
- Domain/family support: UniProt assigns the SCF family and four-helix cytokine-like
  core (IPR009079, IPR003452/PF02404); RecName "Kit ligand", AltNames "Stem cell
  factor", "Mast cell growth factor", "c-Kit ligand" (kitlga-uniprot.txt).
- The signaling output is the conserved KIT–RAS/MAPK cascade (Reactome R-DRE entries for
  Signaling by SCF-KIT, RAF/MAP kinase cascade, PI3K/AKT; kitlga-uniprot.txt DR lines).

## 3. Localization

Synthesized as a membrane-associated (single-pass type I) ligand that can be released as
a soluble extracellular form; operative compartments are the producing-cell surface
(juxtacrine) and the extracellular/paracrine space.
- UniProt SUBCELLULAR LOCATION: Cell membrane; Secreted; also cytoskeleton and cell
  projection (filopodium/lamellipodium) keywords, all ARBA by-similarity
  (kitlga-uniprot.txt). The cytoskeleton and filopodium/lamellipodium calls are
  by-similarity keyword transfers (the same by-similarity keywords underlie the human
  KITLG annotations, where the projection localizations were directly observed for the
  transmembrane form by IF, PMID:26522471); for zebrafish they are electronic and
  non-core.

## 4. Biological processes (zebrafish-specific in vivo phenotypes)

- **Melanocyte / pigment-pattern development (GO:0030318):** the strongest and most
  specific experimental role. Expression along the medial melanocyte-migration route
  (18–30 hpf) then in skin (4–5 dpf) [PMID:17257055 "kitla mRNA is expressed in the trunk adjacent to the notochord in the middle of each somite during stages of melanocyte migration and later expressed in the skin, when the receptor is required for melanocyte survival"]. Loss of function (morpholino) and gain of function
  establish requirement for both migration and survival. A second, independent line:
  the *sparse like (slk)* mutant is kitlga, lacking larval and metamorphic melanophores
  [PMID:23364329 "We show that the sparse like (slk) mutant lacks larval and metamorphic melanophores and identify kit ligand a (kitlga) as the underlying gene. Our data suggest that kitlga is required for the establishment or survival of embryonic MPs"]. The Kelsh 1996
  mutagenesis screen [PMID:9007256] isolated the pigmentation mutant (the ZFIN genotype
  ZDB-GENO-120316-63 later mapped to kitlga) among chromatophore-number/differentiation
  genes; this abstract does not name kitlga (screen paper, abstract-only cache), so the
  annotation rests on the ZFIN curator's genotype assignment.
- **Positive regulation of cell population proliferation (GO:0008284):** SCF is a
  mitogen for KIT+ cells; in zebrafish, kitlga drives increased melanocyte number
  (hyperpigmentation) and, per deep research, cooperates with Epo to expand erythroid
  progenitors (Oltova 2020 preprint, not cached).
- Note on qualifiers: the GO:0030318 rows use `acts_upstream_of_or_within`, i.e. kitlga
  acts upstream of / within melanocyte differentiation (as the ligand), not that it is
  itself a melanocyte differentiating — consistent with treating it as a non-core
  developmental/lineage outcome relative to the core ligand activity.

## 5. Curation decisions summary

Core (ACCEPT): GO:0005173 stem cell factor receptor binding (IEA); GO:0005886 plasma
membrane (IBA is_active_in, and IEA); GO:0008284 positive regulation of cell population
proliferation (IBA); GO:0005576 extracellular region (IEA); GO:0016020 membrane (IEA,
general parent).

Non-core (KEEP_AS_NON_CORE): GO:0005856 cytoskeleton (by-similarity keyword);
GO:0007155 cell adhesion (InterPro2GO, broad/secondary); GO:0030027 lamellipodium and
GO:0030175 filopodium (by-similarity keyword, non-core projection localizations); all
five GO:0030318 melanocyte differentiation rows (well-supported developmental/lineage
phenotype, but downstream of the core ligand activity).

No annotations warranted REMOVE (no generic `protein binding` GO:0005515 row is present;
no contradicted or demonstrably wrong terms). No NEW existing_annotation added — the
core molecular function (stem cell factor receptor binding) is already present, and
cytokine/growth-factor activity is captured in `core_functions` rather than manufactured
as a new GOA-style row. Comparator/participation tests were not triggered because no new
process term is proposed.
