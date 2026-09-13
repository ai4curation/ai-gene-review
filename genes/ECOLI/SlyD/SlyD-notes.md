# SlyD review notes

## 2026-08-30 refresh and evidence collection

- Refreshed UniProt and GOA through `just fetch-gene ECOLI SlyD --force`. The current
  GOA has 35 physical rows but 32 unique term/evidence/reference signatures because
  several `protein binding` records differ only by WITH/FROM partner. Three prior
  records are absent from current GOA: GO:0016853, GO:0046872, and GO:0051082.
- Falcon deep research timed out after 600 seconds and the configured Perplexity-lite
  fallback failed for quota. The existing Falcon report was retained unchanged and
  the review instead uses the 21 cached publications plus this manual journal.
- All 21 cited PMIDs were successfully checked by `just fetch-gene-pmids ECOLI SlyD`.
  Most caches are abstract-only; experimental annotations are therefore reviewed with
  curator deference rather than removed when assay details cannot be reconstructed.
- `just fetch-fitness ECOLI SlyD` could not reach a local FEBA source or the remote
  endpoint. The corrected wrapper exited nonzero and wrote no fitness artifact, so no
  phenotype inference is made from missing data.

## Core biochemical functions

- The N-terminal FKBP domain is a bona fide PPIase. The family study reports that
  “All SlyD variants catalyze the proline-limited refolding of ribonuclease T1” and
  that SlyD has pronounced chaperone properties [PMID:16388577]. The PAINT slice for
  PTHR47861 places GO:0003755, GO:0042026, and cytosol at PTN005358675; SlyD itself
  is one of the experimental descendants supporting those ancestral assertions.
  This self appearance is expected IBA evidence, not circularity.
- SlyD is also a nickel metallochaperone for [NiFe]-hydrogenase maturation. Loss of
  slyD reduces nickel accumulation and hydrogenase processing, while excess nickel
  rescues the phenotypes [PMID:15569666, “These experiments demonstrate that SlyD
  has a role in the nickel insertion step of the hydrogenase maturation pathway”].
  SlyD stimulates nickel release from HypB [PMID:17426034, “SlyD stimulates release
  of nickel from the high affinity Ni(II)-binding site of HypB”] and contacts HycE
  before metal insertion [PMID:21185288, “A SlyD-HycE interaction preceding both
  iron and nickel insertion to the enzyme was detected”]. GO:0170061 is therefore
  an evidence-matched authored term.
- Nickel maturation is separable from PPIase catalysis: PPIase-deficient mutants do
  not show corresponding hydrogenase-production defects [PMID:17720786, “Mutations
  that result in deficient PPIase activity do not produce corresponding decreases
  in the other activities of SlyD in vitro or in hydrogenase production levels in
  vivo”].

## Holdase ontology gap

- The insert-in-flap domain directly recognizes unfolded or partially folded clients
  and slows insulin aggregation [PMID:19356587, “NMR titration experiments revealed
  that the IF domain recognizes and binds unfolded or partially folded proteins and
  peptides. Insulin aggregation is markedly slowed by SlyD*”]. This is a constitutive,
  ATP-independent in-situ holdase activity.
- GO:0051082 is now obsolete and has disappeared from the current SlyD GOA. It should
  not remain as an authored core-function ID. GO:0140309 is also not evidence-matched:
  its definition requires escort to an acceptor molecule or defined location, whereas
  the SlyD anti-aggregation experiments demonstrate binding and stabilization in situ,
  not a delivery step. The project-standard general `holdase chaperone activity` NTR
  is retained as the ontology request [file:projects/UNFOLDED_PROTEIN_BINDING.md].

## Interaction annotations

- Generic GO:0005515 records are not treated as proof of nickel delivery merely because
  the partner is a hydrogenase maturation protein. High-throughput interaction-atlas
  records are retained as non-core when they establish only physical association.
  Pathway-focused HypB/HycE studies can be modified toward GO:0170061 only when their
  biological evidence supports nickel delivery, rather than transmuting IPI evidence
  from unrelated partners such as GrcA or Fur.
