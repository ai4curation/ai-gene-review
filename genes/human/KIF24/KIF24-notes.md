# KIF24 curation notes

## Deep research status
- `just deep-research-falcon human KIF24` was run (first with the unavailable perplexity-lite fallback, then `--timeout 2400`). See the end of this file for the outcome. The review was written from cached primary literature.

## Key findings (with provenance)
- Kinesin-13-like protein that binds CP110/CEP97 and localizes to mother centrioles [PMID:21620453 "Kif24 preferentially localizes to mother centrioles."]
- Loss causes CP110 loss from mother centrioles and aberrant ciliation in cycling cells [PMID:21620453 "We found that loss of Kif24 leads to the disappearance of CP110 from mother centrioles, specifically in cycling cells able to form cilia."]
- Binds and depolymerizes microtubules; remodels centriolar MTs specifically [PMID:21620453 "Kif24 is able to bind and depolymerize microtubules in vitro."]
- NEK2 phosphorylation stimulates KIF24 and prevents cilium outgrowth in proliferating cells [PMID:26290419 "We show that Kif24, a microtubule depolymerizing kinesin, is phosphorylated by Nek2, which stimulates its activity and prevents the outgrowth of cilia in proliferating cells, independent of Aurora A and HDAC6."]
- Intramolecular N/C-terminal interaction (autoinhibition) relieved by NEK2 [PMID:26290419 "Taken together with our observation that the amino- and carboxy-terminal regions of Kif24 can interact"]
- Recruits MPHOSPH9, which recruits CP110-CEP97 [PMID:30375385 "Here we show that M-Phase Phosphoprotein 9 (MPP9) is recruited by Kinesin Family Member 24 (KIF24) to the distal end of mother centriole where it forms a ring-like structure and recruits CP110-CEP97 by directly binding CEP97."]
- UniProt notes KIF24 does not disassemble fully formed axonemes; so I did not propose a NEW cilium disassembly annotation (raised as a question instead).

## Curation decisions (summary)
- Motor activity (IBA/IDA/IEA): ACCEPT with caveat (kinesin-13 depolymerase; GO lacks a depolymerase MF). Microtubule-based movement IEA: MARK_AS_OVER_ANNOTATED (not a translocating motor).
- Microtubule depolymerization, microtubule binding, centrosome/centriole, negative regulation of cilium assembly: ACCEPT.
- Cilium assembly IMP: MODIFY -> negative regulation of cilium assembly (direction of phenotype).
- Identical protein binding: MARK_AS_OVER_ANNOTATED (intramolecular fold-back, not homo-oligomer). Protein binding x10: REMOVE.

## HPA cilium atlas vs module role
- Module: stage 1 cap component, "MT-depolymerizing kinesin at mother centriole (ciliogenesis suppressor)"; the cap participant notes KIF24 contributes MT-depolymerizing activity and lists negative regulation of cilium assembly.
- HPA v25: no data ("not in HPA"); no HPA-sourced GOA rows. The HPA cilium atlas therefore provides no evidence for or against.
- Assessment: core_functions agree with the module (microtubule binding/depolymerization and negative regulation of cilium assembly at the mother centriole). Minor point: KIF24 is better described as the upstream recruiter of the cap (via MPHOSPH9) plus a depolymerase, rather than a structural "cap component" in the same sense as CP110/CEP97.

## Deep research outcome
- Falcon succeeded on retry (`--timeout 2400`): `KIF24-deep-research-falcon.md`. Consistent with the review. Two refinements taken on board: (1) the 2011 KIF24 motor fragment depolymerized microtubules similarly with ATP and AMP-PNP, so ATP-hydrolysis dependence is not demonstrated for KIF24 (the description and motor-activity review were worded accordingly); (2) biallelic KIF24 missense variants cause a skeletal ciliopathy/acromesomelic dysplasia (Reilly et al. 2022, JBMR, DOI 10.1002/jbmr.4639), with patient cells paradoxically showing fewer cilia and centriole amplification - noted in the description, not used for annotations. The deep research also supports NEK2-KIF24 mainly maintaining the disassembled state rather than disassembling full axonemes, consistent with not proposing a cilium disassembly annotation.
