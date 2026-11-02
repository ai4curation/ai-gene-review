# oca8 (SPCC16A11.10c; UniProt Q9USM6) notes

Fetch: `just fetch-gene SCHPO oca8` fetched `AC   Q9USM6` (CYB52_SCHPO, "Probable cytochrome b5 2", 129 aa) - correct accession [UniProt:Q9USM6].
PomBase API (2026-10-06): name oca8, product "cytochrome b5", characterisation "biological role published", deletion viable. The gene name is not informative about biochemical function (not verified here what the "oca" screen measured).

## Sequence-based evidence
- Cyt-b5 heme-binding domain (PF00173, 3-79), heme-ligand binding sites 38 and 62, cytochrome b5 heme-binding-site signature (IPR018506), and a C-terminal TM segment (105-125): a tail-anchored microsomal-type cytochrome b5 [UniProt:Q9USM6].
- UniProt function by similarity [UniProt:Q9USM6 "Membrane bound hemoprotein which function as an electron"].
- UniProt location: ER membrane and microsome membrane by similarity; "Mitochondrion" with ECO:0000269 from the ORFeome YFP screen (PMID:16823372) [UniProt:Q9USM6]. ORFeome tagged ORFs at the C terminus; for a tail-anchored protein this can mistarget the fusion (tail anchors must be C-terminal), so the mitochondrial call is uncertain. PomBase has not made an HDA mitochondrion annotation for oca8.
- PANTHER PTHR19359:SF147 (CYTOCHROME B5 2-RELATED); paralog cyb502 (O94391) is SF150.

## Experimental data
- No biochemical or sterol data for Oca8. PomBase lists large-scale phenotypes including itraconazole sensitivity (PomBase gene page API), compatible with but not specific for a sterol-pathway role.

## Ortholog (S. cerevisiae CYB5) and GO-CAM
- Same reasoning as cyb502 notes; CYB5 review core = GO:0009055, sterol biosynthesis, ER membrane. I use GO:0006696 (descendant), not a disagreement.
- GO-CAM gomodel:66c7d41500002088 activity 678073a900001241: oca8 enables GO:0009055 in ER membrane, part_of ergosterol biosynthesis; Cbr1 provides input; oca8 provides input to erg31 and erg32. No link to erg25 (module has cyb5 -> erg25).
