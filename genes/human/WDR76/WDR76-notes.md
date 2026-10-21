# WDR76 (human, Q9H967) review notes

## Provenance / process

- 2026-10-20: `just fetch-gene human WDR76` (13 GOA rows; one experimental paper, PMID:27248496).
- Deep research FAILED: `just deep-research-falcon human WDR76 --fallback perplexity-lite`
  - falcon: `Edison API request failed: Failed to authenticate` (403 on auth/login)
  - perplexity-lite fallback: `Perplexity API HTTP error: 401 ... insufficient_quota`
  - No deep-research file exists; review is built from literature fetched directly
    (PubMed search "WDR76" and "CMR1/YDL156W yeast"), cached with `just fetch-pmid`.
- ProtNLM2 output deliberately not consulted (campaign rule).

## Evolutionary frame

- UniProt: PANTHER PTHR14773 / PTHR14773:SF0 (only subfamily); "Belongs to the WD repeat
  DDB2/WDR76 family". InterPro IPR050853 (WD_repeat_DNA-damage-binding); 7 WD40 repeats in the
  C-terminal half (311-626), N-terminal disordered region (1-21, 95-159).
- The PAINT node PTN000381277 covers human WDR76, yeast CMR1 (SGD:S000002315) and Arabidopsis
  DRS1. Donors: human WDR76 (heterochromatin, nucleus) and yeast Cmr1 (DNA binding, nucleus,
  regulation of DNA damage checkpoint).
- Gallina et al. call WDR76 "the closest orthologue of Cmr1 in higher eukaryotes"
  [PMID:25817432 "WDR76 is the closest orthologue of Cmr1 in higher eukaryotes"].
- Notably PAINT did NOT propagate a ubiquitin-ligase adaptor activity or RAS degradation to the
  node; these are human/mouse-specific experimental findings and are not claimed for the family.

## Evidence established in human (or mouse) WDR76 itself

1. Nuclear localization, puncta co-localizing with HP1 homologs CBX1/CBX5 (heterochromatin),
   rapid recruitment to laser-microirradiation DNA damage stripes (HEK293, Halo-tag live
   imaging) [PMID:27248496 "We found that WDR76 was rapidly (within a second) and intensely
   recruited to sites of damage."]. Recruitment is PARP-inhibitor insensitive [PMID:27248496
   "Neither intensity nor kinetics of WDR76 recruitment to microirradiation regions was affected
   by PARP1 inhibitor KU-0058948 concentrations up to 100uM"]. No loss-of-function experiment in
   this paper; the IMP evidence codes on its GOA rows effectively describe imaging observations.
2. Interactions (AP-MS + co-IP): PARP1, XRCC5/XRCC6 (Ku), CBX1/3/5, SPIN1, HELLS, GAN, SIRT1,
   CCT chaperonin [PMID:27248496; PMID:31353912; PMID:25817432]. WDR76:SPIN1 subcomplex
   binds H3K4me3 nucleosomes via SPIN1 [PMID:39116123].
3. Relocalizes to nuclear foci on MMS/MG132; foci do not coincide with 53BP1 (DSB) foci
   [PMID:25817432 "Consistent with data from yeast, WDR76 did not co-localize with 53BP1 foci,
   excluding that WDR76 accumulates at the site of DSBs."]. Gallina et al. explicitly leave
   open whether WDR76 participates in the replication stress response.
4. CRL4 adaptor-like role in RAS degradation (Choi lab): WDR76 binds HRAS/KRAS/NRAS, forms a
   complex with CUL4A and RAS, and overexpression/knockdown in human cancer cell lines
   decreases/increases RAS protein but not mRNA; Wdr76-/- MEFs have elevated Ras
   [PMID:30655611; PMID:31362761; PMID:31873167]. Caveat: no in vitro reconstitution of the
   ubiquitination, and DDB1 binding is cited from earlier screens (Higa 2006, PMID:17041588,
   abstract-only in cache; UniProt SUBUNIT: interacts with CUL4A and/or CUL4B, ECO:0000269).
5. Opposing CRL4 role: WDR76 inhibits CRL4-DCAF8-mediated degradation of LSH/HELLS by
   competitive inhibition of complex assembly [PMID:33288900]. So WDR76 is not simply a
   universal substrate receptor; it interfaces with the CRL4 machinery in more than one way.
6. 5hmC reader: identified in a mouse ESC DNA-pulldown screen (Spruijt 2013, PMID:23434322;
   abstract-only, abstract does not name WDR76). UniProt FUNCTION is ECO:0000250 (by
   similarity). Not established for human.

## Evidence established in yeast Cmr1 (same node; transfer only via IBA)

- Purified recombinant Cmr1 binds DNA with preference for UV-damaged DNA [PMID:22367945].
- cmr1 deletion: defect in DNA-damage checkpoint adaptation, increased chromosome loss,
  INQ (intranuclear quality control) compartment marker [PMID:25817432].
- Recruited to transcribed coding regions [PMID:26848854]; histone associated [PMID:22199229].

## Decisions summary

- nucleus (IBA, IDA): ACCEPT.
- heterochromatin (IBA, IMP): KEEP_AS_NON_CORE (puncta co-localization only).
- site of DNA damage (IMP): ACCEPT (direct live-imaging observation; core distinguishing feature).
- DNA damage response (IMP): KEEP_AS_NON_CORE (recruitment = response; functional
  participation in human not shown).
- DNA binding (IBA): ACCEPT (yeast biochemistry, inherited at node; human not directly tested).
- regulation of DNA damage checkpoint (IBA): KEEP_AS_NON_CORE (yeast-only mechanistic
  evidence, inherited claim).
- protein binding x3 (CBX1/3/5): REMOVE per policy (interactions are real but uninformative).
- enzyme binding (PARP1, XRCC5): KEEP_AS_NON_CORE (validated co-IP, functional meaning unknown).
- NEW: ubiquitin-like ligase-substrate adaptor activity (GO:1990756) and proteasome-mediated
  ubiquitin-dependent protein catabolic process (GO:0043161), from the human cell-line RAS
  degradation data (PMID:30655611, PMID:31362761). Participation: as the substrate-recognition
  subunit, WDR76 performs the substrate-selection step of CRL4-mediated ubiquitination.
  Comparator check (QuickGO, 2026-10-20, with descendants): DCAF1/VPRBP (Q9Y4B6) carries
  GO:1990756 by IDA; DTL (Q9NZJ0), DCAF8 (Q8N7N5) and DDB2 (Q92466) do not. So the convention is
  mixed, not a systematic absence; the term is defined for exactly this role. Cul4-RING complex
  membership (GO:0080008) was NOT proposed: CUL4A co-IP only, DDB1 binding not shown in the
  cached full texts. These are human/mouse-specific findings and should NOT be transferred to
  DRS1 or Cmr1 (PAINT did not place them at the node).
