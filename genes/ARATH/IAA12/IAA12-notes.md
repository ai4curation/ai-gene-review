# IAA12 / BODENLOS (At1g04550; Q38830) curation notes

## 2026-10 review (auxin_nuclear_signaling module)

- Deep research (falcon) failed (HTTP 402); review based on cached literature.
- Identity: UniProt Q38830 IAA12_ARATH, synonym BDL. Correct.

### Function
- bdl is a domain II (degron) gain-of-function: "the bodenlos phenotype results from an amino-acid exchange in the conserved degradation domain of IAA12"; "BODENLOS and MONOPTEROS interact in the yeast two-hybrid assay" [PMID:12101120].
- Embryo phenotype: "BDL is involved in auxin-mediated processes of apical-basal patterning in the Arabidopsis embryo" [PMID:10068632].
- TPL co-repressor: "TOPLESS (TPL) can physically interact with IAA12/BODENLOS (IAA12/BDL)" and TPL "is required for IAA12/BDL repressive activity"; "tpl-1 can suppress the patterning defects of the bdl-1 mutant" [PMID:18258861].
- Aux/IAA domain I = active, transferable repression domain with LxLxL motif [PMID:14742873].
- Receptors: "all TIR1/AFB proteins interact with BDL, and BDL is stabilized in triple mutant plants" [PMID:15992545]; IAA12 needs high auxin to bind TIR1/AFB2 in yeast [PMID:22466420].
- Specificity: "stabilization of BDL/IAA12 or its sister protein IAA13 prevents MP/ARF5-dependent embryonic root formation" [PMID:15889151]; MP and BDL act in the proembryo to specify the hypophysis [PMID:16459305].

### Decisions
- GO:0003700 (ISS, TF catalogue) -> MODIFY to GO:0003714 transcription corepressor activity (no DNA-binding domain).
- GO:0000976 IBA and Y1H IPI -> MARK_AS_OVER_ANNOTATED (indirect promoter association via ARFs).
- Protein binding: ARF partners -> GO:0140297; Aux/IAA partners -> GO:0046982; unrelated HT partners -> REMOVE.
- NEW: GO:0009734 auxin-activated signaling pathway (IAA12 is the co-receptor/substrate that does the signalling step).
