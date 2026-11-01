# VP35 (Zaire ebolavirus, Mayinga-76; UniProt Q05127) — curation notes

## Provenance of this file

No deep-research API keys are available in this container, so `just deep-research`
was **not** run and there is no `VP35-deep-research-<provider>.md` file. The
literature below was read directly from the cached publications in
`publications/` (nine of the thirteen cited papers have
`full_text_available: true`), from the curated UniProt record
`VP35-uniprot.txt`, and from PubMed abstracts. The GONUTS wiki
(`gowiki.tamu.edu`), which records CACAO students' per-paper evidence, was
**offline** when checked (2026-10-29): both `PMID:12191476` and `PMID:22238300`
pages returned only "This site is temporarily offline while we perform
upgrades.", so the student-recorded evidence for the two abstract-only CACAO
rows could not be inspected.

## What the protein is

A 340-residue filoviral phosphoprotein (P-protein) homologue with two
functional halves:

- an **N-terminal oligomerization region** (a coiled coil in residues ~82–145,
  crystallised as a bipartite parallel helix bundle) plus a highly conserved
  N-terminal peptide (residues 20–48) that binds the nucleoprotein NP, and
- a **C-terminal interferon inhibitory domain (IID**, residues ~215–340) that
  binds dsRNA.

UniProt: `[file:EBOZM/VP35/VP35-uniprot.txt "DOMAIN: The interferon inhibitory
domain (IID) binds dsRNA"]` and `[file:EBOZM/VP35/VP35-uniprot.txt "The
oligomerization domain forms bipartite parallel helix bundles with a coiled coil
in the N-terminal half"]`. Family assignment is PROSITE-ProRule PRU01071 /
Pfam PF02097 Filo_VP35 / PIRSF018326 VP35_FiloV.

## Core function 1 — polymerase cofactor and NP chaperone

VP35 is the filoviral equivalent of the *Mononegavirales* P protein: it bridges
the catalytic polymerase L and the NP-encapsidated template.

- `[PMID:23493393 "For transcription of the viral genome four viral proteins are
  essential: the nucleoprotein NP, the polymerase L, the polymerase cofactor
  VP35, and VP30."]` and `[PMID:23493393 "The enzymatically active part of the
  viral polymerase L is bound to the nucleocapsid by interaction with the
  polymerase cofactor VP35"]`.
- The mechanism of the NP interaction: `[PMID:25865894 "We identify an
  intrinsically disordered peptide derived from EBOV VP35 (NPBP, residues 20-48)
  that binds NP with high affinity and specificity, inhibits NP oligomerization,
  and releases RNA from NP-RNA complexes in vitro."]` — i.e. VP35 holds NP in a
  monomeric, RNA-free state, which is a **molecular sequestering** activity
  (GO:0140313), and the crystal structure of the NPBP/ΔNP<sub>NTD</sub> complex
  (PDB 4YPI) shows the peptide occludes the NP surfaces needed for NP–NP and
  NP–RNA contacts: `[PMID:25865894 "Our results also show that the VP35 NPBP
  binding relieves NP oligomerization and NP-RNA binding by interacting with two
  distinct regions within NP that are important for viral RNA synthesis."]`.
- UniProt frames the same switch: `[file:EBOZM/VP35/VP35-uniprot.txt "VP35-NP
  interaction controls the switch between RNA-bound NP and free NP and thus the
  switch between genome replication and genome packaging into the
  nucleocapsid"]`.
- Minigenome (MG) assays in several of these papers read out VP35-dependent
  transcription and replication of an EBOV reporter genome, which is what the
  `GO:0019079` / `GO:0019083` IDA rows rest on.

## Core function 2 — structural component of the nucleocapsid

NP + VP35 + VP24 alone suffice to build nucleocapsids:
`[PMID:12191476 "Expression of the nucleoprotein (NP) and virion-associated
proteins VP35 and VP24 led to spontaneous assembly of nucleocapsids in
transfected 293T cells by transmission electron microscopy."]`. In situ
cryo-electron tomography later placed VP35 structurally:
`[file:EBOZM/VP35/VP35-uniprot.txt "Part of the external layer of the
nucleocapsid, likely tethering the nucleocapsid to the matrix and membrane"]`
(PubMed:39293445, not cached here).

## Core function 3 — antagonism of interferon *induction* (not of IFN signalling)

This distinction is the single most important point for reviewing the existing
annotations, because one CACAO row gets it backwards.

