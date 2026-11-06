# hldE curation notes

- Q88D93 is a bifunctional HldE whose kinase domain forms
  D-glycero-beta-D-manno-heptose 1,7-bisphosphate and whose
  adenylyltransferase domain forms ADP-D-glycero-beta-D-manno-heptose
  [file:PSEPK/hldE/hldE-uniprot.txt, "yielding
  ADP-D-glycero-beta-D-manno-heptose"].
- The target-genome analysis found no credible HldD/GmhD ortholog by KEGG,
  UniProt/UniRef, RefSeq, or genome-level similarity search
  [file:projects/P_PUTIDA/deep-research/PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist.md,
  "is a genome-confirmed GAP in KT2440"]. No broad NAD-dependent epimerase is
  assigned to fill this step.
- GO:0097171 names the downstream ADP-L,D-heptose endpoint and remains
  `UNDECIDED`. GO has no process term for the directly produced ADP-D,D-heptose
  endpoint, so a new child of GO:0009226 is proposed without inventing an id.

## 2026-10-25 source-specific annotation audit

All 11 seeded annotations were reviewed individually. Both exact catalytic activities are accepted by curated HldE-specific domain/rule evidence with E. coli primary homolog support, not a KT2440 biochemical assay.

- The reaction order is HldE kinase → GmhB phosphatase → HldE adenylyltransferase. It is essential to retain the intervening C-7 dephosphorylation, since HldE's second domain consumes heptose 1-phosphate, not the bisphosphate kinase product.
- [PMID:11751812, "Synthetic d -β- d -heptose 1-phosphate was incubated with the RfaE protein and ATP, resulting in a peak comigrating with synthetic ADP- d -β- d -heptose"] supports the E. coli reaction. The tested proteins are E. coli and, in some coupled mixtures, A. thermoaerophilus; Q88D93 was not assayed in this study.
- The adenylyltransferase transfers **AMP**, not ADP, from ATP to the phosphate-bearing sugar, releasing pyrophosphate. The previous review and UniProt CC:FUNCTION phrase "ADP transfer" were chemically misleading. The review now quotes the correct curated CC:CATALYTIC ACTIVITY equation. Immutable UniProt source text was preserved.
- Kinase, alcohol-acceptor phosphotransferase, nucleotidyltransferase and broad catalytic/transferase rows are MODIFY to the appropriate one or both existing exact activities. ATP binding is accepted as core cosubstrate recognition. Carbohydrate metabolism is refined to nucleotide-sugar biosynthesis without imposing terminal stereochemistry.
- Cytosol was UNDECIDED in this round and is now ACCEPT (see the 2026-11-02 entry): TreeGrafter supplies the original annotation and no independent target localization statement was found, but the PAINT node the graft descends from is seeded by E. coli HldE's own IDA cytosol rows. Purified soluble E. coli HldE is compatible with the inference but still does not directly localize native Q88D93.
- GO:0097171 was UNDECIDED in this round and is now MODIFY to the proposed ADP-D,D-heptose term (see the 2026-11-02 entry); the adenylyltransferase makes ADP-D,D-heptose, and terminal C-6 epimerization is separate. The proposed term for ADP-D,D-heptose biosynthesis is retained with reaction-level support and no invented GO identifier, and is now the row's replacement target.
- Falcon research was attempted with perplexity-lite fallback: Falcon authentication failed (403); Perplexity returned 401 insufficient_quota. Logs: `/tmp/adp-hldE-deep.log`. No provider report was fabricated; this section records manual primary-literature work.

### Row ledger

1. GO:0003824 IEA — MODIFY: HldE has two specific catalytic activities.
2. GO:0005524 IEA — ACCEPT: ATP is a cosubstrate for both HldE reactions.
3. GO:0005829 IEA — ACCEPT: Cytosol is the compartment the core activity operates in, inherited from an experimentally seeded PAINT node.
4. GO:0005975 IEA — MODIFY: HldE directly catalyzes nucleotide-sugar biosynthesis.
5. GO:0016301 IEA — MODIFY: The N-terminal HldE domain is a heptose 7-phosphate kinase.
6. GO:0016772 IEA — MODIFY: Both HldE domains transfer phosphorus-containing groups.
7. GO:0016773 IEA — MODIFY: The kinase transfers phosphate to the C-1 hydroxyl of heptose 7-phosphate.
8. GO:0016779 IEA — MODIFY: The C-terminal HldE domain is an adenylyltransferase.
9. GO:0033785 IEA — ACCEPT: HldE phosphorylates beta-heptose 7-phosphate at C-1.
10. GO:0033786 IEA — ACCEPT: HldE activates heptose 1-phosphate to form ADP-D,D-heptose.
11. GO:0097171 IEA — MODIFY (NTR ADP-D-glycero-beta-D-manno-heptose biosynthetic process): KT2440 reaches only the D,D endpoint.

Action counts: 7 MODIFY, 4 ACCEPT, 0 UNDECIDED.

### Evidence and retrieval limits

- The publication cache was populated with `just fetch-gene-pmids` in parallel with research retrieval. Existing UniProt/GOA files were not modified.
- `just fetch-fitness PSEPK hldE` failed: no local FEBA database or BarSeqR tables were available and no remote FEBA source was reachable. No fitness artifact was written and no growth phenotype or essentiality claim is inferred from this failure.
- No NEW annotations were added. All seeded annotation fields and rows were preserved; only review judgments and synthesis were revised. Broad correct metabolic/catalytic terms were refined with MODIFY, not removed or marked false merely because they were broad.
- The generated OpenScientist report's assertion of a genome-confirmed HldD gap was not independently reproduced in this round. It has since been reproduced from two independent directions (see the 2026-11-02 entry), so the L,D endpoint is now treated as not reached in KT2440.

## 2026-11-02 — HldD absence settled; cytosol and GO:0097171 resolved

Follow-up round on the ADP-heptose module. Two rows that this file recorded as
`UNDECIDED` are now decided, on evidence that did not exist when they were written.

**GO:0097171 → MODIFY, replacement NTR "ADP-D-glycero-beta-D-manno-heptose
biosynthetic process".** The open question was whether KT2440 reaches the L,D
endpoint, which needs a C-6 epimerase. It does not, and this is now supported from
two independent committed sources rather than the earlier unresolved assignment:

- PANTHER's member inventory for the HldD family puts KT2440's only `PTHR43103`
  member, the uronate dehydrogenase Q88NN6, in the 4-epimerase subfamily `SF5`,
  while the 161-member heptose 6-epimerase subfamily `SF3` that holds PSEAE hldD
  (Q9HYQ8) and E. coli hldD (P67910) has no KT2440 member at all. KT2440 is itself
  present in that inventory, so this is not a sampling artefact
  [file:interpro/panther/PTHR43103/PTHR43103-entries.csv].
- The project deep-research page reaches the same conclusion from KEGG,
  UniProt/UniRef, RefSeq and genome-level similarity search
  [file:projects/P_PUTIDA/deep-research/PSEPK__adp-heptose-biosynthesis__ppu00541-deep-research-openscientist.md,
  "is a genome-confirmed GAP in KT2440"].

A reproducible UniProt query, with *P. aeruginosa* as a positive control, is
committed at `hldE-bioinformatics/` (script, raw TSV, RESULTS.md) so the negative is
checkable rather than asserted in prose. It returns no `hldD`/`rfaD` gene, no
EC 5.1.3.20 protein, and only a generic NAD-dependent epimerase (Q88HZ6, PP_3206)
on a name-text search, against three positive hits for *P. aeruginosa*.

Because the L,D endpoint is never reached, the `GO_REF:0000041` UniPathway mapping is
false for KT2440 and `REMOVE` would be sanctioned. `MODIFY` is chosen as the more
informative action, since the gene genuinely does make the D,D nucleotide sugar. The
replacement is the NTR already proposed in this review, **not** `GO:0009226`, because
`GO:0009226` is already the replacement for the generic `GO:0005975` row in this file
and using it twice would erase all heptose specificity from the process aspect.

**GO:0005829 cytosol → ACCEPT.** Decided by the new `PTHR46969` family review. The
row is a TreeGrafter assignment whose with/from is the graft node `PTN005327360`,
while the cytosol IBD sits at `PTN000062036`; the descent of the former from the
latter follows from the TreeGrafter mechanism and is the one link not checkable in the
committed PAINT slice, which carries IBD rows but no tree topology. Granting it, the
claim inherits experimental grounding, because `PTN000062036` is seeded by E. coli
HldE itself, whose cytosol rows are IDA against the K-12 fractionation proteome
[PMID:15911532] and the cytosolic abundance proteome [PMID:18304323]. Neither paper
names HldE in the text available here, so they establish the experiments behind those
IDA rows rather than target-specific peptide evidence.

**Limits.** The HldD argument is an annotation-absence argument: it cannot exclude an
unannotated or non-orthologous enzyme performing the C-6 epimerization, and Q88HZ6 is
an uncharacterized epimerase/dehydratase that is not positively ruled out as a
candidate. No assay on KT2440 heptose stereochemistry was examined.
