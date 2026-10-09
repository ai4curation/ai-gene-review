# DYNC2H1 notes

Deep research: not run. In this environment falcon times out after 600 s and perplexity-lite is not
installed. The review uses the cached GOA-cited publications, PMID:19442771 and the UniProt record.

## Key points
- Dynein-2 minus-end motor activity in vitro. [PMID:21723285 "In an in vitro MT gliding assay, both dynein-1 and dynein-2 showed minus-end-directed motor activities."]
- Structure and loading onto IFT-B trains. [PMID:31451806 "Dynein-2 assembles with polymeric intraflagellar transport (IFT) trains to form a transport machinery that is crucial for cilia biogenesis and signaling."]
- The heavy chain binds LIC3/DYNC2LI1. [PMID:31451806 "Both copies of DHC2 bind a LIC3 subunit."]
- Disease. [PMID:19442771 "DYNC2H1 is a component of a cytoplasmic dynein complex and is directly involved in the generation and maintenance of cilia."]

## Curation decisions
- REMOVE: cilium movement involved in cell motility (IBA, PTN000743491). This node is dominated by
  axonemal dynein heavy chain donors (DNAH1/3/5/11, DNHD1), and dynein-2 does not power ciliary
  beating. A propagation_review was added.
- REMOVE: male germ cell nucleus (NAS, PMID:36973253). That paper is about DYNLRB1/2 dynein-1
  complexes and does not mention DYNC2H1.
- MODIFY: protein binding with DYNC2LI1 changed to dynein light intermediate chain binding.
  Cytoskeletal motor activity changed to minus-end-directed microtubule motor activity.
- Golgi localization and Golgi organization (PMID:8666668, 1996 antibody study) are kept as non-core.
- There is no PANTHER family review for PTHR46532, so no family/gene disagreement arises.
