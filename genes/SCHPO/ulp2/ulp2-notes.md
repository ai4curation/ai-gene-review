# ulp2 notes

Identity: ulp2, UniProt O13769; current PomBase systematic identifier is recorded in the benchmark cohort. The UniProt sequence is the reviewed current record, whereas the source XML uses placeholder taxonomy and sequence fields. Those placeholders are not biological evidence.

## ProtNLM source provenance

Source: PRE-RELEASE post-processed-2026_02_28k.xml. The exact entry is in `ulp2-protnlm-source.xml`. No entry belongs to the published 26,856-record pilot list. Current API availability does not change the original source version.

The XML evidence keys, model scores, string-match hydration metadata and alignment accessions/scores are retained verbatim in that source file. Assessments use current sequence features and primary sources; annotation overlap and ARBA output do not independently validate a prediction.

## Biological evidence and interpretation

LSP: Purified fission-yeast Ulp2 directly deconjugates SUMO from high-molecular-weight species, and the study identifies it as a cysteine protease. SUMO is a ubiquitin-like modifier, so the broad ubiquitin-like protein peptidase term is biologically correct. The more specific deSUMOylase activity GO:0016929 is experimentally established and already annotated; the XML records hydration from that term. This prediction loses substrate specificity and is therefore LSP. It does not imply a demonstrated ability to remove ubiquitin itself.

[PMID:24818994 "These results confirm that like S. cerevisiae Ulp2, S. pombe Ulp2 is a cysteine protease whose main function is in deconjugating SUMO from target proteins."]

LSP: Direct biochemical experiments establish Ulp2 as a SUMO-deconjugating cysteine protease, including sensitivity to N-ethylmaleimide. The conserved C48 catalytic domain is consistent with that mechanism. Cysteine-type peptidase activity is true but less precise than the already annotated deSUMOylase activity and its SUMO substrate specificity. The XML keyword hydration does not supply independent validation; the target biochemical result does.

[PMID:24818994 "These results confirm that like S. cerevisiae Ulp2, S. pombe Ulp2 is a cysteine protease whose main function is in deconjugating SUMO from target proteins."]


## Ontology specificity

QuickGO GO:0070139 (SUMO-specific endopeptidase activity), accessed 2026-09-08: "Catalysis of the hydrolysis of peptide bonds between an alpha-carboxyl group and an alpha-amino group within the small conjugating protein SUMO.". The frozen JSON is adjacent to this file.


## Assay scope

