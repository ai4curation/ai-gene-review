# RFC1 (ARATH, Q9C587) review notes

## Session 2026-10-28

- `just fetch-gene ARATH RFC1` resolved Q9C587 (Swiss-Prot, TAIR AT5G22010, GeneID 832261); GOA has 15 rows.
- Literature: see RFC1-deep-research-manual.md (manual synthesis; no provider run).
  Full text read: PMID:23144629, PMID:20639449, PMID:29971074. Abstract only: PMID:22974522,
  PMID:17556804, PMID:24053948.
- Picture: RFC1 is the large subunit of the RFC clamp loader [PMID:29971074 "AtRFC1, like p140, binds to the core complex with the help of the other subunits."];
  nuclear [PMID:20639449 "GFP fluorescence was mainly detected in the nucleus"]; essential
  (rfc1-3 seed lethal, PMID:23144629); required for somatic DNA-damage tolerance (MMS, cisplatin;
  PMID:20639449) and for class I meiotic crossovers downstream of RAD51 (PMID:23144629).

## Decisions

- Clamp loader activity: kept (ACCEPT); core function written as contributes_to (RFC1 cannot load PCNA alone).
  ATP binding (Walker A 399-406) is a subunit-level activity and goes in molecular_function.
- ATP hydrolysis IEA: KEEP_AS_NON_CORE (ATPase sites in clamp loaders are formed at subunit
  interfaces with a trans arginine finger; no Arabidopsis biochemistry).
- DNA binding (IBA, IEA): KEEP_AS_NON_CORE; true for the family (primer-template junction
  binding) but generic, and a more specific descendant cannot be supported for the plant protein.
- DNA damage response IMP -> MODIFY to DNA repair (GO:0006281, is_a descendant checked with OAK);
  mutant sensitivity to MMS/cisplatin and elevated SHR support repair participation.
- Meiotic cell cycle IMP (PMID:22974522, abstract only) -> MODIFY to reciprocal meiotic
  recombination GO:0007131 (part_of/is_a descendant of GO:0051321, checked with OAK); abstract
  explicitly supports meiotic HR DSB repair.
- Resolution of meiotic recombination intermediates IMP (PMID:23144629): ACCEPT under
  acts_upstream_of_or_within; data place RFC1 upstream of dHJ formation/resolution in class I COs.
- Epigenetic regulation of gene expression IMP: KEEP_AS_NON_CORE; the authors themselves suggest
  part of the TGS release is an indirect consequence of genome instability.
- NEW: chromosome (GO:0005694) IDA from PMID:22974522 (immunolocalization to meiotic chromosomes
  stated in abstract). No NEW process terms proposed.
- UniProt FUNCTION mentions "hypersensitive response (HR)"; could not trace this in cached texts.
  Raised as a suggested question only.
