# CG32354 (Q9VSK1): evidence and ProtNLM claim review

CG32354 is a 662-residue protein with seven Kazal-like domains and a predicted N-terminal membrane-spanning segment. It is compatible with an extracellular or cell-surface interaction protein; intrinsic protease-inhibitor activity, soluble secretion, and the precise developmental role remain unresolved.

Exact input: [Q9VSK1](https://www.uniprot.org/uniprotkb/Q9VSK1/entry), 662 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG32354-predictions-source.json](CG32354-predictions-source.json). Source features: [CG32354-uniprot.txt](CG32354-uniprot.txt), with an exact extraction in [CG32354-sequence-evidence.json](CG32354-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR002350; Kazal_dom.
DR   InterPro; IPR036058; Kazal_dom_sf.
DR   InterPro; IPR050653; Prot_Inhib_GrowthFact_Antg.
FT   TRANSMEM        57..78
FT                   /note="Helical"
FT                   /evidence="ECO:0000256|SAM:Phobius"
FT   DOMAIN          158..214
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          215..268
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          270..322
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          374..432
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          438..495
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          497..550
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
FT   DOMAIN          600..652
FT                   /note="Kazal-like"
FT                   /evidence="ECO:0000259|PROSITE:PS51465"
```

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Kazal-like domain-containing protein | CNN | Seven domain features and PROSITE PS51465 independently establish the Kazal-like architecture. This validates the domain name without asserting serine-protease inhibition. |
| Location | Secreted (SL-0243) | UNC | The extracellular IBA supports an exposed or extracellular protein region, but the exact source has a transmembrane segment at residues 57-78 and no cleavable signal-peptide feature. An ectodomain on a membrane-tethered protein is not equivalent to soluble secretion; topology or shedding evidence is needed. |

## 2026-09-28 IBA re-review

PTHR10913 is a heterogeneous follistatin/Kazal family. The current PAINT snapshot records `GO:0005576` on `PTN000099217` with `taxon:2759` and `GO:0030154` on `PTN000099219` with no taxon value; the empty PTN000099219 taxon and the same PTN's appearance in the unrelated PTHR21632 slice mean the cached TSV alone does not establish it as the PTHR10913 root. The more specific activin/TGF-beta-binding assertions are instead on `PTN001657053` with `taxon:6072` and no corresponding `GO:0048185`, `GO:0030510`, or `GO:0032926` rows in `CG32354-goa.tsv`, so CG32354 is not receiving those follistatin-specific functions.

This supports keeping extracellular region as a broad, non-committal IBA: the transmembrane segment plus seven Kazal-like domains are compatible with a surface or exposed ectodomain. It does not convert the protein into a soluble secreted protein or establish either a specific serine-protease inhibitor activity or follistatin-like growth-factor antagonism.

The cell-differentiation IBA should stay unresolved. The PAINT source node aggregates heterogeneous extracellular descendants, including identifiable FSTL3/FST seeds plus unresolved FlyBase, MGI, UniProt and ZFIN seeds, and the CG32354 branch has no direct developmental-process assay or molecular target.

Exact searches for `Q9VSK1`, `CG32354`, `FBgn0052354` and `CG7159` did not recover a recent target-specific functional paper. The FlyBase/NCBI-linked full-text paper from Firth et al. reports `CG32354` among "`10 genes upregulated in GMR>sSpi: CG32354`" in the Drosophila eye-disc peripodial-epithelium screen [PMID:17553483, "Spitz from the retina regulates genes transcribed in the second mitotic wave, peripodial epithelium, glia and plasmatocytes of the Drosophila eye imaginal disc"], but this is expression-screen evidence, not a direct assay of CG32354 localization, molecular function or developmental participation.

## Literature evidence

No target-specific primary finding is used to establish a molecular activity here. The current assessment is bounded by exact-record architecture and the explicitly identified curated inferences.

## Annotation decisions

- GO:0004867 serine-type endopeptidase inhibitor activity (IEA): **UNDECIDED**. Repeated Kazal-like domains support a protease-interaction hypothesis, but the exact inhibitory loops and target protease have not been functionally resolved. This fold also occurs in non-inhibitory extracellular proteins.
- GO:0005576 extracellular region (IBA): **KEEP_AS_NON_CORE**. Seven Kazal-like domains and an N-terminal hydrophobic segment support the existing curated IBA extracellular localization. This does not imply release as a soluble secreted protein or a resolved core function.
- GO:0030154 cell differentiation (IBA): **UNDECIDED**. Extracellular Kazal-domain proteins can have regulatory or structural functions; family architecture does not establish which differentiation process this fly protein participates in. The ancestral assertion and target function need resolution.

## Research provenance

Genuine external literature research is requested through the repository Falcon wrapper, with perplexity-lite configured as fallback. Provider output is retained separately as `CG32354-deep-research-<provider>.md`; its source leads are checked against the underlying publications and exact sequence record.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** Q9VSK1 (662 aa, TrEMBL, PE 4) is the only UniProt entry cross-referenced to FlyBase FBgn0052354 (UniProt query `xref:flybase-FBgn0052354`), so the benchmark accession is the canonical product of this gene, not an isoform, fragment or alternative gene model. UniProt now gives the gene name as CG7159 (GOA uses this symbol); CG32354 is the FlyBase annotation ID used for this folder. The sequence has seven PROSITE PS51465 Kazal-like domains (158-652), an N-terminal disordered region (1-31), a single Phobius helix at 57-78 and no SIGNAL feature.

**Phylogeny** (`CG32354-bioinformatics/panther_tree_rereview.py`, `RESULTS-rereview.md`). In the PANTHER 19 PTHR10913 tree, Q9VSK1 descends from PTN000099217 (Eukaryota root) and PTN000099219 (Eumetazoa duplication), the two nodes that give it IBA annotations. This settles the earlier uncertainty about PTN000099219, which arose because the cached PAINT slice had no taxon for it. The nearest relatives are the fly paralogs Fs, CG12716 and anon-f (LCA PTN002588941, Hexapoda-Crustacea duplication). Worm ZK813.6/F29G6.1 are uncharacterised Ecdysozoa orthologs. Human SPINK5 and TMEFF2 (and TMEFF1) are many-to-many co-orthologs via the Bilateria speciation node PTN000857333. FST/FSTL3 are distant paralogs (Eumetazoa duplication). SF79 has about 291 UniProt members: all are arthropods except one Trichoplax entry, and none is reviewed.

**PAINT decisions treated as deliberate.** PAINT placed GO:0004867 only on PTN000099251 (Theria, SPINK5) and the activin-binding terms only on PTN001657053 (taxon:6072 in the PAINT slice; a node in the follistatin/FSTL3 lineage). Neither node is an ancestor of CG32354, so no subfamily-specific function is transferred.

**Annotation decisions (revised).**
- GO:0004867 serine-type endopeptidase inhibitor activity (IEA, UniRule): UNDECIDED, unchanged. The rationale is now phylogenetic: PAINT did not propagate the activity, the domains are of the KAZAL_FS type, UniProt flags a residue caution, and the P1 residues are mixed (P, T, S, K, K, R, R).
- GO:0005576 extracellular region (IBA): KEEP_AS_NON_CORE, unchanged. The source node was verified as an ancestor. Topology (signal-anchored vs secreted) is unresolved.
- GO:0030154 cell differentiation (IBA): changed from UNDECIDED to KEEP_AS_NON_CORE. The source node is now confirmed as an ancestor, and there is no evidence of loss. The term is broad and untested for CG32354.

**Literature.** A PubMed search for CG32354 OR FBgn0052354 OR CG7159 returned 0 records (2026-10-21). The only target mention is the full-text eye-disc expression screen [PMID:17553483 "10 genes upregulated in GMR>sSpi: CG32354"]. No Falcon re-run: the existing deep-research file reports no target-specific primary literature.

**Relative for next review.** Human SPINK5 (Q9NQ38) is the best-characterised co-ortholog by tree (Bilateria speciation node PTN000857333) and has no review in the repo. Fs (Q86NV3) is the phylogenetically closer fly paralog and is also unreviewed. No module in `modules/` includes CG32354. `modules/dmel_activin_signaling.yaml` mentions Follistatin only as an extracellular regulator.
