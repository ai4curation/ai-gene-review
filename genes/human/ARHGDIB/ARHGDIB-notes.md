# ARHGDIB (Rho GDP-dissociation inhibitor 2; Ly-GDI; D4-GDI; RhoGDI2) — review notes

**Deep research status:** automated falcon (Edison) deep research failed with an
authentication error on 2026-10-24, and no other provider key was available. No
`-deep-research-*.md` file exists for this gene. The notes below come from the cached
publications in `publications/`, the UniProt record (P52566), cached Reactome entries,
and targeted web searches used only to locate PMIDs (all cited papers were then cached
and read from `publications/`).

## Why this gene was reviewed

Flagged by rule FRR:0010 (projects/FUNCTION_REQUIREMENT_RULES.md): an IMP annotation
to GO:0003924 GTPase activity (assigned by CACAO, PMID:24554735). GO defines GTPase
activity as "Catalysis of the reaction: GTP + H2O = GDP + H+ + phosphate." ARHGDIB has
no P-loop GTPase domain; it is a Rho GDI family member (Pfam PF02115 Rho_GDI;
InterPro IPR000406; PANTHER PTHR10980:SF15).

## Identity and family

- UniProt P52566, 201 aa (initiator Met removed, N-acetylthreonine at 2).
- "Belongs to the Rho GDI family" (UniProt SIMILARITY). Paralogs: ARHGDIA (RhoGDI1,
  ubiquitous) and ARHGDIG (RhoGDI3, Q99819). [PMID:9113980 "We propose that RhoGDI be
  renamed RhoGDIα and GDID4 be renamed RhoGDIβ."]
- Hematopoietic expression: [PMID:8356058 "Ly-GDI is expressed only in hematopoietic
  tissues and predominantly in B- and T-lymphocyte cell lines"]; [PMID:7512369
  "confirm its preferential expression in hematopoietic tissues"].

## Molecular function: Rho GDP-dissociation inhibitor

- [PMID:8356058 "The full-length Ly-GDI cDNA encodes a 27-kDa protein which binds to
  RhoA and inhibits GDP dissociation from RhoA."]
- [PMID:7512369 "D4 has GDI activity against the CDC42Hs and rac I proteins, but binds
  to these proteins with a significantly weaker affinity than does the rho-subtype
  GDI."]
- Structure with Rac2 (PDB 1DS6): [PMID:10655614 "We have solved the crystal structure
  of a complex between the RhoGDI homolog LyGDI and GDP-bound Rac2"]; mechanism
  [PMID:10655614 "suggests a mechanism for the inhibition of guanine nucleotide
  dissociation that is based on the stabilization of the magnesium (Mg2+) ion in the
  nucleotide binding pocket."]; RhoGDIs [PMID:10655614 "decrease the rate of nucleotide
  dissociation and release Rho proteins such as RhoA, Rac and Cdc42 from membranes,
  forming tight complexes that shuttle between cytosol and membrane compartments."]
- Reactome lists ARHGDIB as a GDI for RHOA, RAC1, CDC42 and RHOG, and as binding RHOH
  (Reactome:R-HSA-9012835, R-HSA-9013147, R-HSA-9013158, R-HSA-9014456, R-HSA-9018754).

## Cellular effects / processes

- Overexpression disrupts stress fibres and focal contacts [PMID:8262133 "overexpression
  of both GDI proteins leads to rounding up of the cells and loss of stress fibers and
  focal contact sites"], consistent with inactivation of Rho proteins.
- Trophoblast migration [PMID:24554735 "Overexpression of RhoGDI2 in HTR-8/SVneo cells
  was associated with reduced RAC1-guanosine triphosphate (GTP) levels and inhibited
  cell migration."; "small interfering RNA-mediated downregulation of RhoGDI2 resulted
  in significantly increased RAC1-GTP levels"]. These are read-outs of reduced Rac1
  activation, not GTP hydrolysis by RhoGDI2.
- Cancer: [PMID:12438227 "These results indicate that RhoGDI2 is a metastasis
  suppressor gene, a marker of aggressive human cancer"].
- Knockout mice largely normal: [PMID:9307064 "These mice showed no striking
  abnormalities of lymphoid development or thymocyte selection."]; [PMID:9307064
  "Ly-GDI deficiency decreased IL-2 withdrawal apoptosis of lymph node cells"].
  Partial redundancy with RhoGDI1 is likely.
- Caspase-3 substrate in apoptosis: [PMID:11989976 "D4-GDI was cleaved to a 23 kDa
  fragment by daunorubicin treatment in HL-60 cells with kinetics that parallel the
  onset of apoptosis."]

## Localization

- Cytosol: UniProt "Cytoplasm, cytosol {ECO:0000269|PubMed:10802295}"; bovine
  neutrophil cytosol [PMID:10802295 "D4-GDI was the predominant GDI species in bovine
  neutrophil cytosol"].
- GFP-D4 is diffuse cytoplasmic, unlike RhoGDIγ: [PMID:9113980 "A similar construction
  with GFP tagged to the amino terminus of GDI/D4 or RhoGDI showed only a diffuse
  distribution in the cytoplasm without any of the perinuclear aggregates seen with
  RhoGDIγ"]. The cytoplasmic vesicle localisation in that paper is for RhoGDIγ
  (ARHGDIG), so the PINC TAS row "cytoplasmic vesicle" for ARHGDIB from PMID:9113980 is
  attached to the wrong paralog.
- PMID:16130169 (HUVEC 2-DE proteome) is a protein inventory; it does not establish
  cytoskeletal localisation.

## Decision on the flagged GO:0003924 row

The abstract of PMID:24554735 measures RAC1-GTP levels after RhoGDI2 over-expression or
knockdown; that is inhibition of Rac1 activation, the expected consequence of GDI
activity. Nothing reported is GTP hydrolysis catalysed by RhoGDI2, and the protein has
no GTPase fold. Action: MODIFY to GO:0005094 Rho GDP-dissociation inhibitor activity,
with a `source_defects` WRONG_TERM entry for CACAO (confidence PROBABLE because only the
abstract is cached).

## Open questions

- Physiological target selectivity of RhoGDI2 among RAC2/RAC1/RHOA/CDC42 in leukocytes.
- Role of Src-mediated tyrosine phosphorylation and caspase cleavage in GDI function.