- VP35 blocks the induction arm: `[PMID:12829834 "VP35 blocks virus-induced
  IRF-3 phosphorylation and subsequent IRF-3 dimerization and nuclear
  translocation."]`, and it cannot block the response arm: `[PMID:12829834
  "Neither the Zaire or Reston VP35 proteins were able to inhibit IFN-β-induced
  activation of the ISG54 or the ISG56 promoters (Fig. 1C and D)."]`. In EBOV it
  is **VP24**, not VP35, that blocks the cellular response to IFN
  `[PMID:19557165 "VP24 inhibits the cellular response to exogenous IFN by
  interacting with karyopherin α1, preventing the nuclear accumulation of
  tyrosine-phosphorylated Stat1 and Stat2"]`.
- Two mechanisms converge on IRF-3:
  - **dsRNA sequestration by the IID.** `[PMID:16698997 "We now provide evidence
    that VP35 possesses double-stranded RNA (dsRNA)-binding activity."]`,
    specific for duplex RNA `[PMID:16698997 "VP35 interacted specifically with
    poly(rI) · poly(rC), poly(rA) · poly(rU), or in vitro-transcribed dsRNAs
    derived from EBOV sequences, and not with single-stranded RNAs (ssRNAs) or
    double-stranded DNA"]`, and this blocks the RIG-I arm `[PMID:16698997 "These
    experiments indicate that VP35 blocks activation of IRF-3 induced by
    overexpression of RIG-I, a cellular helicase recently implicated in the
    activation of IRF-3 by either virus or dsRNA."]`. R312A and K309A are the
    dsRNA-binding point mutants.
  - **Inhibition of the IRF-3-activating kinases.** `[PMID:19153231
    "Coimmunoprecipitation experiments now demonstrate physical interactions of
    VP35 with IKKepsilon and TBK-1"]` and `[PMID:19153231 "These data suggest
    that VP35 exerts its IFN-antagonist function, at least in part, by blocking
    necessary interactions between the kinases IKKepsilon and TBK-1 and their
    normal interaction partners, including their substrates, IRF-3 and IRF-7."]`
    — VP35 also suppresses IKKε kinase activity toward IRF-3 in vitro, which is
    a protein-kinase-inhibitor-like activity rather than bare binding.
  - A third, RIG-I-proximal mechanism: VP35 strips the RIG-I activator PACT
    (PRKRA) off RIG-I `[PMID:23870315 "Here, we show that EBOV VP35 inhibits
    PACT-induced RIG-I ATPase activity in a dose-dependent manner. The
    interaction of PACT with RIG-I is disrupted by wild-type VP35, but not by
    VP35 mutants that are unable to bind PACT."]`, and the same interaction
    reciprocally costs VP35 its polymerase association `[PMID:23870315 "In
    addition, PACT-VP35 interaction impairs the association between VP35 and the
    viral polymerase, thereby diminishing viral RNA synthesis and modulating
    EBOV replication."]`.

## Secondary immune-evasion arms (real, but narrower)

- **IRF7 via the host SUMO machinery.** `[PMID:19557165 "VP35, while not itself
  a SUMO ligase, increased PIAS1-mediated SUMOylation of IRF7, and repressed Ifn
  transcription."]`; in Fig. 7 `[PMID:19557165 "Importantly, in the presence of
  both PIAS1 and VP35, the levels of SUMO conjugated IRF7 were significantly
  greater than those expressing PIAS1 alone."]` and `[PMID:19557165 "In
  agreement with the idea that VP35 promotes IRF7 SUMOylation, VP35, when
  expressed at higher levels, increased IRF7 SUMOylation in a dose dependent
  manner even in the absence of PIAS1 (Figure S4A)."]`. This is a genuine
  *positive* regulation of a host PTM used for a repressive end.
- **PKR/eIF2α.** UniProt: `[file:EBOZM/VP35/VP35-uniprot.txt "Also inhibits the
  antiviral effect mediated by the host interferon-induced, double-stranded
  RNA-activated protein kinase EIF2AK2/PKR (PubMed:17065211)"]`; PKR antagonism
  was also assayed in `[PMID:22238300 "Analysis of mutant proteins demonstrated
  that reporter activity in RSS assays did not correlate with their ability to
  antagonize double-stranded RNA (dsRNA)-activated protein kinase R (PKR) or
  bind siRNA."]`.
