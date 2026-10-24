# NCU01245 evidence notes

NCU01245 is the conserved RPC4/C53 subunit of nuclear RNA polymerase III. It associates with the C37 subunit and supports promoter opening, transcription termination and polymerase recycling during synthesis of tRNAs and other polymerase III RNAs. Its role is structural and regulatory within the enzyme complex.

## Identity and provenance

The exact current accession is Q1K6K5; NCU01245 is retained as the current locus identifier. No independently established formal gene-symbol replacement was found. Original claims are preserved in NCU01245-protnlm-source.json from the live API snapshot retrieved 2026-09-09T03:00:51.831347+00:00. The current sequence is not proven to be the prediction-time input, and placeholder API dates do not establish release or training membership.

## Primary evidence and justified transfer

- [PMID:16362040] "The specific requirement for
the C37-C53 complex in terminator recognition was determined."
- [PMID:19940126] "Protein-RNA and protein-DNA photochemical cross-linking analysis places
a segment of C53 close to the RNA 3' end and transcribed DNA strand at the
catalytic center of the pol III elongation complex."

The specific domain/family observation used is `DR   InterPro; IPR007811; RPC4.`. Family membership and characterized relatives establish the inference; ARBA or AI-generated names are not independent functional evidence. PAINT is a curator-reviewed ancestral assertion, not donor-count evidence.

## Unresolved assertions

No unresolved GOA assertion remains at the reviewed level of specificity. Experimental observations on relatives are distinguished from target observations.

## Falcon report appraisal

The actual Falcon report was inspected. It agrees with the RPC4/C53-C37 module and distinguishes RPC4 from the Rpb4-like C17 subunit. Its indirect termination and recycling model agrees with the primary reconstitution and crosslinking papers used here (PMID:16362040; PMID:19940126). Gene-specific Neurospora phenotypes and direct autonomous polymerase or nuclease catalysis are not inferred. References that foreground mutations in the partner C37 subunit are not used as direct RPC4 mutant experiments.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: all six GOA rows, description and core function re-examined against the cached primary papers, the PANTHER/PAINT data for PTHR13408, and the UniProt family/domain cross-references. No ProtNLM2 file was opened or used.

### Identity
- Q1K6K5 is the full-length NCU01245 product (516 aa, unreviewed TrEMBL, PE 4), not a fragment or isoform. The conserved RPC4 domain (Pfam PF05132) maps to residues 345-494 (InterPro API, fetched 2026-10-21) and the C-terminus runs past it. Residues 1-142 are a MobiDB-lite disordered, low-complexity/basic region; fungal RPC4 proteins typically carry such N-terminal extensions (yeast RPC53 422 aa, human POLR3D 398 aa).
- PANTHER PTHR13408:SF0 (DNA-DIRECTED RNA POLYMERASE III SUBUNIT RPC4) contains NCU01245, S. cerevisiae RPC53 (P25441) and human POLR3D (P05423) (`interpro/panther/PTHR13408/PTHR13408-entries.csv`). The family has one RPC4 subfamily relevant here; no conflicting placement.

### Evolutionary grounding
- PAINT node PTN000334172 (taxon:2759) carries IBD for GO:0005666 (seeds SGD:S000002309 = RPC53, UniProtKB:P05423) and GO:0042797 (seed RPC53) only (`PTHR13408-paint.tsv`).
- Yeast RPC53 in QuickGO (queried 2026-10-21) additionally has IDA for GO:0006384 (Pol III transcription initiation), GO:0006386 (Pol III termination), GO:0006383, and contributes_to GO:0003899. PAINT did not propagate these; I treat that as a deliberate curator choice and add no NEW rows. Raised as a suggested question.
- DNA binding on yeast RPC53 is itself only InterPro2GO IEA.

### Decisions
- GO:0003677 DNA binding (IEA): ACCEPT -> KEEP_AS_NON_CORE. The C53 cross-link to the template strand [PMID:19940126 "Protein-RNA and protein-DNA photochemical cross-linking analysis places a segment of C53 close to the RNA 3' end and transcribed DNA strand"] shows proximity inside the elongation complex, not an autonomous binding activity.
- GO:0005666 (IBA, IEA), GO:0042797 (IBA), GO:0006383 (IEA): ACCEPT; reasons rewritten to cite subfamily membership and the PAINT node. [PMID:16362040 "The specific requirement for the C37-C53 complex in terminator recognition was determined."] [PMID:16362040 "Pol III purified from this strain lacked the C37 subunit in addition to C11 and C53"] (S. cerevisiae, per the paper's keywords).
- GO:0005634 nucleus (IEA, ARBA-derived SubCell): ACCEPT, grounded in pol III membership, not in the ARBA line.
- Description and core function rewritten to state orthology (C53/POLR3D), domain layout and the initiation/termination/reinitiation roles; reference_review added for all non-GO_REF references.

### Relative and context
- Closest characterised relative by phylogenetic placement: S. cerevisiae RPC53 (P25441), the PAINT seed in the same SF0 subfamily. No review exists in genes/ (neither yeast RPC53 nor human POLR3D).
- PANTHER family review `interpro/panther/PTHR13408/PTHR13408-review.yaml` agrees (SF0, RPC4, noncatalytic); no subfamily disagreement.
- No module contains this gene; `modules/dmel_nuclear_rna_polymerases.yaml` covers the Drosophila ortholog Polr3D (pol III subunit context only).
