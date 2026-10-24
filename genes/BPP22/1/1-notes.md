# Gene 1 (PORTL_BPP22, P26744) Notes

## Overview
- **Gene symbol:** `1`
- **UniProt ID:** `P26744` (`PORTL_BPP22`)
- **Protein name:** Portal protein (gp1; Coat protein 1; Gene product 1)
- **Length:** 725 AA

## Function & Structural Insights
- **Dodecameric Portal Vertex (~0.96 MDa):** Assembles into a 12-subunit ring (~300 Å tall, channel diameter 35–75 Å) situated at a single unique 5-fold vertex of the T=7 icosahedral capsid (12:5 symmetry mismatch) [PMID:21499245, PMID:37952769].
- **Three-domain architecture:** Comprises a portal protein core (residues 1-602, folded into leg and hip domains) and a unique ~200 Å-long C-terminal alpha-helical barrel domain (residues 603-725) that extends deeply into the capsid interior like a rifle barrel, guiding DNA spooling during packaging and collimating DNA delivery during host ejection [PMID:21499245].
- **Procapsid Nucleation:** Interacts with scaffolding protein (gp8), which catalyzes oligomerization of portal monomers into dodecameric rings and forms a nucleation complex that initiates procapsid assembly, ensuring incorporation of a single portal vertex per virion [PMID:30787152, PMID:21220301].
- **Headful Packaging Gauge & Signal Transmission:** Point mutations in the portal protein (e.g., V64M / NT5/1a and core compression mutants) alter intravirion DNA length and packing density, showing that DNA pressure-induced compression of the portal core transmits the headful termination signal to the terminase (gp2) to cleave the packaged genome and allows sequential binding of tail completion protein gp4 [PMID:1569567, PMID:28242514].
- **Tail Attachment & Ejection Conduit:** Binds 12 copies of the head-to-tail adapter gp4 at the base of the portal ring, anchoring the 2.9 MDa tail apparatus (gp4, gp10, gp26, gp9) and serving as the conduit for ejection proteins (gp7, gp16, gp20) and viral dsDNA into the Salmonella host cell [PMID:21499245, PMID:37952769].

## Domains & Orthology
- **InterPro:** `IPR032427` (`P22_portal`)
- **Pfam:** `PF16510` (`P22_portal`, 1 hit)
- **Gene3D:** `G3DSA:1.10.1740.160`, `G3DSA:6.10.280.90`

## Curation Decisions
- `GO:0019028` (viral capsid, IEA): **MODIFY** to `GO:0046798` (`viral portal complex`) — `GO:0046798` is a `part_of` child of `GO:0019028` already present in the annotations.
- `GO:0019068` (virion assembly, IDA, PMID:30787152): **ACCEPT** — portal rings nucleate procapsid assembly with scaffolding protein gp8 [PMID:30787152].
- `GO:0019073` (viral DNA genome packaging, IMP, PMID:28242514): **MODIFY** to `GO:0098006` (`viral DNA genome packaging, headful`) — PMID:28242514 specifically investigates the headful packaging density gauge in P22, captured by `GO:0098006`.
- `GO:0046718` (symbiont entry into host cell, IEA): **MODIFY** to `GO:0099002` (`symbiont genome ejection through host cell envelope, short tail mechanism`) — `GO:0099002` is a specific descendant already annotated on `1`.
- `GO:0046798` (viral portal complex, IDA, PMID:21499245): **ACCEPT** — forms the dodecameric viral portal complex [PMID:21499245].
- `GO:0098006` (viral DNA genome packaging, headful, IMP, PMID:1569567): **ACCEPT** — acts as the headful gauge and translocation channel during headful DNA packaging [PMID:1569567].
- `GO:0098015` (virus tail, IDA, PMID:37952769): **KEEP_AS_NON_CORE** — while gp1 forms the viral portal complex (`GO:0046798`), cryo-EM reconstruction of the extracted tail machinery (`PMID:37952769`) shows that the portal dodecamer is an integral structural component of the 2.9 MDa tail apparatus at the unique 5-fold vertex.
- `GO:0099002` (symbiont genome ejection through host cell envelope, short tail mechanism, IDA & IEA): **ACCEPT** — its C-terminal alpha-helical barrel collimates and delivers the viral genome during short-tail ejection [PMID:21499245].
