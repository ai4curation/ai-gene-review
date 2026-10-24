# GEMIN5: paired human–horse review notes

## Biological evidence

Primary RNA-bound structures establish cap/snRNA recognition by tandem WD40 propellers. Direct SMN-UTR binding and ribosome experiments establish transcript-dependent translation regulation. Generic physical interactions are not substituted for these specific molecular activities.

- [PMID:27881600: Structural insights into Gemin5-guided selection of pre-snRNAs for snRNP assembly.](https://pubmed.ncbi.nlm.nih.gov/27881600/) — abstract cached; full-text availability must be checked separately.
- [PMID:27881601: Structural basis for snRNA recognition by the double-WD40 repeat domain of Gemin5.](https://pubmed.ncbi.nlm.nih.gov/27881601/) — full text cached.
- [PMID:25911097: Gemin5 Binds to the Survival Motor Neuron mRNA to Regulate SMN Expression.](https://pubmed.ncbi.nlm.nih.gov/25911097/) — full text cached.
- [PMID:27507887: The RNA-binding protein Gemin5 binds directly to the ribosome and regulates global translation.](https://pubmed.ncbi.nlm.nih.gov/27507887/) — full text cached.
- [PMID:11714716: Gemin5, a novel WD repeat protein component of the SMN complex that binds Sm proteins.](https://pubmed.ncbi.nlm.nih.gov/11714716/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

The horse model lacks human723–798, spanning the end of the WD40 RNA-recognition module. Nuclear/cytoplasmic localization remains plausible, but specific RNA recognition and assembly require the module integrity to be resolved. Protein ubiquitination has no demonstrated mechanistic role in the retrieved sources; being a ubiquitination substrate would not establish that process.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/GEMIN5/GEMIN5-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Inspect the deletion in the tandem-propeller structure and check horse transcripts. Resolve high-throughput partner rows from supplementary records; do not infer their validity from other known GEMIN5 interactions.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of every existing annotation, the description and core functions of human GEMIN5 (Q8TEQ6). ProtNLM2 outputs were not opened or used.

### Identity
- Q8TEQ6 is the reviewed, canonical UniProt entry (GEMI5_HUMAN, 1508 aa, sequence version 3). It is not a fragment, isoform or alternative gene model. Domain architecture is complete: 13 WD repeats (62-720) forming the tandem WD40 propellers, the central TPR-like dimerization module, and the C-terminal RBS1/RBS2 RNA-binding region (Pfam PF23770, PF23775, PF23774, PF23777).
- PANTHER PTHR46362 (GEM-ASSOCIATED PROTEIN 5) has a single subfamily, SF1, containing Gemin5 orthologs (human, mouse, Drosophila rig). The family review (interpro/panther/PTHR46362/PTHR46362-review.yaml) assesses snRNA binding as FAMILY_WIDE; this review agrees and finds no placement disagreement.

### Evidence base (primary literature)
- snRNA recognition: GEMIN5 is the snRNA-binding protein of the SMN complex and binds the Sm site and adjacent features directly [PMID:16857593 "Gemin5 binds directly and specifically to the unique features, including the Sm site, of snRNAs."]; WD40 domain necessary and sufficient [PMID:19377484 "The entire WD repeat domain, comprising 13 WD motifs, is both necessary and sufficient for sequence-specific, high-affinity binding of Gemin5 to its RNA targets."]; delivers pre-snRNAs [PMID:20513430 "highlighting Gemin5's function in delivering pre-snRNAs as substrates for Sm core assembly and processing"].
- Cap binding is direct, not via eIF4E [PMID:19750007 "This observation indicates that eIF4E is not responsible for tethering gemin5 to m7G."]. This contradicts the earlier claim of a direct GEMIN5-eIF4E interaction (PMID:16739988), now marked DISPUTED.
- Translation: SMN 3'-UTR binding increases SMN translation [PMID:25911097 "Gemin5 binding to the SMN 3′-UTR activates expression of SMN protein by increasing translation of the SMN mRNA."]; ribosome binding and depletion enhances global synthesis [PMID:27507887 "Gemin5 siRNA depletion decreased the polysome/80S ratio, and enhanced global protein synthesis."].
- Disease: patient variants reduce snRNP assembly [PMID:33963192 "suggesting that loss of GEMIN5 in Leu1068Pro and His913Arg neurons leads to disruption of snRNP assembly formation"].
- Newly cached: PMID:16314521, PMID:33963192. PMID:27834343 (cited by UniProt) failed to fetch.

### Changes relative to the previous review
- All 17 bare GO:0005515 rows: KEEP_AS_NON_CORE/UNDECIDED -> REMOVE under the protein-binding policy (interactions not denied; captured by SMN complex / SMN-Sm complex membership). The previous text wrongly attributed the PMID:19750007 rows (partners GEMIN4, DDX20) to eIF4E.
- RNA binding (HDA, IPI) -> MODIFY to snRNA binding + mRNA binding.
- regulation of translation -> MODIFY to both positive (SMN mRNA) and negative (global synthesis) regulation of translation.
- mRNA splicing, via spliceosome and protein-containing complex assembly -> MODIFY to spliceosomal snRNP assembly (a descendant of both).
- cytoplasm -> MODIFY to cytosol; nucleus (IBA) -> MODIFY to nucleoplasm + Gemini of Cajal bodies; nuclear body -> MODIFY to Gemini of Cajal bodies.
- SMN-Gemin2 complex -> KEEP_AS_NON_CORE (GEMIN5 is a peripheral SMN-complex component, PMID:17178713, not part of the SMN-Gemin2 stable core); not removed because the curator read the full text.
- snRNA binding kept at the general level: GEMIN5 recognizes the Sm site shared by all Sm-class snRNAs.
- Core functions rewritten: snRNA binding (spliceosomal snRNP assembly, SMN complex), m7G cap binding, mRNA 3'-UTR binding (positive regulation of translation), ribosome binding (negative regulation of translation); all located in the cytosol.
- No NEW terms proposed.

### Relative to review next
- Closest experimentally characterised ortholog in a model organism by phylogenetic placement: Drosophila melanogaster rig (rigor mortis; FBgn0250850, UniProtKB:Q86BY9), in the same PANTHER subfamily (PTHR46362:SF1) and a donor to the Gemin5 PAINT node PTN005299808 (SMN complex, nucleus IBAs). It has IDA/IMP/IGI annotations (SMN complex, snRNP assembly-related). Mouse Gemin5 (Q8BX17) carries only one experimental row (mRNA 3'-UTR binding). No review of rig exists under genes/DROME/.
- Module: modules/dmel_smn_complex.yaml includes rig as the snRNA-binding Gemin5 subunit.
