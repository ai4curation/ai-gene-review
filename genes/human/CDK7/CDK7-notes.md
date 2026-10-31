# CDK7: evidence notes

## Paired horse benchmark evidence review

The human reference supplies mechanistic evidence for the corresponding selected horse protein; the human conclusion alone is not validation of the horse sequence. The exact horse comparison is in `genes/HORSE/CDK7/CDK7-bioinformatics/RESULTS.md`. Research reports are source leads; annotation decisions cite the underlying publication or experimentally supported UniProt passages. Unresolved source-specific results retain UNDECIDED.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 file or prediction-evidence folder was opened; this review rests on the cached literature, UniProt, Reactome and PANTHER/PAINT data only.

### Identity
- P50613 is the canonical, reviewed (Swiss-Prot) human CDK7 entry, 346 aa, with the complete protein kinase domain (12-295), the proton-acceptor active site at 137 and the glycine-rich ATP-binding loop. It is not an isoform, fragment or alternative gene model. The paired horse benchmark protein is genes/HORSE/CDK7 (A0A9L0R074).

### Evolutionary placement
- UniProt places P50613 in PANTHER PTHR24056:SF0 (CYCLIN-DEPENDENT KINASE 7). The PANTHER 19.0 human classification file gives PTHR24056:SF375, which is also named CYCLIN-DEPENDENT KINASE 7. This looks like the same CDK7 subfamily under two subfamily numbers, not a biological disagreement. `interpro/panther/panther-members-overrides.tsv` pins it to SF0, and `interpro/panther/PTHR24056/PTHR24056-review.yaml` keeps human CDK7 as an "unnumbered functional group" pending SF0 vs SF375.
- All IBA rows except nucleus come from PAINT node PTN000624096. This is the eukaryote-wide CDK7 ortholog clade: S. cerevisiae Kin28 (SGD:S000002266), S. pombe Mcs6 (SPBC19F8.07), Drosophila Cdk7 (FBgn0263237), rat Cdk7 (RGD:621124) and human CDK7 itself. The nucleus IBA comes from a deeper CDK node, PTN000623091. Human CDK7 being among the donors is expected.
- PAINT propagated CTD kinase, cyclin-dependent kinase activity, TFIIK, initiation, cytoplasm and regulation of cell cycle from this node. It did not propagate NER or DNA-dependent ATPase activity, which agrees with the decisions below.

### Key decisions
- GO:0000439 TFIIH core complex (PMID:8692841): MODIFY to holo-TFIIH and CAK-ERCC2. The abstract states that core TFIIH* is "devoid of detectable levels of ERCC2 (XPD) and CAK".
- GO:0008094 ATP-dependent activity, acting on DNA (PMID:9852112): REMOVE. CDK7 is a single-domain protein kinase. The DNA-dependent ATPase/helicase activity of TFIIH belongs to XPB/XPD, so this is a complex activity transferred to a subunit that does not perform it.
- GO:0006289 NER (NAS): MARK_AS_OVER_ANNOTATED. CAK is released from TFIIH when XPA binds the lesion (Reactome R-HSA-5689861).
- GO:0045944 positive regulation of Pol II transcription (PMID:9852112): over-annotation. This is a general transcription factor taking part in basal and activated transcription.
- Perinuclear region (from the barley-peptide relocalisation study): over-annotation.
- Bare protein binding: REMOVE, per policy. The exception is PMID:23393140, whose interactor set includes cyclin H; that row is MODIFIED to cyclin binding.
- Regulation of cell cycle (IBA, TAS): MODIFY to regulation of the G1/S transition (CDK4/6/2 activation; PMID:23622515) and regulation of the G2/M transition (CDK1 Thr161; PMID:20360007, PMID:7533895).
- Generic kinase and Ser/Thr kinase rows: MODIFY to GO:0004693 plus the CTD kinase terms (S5 and S7 for the Reactome snRNA reaction).
- NEW: GO:0032968 positive regulation of transcription elongation by RNA polymerase II. CDK7 phosphorylates the CDK9 T-loop and SPT5 (PMID:28768201, PMID:16327805), and THZ1 reduces pausing and blocks DSIF loading (PMID:26257281). Participation test: CDK7 does the phosphorylation itself. Comparator: the S. pombe ortholog Mcs6 review carries this process, as does CDK9.
- Considered and not added: GO:0045737 positive regulation of CDK S/T kinase activity, for the CAK step. Comparator: budding-yeast CAK1 (a CAK) does not carry it, and no reviewed gene in the repo does. GO represents CAK through the kinase MF, so this is raised as a suggested question about a dedicated CAK-activity MF.

### Relative
- Closest experimentally characterised ortholog in the same PAINT clade (PTN000624096): S. pombe Mcs6 (Q12126), with a complete review in genes/SCHPO/mcs6/mcs6-ai-review.yaml. The module modules/g2_m_transition.yaml includes the CDK7-cyclin H-MAT1 CAK step.
