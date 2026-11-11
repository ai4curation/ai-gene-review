# TGFBR3 (donkey, A0A8C4M6Z6) - review notes

DONKEY40 cohort. 33 IEA GOA rows; most are Ensembl Compara (GO_REF:0000107) transfers of human experimental annotations; 4 TreeGrafter rows.

## Sequence
- [file:EQUAS/TGFBR3/TGFBR3-bioinformatics/RESULTS.md "89.47% identity over 836 paired residues"]; signal peptide, ZP-domain disulfides and TM helix conserved (["TRANSMEM Helical: human [788, 809] MY -> donkey [773, 794] MY"]).

## Function
- [PMID:18184661 "The TGF-beta type III receptor (TbetaRIII or betaglycan) is an abundant cell surface proteoglycan that has been well characterized as a TGF-beta and inhibin receptor."]
- [PMID:18184661 "TbetaRIII directly and specifically binds to multiple members of the BMP subfamily, including BMP-2, BMP-4, BMP-7, and GDF-5"]
- Human UniProt: [file:EQUAS/TGFBR3/TGFBR3-bioinformatics/human-Q03167-uniprot.txt "In gonadotrope cells, acts as an inhibin A coreceptor and regulates follicle-stimulating hormone (FSH) levels and female fertility"]; ["Exists both as a membrane-bound form and as soluble form in serum and in the extracellular matrix."]
- Immune response source: [PMID:16886151 "We found significant associations with SNPs in IGF1R and genes of the TGF-beta /BMP pathway (BMP6, TGFBR3, BMPR1A, SMAD6 and SMAD3)."] - association only.
- ECM assembly / gene expression source: [PMID:30729664 "TGFBR3 siRNA could increase fibrosis-related genes expression, along with the Smad1 inactivation and Smad3 activation in HAFs."]

## Ontology note
- GO:0070123 (TGF-beta receptor activity, type III) is_a GO:0005024, whose definition includes Ser/Thr kinase catalysis; betaglycan has no kinase domain. Raised as a suggested question; GO:0005024 row MODIFY -> GO:0070123.

## Decisions
- Core: GO:0070123, GO:0015026 coreceptor, GO:0050431 TGF-beta binding, inhibin-betaglycan-ActRII complex, TGF-beta receptor signalling, plasma membrane/external side.
- Over-annotated: organ development, immune response, gene expression, hormone/PGE responses, intracellular signal transduction, SMAD binding, negative regulation of ECM assembly.
- ProtNLM2 GO:0005576 extracellular region: correct (shed soluble betaglycan) and not in donkey GOA -> COR.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Re-review of every existing annotation, the description and the core functions. ProtNLM2 files were not opened or used.

### Deep research
- `just deep-research-falcon EQUAS TGFBR3 --fallback perplexity-lite` failed (falcon timed out at 600 s, then the perplexity-lite fallback also failed); no deep-research file was produced. Review is based on the cached literature below plus sequence analysis.
- Newly cached human source papers: PMID:10746731, PMID:11157754, PMID:12958365, PMID:14557487 (abstract only), PMID:29130787, PMID:30467960 (full text).

### Identity and evolutionary placement
- A0A8C4M6Z6 is the main donkey TGFBR3 gene product (Ensembl ENSEASP00005022721.2, 836 aa, PE 4); the only other donkey TGFBR3 entry is a 139-aa fragment (A0A9L0JW49). There is no reviewed donkey entry, so this is the de facto canonical product.
- UniProt places it in PANTHER PTHR14002:SF7 (TGFBR3 subfamily), separate from endoglin. The human IBA rows come from PAINT node PTN002678643 (taxon Euteleostomi), seeded by human Q03167, mouse MGI:104637, rat RGD:61821 and chicken Q90998, all TGFBR3 orthologs [file:EQUAS/TGFBR3/TGFBR3-bioinformatics/human-Q03167-quickgo-annotations.tsv; interpro/panther/PTHR14002/PTHR14002-paint.tsv]. Plasma membrane comes from node PTN008553354. Donkey GOA cites an older TreeGrafter node id (PTN001421580); the term set is the same as at PTN002678643. I found no disagreement about subfamily placement. There is no family review for PTHR14002 under interpro/panther/ (only metadata, entries and PAINT files).
- New analysis [file:EQUAS/TGFBR3/TGFBR3-bioinformatics/RESULTS-rereview.md] (script compare_sequences_rereview.py; ortholog sequences in rereview-orthologs.fasta). Conserved in donkey: both GAG-attachment serines (human S534/S545 -> donkey S533/S544), all five N-glycan sites, the TGF-beta interaction region (14/15 identical), the TbetaRII phosphoacceptor (human T840 -> donkey T825) and the whole cytoplasmic domain (42/42 identical).
- Gene-model note: compared with human, the donkey product lacks (a) the residue that human isoform 2 also lacks (human 359), and (b) a 14-residue membrane-proximal stalk segment (human 763-776, GPSMKEPNPISPP...). Segment (b) is present in horse F7E1V2, pig, dog, mouse and rat. Its absence is therefore most likely a donkey gene-model or splice-site choice rather than a lineage-specific deletion, but I cannot confirm this without transcript data. No domain, catalytic or binding element maps to this segment. It is in the stalk next to the membrane, where ectodomain shedding takes place, so whether shedding of the donkey product is affected is an open question.

### Corrections made
- GO:0010628: the earlier review attributed the human source to PMID:30729664. The human IMP is actually from PMID:30467960 (let-7a/HUVEC). I re-quoted that paper; the action stays MARK_AS_OVER_ANNOTATED.
- GO:0034695 and GO:0034699 had cited the GO:0032354 RESULTS line. They now cite their own lines and the PMID:14557487 abstract (expression is regulated by FSH, LH and PGE2, so these rows describe regulation of the gene, not function of the protein).
- I added direct literature quotes (PMID:10746731, 12958365, 29130787, 30467960) to the coreceptor, inhibin complex, TGF-beta binding, regulation of TGF-beta signalling, TGFBR2 binding, NF-kappaB and migration rows. I also added the PAINT node basis to the IBA-derived rows.
- No action changed. Every row's action was re-examined, and the existing judgements hold given the literature and the PAINT placement.
- I updated the description with the conserved sites and the stalk-segment difference.

### Relative
- The closest experimentally characterised relative is human TGFBR3 (Q03167), an ortholog in the same PANTHER subfamily SF7 and under the same PAINT node. The repo has no review for it (no genes/*/TGFBR3 other than this folder), so it needs one. Mouse Tgfbr3 (O88393) and rat (P26342) are also unreviewed.
- Modules: no module under modules/ mentions TGFBR3 or betaglycan.
