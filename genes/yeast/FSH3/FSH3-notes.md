# FSH3 (YOR280C) research notes

Gene: FSH3 / YOR280C, *Saccharomyces cerevisiae* (S288C), UniProt Q99369, SGD S000005806.
Name: "Family of Serine Hydrolases 3". 266 aa. UniProt EC=3.1.-.- (esterase, generic).
This is a functionally dark gene: a putative serine hydrolase of **unknown physiological
substrate / reaction / in-vivo role**.

## Summary of what is KNOWN vs NOT KNOWN

KNOWN (defensible):
- Belongs to the α/β-hydrolase fold, AB-hydrolase-3 family; Pfam FSH1 (PF03959),
  InterPro AB_hydrolase_fold (IPR029058) + FSH-like domain (IPR005645); PANTHER family
  PTHR48070 subfamily SF6 "ESTERASE OVCA2"; SCOP/SUPFAM alpha/beta-Hydrolases (SSF53474).
- Has an intact, canonical serine-hydrolase catalytic triad (Ser-Asp-His) with the
  nucleophile in a classic GXSXG motif (see domain analysis below).
- Was directly detected as an *active* serine hydrolase by activity-based protein profiling
  (chemical + computational proteomics) in yeast — i.e. the catalytic serine is chemically
  reactive in vivo [PMID:14645503].
- Transcriptionally induced as a target of the Crt1/RFX1 repressor (DNA-damage-checkpoint
  effector) [PMID:15494396], and induced by H2O2/oxidative stress [PMID:30776074].
- Localizes to the peroxisome (IDA, SGD) [PMID:36164978]; is one of a set of newly identified
  peroxisomal proteins of unknown molecular function.
- Overexpression phenotypes: overexpression causes an apoptotic/ROS phenotype dependent on
  NUC1 [PMID:30776074], and overexpression produces the strongest lipidome change (reduction
  of phosphatidylcholine, PC) among a panel of dark peroxisomal proteins [PMID:36164978].

NOT KNOWN (the gaps — primary deliverable):
- The physiological substrate and the specific reaction it catalyzes. UniProt states
  "Serine hydrolase of unknown specificity" and assigns only EC 3.1.-.- (uncommitted esterase).
- The in-vivo biological role / pathway. Single deletion has no reported *growth* phenotype
  under standard conditions, but a double-deletion (Δlpx1Δfsh3) shows reduced peroxisomal
  β-oxidation activity [PMID:36164978], implicating FSH3 (redundantly with Lpx1) in
  peroxisomal fatty-acid β-oxidation. The specific molecular step/substrate remains unassigned.
- Functional redundancy with paralogs FSH1 and FSH2 (double-deletion data below suggest
  partial redundancy / opposing roles but do not assign a molecular function).
- Whether the PC reduction on overexpression reflects a direct enzymatic activity on a
  glycerophospholipid substrate, or an indirect consequence.

## Domain / catalytic-triad analysis (inline, from FSH3-uniprot.txt sequence)

UniProt annotates three "Charge relay system" active-site residues (by similarity, ECO:0000250):
- ACT_SITE 117, 180, 209.

Mapping onto the 266-aa sequence (verified computationally, see below):
- Position 117 = **Ser** (nucleophile), embedded in **G115-F116-S117-Q118-G119 = GFSQG**, a
  textbook **GXSXG** "nucleophile elbow" motif of α/β-hydrolases.
- Position 180 = **Asp** (acid of the triad).
- Position 209 = **His** (base of the triad).

So FSH3 carries a **complete, canonical Ser-Asp-His serine-hydrolase catalytic triad** on an
α/β-hydrolase scaffold, with the nucleophilic serine in the diagnostic GXSXG motif. The triad
is intact (this is NOT a pseudoenzyme). Consistent with this, activity-based profiling detected
FSH3 as a *catalytically active* serine hydrolase in vivo [PMID:14645503]. This makes a generic
serine-hydrolase molecular function (GO:0017171 serine hydrolase activity) domain-defensible;
a *specific* substrate/reaction remains a genuine gap.

Verification (residue identity + motif), reproducible:
```python
seq = ("MSEKKKVLMLHGFVQSDKIFSAKTGGLRKNLKKLGYDLYYPCAPHSIDKKALFQSESEKG"
       "RDAAKEFNTSATSDEVYGWFFRNPESFNSFQIDQKVFNYLRNYVLENGPFDGVIGFSQGA"
       "GLGGYLVTDFNRILNLTDEQQPALKFFISFSGFKLEDQSYQKEYHRIIQVPSLHVRGELD"
       "EVVAESRIMALYESWPDNKRTLLVHPGAHFVPNSKPFVSQVCNWIQGITSKEGQEHNAQP"
       "EVDRKQFDKPQLEDDLLDMIDSLGKL")
assert seq[116] == "S" and seq[179] == "D" and seq[208] == "H"
import re; assert re.search(r"G.S.G", seq).start()+1 == 115  # GFSQG, Ser at 117
```

