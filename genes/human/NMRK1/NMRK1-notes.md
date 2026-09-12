# NMRK1 (Nicotinamide riboside kinase 1) — review notes

UniProt: Q9NWW6 (NRK1_HUMAN). Gene synonyms C9orf95, NRK1. Chromosome 9. HGNC:26057.
199 aa monomer; belongs to the uridine kinase family, NRK subfamily.

## Function (authoritative UniProt summary)

NMRK1 is a small-molecule kinase of the NAD+ salvage pathway. It phosphorylates the NAD+
precursor nicotinamide riboside (NR) and nicotinic acid riboside (NaR), using ATP, to give
nicotinamide mononucleotide (NMN) and nicotinic acid mononucleotide (NaMN) respectively;
these feed the NMNAT step of NAD+ biosynthesis.

- [file:human/NMRK1/NMRK1-uniprot.txt "Catalyzes the phosphorylation of nicotinamide riboside (NR)"] / "and nicotinic acid riboside (NaR) to form nicotinamide mononucleotide" / "(NMN) and nicotinic acid mononucleotide (NaMN). The enzyme also" / "phosphorylates the antitumor drugs tiazofurin and 3-deazaguanosine." (FUNCTION, ECO:0000269|PubMed:15137942)
- EC 2.7.1.22 (nicotinamide riboside → NMN) and EC 2.7.1.173 (nicotinic acid riboside → NaMN); both experimentally supported by PubMed:17914902 and PubMed:8809081 [file:human/NMRK1/NMRK1-uniprot.txt "EC=2.7.1.22 {ECO:0000269|PubMed:17914902, ECO:0000269|PubMed:8809081};"].
- Catalytic reactions (Rhea): RHEA:14017 (beta-nicotinamide D-riboside + ATP = beta-nicotinamide D-ribonucleotide + ADP + H+); RHEA:25568 (beta-D-ribosylnicotinate + ATP = nicotinate beta-D-ribonucleotide + ADP + H+).
- PATHWAY: "Cofactor biosynthesis; NAD(+) biosynthesis." [file:human/NMRK1/NMRK1-uniprot.txt "PATHWAY: Cofactor biosynthesis; NAD(+) biosynthesis."] (ECO:0000305|PubMed:17914902); UniPathway UPA00253.
- SUBUNIT: Monomer (PubMed:8809081) [file:human/NMRK1/NMRK1-uniprot.txt "SUBUNIT: Monomer. {ECO:0000269|PubMed:8809081}."].

## Discovery / key literature

- PMID:15137942 (Bieganowski & Brenner, Cell 2004). Discovery paper: identified conserved NRK
  genes (yeast + human) establishing a Preiss-Handler-independent route to NAD+ via nicotinamide
  riboside; NRKs "found to be highly specific for phosphorylation of nicotinamide riboside and the
  cancer drug tiazofurin" [PMID:15137942 "found to be highly \nspecific for phosphorylation of nicotinamide riboside and the cancer drug \ntiazofurin"]. Abstract-only in cache (full_text_available: false); curator (Reactome EXP) read full text.
- PMID:8809081 (Sasiak & Saunders, Arch Biochem Biophys 1996). Purified the human enzyme
  ("nicotinamide ribonucleoside kinase") to near-homogeneity from placenta; monomer ~29-32 kDa,
  pI 5.6, requires ATP, pH optimum 6.5-9.0. "NRK phosphorylated several substrates including
  nicotinamide ribonucleoside, guanosine, tiazofurin, and 3-deazaguanosine" [PMID:8809081 "NRK phosphorylated several substrates including \nnicotinamide ribonucleoside, guanosine, tiazofurin, and 3-deazaguanosine"]. Abstract-only in cache.
- PMID:17914902 (Tempel et al., PLoS Biol 2007). "Nicotinamide riboside kinase structures reveal
  new pathways to NAD+." X-ray structures (1.32 Å) of human NRK1 in complex with ATP and substrates;
  substrate specificity, kinetics, mutagenesis of catalytic Asp-36 and Glu-98. Establishes both
  EC 2.7.1.22 and EC 2.7.1.173 activities. Full text in cache.
- PMID:17698003 (Khan et al., Structure 2007). Crystal structure; mutagenesis K16A/D36A/D56A/D138A
  (not in GOA, but corroborates catalytic residues). Not separately reviewed here.

## Localization

- UniProt gives no subcellular-location CC block. Reactome places catalysis in the cytosol
  (R-HSA-8869606, R-HSA-8869633; both "Cytosolic NMRK1"). GOA has cytoplasm (IBA), cytosol
  (Reactome TAS, ARBA IEA). Cytosol/cytoplasm is well supported. (Some literature reports
  nuclear NRK1 pools, but not in the local files; not asserted here.)

## Protein interactions (bare "protein binding" IPI)

Two large high-throughput binary-interactome maps, no functional characterization of the
interactions:
- PMID:25416956 (Rolland et al. 2014, "A proteome-scale map of the human interactome network") — Y2H; TAX1BP1 (Q86VP1).
- PMID:32296183 (Luck et al. 2020, "A reference map of the human binary protein interactome") — Y2H;
  REL (Q04864-2), INCA1 (Q0VD86), KCTD21 (Q4G0X4), TAX1BP1 (Q86VP1).
These match the UniProt INTERACTION block (INCA1, KCTD21, REL, TAX1BP1). No evidence these
interactions are part of NMRK1's core catalytic function; treated as uninformative
"protein binding" and marked over-annotated (per policy, not removed).

## Review decisions summary

- Core MF: GO:0050262 ribosylnicotinamide kinase activity (EC 2.7.1.22) and GO:0061769 nicotinate
  riboside kinase activity (EC 2.7.1.173) — both experimentally verified (EXP), ACCEPT. IBA and IEA
  duplicates ACCEPT/KEEP as redundant support.
- Core MF adjunct: ATP binding (GO:0005524) — substrate cosubstrate; captured in core_functions.
- Core BP: NAD+ salvage / NAD+ biosynthesis. GO:0034355 (NAD+ biosynthetic process via the salvage
  pathway, IEA/Ensembl) is the best-fitting BP. GO:0009435 (NAD+ biosynthetic process) is the generic
  parent (KEEP). GO:1901847 (nicotinate metabolic process) is correct but generic (KEEP_AS_NON_CORE).
- Location: cytosol/cytoplasm ACCEPT / KEEP.
- metal ion binding (GO:0046872, IEA-KW): Mg2+ is a genuine cofactor (BINDING His-17/Asp-36 to Mg2+);
  this annotation is NOT in the GOA TSV (only appears in the UniProt DR block, dropped by GOA), so it
  is not a reviewed existing_annotation. Noted for completeness.
- protein binding (GO:0005515) IPI x2 (Rolland, Luck): uninformative; MARK_AS_OVER_ANNOTATED.
