# cem1: functional evidence

Cem1 is a mitochondrial beta-ketoacyl-ACP synthase of the dissociated type II fatty-acid synthesis machinery. Its conserved ketoacyl-synthase domains and catalytic residues support malonyl-ACP-dependent two-carbon acyl-chain extension. Transfer from characterized mitochondrial OXSM/Cem1 homologs supports a role in producing acyl-ACP intermediates needed for mitochondrial metabolism, while its exact substrate range in fission yeast remains unresolved.

- [file:SCHPO/cem1/cem1-uniprot.txt] "DR   InterPro; IPR000794; Beta-ketoacyl_synthase."
- [PMID:15668256] "The enzyme can elongate acyl-chains containing 2-14 carbon
atoms with malonyl moieties attached in thioester linkage to the human
mitochondrial acyl carrier protein and is able to restore growth to the
respiratory-deficient yeast mutant cem1 that lacks the endogenous mitochondrial
beta-ketoacyl synthase and exhibits lowered lipoic acid levels."

Evidence interpretation: sequence/domain records are used for family placement; AI descriptions and ARBA labels are not independent validation. Family transfer is limited to conserved properties and is identified as inference. Genome-scale localization annotations are retained where consistent with the biology; an abstract does not expose every individual observation. All original annotation rows are preserved.

ProtNLM provenance: pre-release `post-processed-2026_02_28k.xml`, exact entry and all evidence keys preserved in the source XML/JSON. These current Swiss-Prot entries are absent from the public TrEMBL pilot. Known-function overlap does not establish model training membership. See the function sidecar for atom-by-atom paragraph assessments.

Research provenance: the gene-focused Falcon report was generated concurrently with publication caching. The report was inspected for source leads; the biological decisions above rely on the cited primary records and specified family evidence.

The completed Falcon search has retrieval gaps: its inability to locate target-level localization is not used to override PomBase’s HDA records. Curated genomic-screen observations and the directly inspected papers take precedence over an empty literature-search result.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all 10 GOA rows, the description and core functions. ProtNLM2 files were not opened or used.

Identity: O94297 is the canonical, reviewed Swiss-Prot entry for SPBC887.13c (426 aa, sequence version 1). It is not an isoform, fragment or alternative gene model. Full KS3 domain (19-423) after an 18-residue predicted transit peptide; catalytic Cys-His-His triad intact (verified on the UniProt sequence: C170 in TTACAAG, H311 in INAHATS, H351 in SIGHLLG) [file:SCHPO/cem1/cem1-uniprot.txt "FT   ACT_SITE        170"]. mtKAS enzymes use this triad [PMID:17242430 "KASes catalyze the C(2) fatty acid elongation reaction using either a Cys-His-His or Cys-His-Asn catalytic triad."].

Evolutionary grounding: PANTHER PTHR11712:SF336 ("3-OXOACYL-[ACYL-CARRIER-PROTEIN] SYNTHASE, MITOCHONDRIAL"), shared with S. cerevisiae CEM1 (P39525), human OXSM (Q9NWU1), mouse Oxsm and bovine OXSM. SF336 is broad (it also contains bacterial FabF/KasA/KasB and Streptomyces aromatic-PKS KS-alpha subunits), so the tighter grounding is the PAINT eukaryotic node PTN000918585 (taxon Eukaryota; mitochondrion IBD seeded by human OXSM and T. brucei Q586W9), from which cem1 inherits its mitochondrion IBA. The KAS activity and fatty acid biosynthesis IBDs sit on the deeper node PTN000918584. PAINT did not propagate lipoate biosynthesis; treated as deliberate, no NEW term proposed. The family-level NOT mitochondrion (PTN000196554, taxon:272561, Chlamydia) does not cover cem1.

Key ortholog evidence: human OXSM elongates C2-C14 acyl-ACP and rescues budding-yeast cem1 [PMID:15668256 "is able to restore growth to the respiratory-deficient yeast mutant cem1 that lacks the endogenous mitochondrial beta-ketoacyl synthase and exhibits lowered lipoic acid levels"]; budding-yeast cem1 null is respiratory deficient with unchanged bulk mitochondrial fatty acids [PMID:8412701 "Inactivation of this gene leads to a respiratory-deficient phenotype."]. The only S. pombe experimental datum is the ORFeome YFP localisation screen [PMID:16823372] (HDA mitochondrion, abstract-only cache; deferred to PomBase). Falcon deep research found no S. pombe-specific functional paper.

Decisions: GO:0004315 (IBA, IEA, ISS) ACCEPT; GO:0005739 (HDA, IBA, IEA) ACCEPT; GO:0006633 (IBA, IEA) ACCEPT; GO:0016746 and GO:0016747 (InterPro2GO) MODIFY -> GO:0004315. Actions unchanged from the previous review, but supporting evidence rewritten: the previous mitochondrion rows quoted the record's own `DR GO` line (restates the annotation), now replaced with the HDA paper, the transit peptide and the OXSM targeting sequence. PMID:17242430 was listed but uncited; it now supports the catalytic triad and single-mtKAS claims. Added PMID:8412701 and reference_review entries. Description rewritten to drop workflow language.

Relative: closest characterised ortholog in the same subfamily and eukaryotic clade is S. cerevisiae CEM1 (P39525), reviewed at genes/yeast/CEM1/CEM1-ai-review.yaml (status COMPLETE). Human OXSM (biochemical seed) has no review in the repo.

PANTHER family review (interpro/panther/PTHR11712/PTHR11712-review.yaml) places O94297 in SF336; agrees with UniProt. No placement disagreement. Modules: modules/type_ii_fatty_acid_synthesis.yaml (bacterial and mitochondrial FAS II; lists yeast CEM1), modules/endogenous_protein_lipoylation.yaml (downstream octanoyl-ACP use), modules/fatty_acid_de_novo_synthesis.yaml (mentions yeast CEM1 as mtFAS II); S. pombe cem1 itself is not a module part.
