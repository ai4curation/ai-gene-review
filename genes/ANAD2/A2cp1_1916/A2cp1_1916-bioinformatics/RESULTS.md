# A2cp1_1916 (B8J768): GH57 catalytic residues, subfamily placement, gene neighbourhood and fusion check

Scope: A2cp1_1916 (B8J768, *Anaeromyxobacter dehalogenans* 2CP-1, 812 aa). The analyses
were run once for the whole GH57 + DUF3536 family, together with GSU2359 (Q74AJ5,
*Geobacter sulfurreducens*) and DVU_2472 (Q728Y0). The family-wide method and numbers
are described in `genes/GEOSL/GSU2359/GSU2359-bioinformatics/RESULTS.md`; this file
gives the A2cp1_1916 results. Scripts are in `scripts/`, outputs in `data/`.

Runs (BERIL hackathon project, `uv run beril run`): `20261030T234043Z-gh57-catalytic`,
`20261030T234824Z-gh57-identity`, `20261030T234844Z-gh57-cazy`,
`20261030T233053Z-gh57-synteny`, `20261030T234618Z-gh57-fusion-check`.

## 1. Domain architecture

hmmsearch gives A2cp1_1916 a GH57 domain (PF03065, envelope 49-308, i-Evalue 1.2e-21)
followed by a full-length DUF3536 domain (PF12055, envelope 338-621, i-Evalue 2.3e-101),
and no other Pfam domain.

## 2. Catalytic residues

Aligned to the Pfam GH57 HMM, the nucleophile and proton donor of four structurally or
experimentally defined GH57 enzymes (T. litoralis 4-alpha-glucanotransferase Glu123/Asp214,
and the T. kodakarensis, T. thermophilus and P. horikoshii branching enzymes) all map to HMM
columns 150 and 241.

A2cp1_1916 keeps both GH57 catalytic residues: Glu154 at the nucleophile position and Asp261 at the proton-donor position.

Its CSR-3 window reads WLPETA (T. litoralis WLTERV) and its CSR-4 window AVDGETLGHH
(T. litoralis HDDGEKFGVW). The nucleophile Glu is present in 583 of 583 and the
proton-donor Asp in 582 of 583 aligned UniProtKB DUF3536 proteins.

## 3. Identity to relatives

| Pair | % identity (aligned columns) | aligned columns |
|---|---|---|
| A2cp1_1916 vs GSU2359 | 45.4 | 798 |
| A2cp1_1916 vs DVU_2472 | 39.1 | 740 |
| A2cp1_1916 vs PoGH57 (QCR22797.1, characterized) | 38.9 | 795 |
| A2cp1_1916 vs Amo45 (D3SMQ0, characterized) | 37.6 | 667 |

## 4. CAZy subfamily

CAZy assigns A2cp1_1916 (ACL65258.1) to subfamily GH57_6, the same subfamily as GSU2359 and DVU_2472.
The characterized GH57_6 members are three alpha-amylases (Pcal_0672, Amo45, Amy_GH57) and the Pontibacter PoGH57 (EC 2.4.1.25 and 3.2.1.1); no characterized GH57 enzyme is an alpha-mannosidase.

## 5. Gene neighbourhood

A2cp1_1916 (pangenome gene NC_011891.1_1918) has no alpha-glucan or trehalose gene within 5 genes.
Its neighbours are a von Willebrand factor A domain protein (-2), ThiD phosphomethylpyrimidine kinase (-1), a MarC/UPF0056 membrane protein (+1), a GDSL-family lipase (+2), and an ABC transporter ATPase and FtsX-like permease (+4, +5).
The same holds in the two other Anaeromyxobacter genomes sampled (A. dehalogenans 2CP-C and Anaeromyxobacter sp022808855).
Across the family, only 9.6% of 1257 species have both treY and treZ within 5 genes of their DUF3536 gene; the treZ-GH57-treY arrangement of Geobacter and Pontibacter is lineage-specific.

## 6. Fusion with TreY

None of the 1369 DUF3536 gene clusters in the pangenome is fused to TreY: all carry only the DUF3536 + Glyco_hydro_57 domains and none is 1200 aa or longer.
STRING's fusion-channel link between the Anaeromyxobacter protein and TreY is not supported by any fused gene in the pangenome.

## 7. Limitations

Activity is inferred from the subfamily and conserved catalytic residues; A2cp1_1916 has not been assayed, and no characterized relative is closer than 38.9% identity.
