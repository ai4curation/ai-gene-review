# moeB curation notes

## 2026-07-20 OpenScientist report assessment

The completed OpenScientist report is retained unchanged as provider output and
assessed as `LOW_QUALITY`. Its conserved MoaD acyl-adenylation reaction agrees
with reviewed target UniProt, and it explicitly acknowledges that Q88PW3 has no
direct assay, structure, or knockout evidence. The report nevertheless presents
unsaved target motif, zinc-site, global-alignment, architecture, partner, and
broad physiological analyses as decisive evidence. Those claims are not
propagated.

The E1-like evolutionary relationship does not make MoeB a ubiquitin-like
modifier activating enzyme under the live GO:0008641 definition. Q88PW3 is
supported for MoaD C-terminal acyl-adenylation, not the high-energy thiolester
formation required by that term, so the existing GO:0008641 row remains
`REMOVE`. Sulfur loading onto MoaD is a separate reaction outside MoeB's direct
catalytic function.


## Full-gene re-review, 2026-09-20

All eight rows and core synthesis reviewed. Restored catalytic activity, nucleotidyltransferase activity, cytoplasm and cytosol as valid core terms; broad ancestors and duplicate compatible locations are not biological errors. Retained three chemistry-specific rejections: target lacks the rhodanese fusion needed for that sulfurtransferase hypothesis, sulfate transfer differs from MoaD adenylation, and live GO:0008641 requires a high-energy thiolester bond whereas classical MoeB forms an acyl-adenylate. Read all OpenScientist findings and caveats; added primary PMID:11713534/17223713 comparative mechanism. No native PP_0735 assay is claimed. All source rows preserved; no NEW added.


## Recovery PR evidence refinement (2026-09-22)

Refine the catalytic-activity ancestor to the already supported specific reaction. Source GOA assertions are unchanged.


## Completion pass (2026-11-10)

Brought to COMPLETE, aligned with the new genes/ECOLI/moeB review and the PTHR10953 family review.
Nucleotidyltransferase (GO:0016779) and cytoplasm (GO:0005737) changed from ACCEPT to MODIFY
(correct but general; GO:0061605 and GO:0005829 are carried). GO:0004792 and GO:0008146 REMOVE kept,
now with PANTHER (TreeGrafter) source defects naming the PAINT nodes PTN000102040 (Uba4-only seed,
TOO_DEEP) and PTN000102608 (MoeZ-only seed, WRONG_NODE); GO:0008641 REMOVE kept with an INTERPRO
source defect. ARBA-derived UniProt FUNCTION quotes and the self-citing GOA table were replaced by
the PubMed-tied E. coli UniProt FUNCTION line and PMID:11463785
["the formation of a thioester intermediate between MoeB and MoaD could not be observed"].
The OpenScientist report reference was re-rated LOW_QUALITY to match the 2026-07-20 note.
Core MF GO:0061605.