The full text of [PMID:24818994](https://pubmed.ncbi.nlm.nih.gov/24818994/), DOI [10.1371/journal.pone.0094182](https://doi.org/10.1371/journal.pone.0094182), separates precursor maturation from deconjugation. Figure 1 compares full-length SUMO processing by Ulp1 and Ulp2, then tests high-molecular-weight SUMO conjugates in pombe extracts with increasing Ulp2 amounts and an NEM-treated enzyme control. These experiments establish deSUMOylation more specifically than either external peptidase prediction. Reduced precursor-processing efficiency is not a demonstration of absolute inability to process precursor SUMO.

The eIF4G/eIF3h interactions do not make Ulp2 a constitutive translating-ribosome component. The discussion reports that Ulp2 remained in large sedimenting complexes when EDTA disrupted polysomes. Its stress and translation-factor associations therefore should not be treated as evidence for ribosomal residence or an intrinsic translation activity. This is the same primary study used in the review, not an additional experimental replication.

## Appraisal of completed Falcon report

The original Falcon request completed after 1295.37 seconds (about 21.6 minutes), despite the wrapper reporting a 600-second timeout and the fallback failing with quota HTTP401. The returned provider report and its artifact were retained unchanged and inspected. No duplicate request was made.

The report agrees with the primary biochemical and localization evidence already used here: Ulp2 is predominantly a SUMO-deconjugating cysteine protease in intranuclear foci, with substantially weaker SUMO-precursor processing than Ulp1. Its eIF4G discussion correctly distinguishes co-purification and eIF4G sumoylation from direct Ulp2-dependent substrate turnover. It supplies no evidence resolving the specific stress-granule or translation-regulation assertions. Both external broad peptidase predictions therefore remain LSP.

The additional 2016 primary source was verified and cached in full: PMID:27398807, Functional Crosstalk between the PP2A and SUMO Pathways Revealed by Analysis of STUbL Suppressor, razor 1-1. The Ulp2-relevant results support genetic suppression and altered SUMO-conjugate abundance: [PMID:27398807 "Strikingly, as for slx8-29, we found that pab1-1 strongly suppressed the HU sensitivity of ulp2∆ cells (Fig 6A). Moreover, western analysis of SUMO again revealed a small but detectable reduction in HMW species in ulp2∆ pab1-1 double mutant versus ulp2∆ single mutant cells (Fig 6B)."]. This strengthens SUMO-homeostasis context without changing modifier specificity, localization or the existing GO judgments.

The STUbL relationship must remain genotype-dependent rather than being reduced to two interchangeable routes that prevent SUMO accumulation. The primary paper explicitly states [PMID:27398807 "Therefore, unscheduled STUbL activity on SUMO-chain modified proteins, rather than the SUMO chains themselves, is toxic to ulp2∆ cells."]. Neither the generated synthesis nor this genetic relationship identifies a direct Ulp2-STUbL complex or a shared named substrate. No biological YAML changes were warranted by the late report.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined every GOA row, the description and core functions against PMID:24818994 (full text), PMID:16823372 (abstract), PMID:27398807 (full text), the UniProt record and PANTHER/PAINT placement. ProtNLM2 files were not opened or used.

### Identity
- Benchmark accession O13769 is the reviewed canonical UniProt entry for ulp2 (SPAC17A5.07c), 638 aa, full-length; not an isoform, fragment or alternative gene model.
- Catalytic triad present at the UniProt-annotated positions (checked against the sequence in ulp2-uniprot.txt): His440, Asp494, Cys544 (context ...SNFSDC544GIYALH...). Peptidase C48 domain (PF02902, PS50600) intact.

### Evolutionary placement
- UniProt PANTHER: PTHR46896 (SENTRIN-SPECIFIC PROTEASE) subfamily SF3 (FI06413P-RELATED). Human SENP6 (Q9GZR1) is SF1 and SENP7 (Q9BQF6) is SF2 of the same family.
- S. cerevisiae Ulp2/Smt4 (P40537) is in a different family, PTHR46915:SF2 (UBIQUITIN-LIKE PROTEASE 4) (UniProt REST, retrieved 2026-10-21). The shared name "Ulp2" and the 2014 paper's "like S. cerevisiae Ulp2" comparison are name/sequence-resemblance statements, not orthology. Budding-yeast Ulp2 substrate- or locus-specific functions should not be transferred to O13769.
- The IBA rows come from PAINT node PTN002930416, whose donors are SENP6 (human/mouse), Senp7 (mouse), SENP7 (human), two Drosophila genes, and for cytoplasm pombe ulp2 itself. Ulp2 lies inside this clade. PAINT propagated deSUMOylation, SUMO-specific endopeptidase activity, nucleus and cytoplasm. Vertebrate SENP6-specific roles (kinetochore/CENP-A, SUMO2/3 chain specificity) were not propagated, and I treat that omission as deliberate.
- Closest experimentally well-characterised relative by phylogenetic placement: human SENP6 (Q9GZR1), a main IBD donor. Neither SENP6 nor SENP7 has a review in the repo.
- Family review interpro/panther/PTHR46896/PTHR46896-review.yaml lists ulp2 under SF3 as well; no disagreement about subfamily placement. Its deSUMOylase term assessment is UNRESOLVED in scope, which is compatible with this review.

### Changes vs the previous review
- GO:0005515 protein binding (IPI, eIF4G = tif471/SPAC17C9.03): KEEP_AS_NON_CORE -> REMOVE, following the protein-binding policy. The co-purification is real but generic.
- Nucleus HDA (PMID:16823372): its support previously cited only the 2014 paper. Added the UniProt curated location line, which cites PMID:16823372.
- Cytoplasm IBA: ACCEPT -> KEEP_AS_NON_CORE (minor pool; the activity is mainly nuclear). Cytoplasm dropped from core-function locations.
- Proteolysis / cysteine-type peptidase / Ubl peptidase IEA rows: MODIFY kept. Checked in OLS that GO:0016929 is_a GO:0008234 and GO:0019783. Proteolysis -> desumoylation is a lateral correction (GO:0016926 is under protein modification, not proteolysis).
- Stress granule IDA: stays UNDECIDED. I read every Ulp2 localisation sentence in the full text; the KCl stress-granule imaging uses eIF4G-HA, SUMO and PABP-RFP, and no Ulp2 granule image is described. Not removed, because the curator may have used supplementary data.
- Regulation of cytoplasmic translation EXP: UNDECIDED -> MARK_AS_OVER_ANNOTATED. With the full text in hand, the evidence is co-purification plus a pleiotropic cycloheximide sensitivity [PMID:24818994 "They are also sensitive to the protein synthesis inhibitor, cycloheximide (CHX, 10 and 20 µg/ml) and KCl (1 M) indicating that Ulp2 likely has roles in numerous cellular processes."]. No translation measurement is reported.
- Added PMID:27398807 to the references (genetic SUMO-chain/STUbL context) [PMID:27398807 "Therefore, unscheduled STUbL activity on SUMO-chain modified proteins, rather than the SUMO chains themselves, is toxic to ulp2∆ cells."]. No new GO annotations proposed: the genetic interactions are not participation evidence.
- Description rewritten to include the domain, triad, family placement and genetic context. New suggested questions/experiments added.

### Modules
- No module in modules/ references ulp2/O13769 or a SUMO deconjugation pathway.
