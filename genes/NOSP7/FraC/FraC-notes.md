# FraC (Npun_R1227 / B2IXC9) — research notes

Gene: **fraC** / OrderedLocusName **Npun_R1227**
UniProt: **B2IXC9** (B2IXC9_NOSP7), Unreviewed (TrEMBL), 181 aa, MW ~21 kDa.
Organism: *Nostoc punctiforme* (strain ATCC 29133 / PCC 73102) (NCBITaxon:63737).
Product name (UniProt SubName): "Filament integrity protein".
RefSeq: WP_012407972.1. AlphaFoldDB: B2IXC9.

## Summary

B2IXC9 is the *Nostoc punctiforme* PCC 73102 ortholog of the characterized *Nostoc*
(*Anabaena*) sp. PCC 7120 filament-integrity protein **FraC** (UniProt P46078; locus
alr2392). It is a small, polytopic integral cytoplasmic-(inner)-membrane protein that
belongs to the FraC-specific protein family restricted to filamentous,
heterocyst-forming cyanobacteria. By orthology to PCC 7120 FraC, it is inferred to be a
structural component of the septal-junction machinery at the intercellular septa,
required for filament integrity, correct localization of the septal protein SepJ, and
gated intercellular molecular exchange along the filament. No functional assays have been
performed on the *N. punctiforme* protein itself; the functional assignments here are
transferred from the PCC 7120 ortholog with ISS evidence.

## Orthology evidence (basis for ISS transfer)

The ortholog call comes from a septal-junction module genome scan
(`file:modules/septal_junction/RESULTS.md`):

- **Sequence homology.** phmmer of the PCC 7120 FraC exemplar (P46078) against the
  *N. punctiforme* reference proteome returns B2IXC9 as the single best hit at
  **E ≈ 4e-64 with ~60% amino-acid identity** — a strong, unambiguous ortholog-level
  match. [file:modules/septal_junction/RESULTS.md "P46078 (100%) | **B2IXC9** (4e-64, 60%)"]
- **Diagnostic protein family.** B2IXC9 is a member of the FraC-specific InterPro family
  **IPR054663** (Pfam **PF24301**, NCBIfam **NF045624** filament_FraC). This family is
  present in exactly one copy in every filamentous heterocyst-forming cyanobacterium
  scanned and absent from every unicellular cyanobacterium, i.e. it is diagnostic of the
  septal-junction apparatus. [file:modules/septal_junction/RESULTS.md "FraD and FraC families are **diagnostic** (present in every heterocyst-former, absent from every unicellular genome)."]
  The InterPro/Pfam/NCBIfam assignments are recorded directly on the UniProt entry.
  [file:NOSP7/FraC/FraC-uniprot.txt "InterPro; IPR054663; FraC."]
- **Operon synteny conserved.** The best hits for FraC/FraD/FraE carry consecutive
  accessions in *N. punctiforme* — **B2IXC9 (FraC) / B2IXC8 (FraD) / B2IXC7 (FraE)** —
  reconstituting the intact, syntenic *fraC-fraD-fraE* operon found at the PCC 7120 locus.
  [file:modules/septal_junction/RESULTS.md "*N. punctiforme* **B2IXC9 / B2IXC8 / B2IXC7**"]

Together, specific-family membership + high homology + conserved operon synteny make
B2IXC9 a high-confidence FraC ortholog (the "gap-fill" candidate for curation).

## Function transferred from PCC 7120 FraC (P46078)

The following are established for the characterized PCC 7120 FraC ortholog and are
transferred to B2IXC9 by orthology (ISS); they are NOT direct assays on the
*N. punctiforme* protein.

- **Operon / expression.** *fraC* is the first gene of the constitutively expressed
  *fraC-fraD-fraE* operon in PCC 7120.
  [PMID:20487302 "Whereas fraC (alr2392) was constitutively expressed as an operon together with two downstream genes, alr2393 (fraD) and alr2394 (fraE)"]
