# OLAH (Q9NV23) — review notes

## Identity

- UniProt: Q9NV23, `SAST_HUMAN`. RecName: "S-acyl fatty acid synthase thioesterase, medium chain" with EC=3.1.2.14 [file:human/OLAH/OLAH-uniprot.txt, "RecName: Full=S-acyl fatty acid synthase thioesterase, medium chain" / "EC=3.1.2.14 {ECO:0000269|PubMed:26663084}"].
- AltNames capture the many historical names: **Oleoyl-ACP hydrolase**, **Thioesterase 2 (TE2)**, **Thioesterase II**, "Augmented in rheumatoid arthritis 1 (AURA1)", "Thioesterase domain-containing protein 1 (THEDC1)" [file:human/OLAH/OLAH-uniprot.txt, "AltName: Full=Oleoyl-ACP hydrolase" / "AltName: Full=Thioesterase 2 {ECO:0000303|PubMed:26663084}" / "AltName: Full=Thioesterase II"].
- HGNC:25625; synonym THEDC1 [file:human/OLAH/OLAH-uniprot.txt, "GN   Name=OLAH {ECO:0000312|HGNC:HGNC:25625}; Synonyms=THEDC1;"].
- Gene on chromosome 10; 265 aa; belongs to the thioesterase family [file:human/OLAH/OLAH-uniprot.txt, "SIMILARITY: Belongs to the thioesterase family. {ECO:0000305}."].

## Core function

OLAH is a cytosolic type II thioesterase (TE II / TE2) that works in trans with the type I
fatty acid synthase (FASN). By hydrolyzing the thioester bond linking the growing acyl chain to
the acyl-carrier-protein (ACP) domain of FASN, it releases free fatty acids prematurely,
terminating chain elongation early and shifting the product spectrum toward shorter (medium-chain)
fatty acids.

- FUNCTION: "Contributes to the release of free fatty acids from fatty acid synthase (FASN). Has broad substrate specificity, giving rise to a range of free fatty acids with chain lengths between 10 and 16 carbon atoms (C10 - C16)." [file:human/OLAH/OLAH-uniprot.txt; ECO:0000269|PubMed:26663084].
- Primary catalytic activity (experimentally established, EC 3.1.2.14): (9Z)-octadecenoyl-[ACP] + H2O = (9Z)-octadecenoate + holo-[ACP] + H+ (i.e., oleoyl-[ACP] hydrolase) [file:human/OLAH/OLAH-uniprot.txt, "Reaction=(9Z)-octadecenoyl-[ACP] + H2O ..." with "EC=3.1.2.14; Evidence={ECO:0000269|PubMed:26663084}"].
- The crystal structure paper (PMID:26663084) directly demonstrates the ACP-based physiological
  mechanism: human TE2 prefers an engineered acyl-ACP substrate over acyl-CoA mimetics and releases
  short-chain fatty acids from full-length FASN during turnover [PMID:26663084 abstract, "In contrast,
  TE2 prefers an engineered human acyl-ACP substrate and readily releases short chain fatty acids from
  full-length FASN during turnover."]. The Ser-101–His-237–Asp-212 catalytic triad sits in an
  α/β-hydrolase core with a novel capping domain [PMID:26663084 abstract, "the capping domain had
  collapsed onto the active site containing the Ser-101-His-237-Asp-212 catalytic triad."].
- Interacts (via C-terminus) with FASN [file:human/OLAH/OLAH-uniprot.txt, "SUBUNIT: Interacts (via C-terminus) with FASN."; inferred by homology ECO:0000250|UniProtKB:P08635].
- Active-site residue Ser-101 established experimentally [file:human/OLAH/OLAH-uniprot.txt, "ACT_SITE        101" /evidence="ECO:0000305|PubMed:26663084"].

## Localization

- Cytoplasm, cytosol [file:human/OLAH/OLAH-uniprot.txt, "SUBCELLULAR LOCATION: Cytoplasm, cytosol"; inferred by homology ECO:0000250|UniProtKB:P08635].
  This is consistent with the cytosolic FASN it partners with.

## Biological role / tissue specificity

- The rat/mammalian TE II is the classic thioesterase II of the lactating mammary gland that
  redirects FASN toward medium-chain fatty acids for milk. The human enzyme "generates a broad lipid
  distribution within milk" [PMID:26663084 abstract, "TE2 has been implicated in breast cancer and
  generates a broad lipid distribution within milk."].
- Detected in both lactating and non-lactating breast epithelium at the protein level (historical
  "thioesterase II marker enzyme for breast epithelial cells") [file:human/OLAH/OLAH-uniprot.txt,
  "TISSUE SPECIFICITY: Detected both in lactating and non-lactating breast epithelium (at protein
  level) (PubMed:6589427)." — PMID:6589427 not in local cache].
- Isoform 2 is up-regulated in bone-marrow-derived mononuclear cells of rheumatoid-arthritis patients
  (hence the AURA1 name) [file:human/OLAH/OLAH-uniprot.txt, "Isoform 2 is up-regulated in bone marrow-
  derived mononuclear cells of rheumatoid arthritis patients (PubMed:17082220)." — PMID:17082220 not
  in local cache]. Isoform 2 (VSP_040022) replaces the C-terminus, so it likely lacks full catalytic
  activity; the up-regulation is a disease-association marker, not evidence of enzymatic function.

## GO annotation review summary (9 GOA annotations)

Core (ACCEPT):
- GO:0016297 fatty acyl-[ACP] hydrolase activity — IDA (PMID:26663084) — the experimentally
  established, physiologically relevant MF. ACCEPT (core). The redundant IEA copy of the same term
  also ACCEPT (correct core MF, not an over-annotation).
- GO:0051792 medium-chain fatty acid biosynthetic process — IDA (PMID:26663084) — core BP (early
  chain termination yields medium-chain FAs). ACCEPT (core). Redundant IEA copy also ACCEPT.
- GO:0005829 cytosol — ISS and IEA — correct core CC. ACCEPT (keep one core; both are correct).

Non-core / over-annotation:
- GO:0008610 lipid biosynthetic process — IBA — correct but very general parent of the specific BP;
  KEEP_AS_NON_CORE (redundant with GO:0051792).
- GO:0052815 medium-chain fatty acyl-CoA hydrolase activity — IEA (RHEA) — acyl-CoA hydrolysis is a
  substrate-mimetic side activity inferred by homology from rat P08635; the human enzyme physiologically
  acts on acyl-ACP, and PMID:26663084 shows it PREFERS acyl-ACP over acyl-CoA. MARK_AS_OVER_ANNOTATED.
- GO:0052816 long-chain fatty acyl-CoA hydrolase activity — IEA (RHEA) — same reasoning;
  additionally long-chain (C13-C22) exceeds the C10-C16 physiological product range.
  MARK_AS_OVER_ANNOTATED.

## Provenance notes

- PMID:26663084 cached as abstract only (`full_text_available: false`); all supporting_text quotes
  taken verbatim from the cached abstract.
- PMID:6589427 and PMID:17082220 (tissue specificity) are NOT in the local publications cache; those
  facts are cited only from the UniProt CC lines (verbatim file: quotes).
