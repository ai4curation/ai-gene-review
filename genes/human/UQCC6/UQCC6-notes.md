# UQCC6 (BRAWNIN, C12orf73) review notes

## 2026-09-30 — initial review (claude-code)

### Identity
- UniProt Q69YU5, 71 aa, HGNC:34450. Synonyms BR, BRAWNIN, C12orf73. Small ORF-encoded
  peptide (microprotein) that was unannotated as a functional protein until 2020.
- Topology (UniProt FT): residues 1-8 matrix, 9-25 helical signal-anchor (type II), 26-71
  intermembrane space. C-terminal IMS orientation is experimental in both key papers.
- Family: InterPro IPR027858 "Protein BRAWNIN"; Pfam PF14990 (DUF4516); PANTHER PTHR28492.
  Vertebrate-conserved; IBA donors include fly (FBgn0259204), mouse and zebrafish, so the
  PAINT node extends beyond vertebrates.

### Discovery and function (Zhang et al. 2020, PMID:32161263, full text cached)
- [PMID:32161263 "we demonstrate that BRAWNIN, a 71 a.a. peptide encoded by C12orf73, is essential for respiratory chain complex III (CIII) assembly"]
- Localisation: carbonate-resistant IMM protein, C-terminus in IMS
  [PMID:32161263 "using differential detergent extraction, we determined that BR resides in the IMM and not in the outer mitochondrial membrane (OMM)"].
- Zebrafish KO: [PMID:32161263 "In zebrafish, Brawnin deletion causes complete CIII loss, resulting in severe growth retardation, lactic acidosis and early death."]
  CIII-specific: [PMID:32161263 "while CI, CII, and CIV activities were not significantly affected"].
- Mouse MEF KO also reduced CIII2 [PMID:32161263 "demonstrating that the requirement for BR in CIII assembly or stability extends to higher vertebrates"].
- Interactions: IP/MS intersection BR, GHITM, UQCRC1; UQCRC1 validated by co-IP in mouse heart
  mitochondria; UQCRQ-FLAG co-IP of BR-HA [PMID:32161263 "the interaction between BR and UQCRC1 detected in human cells was validated by co-immunoprecipitation(co-IP)/western blot"].
  This is the basis of the GO:0005515 IPI row (with UniProtKB:P31930 = UQCRC1).
- Induced by AMPK / nutrient stress [PMID:32161263 "In human cells, BRAWNIN is induced by the energy-sensing AMPK pathway, and its depletion impairs mitochondrial ATP production."]

### SMIM4/UQCC5 partner and early CIII assembly (Dennerlein et al. 2021, PMID:34969438, full text cached)
- Topology confirmed [PMID:34969438 "These results confirmed that C12ORF73 represents a protein of the IMM that exposes its C-terminus into the IMS, which agrees with previous studies (Zhang et al., 2020)."]
- Early-intermediate complex with UQCC1, UQCC2, SMIM4 (not UQCC3, not RIESKE)
  [PMID:34969438 "These results demonstrate that C12ORF73FLAG forms a complex with UQCC1, UQCC2, and SMIM4 but not with UQCC3."]
- Binds newly synthesised cytochrome b [PMID:34969438 "As expected, both immunoisolations clearly enriched newly synthesized CYTB."]
- Contradicts late-subunit (UQCRC1/UQCRQ) interactions from Zhang 2020:
  [PMID:34969438 "In contrast to the reports on BR (Zhang et al., 2020), C12ORF73 does not interact with late complex constituents but rather shows exclusively"]
  and the UQCRQ co-IP reproduced only "marginal amounts".
- Complex IV? The only data: siRNA knockdown [PMID:34969438 "Knockdown of C12ORF73 impaired slightly the level of the NADH:ubiquinone oxidoreductase, cytochrome c oxidase, and the ATP synthase; however, the cytochrome c reductase was, similar to SMIM4 knockdown, significantly reduced (Figure 5E)."]
  The paper's own conclusions attribute to C12ORF73 only a CIII biogenesis role. Zebrafish KO
  shows CIV activity unaffected (PMID:32161263) and UniProt's mouse entry (Q8BTC1, from
  PMID:35977508) records that CIV subunits are not affected in Uqcc6 deficiency. The GOA IDA
  row for GO:0033617 complex IV assembly therefore rests on a slight, pleiotropic effect →
  MARK_AS_OVER_ANNOTATED (not removed; it is an experimental curation).

### COMB complex (Liang et al. 2022, PMID:35977508, abstract only)
- [PMID:35977508 "Subsequently, microproteins SMIM4 and BRAWNIN together with COMA subunits form the COMB complex to stabilize nascent CYTB."]
- [PMID:35977508 "Furthermore, when nuclear CIII subunits are limiting, COMB is required to chaperone nascent CYTB to prevent OXPHOS collapse."]
- This is the mouse work behind the ISS row (with UniProtKB:Q8BTC1).
- No GO CC term exists for COMA/COMB/COMC (QuickGO search for "COMB complex" returned nothing
  relevant) → suggested question only, not a NEW annotation.

### Dissenting / nuance (Wang et al. 2024, PMID:37769950, abstract only)
- [PMID:37769950 "we showed that the deletion rather than knockdown of BRAWNIN impaired the assembly of CIII"]
- [PMID:37769950 "although only a minimal amount of BRAWNIN was required for CIII assembly"]
- Supports KO-level requirement; knockdown phenotypes are weak. Consistent with CIII assembly
  as core function; argues further against reading knockdown-based CIV effects as function.

### Other
- PMID:38514619 (NUAK1, neurons) — BRAWNIN is a NUAK1-regulated transcript; regulates cortical
  axon branching downstream of NUAK1. Contextual, not a direct GO annotation candidate
  (indirect/pleiotropic).
- PMID:34800366 MitoCoP — HTP mitochondrial proteome; supports mitochondrion.

### Decisions
- protein binding (IPI, UQCRC1) → REMOVE (uninformative; interaction with late subunits also
  not reproduced by PMID:34969438). No informative MF term: the protein's activity (stabilising
  nascent CYTB within COMB) has no clean GO MF; follow UQCC2 precedent of no MF.
- mitochondrion (HTP, IBA) → ACCEPT; mitochondrial inner membrane (IDA x2, IEA) → ACCEPT.
- complex III assembly (IBA, IEA, IMP, ISS) → ACCEPT (core).
- complex IV assembly (IDA) → MARK_AS_OVER_ANNOTATED.
- Comparators: UQCC2 review (genes/human/UQCC2) uses directly_involved_in GO:0034551 + IMM,
  no MF — same pattern applied here. UQCC3 review exists (cardiolipin binding MF).
- No NEW annotations proposed. Complex III assembly is a process in which UQCC6 does part of the
  work (chaperoning/stabilising nascent CYTB within COMB), so it passes the participation test,
  but it is already annotated.
