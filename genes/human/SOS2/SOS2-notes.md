# SOS2 (human, UniProt Q07890) - curation notes

## Identity

- UniProt Q07890 (SOS2_HUMAN), 1332 aa, Son of sevenless homolog 2; paralog of SOS1
  [file:human/SOS2/SOS2-uniprot.txt].
- Domains: N-terminal histone fold, DH (198-388), PH (442-546), N-terminal Ras-GEF/REM (595-739),
  Ras-GEF/CDC25 (778-1017), C-terminal disordered proline-rich region (1142-1332)
  [file:human/SOS2/SOS2-uniprot.txt].
- PANTHER PTHR23113 (GUANINE NUCLEOTIDE EXCHANGE FACTOR), subfamily PTHR23113:SF150 (SON OF SEVENLESS
  HOMOLOG 2) [file:human/SOS2/SOS2-uniprot.txt]; PAINT node PTN000560991 carries GEF activity and Ras
  protein signal transduction (also used in modules/erk_cascade.yaml).
- No GO-CAM model in `gocams/index.tsv` contains Q07890.

## Molecular function

- Ras GEF [file:human/SOS2/SOS2-uniprot.txt "Acts as guanine nucleotide exchange factor (GEF) for RAS
  proteins."]; the CDC25-homology domain promotes GDP release from RAS
  [file:human/SOS2/SOS2-deep-research-falcon.md "The CDC25-homology domain destabilizes nucleotide
  coordination and promotes GDP dissociation."].
- Cellular evidence: SOS2 in a TPR1-Galpha16 complex enhances Ras activation [PMID:20639119 "Expression of
  SOS2 enhanced Galpha16QL-induced Ras activation and its subsequent signaling."].
- Rac/Rho GEF activity of SOS2 (via DH domain) is not established, unlike SOS1
  [file:human/SOS2/SOS2-deep-research-falcon.md "SOS1 is a demonstrated RAC-GEF, whereas SOS2 has supporting
  interaction and homology evidence but had not, as of the authoritative 2021 synthesis, been formally
  established as an equivalent RAC-GEF."]. The two Reactome cytosol rows come from Rho/Rac GEF events;
  the location is fine but the implied activity is provisional.

## Recruitment / binding

- GRB2 binds the SOS2 proline-rich C-terminus through its SH3 domains, with higher affinity than SOS1
  [PMID:7629138 "We show that hSos2 interacts with Grb2 via its proline-rich COOH-terminal domain and that
  this interaction is dependent on the SH3 domains of Grb2."; "the apparent binding affinity of hSos2 for
  Grb2 is significantly higher relative to that of hSos1 both in vitro and in vivo"].
- Other IPI partners are all SH3-domain proteins (NCK1, CRK, PLCG1, ABL1, PACSIN3, SNX9), identified in
  SH3/proline-peptide screens [PMID:17474147; PMID:14679214 "The proline-rich Sos peptide retrieved only
  SH3 domain containing proteins as specific binding partners."]. All GO:0005515 rows -> MODIFY to
  GO:0017124 SH3 domain binding.

## Localization

- Cytosolic at rest, acts at the plasma membrane on prenylated RAS after GRB2-mediated recruitment
  [file:human/SOS2/SOS2-deep-research-falcon.md "SOS2 is a soluble intracellular protein that is primarily
  cytosolic in unstimulated cells."].

## Processes

- Ras protein signal transduction (core), downstream of RTKs; contributes preferentially to PI3K-AKT output
  in some contexts; partially redundant with SOS1 (Sos2-null mice viable).
- Insulin receptor signalling (IEA from mouse ortholog): plausible, non-core.

## Disease

- Noonan syndrome 9 (heterozygous gain-of-function variants) [PMID:25795793 "We identified two novel genes,
  SOS2 and LZTR1, associated with Noonan syndrome"].

## Annotation decisions

- GEF activity (IBA, IEA) ACCEPT; GO:0005085 is the current term (Ras-specific GEF term GO:0005088 no longer
  resolves in the GO build).
- GO:0046982 protein heterodimerization activity (InterPro2GO from histone-fold IPR009072) -> REMOVE: the
  SOS histone fold is an intramolecular tandem histone-like domain within a single chain, not evidence of a
  heterodimerization activity with another protein.
- PMID:19593445 (known batch miscitation) is not present in the SOS2 GOA set.

## Earlier independent review on main (commit fda391d9a)

SOS2 was reviewed independently on main (commit fda391d9a) while this review was in progress. When PR #3381 was merged with main (2026-10-08), this review was kept as canonical because it is COMPLETE and re-types bare protein-binding rows to informative terms where the other review removed them; what the other review added that this one lacked was ported: the NEW EGFR signaling pathway row from PMID:30181243 and two open questions. Its notes are preserved below for provenance; its deep-research file is in git history at fda391d9a.

### SOS2 (human, Q07890) curation notes

#### 2026-09-30 initial review

Context: reviewed as the SOS2 paralog variant of the Ras GEF step in the FGFR signaling module
(`modules/fgfr_signaling.yaml`, not edited). SOS1 review (`genes/human/SOS1/`) used as comparator.

##### Molecular function: RAS GEF
- GEF activity is SOS2-specific, not only inferred from SOS1. A GEF-dead mutant fails to rescue:
  [PMID:30181243 "These data indicate that SOS2 GEF activity, but not allosteric feedback activation of SOS2 by oncogenic KRAS, is key to SOS2-dependent activation of wild-type HRAS downstream of RTKs."]
- Noonan syndrome DH-domain mutants raise RAS-GTP at near-endogenous expression:
  [PMID:26173643 "These findings are consistent with a direct GOF effect on the RAS-GEF activity of NS-associated SOS2 mutations."]
- GPCR input: [PMID:20639119 "Expression of SOS2 enhanced Galpha16QL-induced Ras activation and its subsequent signaling."]
- GO:0005088 (Ras GEF activity) no longer resolves in the current GO build (runoak returns None), so GO:0005085 is kept, as for SOS1.

##### GRB2 / SH3 coupling
- [PMID:7629138 "We show that hSos2 interacts with Grb2 via its proline-rich COOH-terminal domain and that this interaction is dependent on the SH3 domains of Grb2."]
- Higher GRB2 affinity than SOS1: [PMID:7629138 "the apparent binding affinity of hSos2 for Grb2 is significantly higher relative to that of hSos1 both in vitro and in vivo"]
- The protein binding IPI rows from domain-mapped studies (PMID:7629138, PMID:14679214 SOS proline-rich peptide pull-down, PMID:17474147 SH3 peptide array) -> MODIFY to GO:0017124 SH3 domain binding. The high-throughput AP-MS/Y2H rows -> REMOVE (uninformative), matching SOS1.

##### SOS2 vs SOS1 (redundancy)
- Sos2-null mice are normal: [PMID:10938118 "Our results show that unlike the case for sos1, sos2 gene function is dispensable for normal mouse development, growth, and fertility."]
- Short- vs long-term signaling (mouse cells): [PMID:10675333 "We conclude that Sos1 participates in both short- and long-term signaling, while Sos2-dependent signals are predominantly short-term."]
- Ancillary role: [PMID:34205562 "the defective phenotypes observed in SOS1/2-DKO samples are always much stronger than in single SOS1-KO cells, while undetectable in single SOS2-KO contexts, suggesting a specific, ancillary role of SOS2 that only becomes easily visible in the absence of SOS1"]
- PI3K-AKT bias: [PMID:34205562 "dominant contribution of SOS1 to the RAS–ERK axis and SOS2 to the RAS–PI3K/AKT axis"]
- Rac-GEF role unproven for SOS2: [PMID:34205562 "So far, only SOS1 has been formally demonstrated to act as a bona fide Rac-GEF [13,58], and the hypothetical function of SOS2 as an Rac-GEF awaits future, stronger experimental evidence."]
  Consequence: no Rac process term proposed for SOS2 (SOS1 has GO:0035022; SOS2 does not get it).

##### Decisions
- GEF (IBA, IEA), Ras protein signal transduction (IBA), small GTPase-mediated signal transduction (IEA), plasma membrane (IBA), cytosol (IEA, 2x Reactome TAS): ACCEPT. Reactome rows are RHO/RAC-activation reactions whose SOS2 involvement is weak, but the location is right.
- Insulin receptor signaling (IEA Ensembl Compara): KEEP_AS_NON_CORE (generic RTK-GRB2-SOS step; no SOS2-specific evidence).
- Protein heterodimerization activity (IEA, histone-fold InterPro2GO): REMOVE (domain mapping artifact; also removed for SOS1).
- NEW: GO:0007173 EGFR signaling pathway, IMP PMID:30181243. Participation: SOS2 performs the GEF step. Comparator: SOS1 carries the term.
- No FGFR-specific SOS2 evidence found; FGFR role is inferred from the shared GRB2 mechanism (raised as a question, not annotated).
