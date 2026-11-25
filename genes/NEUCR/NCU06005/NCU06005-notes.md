# NCU06005: biological evidence

NCU06005 is a glycerol-kinase-family enzyme predicted to phosphorylate glycerol with ATP, producing sn-glycerol-3-phosphate. This reaction initiates glycerol assimilation and supplies an intermediate for carbon and glycerolipid metabolism. Classical Neurospora crassa enzymology identifies a cytosolic glycerokinase in the inducible glycerol-dissimilation pathway; the precise correspondence of that historical glp-4 activity to the modern NCU06005 locus and any additional mitochondrial pool remain unresolved.

- glycerol kinase activity: The glycerol-kinase-specific IPR005999 and PANTHER glycerol-kinase subfamily distinguish this enzyme from generic FGGY carbohydrate kinases. Classical N. crassa experiments establish glycerokinase-dependent glycerol utilization, grounding transfer of ATP-dependent glycerol phosphorylation; a modern target-specific purified assay was not recovered.
- mitochondrion: The mitochondrial IBA is an ancestral localization assertion at PTN000023394, but classical N. crassa enzymology identifies cytosolic glycerokinase and mitochondrial glycerol-3-phosphate dehydrogenase as separate activities. The historical glp-4 to NCU06005 mapping and any dual localization are not fully resolved, so the IBA is neither confirmed nor removed.
- carbohydrate metabolic process: Glycerol phosphorylation is the entry reaction of the experimentally characterized fungal glycerol-dissimilation pathway. Glycerol catabolism describes that established role more precisely than broad carbohydrate or glycerol metabolism.
- glycerol metabolic process: Glycerol phosphorylation is the entry reaction of the experimentally characterized fungal glycerol-dissimilation pathway. Glycerol catabolism describes that established role more precisely than broad carbohydrate or glycerol metabolism.
- glycerol-3-phosphate metabolic process: The kinase produces glycerol-3-phosphate directly, supporting its biosynthetic process rather than unspecified metabolism of that intermediate.
- triglyceride metabolic process: Glycerol kinase supplies glycerol-3-phosphate, a glycerolipid precursor, so the curated triglyceride-metabolism inference is a plausible downstream role. It does not make this enzyme a triglyceride synthase, and target lipid flux was not measured in the retrieved glycerol-utilization studies.
- kinase activity: The diagnostic glycerol-kinase family resolves the phosphoryl acceptor as glycerol and supports the specific kinase activity.
- phosphotransferase activity, alcohol group as acceptor: The diagnostic glycerol-kinase family resolves the phosphoryl acceptor as glycerol and supports the specific kinase activity.
- glycerol catabolic process: ATP-dependent glycerol phosphorylation both initiates glycerol catabolism and directly produces glycerol-3-phosphate. The specific family assignment and classical fungal glycerol-utilization enzymology support this process.
- glycerol-3-phosphate biosynthetic process: ATP-dependent glycerol phosphorylation both initiates glycerol catabolism and directly produces glycerol-3-phosphate. The specific family assignment and classical fungal glycerol-utilization enzymology support this process.

Primary evidence excerpts

- [file:NEUCR/NCU06005/NCU06005-uniprot.txt] “DR   InterPro; IPR005999; Glycerol_kin.”
- [PMID:6284716] “Evidence from the enzymatic characterization of these
mutants indicated that glp-2 and glp-4 were the structural genes encoding the
mitochondrial glycerol-3-phosphate dehydrogenase and cytosolic glycerokinase,
respectively.”

Provenance: live API snapshot 2026-09-09T03:00:51.831347+00:00. Complete API prediction JSON and all emitted claim IDs, text, and original evidence are preserved in the source and provenance JSON files. Current sequence/annotation data are separate comparison snapshots. Annotation overlap records known biology, not demonstrated training membership. All seven gene-focused Falcon jobs completed; the provider reports were inspected and useful primary leads checked. Publication retrieval used Europe PMC metadata/XML when the canonical PubMed fetch returned HTTP 429.

PMID:29563189 lists NCU06005 as glycerol kinase GLK-1 in a cold-sensitive mutant screen. This locus-level phenotype is not a purified kinase or localization assay. The old glp-4 name is not adopted without an authoritative locus mapping. Cytoplasm SL-0086 was emitted with string_match_text GO:0005739 (mitochondrion); the original mismatch is retained and the emitted location is assessed separately.

