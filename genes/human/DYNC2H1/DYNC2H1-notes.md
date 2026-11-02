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


## 2026-10-18 source-specific augmentation

This reassessment preserves all 46 imported annotation source dictionaries and the three official alternative-product identities. It retains 31 annotations as core, retains six as non-core, refines five, leaves two plasma-membrane assertions undecided, and removes two source-specific assertions. No new annotation is proposed. The earlier notes above remain intact; the qualifications below supersede their compressed explanations where needed.

### Motor and products

One integrated heavy-chain motor function replaces the earlier split between motor activity and light-intermediate-chain binding. The N-terminal assembly interfaces support the same dynein-2 motor. Human recombinant ensemble microtubule-gliding evidence establishes minus-end polarity; the human recombinant structure explains an inhibited assembly. Neither establishes single-complex processivity, a maximum physiological speed, or every modeled loading/activation step in human cilia (PMID:21723285; PMID:31451806). The human tail association study separately supports DYNC2LI1 binding (PMID:29742051).

Q8NCM8-1 is the 4,307-residue canonical sequence. Q8NCM8-2 is 4,314 residues because Q3273 is replaced by QIIGLKSW; being longer does not make it canonical. Q8NCM8-3 is 920 residues, retaining canonical residues 1–735 and 4123–4307. It is not the first 920 residues of the canonical protein. Its deletion removes the six AAA regions and microtubule-binding stalk, so full-length motor evidence is not transferred to it. The retained short-product molecular activity and physiological role remain unresolved.

### Source distinctions and positive observations

The 1996 original supports a human HeLa Golgi pool; its Golgi-dispersal perturbation was performed in rat NRK cells. Later mouse ciliated-tissue imaging does not invalidate that positive cell-line observation. Both Golgi annotations remain non-core, with species and assay limits explicit (PMID:8666668; PMID:12802074). The rat Q9JJ79 cytoplasmic donor is not mislabeled as mouse. The two plasma-membrane assertions remain undecided because the traced source chain does not resolve that pool; they are not rejected for lacking a membrane-spanning segment or a separately established membrane function.

The original-linked urinary-exosome identification table contains DYNC2H1/NP_001073932 with two peptides. This positive detection is retained as non-core rather than inferred to be contamination. It does not establish an active secretion route, an exosome-specific function, topology, or isoform-specific peptides (PMID:19056867).

The PMID:36973253 nuclear attribution was assessed beyond the title and abstract. Its operative antibody Methods identify DYNC1H1 antibody 12345-1-AP; Supplementary Figure 4 explicitly identifies DYNC1H1, DYNC1LI2 and p150 in mouse pachytene spermatocytes. The full saved body, supplementary PDF text and workbook target survey corroborate these target names. This supports a source-specific NAS attribution correction, not a universal denial of nuclear dynein-2. Nuclear-envelope association can support a nuclear component annotation and is not the rejection criterion. Figure pixels, image-only names and hypothetical antibody cross-reactivity were not verified.

### Phylogeny and the cilium-motion decision

The official target-containing PANTHER family is PTHR10676:SF352; its 787-node tree and MSA reproduce the 4,307-residue Q8NCM8-1 sequence. The UniProt-linked PTHR46532 lookup is preserved, but its retrieved current topology lacks the target and source nodes. The target lineage contains PTN002472914 and the broad root PTN000743491. Literal IBD evidence is retained; dynein-1 sibling IRDs are not transferred to DYNC2H1. Donor count and self-grounding are not treated as errors.

GO:0060294 is a child of cilium movement and part of both cilium-dependent cell motility and cell motility. The proposed removal challenges the broad ancestral placement of a ciliary-motion function across the specialized IFT branch. It does not deny that IFT can help a cell move: the review explicitly describes protozoan surface gliding, where cargo movement along a cilium transmits traction. That differs from the term's movement of the cilium. Positive motile-cilium, 9+2-cilium, assembly and retrograde-transport annotations are preserved (PMID:30065109; PMID:31451806).

### Access and reproducibility

The [source guide](DYNC2H1-source-guide.md) distinguishes preserved cache contents from separately recovered originals and lists precise assay windows. The [saved-input analysis](DYNC2H1-bioinformatics/RESULTS.md) reproduces PAINT joins, Reactome target paths, current interaction identities and the urinary-exosome target row. It reconstructs data, not annotation verdicts.

The configured Falcon attempt failed at authentication (HTTP 403); the genuine Perplexity-lite fallback failed with HTTP 401 and insufficient quota. Existing provider files remain unchanged; no replacement provider narrative was fabricated. Additional normal publication fetching regenerated the isolated workspace's lock file. Those generated bytes were archived, its pinned preimage restored and all protected positions rechecked; no canonical runtime change is proposed.

No new source excerpts were authored. Valid inherited row-level excerpts and the original notes remain unchanged. Four excerpts attached to the two superseded cores were removed during consolidation; the integrated core retains their primary reference identifiers with reference-only support. This does not claim that the aggregate historical quotations were within a new 25-word budget.

## 2026-10-18 — review follow-up

The source-preserving follow-up clarifies direct human motor-track evidence, the genuine ancestral PAINT assertion challenged for cilium movement, and the separate retained motile-cilium compartment. The urinary-exosome table maps its RefSeq identifier to Q8NCM8-2, but the original study permits splice-shared peptides for gene identification and therefore does not resolve a specific product. Positive fraction-level detection remains contextual; protein size or solubility is not evidence of contamination.

The core summary now exposes the heavy-chain tail's light-intermediate-chain-binding activity beside motor activity. Intermediate-chain contacts remain accepted and are described in the same assembly unit; the LIC term does not subsume the IC term. Axoneme and ciliary-tip locations replace their broad cilium ancestor. Cilium assembly and retrograde transport are nonredundant in the checked typed ontology closure; the assembly contribution is return transport, not an assertion that the heavy chain polymerizes the axoneme. The experimental tail and full-length constructs do not establish every natural product's competence. The replayable local evidence report is now cited directly. No imported assertion, action, product or quotation changed.
