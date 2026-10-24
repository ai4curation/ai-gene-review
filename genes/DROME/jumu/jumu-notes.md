# Jumu evidence notes

Q9XTP7 is the native 719-residue PA protein of FBgn0015396 (AAF54525/NP_524302); FlyBase lists one protein product. Jumu/Jumeaux and the historical Domina/DOM name in PMID:10940625 refer to this locus, rather than the distinct chromatin remodeler domino. [FlyBase](https://flybase.org/reports/FBgn0015396).

[PMID:22378636](https://pmc.ncbi.nlm.nih.gov/articles/PMC3308180/) is cached with full text and directly establishes Forkhead-site-dependent Nidogen enhancer regulation by Jumu and CHES-1-like. It supplies the decisive evidence for the ProtNLM sequence-specific DNA-binding prediction, rated LSP relative to cis-regulatory sequence binding. Transcriptional effects are not inferred solely from the protein-family name.

[PMID:10887088](https://pubmed.ncbi.nlm.nih.gov/10887088/) describes nuclear Jumu and asymmetric neuronal fate regulation. [PMID:10940625](https://pubmed.ncbi.nlm.nih.gov/10940625/) explicitly reports the 719-residue protein, chromocenter/euchromatic localization, position-effect variegation and eye/wing defects. [PMID:20213139](https://pubmed.ncbi.nlm.nih.gov/20213139/) reports dosage-dependent chromatin and nucleolar effects. Their target-specific abstracts support the stated conclusions, while detailed uninspected full-text experiments are not invented. The genome-wide PMID:17412918 and heterochromatin PMID:27514026 annotations are consistent with independently established target chromatin/nuclear residence.

[PMID:22814603](https://pmc.ncbi.nlm.nih.gov/articles/PMC3401414/) full text supports cardiac division control through Polo. [PMID:34999256](https://pubmed.ncbi.nlm.nih.gov/34999256/) supports wound-responsive JAK/STAT activation. These roles are retained as non-core tissue/pathway consequences of the transcriptional regulator. The dorsal-closure TAS reference PMID:12147138 remains abstract-only and its Jumu-specific support cannot be located; that one role remains UNDECIDED rather than being removed from incomplete evidence.

Falcon completed and was inspected. Its 2024 cardiac-network lead was verified in [PMID:39684645](https://pmc.ncbi.nlm.nih.gov/articles/PMC11641245/), cached with full text: “Phenotypic analysis of a subset of these targets identified 21 jumu-regulated genes that mediate cardiac progenitor cell division”. This expands the downstream network while preserving the distinction between expression/genetic regulation and direct functional enhancer binding. The provider describes approximately 720 residues; the exact frozen Q9XTP7/native PA sequence is 719 residues, also reported in the original Domina paper. Its literature selection omits the directly relevant 2012 Nidogen enhancer study, which remains the decisive sequence-specific regulatory-DNA evidence.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: every existing annotation, the description and core functions were re-examined against the cached literature (PMID:22378636, PMID:22814603, PMID:39684645 and PMID:27514026 full text; the other primary papers abstract-only) and the PANTHER/PAINT evidence. ProtNLM2 output was not consulted.

Identity: Q9XTP7 is the full-length 719-residue product of FBgn0015396 (forkhead DNA-binding domain at residues 411-508 in the UniProt record), the length reported for Domina in [PMID:10940625 "encode a 719-amino-acid protein with a FKH/WH domain and a putative acidic transactivation domain"]. It is not a fragment, isoform or alternative gene model.

Evolutionary placement: new analysis `jumu-bioinformatics/panther_placement_rereview.py` (results in `RESULTS-rereview.md`) reads the PANTHER 19.0 HMM classification files. Jumu is in PTHR13962:SF17 (FORKHEAD BOX PROTEIN N4) with human FOXN4 Q96NZ1, mouse Foxn4 Q8K3Q3 (MGI:2151057) and zebrafish foxn4 A2BGM5. The UniProt cross-reference (PTHR46721:SF3, FORKHEAD BOX N1) disagrees; the family review `interpro/panther/PTHR46721/PTHR46721-review.yaml` already records this conflict and does not assert Jumu as a PTHR46721 member. The IBA donors at PTN000216159 (mouse/zebrafish/human FOXN4, FOXN3 O00409, FOXN2 P32314) are all PTHR13962 members, consistent with the official placement. Only the generic forkhead TF mechanism is transferred; FOXN4-specific programs (retina, AV canal, multiciliogenesis) are not.

Key molecular evidence: [PMID:22378636 "By contrast, the binding of Jumu was detected in vitro only at the Fkh2 site, with only an excess of wild-type but not mutated Fkh2 unlabeled probe being capable of competing."] and [PMID:22378636 "Overexpression of Jumu is unable to repress reporter expression from an enhancer with mutations in all three Fkh sites."] Together with trans loss-of-function assays this meets the standard for RNA polymerase II-specific repressor activity. Activation is so far shown only by expression profiling: [PMID:39684645 "we intend to assess which of these genes are direct targets of Jumu in the future"].

Changes made:
- GO:0003700 (IBA, IEA): ACCEPT -> MODIFY to GO:0001227 DNA-binding transcription repressor activity, RNA polymerase II-specific; core function MF changed accordingly.
- GO:0006355 (IBA, IEA): ACCEPT -> MODIFY to GO:0000122 negative regulation of transcription by RNA polymerase II.
- GO:0000976, GO:0003677, GO:0043565: MODIFY to GO:0000987 (unchanged), now quoting the EMSA result.
- GO:0006325 chromatin organization: ACCEPT -> KEEP_AS_NON_CORE (mechanism, structural vs transcriptional, unresolved).
- Euchromatin, polytene chromosome and chromocenter rows: ACCEPT -> KEEP_AS_NON_CORE; chromatin and nucleus stay ACCEPT.
- Dorsal closure TAS stays UNDECIDED (review abstract does not mention jumu; full text not cached).
- Developmental, wounding, JAK/STAT and cell-division rows stay KEEP_AS_NON_CORE.
- No NEW annotations. Hematopoiesis phenotypes (Hao 2017/2018 in the falcon report) are phenotype-level and were not added.
- Added reference_review entries, the falcon report and the re-review analysis as references; status set to COMPLETE.

Relative to review next: mouse Foxn4 (Q8K3Q3, MGI:2151057), in the same PANTHER 19.0 subfamily and a donor of every IBA here; no review exists in the repo. Modules: no module includes jumu; `modules/cardiac_specification_network.yaml` and `modules/dmel_jak_stat_signaling.yaml` are related context only.