## 2026-10-01 re-review after GOA refresh

GOA/UniProt sources were refreshed; no new (PENDING) rows and no vanished GOA rows for this gene. Existing judgments were re-audited and retained. Added structured `propagation_review` to the two IBA rows that lacked it: the mitochondrion IBA (UNDECIDED; PTN000023394 node placement versus classical cytosolic glycerokinase fractionation left UNRESOLVED) and the glycerol metabolic process IBA (MODIFY to glycerol catabolic process; TERM_SCOPING_PROBLEM, node transfer itself sound).

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used. Evidence: UniProt record, GOA, PAINT rows for PTHR10196, the PTHR10196 family review, the falcon deep-research report, PMID:6284716 (abstract-only), PMID:17054397, and the yeast GUT1 review.

Identity: Q7S2F2 is the canonical (and only) UniProt entry for NCU06005, 584 aa, sequence version 3, Linkage Group VI. Not an isoform, fragment or alternative gene model; it carries the full FGGY_N/FGGY_C architecture and the glycerol-kinase-specific IPR005999/TIGR01311 signatures. New analysis (`NCU06005-bioinformatics/compare_sequences_rereview.py`, `RESULTS-rereview.md`): NCU06005 is the only N. crassa entry with EC 2.7.1.30 and one of only two PTHR10196 members (the other is xylulose kinase NCU11353, SF57).

Evolutionary grounding: PANTHER PTHR10196:SF69 (GLYCEROL KINASE) contains NCU06005 together with experimentally characterised S. cerevisiae GUT1 (P32190), A. thaliana GLPK and E. coli GlpK; mammalian GK is SF56. Pairwise identity is similar to all (46-51%), so GUT1 is chosen by subfamily and lineage (fungal SF69), not best hit. The glycerol kinase activity IBD sits at PTN000023392; the location and process IBDs at the eukaryotic node PTN000023394. The family review (interpro/panther/PTHR10196/PTHR10196-review.yaml) also places NCU06005 in SF69; no disagreement. It flags the cytosol IRD at PTN000023394 as LOSS_CONTRADICTED.

Locus identity: classical glp-4 (cytosolic, glycerol/cold/deoxyribose-inducible glycerokinase; linkage group VI; PMID:6284716) is best explained as NCU06005 (sole GK gene, same chromosome), but no molecular complementation is published.

Changes in this pass:
- mitochondrion IBA: MARK_AS_OVER_ANNOTATED -> KEEP_AS_NON_CORE. The SF69 sister seed Gut1p has an experimentally shown imported mitochondrial pool (PMID:17054397), and the 1982 Neurospora fractionation reports the main cytosolic pool without excluding a minor one. No target-specific evidence of loss, so the inheritance stands as a minor location; consistent with the GUT1 review and with the family review's call that the clade inherits both locations. propagation_review now NO_FAILURE_NON_CORE / SUPPORTS_TRANSFER.
- cytosol NEW: evidence code IDA -> IC, because the paper assayed the activity but did not identify the gene molecularly; attribution to NCU06005 is curator inference.
- Retained: glycerol kinase activity (IBA, IEA) ACCEPT; glycerol catabolic process ACCEPT; glycerol-3-phosphate biosynthetic process ACCEPT; kinase activity, phosphotransferase alcohol-acceptor, carbohydrate metabolic process, glycerol metabolic process, glycerol-3-phosphate metabolic process MODIFY to the specific descendants already carried; triglyceride metabolic process MARK_AS_OVER_ANNOTATED (mammal-specific SF56 physiology, precursor supply is not participation; same call as on GUT1).
- PMID:29563189 (cold-shock knockout screen) kept as LOW-relevance reference; organismal phenotype, not used as support.

Relative: yeast GUT1 (P32190), SF69 fungal ortholog-level relative; complete review exists at genes/yeast/GUT1/GUT1-ai-review.yaml. Modules: modules/glycerol_metabolism.yaml (yeast GUT1-GUT2 route); modules/bacterial_glycerol_uptake_catabolism.yaml (GlpK) is the bacterial counterpart.
