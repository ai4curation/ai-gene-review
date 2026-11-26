# GNRHR (human, P30968) review notes

## 2026-11-26: de novo review

### Sources and searches

- `just fetch-gene human GNRHR`: 22 GOA rows, UniProt record, PANTHER family PTHR24241 (subfamily SF22).
- Deep research: no provider output is kept. Falcon and perplexity are not configured in this
  environment. Asta returned 20 papers retrieved on the wording of the prompt template (UniProt ID
  mapping, database papers), none on the receptor, so that file was discarded and not committed.
  The OpenScientist deep-research job (`just deep-research-openscientist human GNRHR`) ran for the
  two-hour limit and was stopped without writing a report.
- Own literature search, PubMed (E-utilities and the PubMed connector), 2026-11-26. Queries:
  "GnRH receptor mutants pharmacoperone misfolded rescue" (18 hits);
  "human gonadotropin-releasing hormone receptor structure (crystal OR cryo-EM)" from 2019 (13);
  "GNRHR mutations hypogonadotropic hypogonadism functional characterization" (45);
  "dominant-negative GnRH receptor mutants Leanos-Miranda"; "GNRHR heterozygous genetic load
  phenotypic spectrum Gianetti"; "gonadotropin-releasing hormone receptor Lys191 primate";
  "GnRH receptor carboxyl-terminal tail desensitization internalization"; "GnRH receptor[Title]
  signaling gonadotrope review Naor"; "GnRH pulse frequency gonadotropin subunit gene expression";
  "GNRHR hypogonadotropic hypogonadism reversal"; "GNRHR constitutional delay puberty heterozygous
  mutations"; "Gnrhr knockout mice gonadotrope hypogonadism". 46 papers were cached in
  `publications/`; 11 have full text, the rest are abstract-only.
- GO-CAMs: `gocams/index.tsv` has no row for GNRHR or P30968, so there is no model to review.

### What the gene product does

