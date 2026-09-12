# KDX1 (MLP1 / YKL161C) — curation notes

*S. cerevisiae* KDX1 (systematic name YKL161C; commonly called MLP1 in the primary literature).
UniProt P36005. This is a poorly-characterized ("dark") paralog of the cell-wall-integrity (CWI)
MAP kinase SLT2/MPK1. This journal separates what is genuinely KNOWN about **KDX1/Mlp1 itself**
from what is known about the well-studied paralog **SLT2/MPK1**, and records inline provenance.

## Identity and nomenclature

- SGD standard name: **KDX1**; the primary literature almost always uses **MLP1**
  ("Mpk1-like protein kinase 1"). Systematic name **YKL161C** [uniprot P36005].
- UniProt AltName is telling: **"Kinase dead X-talker protein 1"** — the "KDX" of the SGD name
  literally encodes "**K**inase **d**ea**d** **X**-talker", i.e. the community regards it as a
  catalytically dead (pseudo)kinase that cross-talks with signaling/transcription machinery
  [file:yeast/KDX1/KDX1-uniprot.txt "AltName: Full=Kinase dead X-talker protein 1"].
- Paralog of **SLT2/MPK1** (UniProt Q00772). KDX1 and SLT2 arose from the whole-genome
  duplication; both are terminal-MAPK-like components of CWI signaling.

## Domain / sequence analysis (done inline; pseudokinase determination)

The protein is 433 aa with a single protein-kinase domain (UniProt DOMAIN 23–318). I aligned
the three catalytic motifs of KDX1 (P36005) against its active paralog SLT2/MPK1 (Q00772);
the two align residue-for-residue at each anchor (both HRD-loop at position 151, DFG at ~171):

| Catalytic element (subdomain) | SLT2/MPK1 (active) | KDX1/Mlp1 | Interpretation |
|---|---|---|---|
| Gly-rich P-loop (I) | GHGAYGIV (G30…) | GRGSHS (G30, G32) | Gly-rich loop present |
| β3 VAIK lysine (II) | VAIK**K** (K54/55) | VAIR**K** (R54, **K55**) | The invariant ATP-anchoring Lys is present (UniProt BINDING K55) |
| **HRD catalytic loop (VIb)** | **H**R**D**LKPGN (H151-R152-D153) | **H**C**D**LKPKN (H151-**C152**-D153) | **HRD→HCD**: the catalytic-loop Arg is lost; the catalytic Asp **D153 is retained** (UniProt ACT_SITE 153 "Proton acceptor") |
| **DFG Mg²⁺-binding (VII)** | C**D**FGLAR (**D171**-F172-G173) | C**N**FGLSC (**N171**-F172-G173) | **DFG→NFG**: the Mg²⁺-chelating Asp is replaced by Asn — a canonical pseudokinase-defining substitution |
| MAPK activation-loop T-x-Y | LT**E**Y (Thr-Glu-Tyr dual phosphoacceptor) | *absent* (no TxY at the aligned position) | The MAPK-defining TEY dual-phosphorylation motif is **not present** in KDX1 |

**Conclusion (inline domain reasoning):** KDX1/Mlp1 is a **degenerate protein-kinase-fold
protein / pseudokinase**. The DFG Asp→Asn substitution removes the essential Mg²⁺-coordinating
residue, and the HRD Arg (which orients the catalytic loop) is also lost. Although the fold and
the catalytic Asp (D153) are retained, loss of the DFG aspartate is on its own strongly
predictive of loss of Mg-ATP–dependent phosphotransfer. In addition, the MAPK TEY
activation-loop dual-phosphorylation motif is absent, so KDX1 cannot be activated as a canonical
MAP kinase the way SLT2 is. This structural prediction is **directly confirmed by the
literature**, which repeatedly and explicitly calls Mlp1 a "catalytically inactive pseudokinase"
(see below). UniProt still carries EC 2.7.11.1 and Ser/Thr-kinase MF terms by family homology
(PROSITE PRU00159), but these are family-propagated, not KDX1-specific evidence.

