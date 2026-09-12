# acn1 (SPBC3H7.05c / O74380) — curation notes

Fission yeast (*Schizosaccharomyces pombe* 972 / ATCC 24843). UniProt entry name **YNV5_SCHPO**.
PomBase standard name **acn1**; systematic name **SPBC3H7.05c**; UniProt accession **O74380**.

## Summary / bottom line

`acn1` is an **understudied ("conserved unknown") gene** encoding a polytopic
integral membrane protein of the **membrane-bound O-acyltransferase (MBOAT)
superfamily**. PomBase characterisation status is *conserved unknown* and UniProt
PE level is *4: Predicted*. There is **no dedicated functional/biochemical study**
of acn1; essentially all annotations are either sequence/domain-based inference or
high-throughput screen phenotypes. The confident statements one can make are about
its **domain architecture and localization**; its **specific molecular substrate,
biological process, and physiological role remain unknown**.

## Identity and provenance

- PomBase gene page (API `www.pombase.org/api/v1/dataset/latest/data/gene/SPBC3H7.05c`):
  - `name: acn1`, `product: "membrane bound O-Acyl transferase (MBOAT) family"`,
    `characterisation_status: conserved unknown`, `deletion_viability: viable`,
    `uniprot_identifier: O74380`.
  - `name_descriptions: ["ACetylation of Hy8Z (Nitrogen Signaling Factor (NSF)"]` —
    i.e. the symbol *acn1* was coined from a proposed "ACetylation of Nsf"
    hypothesis; this is a name derivation, **not** experimentally established
    function.
  - Taxonomic distribution flags: `conserved in eukaryotes`, `conserved in fungi`,
    `no apparent S. cerevisiae ortholog` (PBO:0000055).

## Domain / sequence analysis (from UniProt O74380 record, inline)

- 357 aa; 9 predicted TM helices (TRANSMEM 13-33, 44-64, 72-92, 148-168, 181-201,
  203-223, 266-286, 293-313, 327-347) — a **multi-pass integral membrane protein**.
- InterPro **IPR032805 (Wax_synthase_dom)** / Pfam **PF13813 (MBOAT_2)**. This is the
  wax-synthase branch of the MBOAT superfamily (distinct Pfam clan member from the
  "core" MBOAT PF03062). Pfam PF13813 = "Membrane bound O-acyl transferase family";
  associated activity is O-acyltransferase (verified via InterPro API PF13813).
