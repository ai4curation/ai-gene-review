# CG13096 (H0RNN8): evidence and ProtNLM claim review

CG13096 is a 681-residue protein containing ribosomal-uL1-like domains associated with ribosome biogenesis proteins. Its architecture suggests an RNA-associated role, but the exact molecular activity, RNA substrate, and localization of this fly product remain unresolved.

Exact input: [H0RNN8](https://www.uniprot.org/uniprotkb/H0RNN8/entry), 681 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG13096-predictions-source.json](CG13096-predictions-source.json). Source features: [CG13096-uniprot.txt](CG13096-uniprot.txt), with an exact extraction in [CG13096-sequence-evidence.json](CG13096-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR053110; Ribosomal_L1-TF.
DR   InterPro; IPR023674; Ribosomal_uL1-like.
DR   InterPro; IPR028364; Ribosomal_uL1/biogenesis.
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Uncharacterized protein | UNC | Uncharacterized protein supplies no testable function. Ribosomal-uL1-like architecture narrows the likely biology but does not establish an intrinsic ribosomal-subunit role. |
| Location | Nucleolus (SL-0188) | UNC | Ribosomal-uL1-like domains occur in ribosome-biogenesis factors and make nucleolar localization plausible. The exact target has no localization experiment or curated GO localization in the retrieved evidence, so nucleolar residence is not established. |
| Location | Nucleus (SL-0191) | UNC | A nuclear location is compatible with ribosome biogenesis but is not established solely by the uL1-like fold. The exact target needs localization or a well-resolved characterized ortholog inference. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

The accession-specific GOA fetch contains no existing annotation rows. The molecular activity remains unresolved; no broad GO root or invented function is added to create apparent coverage.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG13096-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output and the prediction files were not used in this section.

### Identity of the benchmark accession

- H0RNN8 is an unreviewed TrEMBL entry for the FI17503 cDNA clone (EMBL AEW48266.1). Its 681-residue sequence is identical to the reviewed Swiss-Prot canonical entry Q9VLK2 ("Ribosomal L1 domain-containing protein CG13096", FBgn0032050) [file:DROME/CG13096/CG13096-bioinformatics/RESULTS.md "H0RNN8 length 681; Q9VLK2 length 681; identical sequence: True"]. It is therefore neither a fragment, an isoform nor an alternative gene model, just a redundant record for the full-length product. A third redundant TrEMBL record, X2J965, carries the FlyBase synonym "UTP30".
- GOA has no rows for H0RNN8. Q9VLK2 has only three ND rows (GO_REF:0000015) for the MF, BP and CC roots, so FlyBase/UniProt found no published experimental basis for annotation.

### Domain architecture

From the UniProt record: N-terminal disordered region 1-248 (lysine/alanine-rich, basic), Pfam PF00687 / CDD cd00403 ribosomal-L1 domain in the middle, disordered acidic tail 579-681 (611-681 almost entirely D/E). That combination, a basic N-terminal region, an L1 fold and a long acidic tail, is typical of nucleolar ribosome-biogenesis factors and not of ribosomal proteins.

### Evolutionary placement (new analysis)

New script `CG13096-bioinformatics/l1_family_placement.py`, results in `CG13096-bioinformatics/RESULTS.md`.
- phmmer with CG13096 as query: top hits human RSL1D1 (E=3.8e-25), mouse Rsl1d1 (4.1e-25) and worm F53F4.11 (2.7e-21). Human RPL10A is much weaker (3.3e-06). There are no significant hits to the PANTHER co-members (Candida NRI1, Dictyostelium DDB_G0279335, VZV ORF11) or to mitochondrial uL1m.
- In the NJ tree CG13096 pairs with worm F53F4.11, apart from the NRI1/DDB_G0279335/VZV cluster. Deep internal branches are very short, so the branching order between lineages is unresolved.
- UniProt cross-references: CG13096, RSL1D1, yeast UTP30 and yeast CIC1 share eggNOG KOG1685 and OrthoDB 10251727at2759. Candida NRI1 (the PANTHER co-member) is in a different eggNOG/OrthoDB group (ENOG502QQIF; 4084568at2759).
- Alliance orthology: CG13096 maps to RSL1D1 (human, mouse, frog, zebrafish) by OrthoFinder, OrthoInspector, PhylomeDB and SonicParanoid, and to worm F53F4.11 by five methods including Ensembl Compara. PANTHER does not support either call.
- **PANTHER disagreement.** PANTHER 19.0 puts CG13096 in PTHR48162:SF1 (family "YALI0A06930P"), while RSL1D1, UTP30 and CIC1 are in PTHR23105 (SF31/SF203). No fly protein is assigned to PTHR23105:SF31 or SF203. The family review `interpro/panther/PTHR48162/PTHR48162-review.yaml` (functional_coherence UNKNOWN) lists only CG13096 and VZV ORF11 as SF1 members. It omits the Candida NRI1 and Dictyostelium DDB_G0279335 SF1 members that are in the PANTHER 19.0 classification files, and it does not mention that orthology resources other than PANTHER group CG13096 with RSL1D1. I read PTHR48162 as a split of a highly divergent sequence, not a functionally distinct subfamily. No PAINT node with experimental annotations covers CG13096, so no IBA-style transfer applies.
- CG13096 is not mitochondrial uL1m (mRpL1 = CG7494, PTHR36427) and not a cytoplasmic uL1 (RpL10Aa/RpL10Ab).

### Literature

- No peer-reviewed paper characterizes CG13096. The falcon deep research draws on one unpublished doctoral thesis (Hoecker 2022, Heidelberg, doi:10.11588/heidok.00031917). According to that report, the thesis names CG13096 "Centagon 3", one of four satellite-III-RNA-associated nucleolar proteins together with CG1234 (NOC3L-like), CG8545 (NOP2-like) and CG32344. It reports endogenous GFP knock-in localization to the nucleolus in ovarian germ and follicle cells, in vitro binding to satellite-III and tubulin RNA, and germline RNAi defects. I could not open the thesis (the Heidelberg repository returned an access-denied page). A web search snippet from the repository confirms the thesis and its general findings (nucleolar Centagon complex in ovarian germ and somatic cells; RNAi germline defects), but not the CG13096-specific details.
- The RNAi gonad phenotypes (germ-cell loss, fragmented nurse-cell nuclei, reduced hatching) are downstream organismal phenotypes. Per campaign rules they are not annotated as process participation.

### Decisions

- existing_annotations: none to review (GOA empty for H0RNN8; Q9VLK2 has only ND root annotations).
- No NEW annotations proposed. The only direct evidence is an unpublished, unverifiable thesis, FlyBase's ND indicates curators found no citable basis, and the family placement is contested. The validator warns that the core-function terms are not mirrored in existing_annotations; this is deliberate.
- core_functions: one hedged entry (RNA binding, nucleolus), supported by the thesis-relayed report and the family analysis, with a BIOLOGY knowledge gap on RNA targets and the ribosome-biogenesis step.
- Description rewritten without project or ProtNLM commentary.

### Relative to review next

The benchmark is the full-length product, and its canonical entry Q9VLK2 is the same gene in this folder, so the same_gene_canonical rule does not apply. The closest experimentally characterized relative is human RSL1D1 (O76021): nucleolar, with experimental UniProt function annotation. It is supported by orthology methods, eggNOG/OrthoDB and the phmmer/tree analysis, but not by PANTHER. The repo has no RSL1D1 review.

### Modules

None found in modules/ that include CG13096 (no ribosome-biogenesis/pre-ribosome module exists; `dmel_cytoplasmic_ribosome.yaml` and `dmel_mitochondrial_ribosome.yaml` do not and should not include it).
