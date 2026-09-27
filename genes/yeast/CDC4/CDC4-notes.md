# CDC4 (YFL009W, UniProt P07834) - curation notes

Working notes for the GO annotation review of *Saccharomyces cerevisiae* Cdc4, the
WD40 F-box substrate receptor of SCF(Cdc4). Inline citations quote the cached
publications in `publications/` or the deep-research file.

## Identity and architecture

- 779 aa; F-box domain (272-319) followed by eight WD40 repeats (380-698 region)
  per the UniProt feature table. PANTHER places it in PTHR19849 (family label
  "PHOSPHOLIPASE A-2-ACTIVATING PROTEIN", a WD40 family dominated by PLAA/Doa1)
  subfamily SF1 "F-BOX/WD REPEAT-CONTAINING PROTEIN 7", i.e. the FBXW7 branch.
- Function summary from UniProt: "Substrate recognition component of a SCF
  (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex ... Recognizes and
  binds to phosphorylated target proteins. Directs ubiquitination of the
  phosphorylated CDK inhibitor SIC1."
- Deep research framing: [file:yeast/CDC4/CDC4-deep-research-falcon.md "Cdc4 is
  best annotated as the **phosphorylation-dependent substrate receptor of the
  SCF^Cdc4 E3 ubiquitin-ligase complex**."] and "Thus, **Cdc4 selects substrates
  and orients them for ubiquitination; Cdc34 performs ubiquitin transfer**."

## Core mechanism (SCF(Cdc4) reconstitution)

- [PMID:9346239 "We show here that Cdc4p, Cdc53p, and Skp1p assemble into a
  ubiquitin ligase complex named SCFCdc4p."] and "When mixed together, SCFCdc4p
  subunits, E1 enzyme, the E2 enzyme Cdc34p, and ubiquitin are sufficient to
  reconstitute ubiquitination of Cdk-phosphorylated Sic1p." Substrate binding
  resides in the Cdc4/Skp1 subcomplex: "Phosphorylated Sic1p substrate is
  specifically targeted for ubiquitination by binding to a Cdc4p/Skp1p subcomplex."
- [PMID:9346238 "Skp1 functions as the receptor that selectively binds
  phosphorylated Sic1."] (Cdc4 assembled with Skp1).
- [PMID:8706131 "directly binds Skp2p, cyclin F, and Cdc4p through a" ... "novel
  structural motif called the F-box"] - the F-box/Skp1 link; SKP1 was isolated as
  a suppressor of cdc4.
- [PMID:9499404 "Cdc53 serves as a scaffold protein that links Skp1/F-box proteins
  and Cdc34"] and "Cdc4 is specific for degradation of Sic1".
- [PMID:14747994 "ubiquitination of Sic1 by the reconstituted SCF(Cdc4) complex was
  specifically" ... "catalyzed by two of the five E2 enzymes tested in vitro; Cdc34
  and Ubc4"].
- Phosphodegron reading: [PMID:19008353 "The disordered cyclin-dependent kinase
  (CDK) inhibitor Sic1 interacts with a single site on its receptor Cdc4 only upon
  phosphorylation of its multiple dispersed CDK sites."]; [PMID:23314252 "Cdc4
  displays a preference for diphosphorylated degrons, often grouped in clusters"
  and "Phosphorylation of Thr94 and Ser98 promotes Cdc4 binding"] on Eco1, where
  "phosphorylation sites are spaced correctly to bind Cdc4, resulting in strict"
  discrimination between Cdk1- and Cdc7-added phosphates.
- Ubiquitin binding by the propeller: [PMID:21070969 "by the F box protein Cdc4
  promotes its autoubiquitination and turnover"]; "mutations that diminished Ub
  binding extended the half-life of Cdc4"; the Ub site is separate from the degron
  pocket ("phosphodegron peptides that bind Fbw7 and Cdc4 did not diminish Ub
  binding by the" propeller). Graded non-core (regulates Cdc4's own turnover).
- Cdc4 is itself turned over via the proteasome adaptor Cic1: [PMID:11500370
  "proteins Cdc4 and Grr1, substrate recognition subunits of the SCF complex" are
  stabilised in cic1 mutants; Cic1 "interacts in vitro and in vivo with Cdc4"].

## Localisation

- [PMID:11080155 "whereas the F-box protein Cdc4 was exclusively nuclear"];
  "Cdc4 is exclusively localized to the cell nucleus"; a monopartite NLS in residues
  1-106; the NES-fused cytoplasmic form "Cdc4 was unable to complement the growth
  defect of cdc4-1 cells" but degrades cytoplasmic Far1. Basis of the nucleus and
  nuclear SCF complex IDA rows (both ACCEPT).
- [PMID:2244914 "the CDC4 gene product localizes in the nucleus by two different
  biochemical" preparations of nucleoskeletal proteins; "includes the CDC4 gene
  product as a component of the yeast nuclear skeleton"]. Nuclear-matrix IDA graded
  MARK_AS_OVER_ANNOTATED: the nucleus is right, the "matrix" claim is a 1990
  fractionation interpretation never substantiated later; deep research: "the most
  defensible modern annotation is **nuclear SCF substrate receptor**".

## Cell-cycle roles

- G1/S (core): [PMID:10409741 "Cdc4 is involved in the proteolysis of the Cdk
  inhibitor, Sic1, necessary for G(1)/S transition"]; the G1/S block of cdc4-12
  and cdc4-delta is "abolished by the deletion of the SIC1 gene". [PMID:7954792
  "Proteolysis of a cyclin-specific inhibitor of Cdc28 is therefore an essential
  aspect of the G1 to S phase transition."]
- G2/M (non-core): [PMID:10409741 "lacking the CDC4 gene are arrested both at
  G(1)/S and at G(2)/M"]; the preanaphase arrest of "cdc4-12 mutant is relieved by
  the deletion of PDS1", which "suggests that the Cdc4 function in G 2 /M may be
  linked to the degradation of Pds1". Substrate not identified; the IGI row with
  SIC1 (PMID:7954792) is abstract-only in the cache and was deferred to SGD.
- Meiosis (non-core): [PMID:328339 "thus suggesting that the function of cdc4 is
  required at several points in meiosis (at least at three different times)"].

## Substrates recorded in GOA rows (resolved from protein binding to GO:1990756)

- Sic1: PMID:15448699 (Hog1 stabilises Sic1 against Cdc4; abstract-only),
  PMID:18787112 ("Such phosphorylation enables Sic1-Cdc4 interaction required for
  ubiquitination of Sic1."), PMID:19008353 (NMR).
- Rcn1: [PMID:17954914 "phosphorylation of yeast RCN, Rcn1, triggers degradation
  through the SCF(Cdc4)"; "SCF(Cdc4)-dependent degradation required phosphorylation
  of Rcn1 by Mck1"]; also recovered in PMID:18787112 ("We identified Swi5, Rcn1,
  and Spo74 as substrates of the SCF Cdc4 complex.").
- Other substrates with rows: Ash1 [PMID:21098119 "ubiquitinated by SCF(Cdc4) in a
  phosphorylation-dependent manner in vitro"], Ste7 [PMID:23645675 "we demonstrate
  that SCF(Cdc4) ubiquitinates Ste7 directly"] (signalling output, not shown to be
  degradative), Far1 (PMID:11080155), Eco1 (PMID:23314252).
- Substrates in the literature but not in GOA rows (deep research): Cdc6, Gcn4,
  Tec1, Hst3, Ame1, Cse4 (with Met30). Not proposed as NEW annotations; raised as a
  GO-CAM has_input question instead.

## Protein-binding (GO:0005515) row policy applied

- MODIFY to GO:1990756 ubiquitin-like ligase-substrate adaptor activity: focused
  Skp1 papers (PMID:8706131, 9499404, 14747994) and phosphodegron substrates
  (Sic1: 15448699, 18787112, 19008353; Rcn1: 17954914, 18787112).
- MODIFY to GO:0097602 cullin family protein binding: Cdc53 in PMID:9499404 (same
  convention as the human SKP2-CUL1 rows).
- REMOVE as uninformative (interaction not disputed): high-throughput or
  methodological records (PMID:10688190, 11805837, 17960736, 18719252, 19882662 x3,
  23267104 x2, 37968396) and the Cic1 row (PMID:11500370), where Cdc4 is the
  proteasome substrate rather than the agent. PMID:23267104 concerns S. pneumoniae
  proteins and never mentions Cdc4 in the cached full text; PMID:11805837 is
  title-only in the cache.

## IBA rows from PANTHER:PTN000457905 (removed)

- Five IBAs (GO:0000472, GO:0000480, GO:0030686, GO:0034511, GO:0005730) descend
  from PTN000457905 in PTHR19849. `interpro/panther/PTHR19849/PTHR19849-paint.tsv`
  shows the four ribosome-biogenesis IBDs on this node were each seeded on
  2020-02-27 by a single gene, SGD:S000004212, which SGD resolves to UTP13
  (YLR222C), a U3 snoRNP/90S preribosome WD40 protein. The nucleolus IBD (updated
  2025-12-19) adds AT5G16750, CGD:CAL0000184822, PomBase:SPCC16A11.02,
  UniProtKB:Q12788 and UniProtKB:Q387K5.
- The argument is with node placement, not donor count: the node groups Cdc4 with
  beta-propeller proteins of unrelated function, while the F-box branch is curated
  separately (FBXW7 receives GO:1990756 and GO:0031146 at PTN008571532; Doa1/PLAA
  receives ubiquitin-reader terms at PTN000457424). Cdc4 has no reported
  association with the SSU processome or rRNA processing, its propeller binds
  phosphodegrons and ubiquitin, and it is nuclear with nucleoplasmic/chromatin
  substrates. All five graded REMOVE with `propagation_review` (PROPAGATION_BAD;
  WRONG_ORTHOLOG_OR_PARALOG plus FUNCTIONAL_DIVERGENCE or
  COMPARTMENT_OR_COMPLEX_MISMATCH).

## Decisions on the E3-activity rows

- GO:0004842 / GO:0061630 rows carry `contributes_to` as seeded and are ACCEPTed on
  that claim: E3 activity belongs to the assembled SCF(Cdc4), and Cdc4 supplies the
  substrate-recognition arm. The subunit's own MF is GO:1990756, proposed via the
  protein-binding MODIFY rows and used in `core_functions`.
- GO:0006511 (three IDA rows) MODIFY to GO:0031146: the biology is core, the term is
  the generic parent of the SCF-specific term already present from the same papers.

## Open items

- Substrate for the G2/M requirement (Pds1 link) remains unresolved.
- Whether D-domain dimerisation deserves representation as a separate activity.
