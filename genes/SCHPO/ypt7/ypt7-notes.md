# SCHPO/ypt7 manual review notes

## Scope and source availability

Provider deep research was unavailable in this sparse worktree because the
configured deep-research providers require credentials that were not present. I
used the seeded GOA review, the cached UniProt flat file, the cached PTHR47981
PAINT rows, the cached PomBase GO-CAM for early endosome-to-late endosome and
late endosome-to-vacuole transport, the publication PMIDs cited by the existing
GOA rows, and a PubMed/Europe PMC search for newer `ypt7` and Rab7 fission-yeast
papers.

## PANTHER/IBA assessment

PTHR47981 is the Rab-family PAINT tree. S. pombe ypt7 (`O94655`,
`SPBC405.04c`) is in `PTHR47981:SF20`, `RAS-RELATED PROTEIN RAB-7A`, together
with S. cerevisiae YPT7, N. crassa gtp-14/RAB-7, A. nidulans AvaA/RabS, and
other fungal Rab7/Ypt7 orthologs.

The key fungal node is `PTN001178553`. It places `GO:0000329 fungal-type vacuole
membrane`, `GO:0032889 regulation of vacuole fusion, non-autophagic`, and
`GO:0042144 vacuole fusion, non-autophagic` on the fungal Rab7/Ypt7 branch,
while explicitly pruning lysosome and phagosome-lysosome rows inherited from
broader Rab7 ancestors. S. pombe ypt7 is itself one of the experimental seeds,
so the IBA row is grounded in target-specific evidence and is not circular.

The broader Rab7 node `PTN000635769` places `GO:0005770 late endosome` from
fungal and animal Rab7/Ypt7 seeds. The fungal node leaves that placement intact,
and it matches both the known endosome-to-vacuole fusion role and the 2026
PomBase GO-CAM in `gocams/6918f23700004001`.

`GO:0005773 vacuole` and `GO:0005774 vacuolar membrane` are true but
parent-level beside `GO:0000329 fungal-type vacuole membrane`; I marked those
generic localization rows as too general.

The July 2026 `PTN001939797` PAINT update places `GO:0003925 G protein activity`
on a eukaryotic Rab7 ancestor. That assertion captures the Rab molecular-switch
activity more directly than the older GTPase parent, so I used it as a
replacement for the two generic `GO:0003924` rows.

## Cached publication findings

Bone et al. 1998 identified ypt7 as a fission-yeast factor required for the
rapid vacuole fusion that occurs after hypotonic stress
[PMID:9443913, "Fusion requires Pmk1, Ypt7"].

Kashiwazaki et al. 2005 showed that Ypt7p mediates fusion of endosomes to
vacuoles and homotypic vacuole fusion, and that the extensive vacuole fusion of
sporulating cells depends on Ypt7p
[PMID:16357443, "mediates fusion of endosomes to vacuoles and homotypic vacuole fusion."].

Kashiwazaki et al. 2009 studied the second Rab7 homolog ypt71 and showed that
ypt7 deletion produces small fragmented vacuoles, whereas ypt71 deletion has the
opposite morphology and ypt71 overexpression phenocopies ypt7 loss
[PMID:19453973, "small fragmented vacuoles found in the ypt7 null mutant."].

The Matsuyama et al. 2006 ORFeome localization row is a high-throughput,
C-terminal YFP assay [PMID:16823372, "we determined the localization of 4,431
proteins"]. Because Ypt7 is C-terminally prenylated, and because active
GTP-bound Rab7/Ypt7 works on late endosomal and vacuolar membranes rather than
as a GDP/GDI-bound cytosolic pool, I removed the `is_active_in cytosol` HDA row.

The 2026 PomBase GO-CAM already models the ypt7 GTPase activity as part of
`GO:0045324 late endosome to vacuole transport` at `GO:0005770 late endosome`,
using sequence-orthology evidence from S. cerevisiae YPT7 and PMID:28100638.
This agrees with the direct S. pombe 2005 abstract stating that Ypt7 mediates
endosome-to-vacuole fusion, so I added `GO:0045324` as a conservative NEW row.

## 2024-2026 literature search

PubMed and Europe PMC searches for `(ypt7 OR SPBC405.04c OR Rab7) AND (pombe OR
fission yeast)` found the standard 1998, 2005, and 2009 direct ypt7 papers plus
several broader trafficking papers. The only newer direct fission-yeast ypt7 hit
I found was Wang et al. 2026, which used an Erg6-yeGFP forward screen for
lipid-droplet morphology mutants and recovered mutations in HOPS-complex genes
and their Rab partner Ypt7 [PMID:42882422, "subunits of HOPS complex or its
binding partner Ypt7"].

I did not add a lipid-droplet GO term from the 2026 paper. The phenotype is
interesting and direct enough to record, but the paper frames lipid-droplet
morphology as a genetic consequence of HOPS/Ypt7-dependent vacuolar integrity
rather than as evidence that Ypt7 itself performs a lipid-droplet biogenesis or
lipid-transfer step.
