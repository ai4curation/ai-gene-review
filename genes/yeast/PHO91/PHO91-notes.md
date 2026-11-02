# PHO91 (YNR013C, P27514) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PHO91 is the closest experimentally characterised relative of NEUCR/NCU01540
(Q7RWZ3); both are in PANTHER subfamily PTHR10283:SF92 (LOW-AFFINITY PHOSPHATE TRANSPORTER
PHO91). Pho91 (SGD:S000005296) is an experimental seed of the PAINT nodes PTN007430421
(GO:0005315) and PTN000815044 (GO:0006817, GO:0006797), together with Pho87 (SGD:S000000633)
and Pho90 (SGD:S000003734). ProtNLM2 outputs were not opened or used.

Deep research: `just deep-research-falcon yeast PHO91 --fallback perplexity-lite` failed
(falcon "Failed to authenticate"; perplexity HTTP 401 insufficient_quota). Review is based on
the cached literature below, the UniProt record and the PANTHER/PAINT files.

### Architecture
- 894 aa; N-terminal SPX domain (1-256, PROSITE PS51382) and a C-terminal SLC13/DASS-like
  (CitMHS, PF03600; IPR004680) transporter domain with 13 predicted TM helices (UniProt).
- PANTHER PTHR10283:SF92; TCDB 2.A.47.2.2 (DASS family). Paralogs Pho87 and Pho90 sit in a
  separate subfamily (SF110 per campaign brief) and are plasma-membrane low-affinity Pi
  transporters.

### Experimental evidence (S. cerevisiae)
- Phosphate transporter, genetic: Wykoff & O'Shea identified PHO90 and PHO91 as phosphate
  transporters; quintuple transporter inactivation is synthetic lethal
  [PMID:11779791 "identifying two new phosphate transporters, PHO90 and PHO91"].
- Constitutive expression of Pho91 sustained high Pi transport in starved cells but no PKA
  signalling [PMID:12581367 "Pho90 and Pho91 sustained highest phosphate transport but did not sustain trehalase activation"].
- Vacuolar membrane localisation, and pho91 deletion raises polyP in pho85 background;
  hypothesis of vacuolar export [PMID:17804816 "the unexpected localization of Pho91 in the vacuolar membrane"].
- Electrophysiology: IP7-stimulated outward Na+/Pi currents in giant vacuoles depend on Pho91
  and its SPX domain [PMID:30315104 "TbPho91 and Pho91p are responsible for vacuolar Pi and Na+ efflux"].
- Bru et al. 2025 (full text): endogenous, untagged Pho91 co-enriches 39-fold with vacuolar
  markers in purified vacuoles; tagged versions mis-sort. Pho91 as sole transporter does
  NOT support growth (contradicting earlier sole-transporter claims). pho91Δ vacuoles
  accumulate Pi twice as fast in vitro; 5-InsP7 abolishes the difference; SPX K237A
  (InsPP-binding) mutant behaves as activated exporter [PMID:41324358].
- G3P transport: Gly3P "is transported by two other carriers, Git1 and Pho91, without
  triggering signaling" [PMID:20133652].
- Turnover: Rsp5-dependent ubiquitination and endocytic degradation [PMID:18165238]; implies
  some Pho91 transits the plasma membrane / endocytic route, but the major steady-state pool
  is vacuolar [PMID:41324358].
- Low-affinity transporter mutants derepress PHO genes, independent of internal Pi
  [PMID:12821119, PMID:15194704]; Bru 2025 reinterprets the pho91Δ effect as cytosolic Pi
  scarcity caused by retained vacuolar Pi.
- vCLAMP contact-site localisation from an overexpression-based screen [PMID:25026036].

### Coupling ion: unresolved
UniProt models H+ coupling (ECO:0000305 only); Potapenko 2018 reports Na+-dependent currents;
Bru 2025 cites pH-gradient dependence. Hence MF kept at GO:0005315 rather than a symporter term.

### Decisions summary
- Core: GO:0005315 phosphate transmembrane transporter activity; GO:0000329 fungal-type vacuole
  membrane; GO:0035435 phosphate ion transmembrane transport (vacuole -> cytosol export; GO has
  only the opposite-direction term GO:1905011, so no export-specific term is used).
- GO:0006817 / GO:0055085 rows -> MODIFY to GO:0035435. Membrane / vacuolar membrane IEA ->
  MODIFY to GO:0000329. ARBA transmembrane transporter activity -> MODIFY to GO:0005315.
- Plasma membrane IBA (PTN000031793, seeded by Pho87/Pho90 and animal SLC13s, not by Pho91):
  MARK_AS_OVER_ANNOTATED; Pho91 diverged to vacuolar localisation.
- polyphosphate metabolic process (IBA, IMP) and regulation of phosphate transmembrane
  transport (IGI): MARK_AS_OVER_ANNOTATED: these are downstream phenotypes of Pi
  redistribution; Pho91 neither synthesises/degrades polyP nor regulates another transporter.
- G3P transport (IMP/IGI): KEEP_AS_NON_CORE.
- vCLAMP: KEEP_AS_NON_CORE.

### Transfer guidance for SF92 orthologs (e.g. NCU01540)
Transferable with phylogenetic support (same subfamily, PAINT PTN007430421): phosphate
transmembrane transporter activity. Vacuolar localisation is experimentally established only
in S. cerevisiae (and for TbPho91 acidocalcisomes, a distant homolog); G3P transport and
polyP phenotypes are S. cerevisiae-specific observations and should not be transferred
without evidence.
