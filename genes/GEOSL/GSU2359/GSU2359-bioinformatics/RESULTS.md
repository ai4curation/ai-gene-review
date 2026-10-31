# GSU2359 (Q74AJ5): GH57 catalytic residues, subfamily placement, gene neighbourhood and fusion check

Scope: GSU2359 (Q74AJ5, *Geobacter sulfurreducens* PCA, 817 aa) and its GH57 + DUF3536
relatives A2cp1_1916 (B8J768, *Anaeromyxobacter dehalogenans* 2CP-1) and DVU_2472 (Q728Y0,
*Nitratidesulfovibrio vulgaris* Hildenborough, the comparator without glucan neighbours).

All analyses were run from the BERIL hackathon project with `uv run beril run`; the scripts
are copied in `scripts/` and the run outputs in `data/`.

| Run | Script | What it does |
|---|---|---|
| `20261030T234043Z-gh57-catalytic` | `scripts/gh57_catalytic.py` | hmmalign/hmmsearch (pyhmmer) against Pfam PF03065 (GH57) and PF12055 (DUF3536) |
| `20261030T234824Z-gh57-identity` | `scripts/gh57_identity.py` | pairwise global identities |
| `20261030T234844Z-gh57-cazy` | `scripts/gh57_cazy.py` | CAZy GH57 subfamily placement and characterized activities |
| `20261030T233053Z-gh57-synteny` | `scripts/gh57_synteny.py` | gene neighbourhoods of all DUF3536 genes in the BERDL pangenome (kbase.ke_pangenome) |
| `20261030T234618Z-gh57-fusion-check` | `scripts/gh57_fusion_check.py` | are any GH57/DUF3536 genes fused to TreY? |

## 1. Domain architecture

hmmsearch (Pfam HMMs from InterPro) gives GSU2359 a GH57 domain (PF03065, envelope 19-312,
i-Evalue 1.7e-22) followed by a full-length DUF3536 domain (PF12055, envelope 340-623,
i-Evalue 7.7e-120). The characterized Pontibacter PoGH57 (QCR22797.1) has the same
architecture: GH57 6-311 and DUF3536 339-623. The characterized Thermocrinis albus Amo45
(D3SMQ0) also carries both domains (GH57 1-268, DUF3536 296-491). No other Pfam domain
was found in any of these proteins (data/domains.tsv).

## 2. Catalytic residues

GH57 enzymes use a Glu nucleophile on strand beta4 (CSR-3) and an Asp proton donor on
strand beta7 (CSR-4) (PMID:15233783, PMID:29998051). Four GH57 enzymes with UniProt
active-site annotations were aligned to the PF03065 HMM: T. litoralis 4-alpha-glucanotransferase
O32462 (Glu123, Asp214; crystal structure PMID:12618437), T. kodakarensis branching enzyme
Q5JDJ7 (Glu183, Asp354), T. thermophilus branching enzyme Q5SH28 (Glu184, Asp353) and
P. horikoshii branching enzyme O50094 (Glu185, Asp355).
All four nucleophiles fall in HMM match column 150 and all four proton donors in column 241.

| Protein | Nucleophile (col 150) | Proton donor (col 241) | CSR-3 window | CSR-4 window |
|---|---|---|---|---|
| T. litoralis 4AGT O32462 | Glu123 | Asp214 | WLTERV | HDDGEKFGVW |
| GSU2359 Q74AJ5 | Glu154 | Asp263 | WLAETA | ATDGETYGHH |
| A2cp1_1916 B8J768 | Glu154 | Asp261 | WLPETA | AVDGETLGHH |
| DVU_2472 Q728Y0 | Glu153 | Asp262 | WLAESA | CTDGETYGHH |
| PoGH57 QCR22797.1 (characterized) | Glu154 | Asp262 | WLGETA | ATDGETYGHH |
| Amo45 D3SMQ0 (characterized) | Glu139 | Asp223 | WLPELA | AVDGETFGHH |

GSU2359 keeps both GH57 catalytic residues: Glu154 at the nucleophile position and Asp263 at the proton-donor position.

Across every UniProtKB protein carrying DUF3536 (588 sequences, 583 aligned at these
columns), the nucleophile Glu is present in 583 of 583 and the proton-donor Asp in 582 of 583.
DUF3536-containing GH57 proteins are therefore not a "like" group that has lost its catalytic machinery.

GSU2359 lacks the CSR-4 fingerprint of GH57 glycogen branching enzymes (E-L-F/Y-G-H-W in the
branching enzymes, ETYGHH in GSU2359), as does PoGH57, whose authors used this to rule out branching-enzyme activity.
The N-terminal CSR-1 (HQP in O32462) lies before the region the HMM aligns in the DUF3536 proteins, so it was not scored.

## 3. Pairwise identity to characterized relatives

