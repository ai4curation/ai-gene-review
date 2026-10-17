# hal3 (SPAC15E1.04, UniProt Q9UTI7) notes

Fetch: `just fetch-gene SCHPO hal3` failed (no UniProt ID found for "hal3"; UniProt names the entry "Probable thymidylate synthase" with ORF name only). Fetched with `-u Q9UTI7`; uniprot file confirmed `TYSY_SCHPO`, AC Q9UTI7.

## Evidence
- Fusion protein: N-terminal Hal3-like (HFCD flavoprotein) half + C-terminal thymidylate synthase half [PMID:23962284 "whose amino-terminal half is similar to Sc Hal3 whereas its carboxyl-terminal half is related to thymidylate synthase (TS)"]; [UniProt:Q9UTI7 "In the N-terminal section; belongs to the HFCD (homo-"].
- PPCDC: [PMID:23962284 "also exhibit PPCDC activity in vitro and provide PPCDC function in vivo, indicating that Sp Hal3 is a monogenic PPCDC in fission yeast"]. Contrast S. cerevisiae, where PPCDC is the Cab3 + Sis2/Vhs3 heterotrimer (see genes/yeast/CAB3, SIS2 reviews).
- TS: [PMID:23962284 "the entire protein and its carboxyl-terminal domain rescue the S. cerevisiae cdc21 mutant, thus proving TS function"]. S. pombe has no separate TS gene; hal3 is the TS.
- Ppz inhibition (moonlighting, modest, in vitro): [PMID:23962284 "retain the ability to bind to and modestly inhibit in vitro S. cerevisiae Ppz1 as well as its S. pombe homolog Pzh1"].
- Essential, not processed: [PMID:23962284 "as predicted, Sp hal3 is an essential gene"].
- Localization: cytoplasm/cytosol from ORFeome screen [PMID:16823372].

## Decisions
- Core: GO:0004633 (CoA biosynthesis, cytosol) and GO:0004799 (dTMP biosynthesis, cytosol).
- Protein phosphatase inhibitor IDA kept non-core. FMN binding IDA kept non-core (cofactor of PPCDC).
- Mitochondrion IBA (human TYMS / plant DHFR-TS seeded) marked over-annotated, as in genes/yeast/CDC21.
- Comparison with S. cerevisiae: the budding-yeast PPCDC subunits (CAB3, SIS2) have no molecular_function in core_functions because neither is active alone (contributes_to); hal3 is a complete monogenic PPCDC so `enables` GO:0004633 is appropriate. This is an S. pombe-specific difference, consistent with the module's homo-oligomeric PPCDC variant.
- PomBase GO-CAM 678073a900002636: hal3 enables GO:0004633 in cytosol (IDA PMID:23962284) - agrees. The model does not include the TS activity (out of scope for that model).
