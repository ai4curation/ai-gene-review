# FraC (FJSC11DRAFT_2571 / G6FUM4) — research notes

Gene: **fraC** / ORFNames **FJSC11DRAFT_2571**
UniProt: **G6FUM4** (G6FUM4_9CYAN), Unreviewed (TrEMBL), 178 aa, MW ~20.4 kDa.
Organism: *Fischerella thermalis* JSC-11 (Nostocales; Hapalosiphonaceae; **Stigonematales**)
(NCBITaxon:741277).
Product name (UniProt SubName): "Filament integrity protein".
RefSeq: WP_009457250.1. AlphaFoldDB: G6FUM4.

## Summary

G6FUM4 is the *Fischerella thermalis* JSC-11 ortholog of the characterized *Nostoc*
(*Anabaena*) sp. PCC 7120 filament-integrity protein **FraC** (UniProt P46078; locus
alr2392). It is a small, polytopic integral cytoplasmic-(inner)-membrane protein that
belongs to the FraC-specific protein family restricted to filamentous,
heterocyst-forming cyanobacteria. By orthology to PCC 7120 FraC, it is inferred to be a
structural component of the septal-junction machinery at the intercellular septa,
required for filament integrity, correct localization of the septal protein SepJ, and
gated intercellular molecular exchange along the filament. No functional assays have been
performed on the *F. thermalis* protein itself; the functional assignments here are
transferred from the PCC 7120 ortholog with ISS evidence.

## Stigonematales significance

*Fischerella thermalis* belongs to the **Stigonematales** (family Hapalosiphonaceae), the
deepest-branching, morphologically most complex clade of the heterocyst-forming
cyanobacteria — characterized by true (multiseriate) branching filaments. The presence of
a complete, syntenic *fraC-fraD-fraE* operon and the wider septal-junction module in this
deep-branching lineage (all six components are reciprocal orthologs at 48–66% identity)
indicates that the FraC-based septal-junction apparatus is **ancestral to the
heterocyst-forming cyanobacteria as a whole**, not a *Nostoc/Anabaena*-specific
innovation. This is consistent with the SepN discovery paper's report of the module
across Nostocaceae, Oscillatoriales **and Stigonematales**.
[file:modules/septal_junction/RESULTS.md "*Fischerella thermalis* JSC-11 (taxon 741277)** — all six components reciprocal (48–66%"]

## Orthology evidence (basis for ISS transfer)

The ortholog call comes from a septal-junction module genome scan
(`file:modules/septal_junction/RESULTS.md`):

- **Sequence homology (RBH).** G6FUM4 is a reciprocal-best-hit ortholog of the PCC 7120
  FraC exemplar (P46078): forward best hit at **E ≈ 2.2e-45 with 48.0% amino-acid
  identity**, reciprocated back to P46078 — an unambiguous ortholog-level match.
- **Diagnostic protein family.** G6FUM4 is a member of the FraC-specific InterPro family
  **IPR054663** (Pfam **PF24301**, NCBIfam **NF045624** filament_FraC). This family is
  present in exactly one copy in every filamentous heterocyst-forming cyanobacterium
  scanned and absent from every unicellular cyanobacterium, i.e. it is diagnostic of the
  septal-junction apparatus. The InterPro/Pfam/NCBIfam assignments are recorded directly
  on the UniProt entry.
  [file:FISTH/FraC/FraC-uniprot.txt "InterPro; IPR054663; FraC."]
- **Operon synteny conserved.** The best hits for FraC/FraD/FraE carry consecutive
  accessions and consecutive loci in *F. thermalis* —
  **G6FUM4 (FraC, FJSC11DRAFT_2571) / G6FUM3 (FraD, FJSC11DRAFT_2570) / G6FUM2 (FraE,
  FJSC11DRAFT_2569)** — reconstituting the intact, syntenic *fraC-fraD-fraE* operon found
  at the PCC 7120 locus.
  [file:modules/septal_junction/RESULTS.md "FraD G6FUM3, FraC G6FUM4, FraE G6FUM2 (syntenic operon FJSC11DRAFT_2571/2570/2569)"]

Together, specific-family membership + high homology (RBH) + conserved operon synteny make
G6FUM4 a high-confidence FraC ortholog (the "gap-fill" candidate for curation).

## Function transferred from PCC 7120 FraC (P46078)

The following are established for the characterized PCC 7120 FraC ortholog and are
transferred to G6FUM4 by orthology (ISS); they are NOT direct assays on the
*F. thermalis* protein.

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

## Structural / biophysical features (G6FUM4)

- UniProt annotates G6FUM4 as a membrane protein with **4 predicted transmembrane
  helices** (Phobius: residues 12-34, 46-67, 87-110, 152-175) and no large soluble
  domain — the same four-TM polytopic architecture as PCC 7120 FraC.
  [file:FISTH/FraC/FraC-uniprot.txt "Transmembrane helix {ECO:0000256|SAM:Phobius}."]
- 178 aa; phenylalanine-rich, consistent with the PCC 7120 FraC description.

## Protein family

- **InterPro IPR054663 (FraC)**; **Pfam PF24301 (FraC)**; **NCBIfam NF045624
  (filament_FraC)**. [file:FISTH/FraC/FraC-uniprot.txt "Pfam; PF24301; FraC; 1."]
- The FraC family is restricted to multicellular, filamentous, heterocyst-forming
  cyanobacteria (Nostocales, including the deep-branching Stigonematales), consistent with
  a dedicated role in the cyanobacterial septal junction / filament-integrity machinery
  rather than a housekeeping function.
- Operon partner FraD (G6FUM3) belongs to the related filamentous cyanobacterial septal
  pore family.

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

- None. GOA is empty for G6FUM4 (0 annotations). Orthology-based proposals are entered as
  `action: NEW` with `evidence_type: ISS`.

## Caveats

- All functional assignments are ISS transfers from PCC 7120 FraC (P46078); no assays have
  been performed on the *F. thermalis* protein.
- Cached PMID:20487302 and PMID:7883709 are abstract-only; the PCC 7120 experimental
  results rest on the full-text assays (GFP localization, calcein-transfer FRAP, mutant
  phenotyping) reported by those primary papers.