| Pair | % identity (aligned columns) | aligned columns |
|---|---|---|
| GSU2359 vs PoGH57 (QCR22797.1) | 49.4 | 806 |
| GSU2359 vs A2cp1_1916 | 45.4 | 798 |
| GSU2359 vs DVU_2472 | 41.8 | 728 |
| GSU2359 vs Amo45 (D3SMQ0) | 33.9 | 655 |

GSU2359 is 49.4% identical to the characterized Pontibacter sp. SGAir0037 PoGH57 over 806 aligned residues.

## 4. CAZy subfamily and characterized activities

CAZy assigns GSU2359 (AAR35733.2), A2cp1_1916 (ACL65258.1) and DVU_2472 (AAS96944.1) all to subfamily GH57_6.
GH57_6 is the "non-specified amylase" subfamily of Polacek et al. 2025 (PMID:40187459).
CAZy lists four characterized GH57_6 members: alpha-amylase Pcal_0672 (Pyrobaculum calidifontis), alpha-amylase Amo45 (Thermocrinis albus), alpha-amylase Amy_GH57 (uncultured bacterium) and PoGH57 (Pontibacter sp. SGAir0037; EC 2.4.1.25 and 3.2.1.1).
Of the 41 characterized GH57 entries in CAZy, the EC numbers are 3.2.1.1 (25), 3.2.1.41 (15), 2.4.1.25 (8), 2.4.1.18 (7), 3.2.1.133 (3), 3.2.1.54 (2) and 3.2.1.22 (1).
No characterized GH57 enzyme is an alpha-mannosidase (EC 3.2.1.24, 3.2.1.113, 3.2.1.114 or 3.2.1.170).

The "alpha-mannosidase" in the COG1449 name and the "Glycoside hydrolase 38, N-terminal
domain" Gene3D hit reflect the shared fold of the GH57 and GH38 catalytic domains (the
T. litoralis 4AGT structure resembles Golgi alpha-mannosidase II, PMID:12618437), not a
mannosidase activity of any GH57 member.

## 5. Gene neighbourhood across genomes (BERDL pangenome)

Method: the 1369 kbase.ke_pangenome gene clusters whose eggNOG-mapper Pfam list includes
DUF3536 were taken as the family. One genome per GTDB species was sampled (1257 species,
1288 genes, plus the dashboard genomes). Genes within 5 positions on the same contig were
annotated with eggNOG KEGG orthologs: TreY K06044, TreZ K01236, TreS K05343, MalQ K00705,
GlgB K00700, GlgE K16147 and other alpha-glucan markers (data/synteny_results.json).

In G. sulfurreducens the gene order is treZ (-1), GSU2359, treY (+1), treS/maltokinase (+2).
The same treZ-GH57-treY-treS order is found in the second G. sulfurreducens genome and in Geobacter metallireducens.
In Pontibacter (5 species) the GH57/DUF3536 gene lies between treZ and treY, with treS, malQ and glgB within 4 genes.

| Within 5 genes of a DUF3536 gene | species | fraction of 1257 species |
|---|---|---|
| treY | 144 | 11.5% |
| treZ | 160 | 12.7% |
| treY and treZ | 121 | 9.6% |
| treY or treZ | 183 | 14.6% |
| treY directly adjacent | 130 | 10.3% |
| glgB | 307 | 24.4% |
| malQ | 178 | 14.2% |
| treS | 132 | 10.5% |
| any alpha-glucan marker | 507 | 40.3% |

The TreZ-GH57-TreY arrangement is a lineage-specific feature (for example 21 of 30 sampled Desulfobacterota_F genes have both treY and treZ nearby, but 0 of 259 Cyanobacteriota genes do), not a property of the whole DUF3536 family.
Most DUF3536 genes (about 60% of species) have no alpha-glucan marker gene within 5 genes.
Neither A2cp1_1916 (or the other two Anaeromyxobacter genomes sampled) nor DVU_2472 has any alpha-glucan marker gene within 5 genes.

## 6. Is GH57/DUF3536 ever fused to TreY?

All 1369 DUF3536 gene clusters carry exactly the same Pfam pair, DUF3536 + Glyco_hydro_57, and no other domain.
None of the 1369 clusters encodes a protein of 1200 aa or more (median 807 aa), so none is a fusion with TreY (about 1000 aa in G. sulfurreducens).
eggNOG-mapper gives 128 of these clusters the TreY ortholog K06044, but they are 777-819 aa (10th-90th percentile) and have no GH13 Alpha-amylase domain, so the TreY label is an orthology-transfer artefact rather than a fusion.
STRING's "fusion" channel linking the Anaeromyxobacter protein to TreY is therefore not supported by any fused gene in the pangenome.

## 7. Limitations

- Activities are inferred from the subfamily; GSU2359 itself has not been assayed.
- PoGH57 activity is low and its mode (hydrolysis versus 4-alpha-glucanotransfer) depended on substrate and enzyme order (PMID:38930854).
- Neighbourhood markers depend on eggNOG KO calls; a missed KO would lower the counts.
- CAZy subfamily assignments were read from the CAZy web pages on 2026-10-30.
