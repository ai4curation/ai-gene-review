# NOTCH1 review notes

## 2026-07-14 — cerebellum-module quality audit

- Audited the existing complete human NOTCH1 review rather than reseeding it. All 378
  GOA-derived annotations have explicit review actions and none remains `PENDING`.
  The project-independent description and three core-function units were retained.
- Added structured propagation metadata to the removed axon-guidance IBA annotation.
  Inspection of the recorded PANTHER node and GOA support traced the inference to
  SLIT-family donors rather than a conserved NOTCH-family function, supporting the
  existing removal decision.
- NOTCH1 is intentionally not an annoton in the cerebellum-development module. The
  original DNER study proposed a DNER–NOTCH1 mechanism, but a later full-text direct
  replication found no DNER binding or activation of NOTCH1
  [PMID:27622512 "DNER is not a Notch ligand and its true function remains unknown."].
  This module-specific evidence correction does not alter NOTCH1's well-supported
  canonical receptor activities elsewhere in the gene review.

## Evidence re-review, 2026-09-20: context and family transfer

The SLIT-seeded PTN002911625 trace does not establish a NOTCH1-specific axon-guidance mechanism, but it also does not refute one. The axon-guidance IBA is now UNDECIDED: direct Drosophila evidence identifies a noncanonical Notch/Disabled/Trio pathway for axon growth and guidance independent of canonical cell-fate signaling [PMID:18062953, “Molecular separation of two signaling pathways for the receptor, Notch.”]. A neutral focused OpenScientist report has been submitted by the coordinating reviewer to distinguish directional guidance, neurite growth and cell-fate effects in human NOTCH1; no duplicate was launched. Enzyme-inhibitor activity is retained as non-core because Notch ankyrin repeats compete with HIF for FIH hydroxylation [PMID:17573339, “Asparaginyl hydroxylation of the Notch ankyrin repeat domain by factor inhibiting hypoxia-inducible factor.”], with follow-up FIH sequestration/cross-talk evidence [PMID:18299578]. Broad transcription/coactivator and cell-periphery terms remain core where they directly capture canonical NOTCH1 function. DLL3 was removed from the list of canonical activating trans ligands. All 378 rows were screened, preserving pleiotropic developmental processes as non-core where appropriate.


## Focused axon-guidance report adjudication, 2026-09-20

