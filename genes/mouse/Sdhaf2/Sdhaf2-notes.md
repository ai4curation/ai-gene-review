# Sdhaf2 (mouse, A0A494B8X4) notes

## 2026-10-20 full re-review (independent of any ProtNLM output)

### Identity: alternative gene model, not the canonical product

- A0A494B8X4 is a TrEMBL, Ensembl-derived entry (ENSMUSP00000157391 / ENSMUST00000237827), 135 aa.
- Canonical mouse Sdhaf2 is Q8C6I2, 164 aa, Swiss-Prot. Residues 1-121 are identical. A0A494B8X4 then
  ends in a novel 14-residue tail, DTPEEGVGSHCRWL, and so lacks canonical residues 122-164 (43 aa).
  [file:mouse/Sdhaf2/Sdhaf2-bioinformatics/RESULTS.md]
- The tail does not match either Swiss-Prot alternative isoform of Q8C6I2. Isoform 2 replaces
  122-164 with GMPYAELHLGIIR, and isoform 3 lacks residues 1-94. A0A494B8X4 is therefore a third
  alternative C-terminus.
- Retained: the mitochondrial transit peptide (1-27, predicted) and the RGxxE motif (mouse 75-79;
  the human paraganglioma variant G78R sits at mouse G76).
- Lost: canonical residues 122-141 at the end of the Pfam PF03937 Sdh5 domain (66-141), plus the
  C-terminal 23 residues. Whether this product is expressed as a stable protein or is active has not
  been tested.

### Evolutionary grounding

- PANTHER PTHR12469 (PROTEIN EMI5 HOMOLOG, MITOCHONDRIAL), subfamily SF2 (SUCCINATE DEHYDROGENASE
  ASSEMBLY FACTOR 2, MITOCHONDRIAL). The human ortholog SDHAF2 Q9NX18 is in the same subfamily.
- PAINT (interpro/panther/PTHR12469/PTHR12469-paint.tsv): the eukaryotic node PTN000279729 carries IBD
  mitochondrion (seeds Arabidopsis, yeast and human), TCA cycle, mitochondrial electron transport, and
  complex II assembly (seeds yeast Sdh5 and human SDHAF2). PTN000279784 (taxon 284812, S. pombe)
  carries NOT IRD for the process terms. No EMT or Wnt terms were propagated. I treat this as a
  deliberate decision, so the EMT/Wnt rows are not family functions.
- This product's GOA set has none of the IBA rows, only SubCell and ARBA IEA rows.

### Literature

- PMID:19628817: yeast Sdh5 and human SDH5 bind SDHA and are required for its flavination. SDHAF2 is
  the PGL2 paraganglioma gene.
- PMID:32887801: the human SDHA-SDHAF2 crystal structure. SDHAF2 and a dicarboxylate together orient
  the SDHA flavin and capping domains for covalent FAD attachment.
- PMID:38569044: in mouse muscle and C2C12 cells, Drp1 promotes Sdhaf2 mitochondrial translocation.
  Mitochondrial Sdhaf2 is limiting for complex II assembly, and restoring Sdhaf2 rescues complex II
  activity.
- PMID:23983127: a single study in lung cancer. SDH5 loss leads to EMT and SDH5 binds GSK-3beta,
  restraining beta-catenin. A knockout-mouse lung phenotype is reported.
- Falcon deep research (Sdhaf2-deep-research-falcon.md) agrees with this picture. It said no dedicated
  Sdhaf2-null mouse study was found, yet PMID:23983127 reports "SDH5 knock-out mice". The knockout is
  not characterised further in the abstract.

### Decisions

- GO:0005759 mitochondrial matrix (IEA SubCell): ACCEPT, because the targeting peptide is intact and
  the location is a family-level property.
- GO:0010719 negative regulation of EMT (IEA ARBA): MARK_AS_OVER_ANNOTATED. It is a downstream
  phenotype from necessity evidence, was not propagated by PAINT, and is applied to a truncated
  product.
- GO:0090090 negative regulation of canonical Wnt (IEA ARBA): KEEP_AS_NON_CORE. It has a mechanistic
  claim behind it (GSK-3beta binding), but only from a single cancer study. This matches the human
  ortholog review.
- I proposed no NEW annotations. The canonical product's function (GO:0044183 protein folding
  chaperone, GO:0018293 protein-FAD linkage, GO:0034553 complex II assembly) is recorded in
  core_functions as gene-level and caveated. It is not asserted as a new annotation on this
  truncated product, because the end of the Sdh5 domain is missing and no product-specific assay
  exists.
- The bioinformatics folder was redone: compare_products.py works from the UniProt flat file and REST
  data only. The earlier script read a ProtNLM input file, so it was replaced.

### Closest characterised relative

- Human SDHAF2 (Q9NX18), ortholog in PTHR12469:SF2 and a PAINT seed for complex II assembly. It has a
  complete review at genes/human/SDHAF2/SDHAF2-ai-review.yaml.