## FSH3 vs paralogs FSH1 / FSH2 and human OVCA2 (keep these separate)

*S. cerevisiae* has three FSH paralogs, all named for this "Family of Serine Hydrolases":
- **FSH1** = P38777 / YHR049W (243 aa). PANTHER subfamily **SF9** (distinct from FSH3).
  The crystal structure 1YCD is FSH1/YHR049W, "a member of the serine hydrolase family"
  (PANTHER PTHR48070 representative structure).
- **FSH2** = Q05015 / YMR222C (223 aa). PANTHER subfamily **SF6** (same subfamily as FSH3).
- **FSH3** = Q99369 / YOR280C (266 aa). PANTHER subfamily **SF6** "ESTERASE OVCA2".

So FSH3 is in the OVCA2 subfamily (SF6) together with FSH2 and human OVCA2, and is more
distantly related to FSH1 (SF9). The human ortholog is **OVCA2 (Q8WZ82)**, a candidate ovarian
tumor-suppressor esterase; OVCA2 is the source of the phylogenetic (IBA) inferences in GOA
(GOA IBA uses UniProtKB:Q8WZ82 and PANTHER:PTN000512658 as with/from). The *S. pombe* member of
this family is DYR-SCHPO / SPAC22A12.06c.

Provenance for the family framing:
- [PMID:14645503 "Three of the previously uncharacterized proteins are members of a eukaryotic
  serine hydrolase family, designated as Fsh (family of serine hydrolase), identified here for
  the first time. OVCA2, a potential human tumor suppressor, and DYR-SCHPO, a dihydrofolate
  reductase from Schizosaccharomyces pombe, are members of this family."]
- [PMID:30776074 "Family of Serine Hydrolases (FSH) members FSH1, FSH2 and FSH3 in
  Saccharomyces cerevisiae share conserved sequences with the human candidate tumor suppressor
  OVCA2."]

CAUTION: The DYR-SCHPO/DHFR association in [PMID:14645503] and the speculation in
[PMID:15494396] that "FSH3p ... may be involved in folate metabolism ... by carrying serine
hydrolase activity required for the novel metabolic pathway involving dihydrofolate reductase
(DHFR) or by directly interacting with the DHFR enzyme" is **speculation from sequence
similarity**, not experimental evidence for a FSH3 DHFR/folate function. Do not annotate folate
metabolism from this.

## Evidence by reference

### PMID:14645503 (Baxter et al. 2004, Mol Cell Proteomics) — FUNCTION (ABPP)
Activity-based/computational proteomics identifying active serine hydrolases in yeast; defines
the Fsh family and detects FSH3 as an active serine hydrolase. This is the source cited by
UniProt for FUNCTION "Serine hydrolase of unknown specificity" (ECO:0000269|PubMed:14645503).
- Supports: serine hydrolase activity (catalytically active in vivo), family definition.
- Abstract-only in cache (full_text_available: false).

### PMID:15494396 (Zaim et al. 2005, J Biol Chem) — INDUCTION (Crt1/RFX1)
FSH3 is a confirmed transcriptional target of Crt1p (RFX1), the DNA-damage-checkpoint effector.
- [PMID:15494396 "Our results indicated that FSH3, YLR345W, and NTH2 are indeed under the
  regulation of Crt1p."]
- The DHFR/folate idea here is speculative (see CAUTION above).
- Source of UniProt INDUCTION "Regulated by RFX1/CRT1".

### PMID:36164978 (Yifrach et al. 2022, EMBO J-family) — peroxisome IDA + lipidome
Systematic multi-level analysis of the peroxisome proteome. FSH3 is a newly identified
peroxisomal protein (basis of the SGD IDA C:peroxisome annotation).
- [PMID:36164978 "Lipidomic analysis on mutants of 10 newly identified peroxisomal proteins
  whose molecular function in the yeast cell is putative or unknown shows that cells
  overexpressing FSH3 had the most significant change in all conditions compared to the control
  strain, with a reduction of PC (raw data is in Dataset EV7)."]
- Supports: C:peroxisome (IDA); a lipid-metabolism-linked phenotype on overexpression
  (reduction of phosphatidylcholine). Note this is an overexpression lipidome effect, not
  proof of a direct PC-hydrolase activity.
- IMPORTANT (deletion-based phenotype, from full text): a peroxisomal β-oxidation activity
  assay of single and double deletions shows Δfsh3 contributes to β-oxidation:
  [PMID:36164978 "A β‐oxidation activity assay of Δlpx1, Δfsh3, and Δlpx1Δfsh3 strains
  supplemented with labeled 8 carbon‐ or 18 carbon‐free fatty acids in media supplemented
  with 0.5% glucose shows a significant reduction in β‐oxidation activity compared to the
  control strain and the two single mutants, suggesting an overlapping role for Fsh3 with
  Lpx1."]. Lpx1 is the peroxisomal lipase; the double mutant Δlpx1Δfsh3 (but not either
  single mutant) has reduced β-oxidation. This is a concrete deletion (loss-of-function)
  clue that FSH3 has a redundant/overlapping role in peroxisomal fatty-acid β-oxidation —
  consistent with the peroxisomal localization and the PC-reduction lipidome result. It
  refines the "no deletion phenotype" statement: single-deletion *growth* is silent, but
  a biochemical double-mutant β-oxidation phenotype exists and points to a candidate
  pathway (GO:0006635 fatty acid beta-oxidation; in yeast this is exclusively peroxisomal).
  This is why single fsh/lpx1 deletions look silent (redundancy). The molecular role of
  FSH3 in that pathway (which acyl-ester substrate it hydrolyzes) is still unassigned.

### PMID:30776074 (Gowsalya et al. 2019, FEMS Yeast Res) — overexpression apoptosis, NUC1
- [PMID:30776074 "hydrogen peroxide (H2O2) exposure increased the expression of both mRNA and
  protein levels of FSH3"] — H2O2/oxidative-stress induction.
- [PMID:30776074 "The overexpression of FSH3 in WT yeast cells caused an apoptotic phenotype,
  including accumulation of reaction oxygen species, decreased cell viability and cell death."]
- [PMID:30776074 "Our results suggest that FSH3 induced apoptosis of yeast in a NUC1 dependent
  manner."]
- [PMID:30776074 "The deletion of FSH3 improved the yeast growth rate under H2O2-induction as
  compared to WT control cells."] — deletion is not required for viability; gives a growth
  benefit under H2O2.
- [PMID:30776074 "The double deletions fsh1Δ fsh2Δ, fsh1Δ fsh3Δ and fsh2Δ fsh3Δ displayed
  increased growth compared to WT cells."] — partial redundancy / shared pathway among paralogs.

### PMID:24187129 (Ploier et al. 2013, J Biol Chem) — background on yeast peroxisomal/LD hydrolases
Screen for hydrolytic enzymes in yeast peroxisomes and lipid droplets using GXSXG-motif serine
hydrolases; identifies Ayr1p as a TG lipase and confirms Lpx1p. Provides context for the class
of GXSXG serine hydrolases acting in peroxisomal/lipid metabolism (not a FSH3-specific paper).
- [PMID:24187129 "All of these proteins contain the consensus sequence for a classical lipase
  (G X S X G motif) with a classical catalytic triad containing a nucleophile serine."]
- Relevance: contextual (LOW/MEDIUM) — supports plausibility of a peroxisomal lipid-related
  serine-hydrolase role, does not assign FSH3 a substrate.

## Annotation decisions (rationale)

- GO:0016787 hydrolase activity (IBA, MF): correct but too general. The intact Ser-His-Asp
  triad + GXSXG + ABPP reactivity support the more specific GO:0017171 serine hydrolase
  activity. MODIFY → GO:0017171.
- GO:0005777 peroxisome (IDA, PMID:36164978): ACCEPT (experimental, curator-verified).
- GO:0005634 nucleus (IBA), GO:0005737 cytoplasm (IBA): phylogenetically-inferred locations
  from the OVCA2 family. Cytoplasm is plausible/general; nucleus is not supported by the
  yeast-specific IDA evidence (which places it in peroxisome) and is a weak IBA. Keep as
  non-core (cytoplasm) / mark over-annotated (nucleus) rather than REMOVE — these are IBA, not
  experimental. FSH3 is also reported in stress granules (CD-CODE E03F929F) consistent with
  cytoplasmic pools.
- GO:0003674 molecular_function ND, GO:0008150 biological_process ND: root placeholders; REMOVE
  (superseded by informative annotations we now have / the IBA hydrolase annotation).

## Open questions / gaps (primary deliverable)
1. Physiological substrate + specific reaction (only EC 3.1.-.-; "unknown specificity"). The
   Δlpx1Δfsh3 β-oxidation phenotype nudges this toward a fatty-acyl/lipid ester substrate.
2. In-vivo biological role/pathway. Refined: single-deletion growth is silent, but a
   double-mutant (Δlpx1Δfsh3) β-oxidation defect implicates FSH3 in peroxisomal fatty-acid
   β-oxidation (GO:0006635, peroxisomal in yeast), overlapping with the lipase Lpx1. The
   precise molecular contribution is still unknown.
3. Redundancy vs paralogs and vs Lpx1: fsh double deletions grow faster [PMID:30776074],
   and Δlpx1Δfsh3 (but not single mutants) reduces β-oxidation [PMID:36164978] — redundancy
   is the likely reason single deletions look silent; molecular function still unassigned.
4. Whether peroxisomal FSH3 acts directly on a glycerophospholipid (PC) / fatty-acyl ester,
   or the PC/β-oxidation effects are indirect.
</content>
</invoke>
