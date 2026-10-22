# cab4 (SPAC1F12.08, UniProt Q10350) notes

Fetch: `just fetch-gene SCHPO cab4` failed (UniProt entry is "Uncharacterized protein C1F12.08", no gene name). Fetched with `-u Q10350`; uniprot file confirmed YDA8_SCHPO / Q10350 (316 aa).

## Evidence
- Domain content: only a cytidylyltransferase-like domain [UniProt:Q10350 "IPR004821; Cyt_trans-like."; "PF01467; CTP_transf_like; 1."]; no CoaE/DPCK domain (no IPR001977/PF01121, contrast cab5).
- Orthology: [UniProt:Q10350 "SIMILARITY: To yeast YGR277c."] (S. cerevisiae CAB4, the PPAT).
- S. cerevisiae CAB4 (YGR277C) is essential and complemented by E. coli coaD [PMID:19266201 "Null mutants could be complemented by their bacterial counterparts coaBC, coaD and coaE, respectively."].
- Localization: cytosol + nucleus (ORFeome YFP, PMID:16823372).

## Decisions
- GOA has NO GO:0004595 PPAT annotation for cab4; only an IBA for GO:0004140 dephospho-CoA kinase (PTN000075336) - REMOVE (domain architecture excludes it), same as genes/yeast/CAB4.
- 'catalytic activity' IEA MODIFIED to GO:0004595 to supply the correct MF.
- Core MF GO:0004595 (by orthology; no S. pombe biochemistry).
- PomBase GO-CAM 678073a900002636 has two cab4 activities: GO:0004595 (ISO from human COASY, GO_REF:0000024; agrees) and GO:0004140 (69b3372b00002564, IBA PTN000075336; disagrees - cab4 lacks a DPCK domain; cab5 already provides GO:0004140 in the same model).
