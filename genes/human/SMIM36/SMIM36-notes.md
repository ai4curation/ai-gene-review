# SMIM36 notes

## 2026-10-03 - initial review (MICROPROTEINS Tier 2)

### Identity
- UniProt A0A1B0GVT2 (SIM36_HUMAN), 93 aa, PE1 (proteomics identification). HGNC:53654, chr 17q22.
  No aliases in NCBI Gene (GeneID 101927367); gene previously known only by its LOC number.
- Single predicted helical TM segment near the N-terminus, residues 14-34
  [file:human/SMIM36/SMIM36-uniprot.txt "FT   TRANSMEM        14..34"]; C-terminal disordered region 73-93
  [file:human/SMIM36/SMIM36-uniprot.txt "FT   REGION          73..93"]. The C-terminal half is Pro/Gly-rich
  (own sequence inspection). Membrane location is by sequence prediction (ECO:0000255).
- Ensembl: ENSG00000261873, chr17:55449856-55511452 (- strand), ~62 kb locus; only unnamed lncRNAs overlap.

### Family / conservation
- Own family: InterPro IPR063159 SMIM36, Pfam PF30955 [file:human/SMIM36/SMIM36-uniprot.txt "DR   InterPro; IPR063159; SMIM36."]. No PANTHER family; PAN-GO 0 IBA.
- Ensembl Compara (REST homology/id/human/ENSG00000261873, orthologues): 89 species, including teleosts
  (danio_rerio, cyprinodon_variegatus) and reptiles/birds -> conserved across bony vertebrates. No human paralogues listed.

### Expression
- HPA "Group enriched (retina, testis)" [file:human/SMIM36/SMIM36-uniprot.txt "DR   HPA; ENSG00000261873; Group enriched (retina, testis)."]; Bgee top: testis.

### Literature
- PubMed esearch "SMIM36" (2026-10-03): 1 hit, PMID:41153404 (psoriasis anti-IL-17 response GWAS, 88 patients).
  An intronic SNP of SMIM36 is among 21 response-associated variants
  [PMID:41153404 "rs115790464 in TMEM9; rs9914970 in SMIM36"], but the authors' own functional reading assigns it
  to a neighbouring gene: [PMID:41153404 "rs9914970, an intronic variant in SMIM36, has been identified as eQTL for the nearby (~34 Kb) MMD gene in whole blood"].
  Small cohort, needs replication; says nothing about the SMIM36 protein.
- NCBI Gene-linked PMIDs: only the chr17 genome sequencing paper (16625196).

### Conclusion
- No functional literature. IEA membrane: ACCEPT. core_functions empty. No NEW terms. Not in gocams/index.tsv.
- Ensembl Compara spot check (2026-10-03): orthologues in rat, zebrafish, chimpanzee; NONE annotated in mouse
  (mus_musculus) - possible loss or annotation gap; relevant for choosing a model organism.
