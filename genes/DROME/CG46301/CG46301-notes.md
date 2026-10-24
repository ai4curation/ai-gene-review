# CG46301 (A0A1W5PXH3): evidence and ProtNLM claim review

CG46301 is a 1237-residue NOL4/NOL4L-family protein with a nucleolar-protein-4 helical domain. Its gene model incorporates the CG17341 and CG16879 names. A nuclear location is inferred by curated similarity annotation, while its molecular activity and the role of its extended sequence remain unresolved.

Exact input: [A0A1W5PXH3](https://www.uniprot.org/uniprotkb/A0A1W5PXH3/entry), 1237 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG46301-predictions-source.json](CG46301-predictions-source.json). Source features: [CG46301-uniprot.txt](CG46301-uniprot.txt), with an exact extraction in [CG46301-sequence-evidence.json](CG46301-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR056549; HTH_NOL4.
DR   InterPro; IPR039788; NOL4/NOL4L.
FT   DOMAIN          789..886
FT                   /note="Nucleolar protein 4 helical"
FT                   /evidence="ECO:0000259|Pfam:PF23079"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Nucleolar protein 4 | CNN | IPR039788 establishes NOL4/NOL4L-family membership and PF23079 identifies a nucleolar-protein-4 helical domain. The family-level name is supported; the wording alone is not evidence of nucleolar localization or a specific NOL4 paralog. |
| Location | Nucleus (SL-0191) | LSP | The existing curated ISS nucleoplasm annotation is a more specific nuclear location. Family architecture supports this inference without establishing a nucleolar role. |

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0003674 molecular_function (ND): **ACCEPT**. NOL4/NOL4L family assignment and the helical domain are insufficient to specify an enzymatic or RNA-processing activity.
- GO:0005654 nucleoplasm (ISS): **ACCEPT**. The NOL4/NOL4L assignment supports the existing ISS nuclear localization inference; there is no target-specific evidence contradicting it. The name nucleolar protein does not by itself establish nucleolar residence.
- GO:0008150 biological_process (ND): **ACCEPT**. The exact 1237-residue gene model contains NOL4-family sequence but no directly characterized biological process is established.

## Research assessment

The Falcon source leads do not establish a fly-specific molecular activity. PMID:25366156 studies murine NOL4 splice variants interacting with mouse Mlr proteins; use of Drosophila S2 cells as an assay host does not make the assayed NOL4 a fly gene product. The exact NOL4-family architecture and existing curated ISS support a nuclear inference, with no transfer of the mouse transcriptional mechanism.

Provider output: [CG46301-deep-research-falcon.md](CG46301-deep-research-falcon.md). Primary papers and source records, rather than provider verdicts, support the assessment.

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This pass uses no ProtNLM2 output. It re-examines identity, family placement and all three GOA rows.

### Identity of the benchmark accession

UniProt lists four unreviewed products for FBgn0283651 (CG46301), and no Swiss-Prot entry:
A0A1W5PXH3 (1237 aa), A0A1W5Q009 (636), A0A1W5PVN5 (667) and A0A1W5PW03 (623). In local alignment
([RESULTS-rereview.md](CG46301-bioinformatics/RESULTS-rereview.md), script
`compare_isoforms_rereview.py`), A0A1W5PVN5 and A0A1W5PW03 match A0A1W5PXH3 residues 1-614 at 100% identity,
and A0A1W5Q009 matches 615-1237 at 100%. Only A0A1W5PXH3 and A0A1W5Q009 contain the HTH_NOL4 domain
(PF23079, 789-886 on A0A1W5PXH3). A0A1W5PXH3 is therefore the longest, most complete product, joining the
former CG17341 (N-terminal) and CG16879 (C-terminal) regions. It is the accession PANTHER 19.0 uses for the
gene. It is not a fragment or an aberrant model. No reviewed canonical entry exists for any other accession.

### Evolutionary placement

PANTHER: PTHR12449 (official name "DEATH DOMAIN-CONTAINING PROTEIN"), subfamily SF22 "NUCLEOLAR PROTEIN 4".
Vertebrate NOL4 is in SF17 (human O94818, mouse P60954) and NOL4L in SF19 (human Q96MY1, mouse Q6DIB4). The
PANTHER 19.0 fruit-fly classification file has only this one PTHR12449 gene. The fly HTH_NOL4 domain is
80% identical to human NOL4 and 82% to human NOL4L over 95 aa. Over the full length, the fly protein aligns
with human NOL4 from residue 73 to 924 (44% identity over 523 aligned residues), so the long fly product has
NOL4-like N-terminal sequence and is not just the helical domain. This fits a single invertebrate
co-ortholog of both vertebrate paralogs, but no tree was built. There are no PAINT/IBA annotations for this
gene.

### Literature

The literature search (falcon deep research, PubMed-cached leads) found no study of the fly gene product.
The only family-level experiment is PMID:25366156 (mouse NOL4 splice variants bind and modulate the
Mblk-1-related TFs Mlr1/Mlr2; S2 cells were only the reporter host). The partners and variant-specific
effects belong to vertebrate SF17 and are not transferred.

### Annotation decisions (re-review)

- GO:0003674 (ND): ACCEPT. No activity has been demonstrated.
- GO:0005654 nucleoplasm (ISS from human NOL4L): ACCEPT. Nucleoplasm localization (HPA) is reported for
  both vertebrate paralogs, so it is a family-level property and the fly helical domain matches both.
  Nucleolar residence is not inferred.
- GO:0008150 (ND): ACCEPT. No process has been established.

No NEW terms. Core functions are left empty because no molecular activity is supported.

### Relative to review next

There is no reviewed canonical entry for this gene, and A0A1W5PXH3 is already the full-length product, so
the next relative is the closest characterized vertebrate family member. Human NOL4 (O94818, SF17) has the
widest sequence coverage of the fly protein and is the human counterpart of the only experimentally studied
member (mouse Nol4, PMID:25366156). The repo has no review of NOL4, Nol4 or NOL4L.

### Family review

interpro/panther/PTHR12449/PTHR12449-review.yaml lists CG46301 under SF22. That agrees with the UniProt and
PANTHER classification files, so there is no disagreement about subfamily placement. No modules or GO-CAM
models contain this gene.