NB: UniProt annotates K55, not K54, as the ATP-binding Lys; the alignment above shows SLT2 has
the classic "VAIKK" (two lysines) whereas KDX1 has "VAIRK", but the functionally invariant β3
lysine is conserved in both. So the ATP-binding lysine is not the degenerate element; the DFG
Asp and HRD Arg are.

## What is KNOWN about KDX1/Mlp1 (with provenance)

1. **Mlp1 is a catalytically inactive pseudokinase paralog of Mpk1/Slt2.** Stated explicitly
   in multiple Levin-lab papers:
   - [PMID:18268013 "We show that the MAPK of this pathway (Mpk1) and its pseudokinase paralog (Mlp1) use a noncatalytic mechanism to activate transcription of the FKS2 gene."]
   - [PMID:20641022 "Induction was only partially dependent on the Mlp1 pseudokinase (Figure 2), a catalytically inactive paralog of Mpk1 (Kim et al., 2008)."]
   - [PMID:35420390 "the Swi4/Swi6 activation is noncatalytic and triggered by the binding of phosphorylated forms of both Slt2 and a catalytically inactive pseudokinase (Mlp1)."]

2. **Mlp1 acts non-catalytically with SBF (Swi4/Swi6) to drive FKS2 (and related genes)
   transcription under cell wall stress.** Activated (phosphorylated) Mpk1 *or* Mlp1 binds Swi4
   and confers DNA-binding ability, then recruits Swi6.
   - [PMID:18268013 "Activated (phosphorylated) Mpk1 and Mlp1 were detected in a complex with Swi4 and Swi6 at the FKS2 promoter."]
   - [PMID:20641022 "the binding of activated (phosphorylated) Mpk1, or its pseudokinase paralog, Mlp1, to the Swi4 transcription factor. This dimer binds to the FKS2 promoter, but requires the further binding of the Swi6 transcriptional activator for transcriptional initiation."]
   - The same non-catalytic mechanism drives CHA1, YKR013w, YLR042c [PMID:20641022 "a common mechanism that involves activation of Mpk1 and Mlp1 to engage Swi4 and Swi6."].

3. **Mlp1 is itself a transcriptional target of the CWI pathway (Mpk1→Rlm1), i.e. its
   expression is induced by cell wall stress**, which is why it is only partially required
   (little Mlp1 present unless the pathway is on).
   - [PMID:20641022 "The greater dependence on Mpk1 over Mlp1 results from the fact that MLP1 is transcriptionally induced by Mpk1 through the Rlm1 factor (Jung and Levin, 1999; Jung et al., 2002). Therefore, in the absence of Mpk1, very little Mlp1 is present"].
   - Mlp1 protein "accumulated in large amounts when cell wall integrity was compromised" and is "almost undetectable under normal growth conditions" — the basis of the MLP1-promoter cell-wall-stress biosensor [PMID:18055054 "One of these activated genes, namely MLP1/YKL161c, is an ideal indicator of cell wall perturbations, Mlp1p, being almost undetectable under normal growth conditions, accumulated in large amounts when cell wall integrity was compromised."].

4. **Mlp1 physically associates with the transcription factor Rlm1** and genetically
   contributes to Rlm1-dependent output; the original identification was as an Rlm1-associated
   protein in a two-hybrid screen. The 1997 paper carefully calls it a "MAP kinase-like kinase"
   (not a kinase) and shows genetic additivity with mpk1Δ.
   - [PMID:9111331 "We identified a Mpk1-like protein kinase, Mlp1, as an Rlm1-associated protein by using the yeast two-hybrid system."]
   - [PMID:9111331 "the activity of Rlm1 is regulated independently by Mpk1 MAP kinase and the Mlp1 MAP kinase-like kinase."]
   - [PMID:9111331 "Overexpression of MLP1 suppresses the caffeine-sensitive phenotype of the bck1 delta mutation."]
   - UniProt SUBUNIT: "Interacts with RLM1" [uniprot P36005, ECO:0000269|PubMed:9111331].

5. **Mlp1 functionally partially overlaps with (is redundant with) Mpk1 in the non-catalytic
   SBF branch**; loss of both, but not either alone, abolishes non-catalytic FKS2/CHA1/…
   induction. [PMID:20641022 "all induction was blocked in an mpk1Δ mlp1Δ double mutant, reflecting the partial overlap in function of Mpk1 and Mlp1 in this context."]

