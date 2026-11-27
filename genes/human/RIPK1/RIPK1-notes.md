# RIPK1 (human, Q13546) — curation notes

**Provenance note:** Provider deep research for this gene failed (Falcon returned
HTTP 402 Payment Required; Perplexity is not configured). No
`RIPK1-deep-research-<provider>.md` file exists. This notes file is a manual
literature synthesis built from the UniProt record (`RIPK1-uniprot.txt`), the
cached publications in `publications/`, and cached Reactome entries, and it
replaces the provider deep research for this review.

## Identity and architecture

- Receptor-interacting serine/threonine-protein kinase 1; 671 aa.
- N-terminal protein kinase domain (17-289; active-site proton acceptor D138),
  intermediate domain carrying the RIP homotypic interaction motif (RHIM,
  531-547), C-terminal death domain (DD, 583-669) (UniProt features).
- Caspase-8 cleavage site D324 separates the kinase domain from the
  intermediate domain and DD [PMID:10521396 "The cleavage site was mapped to the aspartic acid at position 324 of RIP."].

## Molecular function

- **Ser/Thr protein kinase.** "RIP is a serine-threonine kinase that is
  recruited by TRADD to TNFR1 in a TNF-dependent process" [PMID:8612133].
  Crystal structures of the kinase domain with necrostatins: "Necrostatins, a
  series of small-molecule inhibitors, suppress necroptosis by specifically
  inhibiting RIP1 kinase activity" [PMID:23473668]. Autophosphorylation sites
  (S14/15, S20, S161, S166) are readouts of activation [PMID:30988283
  "autophosphorylation of RIPK1 on Ser166—used as a readout for RIPK1 kinase activation"].
- Known substrates are few: RIPK1 itself, RIPK3 (reciprocal phosphorylation
  within the necrosome) [PMID:19524513 "The phosphorylation of RIP1 and RIP3 stabilizes their association within the pronecrotic complex, activates the pronecrotic kinase activity"],
  and DAB2IP/AIP1 Ser-604 [PMID:17389591 "RIP1 (the Ser/Thr protein kinase receptor-interacting protein) associates with the GAP domain of AIP1 and mediates TNF-induced AIP1 phosphorylation at Ser-604"].
- **Scaffold/adaptor (kinase-independent).** In TNFR1 complex I RIPK1 is
  ubiquitinated (cIAP1/2, LUBAC) and recruits NEMO/IKK and TAB/TAK1, driving
  canonical NF-kB activation. "In contrast to its role in nuclear factor kappa B
  activation, RIP requires its own kinase activity for death signaling"
  [PMID:11101870]. "RIPK1 regulates cell death and inflammation through
  kinase-dependent and -independent mechanisms. As a scaffold, RIPK1 inhibits
  caspase-8-dependent apoptosis and RIPK3/MLKL-dependent necroptosis. As a
  kinase, RIPK1 paradoxically induces these cell death modalities."
  [PMID:30988283]. RIP interacts with IKKgamma via a region homologous to ABIN-2
  [PMID:14653779 "a portion of RIP, which is similar to this 50-residue domain of ABIN-2, is also essential for RIP interaction with IKKgamma"];
  p62/SQSTM1 links RIP to aPKC [PMID:10356400].
- **Death-domain interactions.** DD binds TRADD, FAS, TNFR1, FADD and CRADD
  [PMID:7538908; PMID:8612133; PMID:9044836 "a COOH-terminal DD that interacts with RIP"].
  DD-mediated homodimerization activates the kinase [PMID:29440439 "Our study demonstrates the role of RIPK1-DD in mediating RIPK1 dimerization and activation of its kinase activity during necroptosis and RIPK1-dependent apoptosis."].
- **RHIM amyloid.** RHIMs of RIP1 and RIP3 form hetero-amyloid fibrils required
  for necrosis [PMID:22817896 "the RIP homotypic interaction motifs (RHIMs) of RIP1 and RIP3 mediate the assembly of heterodimeric filamentous structures"].

## Complexes / locations

- Complex I (TNF-RSC), plasma-membrane-bound receptor complex
  [PMID:12887920 "The initial plasma membrane bound complex (complex I) consists of TNFR1, the adaptor TRADD, the kinase RIP1, and TRAF2 and rapidly signals activation of NF-kappa B."].
