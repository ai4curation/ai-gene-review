# PP_4572 (Q88E94) curation notes

Reached from KBase gene-annotate dashboard protein
[CP069317.1_1962](https://gene-annotate-dashboard.kbase.us/review/CP069317.1_1962)
(P. putida, tier B, "Dark (no prior function)"). The query is 97.2% identical over 357/357 residues to
KT2440 PP_4572. The same value comes from the final mapping run and from the local alignment in
`PP_4572-bioinformatics/homology_topology_results.json`. The exact-match UniParc entries were deleted,
so the review is filed on reference-proteome entry Q88E94, with the dashboard ID as an alias.

## Conclusion

PP_4572 is an **inner-membrane-anchored AsmA-like protein of unknown function**. It is the full-length
orthologue of *P. aeruginosa* PA2708 (Q9I0D4).

- **Family.** It belongs to InterPro IPR052894 / PANTHER PTHR30441:SF4 (AsmA-like; the query hit spans
  residues 8-244).
  - The UniProt name "DUF748 domain-containing protein" is a ProtNLM prediction. Q88E94 itself has no
    recorded Pfam PF05359 (DUF748) match, but PA2708 and other Pseudomonas orthologues carry DUF748
    (dashboard homolog-domain block).
  - "AsmA-related" is therefore justified at the family level by PANTHER, InterPro and orthology, not
    by the DUF748 domain on the query.
- **Topology.** DeepTMHMM predicts residues 1-6 cytoplasmic, a transmembrane helix at 7-30, and 31-357
  outside, i.e. periplasmic. There is no signal peptide, so this is a signal-anchor.
  - A Kyte-Doolittle scan finds only this one hydrophobic segment.
  - The AlphaFold v6 model has mean pLDDT 79.9. Its periplasmic region is strand-rich (46% of CA i/i+3
    distances are strand-like, a crude estimate) and extends at most about 86 A.
  - Run: `20261030T215439Z-pp4572-homology-topology`.
- **Orthology.**
  - PP_4572 vs PA2708: 71.7% identity over 357 aligned residues, covering both full sequences.
  - E. coli AsmA-like proteins give only weak, partial local alignments: AsmA 24.1% over 195 residues
    (SW 51), TamB 26.2% over 126, and YhdP, YdbH, YicH and YhjG cover less than 21% of PP_4572. It is
    not an orthologue of any of them.
  - This agrees with the PP_4704 review, which lists PP_4572 as the PA2708 orthologue within the
    KT2440 AsmA-like set (TamB PP_2893, YhdP PP_0938, YhjG PP_4857, AsmA PP_0287, EpaF PP_4704,
    PA2708-like PP_4572).
- **What is known about PA2708** (Sposato et al. 2024, PMID:38305166):
  - It is much shorter than the other AsmA-like proteins, and its periplasmic domain is "likely not
    sufficient to span the entire periplasmic space".
  - Deleting it did not worsen growth of a TamB-depleted ΔyhdP ΔydbH strain, so it "is not required
    for P. aeruginosa growth".
  - Its role is open. The authors speculate that it might work with outer-membrane partners.
- **KT2440 fitness** (BERDL, run `20261030T214253Z-pp4575-pp4572-fitness`):
  - There is no phenotype in 300 experiments. Fitness ranges from -0.39 to +0.39, with no |fit| ≥ 1
    and |t| ≥ 4.
  - The top cofitness is only 0.27, with a transmembrane sensor, an ECF sigma factor and FpvA. That is
    uninformative.
  - It does not share the pyroglutamate phenotype of the neighbouring PP_4575-PP_4579 Pxp cluster, so
    it is not part of that operon functionally. Its downstream same-strand neighbours (PP_4573 AAA
    ATPase, PP_4574) also have no phenotype.

## Dashboard verdict

**Recommended verdict: supported** for a family-level call.

Corrected annotation: "AsmA-like (PTHR30441:SF4) inner-membrane-anchored protein with a periplasmic
beta-rich domain; orthologue of P. aeruginosa PA2708; function unknown, dispensable in the orthologue;
no lipid-transport or OM-biogenesis role demonstrated."

| GO term | Assessment |
|---|---|
| GO:0005886 plasma membrane | **CNN** (2). Correct, but already in GOA as a TreeGrafter IEA. |

The call was appropriately cautious. It rejected an outer-membrane beta-barrel reading and a specific
lipid-transport activity. It did not identify PA2708 as the orthologue or use the one experiment on it.
The dashboard's PaperBLAST panel showed only a table snippet of Sposato et al. One wording issue: the
call says InterProScan identifies the family, but on the query that is only a PANTHER hit.

## GOA review

- GO:0005886 plasma membrane (IEA): **ACCEPT**.
- GO:0090313 regulation of protein targeting to membrane (IEA, TreeGrafter): **REMOVE**. It is a
  family-wide propagation from the historical E. coli AsmA/OmpF phenotype, and PP_4572 is not an AsmA
  orthologue.
- No NEW terms. Lipid transfer (GO:0120010) and OM assembly (GO:0043165) were deliberately not added:
  PA2708 is dispensable and too short to bridge the periplasm, and no PP_4572 data exist.

## Caveats

- No experiment has been done on PP_4572. The only experiment on PA2708 is a negative growth test.
- Membrane topology is predicted only.
- The AlphaFold-based length and strand estimates are crude geometric measures, not a DSSP assignment.

## Tooling

- **`just fetch-gene`.** The first try hit an EBI OLS read timeout and the retry succeeded. The PANTHER
  family fetch for PTHR30441 returned InterPro 500, which was not fatal.
- **`just fetch-fitness`.** It failed (403, no local FEBA). The BERDL lakehouse was used instead (see
  `PP_4575-notes.md`).
- **AlphaFold DB.** Inside `beril run` it returned 403, and plain curl alternated between 403 and 200
  depending on the User-Agent. The v6 model was downloaded beforehand with a browser User-Agent into
  `PP_4572-bioinformatics/` and read locally.
- **InterPro.** The protein-entry API timed out, so the absence of a Pfam DUF748 match on Q88E94 rests
  on the UniProt DR lines and the dashboard IPRSCAN block.
- **Deep research.** It used the `claude-code` provider.
