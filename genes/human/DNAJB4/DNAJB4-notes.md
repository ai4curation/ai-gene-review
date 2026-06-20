# DNAJB4 (HLJ1 / DNAJW) research notes

UniProt: Q9UDY4. 337 aa. DnaJ homolog subfamily B member 4. Cytosolic HSP40/J-protein,
paralog of DNAJB1. J-domain at residues 2-70.

## Core function: HSP70 co-chaperone (class B J-protein)
- UniProt FUNCTION: "Probable chaperone. Stimulates ATP hydrolysis and the folding of unfolded
  proteins mediated by HSPA1A/B (in vitro) (PubMed:24318877)."
- [PMID:36264506 "DNAJ/HSP40 co-chaperones are integral to the chaperone network, bind client
  proteins and recruit them to HSP70 for folding."]
- [PMID:36264506 "DNAJB chaperones recognize misfolded client proteins and recruit HSP70 proteins.
  The DNAJB-client complex stimulates HSP70 ATP hydrolysis which then facilities the refolding of
  the client"]
- GOA: GO:0001671 ATPase activator activity IDA PMID:24318877 — the experimentally supported core MF
  (stimulates HSP70 ATP hydrolysis).
- GOA: GO:0051087 protein-folding chaperone binding IPI to HSPA1A/HSPA1B (P0DMV8/P0DMV9, P17066) —
  binds HSP70.

## Localization
- Cytosol: UniProt "Cytoplasm" (PMID:18837411); HPA IDA cytosol; GOA cytosol IDA PMID:21231916.
- Z disc / sarcomere: [PMID:36264506 "DNAJB4 normally localizes to the Z-disc and was absent from
  muscle and fibroblasts of affected patients"] — IDA PMID:36264506 GO:0030018 Z disc. Genuine.
- Plasma membrane / cell membrane: from OPRM1 (mu opioid receptor) C-tail interaction
  (PMID:16542645, yeast two-hybrid + in vitro). Membrane association is indirect (via client).
- Nucleoplasm: HPA IDA only; weak, not central.

## Disease: chaperonopathy / myopathy
- [PMID:36264506 "Loss of function variants in DNAJB4 cause a myopathy with early respiratory failure"]
- [PMID:36264506 "DNAJB4 knockout muscle and myotubes had myofibrillar disorganization and
  accumulated Z-disc proteins and protein chaperones."] — implies role in myofibril/Z-disc maintenance.
- R25Q variant: loss of function in chaperone-mediated protein folding (UniProt VARIANT note).

## Interactions (high-throughput / specific)
- OPRM1 C-tail (PMID:16542645) — specific Y2H+in vitro.
- SDIM1 (PMID:21255413).
- HTT (P42858), ATXN1 (P54253), RUVBL2 (Q9Y230) — IntAct; aggregation-prone clients / HT.
  GO:0005515 protein binding IPI PMID:32296183 (RUVBL2), PMID:32814053 (HTT, ATXN1). These are
  consistent with handling aggregation-prone clients but are bare protein-binding HT calls.

## Likely over-annotation
- GO:0000122 negative regulation of transcription by RNA polymerase II IBA (from PANTHER
  PTN008393908 / UniProtKB:P25685 = yeast Sis1/DnaJ family). No direct evidence DNAJB4 regulates
  pol II transcription in human; transferred phylogenetically. MARK_AS_OVER_ANNOTATED.

## MF/BP assignment summary
- Core MF: GO:0001671 ATPase activator activity (HSP70 ATPase stimulation), GO:0051087 chaperone binding.
- GO:0051082 unfolded protein binding (IBA, in DR line) — plausible client-binding holdase function.
- GO:0006457 protein folding: downstream BP, KEEP_AS_NON_CORE (co-chaperone assists HSP70, not foldase).
