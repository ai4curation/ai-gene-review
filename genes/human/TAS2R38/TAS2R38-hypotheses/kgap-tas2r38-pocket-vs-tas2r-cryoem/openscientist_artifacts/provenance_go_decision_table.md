# GO decision table (leads requiring curator verification): TAS2R38 / P59533

All rows are leads. None is a finished curation decision. No row rests on an
experimental TAS2R38 structure, because none exists.

| GO term | Aspect | Lead action | Supporting evidence | Suggested evidence code | Notes and risks |
|---|---|---|---|---|---|
| GO:0033038 bitter taste receptor activity | MF | Retain as a core function | PMID 15723792 and the PTC/PROP haplotype literature; PMID 38732607 shows the haplotype explains ~29% of PROP bitterness variation in 243 people | EXP / IDA for the heterologous assays, IEP for the human psychophysics | Well supported independently of this hypothesis. The structural work here neither strengthens nor weakens it |
| GO:0001580 detection of chemical stimulus involved in sensory perception of bitter taste | BP | Retain | Same | EXP | Core process term |
| GO:0005886 plasma membrane | CC | Retain | Heterologous expression and the sinonasal immunohistochemistry in PMID 40353482 | IDA | PMID 40353482 reports translocation from the membrane under inflammatory conditions, worth a qualifier note rather than a term change |
| GO:0004930 G protein-coupled receptor activity | MF | Retain | Fold match to two G-protein-bound TAS2R cryo-EM structures (TM-score 0.708-0.763); the intracellular cavity lining of TAS2R38 is the most conserved part of the receptor across 28 human TAS2Rs (0.673 vs 0.254 background, p = 2.7e-08) | ISS supported by this job's structural and evolutionary analysis | The evolutionary result is new support for the coupling face specifically |
| GO:0005515 protein binding | MF | Do not use as a final recommendation | n/a | n/a | Explicitly avoided per the brief; GO:0031683 G protein beta/gamma-subunit complex binding or GO:0001664 G protein-coupled receptor binding would be more informative if an interaction term is wanted, but neither is supported by direct TAS2R38 data found here |
| Binding-site annotation for PTC/PROP (UniProt BINDING feature or GO MF with a ligand qualifier) | MF / feature | Do not create from the model alone | Model-derived only; the pocket-forming region deviates 4.0-6.2 Å from the templates and ECL2 by 8.9-14.3 Å at pLDDT 68.6; the apo-model orthosteric cavity is 34 Å³, too small for PTC | n/a | This is the main negative recommendation. A binding-site feature would imply a precision the evidence does not have |
| Residue-level note: W99 as the family-conserved activation toggle | MF supporting note | Add as an annotation comment lead | W99 is the structural equivalent of TAS2R46 W88 and TAS2R14 W89, makes the closest approach to the superposed agonist (2.4 Å) and is the only residue of interest lining the detected cavity (3.03 Å); conserved in 22 of 27 human TAS2Rs | ISS | Requires curator verification of the TAS2R46/TAS2R14 toggle assignment in the primary papers |
| Variant annotation, rs10246939 V296I | sequence feature | Lead: annotate as a position at the intracellular / G-protein coupling face, not a ligand-contact position | 296 is 5.1 Å from the intracellular cavity, 6.4 Å from the modelled Gα α5 helix, and 15.9-22.6 Å from the orthosteric ligands; model placement at this residue is the most reliable of the 11 measured (deviation 1.76-1.90 Å); I296 is the family consensus (21/27), so the taster V296 is the divergent state | ISS | The structural placement is solid; the functional consequence is inferred, not measured |
| Variant annotation, rs713598 P49A | sequence feature | Lead: annotate as an intracellular / TM1 cytoplasmic position, not a ligand-contact position | 32.5-34.8 Å from all three orthosteric ligands, 8.27 Å from the modelled α5 helix; deviation 2.26-4.15 Å | ISS | The family carries K or R at this position in 20 of 26 paralogs, so no family-level functional inference is available |
| Variant annotation, rs1726866 A262V | sequence feature | Lead: do NOT annotate as a coupling-only or helix-packing-only variant | 2.12 Å from the superposed orthosteric ligand in the 8XQO frame, 5.88 Å in the 7XP6 frame, 23.4 Å from the α5 helix; independent prediction in PMID 22656649 places residue 262 in contact with PTC and PROP | ISS | Cα placement uncertainty at this residue is 2.6-8.1 Å, so "pocket wall" is the defensible wording, not "direct contact" |
| Any annotation implying an intracellular tastant-binding site in TAS2R38 | MF | Do not transfer from TAS2R14 | PMID 38776963 and PMID 38600377 report intracellular tastant sites in TAS2R14; there is no TAS2R38 equivalent evidence | n/a | Paralog overannotation risk. The cryo-EM finding is TAS2R14-specific so far |

## One-line curation summary

Keep the bitter taste receptor function, process and location terms. Do not
add a PTC/PROP binding-site annotation from the AlphaFold model. Record the
three haplotype positions with the correction that A262 is at the pocket wall
while P49 and V296 are at the intracellular face.
