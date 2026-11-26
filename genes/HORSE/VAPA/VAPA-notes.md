# Horse VAPA evidence notes

The selected 294-aa horse sequence aligns to all 249 human VAPA canonical residues at 98.4% identity. The insertion follows residue 139 and corresponds to the alternatively spliced human region documented in Q9P0L0; the MSP domain and terminal membrane anchor are intact. This supports transfer of the mammalian adaptor mechanism without equating MSP-domain membership with sperm motility.

[PMID:33124732](https://pubmed.ncbi.nlm.nih.gov/33124732/) supplies direct structural and biochemical FFAT-binding/contact-site evidence; “VAP‐A, VAP‐B, and MOSPD2 are anchored in the ER membrane by a carboxyl‐terminal transmembrane domain with their MSP domain projecting into the cytosol.” [PMID:10523508](https://pubmed.ncbi.nlm.nih.gov/10523508/) supplies the peripheral tight-junction localization: “Antibodies to the human VAP-33 co-localized with occludin at the tight junction in many tissues and tissue culture cell lines.” The latter quote has line breaks in the cached abstract. Horse ARBA descriptions repeat these conclusions but do not validate them independently.

Horse UniProt is unreviewed and cites genome sequencing/identification, not a dedicated horse functional study; no horse-specific Edison job was selected. A completed human Falcon report has been inspected.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity of the benchmark accession. A0A3Q2H1L9 (294 aa, Ensembl ENSECAT00000057069) is a full-length VAPA product, not a fragment. It is the horse counterpart of the longer human splice form, isoform 2 (Q9P0L0-2, VSP_038648: "L -> LGITPPGNAPTVTSMSSINNTVATPASYHTKDDPRGLSVLKQEKQK" after residue 139; file:human/VAPA/VAPA-uniprot.txt). A new script, `VAPA-bioinformatics/compare_isoform_ffat_rereview.py` (output `RESULTS-rereview.md`, `results-rereview.json`), shows a gapless 294/294 alignment to human isoform 2 at 95.9% identity, against 249 paired residues plus a 45-residue insertion relative to the canonical isoform 1. The MSP domain (14-131), coiled coil (217-244) and C-terminal helix (273-293) are intact. Horse UniProt has no reviewed VAPA and no 249-aa entry; the only other horse VAPA entry is A0A3Q2H6V0 (320 aa, which also carries the isoform-2 segment plus a further insertion). So no separate "canonical" horse folder is needed.

Evolutionary grounding. PANTHER places the horse protein in PTHR10809:SF155 (VAPA), the same subfamily as human Q9P0L0. In human GOA, PAINT node PTN000087323 propagates ER membrane, plasma membrane and protein-membrane adaptor activity (IBA); neuron projection development comes from a separate node, PTN002585160. PAINT did not propagate bicellular tight junction or FFAT motif binding. All eight FFAT-pocket residues named in the human VAPA crystal structure [PMID:33124732 "F207, the second residue of the FFAT motif, was bound to the hydrophobic pocket at the surface of the MSP domain constituted by aliphatic parts of the side chains of K52, T54, K94, M96, and K125 of VAP‐A"] are identical in horse (K50, K52, T53, T54, K94, F95, M96, K125).

Changes from the previous review:
- ER membrane: ACCEPT kept; the reason is now grounded in the SF155/PAINT node, not only in pairwise identity.
- Plasma membrane: KEEP_AS_NON_CORE kept; it is consistent with the PAINT propagation.
- Bicellular tight junction: changed from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED. The only evidence is one abstract-only 1999 antibody colocalization study [PMID:10523508], and PAINT declined to propagate the term.
- NEW: protein-membrane adaptor activity (GO:0043495, IBA-style inference from PTN000087323 plus pocket conservation). The horse entry had no MF annotation. FFAT motif binding was not added, which respects the PAINT omission.
- The description was rewritten to be a standalone summary and now records the isoform-2 identity. The core function was updated. Status set to COMPLETE.

Relative for the next review: human VAPA (Q9P0L0, same PANTHER subfamily SF155), at genes/human/VAPA. It has a full review (all ~186 GOA rows have actions, none PENDING). The PANTHER family review interpro/panther/PTHR10809/PTHR10809-review.yaml lists this accession under SF155, which agrees with this placement. No module in modules/ covers VAPA.
