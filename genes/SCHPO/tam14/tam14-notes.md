# tam14 (SPCC330.20 / G2TRT3) — curation notes

Journal-style notes for the AI GO-annotation review of *S. pombe* tam14. Inline provenance
throughout as `[SOURCE "verbatim supporting text"]`.

## Identity (verified)

- UniProt **G2TRT3**, `TAM14_SCHPO`, 70 aa, Swiss-Prot reviewed.
  - RecName **Protein tam14**; AltName **Transcripts altered in meiosis protein 14**.
  - Gene `Name=tam14; ORFNames=SPCC330.20` (chromosome III).
  - `PE 2: Evidence at transcript level` (no protein-level evidence).
  - [file:SCHPO/tam14/tam14-uniprot.txt]
- PomBase: gene name **tam14**, product **"ER stress associated protein Tam14"**,
  characterisation status **"biological role inferred"** (i.e. not experimentally
  characterised in fission yeast; role assigned by orthology).
  [PomBase API SPCC330.20, retrieved 2026-07]

## Family / domain reasoning (verified — this is a REAL, conserved family)

- Pfam **PF06624 (RAMP4)**; InterPro **IPR010580 ("ER stress-associated")**.
  [file:SCHPO/tam14/tam14-uniprot.txt]
- UniProt: `SIMILARITY: Belongs to the RAMP4 family. {ECO:0000305}.`
- **Orthologs (curated, reciprocal — PomBase):**
  - Human **SERP1** (HGNC:10759) and **SERP2** (HGNC:20607)
  - *S. cerevisiae* **YSY6** (YBR162W-A)
  - *S. japonicus* SJAG_03611
  [PomBase API SPCC330.20]
- The RAMP4/SERP1 family is a genuine, broadly conserved eukaryotic family: mammalian
  RAMP4/SERP1, budding-yeast Ysy6, and even *Candida albicans* SERP1 have been studied.
  This is materially DIFFERENT from the sibling gene tam10, a fission-yeast-lineage
  "sequence orphan" whose ISS transfers were rejected. tam14's family placement rests on
  a curated, reciprocal ortholog set, so its ER-membrane localisation inference is
  well-grounded even though no pombe-specific function has been measured.

### Domain architecture (from UniProt features)
- CHAIN 1..70 (Protein tam14)
- TRANSMEM 45..65 "Helical" (ECO:0000255) — a single C-terminal transmembrane helix
- REGION 1..20 "Disordered" / COMPBIAS 1..19 "Polar residues" — short N-terminal
  disordered, polar-biased segment
- Architecture = short cytosolic/lumenal N-terminus + single C-terminal TM helix. This
  tail-anchored-like, single-pass topology is exactly the RAMP4/SERP1 architecture (a
  small Sec61-translocon-associated single-span ER membrane protein), consistent with the
  family assignment.
  [file:SCHPO/tam14/tam14-uniprot.txt]

## The mammalian ortholog (Q9R2C1) — source of the ISS/ISO function claims

- Q9R2C1 = **SERP1_RAT** (rat Serp1 / Ramp4). RAMP4 family; ER membrane; single-pass.
  UniProt FUNCTION (verbatim): "Interacts with target proteins during their translocation
  into the lumen of the endoplasmic reticulum. Protects unfolded target proteins against
  degradation during ER stress." Keywords include "Unfolded protein response".
  [UniProt Q9R2C1, retrieved 2026-07]
- Mammalian SERP1/RAMP4 biology (background, NOT measured for tam14):
  - Yamaguchi et al. 1999 (J Cell Biol; PMID:10601334): "Stress-Associated Endoplasmic
    Reticulum Protein 1 (Serp1)/Ribosome-Associated Membrane Protein 4 (Ramp4) Stabilizes
    Membrane Proteins during Stress and Facilitates Subsequent Glycosylation"; interacts
    with Sec61alpha/Sec61beta and calnexin.
  - Park et al. 2006 (MCB; PMID:16481402): SERP1/RAMP4 deletion → ER stress; SERP1-/- mice
    show growth retardation, increased mortality, impaired glucose tolerance.
  These establish the FAMILY function in mammals; they do NOT establish tam14's function
  in *S. pombe*. The tam14 UniProt FUNCTION comment is transferred `By similarity`
  (`ECO:0000250|UniProtKB:Q9R2C1`), not observed in pombe.

