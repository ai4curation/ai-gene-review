# slc15a2 review notes

- Curated in DANRE batch 04. Slc15a2 is a PEPT2 peptide:proton symporter. The response-to-yeast/NLR signaling annotations come from a host-pathogen network study, not direct transporter mechanism, so I marked them as non-core or over-annotated rather than central function.
- Follow-up: changed broad BP/CC peptide transport terms from cross-aspect MODIFY to REMOVE; specific PEPT2 terms remain accepted.

## Re-review 2026-09-29

Re-reviewed all 23 GOA rows against UniProt B0S6T2 and the two cached papers; replaced the
repeated "is supported for Slc15a2/PEPT2" boilerplate with evidence-specific blocks and resolved
the five MARK_AS_OVER_ANNOTATED rows explicitly.

- Core activity/process from the zebrafish oocyte IDA [PMID:16317081 "Electrophysiological analysis
  after cRNA injection in Xenopus laevis oocytes suggested that zebrafish PEPT2 is a
  high-affinity/low-capacity transporter (K(0.5) for glycyl-L-glutamine approximately 18 microM..."]:
  GO:0071916 (IDA, IBA), GO:0015333 (ISS), GO:0042937 (ISS), GO:0140206 (IBA, ISS [was PENDING]),
  GO:0140207 (ISS) all ACCEPT.
- Re-adjudicated the five MARK_AS_OVER_ANNOTATED rows: GO:0006857 oligopeptide transport (IEA),
  GO:0016020 membrane (IEA) and GO:0055085 transmembrane transport (IEA) changed to MODIFY to the
  specific child terms already carried (GO:0140206/GO:0140207; GO:0005886). GO:1902600 proton
  transmembrane transport (IEA, GO_REF:0000108) changed to KEEP_AS_NON_CORE because proton
  co-transport is a genuine, mechanistically inseparable part of symport (UniProt 2:1/3:1
  stoichiometry), just not a standalone role. GO:0001878 response to yeast (IDA, PMID:23947337)
  kept MARK_AS_OVER_ANNOTATED with a proper argument: the "IDA" is membership in a computational
  Candida-zebrafish PPI network [PMID:23947337 "Protein-protein interaction (PPI) data from the
  BioGRID database, ortholog information from CGD, ZFIN, InParanoid, and simultaneous time-course
  microarray data"], not a demonstration of participation; also flagged the reference MISCITED.
- GO:0022857 transmembrane transporter activity (IEA) kept MODIFY (to GO:0015333/GO:0071916) with
  a rewritten reason.
- Immune ISS rows (mouse donor Q9ES07): GO:0015835 peptidoglycan transport KEEP_AS_NON_CORE, now
  anchored to the UniProt MDP:3 H+ catalytic reaction; GO:0070424 NLR-signaling regulation
  KEEP_AS_NON_CORE as a downstream consequence (PEPT2 delivers the MDP agonist, the NLRs signal).
- Localization: plasma membrane and apical plasma membrane rows ACCEPT (apical is ortholog-inferred;
  the deep-research file explicitly notes zebrafish polarity is unresolved); phagocytic vesicle
  membrane IEA KEEP_AS_NON_CORE (mouse macrophage behaviour).
- Description rewritten; core_functions and suggested questions/experiments updated.
- Validation: zero errors, zero warnings.
