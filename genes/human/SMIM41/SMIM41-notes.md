# SMIM41 notes

## 2026-10-03 - initial review (MICROPROTEINS Tier 2)

### Identity
- UniProt A0A2R8YCJ5 (SIM41_HUMAN), 93 aa, PE1 (proteomics identification). HGNC:54075, chr 12q13.13.
  NCBI GeneID 113523638, no aliases.
- Single predicted helical TM segment, residues 38-58 [file:human/SMIM41/SMIM41-uniprot.txt "FT   TRANSMEM        38..58"];
  C-terminal disordered region 71-93 [file:human/SMIM41/SMIM41-uniprot.txt "FT   REGION          71..93"].
  Membrane location by sequence prediction only (ECO:0000255).
- Own sequence inspection: N-x-S sequon at N2 (MNGS), Ala/Ser/Pro-rich N-terminal segment, Gly-rich TM helix
  (LGVLSLLVLCGVLFLGGGLLL), acidic C-terminal tail ending EDGDDDS. Not tested experimentally.
- Locus (Ensembl REST overlap 12:52079704-52108255): SMIM41 (+ strand) overlaps an antisense lncRNA (SMIM41-AS1)
  and the transcribed pseudogene OR7E47P.

### Family / conservation
- Reprimo family: InterPro IPR043383 Reprimo_fam and IPR060618 Reprimo-like_TM, Pfam PF27763, PANTHER PTHR28649
  "PROTEIN REPRIMO-RELATED", subfamily SF1 "SMALL INTEGRAL MEMBRANE PROTEIN 41"
  [file:human/SMIM41/SMIM41-uniprot.txt "DR   PANTHER; PTHR28649; PROTEIN REPRIMO-RELATED; 1."].
  Other subfamilies (interpro/panther/panther.obo): SF2 PROTEIN REPRIMO (RPRM), SF3 REPRIMO-LIKE PROTEIN (RPRML),
  SF5 "REPRIMO, TP53-DEPENDENT G2 ARREST MEDIATOR HOMOLOG 3".
- RPRM's own UniProt function is weak (by similarity: p53-dependent G2 arrest); RPRML has no function line
  (UniProt REST query 2026-10-03). Family membership does not transfer a cell-cycle role to SMIM41: SMIM41 sits
  in a separate PANTHER subfamily and no study links it to p53.
- Ensembl Compara: 0 orthologues and 0 paralogues for ENSG00000284791 (gene too recently annotated / not in a gene tree;
  no GeneTree line in UniProt). However, UniProt gene-name search (gene_exact:SMIM41) finds SMIM41 entries in many
  placental mammals - mouse (A0A2I3BPF5, Q3UYR0), rat, primates, carnivores, cetaceans, bats, aardvark, tenrec.
  So it is a placental-mammal gene. PAN-GO 0 IBA.

### Expression
- HPA "Tissue enhanced (lung, prostate)" [file:human/SMIM41/SMIM41-uniprot.txt "DR   HPA; ENSG00000284791; Tissue enhanced (lung, prostate)."]; Bgee top: right lung.

### Literature
- PubMed esearch "SMIM41" (2026-10-03): 0 hits. NCBI Gene-linked PMID: 12477932 (MGC full-length cDNA collection) only.

### Conclusion
- No functional literature. IEA membrane: ACCEPT. core_functions empty. No NEW terms. Not in gocams/index.tsv.
