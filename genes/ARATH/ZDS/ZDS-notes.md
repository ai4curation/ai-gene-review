# ZDS (Q38893) curation notes — Arabidopsis thaliana zeta-carotene desaturase

Locus AT3G04870. Synonyms: ZDS1, CLB5, SPC1, PDE181. EC 1.3.5.6. Rhea:RHEA:30955.

## What the gene product is / does

ZDS is a nuclear-encoded, plastid-targeted flavoenzyme of the plant poly-cis
carotene-desaturation route. It catalyses the third of the four backbone steps
(PDS -> Z-ISO -> ZDS -> CRTISO) that convert 15-cis-phytoene to all-trans-lycopene.
Specifically ZDS introduces two double bonds (at C-7 and C-7') into
9,9'-di-cis-zeta-carotene, passing through the intermediate 7,9,9'-tri-cis-neurosporene,
to give 7,7',9,9'-tetra-cis-lycopene (pro-lycopene), using a lipophilic quinone
(plastoquinone) as electron acceptor.

- UniProt FUNCTION: [file:ARATH/ZDS/ZDS-uniprot.txt "essential for the biosynthesis of carotenoids."]
  and [file:ARATH/ZDS/ZDS-uniprot.txt "The main product is 7,9,7',9'-tetra-cis-lycopene"].
- Catalytic activity (ECO:0000269|PubMed:9914519): [file:ARATH/ZDS/ZDS-uniprot.txt "Reaction=9,9'-di-cis-zeta-carotene + 2 a quinone = 7,7',9,9'-tetra-cis-"], [file:ARATH/ZDS/ZDS-uniprot.txt "EC=1.3.5.6"].
- Pathway: [file:ARATH/ZDS/ZDS-uniprot.txt "PATHWAY: Carotenoid biosynthesis; lycopene biosynthesis."].
- Family: [file:ARATH/ZDS/ZDS-uniprot.txt "Belongs to the zeta carotene desaturase family."].
- Substrate stereochemistry: ZDS requires the cis-15,15' bond of PDS-derived
  zeta-carotene to be isomerised (by Z-ISO) first; it shows
  [file:ARATH/ZDS/ZDS-uniprot.txt "Shows stereoselectivity toward trans"] C15-C15' zeta-carotene.

## Evidence review of each GOA row

Cached publications: PMID:9914519, 17468780, 24907342, 12938931 are **abstract-only**
(`full_text_available: false`); PMID:18431481, 20061580 have full text but neither names
ZDS/AT3G04870 in the cached body (they are large chloroplast-proteome/HDA datasets whose
curated ZDS hit I cannot re-derive from the text — I defer to the curator and support the
localization from UniProt).

Molecular function — **9,9'-di-cis-zeta-carotene desaturase activity (GO:0016719)**:
Core MF. Directly established biochemically by Bartley et al. 1999 (recombinant Arabidopsis
ZDS in E. coli): [PMID:9914519 "the two carotene desaturases phytoene desaturase and carotene zeta-carotene desaturase from Arabidopsis thaliana"] and
[PMID:9914519 "We show that pro-lycopene (7,9,7',9'-tetra-cis)-lycopene is the main end product of the plant desaturation pathway in these cells."].
IDA (PMID:9914519), IBA (PTN007457606, IBD-seeded by this gene itself), and IEA
(GO_REF:0000120; RHEA:30955, EC 1.3.5.6) rows all ACCEPT. QuickGO confirms GO:0016719 is
current and its definition matches the Rhea reaction exactly.

**GO:0016491 oxidoreductase activity (IEA, InterPro IPR002937 amino-oxidase/FAD domain)**:
correct but generic parent. MODIFY -> GO:0016719 (the specific desaturase activity the
enzyme actually has; it is an oxidoreductase EC 1.3.5.6).

Process — **carotenoid biosynthetic process (GO:0016117)**: IEA (IPR014103), plus two IMP
rows from the null-mutant phenotypes. spc1/zds: [PMID:17468780 "SPC1 encodes a putative zeta-carotene desaturase (ZDS) in the carotenoid biosynthesis pathway"] and
[PMID:17468780 "several major carotenoid compounds downstream of SPC1/ZDS were substantially reduced in spc1-1, suggesting that SPC1 is a functional ZDS"].
clb5/zds: [PMID:24907342 "Biosynthesis of the signal depends on ζ-carotene desaturase activity encoded by the ζ-CAROTENE DESATURASE (ZDS)/CHLOROPLAST BIOGENESIS5 (CLB5) gene in Arabidopsis thaliana"].
All ACCEPT.

**carotene biosynthetic process (GO:0016120)**: IBA (PTN007457606) and IDA (PMID:9914519,
qualifier acts_upstream_of_or_within). ACCEPT. Brief note: GO:0016120 is NOT a descendant
of GO:0016117 in the current ontology — left as-is, not "fixed".

**lycopene biosynthetic process (GO:1901177)** IDA (PMID:9914519): ACCEPT; pro-lycopene is
the direct product class, and UniProt pathway is "lycopene biosynthesis". QuickGO confirms
GO:1901177 current.

Localization — **chloroplast (GO:0009507)** HDA/IEA/ISM, **chromoplast (GO:0009509)** IEA,
**chloroplast envelope (GO:0009941)** HDA x2: all ACCEPT, consistent with
[file:ARATH/ZDS/ZDS-uniprot.txt "SUBCELLULAR LOCATION: Plastid, chloroplast. Plastid, chromoplast"].
The enzyme is membrane-associated (quinone-dependent; assayed on chromoplast membranes in
PMID:9914519). Envelope sub-localization comes from curated chloroplast-envelope proteomics
(PMID:12938931; PMID:20061580 AT_CHLORO).

## Notably NOT annotated (and why I did not add NEW terms)

The zds/clb5/spc1 mutants show leaf-developmental defects, photoprotection loss, ABA
deficiency and altered plastid-to-nucleus retrograde signalling
([PMID:17468780 "expression of Lhcb1.1, Lhcb1.4 and RbcS was absent in spc1-2, suggesting the possible involvement of carotenoids in the plastid-to-nucleus retrograde signaling"];
[PMID:24907342 "zds/clb5 mutant alleles display profound alterations in leaf morphology and cellular differentiation as well as altered expression of many plastid- and nucleus-encoded genes"]).
These are indirect consequences of an **apocarotenoid signal derived from the accumulated
ZDS substrates** (phytofluene/zeta-carotene) cleaved by CCD4, not activities ZDS itself
performs: [PMID:24907342 "phytofluene and/or ζ-carotene are substrates for an unidentified signaling molecule"].
By the participation test (ZDS does none of the work of leaf development / retrograde
signalling; the signal is made from its substrate when the enzyme is absent), no NEW
process terms for those roles are proposed. ABA deficiency is likewise downstream (carotenoid
supply for the ABA pathway), not ZDS catalysis.

GO:0052889 (specific "9,9'-di-cis-zeta-carotene desaturation to ...-lycopene") appears on
UniProt's DR lines but QuickGO reports it **OBSOLETE** — not used.

## Action tally
ACCEPT 15; MODIFY 1 (GO:0016491 -> GO:0016719); UNDECIDED 0; NEW 0.
