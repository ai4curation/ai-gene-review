# Sdhaf2 (A0A494B8X4): evidence and exact-input prediction review

The mitochondrial-matrix prediction has a sound sequence and family basis. The assembly-factor name and flavinylation mechanism describe the Sdhaf2 gene correctly, but their complete functional transfer to the shorter alternative product is uncertain. The epithelial-transition and beta-catenin annotations also have real primary evidence; their uncertainty here concerns the exact product, not merely their electronic evidence code.

## Input identity and functional boundary

A0A494B8X4 is a 135-residue mouse Sdhaf2 product. Reference Q8C6I2 is 164 residues. Selected residues 1–122 match reference 1–122 at 121 positions, including all 27 residues of the reference mitochondrial transit peptide; the remaining 13 residues are an alternative tail. The reference C-terminal region is therefore not fully retained. This is not evidence that every shorter Sdhaf2 product must be inactive.

## Biological evidence

- [PMID:38569044 — Drp1 controls complex II assembly and skeletal muscle metabolism by Sdhaf2 action on mitochondria.](https://pubmed.ncbi.nlm.nih.gov/38569044/): Mouse muscle and myocyte experiments connect mitochondrial Sdhaf2 availability to complex-II assembly and activity; they do not isolate the 135-residue alternative product.

> Restoration of Sdhaf2 normalized complex II
> activity, lipid oxidation, and insulin action in Drp1-KD myocytes.

- [PMID:23983127 — Succinate dehydrogenase 5 (SDH5) regulates glycogen synthase kinase 3β-β-catenin-mediated lung cancer metastasis.](https://pubmed.ncbi.nlm.nih.gov/23983127/): The study directly reports a mouse Sdhaf2/SDH5 loss phenotype in lung epithelial cells, so the EMT association is not supported solely by an ARBA assertion.

> In SDH5 knock-out mice, lung epithelial cells exhibited elevated mesenchymal markers, which is characteristic of EMT.


> SDH5 functions as a negative regulator of Wnt-β-catenin signaling.

## Exact non-GO claims

The complete emitted record is preserved in [Sdhaf2-protnlm-source.json](Sdhaf2-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Succinate dehydrogenase assembly factor 2, mitochondrial

UNC (CS 1) as a complete functional enzyme-assembly-factor name for the selected product. Sdhaf2 family/gene identity and mitochondrial targeting are well supported, but full assembly-factor activity is not established for its altered C-terminus. This is not a wrong-paralog assignment. [Sequence comparison](Sdhaf2-bioinformatics/RESULTS.md); [PMID:38569044](https://pubmed.ncbi.nlm.nih.gov/38569044/).

### Function

> Plays an essential role in the assembly of succinate dehydrogenase (SDH), an enzyme complex (also referred to as respiratory complex II) that is a component of both the tricarboxylic acid (TCA) cycle and the mitochondrial electron transport chain, and which couples the oxidation of succinate to fumarate with the reduction of ubiquinone (coenzyme Q) to ubiquinol. Required for flavinylation (covalent attachment of FAD) of the flavoprotein subunit SDHA of the SDH catalytic dimer

UNC (CS 1). The paragraph correctly describes SDHAF2-mediated SDHA maturation at the gene level. The statements about TCA and respiratory chemistry describe the SDH complex, not intrinsic SDHAF2 catalysis. The selected product retains its mitochondrial targeting sequence but lacks the intact reference C-terminal region; whether it supports flavinylation or complex-II assembly is unresolved. [PMID:38569044](https://pubmed.ncbi.nlm.nih.gov/38569044/); [sequence comparison](Sdhaf2-bioinformatics/RESULTS.md).

### Location

> Mitochondrion matrix

CNN (CS 2). The reference transit peptide is entirely conserved and is consistent with the primary mouse mitochondrial-import mechanism. A reasonable family and targeting-sequence inference supports the existing matrix compartment; no exact-product imaging is claimed. [Sequence comparison](Sdhaf2-bioinformatics/RESULTS.md).

## Emitted GO claims

All 3 emitted GO claims are individually assessed in [Sdhaf2-protnlm-predictions-review.yaml](Sdhaf2-protnlm-predictions-review.yaml).

## Family integration

PTHR12469:SF2 supports Sdhaf2 ancestry. The relevant conserved function is flavoprotein maturation, distinct from SDHA catalysis. The precise C-terminal alteration requires a product-specific qualification of functional transfer, whereas the intact N-terminal targeting sequence supports mitochondrial import. No phylogenetic loss event is inferred from an alternative protein product.

## Evidence limits

Both cited papers have cached full text. The 2024 mouse study supports the Sdhaf2 import/assembly mechanism, and the 2013 study supplies the actual EMT and beta-catenin evidence. None assays A0A494B8X4 specifically. The genuine Falcon synthesis is interpreted using this exact sequence boundary; absence of a product-specific assay is not treated as demonstrated loss of function.

Exact sequence mapping: [Sdhaf2-bioinformatics/RESULTS.md](Sdhaf2-bioinformatics/RESULTS.md). Global alignments can place nonhomologous alternative tails opposite gaps or distant residues; only conserved segments and explicitly retained feature intervals support functional transfer.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This entry was written during a re-review that deliberately ignored the ProtNLM2 predictions; the earlier sections above, including the ProtNLM2 claim assessments, are retained unchanged.

### 2026-10-20 full re-review (independent of any ProtNLM output)

#### Identity: alternative gene model, not the canonical product

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

#### Evolutionary grounding

- PANTHER PTHR12469 (PROTEIN EMI5 HOMOLOG, MITOCHONDRIAL), subfamily SF2 (SUCCINATE DEHYDROGENASE
  ASSEMBLY FACTOR 2, MITOCHONDRIAL). The human ortholog SDHAF2 Q9NX18 is in the same subfamily.
- PAINT (interpro/panther/PTHR12469/PTHR12469-paint.tsv): the eukaryotic node PTN000279729 carries IBD
  mitochondrion (seeds Arabidopsis, yeast and human), TCA cycle, mitochondrial electron transport, and
  complex II assembly (seeds yeast Sdh5 and human SDHAF2). PTN000279784 (taxon 284812, S. pombe)
  carries NOT IRD for the process terms. No EMT or Wnt terms were propagated. I treat this as a
  deliberate decision, so the EMT/Wnt rows are not family functions.
- This product's GOA set has none of the IBA rows, only SubCell and ARBA IEA rows.

#### Literature

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

#### Decisions

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

#### Closest characterised relative

- Human SDHAF2 (Q9NX18), ortholog in PTHR12469:SF2 and a PAINT seed for complex II assembly. It has a
  complete review at genes/human/SDHAF2/SDHAF2-ai-review.yaml.