The completed OpenScientist report is incorporated with a material identifier correction. The report calls the fly/mouse WITH/FROM genes Notch orthologs, but [FlyBase FBgn0264089](https://flybase.org/reports/FBgn0264089) is sli, and MGI:1315202/1315203/1315205 are [Slit3](https://www.informatics.jax.org/marker/MGI:1315202), [Slit1](https://www.informatics.jax.org/marker/MGI:1315203) and [Slit2](https://www.informatics.jax.org/marker/MGI:1315205). A fresh QuickGO exact-term query confirms those identifiers. Independent primary Notch evidence remains biologically relevant: PMID:21246649 establishes the Trio GEF1/Rac contribution, and PMID:29343637 separates cleavage/tyrosine-dependent axon patterning from cell-fate signaling. PMID:10465425 measures neurite outgrowth/morphology, while PMID:27040987 examines mammalian noncanonical synaptic-protein expression. Neither these different outputs nor absent STRING edges prove loss of guidance. The report did not align the fly determinants or reconstruct the PAINT tree; human conservation remains UNDECIDED. The report is complete and no duplicate query was launched.

## Premetazoan origin (ORIGINS_OF_MULTICELLULARITY, 2026-10-01)

Automated deep research was not run for this section. Sources were found with PubMed
searches, PMIDs and titles checked against PubMed, fetched with `just fetch-pmid`, and read
in the cache. All four papers below have `full_text_available: true`.

- PMID:19825158 Gazave et al. 2009, BMC Evol Biol, "Origin and evolution of the Notch
  signalling pathway: an overview from eukaryotic genomes" (35 eukaryotes, 22 components).
- PMID:23942320 Suga et al. 2013, "The Capsaspora genome reveals a complex unicellular
  prehistory of animals."
- PMID:29848444 Richter et al. 2018, "Gene family innovation, conservation and loss on the
  animal stem lineage" (expanded choanoflagellate transcriptomes).
- PMID:40517260 (2025, EvoDevo), "The Notch pathway in Metazoa: a comparative analysis
  across cnidarians and beyond."
- Also already in the project: PMID:18273011 (M. brevicollis genome).

### What the papers report

- **Receptor as a whole: animal-specific in the 2009 survey.**
  [PMID:19825158 "nine of the components are metazoan-specific, including the Notch receptor and the DSL ligands"];
  [PMID:19825158 "the core genes needed for a functional pathway are only present in metazoans and it apparent that the two main players, Notch and Delta, emerged via both the shuffling of old domains (EGF, ANK, LNR), and the invention of new ones (MNLL, DSL)"].
  The NOD/NODP region of the negative regulatory region is younger still:
  [PMID:19825158 "The two enigmatic domains NOD and NODP, the roles of which are still unknown, seem to be an innovation of Eumetazoa."].
- **Choanoflagellates: domain cassettes, and later one full-architecture homolog.** The
  M. brevicollis genome has the domains on separate genes
  [PMID:18273011 "Cassettes of protein domains found in metazoan Notch receptors (EGF, NL and ANK (ankyrin repeats)) are encoded on separate M."].
  Gazave et al. found one M. brevicollis gene with a Notch-like arrangement
  [PMID:19825158 "we also found another gene in this species that possesses the domain arrangement of a Notch gene (1 signal peptide, 1 EGF domain, 2 LNR domains, a transmembrane domain and 3 ANK domains, Additional file 4)"],
  but discounted it
  [PMID:19825158 "although we found a gene that possesses a domain arrangement similar to that of the metazoan Notch genes, it has very weak sequence similarity to these genes"].
  With more choanoflagellate transcriptomes, Richter et al. found a clearer case
  [PMID:29848444 "we detected a clear Notch homolog in Mylnosiga fluctuans with the prototypical EGF (epidermal growth factor), Notch, transmembrane and Ank (ankyrin) domains in the canonical order, while five other choanoflagellates contain a subset of the typical protein domains of Notch proteins"]
  and a Delta-like protein in another species
  [PMID:29848444 "dolichothecata expresses a protein containing both of the diagnostic domains of animal Delta (MNNL and DSL, both of which were previously thought to be animal-specific)"].
  Their interpretation is hedged:
  [PMID:29848444 "The distributions of Notch and Delta in choanoflagellates suggest that they were present in the Urchoanozoan and subsequently lost from most (but not all) choanoflagellates, although it is formally possible that they evolved convergently through shuffling of the same protein domains in animals and in choanoflagellates."]
  Identification used domain architecture only
  [PMID:29848444 "To identify Notch and Delta, we relied solely on conserved protein domain architecture rather than on BLAST-based or phylogenetic evidence."].
  The 2025 survey also failed to confirm a true receptor in M. brevicollis
  [PMID:40517260 "our genomic analysis found no evidence of a true Notch receptor in this species"].
- **Capsaspora: the CSL partner, but no upstream receptor.**
  [PMID:23942320 "some transcription factors that act downstream of some signalling pathways in metazoans, such as CSL (Notch–Delta pathway) and STAT (Jak–STAT pathway), are present in Capsaspora, whereas their upstream proteins are missing."];
  [PMID:23942320 "Notch signalling also seems to be a metazoan innovation, although Capsaspora has several receptor proteins that resemble the metazoan Notch and Delta proteins in their domain architecture, which may represent the ancestral components of this system"].
  Gazave et al. place CSL/Su(H) at the opisthokont ancestor
  [PMID:19825158 "All other genes originated more recently, in the last common ancestor of opisthokonts (Suppressor of Hairless (Su(H))[48]"].
  No functional data exist for any of the Capsaspora or choanoflagellate proteins.
- **Mastermind (MAML) is the youngest core partner.**
  [PMID:19825158 "The gene Mastermind is only found in eumetazoans"];
  the 2025 survey reports MAML [PMID:40517260 "absent in myxozoans, hydrozoans, placozoans, ctenophores, and poriferans"].
- **Sponges do not have the complete bilaterian set.** The lead's "sponges have a complete
  pathway" is too strong:
  [PMID:19825158 "Several Notch components are absent from the demosponge Amphimedon (Furin, Mastermind, SMRT, Numb and Neuralized), yet the pathway may still be functional in this species [30]."]
  Ctenophores look reduced or lack a canonical pathway
  [PMID:40517260 "Despite extensive genomic searches, we found no evidence of Notch ligands in this ctenophore species, suggesting the absence of a canonical Notch signalling pathway."].
- **Domains are old.** EGF, ANK and LNR modules predate animals
  [PMID:19825158 "This is the case for: EGF repeats of Notch and DSL (only present in eukaryotes [59]), ANK repeats of Mindbomb and Notch (present in eukaryotes, Archaea and Bacteria); the LNR domain of Notch"].
  Calcium binding by LNR modules is shared with the unrelated PAPP-A
  [PMID:19825158 "The only common feature that we can note between the LNR domains of Notch and PAPP-A is a calcium binding capability [100]."].

### Core functions of the existing review: ancestral or animal-specific

| Core function (existing review) | Classification | Basis |
|---|---|---|
| Transmembrane signaling receptor for DSL ligands; Notch signaling pathway; cell differentiation | **Animal-specific** (with an unresolved choanozoan prelude) | No receptor with metazoan-level sequence similarity in M. brevicollis or Capsaspora; DSL ligands animal-specific in 2009. One Mylnosiga protein with canonical EGF-LNR-TM-ANK order and a Delta-like protein in one choanoflagellate (PMID:29848444), identified by architecture only, untested biochemically. Cell differentiation and juxtacrine signaling between cells of one body is a multicellular process. |
| NICD as transcription coactivator in the CSL-NICD-MAML ternary complex | **Animal-specific as an activity of Notch; partner ancestral** | CSL is present in Capsaspora and is opisthokont-old (PMID:23942320, PMID:19825158), so the DNA-binding partner is premetazoan. The coactivator activity requires a NICD (RAM + ANK) that no unicellular protein has been shown to have, and MAML is eumetazoan-only and absent from sponges. The MAML1-RBPJ-ICN1 complex term is therefore animal-specific (and arguably eumetazoan). |
| Calcium ion binding by EGF (and LNR) repeats | **Ancestral at the domain level, not at the protein level** | Ca-binding EGF and LNR modules are older than animals (PMID:19825158), but this says nothing about a NOTCH1 ortholog; the activity is a property of the domain type wherever it occurs. |

**Answer to the project question:** NOTCH1 holds up as an animal-innovation comparator, with
one caveat. None of its core functions has a demonstrated premetazoan counterpart *as a
protein activity*. What predates animals is (a) its downstream DNA-binding partner CSL/RBPJ
(opisthokont-old, present in Capsaspora), and (b) its constituent domains. The one
challenge to "animal-specific" is the Mylnosiga fluctuans protein with full Notch domain
order (PMID:29848444), which its authors say may reflect a Choanozoa-level origin followed
by loss, or convergent domain shuffling. Nothing is known of its function. The control
therefore holds for function, but it is not a clean "absent in all unicellular relatives"
control for gene presence.

### Track C check (2026-10-01)

NOTCH1 IBA rows come from two PANTHER nodes in PTHR45836:
- PTN001933897 (taxon:6072 Eumetazoa in `interpro/panther/PTHR45836/PTHR45836-paint.tsv`):
  Notch signaling pathway, plasma membrane, cell surface, receptor complex.
- PTN002911625: axon guidance (SLIT-seeded; see the 2026-09-20 note above).

QuickGO `withFrom=PANTHER:<PTN>&taxonUsage=descendants` returned **0 annotations** for both
nodes in Choanoflagellata (28009), Filasterea (2687318) and Ichthyosporea (127916).
Controls: PTN001933897 has 3943 annotations, all within Metazoa (33208 count = Eukaryota
2759 count); PTN002911625 has 125, also all within Metazoa. No animal tissue, organ or
development term from these nodes reaches a unicellular holozoan. This is the expected
negative result for an animal-innovation comparator, and it is consistent with the Notch
node being placed at Eumetazoa. Note that the choanoflagellate Notch-like proteins
(e.g. from Mylnosiga) are from transcriptomes not in UniProt reference proteomes, so their
absence from QuickGO is not by itself evidence against homology.

### Actions

No existing review action changed: the evolutionary evidence does not bear on any IBA row
(all propagation stays within animals). Added an evolutionary-origin sentence to the
description, the four papers to references, and suggested questions.
