# PP_1134 (Q88NS1) notes — dashboard NZ_BCAU01000123.1_43

Source: https://gene-annotate-dashboard.kbase.us/review/NZ_BCAU01000123.1_43
Dashboard call (tier B): "FAD-dependent dehydrogenase family protein, substrate undetermined." GO terms: GO:0016491 oxidoreductase activity, GO:0071949 FAD binding.

## Mapping
The dashboard query (543 aa) is 99.6% identical to Q88NS1 (535 aa) over 535 aligned residues (query 9-543 = subject 1-535). The 8 extra residues (MAGILDPA) come from an upstream start call. The KT2440 start, MLRITELK..., lines up with the start of the Vibrio VP0956 structure (MIRINEIK...), so the KT2440 model is probably right. There are two substitutions: D234E and L506I (query numbering). Exact UniParc entries are deleted, so the review is filed on Q88NS1 with the dashboard ID as an alias.

## Conclusion
PP_1134 is a cytoplasmic FAD-binding protein of the uncharacterized COG2509 / PIRSF038984 / PTHR42842 family. Its reaction and substrate are unknown.
- **Family.** InterPro IPR028348 describes the family as "uncharacterised FAD dependent proteins. Their function is not clear." The domains are N-terminal DUF8436 (PF28550, residues 1-60), a Rossmann FAD/NAD(P)-binding domain, and the inserted C-terminal domain PF21688. KEGG K07137 calls it an "uncharacterized protein".
- **Homologs.** NCBI BLAST of Q88NS1 (E <= 1e-5) finds one Swiss-Prot entry, the uncharacterized Cbei_0202 (Q05627, 48.0%), and one PDB entry, 3NLC (VP0956, 67.5% over 533 residues, FAD bound, structural genomics, no activity reported). No characterized homolog at >= 40% identity names a substrate.
- **Not a known family.** No UbiI/UbiH-type 2-polyprenylphenol hydroxylase, FixC/ETF-QO, ETF dehydrogenase or geranylgeranyl reductase hits at that threshold. YgiD (a DOPA dioxygenase, not a flavoprotein) is not relevant.
- **Fitness.** KT2440 RB-TnSeq, read from BERDL `kescience.fitnessbrowser` (run `20261030T213420Z-pp1134-fitness`), shows no phenotype in 300 experiments: fitness ranges from -0.59 to +0.47 and no |t| reaches 4. There is no specific phenotype, and the best cofitness is 0.44 (PP_0567), which is uninformative.
- **Neighbourhood.** The neighbours are NhaA (PP_1132), an IS transposase (PP_1133), an uncharacterized exported protein (PP_1135, same strand, ~100 bp away), PP_1136, and a Liv-type ABC transporter (PP_1137-1139). The NhaA/SlyB/lipoprotein synteny is conserved across Pseudomonas, but none of these genes points to a substrate.

## Dashboard verdict
**Supported.** The call is appropriately hedged. Its tier-B rationale is accurate, and it correctly rejected the disulfide-reductase, amine-oxidase and BaiO suggestions, which came from 46-49% homologs or from single domain hits on homologs. "Dehydrogenase" is only the COG2509 label.

Suggested annotation: "FAD-binding oxidoreductase-like protein, COG2509/PIRSF038984 family; reaction and substrate unknown."

PredictionReview scores:
- GO:0071949 FAD binding: **COR**, from the FAD-bound 3NLC structure.
- GO:0016491 oxidoreductase activity: **UNC**, inferred from the fold only, with no activity shown for any member. The rubric prefers UNC for novel terms that rest only on domains.

The gene review still proposes GO:0016491 as a hedged NEW ISS, because it is the most specific defensible molecular-function class.

## Caveats
- The EBI BLAST service refused jobs (fair-use block), so NCBI BLAST URL API was used against `swissprot` and `pdbaa` only. TrEMBL members with experimental data could be missed. One example is the Arabidopsis PDE327 (At4g30720), the only Arabidopsis IPR028348 member with literature, probably the 37.9% Arabidopsis homolog in the dashboard evidence. It is named for a pigment-defective mutant screen and has no biochemistry.
- PaperBLAST and Fitness Browser web (fit/papers.genomics.lbl.gov) returned 403.

## Files and runs
- Runs (in `projects/hackathon/runs/`): `20261030T213754Z-pp1134-homology` and `20261030T213420Z-pp1134-fitness`.
- Frozen evidence in `PP_1134-dashboard-prediction-evidence/`: `dashboard_call.json`, `dashboard_page.txt`, `homology_results.json`, `pdb_3NLC_ligand.json`, `fitness_results.json`.
- Scripts in `PP_1134-bioinformatics/` (`homology.py`, `fb_fitness.py`, `RESULTS.md`).
- History record: `history/genes/PSEPK/PP_1134/2026-10-30T214226Z-claude-code-7bb5e2.yaml`.

## Tooling
- `just fetch-gene` timed out against EBI once and succeeded on retry.
- `just fetch-fitness` failed because no FEBA source was reachable; worked around via BERDL.
- `just fetch-gene-pmids` found no PMIDs.
- Deep research ran with the `claude-code` provider.
- `validate-predictions` writes the shared `reports/prediction-evidence.json`.
