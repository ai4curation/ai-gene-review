# SOCS3 (human, UniProt O14543) — review notes

Journal of research for the SOCS3 gene review. Provenance recorded inline as
[PMID:xxxx "verbatim quote"] or [UniProt O14543] where appropriate.

## Identity / domain architecture (UniProt O14543)

- 225 aa cytoplasmic protein; member of the SOCS/CIS family (8 members: CIS, SOCS1-7).
  Synonyms: CIS-3, SSI-3, STAT-induced STAT inhibitor 3 [UniProt O14543].
- Domain layout (UniProt feature table):
  - KIR (kinase inhibitory region): residues 22–33
  - ESS (extended SH2 subdomain): residues 34–45
  - SH2 domain: residues 46–142
  - SOCS box: residues 177–224
- UniProt DOMAIN comments: "The ESS and SH2 domains are required for JAK
  phosphotyrosine binding. Further interaction with the KIR domain is necessary for
  signal and kinase inhibition." and "The SOCS box domain mediates the interaction
  with the Elongin BC complex, an adapter module in different E3 ubiquitin ligase
  complexes." [UniProt O14543]
- Cytokine-inducible; STAT3 induces SOCS3 expression (classic negative-feedback loop).
  Phosphorylated on Tyr after IL-2/EPO/IGF1 stimulation [UniProt O14543].

## Core function: negative-feedback inhibitor of JAK-STAT signaling

- UniProt FUNCTION: "SOCS family proteins form part of a classical negative feedback
  system that regulates cytokine signal transduction. SOCS3 is involved in negative
  regulation of cytokines that signal through the JAK/STAT pathway ... Inhibits signal
  transduction by binding to transmembrane signaling receptors including IL6ST/gp130,
  LIFR, EPOR, INSR, IL12RB2, CSF3R/G-CSF-R and LEPR. Binding to JAK2 inhibits its
  kinase activity and regulates IL6 signaling." [UniProt O14543].
- Mechanism of JAK inhibition: SOCS3 binds JAK through both the KIR (acting as a
  pseudosubstrate) and the SH2 domain to a phospho-Tyr in the JAK2 JH1 domain
  [UniProt O14543 SUBUNIT, from PubMed:10421843]. The original mechanistic paper:
  Sasaki et al. 1999 "CIS3/SOCS3 inhibits Janus tyrosine kinase by binding through the
  N-terminal kinase inhibitory region as well as SH2 domain" [UniProt RN5 = PubMed:10421843].