- Receptor for GnRH. The cloned human receptor binds GnRH analogues and signals
  [PMID:8386108 "Transfected COS-1 cells manifested a GnRH-stimulated increase in phosphoinositol
  turnover, with an EC50 of approximately 3 nM, which was inhibited by GnRH antagonists"].
- Coupling is to Gq/11 [PMID:10734055 "the murine and human GnRH receptors exclusively couple to
  G proteins of the G(q/11) family"]. In vivo, gonadotrope Gq/11 is what matters for basal
  fertility [PMID:34864945 "Gonadotrope-specific Gα q/11 knockouts exhibit hypogonadotropic
  hypogonadism and infertility, akin to the phenotypes seen in GnRH- or GnRHR-deficient mice"].
  A Gs contribution exists in a gonadotrope cell line and shows in mice only when GnRH drive is
  high (same paper), so cAMP signalling is not put in core_functions.
- No C-terminal tail [PMID:8386108 "most notably the lack of a cytoplasmic C-terminal domain"],
  hence no beta-arrestin recruitment or rapid desensitization [PMID:18039780 "they do not recruit
  beta-arrestin, nor do they undergo rapid desensitization"]. The crystal structure agrees: the
  chain ends at Leu328, the last residue of helix 7 (bioinformatics RESULTS.md).
- GnRH-II acts through this receptor in humans [PMID:15082521 "it appears that GnRH II signaling
  occurs through the type I GnRH receptor"].
- Inefficient folding of the human receptor, linked to Lys191 [PMID:10379888 "Deletion of Lys191
  from the human GnRH receptor caused a 4-fold increase in receptor expression in COS-1 and HEK 293
  cells"; PMID:16446355 "a higher percentage of human GnRHRs are misfolded structures"].
- Isoform 2 (truncated) is inactive and inhibits the full-length receptor in co-transfected cells
  [PMID:9259321 "the splice variant was incapable of ligand binding and signal transduction"].

### Disease mechanism (HH7), for the companion disease entry

- Mode: autosomal recessive, loss of function, from partial to complete. gnomAD: pLI 0.02,
  observed/expected loss of function 0.50; 40 predicted loss-of-function variants, no homozygotes.
- Dominant-negative: shown only in co-transfected cells [PMID:12843188 "Inhibition varied depending
  on the particular hGnRHR mutant coexpressed and the ratio of hGnRHR mutant to WT hGnRHR cDNA
  cotransfected"; PMID:15886197 "due to oligomerization and retention in the endoplasmic
  reticulum"]. Heterozygous parents in the recessive pedigrees are unaffected, so this is an in
  vitro property of misfolded mutants and not the inheritance mechanism. Among compound
  heterozygotes one mutant can lower the other's function [PMID:15728205].
- Gain of function: none reported in patients. Constitutively active mutants exist only as
  engineered helix 6 substitutions revealed after pharmacoperone rescue [PMID:22595961].
- Main molecular mechanism: misfolding and endoplasmic reticulum retention [PMID:12843188 "Loss of
  function by 11 of 13 naturally occurring mutations in the human GnRH receptor (hGnRHR) was thought
  to result from impaired ligand binding or effector coupling, but actually results from receptor
  misrouting"]. Structural counterpart: 30 of 39 modelled disease variants are buried, 19 classed
  as transmembrane core packing.
- Minority mechanisms: lowered GnRH affinity at extracellular positions (N10K, G99E, Q106R) and
  impaired G-protein coupling at the cytoplasmic interface (R262Q; R139H and R139C in the DRS motif).
- Phenotype is normosmic [PMID:11297587 "Five unrelated probands (3 men and 2 women), all
  normosmic"]. The defect is pituitary resistance to GnRH, not GnRH deficiency or failed GnRH
  neuron migration. The UniProt disease text and the disease name ("with or without anosmia") are
  the generic text of the hypogonadotropic hypogonadism series.
- Animal models: ENU Gnrhr mutant mouse [PMID:15625238], E90K knock-in mouse [PMID:22918878], and
  rescue of the knock-in by a pharmacoperone [PMID:24324164].

### Disagreements with sources

- E90-K121 salt bridge (PMID:19095769, repeated in PMID:22918878): contradicted by mutagenesis
  [PMID:30476558 "excluding a salt-bridge interaction"] and by 7BR3, where the side chains are
  9.9 A apart. Recorded as an OVERTURNED finding on PMID:19095769.
- UniProt lists P146S as an HH7 variant (from PMID:25077900, abstract-only here, and the abstract
  is about CHD7). gnomAD has it at 1.1e-3 with four homozygotes. Raised as a question, not as a
  source defect, because the paper's variant table was not read.

### Annotation decisions that needed thought

- GO:0007186 and GO:0016020 each get two different actions across rows. That follows the
  2026-11-14 ruling: the IBA and IEA rows stop at the general term (kept, or TOO_GENERAL for
  membrane), while the TAS rows cite papers whose own data support the specific term (MODIFY).
  `just validate` reports the mix as two warnings.
- GO:0032274 gonadotropin secretion (NAS) is corrected to positive regulation of gonadotropin
  secretion. The receptor signals for release; the secretory machinery does the releasing.
- No NEW rows. GO:0007200 is reached through a MODIFY replacement and core_functions.

### Family, module

- PTHR24241 family review added (GnRH receptor clade and the root nodes that reach GNRHR).
- The existing module `kndy_gnrh_pulse_generator` stops at GnRH release and names pituitary GnRHR
  signalling as downstream; see the module note for what was added.

### Left open

- OpenScientist hypothesis job on the penetrance question: see the history record for its state.

## 2026-11-26: distance correction

- The companion disease-entry session pointed out that PDB 9U4W is deposited with hydrogens and
  that `02_variant_structure.py` kept them on the GnRH and G-alpha-q side. Confirmed (8,486
  hydrogen atoms in the file) and fixed. Heavy-atom distances: R139 to G-alpha-q 3.7 A (was 3.0),
  P146 3.6 (was 2.8), R262 5.2 (was 4.4), Y283 to GnRH 2.8 (was 2.5). R262Q and R262W move from
  the computed interface class to unresolved, because R262 itself is outside the 4.5 A cutoff;
  its neighbours A261, K264 and T265 remain G-alpha-q contacts, and the published coupling defect
  is unchanged. No annotation action changes.
