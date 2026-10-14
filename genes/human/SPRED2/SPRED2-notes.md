# SPRED2 (human, Q7Z698) curation notes

## 2026-10-01 initial review

### Identity and domains
- 418 aa; N-terminal EVH1/WH1, central c-Kit-binding domain (KBD), C-terminal cysteine-rich Sprouty-related (SPR) domain (UniProt; InterPro IPR000697, IPR023337, IPR007875).
- Non-catalytic; UniProt FUNCTION: "Recruits and translocates NF1 to the cell membrane, thereby enabling NF1-dependent hydrolysis of active GTP-bound Ras to inactive GDP-bound Ras" (PMID:34626534).

### Mechanism of Ras-ERK inhibition (key for modules/erk_cascade.yaml)
- NF1 recruitment (best supported):
  - [PMID:22751498 "We also found that the two other Spred1 family members, Spred2 and Spred3, could associate with neurofibromin"]
  - [PMID:22751498 "The ectopic expression of Spred2 also led to a significant redistribution of neurofibromin from the cytoplasm to the membrane fraction"]
  - [PMID:22751498 "the siRNA knockdown of both Spred1 and Spred2 in PC3 cells led to a significant reduction of endogenous neurofibromin in the membrane fraction"]
  - [PMID:34626534 "pathogenic SPRED2 variants can affect protein stability, causing accelerated degradation, but can also affect proper targeting of SPRED2 to the plasma membrane or impair its binding to neurofibromin"]
  - Contrast with Sprouty: [PMID:22751498 "However, Sprouty proteins, which lack the N-terminal EVH1 domain, did not coprecipitate neurofibromin."]
- Acts at/upstream of Ras-GTP (consistent with GAP recruitment):
  - [PMID:15683364 "induction of either Spred-1 or Spred-2 decreased the proportion of both Ras and Rap1 that was in its GTP-bound form following EGF stimulation"]
  - [PMID:15683364 "neither Spred-1 nor Spred-2 was able to interfere with the strong ERK activation induced by RasV12, suggesting their mode of action was upstream of Ras"]
  - SPRED2 (unlike SPRED1) needs its Sprouty domain: [PMID:15683364 "the Sprouty domain of Spred-1 is not required to block MAPK (mitogen-activated protein kinase) activation, while that of Spred-2 is required"]
- Older Ras-Raf model (Wakioka, mouse, abstract only): [PMID:11493923 "Spred constitutively associated with Ras but did not prevent activation of Ras or membrane translocation of Raf"]; [PMID:11493923 "Spred inhibited the activation of MAP kinase by suppressing phosphorylation and activation of Raf"]. Conflicts with the later Ras-GTP data; treated as historical.
- NBR1 arm: [PMID:19822672 "Attenuation of FGF signaling by Spred2 is dependent on the interaction with NBR1 and is achieved by redirecting the trafficking of activated receptors to the lysosomal degradation pathway"]
- Human genetics: [PMID:34626534 "When overexpressed in cells, all variants were unable to negatively modulate EGF-promoted RAF1, MEK, and ERK phosphorylation"]; patient fibroblasts [PMID:34626534 "documented an increased and prolonged activation of the MAPK cascade in response to EGF stimulation"].

### Secondary activities
- DYRK1A: [PMID:20736167 "Both SPRED1 and SPRED2 inhibit the ability of DYRK1A to phosphorylate its substrates, Tau and STAT3"] via substrate competition [PMID:20736167 "SPRED proteins compete for the same binding site to modify this process"]. Abstract-only.
- Localization: vesicles [PMID:15580519 "we found Spred-2 to be strongly colocalized with Rab11 and, to a lesser extent, with Rab5a GTPase"].

### Decisions
- MF for module: molecular adaptor activity (GO:0060090), NEW; the NF1 IPI protein-binding row MODIFIED to GTPase activating protein binding (GO:0032794). Considered protein-macromolecule adaptor activity (GO:0030674) but SPRED2-specific evidence only shows NF1-to-membrane bridging, not a second macromolecule partner (the SPRED1-NF1-KRAS structure is SPRED1); left as a suggested question.
- Rejected kinase inhibitor MF as core for Ras-ERK: unlike SPRY4 (RAF1 binding via CRD), SPRED2's Ras-ERK effect is upstream of Ras via the GAP.
- NEW BP: GO:0046580 (comparator: SPRY2 IBA, SPRY4 core) and GO:0040037 (NBR1/FGF).
- UNDECIDED: GO:0043517 (p53 DNA damage response) ISS/IEA - cited abstract (PMID:20736167) has no p53 content; cannot see full text.
- High-throughput 'protein binding' rows REMOVE per repo policy (removal does not mean interaction false). NBR1 IPI also REMOVE as bare protein binding; biology captured by NEW GO:0040037.
- No NOT (negated) annotations exist for SPRED2.
