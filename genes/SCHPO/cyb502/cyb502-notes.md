# cyb502 (SPBC29A10.16c; UniProt O94391) notes

Fetch: `just fetch-gene SCHPO cyb502` failed (UniProt entry carries no gene name, only the ORF name);
fetched with `fetch-gene SCHPO cyb502 -u O94391`. Verified `AC   O94391` (CYB51_SCHPO, "Probable cytochrome b5 1") [UniProt:O94391].
PomBase API (2026-10-06): uniquename SPBC29A10.16c, name **cyb502**, product "cytochrome b5 Cyb502", characterisation status "biological role inferred", deletion viable.

## Sequence-based evidence
- Cyt-b5 heme-binding domain (Pfam PF00173, residues 3-79) with heme-ligand binding sites at 38 and 62, and a single C-terminal transmembrane segment (100-120): a tail-anchored microsomal-type cytochrome b5 [UniProt:O94391].
- UniProt function is by similarity only [UniProt:O94391 "Membrane bound hemoprotein which function as an electron"].
- PANTHER PTHR19359:SF150 (CYTOCHROME B5); paralog oca8 (Q9USM6) is PTHR19359:SF147.

## Experimental data in S. pombe
- Only the ORFeome YFP localisation (PMID:16823372, abstract-only): ER (PomBase HDA, GO:0005783). Note: ORFs were tagged at the C terminus, which can perturb targeting of tail-anchored proteins; the ER call nevertheless matches expectation.
- PomBase phenotypes (large-scale screens) include sensitivity to terbinafine, itraconazole and tamoxifen (PomBase gene page API), compatible with a role in sterol synthesis but not specific.
- No biochemical characterisation of Cyb502 or Oca8; which paralog supports which sterol enzyme is unknown.

## Ortholog (S. cerevisiae CYB5, P40312)
- CYB5 review core: GO:0009055 electron transfer activity; directly_involved_in GO:0016126 sterol biosynthetic process; ER membrane. Budding-yeast evidence: antibodies to Cyb5 inhibit C-4 demethylation [PMID:6163470 "lanosterol was inhibited by antibodies to yeast cytochrome b5"]; Cyb5 suppresses CPR-deletion azole hypersensitivity [PMID:8181746 "is required and sufficient for the suppressor effect"]; Cyb5/Cbr1 can fully support CYP51 [PMID:10622712 "can be wholly and efficiently supported by the cytochrome b5/NADH cytochrome b5"].
- Here I use GO:0006696 ergosterol biosynthetic process (PomBase's more specific term, the fungal end product), a descendant of the CYB5 review's GO:0016126; not a disagreement.
- S. pombe has two microsomal-type b5 paralogs (cyb502, oca8) versus one in S. cerevisiae; redundancy/specialisation untested.

## GO-CAM (gomodel:66c7d41500002088)
- Activity 678073a900001270: cyb502 enables GO:0009055, ER membrane, part_of ergosterol biosynthesis; cbr1 (GO:0004128) directly provides input for cyb502; cyb502 directly provides input for erg31 and erg32 (C-5 sterol desaturases). The model does not connect cytochrome b5 to erg25 (C-4 methyl oxidase) or erg11, whereas the module's cyb5_activity PROVIDES_INPUT_FOR erg25.
