# NCU09721: biological evidence

NCU09721 is a large beta-adaptin assigned to the AP-1 cargo-adaptor complex by curated phylogenetic inference. It provides a noncatalytic scaffold for membrane-cargo sorting within the Golgi/endosomal trafficking system. Characterized filamentous-fungal AP-1 complexes support post-Golgi secretion, endosome recycling, and clathrin-associated carrier traffic. These conserved roles support Golgi and carrier-membrane recruitment in Neurospora crassa, while its individual cargoes and direct clathrin-binding mechanism remain uncharacterized.

- cytoplasm: Beta-adaptin is a cytoplasmic coat-adaptor subunit that is recruited to the cytoplasmic surfaces of intracellular membranes. The AP-family fold and characterized fungal AP1 assemblies support this broad location.
- trans-Golgi network: The target AP-1 membership IBA and beta-adaptin domain support transfer from experimentally localized filamentous-fungal AP1 beta subunits. Fusarium AP1 beta colocalizes with a trans-Golgi marker, supporting the TGN assignment.
- intracellular protein transport: Characterized filamentous-fungal AP1 supports secretory carrier sorting and endosome recycling. The curated AP1-family assignment grounds a conserved role in intracellular vesicle-mediated protein traffic.
- endocytosis: AP1 contributes to endosomal recycling and endocytic itineraries in filamentous fungi; Fusarium AP1 loss delays internalization of the endocytic dye FM4-64. This supports a process contribution without reassigning the beta subunit to AP2 or claiming a primary plasma-membrane uptake function.
- endomembrane system: The AP1-family placement and direct Golgi localization of the related Fusarium beta subunit support a more precise trans-Golgi-network compartment.
- protein transport: Characterized filamentous-fungal AP1 supports secretory carrier sorting and endosome recycling. The curated AP1-family assignment grounds a conserved role in intracellular vesicle-mediated protein traffic.
- vesicle-mediated transport: Characterized filamentous-fungal AP1 supports secretory carrier sorting and endosome recycling. The curated AP1-family assignment grounds a conserved role in intracellular vesicle-mediated protein traffic.
- membrane coat: AP1 beta forms part of a membrane-associated cargo-adaptor coat. Filamentous-fungal AP1 assembles with other AP1 subunits and supports clathrin-dependent traffic, consistent with membrane coat membership.
- AP-1 adaptor complex: The curated IBA at PTN000123672 assigns this beta-adaptin to AP1 with experimentally characterized fungal AP1 beta descendants. The AP-beta domain and fungal AP1 subunit-interaction experiments support that inherited complex role; it is not inferred from the generic beta1/2/4 domain alone.
- clathrin binding: Dikaryan beta-adaptins lack the canonical C-terminal clathrin-binding appendage, but Aspergillus AP1 beta uses alternative tail motifs. The target sequence contains LLDID at residues 629–633, matching one tested Aspergillus motif, and terminal LLGLF at 745–749; the stronger Aspergillus LLNGF motif is not identical. These observations support clathrin-association plausibility, but short motif similarity and complex traffic do not establish the exact intrinsic target-binding mechanism. Direct target binding remains unresolved.

Primary evidence excerpts

- [file:NEUCR/NCU09721/NCU09721-uniprot.txt] “DR   InterPro; IPR026739; AP_beta.”
- [PMID:36836259] “FgAP1β interacts with FgAP1σ, FgAP1γ, and FgAP1μ”
- [PMID:36836259] “FgAP1β-GFP, FgAP1γ-GFP, and FgAP1μ-GFP also localize to the Golgi apparatus.”
- [PMID:29925567] “its role in clathrin-dependent maintenance of polar traffic of
specific membrane cargoes toward the apex of growing hyphae. We provide evidence
that AP-1 is involved in both anterograde sorting of RabERab11-labeled SVs and
RabA/BRab5-dependent endosome recycling.”
- [PMID:36836259] “the loss of FgAP1σ blocks the transportation of the v-SNARE protein FgSnc1 from the Golgi to the plasma membrane and delays the internalization of FM4-64 dye into the vacuole.”
- [PMID:28220754] “clathrin binding domains are also missing from the AP-1 β subunit (β1) of all Dikarya”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

The Falcon report does not account for the target AP1 IBA when calling complex identity unresolved. The curated AP1 assignment is retained; generic AP-beta domains alone would not distinguish AP1 from AP2. ProtNLM Golgi donor Q22498 is worm COPG-1, a coatomer subunit, so independent AP1 primary evidence is used for the location.

Direct inspection of the frozen Q7S2Q5 sequence gives LLDID at 629–633 and LLGLF at 745–749 (one-based positions after stripping sequence whitespace). PMID:29925567 full-text section “AP-1 associates with clathrin via specific C-terminal motifs” and Fig. 4E identify Aspergillus LLDID at630 and LLNGF at707; mutating these affects clathrin distribution, especially LLNGF. This strengthens family-transfer plausibility but does not equate motif detection with a target binding assay. Primary full text inspected at https://pmc.ncbi.nlm.nih.gov/articles/PMC6063236/.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

The ProtNLM2 outputs (`*-protnlm-*` files) were not opened or used.

