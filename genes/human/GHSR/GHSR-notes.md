# GHSR evidence and annotation tracing

GHSR recognizes acyl-ghrelin. The defining [PMID:10604470](https://pubmed.ncbi.nlm.nih.gov/10604470/), DOI [10.1038/45230](https://doi.org/10.1038/45230), explicitly distinguishes the GHSR pathway from hypothalamic growth-hormone-releasing hormone(GHRH). QuickGO definitions checked 2026-09-08: GO:0016520 binds GHRH, while GO:0001616 binds ghrelin. Human GOA nevertheless has GO:0016520 IDA rows citing this paper and PMID:8688086, plus a rat-derived IEA. The horse row transfers GO:0016520 from human Q92847/ENSP00000241256 under GO_REF:0000107. The correction therefore belongs on the human donor and horse target. It is a ligand/term mismatch, not an allegation of an unsupported experimental organism.

Modern [PMID:35027551](https://pubmed.ncbi.nlm.nih.gov/35027551/) structures directly show active ghrelin receptor bound to ghrelin and G protein. The complete 366 aa horse receptor aligns at 95.1% identity with human Q92847 and retains all seven helices and key ligand-binding features. This grounds receptor-subfamily transfer beyond a generic GPCR-domain label.

[PMID:42426797](https://pubmed.ncbi.nlm.nih.gov/42426797/), DOI [10.1186/s12917-026-05700-8](https://doi.org/10.1186/s12917-026-05700-8), full text cached, measures equine tissue GHSR transcripts and circulating ghrelin. “Sequencing confirmed both products were identical to the equine GHSR1a reference sequence”. The validated tissues are pituitary and adrenal medulla. This is horse-specific identity/expression evidence, not a ghrelin-versus-oxytocin ligand-binding experiment or proof of every inferred physiological role. A horse-specific Falcon job was launched for this reason; it exceeded the local 600s timeout and fallback failed with insufficient quota. Any later-arriving provider report is preserved separately.

Human immune effects are supported by [PMID:15232612](https://pubmed.ncbi.nlm.nih.gov/15232612/). Human decidualization in [PMID:17494105](https://pubmed.ncbi.nlm.nih.gov/17494105/) is not generalized to horse uterine biology. Fine-grained neuronal and metabolic transfers require their own donor-specific assessments; general receptor conservation is not enough for every physiological term.

## Research synthesis

The completed human Falcon synthesis supports acyl-ghrelin recognition, constitutive activity, LEAP2 antagonism and context-dependent G-protein coupling. It distinguishes full-length GHSR1a from the truncated five-transmembrane GHSR1b form. The selected horse protein is a full-length seven-transmembrane receptor. Human signaling and the direct ghrelin-bound structures strengthen ligand specificity without establishing every fine-grained neuronal or endocrine transfer to horse.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. The review YAML was rebuilt row by row; all 90 GOA rows were re-judged.

**Identity.** Q92847 is the reviewed canonical UniProt entry (isoform 1A, Q92847-1, 366 aa, seven TM helices 41-326). It is the full-length signaling receptor, not a fragment or alternative gene model. Isoform 1B (Q92847-2; VSP_001916/VSP_001917) is the truncated five-TM GHSR1b, which does not bind ghrelin. PANTHER PTHR24243:SF7 (GROWTH HORMONE SECRETAGOGUE RECEPTOR TYPE 1). The family review interpro/panther/PTHR24243/PTHR24243-review.yaml places it in SF7 as a representative member, so there is no placement disagreement.

**Evolutionary grounding.** The GHSR-specific PAINT node PTN002797666 (taxon 117571, Euteleostomi) carries IBD GO:0001616 and GO:0009755 (seeds human Q92847, rat O08725, pig Q95254). The broader PTN002797649 carries GPCR activity, GPCR signaling and plasma membrane. Mouse Ghsr Q99P50 and rat Ghsr O08725 are both in PTHR24243:SF7 (UniProt REST, 2026-10-20), so the many Ensembl Compara (GO_REF:0000107) and ISS rows come from same-subfamily one-to-one orthologs. I traced each donor in QuickGO (rat/mouse experimental annotations) and cached the source PMIDs.

**Key changes vs the previous version.**
- The previous text mixed in horse-specific statements (95.1% identity to the horse receptor, equine expression paper). These were removed from the human review. PMID:42426797 is kept in references, marked as not used.
- GO:0016520 (GHRH receptor activity), x3 rows: MODIFY to GO:0001616. QuickGO definitions: GO:0016520 is "Combining with growth hormone-releasing hormone", GO:0001616 is "Combining with ghrelin". PMID:10604470 explicitly separates the ghrelin pathway from GHRH. GO-CAM 67f85f2b00000823 also uses GO:0016520 for GHSR; I raised this as a suggested question.
- Generic MF/CC/BP rows: GO:0004930 and GO:0038023 MODIFY to GO:0001616 (OLS confirms it is an is_a descendant); GO:0016020 MODIFY to GO:0005886; GO:0007154, GO:0023052 and GO:0009725 TOO_GENERAL (ancestors of the accepted GO:0007186/GO:0009755).
- GH axis: GO:0030252 growth hormone secretion (TAS) and GO:0060123 MODIFY to GO:0060124 positive regulation of GH secretion, since the receptor stimulates somatotroph secretion and does not carry it out. GO:0045927 MODIFY to GO:0040018. GO:0060259 MODIFY to GO:1904000.
- REMOVE ten rat IEP-sourced Compara projections: spermatogenesis, female pregnancy, and responses to FSH, estradiol, GH, dexamethasone, LPS, thyroid hormone, L-glutamate and IGF. An expression change is not a function and cannot be transferred by orthology.
- REMOVE GO:0032099 negative regulation of appetite (rat PMID:21778696, a paradoxical antagonist result the authors call "inconsistent with a simple hormone-receptor model"). It contradicts the knockout data (PMID:15070777, PMID:16322794).
- REMOVE GO:0036321 ghrelin secretion (the receptor does not secrete ghrelin).
- MARK_AS_OVER_ANNOTATED: learning, memory, learning or memory (behavioral phenotypes; the mechanistic synaptic plasticity and coreceptor terms are kept), locomotion, fatty-acid metabolism, norepinephrine secretion (an NPY/Y1 circuit effect), nerve impulse, small-intestine smooth muscle contraction (gut smooth muscle lacks GHS-R immunoreactivity, PMID:12890514), and retinal angiogenesis/endothelial proliferation (pathology pharmacology).
- KEEP_AS_NON_CORE: DRD1/DRD2 coreceptor activity (mouse PMID:26590421, PMID:40441153), synaptic plasticity and synaptic locations (rat SynGO), feeding/appetite, GI motility and defecation, immune cytokine suppression (human PMID:15232612), decidualization, and macrophage anti-apoptosis.
- Core function: GO:0001616 at the plasma membrane, via GO:0007200 and GO:0009755.

**Relative for next review.** Mouse Ghsr Q99P50 (MGI:2441906), a same-subfamily (SF7) one-to-one ortholog descending from PTN002797666. It has the richest experimental record: knockouts, the DRD1/DRD2 heteromers, and the defecation mechanism. There is no review in the repo (no genes/mouse/Ghsr).

**Modules.** No module under modules/ covers ghrelin/GHSR signaling; the only grep hits are incidental mentions in deep-research artifacts for other modules. The relevant GO-CAMs are 67f85f2b00000823, 69c59f8a00000139 and 69c59f8a00001474.
