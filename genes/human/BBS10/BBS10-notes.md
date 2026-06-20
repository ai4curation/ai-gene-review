# BBS10 (Q8TAM1) — Gene Review Notes

## Summary of identity and function

BBS10 (C12orf58; HGNC:26291) is a **vertebrate-specific, chaperonin-like protein** of the
group II / TCP-1 (CCT/TRiC) chaperonin family. It is one of three "chaperonin-like" BBS
proteins (with MKKS/BBS6 and BBS12). Together with the CCT/TRiC chaperonin and BBS7 these
form the **BBS-chaperonin complex**, which acts as an **assembly factor (chaperone) for the
BBSome** — it is NOT a stable structural subunit of the mature BBSome (GO:0034464).

- "BBS10 encodes a vertebrate-specific chaperonin-like protein and is a major BBS locus."
  [PMID:16582908 title]. UniProt: "Belongs to the TCP-1 chaperonin family"; RecName "BBSome
  complex assembly protein BBS10"; FUNCTION "Probable molecular chaperone that assists the
  folding of proteins upon ATP hydrolysis."
- The catalytic chaperonin/ATPase activity of BBS10 itself has NOT been demonstrated
  biochemically; it is inferred from the conserved Cpn60/TCP-1 (Pfam PF00118; InterPro
  IPR002423) domain. UniProt flags FUNCTION as "Probable."

## BBS-chaperonin complex / BBSome assembly

[PMID:20080638 "a novel complex composed of three chaperonin-like BBS proteins (BBS6, BBS10,
and BBS12) and CCT/TRiC family chaperonins mediates BBSome assembly... Chaperonin-like BBS
proteins interact with a subset of BBSome subunits and promote their association with CCT
chaperonins. CCT activity is essential for BBSome assembly... BBS6, BBS10, and BBS12 are
necessary for BBSome assembly"].
- UniProt SUBUNIT: "Component of a complex composed at least of MKKS, BBS10, BBS12, TCP1,
  CCT2, CCT3, CCT4, CCT5 and CCT8" [ECO:0000269|PubMed:20080638].
- UniProt INTERACTION: BBS10 binds BBS12 (Q6ZW61), BBS7 (Q8IWZ6), BBS9 (Q3SYG4).
- Disease mutations (e.g. R34P, V240G, S311A, S329L) reduce BBS10 interaction with BBS7/BBS9
  and/or BBS12, linking assembly-factor function to pathology [PMID:20080638; PMID:16582908].
- D81N mutagenesis "Greatly decreases all interactions with BBS7, BBS9 and BBS12 indicating
  that this residue may be required for overall protein conformation" (UniProt FT MUTAGEN).

[PMID:22500027 "Three additional BBS genes (BBS6, BBS10, and BBS12) have homology to type II
chaperonins and interact with CCT/TRiC proteins and BBS7 to form a complex termed the
BBS-chaperonin complex. This complex is required for BBSome assembly... we show that the
BBS-chaperonin complex plays a role in BBS7 stability."] — full text available. This paper
characterizes the ordered, chaperonin-assisted assembly of the BBSome core
(BBS7-BBS2-BBS9), supporting the IMP annotation to regulation of protein-containing complex
assembly (GO:0043254) and chaperone-mediated protein complex assembly (GO:0051131).

## Subcellular location

- UniProt SUBCELLULAR LOCATION: "Cell projection, cilium"; Note "Located within the basal
  body of the primary cilium of differentiating preadipocytes" [ECO:0000269|PubMed:19190184].
  Basis for IEA GO:0005929 (cilium, UniProtKB-SubCell). BBS10 acts as a cytoplasmic assembly
  chaperone; the ciliary/basal-body localization is reported in the adipogenesis context.

## Transcriptional regulation annotation (GO:0061629) — scrutiny

[PMID:22302990 abstract] is primarily about **BBS7** having a nuclear role and interacting
with the PcG protein RNF2 (Q99496). "Our data supports a similar role for other BBS proteins."
The IPI annotation of BBS10 → RNA Pol II transcription factor binding (with RNF2, UniProtKB:
Q99496), assigned by MGI, is peripheral and not a core function of BBS10. Full text not in
cache (full_text_available: false) — defer rather than remove; mark as non-core /
over-annotation candidate.

## Photoreceptor / cilium phenotype annotations (PMID:17980398) — scrutiny

[PMID:17980398 abstract] "Retinal morphology in patients with BBS1 and BBS10 related
Bardet-Biedl Syndrome evaluated by Fourier-domain optical coherence tomography." This is a
**clinical OCT imaging study** describing retinal dystrophy and photoreceptor disruption in
BBS1- and BBS10-mutation patients. It documents a disease phenotype (loss-of-function ->
retinal degeneration) but does NOT provide mechanistic evidence that BBS10 protein is
directly "involved in" photoreceptor cell maintenance (GO:0045494) or "non-motile cilium
assembly" (GO:1905515) at the molecular level. These BHF-UCL IMP annotations are
phenotype-derived and represent downstream/indirect consequences via impaired BBSome
assembly, not a direct molecular role. Full text available. Treat as non-core; the cilium
assembly defect is indirect (BBS10 is an assembly chaperone, not a structural ciliary/IFT
protein).

## Interactome (protein binding) annotations

- IPI GO:0005515 protein binding from PMID:20080638 (partners BBS7 Q8IWZ6, BBS9 Q3SYG4,
  BBS12 Q6ZW61) — bona fide BBS-chaperonin complex interactions.
- IPI GO:0005515 from PMID:28514442 (BioPlex; "Architecture of the human interactome") and
  PMID:33961781 ("Dual proteome-scale networks", BioPlex 3.0) — both with BBS7 (Q8IWZ6).
  High-throughput AP-MS; consistent with the BBS10-BBS7 interaction.
Per curation guidelines, GO:0005515 "protein binding" is uninformative and should not be
treated as core; the underlying interactions are better captured by the assembly-factor BP
terms and complex membership.

## GO term reference notes
- GO:0051082 "unfolded protein binding" is now an OBSOLETE term (deprecated in favor of
  protein folding chaperone activity). Do NOT propose it.
- GO:0044183 "protein folding chaperone": "Binding to a protein or a protein-containing
  complex to assist the protein folding process."
- GO:0140662 "ATP-dependent protein folding chaperone": same, "driven by ATP hydrolysis."
- GO:0034464 "BBSome": structural ciliary complex of the 7 core BBS proteins + BBIP10 —
  BBS10 is NOT a member (it is the assembly factor).

## Core function conclusion
BBS10's core, defining role is as an **ATP-binding, chaperonin-like assembly factor** that,
within the BBS-chaperonin complex (with MKKS/BBS6, BBS12, CCT/TRiC, BBS7), mediates assembly
of the BBSome core. BP: chaperone-mediated protein complex assembly (GO:0051131) and
regulation of protein-containing complex assembly (GO:0043254). MF: ATP binding
(GO:0005524), with probable protein-folding-chaperone activity (GO:0044183 / GO:0140662, not
experimentally proven). All ciliary/retinal phenotypes are downstream of impaired BBSome
assembly.
