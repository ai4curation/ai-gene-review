# Klf3 (rat, D4A4V3) review notes

## Session 1 (initial review)
- `just fetch-gene rat Klf3` resolved D4A4V3 (TrEMBL, PE 1 because of large-scale phosphoproteomics); 16 GOA rows.
- No deep-research API was available; literature compiled manually in `Klf3-deep-research-manual.md`.
- Ortholog check (`Klf3-bioinformatics/`): 97.4% identity to mouse Q60980, 100% identical zinc fingers,
  conserved PVDLT CtBP motif and K10/K197 sumoylation sites. ISO/IEA transfers from mouse/human are sound.
- Only rat experimental paper: PMID:18406357 (Cullingford et al. 2008), full text read. Klf3 is mentioned only
  as transiently downregulated by ET-1 in cardiac myocytes (microarray + qPCR, Fig. 1G)
  [PMID:18406357 "Consistent with our microarray data, Klf3, Klf11 and Klf15 were downregulated in response to ET-1."].
  The IEP `cellular response to endothelin` row records a transient mRNA dip; Klf3 protein does none of the work
  of the response. Marked as over-annotated (both IEP and the ARBA IEA row that likely propagates RGD's
  KLF-family IEP annotations). Note rat Klf4 review kept the same term as non-core; Klf4 is an IEG induced
  by ET-1, whereas Klf3 is only transiently decreased - the claim is weaker here.
- Decisions:
  - GO:0000122 negative regulation of transcription by Pol II: ACCEPT (core).
  - GO:0000977 and GO:1990837 (general DNA-binding terms): MODIFY -> GO:0000978 (already carried via IBA).
  - GO:0000981: MODIFY -> GO:0001227 (repressor; already carried via ARBA IEA).
  - GO:0006357: MODIFY -> GO:0000122.
  - nucleus (IBA, IEA) and nucleoplasm: ACCEPT.
- No NEW terms proposed. Erythropoiesis/adipogenesis roles are mouse knockout phenotypes (necessity evidence);
  under the strict NEW bar they are not added for rat.
