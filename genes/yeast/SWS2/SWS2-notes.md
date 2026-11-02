# SWS2 (YNL081C, P53937) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: SWS2 is the experimentally characterised S. cerevisiae ortholog used as the
reference for SCHPO/sws2 (O59772). No ProtNLM2 files were opened.

### Deep research
`just deep-research-falcon yeast SWS2 --fallback perplexity-lite` failed: Edison
(falcon) returned `403 Forbidden` on `/auth/login`, and the perplexity-lite fallback
also failed. No deep-research file exists; the review is built from cached
literature, UniProt and PANTHER/PAINT files.

### Evolutionary grounding
- UniProt: PANTHER PTHR10871 (30S RIBOSOMAL PROTEIN S13/40S RIBOSOMAL PROTEIN S18),
  subfamily PTHR10871:SF1 (SMALL RIBOSOMAL SUBUNIT PROTEIN US13M); HAMAP MF_01315.
- PAINT (`interpro/panther/PTHR10871/PTHR10871-paint.tsv`): root node PTN000093238
  carries structural constituent of ribosome and small ribosomal subunit (seeds include
  SGD:S000005025, i.e. this gene); mitochondrial node PTN000093341 carries mitochondrion
  (seeds AT1G77750, SGD:S000005025, Q7S2C2) and a curated NOT cytosol (IRD).
  So the curators deliberately kept the root's cytosol annotation off the uS13m lineage.

### Experimental evidence in S. cerevisiae
- Structure: cryo-EM of the yeast mitoribosome models Sws2 as uS13m (chain MM, residues
  2-121) in the mt-SSU [PMID:28154081 "The mitoribosomal small subunit has been built de
  novo and includes 15S ribosomal RNA (rRNA) and 34 proteins"]. Supplementary table
  (copied to `SWS2-28154081-supplement.txt` from the SCHPO/sws2 folder, original source
  the authors' PDF) lists "uS13m! Sws2! P53937!" and uS13m residues in
  mitochondria-specific intersubunit bridges mB8 (with mL46), mB9/mB10 (with uL5m) and
  mB13 (with 21S rRNA H62). The main text notes bacterial bridges B1a/b (the classical
  uS13 bridge) are absent in yeast mitoribosomes.
- Localization: Ynl081c-GFP in dot-shaped and elongated structures [PMID:10649453];
  UniProt cites this and Huh 2003 for Mitochondrion (ECO:0000269).
- Genetics: high-confidence pet gene and [rho0] on deletion [PMID:32904421 Tables 1, 4];
  slow growth [PMID:10649453]. These are necessity phenotypes typical of mitoribosome
  mutants; mtDNA loss is secondary to translation loss, so no mtDNA-maintenance process
  annotation is proposed.
- Name origin: synthetic sickness with pds1 (securin) in SGA [PMID:15579722 "SWS2 and QRI5
  encode mitochondria-associated proteins of unknown function"]. Genetic interaction
  only; no cell-cycle process annotation is warranted.
- Peroxisome IDA [PMID:36164978]: N-terminal GFP / NOP1pr SWAT screen; Sws2 not in cached
  main text; call is in supplementary data not available. Marked UNDECIDED. The 2026
  peroxisomal proteome paper [PMID:41686312] lists Sws2 as multilocalized based on
  database annotation, so it is not independent.

### Established vs inferred (for transfer to SCHPO/sws2)
- Experimentally established in S. cerevisiae: part of mitochondrial small ribosomal
  subunit (cryo-EM, IDA); structural constituent of ribosome (IDA); mitochondrion
  (GFP); required for respiratory growth and mtDNA retention (deletion screens).
- Inferred: mitochondrial translation (IC, from complex membership); RNA binding
  (InterPro + structural rRNA contacts, no direct assay); mitochondrial inner membrane
  (ComplexPortal NAS, complex-level).
- Not established: any peroxisomal or cell-cycle role.

### Actions summary
ACCEPT: structural constituent of ribosome (IBA/IDA/IEA), mitochondrion (IBA/IEA),
mitochondrial small ribosomal subunit (IDA/NAS), mitochondrial translation (IC x2, NAS).
MODIFY: nucleic acid binding -> RNA binding; ribosome -> mitochondrial small ribosomal
subunit; translation -> mitochondrial translation; small ribosomal subunit (IBA) ->
mitochondrial small ribosomal subunit.
KEEP_AS_NON_CORE: RNA binding; mitochondrial inner membrane (NAS).
UNDECIDED: peroxisome (IDA, PMID:36164978).

## SGD description follow-up: H2O2 relocalisation and sporulation

- Vacuole on H2O2: in a high-throughput single-cell GFP screen of stress responses, Sws2-GFP moved to the vacuole lumen after H2O2, together with other mitoribosomal proteins [PMID:23509072 "Three of the proteins whose localization were altered (Sws2, Mrpl23, and Mrpl11) are components of mitochondrial ribosomes, therefore their elimination would enable a major and rapid down-regulation in mitochondrial proteome production."]. This reads as stress-induced removal of mitoribosomes (probably mitophagy-related turnover), not a vacuolar function, so it is not annotated.
- Sporulation efficiency: the source of the SGD claim was not identified or checked. Respiratory competence is needed for sporulation, so a sporulation defect would be an expected indirect consequence of losing a mitoribosomal protein. Not annotated.
