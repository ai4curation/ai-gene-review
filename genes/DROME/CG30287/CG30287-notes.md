# CG30287 (Q8MLV8): evidence and ProtNLM claim review

CG30287 is a predicted secreted S1-family serine endopeptidase with an intact annotated catalytic triad. The 284-residue product is also called SP224 and historically SPH37, but the latter name alone does not establish catalytic inactivity. Its physiological substrates and relationship to vertebrate PRSS55 remain unresolved.

Exact input: [Q8MLV8](https://www.uniprot.org/uniprotkb/Q8MLV8/entry), 284 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG30287-predictions-source.json](CG30287-predictions-source.json). Source features: [CG30287-uniprot.txt](CG30287-uniprot.txt), with an exact extraction in [CG30287-sequence-evidence.json](CG30287-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR009003; Peptidase_S1_PA.
DR   InterPro; IPR001314; Peptidase_S1A.
DR   InterPro; IPR051487; Ser/Thr_Proteases_Immune/Dev.
DR   InterPro; IPR001254; Trypsin_dom.
DR   InterPro; IPR018114; TRYPSIN_HIS.
DR   InterPro; IPR033116; TRYPSIN_SER.
FT   SIGNAL          1..21
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          42..282
FT                   /note="Peptidase S1"
FT                   /evidence="ECO:0000259|PROSITE:PS50240"
FT   ACT_SITE        82
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        136
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        232
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
```

At the annotated catalytic positions, direct indexing of the exact sequence gives: H82, D136, S232. These positions come from PROSITE features, not a new alignment; no substrate preference or assay result is inferred.

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Serine protease 55 | UNC | Serine-protease potential is supported by the intact annotated triad, but the vertebrate PRSS55-specific name exceeds the evidence. Q6UWB4 is a human PRSS55 source; a similarity hit without resolved orthology or conserved physiological function does not establish that precise identity in fly. |
| Location | Secreted (SL-0243) | CNN | The SignalP signal peptide at residues 1-21 and soluble S1-domain architecture support secretion, consistent with the curated extracellular IBA. This does not identify a reproductive substrate or PRSS55-specific function. |

## Literature evidence

- [PMID:30367934](https://pubmed.ncbi.nlm.nih.gov/30367934/): “The SP-related sequences in each species were divided into SPs or SPHs based on the presence or absence of the His-Asp-Ser catalytic triad”

## Annotation decisions

- GO:0004252 serine-type endopeptidase activity (IBA): **ACCEPT**. H82 D136 and S232 are retained at the annotated catalytic sites in the S1 domain. The historical SPH37 alias is insufficient to call it a pseudoenzyme.
- GO:0004252 serine-type endopeptidase activity (IEA): **ACCEPT**. The exact record has an intact annotated H-D-S catalytic triad and a complete S1 domain, supporting the existing broad activity mapping.
- GO:0004252 serine-type endopeptidase activity (ISM): **ACCEPT**. PMID:30367934 distinguishes SPs from SPHs using catalytic-residue conservation. The exact sequence has H82 D136 S232 at the annotated sites, supporting proteolytic potential despite older SPH naming.
- GO:0005576 extracellular region (IBA): **ACCEPT**. A SignalP signal peptide at residues 1-21 and a soluble mature S1-domain architecture support the curated IBA.
- GO:0006508 proteolysis (IBA): **ACCEPT**. The catalytic triad is retained in the S1 domain; no specific physiological substrate is established.
- GO:0006508 proteolysis (IEA): **ACCEPT**. The annotated H-D-S residues are present and no loss-of-catalysis conclusion follows from the historical SPH37 alias.
- GO:0008233 peptidase activity (IEA): **MODIFY**. The intact S1 catalytic architecture supports the more informative peptidase class.
- GO:0016787 hydrolase activity (IEA): **MODIFY**. The exact domain and catalytic residues support serine-type endopeptidase activity.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG30287-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: I re-examined every existing annotation, the description and the core function from the UniProt record, the cited literature, the Falcon deep research, and the PANTHER 19.0 tree. I did not consult ProtNLM2 output. New analysis: `CG30287-bioinformatics/sequence_features_rereview.py` and `RESULTS-rereview.md`.

Identity: Q8MLV8 is the canonical and only UniProt product of FBgn0050287: 284 aa, sequence version 1, complete from signal peptide to C-terminus. It is not a fragment, isoform or alternative gene model.

Sequence:
- Intact triad: His82, Asp136, Ser232 (GDSGGP).
- S1-pocket position 189 is Ser226, so not trypsin-like Asp. P1 specificity is not assigned.
- Candidate activation cleavage after Arg41, giving the atypical mature N-terminus VINGK.
- The 20-residue propeptide has one Cys and no clip domain. UniProt's ARBA "CLIP subfamily" statement is therefore not supported.
- The UniProt CAUTION about missing conserved residues refers to ProRule feature propagation, not to the triad.

Literature: no gene-specific study exists. The deep research confirms this and warns that the Skanda findings (CG15046) do not apply to CG30287. PMID:30367934 classifies SP and SPH by triad retention, which is the basis for the ISM row.

Evolution: CG30287 is in PTHR24256:SF553 (IP20273P-RELATED), an insect clade (PTN002799547) whose nine *D. melanogaster* members include Jon99Ciii and CG4914. That clade sits in an unresolved polytomy with the Easter/Sp7/CLIPB clade, the SP20/tpr clade, CG11836, and the CG30288 clade. The GO:0004252, GO:0006508 and GO:0005576 IBDs are at PTN001207268, which is on the CG30287 lineage. None of the NOT|GO:0004252 IKR nodes is an ancestor of CG30287. The innate-immune-response IBD (PTN000667087) is not on its lineage either. I treat that omission as deliberate and propose no immune process term.

Not transferred:
- Vertebrate PRSS55 lies in a different PANTHER family (PTHR24253:SF90), so it is not a relative.
- Easter's patterning and Spätzle roles are subfamily-specific (SF527, clip-domain protease) and are not transferred.

Decisions:
- ACCEPT GO:0004252 (IBA, IEA and ISM).
- ACCEPT GO:0005576 (IBA).
- ACCEPT GO:0006508 (IBA and IEA).
- MODIFY GO:0008233 and GO:0016787 to GO:0004252.

Description rewritten: I removed the PRSS55 framing and added the facts that the protein has no clip domain and belongs to subfamily SF553.

Relative for next review:
- No SF553 member has a characterised function. CG4914 and Jon99Ciii have only HDA serine-hydrolase rows from ABPP (PMID:33827210).
- The nearest well-characterised relative by tree placement is Easter (ea, P13582). It is in the sister clade of the PTN002799546 polytomy and is a donor of the PTN001207268 catalytic-activity IBD. The repo has no review for it.

Family review: `interpro/panther/PTHR24256/PTHR24256-review.yaml` lists Q8MLV8 under "Benchmark members without resolved subfamily placement". PANTHER 19.0 does resolve it to SF553. There is no disagreement about function.

Modules: no module contains CG30287. `modules/dmel_toll_signaling.yaml` covers Drosophila extracellular protease signalling, but nothing places CG30287 in it.
