# ERF094 / ORA59 (At1g06160, Q9LND1) notes

## Identity
- UniProt Q9LND1, ERF094, synonym ORA59 (OCTADECANOID-RESPONSIVE ARABIDOPSIS AP2/ERF 59), At1g06160. Group IX ERF, single AP2/ERF domain (PF00847); PANTHER PTHR31190:SF314.
- Closest relatives: ERF1 (At3g23240) and AtERF15 (At2g31230) [PMID:18467450 "ERF1 and ORA59 form a small subgroup within group IX of the ERF family, which includes a third protein, AtERF15"].

## Molecular function: GCC-box (and ERE) binding transcriptional activator
- Direct binding and in vivo occupancy of the PDF1.2 promoter [PMID:21246258 "ORA59 bound in vitro to these GCC boxes and trans-activated the PDF1.2 promoter in transient assays via these two boxes"; "Using the chromatin immunoprecipitation technique we were able to show that ORA59 bound the PDF1.2 promoter in vivo"].
- Activates PDF1.2 promoter in protoplasts, unlike AtERF1/AtERF2 [PMID:18467450 "only ORA59 and ERF1 were able to activate PDF1.2 gene expression, in contrast to the related proteins AtERF1 and AtERF2"].
- Second target class: AtACT (agmatine coumaroyltransferase, HCAA biosynthesis); two GCC boxes, EDLL Leu228, MED25 and homodimer required [PMID:29752755 "MEDIATOR25 (MED25) and ORA59 homodimer are also required for ORA59-dependent activation of the AtACT gene"]. Abstract only.
- Dual DNA specificity: GCC box (JA-favoured) and ERELEE4 (ET-favoured), phosphorylation-dependent [PMID:34890461 "ORA59 exhibited a differential preference for GCC box and ERELEE4, depending on whether ORA59 activation is achieved by JA and ET, respectively"]. Abstract only.

## Location
- Nucleus; ethylene promotes nuclear accumulation [PMID:30510560 "ORA59 and RAP2.3 interacted in the nucleus and showed ethylene-dependent nuclear localization"]. Nuclear co-localization with EIN3 [PMID:28168848 "Co-infiltration assays revealed nuclear co-localization of ORA59 and EIN3"].

## Pathway role
- Terminal integrator of JA and ET signalling for a subset (~5-10%) of JA/ET genes (PDF1.2, HEL, ChiB); acts downstream of COI1 [PMID:18467450 "ORA59 is the terminal integrator of the JA and ethylene signal inputs for a subset of JA- and ethylene-responsive genes, including PDF1.2 and HEL"].
- ORA59 expression induced by JA and ethephon, requires COI1 and EIN2 [PMID:18467450 "the induction of ORA59 gene expression by JA, ethylene, or a combination of both requires intact JA as well as ethylene signaling pathways for full responsiveness"].
- Defense against Botrytis: OE resistant, RNAi susceptible [PMID:18467450 "overexpression of ORA59 caused increased resistance against the fungus Botrytis cinerea, whereas ORA59-silenced plants were more susceptible"]. Not required for basal resistance to Alternaria brassicicola [PMID:18467450 "the level of basal resistance against A. brassicicola in ORA59 -silenced plants did not differ from that of wild-type plants"].
- Local (inoculated-leaf) resistance assays only; ORA59 induced systemically by Botrytis, but no systemic resistance assay was done. GO:0009861 (JA/ET-dependent systemic resistance, i.e. ISR) thus over-reaches the IMP; better captured by defense response to fungus (GO:0050832).
- Positive role in ethylene responses (triple response; Pectobacterium resistance), RAP2.3-dependent [PMID:30510560].
- SA antagonism acts via ORA59 protein depletion [PMID:23435661 "SA strongly reduces the accumulation of ORA59 but not that of ERF1"]; EIN3-dependent 26S proteasome degradation [PMID:28168848 "The functional ramification of the physical interaction is EIN3-dependent degradation of ORA59 by the 26S proteasome"].

## Curation decisions summary
- MF: GO:0003700 accepted; generic DNA binding -> GO:0000976; NEW GO:0001216 DNA-binding transcription activator activity (IDA, PMID:21246258).
- BP: ethylene-activated signaling accepted; NEW jasmonic acid mediated signaling pathway (GO:0009867) because ORA59 is the transcriptional effector acting downstream of COI1 (participates as terminal TF, analogous to its existing ethylene-signalling term). GO:0009861 -> MODIFY to GO:0050832 defense response to fungus. TAS regulation of transcription row -> GO:0045893.
- IEP response to JA/ethylene: keep as non-core (expression-level response).
- Project question 3 (necessity vs participation): the defense-response-to-fungus term is defensible here because ORA59 directly transcribes antimicrobial effector genes (PDF1.2, AtACT->HCAAs); the mechanistic core is the activator MF.

## Sources
- Deep research: ERF094-deep-research-falcon.md (consistent with primary literature above).
- Abstract only: PMID:29752755, PMID:34890461, PMID:23435661, PMID:10715325, PMID:11118137, PMID:9687012.
