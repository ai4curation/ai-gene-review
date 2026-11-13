# galU (PA2023, Q9I291) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I291 --alias galU` (symbol fetch hit
UniProt rate limits). Accession Q9I291 matches the worklist (rank 322).
Reviewed Swiss-Prot entry GALU_PSEAE, 279 aa. No deep-research provider was
used; literature checked with the PubMed MCP (searches failed with API errors
on 2026-11-05, so only the PseudoCAP-cited paper was read, abstract only).

### Identity

- UTP--glucose-1-phosphate uridylyltransferase, EC 2.7.7.9; NCBIfam TIGR01099
  galU; Pfam PF00483 NTP_transferase; PANTHER PTHR43197:SF1. Belongs to the
  UDPGP type 2 family.
- Reaction: alpha-D-glucose 1-phosphate + UTP + H+ = UDP-alpha-D-glucose +
  diphosphate (UniProt catalytic activity, Rhea:19889).

### Literature

- Dean and Goldberg 2002 (PMID:12044687; abstract only):
  [PMID:12044687 "When the wild-type galU gene was introduced into strain PA103
  wbpM-C containing the cloned wbpM gene, both LPS defects were corrected."]
  [PMID:12044687 "Construction of galU mutants in P. aeruginosa serogroups O11,
  O5, O6 and O17 strains led to truncation of the LPS core, indicating the
  involvement of GalU in P. aeruginosa LPS core synthesis."]
- GalU supplies the UDP-glucose used by core glucosyltransferases; it makes the
  precursor rather than assembling the core. Kept as a non-core process.

### Clade checks (cached PAINT IBD/leaf GAF; QuickGO 2026-11-05)

- PTN000501197 (GO:0009244 LPS core region biosynthetic process): IBD seeds
  are Q9I291 (this gene, PseudoCAP IMP) and E. coli GalU P0AEP3 (EcoCyc IMP
  PMID:10398745, qualifier acts_upstream_of_or_within). 33 leaf IBAs. Leaves
  include B. subtilis GtaB (Q05852), YngB (O31822) and YtdA (P42407),
  S. aureus GtaB (Q2G1T6), Listeria lmo1078 (Q8Y840), Streptococcus Q8DN58,
  Clostridium GtaB (A5I6J3), Bacillus cereus BC_4918/BC_5275, Mycoplasma
  P47691, Streptomyces GtaB (Q9RKA6), M. tuberculosis GalU (O05576),
  Dictyoglomus, Aquifex GalF. None of the Gram-positive, Mollicute or
  actinobacterial leaves makes LPS.
- The MF IBA (GO:0003983) and cytosol come from PTN000501189, seeded by
  experimentally characterised E. coli and B. subtilis enzymes; sound.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000501197 | GO:0009244 lipopolysaccharide core region biosynthetic process | 2 | 33 (27 taxa) | GO:0009244, IMP, PMID:12044687 (PseudoCAP) | SOUND | Knockouts in four serogroups truncate the LPS core and galU complements the PA103 core defect; GalU makes the UDP-glucose donor. Right for P. aeruginosa (kept non-core, as precursor supply). | E. coli GalU P0AEP3 (EcoCyc IMP, acts_upstream_of_or_within) | Formally yes (E. coli seed), but the node term does not suit the clade: it reaches LPS-less Gram-positive, Mollicute and actinobacterial GalU/GtaB proteins. GO_CENTRAL WRONG_TERM (CHECK, CONFIRMED from leaf list) filed on the IBA row. |

Defects filed: GO_CENTRAL WRONG_TERM on PTN000501197 (CHECK; CONFIRMED,
resting on the cached leaf list). No PseudoCAP defect.

## Decisions summary

- ACCEPT: UTP:glucose-1-phosphate uridylyltransferase activity (IBA, IEA);
  cytosol (IBA).
- MODIFY: UDP-alpha-D-glucose metabolic process (IEA) -> UDP-alpha-D-glucose
  biosynthetic process.
- KEEP_AS_NON_CORE: LPS core region biosynthetic process (IBA, IMP).
