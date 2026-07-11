# THI22 (YPR121W, Q06490) — curation notes

Journal of research for the AI GO-annotation review. THI22 is an understudied ("dark")
*S. cerevisiae* gene: a member of the three-gene thiaminase-2 / HMP-P-kinase family
(THI20/THI21/THI22). The central curation problem is that THI22 is highly homologous to
the biochemically characterized paralogs THI20 and THI21, yet no enzymatic activity has
been demonstrated for it, and it is dispensable for thiamine biosynthesis. All
THI22-specific claims must be separated carefully from what is known only for THI20/THI21.

## Identity and family placement

- UniProt: Q06490 (THI22_YEAST). Systematic name YPR121W. SGD:S000006325.
- 572 aa. UniProt annotates a signal peptide (1-19) and chain (20-572); predicted
  Secreted (SL-0243) — this is a computational SubCell/SignalP prediction (ECO:0000255 /
  ECO:0000305), not experimentally demonstrated. [file:genes/yeast/THI22/THI22-uniprot.txt]
- Family: PANTHER PTHR20858 (PHOSPHOMETHYLPYRIMIDINE KINASE), subfamily PTHR20858:SF17
  ("HYDROXYMETHYLPYRIMIDINE/PHOSPHOMETHYLPYRIMIDINE KINASE THI20-RELATED"). All three
  yeast paralogs are in SF17: THI20 (Q08224, 551 aa), THI21 (Q08975, 551 aa), THI22
  (Q06490, 572 aa). [file:interpro/panther/PTHR20858/PTHR20858-entries.csv]
- Two-domain (fused) architecture, one gene fusion event ancestral to the family:
  - N-terminal HMP/HMP-P kinase domain (ribokinase-like; Pfam PF08543 Phos_pyr_kin;
    CDD cd01169 HMPP_kinase; TIGR00097 HMP-P_kinase). Corresponds to bacterial ThiD.
  - C-terminal TenA / thiaminase-II-like domain (Pfam PF03070 TENA_THI-4; CDD cd19367
    TenA_C_ScTHI20-like; TIGR04306 salvage_TenA; InterPro IPR027574 Thiaminase_II).
    Corresponds to bacterial TenA (thiamine-salvage thiaminase II).
  [file:genes/yeast/THI22/THI22-uniprot.txt]

## KNOWN (experimentally established) — but note attribution

