# pav review notes

## Setup
- `just fetch-gene DROME pav` resolved Q9VZF5 (FlyBase FBgn0011692, GeneID 38515); 49 GOA rows.
- `just fetch-gene-pmids DROME pav`: 15 PMIDs cached. Additionally cached PMID:9585508 (Adams 1998,
  original pav cloning), PMID:12530961 (Somers & Saint 2003), PMID:25557664 (Del Castillo 2015).
- No deep-research provider keys; literature synthesis is in `pav-deep-research-manual.md`.
- Abstract-only: PMID:12134082, 16174742, 20516152, 19297411, 17046997, 8060613, 26659188,
  9585508, 12530961.

## Key paper PMID:9813088 (Carmena et al. 1998, polo and cytokinesis)
Full text read. Supports Pav localization in male meiosis: cleavage furrow ["we could readily
observe the protein in the cleavage furrows at the telophase of both meiotic divisions"], ring of
the furrow ["Pav-KLP is present in the rings of the cleavage furrows"], ring canals ["In male
meiosis it persists to become incorporated into the 15 ring canals of the primary spermatocyte
cyst"], and axonemes ["In addition, Pav-KLP is found associated with some (putative immature)
axonemes"]. Polo is needed for Pav-KLP relocalization to the midzone.

## Decisions (summary)
- Core: kinesin-6 microtubule motor; centralspindlin subunit; spindle midzone assembly and mitotic
  cytokinesis; localization at midzone, cleavage furrow, contractile ring, midbody, ring canals.
- MODIFY: cytoskeletal motor activity -> microtubule motor activity; nucleotide binding -> ATP
  binding; cytoskeleton / microtubule cytoskeleton -> mitotic spindle midzone; kinesin complex ->
  centralspindlin complex (centralspindlin is a kinesin-dimer-containing complex but not is_a
  kinesin complex in GO); mitotic spindle organization -> mitotic spindle midzone assembly;
  actomyosin contractile ring contraction -> actomyosin contractile ring assembly (ATP-binding
  mutant prevents furrow formation, PMID:14517316; ring components mislocalized, PMID:9585508);
  maintenance of protein location in cell -> maintenance of protein location in cell cortex
  (myosin II at equatorial cortex); microtubule sliding -> negative regulation of plus-end directed
  microtubule sliding (Pav brakes kinesin-1 sliding); negative regulation of neuron projection
  arborization -> negative regulation of neuron projection development (dendrite length increased,
  branch number unchanged in Pav RNAi, PMID:32022690).
- REMOVE: protein binding (14-3-3 IPI) per protein-binding policy.
- MARK_AS_OVER_ANNOTATED: cytoskeleton-dependent intracellular transport (IBA from cargo
  kinesins; Pav cargo transport only speculated); PNS development TAS (indirect consequence of
  cytokinesis failure).
- UNDECIDED: kinetochore microtubule IDA (PMID:17046997 abstract-only; abstract describes plus ends
  of central spindle microtubules, not kinetochore fibres).
- No NEW annotations; the gene's core activities are already covered by existing rows.
