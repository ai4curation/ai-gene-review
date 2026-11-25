# BICD1 (Bicaudal D1) review notes

UniProt: **Q96G01** → **BICD1**. PANTHER: PTHR31233. Taxon: 9606. Belongs to the
BicD family (coiled-coil).

## Core function (standalone summary)

BICD1 is a **dynein activating / cargo adaptor**. It couples the minus-end-directed
microtubule motor **dynein–dynactin** to **Rab6**-bearing Golgi and secretory-vesicle
cargo: it binds the dynein complex (and the dynein intermediate chain) and dynactin
at one end and the Rab6 GTPase at the other, driving **COPI-independent Golgi-to-ER
transport** and minus-end-directed organelle movement along microtubules. Localises
to the Golgi apparatus, cytoplasmic vesicles, cytosol, perinuclear region and
centrosome (minus-end destination).

## Key evidence (provenance)

- [PMID:12447383 abstract]: "Bicaudal-D regulates COPI-independent Golgi-ER transport
  by recruiting the dynein-dynactin motor complex." Identifies BICD as a Rab6a
  binding partner coupling it to the motor.
- [PMID:20089649 abstract]: "BicD1 is known to interact with the dynein motor complex
  and the Rab6 GTPase." (HCMV pp150 trafficking study.)
- [PMID:17139249 abstract]: GSK-3beta-regulated interaction of BICD with dynein;
  GSK-3beta is required for BICD binding to dynein but not dynactin — basis for the
  GO:0019901 protein kinase binding (GSK3B) row.
- [PMID:20164183]: BicD1 is a PAR1 (protease-activated receptor-1) interactor that
  regulates receptor trafficking — basis for the (peripheral) PAR/GPCR and
  endocytosis annotations.
- UniProt Q96G01 CC:FUNCTION/SUBUNIT: recruits dynein-dynactin for Golgi-ER
  transport; interacts with RAB6A/RAB6B.

## Annotation landscape (GOA, 54 rows)

- Adaptor MF: GO:0008093 cytoskeletal adaptor activity (IDA/IBA/IEA) — core.
- Motor-side binding (core): GO:0034452 dynactin binding, GO:0045505 dynein
  intermediate chain binding, GO:0070840 dynein complex binding.
- Cargo-side binding (core): GO:0031267 small GTPase binding (Rab6).
- Core process/location: GO:0072385 minus-end-directed organelle transport along
  microtubule; Golgi/TGN, cytoplasmic/secretory vesicle, cytosol, microtubule.
- Legacy 1997-paper terms (PMID:9367685) triaged: GO:0005200 structural constituent
  of cytoskeleton -> MODIFY to GO:0008093 (BICD1 is an adaptor, not structural);
  GO:0006396 RNA processing and GO:0009653 morphogenesis -> MARK_AS_OVER_ANNOTATED;
  GO:0008298 intracellular mRNA localisation -> KEEP_AS_NON_CORE (conserved BicD role).
- protein binding (IPI): GSK3B (P49841) -> MODIFY GO:0019901 protein kinase binding;
  viral P08318 and STAT3 (P40763) -> REMOVE.
- Peripheral: GO:0019068 virion assembly (HCMV hijacking), PAR1/GPCR endocytosis
  (GO:0048260, GO:1900737, GO:0031871 ISS) -> KEEP_AS_NON_CORE / MARK_AS_OVER_ANNOTATED.
