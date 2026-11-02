# SHLD2: paired human–horse review notes

## Biological evidence

The important distinction is shieldin-family identity versus an intact DNA-end-protection module. Human SHLD2 has experimentally distinct long/short splice products; a short product can still recruit to damage sites and assemble with shieldin while failing to suppress homologous recombination.

- [PMID:30022168: The shieldin complex mediates 53BP1-dependent DNA repair.](https://pubmed.ncbi.nlm.nih.gov/30022168/) — full text cached.
- [PMID:29789392: FAM35A associates with REV7 and modulates DNA damage responses of normal and BRCA1-defective cells.](https://pubmed.ncbi.nlm.nih.gov/29789392/) — full text cached.
- [PMID:29656893: DNA Repair Network Analysis Reveals Shieldin as a Key Regulator of NHEJ and PARP Inhibitor Sensitivity.](https://pubmed.ncbi.nlm.nih.gov/29656893/) — full text cached.

## Exact horse model

The 883-residue horse model retains the insertion absent from human canonical SHLD2, but its distal OB-domain region is divergent/gapped in the long-isoform alignment. Nuclear and damage-site recruitment are plausible; the complete NHEJ/resection-suppression mechanism is UNC for the exact model. Human Protein Atlas XML supports an additional human actin-associated pool, so the actin prediction is unresolved in horse rather than refuted as incompatible with nuclear localization.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/SHLD2/SHLD2-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Obtain a transcript-supported horse C terminus and inspect the OB folds. Distinguish long/short human isoforms in any assay transfer. Inspect the HPA antibody/cell-line context before transferring secondary actin localization.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined every GOA row, the description and core functions against the cached full texts
(PMID:30022168, PMID:29789392), the partial Gupta et al. text (PMID:29656893), the ASTE1 abstract
(PMID:34354233), the UniProt record and the PTHR14495 PAINT data. ProtNLM2 output was not consulted.

### Identity of the benchmark accession
- Q86V20 is the reviewed, canonical UniProt entry for human SHLD2, so this folder is keyed to the right
  gene. It is not a fragment or an alternative gene model.
- Caveat: the UniProt *displayed* sequence (Q86V20-1, 835 aa) is the SHORT splice form. Q86V20-2
  (904 aa, VSP_016165, 69-residue insertion after K654) is the LONG form. Tomida et al. name them in the
  reverse order: "Isoforms 1 and 2 are the most common, encoding 904 and 835 amino acid proteins,
  respectively" and "One exon is absent in isoform 2 compared to isoform 1, deleting 69 aa from OB domain B"
  [PMID:29789392].
- The biochemistry and rescue work use the long form. SHLD2C is residues 421-904 [PMID:30022168], and
  the NHEJ rescue uses "FAM35A isoform 1" [PMID:29789392]. Noordermeer's SHLD2S is "a splice variant of
  SHLD2 that disrupts OBB" cloned from the ORFeome "short isoform". It is almost certainly the 835-aa
  UniProt displayed sequence. I infer this; the paper does not give the length. SHLD2S still localises to
  DSBs and assembles with shieldin, but "the SHLD2-m1 and SHLD2S mutants are defective in suppressing HR"
  and SHLD2C-S "displayed reduced and aberrant ssDNA-binding behaviour" [PMID:30022168].
- The gene-level annotations rest on the long form. Any sequence-based predictor fed the canonical
  835-aa sequence sees a form with a disrupted OB fold B.

### Evolutionary grounding
- PANTHER PTHR14495 has a single subfamily, SF2 "SHIELDIN COMPLEX SUBUNIT 2". Human, mouse (Q3UEN2) and
  horse SHLD2 all sit in SF2.
- PAINT node PTN001025652 (taxon 6072, Eumetazoa) is seeded only by human SHLD2. It carries nucleus,
  site of DSB and *regulation of* DSB repair via HR. The curator did not propagate NHEJ promotion, isotype
  switching or ssDNA binding. I read that as a deliberate choice: it matters for transfers to other
  species, not for the human rows, which rest on human experiments.
- The PTHR14495 family review (interpro/panther/PTHR14495/PTHR14495-review.yaml) has the same subfamily
  placement (SF2) and no disagreement. Its summary does not mention ssDNA binding; that could be added at
  family level.

### Changes from the previous review
- NEW GO:0003697 single-stranded DNA binding (IDA, PMID:30022168): "We estimate the binding affinity of
  the SHLD2C-ssDNA interaction to be ~10 nM ... We conclude that SHLD2 possesses ssDNA-binding activity."
  This is now the first core MF. The adaptor (scaffold) activity is kept as a second core function.
- GO:0005515 rows now follow the protein-binding policy. SHLD1, SHLD3 and REV7 (both papers) → MODIFY
  to GO:0030674 protein-macromolecule adaptor activity, on the basis of the N-terminal SHLD3-REV7 and
  C-terminal SHLD1 mapping. TP53BP1, RIF1 and ASTE1 → REMOVE (uninformative; the interactions are not
  disputed).
- chromosome (IDA and IEA) → MODIFY to site of double-strand break (part_of chromosome; already on the gene).
- somatic diversification of immunoglobulins (NAS) → MODIFY to GO:0045190 isotype switching. The term
  note on GO:0045190 asks for gene products in the recombination mechanism, which fits shieldin's end joining.
- IBA regulation of HR → MODIFY to negative regulation (GO:2000042), unchanged from before.
- Telomere maintenance in response to DNA damage stays KEEP_AS_NON_CORE, with the caveat that the readout
  is NHEJ fusion of deprotected telomeres.
- Removed the triplicated supporting_text anchors on the NHEJ rows and gave each row its own support.

### Relative for next review
- Mouse Shld2, UniProtKB:Q3UEN2 (reviewed, 891 aa, PTHR14495:SF2). It is the 1:1 ortholog in the same
  PANTHER subfamily, and is characterised in mouse cells and B cells for CSR and PARPi responses.
  There is no review in the repo (no genes/mouse/Shld2).

### Modules
- No module under modules/ covers shieldin or 53BP1-dependent DSB repair pathway choice. The only grep
  hits ("shielding" in viral_factory.yaml) are unrelated.
