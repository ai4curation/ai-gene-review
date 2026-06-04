# UMAD1 notes

## Local evidence reviewed

- `just fetch-gene human UMAD1` created the review stub, UniProt record, and GOA table. The UniProt entry is `UMAD1_HUMAN`, accession `C9J7I0`, a 137 aa protein named "UBAP1-MVB12-associated (UMA)-domain containing protein 1" with synonyms `RPA3-AS1` and `RPA3OS`. UniProt does not provide a FUNCTION comment or GO cross-references for UMAD1, but records a predicted UMA domain at residues 86-134 and classifies the protein in InterPro `IPR053292`/`IPR023340` and PANTHER `PTHR36291` [UniProt:C9J7I0, "DR   InterPro; IPR053292; UBAP1-MVB12_assoc_domain."; UniProt:C9J7I0, "DR   PROSITE; PS51497; UMA; 1."].
- `just deep-research-falcon human UMAD1` was attempted and timed out after 600 seconds, producing no Falcon report. The review therefore relies on the local UniProt, GOA, cached publication, and PN-context evidence below.
- GOA contains only two raw rows, both collapsed to `GO:0005515 protein binding` from IntAct/PMID:32296183, with `WITH/FROM` partners `P07101-3` and `Q9H0R8`. UniProt lists the corresponding interactors as TH isoform 3 and GABARAPL1 [UniProt:C9J7I0, "CC       C9J7I0; Q9H0R8: GABARAPL1; NbExp=3; IntAct=EBI-10989060, EBI-746969;"; UniProt:C9J7I0, "CC       C9J7I0; P07101-3: TH; NbExp=3; IntAct=EBI-10989060, EBI-12001016;"].
- PMID:32296183 is a systematic HuRI binary interactome map. It generated a large reference dataset using yeast two-hybrid screens and retesting, not a focused UMAD1 functional study [PMID:32296183, "To map the reference interactome, we performed nine screens of Space III, followed by pairwise verification by quadruplicate retesting and sequence confirmation."; PMID:32296183, "The dataset, versioned HI-III-20 (Human Interactome obtained from screening Space III, published in 2020), contains 52,569 verified PPIs involving 8,275 proteins"].
- PMID:32424346 places UMAD1 in the set of possible human UMA-containing ESCRT-I fourth-subunit family members, but the structural/biophysical work in that paper centers on a VPS37B-MVB12A ESCRT-I headpiece and explicitly notes that some theoretical UMA-containing complexes may not form [PMID:32424346, "Human ESCRT-I is a heterotetrameric complex consisting of a 1:1:1:1 complex of (a) TSG101, (b) VPS28, (c) one of VPS37A, B, C, or D, and (d) one of the MVB12A, MVB12B, UBAP1, UBA1L, or UMAD1"; PMID:32424346, "While it has been reported that some of these theoretical complexes do not actually form39"].

## Curation synthesis

UMAD1 should be treated as a poorly characterized UMA-domain protein rather than as an experimentally established ESCRT-I subunit in this review. The name and domain architecture make ESCRT-I membership plausible, and the proteostasis network entry is useful search context, but the local evidence does not show UMAD1 incorporation into an ESCRT-I complex, endosomal cargo sorting, membrane fission, autophagy, or viral budding.

The existing `GO:0005515 protein binding` annotation is supported as a broad interaction-screen observation, but it is uninformative as a molecular function and should be marked as over-annotated. The interaction partners in the local records, TH isoform 3 and GABARAPL1, do not by themselves establish a coherent UMAD1 core function or a proteostasis pathway role.

No core GO function is assigned in this review. Adding ESCRT-I complex membership, MVB sorting, ubiquitin binding, phospholipid binding, membrane fission, or macroautophagy terms would overstate the available evidence.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording said the local evidence reviewed here does not establish a specific ESCRT-I complex, endosomal sorting, autophagy, membrane fission, or viral budding function for UMAD1. That is a curation observation rather than standalone gene biology.