For the FAMILY / paralogs (NOT necessarily THI22):
- Two of the three family members (THI20 = YOL055c and THI21 = YPL258c) are isofunctional
  and encode an HMP-P kinase (EC 2.7.4.7), an activity required for the final steps of
  thiamine biosynthesis in yeast.
  [PMID:10383756 abstract, "we demonstrate that two members are isofunctional and encode a
  hydroxymethylpyrimidine phosphate (HMP-P) kinase (EC 2.7.4.7), an activity required for
  the final steps of thiamine biosynthesis, whose genes were not previously known in yeast"]
- THI20 is a trifunctional enzyme: HMP kinase (EC 2.7.1.49) + HMP-P kinase (EC 2.7.4.7) +
  thiaminase II (EC 3.5.99.2), the last activity degrading thiamine to HMP for salvage.
  [UniProt Q08224, CATALYTIC ACTIVITY / FUNCTION; ECO:0000269|PubMed:15967475]
- The C-terminal domain of the family proteins is NOT required for HMP-P kinase activity;
  its function was unresolved at the time of the 1999 paper.
  [PMID:10383756 abstract, "The function of the carboxy-terminal part of the proteins is
  not yet understood, but it is not required for HMP-P kinase activity"]
- All three genes are co-regulated and induced by thiamine absence.
  [PMID:10383756 abstract, "Expression of all three genes is regulated in the same way";
  UniProt Q06490 INDUCTION "By absence of thiamine", ECO:0000269|PubMed:10383756]

Specifically for THI22 (what the primary literature actually says):
- THI22 is NOT required for thiamine biosynthesis (dispensable; single deletion has no
  thiamine-auxotrophy phenotype in the redundant family context).
  [UniProt Q06490 FUNCTION "Is not required for thiamine biosynthesis",
  ECO:0000269|PubMed:10383756]
- No HMP-P kinase activity could be demonstrated for THI22, in contrast to THI20/THI21.
  [UniProt Q06490 CAUTION "Although highly homologous to the 2 other thiaminase-2 family
  members THI20 and THI21 in yeast, no hydroxymethylpyrimidine phosphate kinase activity
  could be demonstrated for this protein", ECO:0000305]
- THI22 expression is induced by absence of thiamine (like the paralogs).
  [UniProt Q06490 INDUCTION, ECO:0000269|PubMed:10383756]

## NOT known / open (THI22-specific knowledge gaps)

- Whether THI22 has ANY catalytic activity in vivo (HMP kinase, HMP-P kinase, or
  thiaminase II). The 1999 assay failed to detect HMP-P kinase; other activities untested.
- Whether the failure to detect activity reflects a genuinely inactive protein, a folding/
  expression problem in the assay system, a different substrate, or a regulatory/salvage
  role distinct from the biosynthetic kinase step.
- The true subcellular location. UniProt lists "Secreted" from a signal-peptide/SubCell
  prediction, but the paralogs THI20/THI21 act cytosolically in thiamine metabolism, and
  the phylogenetic (IBA) annotation places THI22 in the cytosol. The secretion claim is
  computational only and is biologically surprising for a thiamine-pathway enzyme.
- Why the cell retains a third, apparently redundant/inactive paralog: possible functions
  include a conditional/cryptic activity, a dosage or buffering role, a role under specific
  stress/nutrient conditions, or ongoing pseudogenization (evolutionary relic).

## Inline domain reasoning (done in this review, not from an external tool)

Pairwise global alignment of THI22 (Q06490) vs THI20 (Q08224) computed here with Biopython
(globalms, match 2 / mismatch -1 / gap-open -5 / gap-extend -0.5):
- 76.4% identity over aligned positions — very high; THI22 is a bona fide close paralog.
- The THI20 experimentally/inferred functional residues are ALL conserved in THI22:
  - HMP substrate-binding Gln (THI20 Q64, N-terminal kinase domain) = THI22 Q86.
  - Thiaminase-II nucleophile Cys (THI20 ACT_SITE C468) = THI22 C489.
  - Thiaminase-II proton-donor Glu (THI20 ACT_SITE E540) = THI22 E561.
  (THI22 positions are offset by ~21-22 residues because of its N-terminal signal-peptide
  extension.)
- The ribokinase-family glycine-rich phosphate-binding motif is present in THI22
  (…IAGSDSSGGAGV…, ~res 52-63; THI20 has …AGTDPSGGAGIE…) and the GGHIP kinase motif is
  present (THI22 res ~222).

Interpretation: THI22 is NOT a residue-dead pseudoenzyme — its catalytic and substrate-
binding residues are intact. This makes the observed lack of demonstrable HMP-P kinase
activity [PMID:10383756] a genuine biological puzzle rather than an obvious consequence of
lost catalytic machinery. Because the catalytic residues are conserved, a domain-based
"pseudoenzyme" REMOVE of the kinase MF terms is NOT justified; but neither is a confident
ACCEPT of demonstrated activity, since the one direct assay failed for THI22. The honest
position is that the kinase/thiaminase MF terms are phylogenetically/InterPro-inferred
(IBA/IEA) and plausible on sequence grounds, but THI22-specific activity is unproven and
partially contradicted by the one experiment that tested it.

## Annotation-by-annotation plan (see YAML for final actions)

GOA has 12 annotations:
1. GO:0005829 cytosol (IBA) — plausible for a thiamine-pathway enzyme; paralogs cytosolic.
   KEEP_AS_NON_CORE (location, phylogenetic).
2. GO:0008902 hydroxymethylpyrimidine kinase activity (IBA) — HMP→HMP-P (EC 2.7.1.49).
   Family activity; THI22-specific unproven. KEEP_AS_NON_CORE with caveat (not core, not
   demonstrated for THI22).
3. GO:0008972 phosphomethylpyrimidine kinase activity (IBA) — HMP-P→HMP-PP (EC 2.7.4.7);
   this is exactly the activity the 1999 paper FAILED to demonstrate for THI22.
   MARK_AS_OVER_ANNOTATED (directly tested and not detected for THI22).
4. GO:0009228 thiamine biosynthetic process (IBA) — THI22 shown NOT required for thiamine
   biosynthesis. MARK_AS_OVER_ANNOTATED.
5. GO:0005576 extracellular region (IEA, SubCell) — computational from signal peptide;
   biologically implausible for a thiamine-metabolism enzyme; conflicts with cytosol IBA.
   MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE with strong caveat.
6. GO:0006772 thiamine metabolic process (IEA, InterPro) — general BP; defensible at the
   family level. KEEP_AS_NON_CORE.
7. GO:0008972 phosphomethylpyrimidine kinase activity (IEA, InterPro) — duplicate MF from
   InterPro; same caveat as #3. MARK_AS_OVER_ANNOTATED.
8. GO:0009228 thiamine biosynthetic process (IEA) — same as #4. MARK_AS_OVER_ANNOTATED.
9. GO:0050334 thiaminase activity (IEA, InterPro, IPR027574 Thiaminase_II) — C-terminal
   TenA domain; catalytic Cys/Glu conserved in THI22. Plausible on sequence; unproven for
   THI22. KEEP_AS_NON_CORE (domain-supported family activity).
10. GO:0003674 molecular_function (ND) — root, no data. ACCEPT (ND placeholder).
11. GO:0005575 cellular_component (ND) — root, no data. ACCEPT (ND placeholder).
12. GO:0009228 thiamine biosynthetic process (IEP, PMID:10383756, SGD) — experimental
    annotation from the primary paper (induction by thiamine absence = IEP "expression
    pattern"). Per rules, do NOT REMOVE an experimental annotation. IEP reflects that the
    gene is thiamine-regulated, which is genuinely established; but the gene is not required
    for biosynthesis. KEEP_AS_NON_CORE (thiamine-regulated; involvement not core), defer to
    SGD curator on the experimental IEP.

## Update (review completed) — falcon corroboration and final actions

Falcon/Edison deep research completed (THI22-deep-research-falcon.md, 21 citations, ~1476s).
It independently corroborates the review's central conclusions:
- "The function of the third member of the same gene family, THI22, is unknown at present"
  (attributed to Kowalska & Kozik 2008 in the report).
- THI20/THI21 are the characterized HMP/HMP-P kinase + thiaminase-II enzymes; THI22's specific
  biochemical function is unresolved and inferred only from homology/domain annotation.
- THI22's predicted signal peptide distinguishes it from cytoplasmic THI20 — falcon raises the
  same hypothesis captured in the localization knowledge gap (possible periplasmic/extracellular
  salvage or degradation role), and notes Huh et al. 2003 GFP screen did not give a clear THI22
  localization.
- THI22 is part of the thiamine (THI) regulon, thiamine-regulated — matches the IEP annotation.
Falcon citations use internal source keys (not PMIDs), so per project memory no verbatim
supporting_text from the falcon report is used to ground annotations; all annotation quotes are
anchored to PMID:10383756 (verbatim, whitespace/case verified) and the inline bioinformatics
RESULTS.md.

Final action breakdown over 12 GOA annotations:
- ACCEPT: 2 (GO:0003674 root MF ND; GO:0005575 root CC ND)
- KEEP_AS_NON_CORE: 4 (GO:0005829 cytosol IBA; GO:0008902 HMP kinase IBA; GO:0006772 thiamine
  metabolic process IEA; GO:0050334 thiaminase activity IEA)
- MARK_AS_OVER_ANNOTATED: 6 (GO:0008972 HMP-P kinase IBA+IEA; GO:0009228 thiamine biosynthetic
  process IBA+IEA+IEP; GO:0005576 extracellular region IEA)
- REMOVE: 0 (catalytic residues intact per alignment; experimental IEP not removed per guidelines)

Inline bioinformatics (THI22-bioinformatics/): reproducible Biopython alignment of THI22 vs THI20
confirms 76.4% identity and conservation of all THI20 functional residues (HMP-binding Q64->Q86,
thiaminase-II C468->C489, E540->E561) — THI22 is NOT a residue-dead pseudoenzyme, which is why
no domain/pseudoenzyme-based REMOVE was applied to the kinase/thiaminase MF terms.
