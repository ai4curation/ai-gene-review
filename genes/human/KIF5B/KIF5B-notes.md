# KIF5B review notes

## Curation scope

Falcon deep research was attempted with `just deep-research-falcon human KIF5B`, but the
provider timed out after 600 seconds and did not generate `KIF5B-deep-research-falcon.md`.
This review therefore relies on cached publications, UniProt/GOA-derived files, PN project
mappings, and these manual curation notes.

## Core function

KIF5B encodes the ubiquitous kinesin-1 heavy chain. The core gene product role is
plus-end-directed, ATP-dependent movement on microtubules as part of the kinesin-1
motor complex, with broad cargo transport roles. Early cloning and localization work
showed human kinesin heavy chain coaligned with microtubules in transfected cells
[PMID:1607388 "Cloning and expression of a human kinesin heavy chain gene: interaction of the COOH-terminal domain with cytoplasmic microtubules in transfected CV-1 cells."], and structural work on the human kinesin motor domain supports the conserved ATPase motor mechanism
[PMID:8606779 "Crystal structure of the kinesin motor domain reveals a structural similarity to myosin."].

KIF5B is pleiotropic because kinesin-1 transports many cargos. The best-supported
process-level abstraction for the canonical role is vesicle/organelle transport along
microtubules rather than any one cargo-specific downstream phenotype.

## Proteostasis network context

The Proteostasis Network places KIF5B under
`Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Lysosomal tubulation`.
The PN mapping marks this row as `context_only` and `too_broad_to_propagate` to
`GO:0007040 lysosome organization`. That restraint is appropriate: KIF5B has strong
evidence for kinesin-dependent lysosome positioning/localization, but the current
evidence does not make KIF5B a specific autophagic lysosome reformation or lysosomal
tubulation factor in the same way as a dedicated ALR machinery component.

The direct lysosome evidence is that Arl8/SKIP recruits kinesin-1 to lysosomes and
that KIF5B knockdown causes lysosomes to cluster near the microtubule-organizing
center [PMID:22172677 "Arl8 and SKIP act together to link lysosomes to kinesin-1."].
In NK cells, Arl8b identifies KIF5B as a binding partner and KIF5B silencing blocks
MTOC-lytic granule polarization and reduces cytotoxicity
[PMID:24088571 "Arf-like GTPase Arl8b regulates lytic granule polarization and natural killer cell-mediated cytotoxicity."].

## Annotation decisions

- Accept the kinesin complex and plus-end-directed microtubule motor role as core.
- Modify generic MF annotations such as `microtubule motor activity`, `ATP binding`,
  and `microtubule binding` to the more informative
  `GO:0008574 plus-end-directed microtubule motor activity`.
- Modify broad `microtubule-based movement` to
  `GO:0047496 vesicle transport along microtubule` where a process replacement is
  needed.
- Keep lysosomal membrane, cytolytic granule membrane, lysosome localization,
  centrosome positioning, channel-trafficking, stress granule, mitochondrial, and
  neuronal cargo annotations as non-core cargo/context-specific roles.
- Mark generic `protein binding`, `identical protein binding`,
  `protein-containing complex binding`, `cadherin binding`, and broad high-throughput
  `membrane` as over-annotated because they do not describe KIF5B's molecular role.
- Do not add a new `GO:0007040 lysosome organization` annotation from the PN
  lysosomal-tubulation row; the PN project intentionally treats this row as
  context-only.
