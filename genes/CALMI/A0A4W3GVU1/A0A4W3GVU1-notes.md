# A0A4W3GVU1 (esrp1, Callorhinchus milii) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No notes file existed before this session; this section is the first entry.

### Identity
- UniProt A0A4W3GVU1 (TrEMBL, PE 3), 684 aa, gene esrp1 (Ensembl ENSCMIP00000007130.1).
  Full-length: aligns across 679 columns of human ESRP1 (Q6NXG1, 681 aa) with 77.9% identity,
  three RRMs (SMART SM00360 x3, CDD RRM1_ESRP1 and RRM3_ESRP1_ESRP2). Not a fragment, isoform or
  alternative gene model issue. Like human ESRP1 it carries the RNase H-like / RNase_T-like
  N-terminal fold (IPR012337, PF00929), which in ESRPs is not known to be catalytic.
- Phylogeny (file:CALMI/A0A4W3GVU1/A0A4W3GVU1-bioinformatics/RESULTS-rereview.md): groups with
  tetrapod ESRP1, inside the ESRP clade (ESRP1/ESRP2 sister to Drosophila fusilli), outside
  hnRNP H/F/GRSF1. UniProt gives only family PTHR13976 (no subfamily); placement is consistent
  with PTHR13976:SF37 (ESRP1).

### PAINT
- PTN001018050 (taxon 6072 Eumetazoa): GO:0003729 mRNA binding IBD, seeds fusilli, ESRP1, ESRP2.
- PTN000360053: GO:0003723 RNA binding, GO:0043484 regulation of RNA splicing, GO:0005654
  nucleoplasm (seeds include ESRP1 Q6NXG1, ESRP2 Q9H6T0, hnRNP F/H).
- The target has no IBA rows in GOA (its record lacks a PANTHER subfamily assignment, so it is
  presumably not in the PANTHER tree); it would otherwise inherit these.
- Human ESRP1 experimental GO (QuickGO, 2026-10-21): mRNA binding IDA, regulation of RNA splicing
  (GO:0043484) IDA, nucleus IDA [PMID:19285943]. Curators chose GO:0043484, not GO:0048024.

### Literature (mammalian ESRP1; none on the shark protein)
- [PMID:19285943 "we identified two paralogous epithelial cell-type-specific RNA-binding proteins that are essential regulators of FGFR2 splicing"]
- [PMID:19285943 "suggesting that they bind specific GU-rich sequence motifs"]
- [PMID:20711167 "Epithelial splicing regulatory proteins 1 and 2 (ESRP1 and ESRP2) are"] hundreds of ESRP-regulated events.
- [PMID:36238894 "competing 5′ splice sites at the end of Esrp1 exon 12 lead to the production of ESRP1 isoforms with distinct nuclear or cytoplasmic localization"]
- [PMID:26371508 "Mice with ablation of Epithelial splicing regulatory protein (Esrp1) develop cleft lip and palate."] — organismal phenotype; not annotated.

### Changes vs previous review
- Fixed two supporting_text quotes that were not verbatim in the deep-research file
  (markdown bold), and replaced most file: support with PMID quotes.
- GO:0003723 RNA binding: ACCEPT -> MODIFY to GO:0003729 mRNA binding (correct but general; the
  specific term is supported by human ESRP1 IDA and the PAINT ESRP node).
- NEW process row changed from GO:0048024 to GO:0043484 regulation of RNA splicing, the term used
  by both the human IDA and the PAINT IBD; the spliceosome-specific child was not chosen by curators.
- Description rewritten with phylogenetic grounding; removed unqualified statements
  (craniofacial/limb development, EMT) from transferred function claims.

### Relative
- Closest characterised relative: human ESRP1 (Q6NXG1), SF37. No review exists in genes/ (no
  ESRP1/Esrp1 folder in any species). Mouse Esrp1 (Q3US41) also unreviewed.
- Family review interpro/panther/PTHR13976/PTHR13976-review.yaml has one generic subfamily
  bucket; it does not contradict the SF37 placement but does not assign it either. Its
  "nucleus UNRESOLVED" family-wide scope is compatible with accepting nucleus for the ESRP1
  ortholog specifically.
- Modules: modules/fgfr_signaling.yaml mentions ESRP1/2-controlled FGFR2 IIIb splicing.
