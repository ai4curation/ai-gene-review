# GPAA1 (GAA1) review notes

UniProtKB: O43292; HGNC:4446; human; 621 aa; MANE NM_003801.4.
Deep research: falcon OUT OF CREDITS (HTTP 402) so no `-deep-research-falcon.md`. Review grounded in
`GPAA1-uniprot.txt`, seeded `GPAA1-goa.tsv`, and cached `publications/PMID_*.md` (all 17 cited PMIDs cached).

## Core biology (verified from cited literature + UniProt)

GPAA1 is a non-catalytic (accessory) subunit of the eukaryotic **GPI-anchor transamidase (GPI-T / GPI-TA)
complex**, an ER-membrane heteropentamer of PIGK, GPAA1, PIGT, PIGS, PIGU
[PMID:35551457 "an equimolar heteropentameric assembly"; PMID:34576938 "GPI-TA consists of five subunits:
PIGK, GPAA1, PIGT, PIGS, and PIGU"]. GPI-T removes the C-terminal GPI-attachment signal peptide of
precursor proteins in the ER and replaces it with a pre-assembled GPI anchor via a transamidation reaction
[PMID:11483512 "GPI transamidase mediates GPI anchoring in the endoplasmic reticulum, by replacing a
protein's C-terminal GPI attachment signal peptide with a pre-assembled GPI"].

- **Catalytic cysteine-protease chemistry resides in PIGK (Gpi8p)**, not GPAA1
  [PMID:10793132 "Gpi8p is a catalytic component that cleaves the GPI attachment signal peptide";
  PMID:34576938 "PIGK is the catalytic subunit of GPI-TA"].
- **GPAA1 role**: M28-family peptidase-like fold; proposed to mediate the second half-reaction — formation of
  the amide bond between the substrate ω-site carbonyl (acyl-enzyme intermediate on PIGK Cys) and the bridging
  ethanolamine-phosphate (EtNP) of GPI [PMID:34576938 "This reaction may be mediated by GPAA1, which is
  structurally similar to M28-type aminopeptidase"; PMID:34576938 "GPAA1 is proposed to catalyze the
  formation of an amide bond between the ω-site and the bridging EtNP on the GPI complete precursor"].
  GPAA1 Asp250 is functionally important (D250A reduces GPI-T activity)
  [PMID:34576938 "The D250A construct reduced GPI-TA activity without changing the protein stability"].
- **GPI (lipid substrate) binding / positioning is a GPAA1 function.** Structures with liganded GPI-T show
  GPAA1 residues coordinate the three EtNP arms of GPI: EtNP1–His354(+Mg2+), EtNP2–Gln355/Ser51,
  EtNP3–Ser51/Asn53 [PMID:37684232]. Truncating GPAA1's C-terminal TM span or mutating a conserved Pro in it
  abolishes GPI co-IP without disrupting assembly [PMID:14660601 "cannot co-immunoprecipitate GPI"].
  UniProt annotates GPAA1 GPI-anchor BINDING at residues 49/51/354/355/356 (ChEBI:144080) from PMID:37684232.
- **Complex assembly / stability**: PIG-T stabilises GAA1+GPI8 expression [PMID:11483512 "PIG-T maintains the
  complex by stabilizing the expression of GAA1 and GPI8"]; GAA1's large luminal loop mediates subunit
  interaction [PMID:12052837].
- **Localization**: ER membrane, multi-pass; GAA1 is passively retained in the ER by a signalless mechanism
  [PMID:15713669 "Gaa1 is passively retained in the ER by a signalless mechanism"; UniProt SUBCELL
  Endoplasmic reticulum membrane, Multi-pass].
- **Disease**: biallelic GPAA1 variants cause GPI biosynthesis defect 15 (GPIBD15; MIM:617810) — developmental
  delay, hypotonia, early-onset seizures, cerebellar atrophy, osteopenia; patient cells show reduced
  cell-surface GPI-anchored proteins [PMID:29100095].

## Annotation-action rationale

- **attachment of GPI anchor to protein (GO:0016255)** and **GPI anchored protein biosynthesis (GO:0180046)**
  and **GPI-anchor transamidase complex (GO:0042765)** and **GPI anchor binding (GO:0034235)** — well
  supported by IDA/IMP/EXP + IBA; ACCEPT (core).
- **GPI anchor biosynthetic process (GO:0006506)** IEA(UniPathway) — parent BP, consistent; ACCEPT.
- **endoplasmic reticulum membrane (GO:0005789)** (EXP/NAS/TAS/IEA) and **endoplasmic reticulum (GO:0005783)**
  (IDA/HPA) — ACCEPT (ER membrane is core location; ER is the parent).
- **membrane (GO:0016020)** IEA/HDA — true but uninformative parent of ER membrane; MARK_AS_OVER_ANNOTATED.
- **protein binding (GO:0005515)** IPI ×8 — all resolve to complex partners (PIGK Q92643, PIGT Q969N2,
  MOXD1 Q6UVY6) or HT interactome studies; uninformative bare term per curation policy;
  MARK_AS_OVER_ANNOTATED (do NOT REMOVE per policy). The real MF is captured by GPI anchor binding +
  transamidase-complex membership.
- **protein retention in ER lumen (GO:0006621)** NAS PMID:12052837 — the cited paper describes GAA1's own ER
  retention (a signalless mechanism), not GPAA1 causing retention of other lumenal proteins; the term is a
  mis-fit (GPAA1 is not a KDEL-receptor-like retention factor and the abstract does not support retaining
  other proteins in the ER lumen). NAS + demonstrably poor term/paper fit → MARK_AS_OVER_ANNOTATED.

## core_functions MF chosen

GOA carries NO transamidase catalytic-activity MF term for GPAA1 (catalysis attributed to PIGK). The only MF
in GOA is GO:0005515 (bare protein binding, dropped) and **GO:0034235 GPI anchor binding** (IDA, PMID:37684232;
IMP contributes_to, PMID:14660601). Per instructions, use the exact GOA MF present → **GO:0034235 GPI anchor
binding** as the core molecular_function. Do NOT invent an independent transamidase catalytic activity.
</content>
