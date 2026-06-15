# CLV3 (CLAVATA3) — Arabidopsis thaliana — Gene Review Notes

UniProt: Q9XF04 (CLV3_ARATH), gene At2g27250. 96-aa precursor; product type PROTEIN.
Member of the CLV3/ESR (CLE) signal peptide family.

## Summary of biology

CLV3 encodes a small secreted precursor protein that is proteolytically processed and
post-translationally modified into a 12-13 amino acid arabinosylated glycopeptide
(MCLV3 / CLV3p) derived from the conserved CLE domain near the C-terminus. The mature
peptide acts cell-non-autonomously as an extracellular ligand in the apoplast. It is
produced by the stem cells in the central zone of the shoot apical meristem (SAM) and
floral meristems and signals to the underlying organizing center, where it binds and
activates leucine-rich-repeat (LRR) receptor Ser/Thr kinases CLV1, BAM1, BAM2 and the
receptor-like protein CLV2 (acting with the pseudokinase CRN/CORYNE). Activation of
these receptors represses the homeodomain transcription factor WUSCHEL (WUS), forming a
CLV3-WUS negative feedback loop that maintains stem-cell homeostasis (balance between
proliferation and differentiation). Loss of CLV3 enlarges shoot and floral meristems
(extra organs, fasciation); overexpression / exogenous peptide consumes the meristem.

## Precursor architecture (from UniProt Q9XF04)

- Signal peptide 1-21; chain "Protein CLAVATA 3" 22-96.
- Mature peptide MCLV3 = residues 70-82 (PEPTIDE feature; "the functional peptide of CLV3 is MCLV3").
- Hydroxyprolines at Pro-73 and Pro-76 (MOD_RES).
- O-linked arabinosylation at hydroxyproline Pro-76 (CARBOHYD); arabinosylation enhances receptor binding affinity.
- His-81 essential for MCLV3 activity (MISCELLANEOUS).
- SUBCELLULAR LOCATION: Secreted, extracellular space.
- 3 alternative-splicing isoforms (Q9XF04-1/-2/-3). Isoform 1 is canonical; 2/3 likely intron retention.

## Key references (provenance)

### Localization / secretion
- [PMID:12034890 "CLV3 localizes to the apoplast and that export to the extracellular space is required for its function in activating the CLV1/CLV2 receptor complex"] — IDA apoplast (GO:0048046); full text available. "CLV3 is a secreted protein that activates the CLAVATA pathway in the extracellular space." Confirms extracellular/apoplast localization and cell-non-autonomous ligand role.

### Mature peptide identity / PTM
- [PMID:16902141 "MALDI-TOF MS applied to in situ Arabidopsis tissues determined the structure of a modified 12-amino acid peptide (MCLV3)"], "Synthetic MCLV3 induced shoot and root meristem consumption as cells differentiated into other organs, displaying the typical phenotype of transgenic plants overexpressing CLV3." Identification of MCLV3 with hydroxyPro-73/Pro-76 (mass 1345.6). Abstract-only cached. Supports regulation of meristem structural organization (GO:0009934, IDA).
- [PMID:19525968 "CLV3 is a 13-amino-acid arabinosylated glycopeptide. Post-translational arabinosylation of CLV3 is critical for its biological activity and high-affinity binding to its receptor CLV1"]. Abstract-only cached, but UniProt RP for this PMID lists "INTERACTION WITH CLV1, GLYCOSYLATION AT PRO-76 ... AND SUBCELLULAR LOCATION." Establishes arabinosylated glycopeptide + direct CLV1 binding. Supports receptor Ser/Thr kinase binding (GO:0033612, IPI vs CLV1=Q9SYQ8).

### Receptor binding / receptor complexes
- [PMID:18202283] (UniProt RN[15], "Arabidopsis CLV3 peptide directly binds CLV1 ectodomain") — Ogawa et al 2008 Science; not in existing_annotations refs but underpins direct CLV1 binding. (Not cached; UniProt-sourced.)
- [PMID:20626648 "CLV2, CLV1 and the CLV1 homologs BAM1 and BAM2 all bind to the CLV3-derived CLE peptide with similar kinetics"], Kd ~30 nM CLV1, 32 nM CLV2, 26 nM BAM1, 36 nM BAM2. "The CLV1 leucine-rich repeat receptor kinase (LRR-RK) binds to the CLV3 CLE peptide through its extracellular domain, providing direct evidence that CLV3-CLV1 function as a ligand-receptor pair". Full text available. GOA WITH/FROM fields for this IPI: O49545, O80809 (BAM1/BAM2), Q9M2Z1, Q9SYQ8 (CLV1). CLV1/BAM are receptor Ser/Thr kinases -> GO:0033612 appropriate; CLV2 is a receptor-LIKE protein lacking a kinase domain.

