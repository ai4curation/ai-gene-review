# CDK7: paired evidence notes

Human reference: https://www.uniprot.org/uniprotkb/P50613/entry

Primary source: [PMID:15530371 The crystal structure of human CDK7 and its protein recognition properties.](https://pubmed.ncbi.nlm.nih.gov/15530371/).

> CDK7, a member of the cyclin-dependent protein kinase family, regulates the 
> activities of other CDKs through phosphorylation on their activation segment and 
> hence contributes to control of the eukaryotic cell cycle. CDK7 also assists in 
> the regulation of transcription as part of the transcription factor TFIIH 
> complex. For maximum activity and stability, CDK7 requires phosphorylation, 
> association with cyclin H, and association with a third protein, MAT1.

The horse sequence comparison is in [CDK7-bioinformatics/RESULTS.md](CDK7-bioinformatics/RESULTS.md). Transfer is assessed for this exact accession; human biochemical evidence is not equine experimental validation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research: `just deep-research HORSE CDK7 --provider falcon` failed ("Exception: Failed to authenticate" from the falcon client; no fallback succeeded), so no deep-research file exists for this folder; the review uses cached literature and the human ortholog record instead.

### Identity of the benchmark accession (alternative gene model)

- A0A9L0R074 (415 aa, TrEMBL, no gene name) is one of eight UniProt models of the horse CDK7 gene (Ensembl ENSECAG00000014570). None is Swiss-Prot reviewed. K9K3U4 (346 aa, PE=2, from mRNA JL616500) is the transcript-supported product and has the same length and C-terminus as human CDK7 P50613 (346 aa).
- A0A9L0R074 and K9K3U4 are identical for residues 1-338; K9K3U4 then ends GLPKKLIF (as human), whereas A0A9L0R074 continues with a 77-residue segment (VAVKIQLSHHRHW...LLPKNWP) that has no counterpart in human CDK7 [file:HORSE/CDK7/CDK7-bioinformatics/RESULTS-rereview.md "A0A9L0R074 and K9K3U4 are identical for residues 1-338."]. It is therefore an alternative 3'-end gene model (alternative or read-through terminal exon), not a fragment.
- The kinase domain (human 12-295) is complete; K41, D137 (catalytic), D155 (DFG), S164 and the T-loop T170 are conserved [file:HORSE/CDK7/CDK7-bioinformatics/RESULTS-rereview.md "| A0A9L0R074 | 415 | 95.38 | 1-346 | 0 | 69 | K41 | D137 | D155 | S164 | T170 |"]. Only the last 8 human residues are replaced; nothing known to be required for cyclin H/MAT1 binding or catalysis is lost, but the extra segment is uncharacterised.
- New analysis: `CDK7-bioinformatics/compare_models_rereview.py` (inputs `horse_CDK7_models-rereview.fasta`; outputs `RESULTS-rereview.md`, `results-rereview.json`). Existing RESULTS.md left unchanged.

### Evolutionary grounding

- PANTHER PTHR24056:SF0 (CYCLIN-DEPENDENT KINASE 7) for the horse model and for human P50613.
- PAINT node PTN000624096 (CDK7/Kin28/Mcs6 clade; seeds human CDK7, S. cerevisiae Kin28 S000002266, S. pombe Mcs6 SPBC19F8.07, fly Cdk7) carries IBD for TFIIK complex (GO:0070985), CTD kinase (GO:0008353), transcription initiation at RNAPII promoter (GO:0006367), cytoplasm and regulation of cell cycle (GO:0051726) [interpro/panther/PTHR24056/PTHR24056-paint.tsv]. Horse has no IBA rows in GOA, but the GOA IEA rows for these terms agree with the PAINT placement.
- Family review interpro/panther/PTHR24056/PTHR24056-review.yaml records horse in SF0 and says human SF0 vs SF375 is "unresolved"; the current human UniProt record lists PTHR24056:SF0, so I see no disagreement for the horse placement.

### Key literature (human ortholog)

- CDK7-cyclin H is a TFIIH component [PMID:7533895 "complex (Cdk7 and cyclin H) as a component of TFIIH after extensive purification"].
- Core-like TFIIH* lacks CAK; CAK sits in ERCC2/CAK [PMID:8692841 "TFIIH* consists of a subset of the TFIIH complex proteins including ERCC3 (XPB), p62, p44, p41, and p34 but is devoid of detectable levels of ERCC2 (XPD) and CAK."]. Basis for MODIFY of the TFIIH core complex projection to TFIIH holo complex.
- Ser5/Ser7 CTD kinase [PMID:26257281 "Cdk7 phosphorylates Ser5 and Ser7 residues"].
- CDK4/6-activating kinase, G1 progression [PMID:23622515 "Here we show that Cdk7 is a Cdk4- and Cdk6-activating kinase in"].

### Decisions changed vs the previous pass

- GO:0008094 ATP-dependent activity, acting on DNA: REMOVE (TFIIH DNA ATPase belongs to XPB/XPD; CDK7 is a protein kinase).
- GO:0008353 CTD kinase: ACCEPT -> MODIFY to S5 (GO:0140836) and S7 (GO:0140837) kinase.
- Generic kinase terms now MODIFY to both specific activities (GO:0004693 and GO:0140836), not only GO:0004693.
- GO:0005634 nucleus: ACCEPT -> MODIFY to nucleoplasm; GO:0005524 ATP binding: ACCEPT -> KEEP_AS_NON_CORE.
- GO:0001650 fibrillar center and GO:0050821 protein stabilization: UNDECIDED -> KEEP_AS_NON_CORE; GO:0045944: ACCEPT -> KEEP_AS_NON_CORE.
- GO:0000307 kept ACCEPT: the specific CAK holoenzyme term GO:0019907 is obsolete.
- Two core functions now: CAK (GO:0004693, G1/S regulation, CDK holoenzyme) and TFIIH CTD Ser5 kinase (GO:0140836, transcription initiation, TFIIK).

### Relative

Human CDK7 (P50613), ortholog in the same PANTHER subfamily SF0 and PAINT node PTN000624096. Review genes/human/CDK7/CDK7-ai-review.yaml exists but is status IN_PROGRESS with 9 UNDECIDED rows explicitly deferred ("still requires detailed assessment"), including GO:0000307, GO:2000045 and GO:0008094, whose papers are cached; it needs a full review. Modules: modules/g2_m_transition.yaml (CAK step).
