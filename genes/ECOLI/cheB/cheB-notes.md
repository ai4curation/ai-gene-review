# cheB (E. coli K-12, P07330) review notes

## 2026-11-03 session

### Sources and attempts
- `just deep-research ECOLI cheB --provider perplexity` failed: provider 'perplexity' not
  available; agentapi not in PATH. No
  deep-research file was produced; review based on cached publications (all abstract-only
  except PMID:16176121, full text) and the UniProt record.
- `just mod-description-deep-research ECOLI cheB`: skipped, no MOD provider configured for ECOLI.
- `just paint-losses ECOLI cheB`: no IRD or IKR loss on this lineage.
- GO term definitions checked in the local GO sqlite (oaklib go.db): GO:1990827, GO:0043424,
  GO:0005102, GO:0009898, GO:0000156; GO:0000160 is_a GO:0035556 is_a GO:0007165;
  GO:0009898 part_of GO:0005886.

### Biology (with provenance)
- CheB is the receptor methylesterase: [PMID:358191 "This enzyme catalyzes the hydrolysis of
  gamma-glutamyl methyl ester residues from membrane-bound 60,000-molecular weight proteins
  that are essential for chemotaxis."] and [PMID:358191 "the methylesterase is a product of the
  cheX gene in Salmonella and the cheB gene in E. coli"].
- Activity is regulated by stimuli: [PMID:392505 "Both methods showed that addition of
  attractants causes a transient inhibition of MCP demethylation."]
- Activation by CheA phosphorylation: [PMID:2188960 "activation of the methylesterase activity
  of CheB involves phosphorylation of CheB by CheA"]; [PMID:3280143 "the phosphate group on CheA
  can be rapidly transferred to CheB, a protein involved in adaptation to stimuli"].
- CheA binding: [PMID:7578071 "CheB bound to CheA1-233 with a KD of 3.2 microM, and also bound
  to intact CheA with the same affinity."]
- Deamidase: [PMID:6304723 "suggests that CheB-dependent modification of MCPI is the enzymatic
  deamidation of glutamine to methyl-accepting glutamic acid"]; [PMID:2033064 "The other two
  sites are glutamines and two methyl-accepting sites are created by two distinct
  deamidations."]
- Receptor docking: [PMID:10485883 "CheB bound specifically to an affinity column carrying the
  isolated pentapeptide, implying that in the intact receptor the pentapeptide serves as a
  docking site for the methylesterase/deamidase"].
- Location: [PMID:334749 "The cheB, cheX, cheZ, and cheA (76,000 daltons) proteins, however,
  were distributed in both the cytoplasm and the inner membrane fractions."]
- Phenotype: [PMID:353036 "cheB or cheZ mutants exhibited very high tumbling rates"].

### Decisions (34 rows)
- MF core: GO:0008984 methylesterase (6 rows ACCEPT), GO:0050568 glutaminase (5 rows ACCEPT),
  GO:0000156 phosphorelay response regulator (2 rows ACCEPT). The module's asserted MF
  (GO:0008984) and the deamidase MF (GO:0050568) are both supported and are core functions.
- GO:0005515 protein binding (4 rows): MODIFY. Tsr/Tar pentapeptide docking (PMID:10485883)
  -> GO:0005102 signaling receptor binding; CheA rows (PMID:7578071, 16176121, 19834901) ->
  GO:0043424 protein histidine kinase binding.
- GO:1990827 deaminase binding (CAFA, PMID:15916610): REMOVE. CheB is the deamidase; the
  term would describe its receptor docking partner. Recorded as a source_defect (WRONG_TERM,
  resource OTHER/CAFA, PROBABLE).
- Cytoplasm (EXP, IEA): MODIFY -> cytosol (GO:0005829, carried by IDA PMID:334749, ACCEPT).
- Plasma membrane (IDA x2): MODIFY -> GO:0009898 cytoplasmic side of plasma membrane (CheB is
  peripheral, no TM; membrane pool reflects receptor docking).
- Signal transduction (4 rows) and intracellular signal transduction (1 row): MODIFY ->
  GO:0000160 phosphorelay signal transduction system (ACCEPTed IEA row).
- Chemotaxis (4 rows), protein demethylation (IMP): ACCEPT.
- PMID:4895809 has no cached abstract; ACCEPTed by deferring to the curator, quoting PMID:353036
  and the UniProt disruption phenotype.
- No NEW rows.
