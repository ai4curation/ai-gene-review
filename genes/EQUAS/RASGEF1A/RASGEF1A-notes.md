# RASGEF1A (donkey, A0A9L0J8J4) notes

DONKEY40 cohort review (ProtNLM2 evaluation). Unreviewed TrEMBL entry from the Ensembl donkey annotation, 516 aa; the donkey record carries no curated CC comments.

## Identity and sequence
- Domains: N-terminal Ras-GEF (REM) 76-205 and catalytic Ras-GEF 249-496 [file:EQUAS/RASGEF1A/RASGEF1A-uniprot.txt "FT   DOMAIN          249..496"]; PANTHER PTHR23113:SF172 (RAS-GEF DOMAIN-CONTAINING FAMILY MEMBER 1A).
- 96.25% identity to human Q8N9B8 across 480 paired residues; donkey has a 36-residue N-terminal extension; both GEF domains complete [file:EQUAS/RASGEF1A/RASGEF1A-bioinformatics/RESULTS.md "The donkey sequence A0A9L0J8J4 (516 residues) aligns to human Q8N9B8 (481 residues) with 96.25% identity across 480 paired residues"].

## Function (human ortholog)
- Human Swiss-Prot: GEF for Rap2A and Ras proteins in vitro, and a role in cell migration [file:EQUAS/RASGEF1A/RASGEF1A-bioinformatics/RASGEF1A-human-Q8N9B8-uniprot.txt "Guanine nucleotide exchange factor (GEF) with specificity for"; "Plays a role in cell migration."]. The underlying papers (PMID:17121879, cholangiocarcinoma growth/migration; PMID:19645719, Rap2-specific exchange) are not cached locally, so the evidence is taken from the Swiss-Prot summary and the human GO lines (GEF activity IDA, cell migration IDA, positive regulation of Ras signal transduction IDA, plasma membrane and Ras signal transduction IBA).
- No experimental subcellular localization in the human record apart from Reactome cytosol (TAS).

## Annotation decisions
- GEF activity: ACCEPT (core).
- Ras protein signal transduction (TreeGrafter) and small GTPase-mediated signal transduction (InterPro): ACCEPT; the broader term also covers the preferred Rap2 substrate.
- plasma membrane (TreeGrafter): KEEP_AS_NON_CORE (PAINT inference only; no experimental localization).
- cell migration and positive regulation of Ras protein signal transduction (Ensembl orthology from human IDA): KEEP_AS_NON_CORE.

## ProtNLM2
- GO:0007264 small GTPase-mediated signal transduction: exact term in donkey GOA -> CNN.
- Non-GO output (not scored): subcellular location "Nucleus" (no supporting evidence in the human record; human has cytosol by Reactome TAS and plasma membrane by IBA).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

- Deep research: `just deep-research-falcon EQUAS RASGEF1A --fallback perplexity-lite` failed (falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). Proceeded with the two primary human papers, now cached (abstract only): PMID:17121879 and PMID:19645719.
- Identity: A0A9L0J8J4 (516 aa) is the full-length donkey RASGEF1A, not a fragment. It is 36 residues longer than human canonical Q8N9B8 (481 aa) at the N-terminus (human Met1 = donkey Met37), most likely an upstream start in the Ensembl gene model; REM (76-205) and CDC25 catalytic (249-496) domains are complete [file:EQUAS/RASGEF1A/RASGEF1A-bioinformatics/RESULTS.md "Human Met1 aligns to donkey Met37"].
- Evolutionary placement: PANTHER PTHR23113:SF172 (RAS-GEF DOMAIN-CONTAINING FAMILY MEMBER 1A), the same subfamily as human Q8N9B8 and Xenopus rasgef1a; paralogs RASGEF1B (SF197) and RASGEF1C (SF186) are separate subfamilies. PAINT PTHR23113: GEF activity (GO:0005085) is IBD at eukaryote node PTN000560991 with Q8N9B8 among seeds; Ras protein signal transduction at the same node is seeded by SOS/yeast/amoeba GEFs, not Q8N9B8; plasma membrane (PTN007734601) seeds are other GEF subfamilies; Rap protein signal transduction (PTN000561159) is seeded only by RAPGEF3 (O95398) and was not propagated to RASGEF1.
- Substrate conflict in the literature: Ura et al. 2006 [PMID:17121879 "RASGEF1A protein has a guanine nucleotide exchange activity to K-RAS, H-RAS, and N-RAS proteins in vitro"] vs Yaman et al. 2009 with purified proteins [PMID:19645719 "They do not act on Rap1 or other members of the Ras subfamily."]. The previous review merged both into a single "Rap2 plus H/K/N-Ras" claim (following the Swiss-Prot summary); this is corrected.
- Changes: GO:0007265 Ras protein signal transduction ACCEPT -> KEEP_AS_NON_CORE (Ras specificity disputed); core process now GO:0007264 small GTPase-mediated signal transduction (GO:0032486 Rap and GO:0007265 Ras are siblings under it; in vivo substrate unknown, so I did not MODIFY to Rap). GEF activity ACCEPT; plasma membrane, cell migration and positive regulation of Ras signal transduction KEEP_AS_NON_CORE, with reasons rewritten and primary-paper quotes added. Description rewritten to state the substrate conflict.
- Modules: none contain RASGEF1A (modules/erk_cascade.yaml, kit_signaling.yaml, fgfr_signaling.yaml match only via PTHR23113/SOS).
- Next relative: human RASGEF1A Q8N9B8 (ortholog, same SF172; the experimentally characterised member). No review in repo.
