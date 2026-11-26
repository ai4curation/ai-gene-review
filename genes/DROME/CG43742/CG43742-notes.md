# CG43742 (A0A0B4KFF2): evidence and ProtNLM claim review

CG43742 is a secretory serine-protease-family protein with tandem protease and protease-like domains. Its first domain retains the annotated histidine-aspartate-serine catalytic triad, supporting proteolytic potential; substrate specificity and physiological substrates remain unresolved. It is distinct from the clip-domain protease Snake.

Exact input: [A0A0B4KFF2](https://www.uniprot.org/uniprotkb/A0A0B4KFF2/entry), 474 residues. The accession was fetched explicitly with the gene-directory alias; no canonical-sequence substitution is made.

Raw emitted predictions: [CG43742-predictions-source.json](CG43742-predictions-source.json). Source features: [CG43742-uniprot.txt](CG43742-uniprot.txt), with an exact extraction in [CG43742-sequence-evidence.json](CG43742-sequence-evidence.json).

## Sequence and domain evidence

These are sequence/domain observations or explicitly named feature predictions, not measurements of biological function. ARBA assertions and ProtNLM-derived UniProt names are not counted as validation.

```text
DR   InterPro; IPR009003; Peptidase_S1_PA.
DR   InterPro; IPR001314; Peptidase_S1A.
DR   InterPro; IPR051487; Ser/Thr_Proteases_Immune/Dev.
DR   InterPro; IPR001254; Trypsin_dom.
DR   InterPro; IPR018114; TRYPSIN_HIS.
FT   SIGNAL          1..20
FT                   /evidence="ECO:0000256|SAM:SignalP"
FT   DOMAIN          35..258
FT                   /note="Peptidase S1"
FT                   /evidence="ECO:0000259|PROSITE:PS50240"
FT   DOMAIN          282..472
FT                   /note="Peptidase S1"
FT                   /evidence="ECO:0000259|PROSITE:PS50240"
FT   ACT_SITE        73
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        121
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
FT   ACT_SITE        207
FT                   /note="Charge relay system"
FT                   /evidence="ECO:0000256|PROSITE-ProRule:PRU00274"
```

At the annotated catalytic positions, direct indexing of the exact sequence gives: H73, D121, S207. These positions come from PROSITE features, not a new alignment; no substrate preference or assay result is inferred.

## ProtNLM claims

The snapshot emits names and location/keyword statements, with no GO or EC prediction for this target. Each actual statement is assessed below; no GO term has been substituted for it. Categories follow the function-prediction rubric, with nonspecific “uncharacterized” names marked UNC because they contain no testable function. CNN records an independently supported existing annotation; it does not assert a particular training-set composition.

| Kind | Verbatim emitted statement | Assessment | Evidence and limitation |
|---|---|---|---|
| Name | Serine protease snake | PLI | The emitted Snake name identifies the wrong characterized paralog. Reviewed snk/P05049 is a 435-residue clip-domain protease; CG43742/SP251 is a 474-residue tandem protease/protease-like-domain protein explicitly classified in PMID:30367934. Shared serine-protease activity does not establish Snake identity or its embryonic Toll-cascade role. |
| Location | Secreted (SL-0243) | CNN | A SignalP signal peptide at residues 1-20 and soluble extracellular protease architecture support secretion, consistent with the curated extracellular IBA. This does not establish a particular immune or developmental cascade. |

## Literature evidence

- [PMID:30367934](https://pubmed.ncbi.nlm.nih.gov/30367934/): “SP49, SP77, SP222, SP248, and SP251 contain a PD and a PLD;”
- [PMID:30367934](https://pubmed.ncbi.nlm.nih.gov/30367934/): “The SP-related sequences in each species were divided into SPs or SPHs based on the presence or absence of the His-Asp-Ser catalytic triad”

## Annotation decisions

- GO:0003674 molecular_function (ND): **MODIFY**. The exact sequence retains the annotated H73 D121 S207 triad in the N-terminal protease domain. PMID:30367934 classifies SP251 as a tandem PD/PLD protein; this supports generic catalytic potential without specifying a substrate.
- GO:0004252 serine-type endopeptidase activity (IEA): **ACCEPT**. The retained annotated H73 D121 S207 triad and intact S1 domain support broad serine proteolysis. The C-terminal protease-like domain does not imply that both domains are catalytic.
- GO:0004252 serine-type endopeptidase activity (ISM): **ACCEPT**. PMID:30367934 explicitly places SP251 among proteins with a protease domain and a protease-like domain. This is comparative sequence evidence rather than a substrate assay; the exact source sequence retains the first-domain triad.
- GO:0005575 cellular_component (ND): **MODIFY**. The N-terminal SignalP feature at residues 1-20 supports entry into the secretory pathway and the mature protein lacks a retained transmembrane segment; extracellular localization is consistent with the IBA.
- GO:0005576 extracellular region (IBA): **ACCEPT**. The signal peptide and soluble tandem protease-domain architecture support the existing curated IBA extracellular annotation.
- GO:0006508 proteolysis (IEA): **ACCEPT**. The first S1 domain retains the annotated H-D-S triad and the second is protease-like. Broad proteolysis is supported without specifying cleavage targets or a developmental cascade.
- GO:0008150 biological_process (ND): **MODIFY**. The intact first-domain catalytic triad supports generic proteolysis; physiological substrate and context remain unresolved.
- GO:0008233 peptidase activity (IEA): **MODIFY**. The S1 catalytic architecture supports the existing serine-type endopeptidase term.
- GO:0016787 hydrolase activity (IEA): **MODIFY**. The first S1 domain and retained catalytic triad support the specific peptidase class rather than a generic hydrolase label.
- GO:0045087 innate immune response (IBA): **KEEP_AS_NON_CORE**. PAINT places the innate-immune assertion at PTN000667087, the same Ecdysozoa-level ancestor that supports the extracellular-region IBA; its immune-process seeds are Dipteran proteases. The exact target is SP251 rather than Snake, so no embryonic Toll-cascade or Snake substrate is inferred; the broad inherited immune-process term is retained as non-core.
- GO:0051604 protein maturation (IEA): **UNDECIDED**. The source sequence supports serine protease potential but no physiological maturation substrate or activation cascade is established for CG43742.

## Research assessment

The Falcon report calls the target a CLIP-subfamily protease without resolving the exact architecture. The target has two S1-domain hits and is explicitly SP251 in PMID:30367934, which lists a protease domain plus a protease-like domain. Reviewed snk/P05049 instead contains a CLIP domain and one S1 domain. This independently verified architecture distinction refutes the specific Snake name; it does not refute broad serine-protease potential.

Provider output: [CG43742-deep-research-falcon.md](CG43742-deep-research-falcon.md). Primary papers and source records, rather than provider verdicts, support the assessment.

The annotation and prediction assessments are complete. UNC/UNDECIDED record delimited scientific or evidence uncertainty. Empty core-function lists indicate that no sufficiently resolved molecular activity can be asserted, rather than an unfinished review.

## 2026-09-28 IBA re-review

Fetched and inspected `interpro/panther/PTHR24256/PTHR24256-paint.tsv`. Both CG43742 IBA rows trace to Ecdysozoa-level `PANTHER:PTN000667087`: extracellular region was placed at that node on 2026-05-29 and innate immune response was placed at the same node on 2025-12-20. The node-level extracellular inference agrees with the exact target signal peptide, and the Dipteran-seeded node-level innate-immune inference resolves the prior placeholder uncertainty about whether the GOA row came from a relevant ancestral assertion.

Exact searches for `CG43742`, `FBgn0263999`, `A0A0B4KFF2`, and Drosophila `SP251` did not identify a newer paper that directly characterizes this protein. PMID:30367934 remains the only direct full-text source naming SP251 in the SP/PD/PLD classification; more recent CLIP/S1A studies characterize other Drosophila proteases or aggregate hemolymph protease activity and should remain contextual.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: A0A0B4KFF2 is the only UniProt product of CG43742 (FBgn0263999, synonym SP251), 474 aa, sequence version 1, RefSeq NP_001261130.1. It is not a fragment, isoform or alternative gene model; it carries both S1 domains, the signal peptide and the complete domain-1 triad. No separate canonical entry exists.

Sequence (re-checked on the exact sequence, `CG43742-bioinformatics/subfamily_tree.py`, `RESULTS.md`): domain 1 (35-258) has H73 (TAAHC), D121 and S207 (DSGGP), so the triad is complete. Domain 2 (282-472) has neither a TAAHC-type His motif nor a GDSGG-type Ser motif; it is a protease-like domain (PLD). This matches PMID:30367934 [PMID:30367934 "SP49, SP77, SP222, SP248, and SP251 contain a PD and a PLD;"]. The UniProt CAUTION line about missing conserved residues refers to the second domain. There is no clip domain (the segment between the signal peptide and domain 1 is ~14 residues), so the UniProt ARBA "CLIP subfamily" similarity note and the Falcon report's "CLIP" framing are not supported.

Evolutionary placement: the PANTHER 19.0 fly HMM file puts A0A0B4KFF2 in PTHR24260:SF147 (EG:BACR7A4.3 PROTEIN-RELATED; 27 fly members, including snk/P05049 and CG10764/SP77/A1ZAT2). UniProt's DR PANTHER line and the GOA IBA rows use PTHR24256 and PAINT node PTN000667087, whose seeds all map to other PTHR24260 subfamilies (SF134-SF145). An NJ tree over a MAFFT alignment of SF147 plus psh/modSP/SPE outgroups puts CG43742 on a branch of long tandem-domain proteins (HDC06631, CG4827, CG10764, CG42694, CG30187); snk sits alone on a deep branch. Identities are only 30-40% to every member, so there is no one-to-one ortholog. The nearest experimentally studied relative is CG10764/SP77, also a PD+PLD protein, with only an RNAi phenotype (reduced wasp-egg encapsulation; PMID:33644706). That phenotype is not transferred.

Annotation changes from the previous review:
- GO:0051604 protein maturation (ARBA IEA): UNDECIDED -> MARK_AS_OVER_ANNOTATED. ARBA-only; no precursor substrate or cascade position is known, so it is an over-specific process claim.
- GO:0045087 innate immune response (IBA): kept KEEP_AS_NON_CORE; reason rewritten to record the SF147 vs PTHR24256 placement discrepancy and that no PAINT seed falls in SF147. The node judgment is not overturned because there is no target-specific loss evidence.
- GO:0004252 (IEA): ACCEPT kept; noted that the EC 3.4.21.1 chymotrypsin rule is not evidence for P1 specificity.
- All other rows unchanged in action (ND rows MODIFY to serine-type endopeptidase activity / extracellular region / proteolysis; peptidase and hydrolase activity MODIFY to GO:0004252; extracellular region IBA and proteolysis IEA ACCEPT); support now cites the exact-sequence triad check.
- Description rewritten without any prediction-specific commentary; core function narrowed to the domain-1 serine endopeptidase.
- Added PMID:33644706 (relative context, LOW relevance) and the bioinformatics RESULTS.md.

Literature: no publication directly studies CG43742/SP251 beyond the Cao and Jiang 2018 classification (consistent with the 2026-09-28 searches above). Modules: no module under modules/ includes CG43742 or PTHR24256.