- **RNA silencing suppression (RSS).** `[PMID:22238300 "A reporter gene
  containing specific microRNA target sequences was used to demonstrate that
  prior expression of wild-type VP35 was able to block establishment of
  microRNA silencing in mammalian cells."]` and, mechanistically,
  `[PMID:21228243 "VP35 directly interacts with Dicer partners TRBP and PACT in
  an siRNA-independent fashion and in the absence of effects on interferon
  (IFN)."]`. The authors are careful that part of the mammalian reporter signal
  is artefactual: `[PMID:22238300 "The results suggest that enhanced reporter
  activity in the presence of VP35 is a composite of nonspecific translational
  enhancement and silencing suppression."]`.
- **Dendritic-cell maturation / adaptive priming.** `[PMID:19828757 "When
  expressed in mouse immature DCs, Ebola virus VP35 prevents virus-stimulated
  expression of CD40, CD80, CD86 and major histocompatibility complex class
  II."]` and `[PMID:19828757 "We conclude from these experiments that the VP35
  protein attenuates the capacity of DCs to stimulate CD4 + T-cell
  activation."]`. Note the mechanism is partly indirect/IFN-mediated:
  `[PMID:19828757 "Addition of type I IFN to mouse DCs only partially reverses
  the inhibitory effects of VP35."]`, and nothing in the paper assays antigen
  processing or peptide loading — MHC class II is measured as a *surface
  maturation marker* by FACS. Mutant mapping: `[PMID:19828757 "Deletion of the
  amino terminus abolishes its activity, whereas a mutation in the RNA binding
  motif has no effect."]`.

## Localization

Virion plus host cytoplasm. Direct imaging: `[PMID:28679761 "In contrast, VP35
showed a diffuse, slightly granular cytoplasmic localization, and in some cases
it localized in apparent inclusion bodies"]` and `[PMID:23493393 "both VP30 and
VP35 are diffusely distributed in the cytoplasm preventing colocalization
analyses"]`. UniProt: `[file:EBOZM/VP35/VP35-uniprot.txt "SUBCELLULAR LOCATION:
Virion. Host cytoplasm"]`.

## Host factors acting *on* VP35 (not VP35 functions)

- **TRIM6** ubiquitinates VP35 at K309 and is co-opted
  `[PMID:28679761 "we also found that TRIM6 enhances EBOV polymerase activity in
  a minigenome assay and TRIM6 knockout cells have reduced replication of
  infectious EBOV, suggesting that VP35 hijacks TRIM6 to promote EBOV
  replication through ubiquitination"]`.
- **DRBP76/ILF3** is an antiviral restriction factor that binds VP35 and
  *reduces* polymerase function: `[PMID:21987769 "Overexpression of DRBP76 did
  not alter the ability of VP35 to inhibit type I IFN production but did impair
  the function of the EBOV transcription/replication complex."]` and
  `[PMID:21987769 "These data suggest that DRBP76, via its association with
  VP35, exerts an anti-EBOV function."]`. The GO:0005515 row with
  `UniProtKB:Q12906` therefore records an interaction whose directionality is
  host→virus; it supports no VP35 molecular function.

## CACAO rows: what the cited paper actually shows

ASSIGNED BY = CACAO on eight rows (six distinct PMIDs). Summary of the
judgements written into the review:

| GO term | Ev | PMID | Verdict |
|---|---|---|---|
| GO:0019013 viral nucleocapsid | IDA | 12191476 | sound; TEM assembly + later cryo-ET confirm |
| GO:0052170 innate immune suppression | IDA | 12829834 | sound and at a useful level |
| GO:0010629 negative regulation of gene expression | IDA | 12829834 | correct but far too general for a host-promoter readout |
| GO:0033235 positive regulation of protein sumoylation | IMP | 19557165 | sound, mechanism-level, secondary arm |
| GO:0039502 suppression of host type I IFN-**mediated signaling pathway** | IMP | 16698997 | **wrong arm of the pathway** — see Core function 3 |
| GO:0052562 suppression of host immune response | IDA | 19828757 | true but the generic parent; the paper's own content is adaptive |
| GO:0039505 suppression of MHC-class-II antigen processing/presentation | IMP | 19828757 | phenotype read as process; MHC-II measured as a FACS maturation marker only |
| GO:0060965 negative regulation of miRNA-mediated gene silencing | IDA | 22238300 | sound (abstract-explicit), secondary arm |

Patterns for the CACAO failure taxonomy: one **wrong-arm/antonym-direction**
error (GO:0039502 — the paper that the student cited is about blocking IFN
*production*, and its companion paper from the same lab explicitly shows VP35
does **not** block IFN-receptor signalling); one **phenotype-as-process**
(GO:0039505); and one **granularity** case (GO:0010629, a root-level host
gene-expression term used for an IFN-promoter reporter result). The remaining
five rows are good annotations.
