# eryCII (A4F7P2, SACE_0725) — review notes

Part of the **BGC exemplar curation project** (`projects/BGC.md`). MIBiG BGC0000055
(*Saccharopolyspora erythraea*, erythromycin PKS). GenBank CAM00066.1 → UniProt
**A4F7P2** (ERYC2_SACEN), gene *eryCII* / SACE_0725. Also relevant to
`projects/PSEUDOENZYMES.md`.

## Function — a P450 PSEUDOENZYME that activates a glycosyltransferase

EryCII is a **cytochrome-P450-family homologue that has lost catalytic competence**
and instead serves as the **activating partner of the desosaminyl transferase
EryCIII** in erythromycin biosynthesis.

- UniProt A4F7P2 CAUTION: "Although related to the cytochrome P450 family, lacks the
  heme-binding sites." (ECO:0000305) — i.e. it cannot bind heme and cannot perform
  P450 monooxygenase chemistry.
- UniProt FUNCTION: "Involved in the erythromycin biosynthesis pathway. Acts by
  forming a complex and stabilizing the desosaminyl transferase EryCIII."
  (ECO:0000269|PubMed:22056329); SUBUNIT: "Heterotetramer composed of EryCII and EryCIII."
- Structure (PDB 2YJN): "EryCIII, in concert with its partner EryCII, attaches a
  nucleotide-activated sugar to the macrolide scaffold... a heterotetramer...
  EryCII stabilizes EryCIII and also functions as an allosteric activator of the GT."
  [PMID:22056329]

## Annotation issues — domain-based over-annotation of a pseudoenzyme

All four GOA molecular-function terms are IEA from the P450 sequence signature and are
**incorrect for this catalytically dead homologue**:

- GO:0004497 monooxygenase activity → REMOVE
- GO:0005506 iron ion binding → REMOVE
- GO:0016705 oxidoreductase activity (paired donors, O2) → REMOVE
- GO:0020037 heme binding → REMOVE (UniProt: "lacks the heme-binding sites")

Accurate roles to assert instead: **GO:0008047 enzyme activator activity** (allosteric
activator of EryCIII), **GO:1901115 erythromycin biosynthetic process** (BP),
**GO:0032991 protein-containing complex** (EryCII-EryCIII heterotetramer).

## Predicted-complex evidence (BGC project)

Moriwaki et al. (bioRxiv 2025.10.26.684697) predict the EryCII-EryCIII interaction
(BGC0000055; CAM00066.1/CAM00067.1) at **ipTM 0.92**, matching PDB 2YJN (hetero 4-mer).

## References
- PMID:22056329 — Moncrieffe et al. 2012, J Mol Biol (EryCIII·EryCII structure, PDB
  2YJN; EryCII stabilizes and allosterically activates EryCIII). VERIFIED.
- UniProt A4F7P2 (CAUTION: lacks heme-binding sites).
