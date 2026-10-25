# ADP-heptose biosynthesis audit

## 2026-10-25: scope and literature

This audit covers the four reactions to ADP-D-glycero-beta-D-manno-heptose and the optional terminal C-6 epimerization to the L,D donor. Optionality is a generic module boundary, not a claim that an organism using the L,D product can omit its epimerase. GDP-alpha-heptose, ADP-altro-heptose, downstream glycosyl transfer and host ALPK1/TIFA signaling remain separate pathways.

Review literature searched: PMID12101286 (2002), PMID32591860 (2020/2021), PMID37317291 (2023). The latter two have accessible full text and supply comparative architecture, distribution and signaling context. PMID12101286 has no cached abstract/full text and is retained here as a searched lead, not used as mechanistic evidence. Review statements about hygromycin B are not evidence that its altro-heptose route is the same manno-heptose pathway. PMID29483275 explicitly distinguishes the stereochemistry.

Primary work establishes three implementations:

- PMID11751812 reconstructs the E. coli route with E. coli HldE/GmhB and **Aneurinibacillus thermoaerophilus GmhA**. Its abstract describes the E. coli pathway but should not be read as an all-E. coli purified-enzyme experiment. HldE domains catalyze nonadjacent phosphorylation and adenylylation steps; GmhB is needed between them. PMID18056714 independently supplies direct E. coli/P. aeruginosa GmhA structural evidence.
- PMID23256532 characterizes standalone Burkholderia HldA kinase. PMID28177319 identifies the complementary HldC adenylyltransferase architecture; PMID33733972 uses beta-glucose-1-phosphate as an assay surrogate, not native-heptose kinetics. Exact RCSB/native protein sequence checks are recorded in the two gene notes.
- PMID29483275 reconstructs the Gram-positive Streptomyces fimbriatus route with SepB/SepL/SepC for septacidin. SepB combines isomerase, kinase and adenylyltransferase domains. Original MF372757 CDS translations were matched exactly to current UniProt records in the SepB bioinformatics analysis. PMID34632535 finds kinase-deficient related tridomain proteins: architecture cannot substitute for functional evidence.

The initial bacterial envelope was revised after the cross-kingdom evidence described below. Bacterial examples span proteobacteria and actinobacteria. No evolutionary origin at the bacterial ancestor or absence outside sampled lineages is inferred. Family groundings preserve official names even where a name is misleading: PTHR30390:SF6 is named for DiaA but contains experimentally demonstrated isomerases; PTHR46969:SF1 is named bifunctional HldE but contains standalone HldA. Required-function constraints distinguish the relevant reaction from the family label. Exact substrate and domain evidence determine function.

All seven original representatives are retained. Five bacterial additions cover split Burkholderia HldA/HldC and Streptomyces SepB/SepL/SepC; four further archaeal members extend the scope. This is sampling across pathway architectures, not a claim that these 16 proteins exhaust pathway diversity. PSEPK GmhB Q88RS0 has direct substrate profiling in PMID25848029; PSEAE HldD is supported by curated family/orthology evidence and is not described as a directly assayed PA3337 protein.

The GmhB reaction remains required even where a gmhB deletion has a partial phenotype. PMID32591860 discusses alternative phosphatase activity; a redundant enzyme can preserve a chemical reaction without making that reaction dispensable. No unknown backup protein is assigned a family or representative.

GO-CAM index was searched for all 16 accessions on 2026-10-25; no matching cached activities were found. Overlapping PR5076 adds ancestral nodes/label normalization for this module but does not supply the present literature/taxon/member audit. The exact ancestry claims in that PR have not been imported without verification.

Provider-generated research was attempted for member reviews; authentication/quota failures and failed fitness retrievals are recorded in individual notes. Manual literature review and independently fetched primary publications support the audit. No source cache was edited manually.

### Cross-kingdom update

PMID39116220 (2024) and author commentary PMID39558531 extend the enzyme repertoire beyond bacteria. The primary paper expressed four heptose-biosynthesis genes from Methanococcus maripaludis DSM2067 in an HBE-negative M. maripaludis S2 host. The resulting ADP-heptose demonstrates the function of the introduced archaeal enzyme set; it does not establish an endogenous pathway in unmodified S2. The commentary compresses this distinction, so the primary experiment governs the module claim. Bacteria plus Archaea is the current complete-route envelope; no universal occurrence is inferred.

Viral and eukaryotic enzymes have biochemical activity but the surveyed complements lack all four necessary genes. A replacement phosphatase is proposed rather than demonstrated. These partial capabilities are distinguished from a verified native complete pathway. CDP- and UDP-heptose production by promiscuous nucleotidyltransferases is a neighboring reaction scope; this module specifically follows the ATP/ADP-heptose route. All four archaeal member reviews are complete. The kinase matches PP708527.1 exactly; the other three preserve qualified family/domain and genomic-context inference without claiming exact construct identity.

### Completed curation and validation scope

All 16 representatives have individual reviews. The 12 bacterial reviews adjudicate 105 original rows and add two direct-assay SepC annotations; seven claims remain UNDECIDED. The four archived archaeal accessions return zero current GOA annotations. Each therefore has an evidence-backed specific core function, without manufactured existing rows or ND claims. Their absence from the live reference-proteome set is not interpreted as biological absence.

Archived records are fetched by `genes/METMI/gmhA1/gmhA1-bioinformatics/fetch_archived_genes.py`: it pins official UniSave versions and uses the ordinary repository pipeline for GOA and review seeding. Source URLs, release dates, version numbers and hashes are retained. The separate `hldE_2-bioinformatics` workflow compares original GenBank construct translations with the archived proteins, with no approximate-match substitution.

The protein architectures listed here are examples; the later paper also describes HldF isomerase/nucleotidyltransferase and HldG phosphatase/nucleotidyltransferase fusions. ATP use does not imply exclusion of CTP/UTP. Archaeal L,D-heptose formation or HldD activity was not demonstrated by the four-gene reconstruction; epimerase absence is not inferred.


### PR5542 follow-up

Deduplicated repeated evidence entries and made the kinase/adenylyltransferase family description explicit: PTHR30390:SF6 is present for the multifunctional SepB protein, not for standalone GmhA/DiaA enzymes, which do not satisfy the required-function constraint. Archaeal GmhB beta-substrate competence is now explicitly inferred from the actual PANTHER subfamily plus pathway context; anomer preference/exclusivity and construct identity remain unverified. Four E. coli GmhB MODIFY rationales now explain their individual terms and replacements. SepC evidence additionally combines its specific epimerase-family membership with sequence identity and the primary per-enzyme interpretation.