### Identity
- Q7S2Q5 (NCU09721; 749 aa; unreviewed) is a complete, full-length product, not an isoform, fragment
  or alternative gene model. The PANTHER PTHR11134 hit spans 18-604, which is the adaptin trunk. The
  length matches its Fusarium (V6RKE4, 747 aa) and Aspergillus (AN3029, 766 aa) orthologs. The protein
  lacks a beta-appendage domain, as expected for Dikarya beta1
  [PMID:28220754 "clathrin binding domains are also missing from the AP-1 β subunit (β1) of all Dikarya"].
- UniProt gives only the family (PTHR11134) and no subfamily. The family review
  (interpro/panther/PTHR11134/PTHR11134-review.yaml) asserts no subfamily or PAINT node placement for
  the target, so there is no disagreement to report. Its comment that NCU09721 "needs AP-1 placement
  evidence" is answered below.

### Phylogenetic placement (new analysis)
`NCU09721-bioinformatics/beta_adaptin_phylogeny_rereview.py` produced the results in `RESULTS-rereview.md`
(MAFFT + NJ, 100 bootstraps, 16 beta-adaptins, rooted on AP3B1).
- NCU09721 groups with F. graminearum V6RKE4 and A. nidulans AN3029 (100/100), then with S. pombe apl2,
  the AP-1 beta (96/100). The S. cerevisiae APL2 placement is weak (40/100) because of its long branch.
- The paralog NCU05232 (Q7S8H6, 748 aa) is in the AP-2 beta clade (apl1/APL1). NCU06569 is the AP-3 beta.
- AN3029 carries LLDID at 653 and LLNGF at 730. These are the motifs the Aspergillus AP-1 paper reports
  at 630 and 707: the spacing is the same and the offset of 23 is a gene-model difference. So AN3029 is
  the studied A. nidulans AP-1 beta.
- NCU09721 has LLDID at 629-633 and LLGLF at 745-749, and has no LLNGF.

### PAINT observations
- AP-1 adaptor complex IBA from PTN000123672, seeded by pombe apl2 (SPBC947.02), budding yeast APL2
  (S000001618) and Dictyostelium ap1b1. This is consistent with the tree, so it is ACCEPTED.
- QuickGO shows that the same PTN000123672 AP-1 IBA also reaches NCU05232, the AP-2 beta paralog. That
  annotation also carries Ensembl Compara IEA to S. pombe apl1 (O43005). This suggests the PTN000123672
  node lies above the fungal beta1/beta2 split. It is a concern for NCU05232, not for this gene, and is
  recorded as a suggested question.
- The endocytosis IBA comes from the deep node PTN000123671, with donors that are AP-2 beta or metazoan
  beta subunits shared by AP-1 and AP-2. Dikarya have separate AP-1 and AP-2 beta genes, and in
  A. nidulans AP-2 carries out apical endocytosis. The action changed from KEEP_AS_NON_CORE to
  MARK_AS_OVER_ANNOTATED. The Fusarium FM4-64 delay was a sigma1-deletion phenotype on delivery to
  the vacuole, which is indirect.
- The newer PTN000123671 IBD to GO:0030674 (dated 2026-08-28) is not yet in this GOA snapshot. No NEW
  annotation was added.

### Action changes vs the previous version
- cytoplasm: ACCEPT changed to MODIFY (replacement trans-Golgi network). The term is correct but general,
  and the specific descendant is already carried.
- endocytosis: KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED, for the paralog/complex mismatch
  described above.
- protein transport: ACCEPT changed to MODIFY (replacement intracellular protein transport).
- vesicle-mediated transport: ACCEPT changed to MODIFY (replacement post-Golgi vesicle-mediated transport,
  GO:0006892). The basis is Aspergillus secretory-vesicle sorting from the trans-Golgi and Fusarium
  Golgi-to-PM delivery of Snc1.
- membrane coat: ACCEPT changed to MODIFY (replacement AP-1 adaptor complex, already carried).
- Unchanged: trans-Golgi network and AP-1 adaptor complex (ACCEPT), intracellular protein transport
  (ACCEPT), endomembrane system (MODIFY to TGN), and clathrin binding (UNDECIDED; LLDID is present but
  LLNGF is absent, and there is no binding assay).
- Core function: changed from contributes_to clathrin-cargo adaptor activity to contributes_to cargo
  adaptor activity (GO:0140312). The reason is that direct clathrin engagement by Dikarya beta1 is
  unresolved. The process is now post-Golgi vesicle-mediated transport plus intracellular protein
  transport.

### Relative to review next
Schizosaccharomyces pombe apl2 (O43079; SPBC947.02) is the AP-1 beta ortholog in the nearest model
organism (96/100 bootstrap) and a PAINT seed of PTN000123672. The repo has no review of it. Human AP1B1
(genes/human/AP1B1, COMPLETE) is a more distant family member. Metazoan beta1/beta2 arose from a separate
duplication.

### Modules
- modules/dmel_clathrin_adaptor_coats.yaml (AP-1/AP-2/AP-3 clathrin adaptor coats, Drosophila).
- modules/synaptic_vesicle_endocytosis.yaml (cites PTHR11134; AP-2 context, not relevant to AP-1).