## Discovery / the ONLY pombe-specific experimental evidence

- tam14 is one of 14 "transcripts altered in meiosis" genes (tam1–tam14) newly annotated by
  Bitton et al. 2011 (Genetics; PMID:21270388), a proteogenomic/comparative reappraisal.
  - [PMID:21270388 "We refer to the novel protein-coding genes with no apparent induction
    in meiosis as new1–new25 , and the 14 genes with t ranscripts a ltered in m eiosis as
    tam1–tam14"]
  - [PMID:21270388 "Fourteen transcripts were differentially expressed during meiosis."]
- CRITICAL: tam14 was NOT among the seven genes selected for deletion phenotyping. The
  functionally assessed set was tam2, new1, new5, tam7, new8, tam11, new21
  [PMID:21270388 "three criteria were used to select seven genes ( tam2 , new1 , new5 ,
  tam7 , new8 , tam11 , and new21 ) for functional assessment"]. So NO tam14 deletion
  phenotype was reported, and no meiotic function was demonstrated — only differential
  meiotic transcript abundance. Meiotic expression change alone does NOT establish a
  meiotic biological process (correlation, not function).
- UniProt INDUCTION: "Differentially expressed during meiosis.
  {ECO:0000269|PubMed:21270388}." — this is an expression, not function, statement.

## GOA annotations to review (6 rows; tam14-goa.tsv)

1. GO:0005783 endoplasmic reticulum (CC) — IEA, GO_REF:0000002, InterPro:IPR010580.
   Domain(family)-based ER localisation. Reasonable but generic; the more specific ER
   membrane term below is preferable.
2. GO:0005789 endoplasmic reticulum membrane (CC) — IEA, GO_REF:0000044,
   UniProtKB-SubCell:SL-0097. From SUBCELL mapping (ultimately the SERP1 By-similarity
   location). Well-grounded by the single TM helix + RAMP4 family. KEEP (core CC).
3. GO:0016020 membrane (CC) — IEA, GO_REF:0000044, UniProtKB-SubCell:SL-0162. Generic
   parent of ER membrane; redundant/over-general → MARK_AS_OVER_ANNOTATED.
4. GO:0003674 molecular_function (MF root) — ND, GO_REF:0000015, PomBase. Correct
   placeholder: no MF experimentally known and no MF term is confidently transferable
   (SERP1's "chaperone-like translocon-associated" activity has no clean GO MF term).
   ACCEPT (honest MF-dark placeholder).
5. GO:0005789 endoplasmic reticulum membrane (CC) — ISS, GO_REF:0000024, UniProtKB:Q9R2C1.
   Curator sequence-similarity transfer from rat SERP1. Duplicate of #2 but with the
   stronger ISS evidence. KEEP.
6. GO:0016020 membrane (CC) — ISS, GO_REF:0000024, UniProtKB:Q9R2C1. Over-general parent
   → MARK_AS_OVER_ANNOTATED (same reasoning as #3).

Note the UniProt DR block also lists GO:0006986 "response to unfolded protein" (IEA,
UniProtKB-KW) — but this is NOT in the QuickGO goa.tsv snapshot (KW-derived GO may have
been retired from GOA), so it is not in existing_annotations. PomBase itself annotates the
BP "endoplasmic reticulum unfolded protein response" by orthology.

## KNOWN vs NOT-known

KNOWN (evidence-supported):
- Bona fide, meiotically-regulated protein-coding gene [PMID:21270388].
- Genuine RAMP4/SERP1-family, single-pass (C-terminal TM) small ER-membrane protein, by
  curated reciprocal orthology (human SERP1/SERP2; Sc YSY6) + Pfam PF06624.
- Differentially expressed during meiosis; low abundance (~5 copies/cell); phosphorylated
  (S8, T6) and ubiquitinylated (K18) per PomBase modification data.

NOT known (the gaps):
- No experimentally determined molecular function IN *S. pombe* — the SERP1-family
  translocon-associated/UPR "chaperone-like" activity is a `By similarity` transfer, never
  assayed in fission yeast. (And even in mammals the activity has no clean GO MF term.)
- No pombe deletion phenotype reported; tam14 was excluded from the tam-gene functional
  assessment [PMID:21270388]. Whether it has any meiotic role (vs incidental meiotic
  expression) is untested.
- No direct localisation data (GFP/immuno) in pombe; ER-membrane placement is
  orthology/topology inference.
- The HT-Y2H interactors (Cut11, Lem2, Ima1 — nuclear-envelope/INM proteins) are
  unvalidated single-method hits and do not by themselves establish function.

## Curation plan

- description: project-independent — RAMP4/SERP1-family single-pass ER-membrane protein,
  meiotically regulated, ortholog set, function inferred not measured. No curation
  commentary.
- CC ER membrane (ISS + IEA): KEEP as core location. ER (IEA/InterPro): ACCEPT/keep as
  non-core (more general than ER membrane). membrane (x2): MARK_AS_OVER_ANNOTATED (root).
- MF root ND: ACCEPT (honest MF-dark).
- core_functions: minimal — the confident statement is CC (ER membrane, RAMP4 family);
  do NOT assert an MF term (no defensible, branch-correct MF for the SERP1 activity).
- knowledge_gaps (REQUIRED): MF-dark biology gap (family known, pombe activity unmeasured)
  + BP gap (meiotic role untested despite the gene's very name).
- reference_review for the two verified PMIDs.

## Falcon deep research (completed 2026-07-06; genuine Edison output, 17 citations)

The falcon report [file:SCHPO/tam14/tam14-deep-research-falcon.md] independently reaches the
same conclusions and adds mechanistic family context (verified against my own UniProt/PomBase
work). Key verbatim points:
- Family/orthologs: RAMP4 (PF06624) = mammalian RAMP4/SERP1 and Sc Ysy6; tam14 predicted to be
  "a **small accessory component of the Sec61 translocon** at the endoplasmic reticulum
  membrane". Mechanistic detail from Lewis et al. 2024 (eLife) cryo-EM of the
  ribosome-translocon (RAMP4 intercalates the Sec61 lateral gate, "surrogate signal peptide")
  and Pool 2009 (JCB) TM-segment-triggered RAMP4 recruitment. RAMP4 is a tail-anchored ER
  membrane protein.
- Evidence level: "rests primarily on **domain and family-level inference** from
  well-characterized orthologs ... but no targeted deletion, localization, or biochemical study
  has been published specifically for tam14/SPCC330.20." Confidence: "Moderate for family-level
  annotation, low for gene-specific detail".
- tam14 "was not among the seven genes selected for functional knockout analysis in the original
  study, so no deletion phenotype has been reported specifically for this gene."
- "No direct localization data for tam14 in *S. pombe* cells has been reported."
- Important pombe-specific caveat: "*S. pombe* lacks Hac1/XBP1 orthologs and instead relies
  primarily on Ire1-dependent mRNA decay (RIDD)" — so the mammalian ER-stress-induction /
  UPR-transcriptional paradigm for RAMP4/SERP1 may not transfer to fission yeast.
- "the meiotic expression change alone does not imply a meiosis-specific biochemical function".

Note: falcon cites Lewis et al. 2024 and Pool 2009 by DOI/preprint. These are mammalian
mechanism papers (not tam14). I anchor gene-specific "unknown" provenance to the falcon file:
and to cached PMID:21270388; I do NOT add the mammalian DOIs as review references (cannot cache
/ verify their full text here, and they are not about tam14).