### Stem-cell / WUS feedback function
- [PMID:10915624 "CLV3 signaling occurs exclusively through a CLV1/CLV2 receptor kinase complex ... the CLV pathway acts by repressing the activity of the transcription factor WUSCHEL"]. Brand et al 2000 Science; abstract-only cached. Overexpression shows meristem cell fate depends on CLV3 activity level. GOA: IMP signal transduction (GO:0007165), IMP cell differentiation (GO:0030154), IPI signaling receptor binding (GO:0005102, WITH CLV1/CLV2 AGI loci AT1G75820/AT1G65380).
- [PMID:16603652 "Stem cells express the secreted peptide CLV3 that activates a signal transduction cascade to restrict WUS expression"], "increasing the CLV3 signal can very rapidly repress WUS expression"; "increased CLV3 signaling restricts meristem growth and promotes allocation of peripheral meristem cells into organ primordia." Full text available. GOA: IDA cell-cell signaling involved in cell fate commitment (GO:0045168), IDA cell surface receptor signaling pathway (GO:0007166), IMP meristem development (GO:0048507).
- [PMID:23321419 "the well-characterized stem cell-restricting CLAVATA3 (CLV3)" ... antagonistic alanine-substituted peptides give "a dominant-negative clv3-like phenotype, with enlarged shoot apical meristems and increased numbers of floral organs"]. IMP maintenance of meristem identity (GO:0010074). Abstract-only cached. Functional dissection of the CLV3 CLE peptide.

### Immunity (contested)
- [PMID:21499263 "the CLAVATA3 peptide (CLV3p) ... can trigger immune signalling and pathogen resistance via the flagellin receptor kinase FLS2"], "125I-Tyr-CLV3p interacted directly with FLS2", Kd 34.7 nM. Lee, Chah & Sheen 2011 Nature; full text available. Basis of GOA IDA innate immune response (GO:0045087).
- [PMID:22923673 "FLS2 does not recognize CLV3 and that the shoot apical meristem is immune to bacteria independently of CLV3 perception"]. Segonzac et al 2012 Plant Cell. Abstract-only cached. This is the basis of the GOA NOT|involved_in pattern recognition receptor signaling pathway (GO:0002221, IEP, negated). Direct refutation of the CLV3p-FLS2 immunity claim.

## Curation reasoning highlights

- Core MF: CLV3 is a secreted peptide ligand for LRR receptor (Ser/Thr) kinases. GO:0033612 (receptor serine/threonine kinase binding) is the most informative MF and is supported experimentally (CLV1/BAM binding). GO:0005102 (signaling receptor binding) is a correct but less specific parent — keep but treat as non-core/supporting; CLV2 is a receptor-like protein (no kinase), so binding to CLV2 is captured by the broader signaling-receptor-binding term.
- Core BP: extracellular cell-cell signaling that restricts WUS to maintain SAM stem-cell homeostasis — captured by GO:0045168 (cell-cell signaling involved in cell fate commitment) and GO:0007166 (cell surface receptor signaling pathway), with meristem-development/maintenance/organization terms as the developmental output.
- Core CC: extracellular region / apoplast (secreted). GO:0048046 apoplast (IDA) is the most precise and directly supported; GO:0005576 extracellular region (IEA/ISM) is a correct parent.
- GO:0005739 mitochondrion (ISM, AtSubP prediction GO_REF:0000122): biologically implausible for a secreted CLE peptide with an N-terminal signal peptide and experimentally demonstrated apoplastic secretion. Algorithmic mislocalization -> REMOVE.
- GO:0045087 innate immune response (IDA, PMID:21499263) vs GO:0002221 NOT (IEP, PMID:22923673): the two annotations are contradictory and both are in the GOA. The community has been unable to reproduce CLV3p-FLS2 immunity; the NOT annotation is the more recent consensus. Treat innate immune response as not a core function (MARK_AS_OVER_ANNOTATED / contested), and ACCEPT the NOT annotation that records the refutation. Per CLAUDE.md, do not REMOVE the experimental IDA; mark it as over-annotated/contested and retain the negation.

## Augmentation: Falcon/Edison deep-research report (2026-06-15)

Incorporated `CLV3-deep-research-falcon.md` (AI-generated GO-focused literature
synthesis) as supporting context. Added it to the top-level `references:` list and
attached verbatim supporting_text quotes to the most important annotations and core
functions (receptor S/T-kinase binding GO:0033612, cell-cell signaling in cell fate
commitment GO:0045168, maintenance of meristem identity GO:0010074, apoplast
GO:0048046, and both core_functions).

No existing action verdicts were flipped. The Falcon report is fully concordant with
the prior review: it endorses extracellular/apoplastic ligand activity, CLV1/BAM/CLV2
receptor binding, and the CLV3-WUS feedback loop, and it explicitly treats
apoptosis/immunity/inflammatory/neuronal roles and cytosolic/nuclear localization as
unsupported. This corroborates (does not contradict) the existing MARK_AS_OVER_ANNOTATED
verdict on innate immune response (GO:0045087) and the REMOVE verdict on mitochondrion
(GO:0005739) — a sentence was appended to the GO:0045087 `reason` recording this.

Caveat recorded in the reference_review: the report is LLM-generated; individual claims
should be traced to primary literature before being treated as definitive.