- In vivo IL-6 specificity: SOCS3 (not SOCS1) is the key brake on IL-6/gp130 signaling.
  [PMID:12754505 "Members of the suppressor of cytokine signaling (SOCS) family are
  potentially key physiological negative regulators of interleukin-6 (IL-6) signaling"]
  and [PMID:12754505 "Socs3 deficiency results in prolonged activation of signal
  transducer and activator of transcription 1 (STAT1) and STAT3 after IL-6 stimulation"].
  This Nat Immunol 2003 paper (Croker et al.) underpins the ISS annotations transferred
  from mouse (UniProtKB:O35718, MGI:1201791) for cell-surface JAK-STAT signaling and
  IL-6-mediated signaling pathway.

## SH2 / phosphotyrosine docking

- SOCS3 SH2 domain binds specific activated phospho-Tyr on receptors: gp130/IL6ST,
  LEPR, EPOR (Y429/Y431), IL12RB2, CSF3R [UniProt SUBUNIT; PubMed:12027890,
  PubMed:14559241]. EPOR high-affinity site: Hoertner et al. 2002 [UniProt RN6 =
  PubMed:12027890].
- This grounds the GO MF terms: phosphotyrosine residue binding (GO:0001784),
  SH2 domain activity / cytokine receptor binding (GO:0005126).

## SOCS box → ECS (Elongin BC–Cullin5–RBX2) E3 ubiquitin ligase

- SOCS3 is the substrate-recognition subunit of a Cullin5-RING E3 ligase. The SOCS box
  recruits Elongin BC, linking bound substrates to CUL5–RBX2 for ubiquitination and
  proteasomal degradation.
- [PMID:15601820 "SOCS-box proteins recruit"] / "substrates to the ECS complex and are
  linked to Cullin-Rbx via Elongin B/C" and [PMID:15601820 "SOCS-box proteins associate
  with Cul5-Rbx2"]. Kamura et al. 2004 Genes Dev (UniProt RN9). UniProt: SOCS3 interacts
  with CUL5, RNF7/RBX2, ELOB and ELOC [UniProt O14543].
- UniProt PATHWAY: "Protein modification; protein ubiquitination." (UPA00143) — basis of
  GO:0016567 protein ubiquitination IEA, and GO:0016567/SOCS-box mechanism.

## Apoptosis / cell survival

- [PMID:9266833 "suppressed the apoptotic effect"] of LIF: forced expression of SSI-2 and
  SSI-3 (SOCS3) in M1 myeloid leukemia cells "suppressed the apoptotic effect of LIF,
  like SSI-1". This is the TAS basis for GO:0043066 negative regulation of apoptotic
  process. Note this is an indirect/downstream consequence of blocking LIF-gp130-STAT3
  pro-differentiation/apoptosis signaling, not a direct anti-apoptotic activity.
- PMID:9266833 (Minamoto et al. 1997) is the cloning/functional paper for human SSI-2
  (SOCS2) and SSI-3 (SOCS3); it is correctly cited for SOCS3.

## Immune / Th17 biology

- SOCS3 limits IL-6 / IL-23-driven Th17 responses; IL-6 trans-presentation paper
  PMID:27893700 (Heink et al. 2017, full text available) is cited as TAS for
  GO:0072540 T-helper 17 cell lineage commitment. SOCS3 is a downstream feedback
  inhibitor in the IL-6→STAT3→Th17 axis. The TAS annotation reflects SOCS3's role in the
  IL-6/Th17 module; keep as non-core (developmental/process context, not SOCS3's
  molecular core).

## Interaction-only (IPI / proteomics) annotations — context

GOA carries several GO:0005515 "protein binding" IPI annotations from IntAct, sourced
from interaction screens. Per curation guidelines, bare "protein binding" is
uninformative and should not be treated as core:

- PMID:19027008 — MAP1S as a SOCS3-interacting protein (IntAct partner Q66K74/MAP1S);
  partner is real, paper is genuinely about SOCS3 [PMID:19027008 "microtubule-associated
  protein 1S (MAP1), a member of the MAP1 family, was identified as a novel SOCS3
  interacting protein"]. Binding annotation only.
- PMID:24728074 — large fluorescence-polarization SH2-domain interactome (c-Met/KIT/ErbB/AR);
  partners P10721 (KIT), Q13480 (c-Met/MET). High-throughput peptide-binding screen.
- PMID:25203322 — SNAI1 (O95863) interaction; this paper is primarily about FBXO11/SNAIL
  EMT but reports a SOCS3–SNAI1 IntAct interaction. Binding only.
- PMID:25416956 (Rolland 2014) and PMID:32296183 (Luck 2020) — large-scale binary
  interactome (Y2H) maps; partners include YES1 (P07947), TXK (P42681), BLK (P51451),
  KIAA1958 (Q8N8K9), PTK2/FAK (I6L996). Systematic Y2H; generic protein-binding.

These IPI binding annotations are kept as non-core (or over-annotated); none establishes a
specific informative MF beyond what SH2/receptor-binding terms already capture.

## Annotations that look like cross-gene / weak transfers

- PMID:9727029 ("Interaction of human SOCS-2 with the IGF-I receptor", Dey et al. 1998)
  is the abstract title about SOCS-2, but UniProt lists Dey/Furlanetto/Nissley IGF1R work
  for SOCS3 too (PubMed:11071852 is the SOCS3-IGF1R paper). The GOA IDA annotation
  GO:0004860 protein kinase inhibitor activity / GO:0009898 cytoplasmic side of PM is
  attributed to PMID:9727029 by UniProt curators. Per CLAUDE.md, do NOT REMOVE an
  experimental (IDA) annotation merely because the cached abstract foregrounds a paralog
  (SOCS2) — the function (kinase inhibitor activity, plasma-membrane-proximal action) is
  correct for SOCS3. The MF protein kinase inhibitor activity is independently strongly
  supported (KIR mechanism, ISS GO:0019210). ACCEPT GO:0004860 as core; the cellular
  component GO:0009898 cytoplasmic side of plasma membrane is consistent with SOCS3
  acting at receptor tails — keep as non-core location.

- GO:0035198 miRNA binding (IEA, Ensembl ortholog transfer from mouse O35718): no strong
  human evidence; SOCS3 is not a recognized RNA-binding/miRNA-binding protein. SOCS3 is
  itself a miRNA target (e.g. miR-221, PMID:25019494), which is the opposite relationship.
  This looks like an erroneous ortholog-transferred annotation — MARK_AS_OVER_ANNOTATED.

- GO:0097398 cellular response to IL-17 (IEA ortholog transfer): plausible (SOCS3 is
  induced by/feeds back on IL-17-related inflammation) but indirect; keep as non-core.

- PMID:25019494 (miR-221 downregulates SOCS1/SOCS3): IMP for GO:0046426 negative
  regulation of JAK-STAT. The paper shows miR-221 represses SOCS3 to enhance IFN/JAK/STAT
  anti-HCV effect, confirming SOCS3 as a JAK-STAT inhibitor whose loss prolongs signaling.
  Supports the negative-regulation-of-JAK-STAT function. ACCEPT (core process).

## Cellular location

- Cytosol (GO:0005829) — many Reactome TAS annotations; SOCS3 acts in the cytosol and at
  the cytoplasmic face of receptors. Keep one representative as non-core location.
- GO:0009898 cytoplasmic side of plasma membrane (IDA) — consistent with receptor-tail
  recruitment. Non-core location.

## Summary of core functions to assign

1. MF: protein kinase inhibitor activity (GO:0004860) — KIR-mediated JAK inhibition.
2. MF: phosphotyrosine residue binding (GO:0001784) / SH2 docking on activated receptors
   (GO:0005126 cytokine receptor binding).
3. BP/MF context: negative regulation of receptor signaling pathway via JAK-STAT
   (GO:0046426) — the integrative core role.
4. BP: protein ubiquitination (GO:0016567) via SOCS-box/ECS(CUL5) E3 ligase
   substrate-recognition.

Validation note: core_functions MF ids are strictly validated; supporting_text must be a
verbatim substring of the cited cached publication.
