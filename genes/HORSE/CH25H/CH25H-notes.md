# CH25H: paired evidence notes

Human reference: https://www.uniprot.org/uniprotkb/O95992/entry

Primary source: [PMID:9852097 cDNA cloning of mouse and human cholesterol 25-hydroxylases, polytopic membrane proteins that synthesize a potent oxysterol regulator of lipid metabolism.](https://pubmed.ncbi.nlm.nih.gov/9852097/).

> Here, we report the cloning of cholesterol 
> 25-hydroxylase cDNAs from the mouse and human. The encoded enzymes are polytopic 
> membrane proteins of 298 and 272 amino acids, respectively, which contain 
> clusters of histidine residues that are essential for catalytic activity. Unlike 
> most other sterol hydroxylases, cholesterol 25-hydroxylase is not a cytochrome 
> P450, but rather it is a member of a small family of enzymes that utilize diiron 
> cofactors to catalyze the hydroxylation of hydrophobic substrates. The 
> cholesterol 25-hydroxylase gene lacks introns, and in the human it is located on 
> chromosome 10q23. The murine gene is expressed at low levels in multiple 
> tissues. Expression of cholesterol 25-hydroxylase in transfected cells reduces 
> the biosynthesis of cholesterol from acetate and suppresses the cleavage of 
> sterol regulatory element binding protein-1 and -2. The data suggest that 
> cholesterol 25-hydroxylase has the capacity to play an important role in 
> regulating lipid metabolism by synthesizing a co-repressor that blocks sterol 
> regulatory element binding protein processing and ultimately leads to inhibition 
> of gene transcription.

The horse sequence comparison is in [CH25H-bioinformatics/RESULTS.md](CH25H-bioinformatics/RESULTS.md). Transfer is assessed for this exact accession; human biochemical evidence is not equine experimental validation.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used.

**Deep research.** `just deep-research-falcon HORSE CH25H --fallback perplexity-lite` failed
(falcon: "Failed to authenticate"; perplexity-lite: HTTP 401 insufficient quota). No
deep-research file was created. A web search found no equine-specific experimental study of
CH25H; the review relies on the human/mouse literature cached in `publications/`
(PMID:9852097, PMID:32944968, PMID:33239446) and the reviewed human UniProt entry.

**Identity of the benchmark accession.** F6T000 (TrEMBL, unreviewed, 270 aa; RefSeq
XP_001503057.1; Ensembl ENSECAP00000003097) is the full-length horse CH25H product, not a
fragment or isoform. It aligns over 100% of its length to human O95992 (272 aa) at 83.3%
identity; the only length difference is the C-terminus (horse ...LRSAHAK vs human
...LRTASVPAR). The gene is intronless in mammals [PMID:9852097 "The cholesterol 25-hydroxylase
gene lacks introns"], so splice isoforms are not expected. No reviewed horse CH25H entry exists.

**Evolutionary grounding.** PANTHER PTHR11863 (sterol desaturase), a functionally
heterogeneous family. Human, mouse and rat CH25H are in subfamily SF213 (CHOLESTEROL
25-HYDROXYLASE) per the PANTHER 19.0 member index; F6T000 has no subfamily call in UniProt
(horse is not a PANTHER reference genome), but its GO:0001567 IBA comes from PTN002627316
(Euteleostomi), the CH25H-clade node seeded by human CH25H and mouse Ch25h, which places it in
that clade. The C-4 methylsterol oxidase (PTN000221246, family root) and zymosterol
biosynthesis (PTN002275159, seeded only by mouse Msmo1) IBAs are deep-node propagations from
the MSMO1/ERG25 branch; removed as functional divergence. The PTHR11863 family review
(`interpro/panther/PTHR11863/PTHR11863-review.yaml`) agrees that C-4 methylsterol oxidase
activity is not supported for CH25H; no subfamily-placement disagreement. Note: panther.obo
also has SF34 named "CHOLESTEROL 25-HYDROXYLASE"; the characterised orthologs are in SF213.

**Histidine boxes.** New script `CH25H-bioinformatics/hisbox_rereview.py` (output
`RESULTS-rereview.md`, `results-rereview.json`) maps the three human UniProt histidine-box
MOTIF features: box-1 WHLLH->WHVLH (142-146), box-2 HKVHH->HKMHH (157-161), box-3
HHDLHHS->HHDLHHS (238-244); every histidine is conserved. The earlier RESULTS.md had an empty
feature list because it only mapped METAL/BINDING features.

**Actions.** ACCEPT: cholesterol 25-hydroxylase activity (IBA, IEA), ER membrane (IBA), iron
ion binding, cholesterol metabolic process. MODIFY: steroid hydroxylase activity ->
GO:0001567; membrane -> ER membrane. KEEP_AS_NON_CORE: lipid biosynthetic process (no oxysterol
biosynthesis term exists), response to type I interferon, B cell chemotaxis, negative
regulation of cholesterol metabolic process, negative regulation of virus-host plasma
membrane fusion. REMOVE: C-4 methylsterol oxidase activity, zymosterol biosynthetic process.
The human review (genes/human/CH25H) uses MARK_AS_OVER_ANNOTATED for the same two IBA rows;
REMOVE is used here because they assert a specific reaction/pathway the CH25H clade does not
perform. Harmonising the human review is a possible follow-up.

**Relative.** Human CH25H (O95992), one-to-one ortholog in PANTHER SF213 / PAINT node
PTN002627316; reviewed at genes/human/CH25H/CH25H-ai-review.yaml (all rows actioned). Modules
listing CH25H: modules/bile_acid_biosynthesis.yaml, modules/bile_acid_synthesis_ring_modification.yaml;
modules/srebp_signaling.yaml mentions its product 25-hydroxycholesterol (SREBP regulation) but not CH25H.
