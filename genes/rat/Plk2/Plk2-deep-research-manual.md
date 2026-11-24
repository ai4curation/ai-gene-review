# Plk2 (rat, Q9R012) - manual literature synthesis

No deep-research provider was available for this session; this summary was assembled
manually from cached publications in `publications/` and the UniProt record.

## Identity

- Polo-like kinase 2 (SNK, serum-inducible kinase), 682 aa, Swiss-Prot Q9R012, RGD:620760, GeneID 83722.
- N-terminal Ser/Thr kinase domain (79-331) and two C-terminal polo-box domains (500-578, 598-682)
  (UniProt features). Lys108 (ATP binding) and Asp202 (proton acceptor) mutants are kinase-dead
  [UniProt MUTAGEN, PMID:20802490, PMID:18723513]. Thr236 phosphorylation enhances activity
  [UniProt PTM, PMID:20802490].
- Member of the CDC5/Polo subfamily (PANTHER PTHR24345:SF44, PLK2 subfamily).

## Neuronal activity-induced kinase

- Snk mRNA is induced by stimuli that produce synaptic plasticity, including LTP; protein is targeted to
  dendrites; the C-terminal region binds CIB1 [PMID:10523297 "Stimuli that produce synaptic plasticity,
  including those that evoke long-term potentiation (LTP), dramatically increase levels of both kinase
  mRNAs." ; "Induced Fnk and Snk proteins are targeted to the dendrites of activated neurons"].
- SNK is targeted to dendritic spines, binds and phosphorylates SPAR (Sipa1l1) causing its degradation,
  depletes PSD-95/Bassoon clusters and causes loss of mature spines [PMID:14576440 "SNK bound to and
  phosphorylated spine-associated Rap guanosine triphosphatase activating protein (SPAR), a postsynaptic
  actin regulatory protein, leading to degradation of SPAR."]. Abstract only.
- Plk2 is required for synaptic scaling during elevated activity; CDK5 primes SPAR for phospho-dependent
  Plk2 (polo-box) binding [PMID:18498738 "the activity-inducible protein kinase Polo-like kinase 2 (Plk2,
  also known as SNK) was required for synaptic scaling"]. Abstract only.
- SPAR degradation after Plk2 phosphorylation is mediated by SCF(beta-TRCP) via a DSGIDT phosphodegron;
  binding of beta-TRCP to SPAR needs active Plk2 (K108M and D201A mutants fail) [PMID:18723513 "SPAR
  degradation by SCF(beta-TRCP) depended on the activity-inducible protein kinase Polo-like kinase 2
  (Plk2)."]. The paper notes that direct Plk2 phosphorylation of S1305/T1309 was not demonstrated, and
  that blocking beta-TRCP did not prevent Plk2-induced spine loss [PMID:18723513 "Although we have clearly
  established the Plk2-SCFβ-TRCP-SPAR degradative pathway, its function in neurons remains to be resolved."].
- Kinase-independent: the Plk2 C-terminus binds NSF directly, ATP-dependently, dislodging GluA2 and causing
  loss of surface GluA2 and decreased AMPAR currents [PMID:20802490 "Plk2 engagement of NSF, but not Plk2
  kinase activity, was required for this mechanism"]. Adaptins were recovered in GST-Plk2c pulldowns but
  lost under stringent conditions; dynamin bound GST and GST-Plk2c equally [PMID:20802490 "Dynamin,
  however, bound equally well to GST and to GST-Plk2c and was not examined further."].
- Plk2 phosphorylates RasGRF1, SPAR (degraded), SynGAP and PDZGEF1 (activated) in vitro; net effect
  suppresses Ras and stimulates Rap; required for homeostatic spine shrinkage; DN-Plk2 mice show memory
  retention defects [PMID:21382555 "CA Plk2, but not KD Plk2, robustly phosphorylated each of these
  Ras/Rap regulators in this defined system"; "their collective regulation by Plk2 profoundly stimulates
  Rap and suppresses Ras"]. This paper does not record LTP or LTD.

## Cell-cycle/centriole function (human and mouse evidence)

- Human PLK2 localizes to centrosomes/centrioles and its kinase activity is required for centriole
  duplication near G1/S [PMID:15242618 "the kinase activity of Plk2 is required for centriole
  duplication"; PMID:19001868 "Plk2 is localized to centrosomes during early G(1) phase where it only
  associates to the mother centriole"]. Abstract only.
- Plk2-/- mouse fibroblasts show delayed S-phase entry [PMID:12972611 "Cultured Plk2(-/-) embryonic
  fibroblasts grow more slowly than normal cells and show delayed entry into S phase."].
- Snk/Plk2 is a p53 target; its silencing increases apoptosis in taxol-treated cells [PMID:12897130].

## Other

- Human PLK2 binds (ATP-dependently) and phosphorylates alpha-synuclein S129, enhancing its autophagic
  degradation; a rat PD model was used [PMID:23983262].
- miRNA studies (miR-126-3p, miR-146a) list Plk2 as a target with downstream effects on vascular cells
  and bone marrow cell senescence/apoptosis [PMID:26934179, PMID:27908889]; these are indirect.
- PLK1, not PLK2, localizes to the synaptonemal complex in spermatocytes [PMID:22854038].

## With/From identifiers resolved (RGD REST API, 2026-10-28)

RGD:2064 is Ap1b1 (adaptor related protein complex 1 subunit beta 1); RGD:71015 is Ap2a2 (adaptor related protein complex 2 subunit alpha 2); RGD:2364 is Cltc (clathrin heavy chain); RGD:2513 is Dnm2, RGD:620416 is Dnm1l and RGD:727949 is Dnm3 (dynamins); RGD:621594 is Nsf; RGD:708497 is Sipa1l1 (SPAR).
