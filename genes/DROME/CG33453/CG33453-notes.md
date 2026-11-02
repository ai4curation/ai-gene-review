# CG33453 review notes

A0A0B4LFV5 is the 174 aa PB isoform, independently linked by FlyBase to FBpp0309413. The [same-gene comparison](CG33453-bioinformatics/RESULTS.md) supports a native short isoform, not wrong sequence. DUF1091 and a signal peptide provide fold/localization leads without identifying a molecular activity.

The enzyme-activator prediction remains UNC because no specific enzyme partner or activation mechanism is established. The ganglioside-catabolism prediction is NPI/PATHWAY_CONTEXT_IGNORED: [PMID:29844375](https://pubmed.ncbi.nlm.nih.gov/29844375/) reports undetectable endogenous gangliosides and engineered reconstitution in flies. The study distinguishes fly mactosylceramide metabolism from the mammalian lactosylceramide/ganglioside pathway. This is not a blanket claim that flies lack sialic acid: glycoprotein sialylation is distinct. The claim under review is a native evolved pathway, not possible turnover of experimentally introduced gangliosides. Human P17900 and macaque Q8HXX6 donor source records are retained.

All three ND GOA root rows remain non-core unknown markers. No speculative positive core molecular function is added. The full original prediction JSON preserves all TM-align scores and source identifiers.

## Provider research assessment

The Falcon synthesis finds no target-specific biochemical function and distinguishes CG33453 from the separate DUF1091 genes daedalus and decima. Its CheA/CheB family discussion suggests secreted chemical-signal handling but does not establish enzyme activation or ganglioside turnover. Exact PB identity and signal-peptide evidence are independently recorded locally; the published endogenous-ganglioside constraint remains the basis for the negative process assessment.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Sources: UniProt A0A0B4LFV5 and A1ZBI2 records, the Falcon deep research, the cached full text of PMID:32502405, QuickGO, and a new local analysis ([RESULTS-rereview.md](CG33453-bioinformatics/RESULTS-rereview.md)).

### Identity of the benchmark accession

- A0A0B4LFV5 is CG33453-PB (174 aa, FBpp0309413), an alternative isoform of FBgn0053453. The other product, CG33453-PA, is A1ZBI2 (175 aa, FBpp0085748). A1ZBI2 is the older TrEMBL entry and carries the STRING, PaxDb, eggNOG and OMA cross-references, so I treat it as the gene's canonical product. Neither entry is Swiss-Prot reviewed.
- PB is not a fragment and is not missing any domain. The new indel mapping shows that PB lacks a two-residue SV block at PA 20-21, inside the predicted signal peptide (SignalP 1..22 in PB, 1..23 in PA), and carries one extra valine at PB 126 in the mature DUF1091 chain (CPYVGLQ vs CPYGLQ). There are no substitutions. The earlier RESULTS.md phrase "different short N termini" understates this; that file is left unchanged.
- QuickGO gives the same three ND root rows (GO_REF:0000015) for both A0A0B4LFV5 and A1ZBI2.

### Evolutionary context

- PANTHER PTHR20898 ("DAEDALUS ON 3-RELATED-RELATED"), subfamily SF0. UniProt 2026_03: 3090 entries, 2997 in Diptera, 1812 in Drosophilidae, 102 in D. melanogaster, 0 reviewed; 3086 are insects, plus four Aspergillus entries not examined. This is an insect-restricted family with a large dipteran expansion, and there is no vertebrate ortholog.
- No IBA rows exist for CG33453, and there is no PAINT-curated function anywhere in the family.
- The only experimentally studied member of SF0 is daedalus/CG33690 (Q4ABJ0). Wilson et al. 2020 [PMID:32502405 "No biological function has been suggested for dls, and the protein it encodes contains a conserved domain of unknown function (InterPro DUF1091)."]. Its diet-dependent climbing and activity phenotypes are organismal phenotypes of a distinct paralog and are not transferred. decima/CG34351 is in a different family (PTHR21029).
- The deep research's CheA/CheB chemosensory hypothesis rests on family-level expression of other CheA members and a weak, remote profile link to CheB (Torres-Oliva et al. 2016, GBE, doi:10.1093/gbe/evw108; no PMID in Europe PMC, not cached). It is recorded only as a hypothesis in suggested_questions and suggested_experiments.

### Annotation decisions

- All three ND root rows (MF, CC, BP) changed from KEEP_AS_NON_CORE to ACCEPT. The ND assertion is the correct statement of current knowledge: the literature search found nothing gene-specific and no family member has a known function. ACCEPT follows the convention used for ND roots in other DROME reviews.
- No NEW annotations. An extracellular-region CC term would rest only on a SignalP prediction. Process terms (chemosensation, locomotion) would rest on paralog phenotypes or family expression, which fails the evolutionary-grounding and participation tests.
- core_functions stays empty, because no function is established.
- The description was rewritten to state the family placement, the isoform structure and the absence of known function.
- Added references: PMID:32502405, the Falcon deep-research file and RESULTS-rereview.md. The flybase.txt and RESULTS.md references are kept although no row quotes them any more.

### Family review and modules

- interpro/panther/PTHR20898/PTHR20898-review.yaml places CG33453 (A0A0B4LFV5) in SF0, which agrees with the UniProt cross-references for both isoforms. There is no disagreement about the subfamily.
- No module in modules/ mentions CG33453, PTHR20898 or DUF1091.

### Next relative

Because the benchmark accession is the PB isoform and the canonical PA product A1ZBI2 has no review in the repo, the next relative is A1ZBI2 (same gene, canonical). Its folder would be genes/DROME/CG33453__A1ZBI2. It is expected to reach the same conclusions. There is no characterised ortholog to choose instead: the nearest experimentally studied paralog, daedalus, has phenotypes only.
