# NOL4 HTH_NOL4 region: computed provenance tables, part 2 (iteration 2)

Continues `nol4_hth_analysis_tables.md`. All values computed in this run from
InterPro API, UniProt REST, QuickGO API, AlphaFold DB and the Foldseek web API.

## Table 9. Foldseek 3Di-AA vs PDB100, three additional NOL4 queries

| Query region | Hits returned | Significant (E < 1e-3) | Best E | Top hit |
|---|---|---|---|---|
| 406-500 (IPR056549) | 17 | **0** | 2.96 | 4x0g_D Bsg25A |
| 1-638 (full length) | 2 | **0** | **6.8** | 1fjg_T Thermus 30S ribosomal subunit |
| 1-210 (N-terminal block) | 2 | **0** | 5.3 | 5ccv_H NS5 |
| 130-210 | 0 | 0 | - | no hits returned |

No region of NOL4 has a structural relative in the PDB at E < 1. Screening every
hit with E < 1 for nucleic-acid-related keywords (dna, rna, nucleic, nucleosome,
chromatin, polymerase, ribosom, helicase, repressor, transcription, histone,
topoisomerase, nuclease, telomer, spliceosom, trna, rrna) returned **NONE** for all
three queries.

## Table 10. Structure-based classification: NOL4 vs a matched true-HTH control

Query: `interpro/api/entry/all/protein/uniprot/{acc}` (all member databases).

| Member database | C. elegans mbr-1 (G5EGQ5, Mblk-1 family) | NOL4 (O94818) |
|---|---|---|
| cathgene3d | **G3DSA:1.10.10.60 Homeodomain-like** | *(no match)* |
| ssf (SUPERFAMILY/SCOP) | **SSF46689 Homeodomain-like** | *(no match)* |
| profile (PROSITE) | **PS50960 Psq-type HTH domain profile** | *(no match)* |
| smart | *(no match)* | *(no match)* |
| cdd | *(no match)* | *(no match)* |
| pfam | PF05225 helix-turn-helix, Psq domain | PF23079, PF38089, PF47726 |
| interpro | IPR007889 **DNA binding HTH domain, Psq-type**; IPR009057 Homeodomain-like superfamily | IPR056549 Nucleolar protein 4, helical domain; IPR039788 NOL4 family |
| panther | PTHR21545 Ligand-Dependent Nuclear Receptor Corepressor-like | PTHR12449 |

CATH-Gene3D and SUPERFAMILY are HMM libraries built on CATH and SCOP structural
superfamilies and both explicitly model the homeodomain-like/HTH fold. Neither
assigns anything anywhere in NOL4's 638 residues.

## Table 11. InterPro entry-level comparison

| Property | IPR007889 (true Psq HTH) | IPR056549 ("HTH_NOL4") |
|---|---|---|
| Full name | DNA binding HTH domain, Psq-type | Nucleolar protein 4, helical domain |
| Short name | HTH_Psq | HTH_NOL4 |
| Type | domain | domain |
| Overlaps with | IPR009057 (Homeodomain-like superfamily) | **[] (none)** |
| Relations | [] | **[] (none)** |
| **GO terms attached** | **GO:0003677 DNA binding** | **none** |
| Description | - | "predicted to form an alpha-helical bundle" |

For reference, IPR009057 Homeodomain-like superfamily overlaps IPR001356, IPR008422,
IPR007889, IPR001005, IPR007526, IPR001647, IPR000281 and IPR003012. IPR056549 is
not among them.

## Table 12. Identification of NOL4's partners Mlr1 and Mlr2

| UniProt | Gene + synonyms | Alternative names | DNA-binding GO |
|---|---|---|---|
| Q3U285 (mouse) | Lcorl, **Mlr1** | "Mblk1-related protein 1", "Transcription factor MLR1" | GO:0003677 (IEA) |
| Q6ZPI3 (mouse) | Lcor, Kiaa1795, **Mlr2** | "Mblk1-related protein 2" | GO:0003677 (IEA) |
| Q96JN0 (human) | LCOR, C10orf12, KIAA1795, **MLR2** | "Mblk1-related protein 2" | GO:0003677 (IEA) |
| Q8N3X6 (human) | LCORL | - | GO:0003677 (IEA) |

Inventory of Psq-HTH (Pfam PF05225) proteins by organism:
- Human: 8 UniProt entries, **all LCOR or LCORL** isoforms.
- Mouse: 4 UniProt entries, **all Lcor or Lcorl**.

So the two mouse Mblk-1 homologs Mlr1 and Mlr2 of PMID 25366156 are Lcorl and Lcor,
and they are the only Psq-HTH proteins in either genome. The DNA-binding HTH in the
NOL4 complex belongs to the partner.

## Table 13. Ortholog curation conflict

| Entry | GO annotations | Keywords |
|---|---|---|
| Human NOL4 (O94818) | GO:0005654 nucleoplasm IDA (HPA); GO:0005730 nucleolus IEA; GO:0005730 nucleolus TAS PMID:9813152; **GO:0003723 RNA binding TAS PMID:9813152 (PINC)** | Alternative splicing, Nucleus, Proteomics identification, Reference proteome |
| Mouse Nol4 (P60954, 483 aa) | **GO:0003674 molecular_function ND** (GO_REF:0000015, MGI); **GO:0008150 biological_process ND** (MGI); GO:0005654 nucleoplasm ISO; GO:0005730 nucleolus IEA | Alternative splicing, Nucleus, Reference proteome |
| Human NOL4L (Q96MY1) | GO:0005654 nucleoplasm IDA; GO:0005515 protein binding IPI x2 (IntAct) | - |

MGI reviewed mouse Nol4 and recorded **ND, "no biological data available"**, for
molecular function. No member of the family other than human NOL4 carries any
nucleic-acid-binding term. Human GO:0003723 is a species-restricted legacy entry.

## Summary of the discriminating evidence

| Evidence line | Verdict on "HTH_NOL4 is a sequence-specific DNA-binding HTH" |
|---|---|
| AlphaFold fold (pLDDT 87.2, 4 helices, no strands) | consistent with alpha-helical bundle, not HTH |
| Foldseek vs PDB100 (domain, full length, N-term) | no relative at E < 1; refutes |
| Calibrated HTH geometry (4/4 true vs 0/3 bundles vs 0 NOL4) | refutes |
| CATH-Gene3D / SUPERFAMILY / PROSITE | no assignment; refutes |
| InterPro name, description and GO attachment | refutes |
| Electrostatic positive patch | ambiguous, does not discriminate |
| Vertebrate conservation of basic residues | ambiguous, patch not more conserved than domain (p = 0.45) |
| Ueki 1998 deletion mapping (PMID 9813152) | basic patch = nucleolar targeting signal; competing explanation |
| Takayanagi-Kiya 2014 (PMID 25366156) | NOL4 is a cofactor of HTH-containing LCOR/LCORL; competing explanation |
| Mouse MGI ND annotations | no molecular function known; qualifies |
