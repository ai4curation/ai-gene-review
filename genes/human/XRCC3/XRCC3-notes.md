# XRCC3 (human, O43542) curation notes

## Provenance / process

- 2026-10-06: New review triggered by PMID:42682019 (Dwivedi et al., Biochem Soc Trans 2026,
  "Distinct functions of mammalian RAD51 paralogs in genome maintenance"), reviewed together with
  targeted updates to the RAD51C and XRCC2 reviews.
- `just deep-research-falcon human XRCC3 --fallback perplexity-lite` failed (no provider available
  in this environment), so there is no `-deep-research-*.md` file. Research below is from the
  cached primary literature in `publications/`.

## Key findings (with provenance)

### Complexes
- CX3 = RAD51C-XRCC3, purified from human cells [PMID:11751635 "the other consists of RAD51C with XRCC3"].
- New assemblies (2026 cryo-EM, three independent groups):
  - X3CDX2 (XRCC3-RAD51C-RAD51D-XRCC2) caps the 5' end of RAD51 filaments
    [PMID:41196948 "the XRCC3 complex stably caps the 5' termini of RAD51 filaments to promote homologous pairing"];
    XRCC3 contacts RAD51 and XRCC2 forms the cap [PMID:41196948 "with XRCC3 directly interacting with RAD51, and XRCC2 forming the cap"].
  - BCDX2-CX3-RAD51 "loader" and DX2-CX3 "anchor" [PMID:41772053 "a dynamic BCDX2-CX3
    'loader' and a stable DX2-CX3 'anchor'"].
  - Autoinhibited RAD51-X3C octamer, remodeled by DX2 into RAD51-X3CDX2 [PMID:42020761].
- There is no GO cellular-component term for X3CDX2; only GO:0033065 (Rad51C-XRCC3 complex)
  and GO:0033063 (BCDX2) exist. Raised as a suggested question rather than a knowledge gap
  (ontology gap, not biology).

### Molecular activity
- XRCC3-containing complexes stimulate RAD51 strand exchange / D-loop formation:
  - [PMID:41196948 "The XRCC3 complex, and to a lesser extent the CX3 complex, stimulated RAD51-mediated strand invasion"]
  - [PMID:41772053 "When RPA was added before RAD51, BCDX2-CX3 and CX3 strongly stimulated D-loop formation"]
  - [PMID:42020761 "RAD51–X3C displayed significantly enhanced DNA strand exchange activity over RAD51 alone"]
  - XRCC3's own RAD51-contacting loop is required [PMID:42020761 "the RAD51-interaction-defective XRCC3 loopΔ/quad mutant failed to support synergistic ssDNA binding with RAD51 or the ability to overcome RPA-mediated inhibition of strand exchange"].
  - -> NEW contributes_to GO:0140619 DNA strand exchange activator activity. Comparator check:
    RAD51AP1 carries GO:0140619 (IDA) for the same kind of RAD51 stimulation; absence on XRCC3
    reflects the 2026 publication date.
- Holliday junction and fork junction binding by CX3 [PMID:20207730].

### HR
- CX3 acts downstream of RAD51 recruitment [PMID:23149936].
- Late-stage HR roles: altered gene-conversion tracts [PMID:12191483]; reduced HJ resolvase
  activity in mutant extracts [PMID:14716019]; XRCC3 with GEN1 at HJ resolution [PMID:23108668].
  The resolvase catalysis is GEN1's: crossover-junction endonuclease MF annotations to XRCC3 are
  marked over-annotated (consistent with RAD51C review).

### Replication stress
- XRCC3 at nascent DNA of stalled forks; RAD51C/XRCC3 ATP hydrolysis needed for restart; XRCC2
  dispensable for restart [PMID:26354865].
- XRCC3 S225 phosphorylation (ATR, in ATM pathway; requires RAD51C not XRCC2) needed for RAD51
  chromatin loading, HR, and collapsed (not stalled) fork recovery [PMID:23438602].
- Purified CX3: no fork reversal; modest fork protection vs BCDX2 [PMID:37843130].
- Trigger review: "only the CX3 complex participates in restarting stalled/collapsed replication
  forks" [PMID:42682019]. Note the review also says FBH1-remodeled forks are protected by DX2 and
  CX3 (its ref 97); the primary paper was not identified/cached, so not used.

### R-loops
- CX3 binds FANCM and recruits it to R-loops; independent of fork functions; XRCC3 S225A
  complements [PMID:41719405]. -> NEW GO:0062176 R-loop processing (non-core; single study).
  Comparator check: GO:0062176 in human is carried by non-catalytic recruiters/regulators
  (SIRT7, SRPK2, NFAT5) as well as nucleases (MRE11).
  QuickGO query (2026-10-10; goId=GO:0062176, goUsage=exact, taxonId=9606) returns 10 rows, all
  involved_in IDA assigned by UniProt: SIRT7 (Q9NRC8, PMID:28790157; deacetylase of the helicase
  DDX21), SRPK2 (P78362, PMID:28076779; kinase acting on the helicase DDX23), NFAT5 (O94916,
  PMID:34049076), MRE11/RAD50/NBN (PMID:31537797), PRIMPOL (PMID:30478192), DDX21 (PMID:28790157),
  DDX23 (PMID:28076779), RAD54L2 (PMID:39028815). So regulators that act on the resolving enzyme,
  not only the enzymes themselves, carry the term, which is the role CX3 plays for FANCM.

### Mitochondria
- XRCC3 in mitochondria [PMID:20413593]; RAD51C/XRCC3 in mitochondrial nucleoid, supports mtDNA
  synthesis and POLG retention [PMID:29158291]. -> NEW located_in GO:0042645 mitochondrial
  nucleoid. No process NEW proposed (mtDNA replication) - the evidence is necessity/support of
  POLG, and RAD51C review did not add one either.

### Telomeres
- XRCC3-dependent t-loop HR deletion [PMID:15507207], telomere trimming [PMID:21903669,
  PMID:27918544]. Kept as non-core.

### Mitotic phenotypes
- Centrosome / SAC phenotypes after XRCC3 loss [PMID:23108668] are attributed to unresolved DNA
  damage [PMID:11025669 "Our results show that unresolved DNA damage triggers this instability"];
  annotations to centrosome duplication / SAC regulation marked over-annotated (not removed, full
  text not available).

## Decisions summary
- 13 GO:0005515 protein binding IPIs -> REMOVE (uninformative; interactions captured by CX3 complex
  CC and the strand-exchange-activator MF).
- GO:0140664 ATP-dependent DNA damage sensor activity (InterPro2GO) -> MARK_AS_OVER_ANNOTATED, as for
  RAD51C and XRCC2.
- GO:0000730 DNA recombinase assembly considered for core function 1 but omitted: the trigger
  review notes X3CDX2 "is unable to stimulate RAD51 filament formation on RPA-coated ssDNA", while
  PMID:42020761 reports enhanced filament assembly; conflicting, so not asserted.

## 2026-10-10 revision (PR #4409 review)
- GO:0062176 comparator substantiated with the QuickGO query and evidence codes (above).
- Completed the truncated PMID:41196948 quote.
- GO:0000403 Y-form DNA binding considered and not added: the PMID:20207730 fork substrate has duplex
  arms, and the authors conclude ssDNA does not drive recognition, whereas GO:0000403 is defined by
  unpaired strands at one end.
