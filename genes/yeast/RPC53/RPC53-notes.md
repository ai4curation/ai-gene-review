# RPC53 (YDL150W, P25441) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: RPC53 is the SGD seed (S000002309) of PAINT node PTN000334172
(PTHR13408, Eukaryota), from which Neurospora NCU01245 (Q1K6K5, same subfamily
PTHR13408:SF0) inherits its IBA annotations. This review is meant to say
precisely which functions are experimentally established in S. cerevisiae.
ProtNLM2 output was not consulted.

### Deep research

`just deep-research-falcon yeast RPC53 --fallback perplexity-lite` failed:
falcon raised "Failed to authenticate" (Edison client) and the perplexity-lite
fallback returned HTTP 401 insufficient_quota. No deep-research file exists; the
review is built from cached primary literature and the UniProt record.

### Evolutionary grounding

- PANTHER: P25441 and human POLR3D (P05423) are both in PTHR13408:SF0
  ("DNA-DIRECTED RNA POLYMERASE III SUBUNIT RPC4"), per
  `interpro/panther/PTHR13408/PTHR13408-entries.csv`.
- PAINT (`interpro/panther/PTHR13408/PTHR13408-paint.tsv`): PTN000334172
  (taxon:2759) carries only two IBDs: GO:0005666 RNA polymerase III complex
  (seeds SGD:S000002309, UniProtKB:P05423) and GO:0042797 tRNA transcription by
  RNA polymerase III (seed SGD:S000002309). The yeast-specific experimental
  terms termination (GO:0006386), initiation (GO:0006384) and contributes_to
  DNA-directed RNA polymerase activity (GO:0003899) were NOT propagated. Treat
  that as a deliberate PAINT decision: those finer terms are experimentally
  established in yeast only.
- UniProt: "Belongs to the eukaryotic RPC4/POLR3D RNA polymerase subunit family."
  The conserved part is the C-terminal ~136 aa (similar to human BN51/POLR3D,
  [PMID:1406624 "The carboxy-terminal 136 amino acids of C53 are significantly
  similar (25% identical amino acid residues) to the same region of the human
  BN51 protein"]). That region is the heterodimerization domain that binds C37.

### What is experimentally established in yeast

1. Stable, specific Pol III subunit. It co-immunopurifies with Pol III
   [PMID:3905793 "C160, C128, C82, C53, C40, C37, C34, C31, C27, C25, C23, C19,
   C14.5, C12.5, and C10"]. Cryo-EM places it on Pol III: [PMID:26605533 "C53 is
   located below the lobe and extension 2 and its C-terminal dimerization domain is
   indeed tightly associated with the C37 dimerization domain"]. The N-terminal
   ~270 residues are flexible; crosslinks place parts of the N-terminus in the
   cleft and funnel.
2. Essential gene. Temperature-sensitive alleles quickly block tRNA synthesis
   [PMID:1406624 "Temperature-sensitive rpc53 mutants were generated and showed a
   rapid inhibition of tRNA synthesis after transfer to the restrictive
   temperature"]. The G1 arrest is a downstream organismal phenotype, so I do not
   annotate a cell-cycle process.
3. Termination. Pol III lacking C11/C37/C53 (Pol IIIΔ) fails to recognise the
   terminator. Adding back recombinant C37–C53 restores it
   [PMID:16362040 "The specific requirement for the C37-C53 complex in terminator
   recognition was determined"]. The complex also slows elongation.
4. Reinitiation (facilitated recycling). This needs C37–C53 together with C11
   [PMID:16362040].
5. Promoter opening / open complex formation [PMID:19940126 "the C53/C37
   subcomplex additionally plays a role in formation of the initiation-ready open
   promoter complex"]. Photo-crosslinking puts a segment of C53 next to the RNA 3'
   end and the template strand at the active centre.
6. In vitro, anti-C53 antibodies inhibit specific tRNA gene transcription but
   inhibit nonspecific transcription much less [PMID:3905793]. So C53 is not part
   of the catalytic core: Pol IIIΔ still elongates, and does so with higher
   processivity. The polymerase activity belongs to the assembled enzyme, and
   C53 contributes to it only as a subunit.
7. Interacts with C37 (RPC37/P36121) in Y2H, TAP-MS and structural interactome
   data, and in the structure as the C53/C37 heterodimer (TFIIF-like dimerization
   module, related to Pol I A49/A34).

### What is inferred (not tested in yeast)

- DNA binding (IEA, InterPro IPR007811). There is no assay of C53 binding DNA on
  its own; there is only crosslinking proximity to template DNA inside the
  elongation complex. Over-annotation.
- Nuclear/nucleoplasmic localisation follows from Pol III membership.
  UniProt cites a localisation study (PMID:14562095, GFP survey) that is not cached.

### Decisions summary

- Accept complex membership, transcription by Pol III, tRNA transcription,
  termination, and initiation (reinitiation plus promoter opening).
- Accept contributes_to DNA-directed RNA polymerase activity. This is the
  conventional subunit contribution, respecting the qualifier.
- protein binding (3 rows, RPC37): REMOVE as uninformative under the
  protein-binding policy. The real interaction is captured by complex membership
  and by the heterodimer described in the core function.
- nucleus → MODIFY to nucleoplasm (the gene also carries nucleoplasm TAS).
- DNA binding IEA → MARK_AS_OVER_ANNOTATED.
- No NEW terms. There is no Pol III-specific open-complex-formation term.
  GO:0001112 (generic) is part_of GO:0006352, and the accepted GO:0006384 already
  covers this role. I raised the gap as a suggested question.
