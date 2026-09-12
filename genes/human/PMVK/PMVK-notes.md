# PMVK (phosphomevalonate kinase, UniProtKB:Q15126) — review notes

## Deep research status
Falcon deep research is OUT OF CREDITS (HTTP 402); no `-deep-research-falcon.md` was
generated. This review is grounded in the UniProt record (`PMVK-uniprot.txt`), the seeded
GOA (`PMVK-goa.tsv`), and the cached publications in `publications/PMID_*.md` (all 12 GOA
PMIDs are present).

## Core biology
PMVK is phosphomevalonate kinase (EC 2.7.4.2), a 192-aa cytosolic enzyme of the
nucleoside-monophosphate (NMP) kinase family (P-loop fold). It catalyses the reversible,
ATP- and cation-dependent phosphorylation of (R)-mevalonate 5-phosphate to (R)-mevalonate
5-diphosphate (+ADP) — the step between mevalonate kinase (MVK) and diphosphomevalonate
decarboxylase (MVD) in the mevalonate/isoprenoid pathway.

- UniProt CATALYTIC ACTIVITY: "Reaction=(R)-5-phosphomevalonate + ATP = (R)-5-diphosphomevalonate + ADP; ... EC=2.7.4.2" [Rhea:16341].
- UniProt PATHWAY: "Isoprenoid biosynthesis; isopentenyl diphosphate biosynthesis via mevalonate pathway; isopentenyl diphosphate from (R)-mevalonate: step 2/3."
- [PMID:16519518 "Phosphomevalonate kinase (PMK) catalyzes a key step in isoprenoid/sterol biosynthesis, converting mevalonate 5-phosphate and ATP to mevalonate 5-diphosphate and ADP"] — recombinant human enzyme; monomer; kinetics both directions.
- [PMID:17902708 "Phosphomevalonate kinase (PMK) catalyzes the cation-dependent reaction of mevalonate 5-phosphate with ATP to form mevalonate 5-diphosphate and ADP, a key step in the mevalonate pathway for isoprenoid/sterol biosynthesis"] — Walker-A / basic-residue mutagenesis (K48, R73, R110, R111, R84, R141).
- [PMID:8663599] cloning of human liver PMKase; PMKase activity expressed in bacteria; sterol-regulated transcription; identified a C-terminal PTS-1 (Ser-Arg-Leu) but this is now known NOT to drive peroxisomal targeting.
- [PMID:9392419] PMKase (with MKase, MDDase) expressed in E. coli and assayed; only MKase (not PMKase) was feedback-inhibited by isoprene intermediates.

## Localization: cytosolic (peroxisomal claim retracted)
Early reports (rat, and PTS-1 motif reasoning) proposed peroxisomal localization
[PMID:10191291 "phosphomevalonate kinase is a peroxisomal protein which requires the
C-terminal peroxisomal targeting signal, Ser-Arg-Leu"]. This was overturned:
- [PMID:14729858 "We found an exclusive cytosolic localization of both endogenously expressed human phosphomevalonate kinase ... and overexpressed human phosphomevalonate kinase ... No indication of a peroxisomal localization was obtained."] — GOA uses this as NOT|peroxisome (IDA) and as cytosol (IDA).
- [PMID:27052676 "The wild-type PMVK exhibited dispersed cytoplasmic localization and showed little co-localization with the peroxisomal marker PEX14"; "PMVK and MVK were predominantly cytosolically localized"] — confirms cytosol.
- UniProt CAUTION: "Was originally thought to be located in the peroxisome (PubMed:10191291). However, was later shown to be cytosolic (PubMed:14729858, PubMed:27052676)."
- [PMID:14680974] shows cholesterol biosynthesis is normal in peroxisome-biogenesis-deficient fibroblasts (presqualene enzymes including PMK retain activity), arguing against obligate peroxisomal function.

The conflicting IDA peroxisome annotation from [PMID:17180682 "the pre-squalene segment of
the cholesterol biosynthetic pathway is localized to peroxisomes"] (Kovacs/Krisans) is the
minority view that the field and UniProt have since rejected. Per curation policy (do not
REMOVE an experimental IDA whose full text I cannot read), this is kept but marked
over-annotated with the contradicting evidence noted.

## Disease
Heterozygous loss-of-function PMVK variants cause autosomal-dominant porokeratosis
(POROK1) — a keratinization disorder — [PMID:27052676], [PMID:26202976]. This is a
downstream phenotype of impaired mevalonate-pathway flux in skin, not the molecular
function; not treated as a core function.

## Annotation decisions summary
- MF phosphomevalonate kinase activity (GO:0004631): multiple EXP/IDA + IBA + IEA/TAS — ACCEPT (core). IEA/TAS/IBA duplicates KEEP_AS_NON_CORE.
- ATP binding (GO:0005524) IDA [PMID:16519518]: ACCEPT (supports mechanism; ATP is the phosphate donor; Walker-A motif).
- BP isopentenyl diphosphate biosynthetic process, mevalonate pathway (GO:0019287): the most precise pathway BP — ACCEPT (core, matches UniProt PATHWAY step 2/3).
- BP cholesterol biosynthetic process (GO:0006695) / sterol biosynthetic process (GO:0016126): correct but downstream/broad — KEEP_AS_NON_CORE (cholesterol is one branch downstream of IPP).
- CC cytosol (GO:0005829) IDA/TAS: ACCEPT (core location). cytoplasm (GO:0005737) IEA: KEEP_AS_NON_CORE (broader parent).
- CC peroxisome (GO:0005777) IDA [PMID:17180682]: MARK_AS_OVER_ANNOTATED (contradicted by field/UniProt CAUTION; do not REMOVE experimental IDA).
- CC NOT|peroxisome (GO:0005777) IDA [PMID:14729858]: ACCEPT (correct negation).
- CC membrane (GO:0016020) HDA / extracellular exosome (GO:0070062) HDA: MARK_AS_OVER_ANNOTATED (large-scale proteomics; not a functional location for a cytosolic kinase).
- MF protein binding (GO:0005515) IPI [PMID:32296183]: MARK_AS_OVER_ANNOTATED (bare, uninformative HuRI Y2H hits; per curation policy, not REMOVE).
- BP response to cholesterol (GO:0070723) IEP [PMID:10191291]: KEEP_AS_NON_CORE (sterol-regulated transcription of the gene; regulatory response, not core enzymatic function).
