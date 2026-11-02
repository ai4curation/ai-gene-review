# MAP2K2 (horse, A0A9L0SHX8) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Deep research.** `just deep-research-falcon HORSE MAP2K2 --fallback perplexity-lite` failed: falcon returned "Failed to authenticate" (403 from the Edison login endpoint), and the perplexity-lite fallback returned HTTP 401 insufficient_quota. No deep-research file was written. This review relies on the cached publications (PMID:8388392, PMID:15866172, PMID:19565474 [abstract only]), the human MAP2K2 UniProt record and review (genes/human/MAP2K2), the human falcon report, and the new gene-model analysis below.

**Identity of A0A9L0SHX8 (alternative gene model with an aberrant C-terminal exon).**
New analysis: `MAP2K2-bioinformatics/compare_horse_models_rereview.py` writes `RESULTS-rereview.md` and `results-rereview.json`, using live UniProt and Ensembl data plus the local PAINT file. The horse MAP2K2 gene, Ensembl ENSECAG00000009157 on chromosome 7, has five protein-coding models. All five are unreviewed TrEMBL entries in PANTHER PTHR47448:SF3, and no reviewed horse MAP2K2 entry exists.
- A0A9L0SHX8 is the benchmark product: transcript ENSECAT00000136538, 390 aa, 11 exons, not Ensembl canonical. Human P36507 is 400 aa. Human residues 1-363 align with 90.3% identity, so the N-terminal ERK-docking region, the ATP-binding Lys101, the HRD catalytic Asp194 and the RAF-phosphorylated Ser222/Ser226 are all retained. After human 363 (…ADLKML) the sequence diverges completely. Human 364-400 (TNHTFIKRSEVEEVDFAGWLCKTLRLNQPGTPTRTAV) is replaced by an unrelated 27-residue tail (MQAVTAPPCYVHHRRHSSALLGSPLFM). As a result:
  - The end of the kinase domain (human 362-369, PROSITE domain 72-369) keeps only 2/8 identical residues.
  - The C-terminal 370-400 segment keeps only 2/31. This segment holds the DVD docking site, "a stretch of about 20 amino acids immediately on the C-terminal side of the MAPKK catalytic domain" that MAPKKs, including MEK1, use to bind their activating MAP3Ks such as Raf-1 [PMID:15866172]. It also holds the Thr394/Thr396 phosphosites.
- The other models are also defective:
  - A0A9L0SF07 (Ensembl canonical, 494 aa) diverges at the same point and carries a long unrelated extension.
  - A0A9L0R4J0 (426 aa) diverges at the same point.
  - A0A9L0SD26 (366 aa) is truncated after human 363.
  - F6YUU0 (430 aa, the only entry with gene name MAP2K2) has the correct human-like C-terminus (30/31 identical over 370-400). Its N-terminal ~110 residues are wrong, and the Lys101 region is replaced.
- A full-length horse MEK2 matching human P36507 is therefore not represented by any single UniProt entry. It would be A0A9L0SHX8 residues 1-363 joined to the F6YUU0 C-terminal exon. A0A9L0SHX8 is best described as an alternative gene model, probably an annotation artefact or a rare 3' splice form. Its own catalytic competence is untested. Loss of the end of subdomain XI could compromise the C-lobe, and loss of the DVD would be expected to impair activation by RAF.

**Evolutionary grounding.**
- Horse ENSECAG00000009157 is in PANTHER subfamily PTHR47448:SF3 "MITOGEN-ACTIVATED PROTEIN KINASE KINASE 2" (UniProt cross-reference). It sits on horse chromosome 7, and its N-terminal 363 residues are 90% identical to human MEK2. It is the horse MAP2K2 ortholog.
- PAINT node PTN000684494 (local file interpro/panther/PTHR48013/PTHR48013-paint.tsv, eukaryote level, 29 seeds including human P36507) asserts GO:0004708 MAP kinase kinase activity and GO:0000165 MAPK cascade by IBD. Horse MAP2K2 descends from this node.
- The horse accession has no IBA rows of its own. Its GOA rows are all IEA (ARBA, UniRule, InterPro2GO, EC and inter-ontology inference).
- PAINT did not propagate any localization terms or Golgi, endosome or stress-MAPK process terms at this node. The six ARBA-derived localization/process rows on horse descend from human TAS rows citing a review article (PMID:19565474; abstract only in cache). I could not verify that these localizations or processes are MEK2 properties rather than MEK1- or ERK-pathway properties, so they stay UNDECIDED, consistent with the human review.

**Actions.**
- GO:0004708 MAP kinase kinase activity: ACCEPT (core).
- GO:0005524 ATP binding: ACCEPT.
- GO:0000166, GO:0004672, GO:0004674, GO:0016301, GO:0016740: MODIFY (to ATP binding or MAP kinase kinase activity).
- GO:0000165 MAPK cascade: MODIFY to GO:0070371 ERK1 and ERK2 cascade. MEK1/2 are the ERK1/2-specific MAP2Ks, and the human review ACCEPTs GO:0070371 from Reactome.
- Six ARBA localization/process rows: UNDECIDED.
- These are judged as gene-level claims about horse MAP2K2. The specific model's aberrant C-terminus is stated in the description, core function, questions and experiments.

**Family review (interpro/panther/PTHR47448/PTHR47448-review.yaml).** It uses A0A9L0SHX8 as the sole SF3 representative and says the "human comparison has 90.26% identity across 390 paired residues and supports MAPKK biology". This passes over the fact that the 390-residue product lacks human 364-400, including the DVD docking site. On subfamily placement there is no disagreement: all five horse MAP2K2 models are SF3. That review already records the separate PTHR47448 vs PTHR48013 source conflict (human P36507 officially PTHR48013:SF8). A full-length-like representative would be better. No horse entry qualifies, so human P36507 is the natural candidate. I did not edit the family file.

**Relative.** Human MAP2K2 P36507 (ortholog, same PANTHER SF3 per UniProt, seed of PAINT node PTN000684494). Complete review exists at genes/human/MAP2K2/MAP2K2-ai-review.yaml. The same-gene "canonical" horse entries (Ensembl-canonical A0A9L0SF07, gene-named F6YUU0) are themselves defective gene models and are not reviewed UniProt entries, so they are not proposed as the next review target.

**Modules.** modules/erk_cascade.yaml (MEK2 node, human P36507), modules/mapk_relay.yaml (generic MAP2K tier, mentions MEK1/MEK2).
