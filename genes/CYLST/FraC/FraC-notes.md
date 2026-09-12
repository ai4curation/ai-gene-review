# FraC (Cylst_1330 / K9WTD1) — research notes

Gene: **fraC** / OrderedLocusName **Cylst_1330**
UniProt: **K9WTD1** (K9WTD1_9NOST), UNREVIEWED (TrEMBL), 179 aa, MW ~20.7 kDa.
Organism: *Cylindrospermum stagnale* PCC 7417 (NCBITaxon:56107; Nostocales, Nostocaceae).
Product name (UniProt): "Filament integrity protein" (ProtNLM).

## Summary

FraC of *Cylindrospermum stagnale* PCC 7417 is a small, polytopic integral
cytoplasmic-(inner)-membrane protein predicted to have four transmembrane helices. It is a
high-confidence ortholog of the experimentally characterized *Nostoc*/*Anabaena* sp. PCC
7120 filament-integrity protein FraC (UniProt P46078). In PCC 7120, FraC is a septal
protein that helps build and maintain the intercellular septa joining adjacent cells of the
filament; it is required for filament integrity and for diazotrophic (N2-fixing) growth,
localizes to the intercellular septa where the septal-junction (SJ) machinery is assembled,
and is required for correct localization of the septal protein SepJ and for gated
intercellular molecular exchange. These functions are transferred to K9WTD1 by orthology
(evidence code ISS); no assays have been performed on the *C. stagnale* protein itself.

## Orthology evidence (source of the ISS transfer)

- **Reciprocal best hit (RBH)** between *C. stagnale* Cylst_1330 (K9WTD1) and PCC 7120 FraC
  (P46078): forward BLAST E = **8.5e-61**, **56.2% identity**; the pairing is reciprocal
  (best-hit in both directions). This is a genome-wide RBH, the standard operational
  criterion for orthology. (Genome-wide reciprocal-best-hit scan, `modules/septal_junction`.)
- **FraC-specific protein family:** K9WTD1 carries **InterPro IPR054663 (FraC)**, **Pfam
  PF24301 (FraC)**, and **NCBIfam NF045624 (filament_FraC)** — a family diagnostic of, and
  restricted to, multicellular filamentous heterocyst-forming cyanobacteria (Nostocales).
  [file:CYLST/FraC/FraC-uniprot.txt "InterPro; IPR054663; FraC."]
- **Conserved fraC-fraD-fraE operon synteny:** in *C. stagnale* the locus order is
  **Cylst_1330 (fraC) – Cylst_1329 (fraD) – Cylst_1328 (fraE)**, mirroring the PCC 7120
  **fraC(alr2392)-fraD(alr2393)-fraE(alr2394)** operon. Conserved gene neighborhood across
  species independently corroborates the orthology assignment.

Together, specific family membership + RBH homology + conserved operon synteny give a
high-confidence ortholog call, justifying ISS transfer of the PCC 7120 FraC core functions.

## Function transferred from the characterized PCC 7120 ortholog (P46078)

- fraC is the first gene of the constitutively expressed fraC-fraD-fraE operon.
  [PMID:20487302 "Whereas fraC (alr2392) was constitutively expressed as an operon together with two downstream genes, alr2393 (fraD) and alr2394 (fraE)"]
- FraC (with FraD) localizes to the intercellular septa.
  [PMID:20487302 "As shown with GFP fusions, FraC and FraD are also located at the intercellular septa."]
- FraC, together with SepJ and FraD, shapes the architecture and function of the
  intercellular septa.
  [PMID:20487302 "at least three different proteins, SepJ, FraC and FraD, influence the architecture and function of the"]
- fraC (and fraD) mutants mislocalize SepJ and are impaired in intercellular transfer of the
  fluorescent tracer calcein — a role in septal-junction-mediated intercellular molecular
  exchange. [PMID:20487302 "The fraC and fraD mutants showed an impaired localization of SepJ at the intercellular septa and were hampered in the intercellular transfer of the fluorescent probe calcein."]
- FraC was discovered as the gene mutated in the PCC 7120 short-filament fragmentation
  strain 129; a unique 179-aa phenylalanine-rich protein.
  [PMID:7883709 "The affected gene in strain 129, fraC, was cloned by complementation and characterized. It encodes a unique 179-amino-acid protein rich in phenylalanine."]
- Insertional inactivation reproduces the phenotype, confirming causality.
  [PMID:7883709 "Insertional inactivation of the chromosomal copy of fraC results in a phenotype identical to that of strain 129"]
- FraC's role is in cell-junction/filament integrity rather than differentiation per se.
  [PMID:7883709 "Thus, FraC is required for the integrity of cell junctions in general but is apparently not directly involved in normal differentiation and nitrogen fixation."]

## Structural / biophysical features (K9WTD1)

- UniProt (K9WTD1) annotates FraC as an integral membrane protein with **4 predicted
  (Phobius) transmembrane helices** (residues 12-34, 46-67, 93-115, 152-175) and no large
  soluble domain — the same four-TM polytopic architecture as PCC 7120 FraC.
  [file:CYLST/FraC/FraC-uniprot.txt "Transmembrane helix {ECO:0000256|SAM:Phobius}."]

## Functional interpretation for GO review (all ISS by orthology to P46078)

- **Molecular function:** non-catalytic, structural integral-membrane component of the
  septal (intercellular-junction) machinery; best captured by **structural molecule activity
  (GO:0005198)**. Avoid the uninformative "protein binding".
- **Biological process:** required for gated intercellular molecular exchange; **cell-cell
  signaling (GO:0007267)** captures the calcein-transfer / intercellular-communication role.
- **Cellular component:** integral to the cytoplasmic (inner) membrane, localized to the
  intercellular septa; **plasma membrane (GO:0005886)**.

## Existing GOA annotation

- **GOA is empty** for K9WTD1 (0 annotations). The three GO terms above are therefore added
  as de-novo, orthology-based proposals (action: NEW, evidence_type: ISS).

## Caveats

- No functional assays exist for the *C. stagnale* protein; all function is inferred by
  orthology to PCC 7120 FraC. Cached PMID:20487302 and PMID:7883709 are abstract-only; the
  underlying experimental annotations rest on the full-text assays reported by those primary
  papers.