- **Septal localization.** GFP fusions place FraC (and FraD) at the intercellular septa.
  [PMID:20487302 "As shown with GFP fusions, FraC and FraD are also located at the intercellular septa."]
- **Cell-cell communication / SepJ localization.** *fraC* mutants mislocalize the septal
  protein SepJ and are impaired in intercellular transfer of the fluorescent tracer
  calcein.
  [PMID:20487302 "The fraC and fraD mutants showed an impaired localization of SepJ at the intercellular septa and were hampered in the intercellular transfer of the fluorescent probe calcein."]
- **Structural/architectural role.** FraC, with SepJ and FraD, influences the
  architecture and function of the intercellular septa.
  [PMID:20487302 "at least three different proteins, SepJ, FraC and FraD, influence the architecture and function of the"]
- **Filament / cell-junction integrity (distinct from differentiation).** FraC is
  required for the integrity of cell junctions in general but is not directly involved in
  differentiation or nitrogen fixation.
  [PMID:7883709 "Thus, FraC is required for the integrity of cell junctions in general but is apparently not directly involved in normal differentiation and nitrogen fixation."]
- **Discovery.** *fraC* was cloned as the gene mutated in the short-filament fragmentation
  mutant strain 129; it encodes a phenylalanine-rich protein (179 aa in PCC 7120).
  [PMID:7883709 "The affected gene in strain 129, fraC, was cloned by complementation and characterized. It encodes a unique 179-amino-acid protein rich in phenylalanine."]

## Structural / biophysical features (B2IXC9)

- UniProt annotates B2IXC9 as a membrane protein with **4 predicted transmembrane
  helices** (Phobius: residues 12-34, 46-66, 96-120, 157-178) and no large soluble
  domain — the same four-TM polytopic architecture as PCC 7120 FraC.
  [file:NOSP7/FraC/FraC-uniprot.txt "Transmembrane helix {ECO:0000256|SAM:Phobius}."]
- 181 aa; phenylalanine-rich, consistent with the PCC 7120 FraC description.

## Protein family

- **InterPro IPR054663 (FraC)**; **Pfam PF24301 (FraC)**; **NCBIfam NF045624
  (filament_FraC)**. [file:NOSP7/FraC/FraC-uniprot.txt "Pfam; PF24301; FraC; 1."]
- The FraC family is restricted to multicellular, filamentous, heterocyst-forming
  cyanobacteria (Nostocales), consistent with a dedicated role in the cyanobacterial
  septal junction / filament-integrity machinery rather than a housekeeping function.
- Operon partner FraD (B2IXC8) belongs to the related filamentous cyanobacterial septal
  pore family (TCDB 1.V.1.1.1).

## Functional interpretation for GO review (all ISS by orthology to P46078)

- **Molecular function:** structural, non-catalytic integral-membrane component of the
  septal-junction machinery — **structural molecule activity (GO:0005198)**. Avoid the
  uninformative "protein binding".
- **Biological process:** required for gated intercellular molecular exchange along the
  filament — **cell-cell signaling (GO:0007267)** captures the calcein-transfer /
  intercellular-communication role. No dedicated GO term exists for the cyanobacterial
  "septal junction" or "filament integrity".
- **Cellular component:** integral to the cytoplasmic (inner) membrane, localized to the
  intercellular septa — **plasma membrane (GO:0005886)**.

## Existing GOA annotation

- None. GOA is empty for B2IXC9 (0 annotations). Orthology-based proposals are entered as
  `action: NEW` with `evidence_type: ISS`.

## Caveats

- All functional assignments are ISS transfers from PCC 7120 FraC (P46078); no assays have
  been performed on the *N. punctiforme* protein.
- Cached PMID:20487302 and PMID:7883709 are abstract-only; the PCC 7120 experimental
  results rest on the full-text assays (GFP localization, calcein-transfer FRAP, mutant
  phenotyping) reported by those primary papers.
</content>
</invoke>
