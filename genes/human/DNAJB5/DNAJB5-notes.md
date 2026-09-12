# DNAJB5 (Hsc40 / HSC40) research notes

UniProt: O75953. 348 aa. DnaJ homolog subfamily B member 5; "heat shock protein cognate 40".
J-domain residues 4-68. Paralog of DNAJB1/DNAJB4. Poorly characterized.

## What is established
- Class B cytosolic J-protein (HSP40). No UniProt FUNCTION line — function inferred from family.
- HSP70 co-chaperone binding: GOA GO:0051087 IPI to HSPA1A/HSPA1B (P0DMV8/P0DMV9, P17066) from
  PMID:21231916 (Hageman et al., mammalian HSP70 machine study). This is the most direct MF evidence.
- Cytosol: IDA GO:0005829 PMID:21231916; IBA cytosol.
- Stress-inducible: [UniProt INDUCTION "Expressed under normal conditions, its expression can further
  be increased after various stress treatments."] Cloning paper PMID:10570961 (Hsc40) — IEP response
  to unfolded protein. Tissue enhanced in skeletal muscle/tongue (HPA).

## Protein-binding IPIs (all high-throughput, uninformative)
- PMID:18457437 EBNA-LP (Q8AZK7) — Epstein-Barr viral nuclear antigen interactome (xeno).
- PMID:21078624 CACNA1A (O00555) — expanded ataxia interactome.
- PMID:22810586 EBNA-LP again — cancer/host network perturbation.
- PMID:23414517 TTN/titin (Q8WZ42) — human skeletal muscle interactome.
None inform core chaperone function; KEEP_AS_NON_CORE (records real interactions).
Note titin interaction + skeletal-muscle enrichment is suggestive of a muscle role akin to DNAJB4/DNAJB6
but not functionally demonstrated.

## Likely over-annotation
- GO:0000122 negative regulation of transcription by Pol II — IEA:Ensembl (DR line only; not in GOA TSV
  as a reviewable row beyond Ensembl). Same family-transfer artifact as DNAJB4. (Not present as separate
  stub row; the GOA TSV does not include a 0000122 row for DNAJB5, so no annotation to review.)

## MF/BP assignment
- Core MF: GO:0051087 protein-folding chaperone binding (binds HSP70). Also GO:0051082 unfolded protein
  binding (IBA, DR line) is plausible holdase/client-binding.
- GO:0006457 protein folding: KEEP_AS_NON_CORE (downstream, co-chaperone not foldase).
- No experimental ATPase-stimulation data for DNAJB5 itself, so do NOT assert GO:0001671 as core.
