# PP_0788 bioinformatics: identity to the dashboard protein, start codon, and Fitness Browser data via BERDL

Runs (from `/home/cmungall/.beril/projects/hackathon/`):

- `runs/20261030T213855Z-pp0788-identity-start` runs `identity_start.py` and writes `identity_start.json`, copied here.
- `runs/20261030T213614Z-pp0788-fitness` runs `fb_fitness.py` against BERDL `kescience.fitnessbrowser` and writes `results.json`, copied here as `fitness_results.json`.

## 1. Identity and the 18-residue length difference

- Query: dashboard protein NZ_CAKNDZ010000038.1_57 (737 aa). Subject: KT2440 PP_0788 (Q88PR0, 719 aa).
- Global alignment (BLOSUM62, free end gaps): 679 identical residues over 717 aligned pairs, 94.7% identity. The mapping table gives 94.6% over 719 pairs.
- The proteins differ only at the N-terminus. The query has 36 residues before the conserved motif RTPHPCLP (query 37, subject 19). PP_0788 has 18. Query residues 1-20 (MALTIFSPFGQDTLQGVQDA) have no counterpart, and the next ~16 residues align poorly with the PP_0788 N-terminus (MQKEGKVVPLAATIDRGG). From RTPHPCLP to the C-terminus the two sequences are colinear and end together (...ESLRQGQAQ).
- This segment lies in the region InterProScan marks as disordered on the query (MobiDBLite 18-40), N-terminal to the conserved DUF1631 core. So the length difference comes from a different start-codon call, or a strain-specific N-terminal sequence, in a non-conserved leader. It does not affect the family assignment.
- KT2440 genome (NC_002947.4, PP_0788 CDS 903742..905901 +): reading the same frame upstream of the annotated ATG, the open extension after the last in-frame stop is LCDFLPIMATSIWRHSFDDFSALSGKTPCKESR, with one in-frame ATG 26 codons upstream. It does not resemble the query's leader. The KT2440 start call (MQKEG...) is not contradicted.

## 2. Domain content and the "Thymidine phosphorylase" name

- The query's InterProScan has one hit, Pfam PF07793 DUF1631, at 40-731 (E = 8.1e-213, covering 99.7% of the HMM). It also has MobiDBLite disorder at 18-40 and 243-265, and a coil at 466-486 (dashboard page).
- In UniProt, Q88PR0 carries four Pfam DUF1631 sub-domain models: PF07793 25-217, PF26671 285-433, PF26672 465-578 and PF26670 630-696. These are the newer split of the old full-length PF07793.
- Q88PR0 has no glycosyltransferase family 3 domain (PF00591 Glycos_transf_3 or PF02885 Glycos_trans_3N). Thymidine phosphorylase (DeoA, EC 2.4.2.4) and its paralog TrpD carry these domains. A UniProt query of KT2440 (taxon 160488) for EC 2.4.2.4, "thymidine phosphorylase" or PF00591 returns three entries. One is TrpD PP_0421 (PF02885;PF00591). One is PpnP PP_4248 (PF06865). The third is Q88PR0, which has only DUF1631 models.
- The UniProt RecName "Thymidine phosphorylase" is evidenced only by ECO:0008006 Google:ProtNLM. Several Fitness Browser orthologs carry the same string (WCS417 GFF773, pseudo1_N1B4 Pf1N1B4_1152, pseudo6_N2E2 Pf6N2E2_3345, pseudo5_N2C3_1 AO356_07365). That points to a propagated legacy gene-description error. The name is unsupported.
- The eggNOG COG1570 (XseA, exonuclease VII large subunit) assignment is also unsupported. KT2440 has a genuine XseA, PP_1027 (Q88P26, 459 aa, PF02601;PF13742). Its XseB is PP_0529. STRING's PP_0788-xseB association therefore probably reflects the mis-assigned orthogroup.

## 3. Fitness (BERDL kescience.fitnessbrowser)

### KT2440 itself (orgId Putida)

- PP_0788 has 300 experiments, with fitness from -0.32 to +0.38. No experiment has |fit| >= 1 and |t| >= 4, and there is no specific phenotype. The top cofitness is 0.25 (PP_3433), which is uninformative.
- The KT2440 compendium has no motility, nitrate-stress or bacitracin experiments. Nitrate and choline chloride were tested only as nitrogen sources, with fitness of -0.08/-0.06 and +0.03/+0.04. So the KT2440 data neither confirm nor refute the dashboard's conditions.
- PP_0788 (+ strand, 903742-905901) lies 88 bp upstream of ampD PP_0789 (+), which is followed by ampE PP_0790 (+). nadC PP_0787 is divergent, on the - strand.

### Orthologs (BBH from the FB ortholog table)

| Ortholog | Experiments | Strong (abs fit >= 1, abs t >= 4) | Groups |
|---|---|---|---|
| WCS417:GFF773 (P. simiae) | 201 | 9 | motility 5, stress 4 |
| psRCH2:GFF703 (S. stutzeri RCH2) | 350 | 47 | stress 30, nitrogen 8, carbon 8, anaerobic 1 (both signs) |
| Dyella79:N515DRAFT_1675 | 68 | 28 | nitrogen 11, carbon 16, stress 1 |
| pseudo6_N2E2:Pf6N2E2_3345 | 188 | 1 | motility 1 (specific phenotype: inner cut, LB soft agar motility) |
| pseudo5_N2C3_1:AO356_07365 | 184 | 0 | - |
| pseudo1_N1B4:Pf1N1B4_1152 | 147 | 0 | - |
| Psyr_0816 (B728a and B728a mexB) | 46 / 23 | 0 | - |
| Marino:GFF1336 | 255 | 0 | - |

- The WCS417 strong set is all negative. The motility hits are five soft-agar motility assays (-1.85, -1.53, -1.14, -1.13, -1.13). The stress hits are nitrate 200 mM (-1.64), choline chloride 300 mM (-1.56), bacitracin 2 mg/ml (-1.30) and phosphomycin 0.003 mg/ml (-1.13). These are the conditions the dashboard named. None is a "specific phenotype" in the FB table.
- Stress phenotypes do not agree across orthologs. RCH2 is sick in L-lysine, carbenicillin, phosphomycin and choline chloride 90 mM, but is fitter in nitrate 250 mM (+1.67), nitrite and chloride. So "nitrate tolerance" goes in opposite directions in the two Pseudomonads where it was measured.
- Reduced motility is the most reproducible signal: five WCS417 experiments plus one specific phenotype in N2E2. Three other Pseudomonas orthologs (N2C3, N1B4, B728a) show nothing. It is not known whether these were tested for motility.
- The Marinobacter homolog cited by the dashboard (33.6%, zinc -3.48) is GFF774, not the BBH GFF1336. GFF1336 has no phenotype.
- Caveat: the gene is co-directional with, and 88 bp upstream of, ampD-ampE. Transposon insertions could be polar on ampDE, which is relevant to the cell-wall-active antibiotics (bacitracin, phosphomycin, carbenicillin) in particular.