6. **Mlp1 appears in a global kinase/phosphatase interaction (KPI) network** (large-scale
   MS/AP-MS study), the basis for the ISS MF annotation transferred from Slt2.
   [PMID:20489023] (abstract-only; the SGD ISS annotation GO:0004674 with:SGD:S000001072
   (=SLT2) is a family/paralog inference from Slt2, NOT direct demonstration of KDX1 catalysis.)

## What is NOT known about KDX1/Mlp1 (knowledge gaps)

- **Does Mlp1 have any residual catalytic (kinase) activity in vivo?** The consensus is NO
  (pseudokinase; DFG→NFG; the community name is "kinase dead"). No study demonstrates
  Mlp1-catalyzed phosphotransfer on a physiological substrate. The UniProt EC 2.7.11.1 /
  Ser-Thr-kinase / ATP-binding annotations are family-homology propagations. (Whether it even
  binds ATP/nucleotide is untested; the β3 Lys is present, so ATP binding is not excluded, but
  Mg-ATP catalysis is predicted lost.)
- **What are Mlp1's direct partners/substrates beyond Swi4 and Rlm1?** Its non-catalytic role
  is a scaffold/adaptor at SBF-dependent promoters, but a complete interaction/target set is
  unknown.
- **What is Mlp1's non-redundant (unique) role vs Mpk1?** In every characterized context Mlp1
  is only *partially* required and overlaps with Mpk1; a phenotype uniquely dependent on Mlp1
  (with Mpk1 intact) has not been clearly defined. mlp1Δ single mutants have subtle phenotypes.
- **The cell-cycle / CDK-holoenzyme IBA annotations** (G1/S, G2/M, cyclin-dependent kinase
  holoenzyme, CDK activity) are phylogenetic propagations from the broad PTHR24055 MAPK/CDK
  family tree and are NOT supported by any KDX1-specific experiment; there is no evidence KDX1
  is a cell-cycle CDK. These are over-annotations for this pseudokinase.

## Annotation-review reasoning summary

- MF kinase terms (protein kinase activity, protein Ser/Thr kinase activity ×2, protein serine
  kinase activity, cyclin-dependent kinase activity): all propagated (IEA InterPro/ARBA/RHEA/EC,
  ISS from Slt2, IBA). Given the pseudokinase evidence, these are over-annotations →
  MARK_AS_OVER_ANNOTATED (or MODIFY toward a non-catalytic MF). Not REMOVE outright for the
  family-level ones since the fold is real, but the catalytic claim is not KDX1-supported.
- ATP binding (IEA): the β3 Lys is intact so ATP binding is plausible, but untested and
  family-propagated → KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED (not a core function).
- CDK holoenzyme / G1/S / G2/M / regulation of cell cycle / CDK activity (IBA): wrong-branch
  phylogenetic over-propagation from the MAPK/CDK superfamily; no yeast KDX1 evidence →
  MARK_AS_OVER_ANNOTATED.
- nucleus (IBA), cytoplasm (IBA): plausible; Mlp1 acts at promoters (nucleus) with SBF and is a
  cytoplasmic-then-nuclear MAPK-like protein. KEEP_AS_NON_CORE (localization, not core function).
- signal transduction (IBA, IEA) / fungal-type cell wall biogenesis (IEA ARBA): correct in
  spirit but general; KDX1 acts in the cell-integrity MAPK cascade / CWI transcriptional output
  → KEEP_AS_NON_CORE or MODIFY toward cell integrity MAPK cascade (GO:0000196).
- ND placeholders (GO:0008150, GO:0005575): uninformative root placeholders → REMOVE per
  standard handling (superseded by specific annotations).

## Candidate GO terms for core_functions (validated ids)

- MF: **GO:0140297** DNA-binding transcription factor binding (binds Swi4) — non-catalytic scaffold role.
- BP: **GO:0000196** cell integrity MAPK cascade (mentions SLT2 in its definition).
- (proposed/alt MF: GO:0003713 transcription coactivator activity — definition fits the
  Swi4-binding/DNA-binding-conferring role well.)