- Complex II / complex IIa (RIPK1-FADD-caspase-8) cytosolic
  [PMID:12887920; PMID:18485876; PMID:21525013].
- Ripoptosome: "RIP1 is the core component of the complex." [PMID:21737330].
- Necrosome (complex IIb: RIPK1-RIPK3-MLKL), with PGAM5 [PMID:22265414].
- Endosomal TNFR complexes (CARP-2 ubiquitinates RIP at endocytic vesicles)
  [PMID:18450452].
- Cytoplasm/cytosol (UniProt; Reactome).

## Biological processes

- **Canonical NF-kB activation downstream of TNFR1 (scaffold).**
  Overexpression induces NF-kB; DD alone is dominant negative [PMID:8612133].
  Cleavage by caspase-8 abolishes NF-kB activation [PMID:10521396 "We demonstrated that the cleavage of RIP resulted in the blockage of TNF-induced NF-kappaB activation."].
- **Pro-survival / anti-death (scaffold).** Inhibits caspase-8 apoptosis and
  RIPK3/MLKL necroptosis [PMID:30988283]; in vivo scaffold function inhibits
  necroptosis in keratinocytes [PMID:36380021 "these results identify RIPK1 scaffold function as an inhibitor of RIPK3–MLKL-dependent necroptosis in keratinocytes"].
  Caspase-8-resistant RIP protects against apoptosis in vitro [PMID:10521396].
- **Necroptosis (kinase-dependent).** RIP kinase required for Fas/TNF/TRAIL
  caspase-independent death [PMID:11101870]; RIPK3 recruited to RIPK1 to form
  necrosis-inducing complex [PMID:19524512]; RIPK3 phosphorylates MLKL
  [PMID:22265413]. Necrostatin-1 blocks TNF/Smac mimetic necroptosis in FADD- or
  caspase-8-deficient cells [PMID:22028622]. In TNF signaling, caspase-8
  inactivation "switches the TNF response to RIPK1 kinase activity-dependent
  necroptosis, which additionally requires recruitment of the kinase RIPK3 and
  of the potential pore-forming pseudo-kinase mixed lineage kinase domain-like
  protein (MLKL) to complex II, now called the ‘necrosome’" [PMID:36380021].
  RIPK1 is therefore an upstream activator; RIPK3 is the MLKL kinase.
- **RIPK1-dependent apoptosis (kinase-dependent).** Smac mimetic-induced
  caspase-8 activation requires RIPK1 [PMID:18485876]; TWEAK/autocrine TNF
  apoptosis [PMID:21525013]; IAP inhibitor + chemotherapy in ALL [PMID:22173242];
  DNA-damage autocrine TNF loop [PMID:21458669].
- **Inflammation.** Non-cleavable human RIPK1 D324V/H variants cause CRIA
  autoinflammatory disease with IL-6/TNF overproduction [PMID:31827280].
  Ser25 phosphorylation by IKKs restrains kinase-dependent death [PMID:30988283].
- Other: JNK/p38 activation via DAB2IP-ASK1 [PMID:17389591]; ROS
  [PMID:17979836 review]; ANT inhibition in necrosis [PMID:16507998].

## Curation issues identified

- GO:0004706 JUN kinase kinase kinase activity (IBA) and derived MAPK cascade:
  no evidence RIPK1 phosphorylates MAP2K4/MAP2K7.
- GO:0004722 protein serine/threonine phosphatase activity (IEA): RIPK1 is a
  kinase; phosphatase activity in the necrosome belongs to PGAM5
  [PMID:22265414]. Remove.
- GO:0070105 positive regulation of IL-6-mediated signaling: evidence
  [PMID:31827280] is for IL-6 production, not IL-6 receptor signaling ->
  GO:0032755.
- GO:1903800 positive regulation of miRNA processing [PMID:26020802]: paper shows
  NF-kB-dependent miRNA induction, not processing.
- GO:0097300 programmed necrotic cell death: GO comment says use when RIPK1/RIPK3
  involvement not shown; necroptotic process is the appropriate term.
- 72 protein binding rows: uninformative; specific functions captured elsewhere.

## Disease

- RIPK1 deficiency (biallelic LoF) causes immunodeficiency with
  early-onset IBD and arthritis; dominant non-cleavable variants cause CRIA
  [PMID:31827280]. RIPK1 kinase activity is implicated in neuroinflammation and
  neurodegeneration (not curated here in GO terms).