- MBOAT enzymes carry a conserved catalytic His in a hydrophobic stretch and an
  invariant upstream Asn/His. In acn1 the His residues fall at 65/66, 250, 287, 326;
  H287 sits in the conserved **"...ALFHDFAY..."** block (the LYHDFAF fingerprint that
  UniProt's OMA record captured), and H250 in "...WSRDWH...". Presence of these
  His/Asn residues is **consistent with** a retained catalytic capacity but does not
  by itself prove activity or identify a substrate. [inline sequence inspection]

## Existing GO annotations (from acn1-goa.tsv; 4 GOA lines)

1. **GO:0031966 mitochondrial membrane** — IEA, GO_REF:0000044 (UniProtKB-SubCell
   mapping SL-0171). Derived from the UniProt subcellular-location statement
   "Mitochondrion membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}".
   ECO:0000305 = curator inference (not direct assay). The primary evidence for a
   mitochondrial localization is the ORFeome GFP screen [PMID:16823372].
2. **GO:0005575 cellular_component** — ND, GO_REF:0000015 (root "no data" placeholder).
3. **GO:0008150 biological_process** — ND, GO_REF:0000015 (root "no data" placeholder).
4. **GO:0016747 acyltransferase activity, transferring groups other than amino-acyl
   groups** — ISS, GO_REF:0000024, `WITH/FROM: PomBase:SPAC24H6.01c`. Transferred by
   curator judgment of sequence similarity from **gup1** (SPAC24H6.01c, Q09758), an
   MBOAT (product "membrane bound O-acyltransferase, MBOAT Gup1"; annotated to
   GO:0006506 GPI anchor biosynthetic process). NOTE: gup1 uses Pfam PF03062
   (MBOAT_fam) whereas acn1 uses PF13813 (Wax_synthase_dom) — related superfamily,
   **different subfamily**; the ISS supports family-level acyltransferase activity but
   NOT gup1's specific GPI-anchor function.

Also present in the UniProt DR block (not in GOA TSV): GO:0005739 mitochondrion
HDA:PomBase (from the ORFeome localization dataset), and the now-**obsolete**
GO:0008374 O-acyltransferase (superseded by GO:0016747). Verified GO:0008374 is
obsolete via QuickGO.

## Localization evidence

- **Mitochondrion / mitochondrial membrane**: ORFeome-wide GFP localization study
  [PMID:16823372 "ORFeome cloning and global analysis of protein localization in the
  fission yeast Schizosaccharomyces pombe"] underlies the HDA mitochondrion call and
  the UniProt SubCell statement. This is a genome-scale screen (moderate confidence
  for any single protein); a mitochondrial *membrane* MBOAT is somewhat atypical (most
  characterized MBOATs are ER/Golgi/plasma-membrane), so localization deserves a
  caveat but is the only localization datum available.

## Phenotype data (all high-throughput or overexpression; PomBase FYPO)

- **PMID:37787768** (Bähler lab broad phenomics / machine-learning profiling of fission
  yeast proteins) contributes ~20 FYPO annotations for acn1delta, e.g. multidrug
  resistance/sensitivity (resistance to diamide, KCl, terbinafine, tert-butyl
  hydroperoxide; sensitivity to cadmium, rapamycin, torin1, tunicamycin, brefeldin A,
  vanadate, X-rays), and nitrogen/carbon-source growth changes (FYPO:0009091 decreased
  growth on lysine+proline N source; FYPO:0009076 increased growth on sucrose). These
  are **pleiotropic screen hits**, not evidence of a specific molecular function.
- **PMID:23695302** (fission-yeast TF overexpression analysis) contributes low-throughput
  **overexpression** phenotypes (FYPO:0001406 increased septum thickness; multiseptate /
  mono-septate binucleate-anucleate cells). Overexpression phenotypes are weak evidence
  for endogenous function.
- **PMID:40424131** (Formation of giant ER sheets by pentadecanoic acid causes
  lipotoxicity in fission yeast, PNAS 2025) contributes FYPO:0010042 **"normal growth on
  pentadecanoic acid"** for acn1delta — i.e. acn1 was screened in a lipotoxicity study
  and its deletion did **not** alter C15:0 sensitivity (a *negative* result). acn1 is
  not discussed in that paper's body text.

## KNOWN vs NOT-known

KNOWN (well-supported):
- It is a **polytopic integral membrane protein** (9 TM helices; UniProt/DeepTMHMM).
- It belongs to the **MBOAT superfamily, wax-synthase (PF13813/IPR032805) branch**.
- It **localizes to mitochondria / mitochondrial membrane** (ORFeome GFP screen; single
  moderate-confidence line of evidence).
- Deletion is **viable** with **no gross morphology defect** (FYPO:0002177), consistent
  with a non-essential gene.
- It has **no apparent S. cerevisiae ortholog** but is conserved across fungi/eukaryotes.

NOT known (knowledge gaps):
- **Molecular function / catalytic activity**: whether acn1 is a *catalytically active*
  acyltransferase, and if so its **acyl-donor and acceptor substrates**, are unknown. The
  MF annotation is ISS-from-paralog at the general "acyltransferase, non-amino-acyl"
  level only.
- **Biological process**: unknown. The "acn1 = ACetylation of Nsf" name is a hypothesis,
  not established. No BP annotation with experimental support exists.
- **Physiological role / pathway**: unknown. Phenotypes are broad pleiotropic
  screen/overexpression hits that do not converge on a mechanism.
- **Localization detail**: sub-mitochondrial location and topology unverified beyond a
  single genome-scale GFP dataset; a mitochondrial-membrane MBOAT is atypical.
- **Direct interactors / regulation**: none experimentally established for function.

## Candidate MF for core_functions

- **GO:0016747** (acyltransferase activity, transferring groups other than amino-acyl
  groups) is the most specific *defensible* MF: it is the current (non-obsolete) term,
  it is family/domain-appropriate for an MBOAT, and it is what GOA already carries via
  ISS. Anything more specific (wax-ester synthase, DGAT, GPI-anchor acyltransferase,
  protein-serine O-palmitoleoyltransferase, etc.) would be an over-annotation given no
  substrate data. core_functions should carry at most this one MF with an explicit
  low-confidence/uncertainty note, plus the mitochondrial-membrane location; the primary
  deliverable is the knowledge_gaps section.

## Falcon deep research (acn1-deep-research-falcon.md, Edison, 26 citations)

The falcon report (completed 2026-07-06, 1659 s) independently reached the same
conclusion and adds useful comparative context. Key points (all secondary/inferential,
about the MBOAT family, NOT direct acn1 data):
- No primary research article has characterized acn1/SPBC3H7.05c function, activity, or
  role; all inference is domain/homology-based. (converges with my analysis.)
- MBOAT superfamily = integral-membrane acyltransferases with conserved catalytic His
  (in a TM stretch) + upstream Asn; three functional subgroups (sterol/DAG acylation
  e.g. ACAT/DGAT1; protein/peptide acylation e.g. PORCN/HHAT/GOAT; lyso-phospholipid
  re-acylation e.g. LPCAT/MBOAT7). The **wax-synthase (WS) branch** acylates fatty
  alcohols with fatty-acyl-CoA to make wax esters, and DGAT1-type members make TAG.
- Predicted acn1 activity: **acyl-CoA-dependent acyltransferase**, most consistent with
  wax-ester-synthase and/or DGAT1-type chemistry — but substrate is unknown.
- S. pombe neutral-lipid context: TAG synthesis is by dga1 (DGAT2 fold, structurally
  UNRELATED to MBOAT) and plh1 (PDAT); sterol esterification by Are1/Are2 homologs
  (Zhang et al. 2003, JBC). acn1 (MBOAT/DGAT1-type) is therefore a **distinct enzyme
  class** and, if catalytically active, would be an additional/accessory acyltransferase.
- Predicted localization by MBOAT analogy: **endoplasmic reticulum** (DGAT1/ACAT are
  ER-resident). NOTE this CONFLICTS with the only experimental localization datum for
  acn1 (mitochondrion, ORFeome GFP screen PMID:16823372). This discrepancy is itself a
  knowledge gap — the family prior says ER, the single S. pombe screen says mitochondrion.
- CAVEAT on the report: it treats "Wax_synthase_dom (IPR032805)" and "MBOAT_2 (PF13813)"
  as two domains; they are the SAME domain (InterPro IPR032805 is the InterPro entry for
  Pfam PF13813). Do not double-count. The falcon DOI citations are family reviews, not
  acn1-specific; I will NOT cite them as supporting acn1 function directly.
