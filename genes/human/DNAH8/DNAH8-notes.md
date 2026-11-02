# DNAH8 notes

## Deep research
- `just deep-research-falcon human DNAH8` failed twice (Edison/FutureHouse API: "Failed to authenticate"). No deep-research file exists; literature was gathered directly from PubMed E-utilities (`DNAH8[tiab]`, 49 hits) and cached with `just fetch-pmid`.

## Identity and structure
- Gamma-type outer dynein arm (ODA) heavy chain; sperm paralog of DNAH5. 4490 aa; six AAA domains, stalk between AAA4 and AAA5, ATP P-loop at 1846-1853 [file:human/DNAH8/DNAH8-uniprot.txt "FT   BINDING         1846..1853"].
- Whitfield et al. classify DNAH8 as gamma-type [PMID:31178125 "γ-type: DNAH5 and DNAH8 and β-type: DNAH9, DNAH11, and DNAH17"]. Mouse Dnahc8 likewise [PMID:16054618 "Dnahc8, an axonemal gamma-type dynein heavy chain (gammaDHC) gene"]. (UniProt's AltName "Axonemal beta dynein heavy chain 8" is a legacy name.)

## Localization
- Sperm axoneme, not respiratory cilia [PMID:31178125 "We show that DNAH17 and DNAH8, but not DNAH5, DNAH9, or DNAH11, colocalize with α-tubulin along the sperm axoneme, whereas the reverse picture is observed in respiratory cilia"].
- Mouse: principal piece [PMID:16054618 "Interestingly, DNAHC8 is confined to the principal piece of the sperm tail."]; cytoplasm of primary spermatocytes (UniProt, by similarity to Q91XQ0) = preassembly stage.

## Disease / phenotype
- SPGF46, MMAF [PMID:32619401 "Dnah8-knockout male mice also presented typical MMAF phenotypes and sterility."]; independent: PMID:32681648, PMID:33704367, PMID:33611675, PMID:36308074.
- DNAH8 and DNAH17 are interdependent: DNAH17 lost in DNAH8-mutant sperm [PMID:32619401; PMID:36308074 "In addition, expression of DNAH17, a DNAH8-associated protein, was significantly reduced in the sperm flagella of the patients with the DNAH8 mutation."], and DNAH8 lost in DNAH17-mutant sperm [PMID:31178125; PMID:41549443].
- Non-axonemal reports (low confidence): AR regulator in prostate cancer [PMID:27363033 "we identified Dynein Axonemal Heavy Chain 8 (DNAH8) as an AR regulator"]; fetal testosterone/hypospadias in KO mice [PMID:41463044]. Not annotated.

## Annotation review decisions
- Core: minus-end-directed microtubule motor activity (IBA, accepted); outer dynein arm; sperm flagellum/axoneme.
- REMOVE dynein light intermediate chain binding (IBA + IEA): seeded only by cytoplasmic dynein 1 heavy chains; the ODA has no light intermediate chain, and DNALI1 (IDA subunit) is retained in DNAH17/DNAH8-null sperm [PMID:31178125].
- MODIFY generic dynein complex IEA -> outer dynein arm; NAS cilium-dependent cell motility -> flagellated sperm motility.
- NEW: flagellated sperm motility (GO:0030317). Comparator check: mouse Dnah1, Dnah7a/b/c, Dnah11 carry GO:0030317 in GOA.

## PANTHER / IBA
- GOA IBAs come from PTHR10676 nodes (PTN000743491 root; PTN002472868 gamma ODA HC; PTN008503977 sperm flagellum). UniProt's PANTHER xref places DNAH8 in PTHR46532:SF11 (named "DYNEIN AXONEMAL HEAVY CHAIN 12"), the same subfamily the DNAH12 review flagged. Despite this, human DNAH8 and mouse Dnah8 (Q91XQ0) receive the same 7 IBAs in QuickGO (checked 2026-10-14), so there is no human/mouse IBA gap for DNAH8.

## 2026-10-17 — consolidate duplicate sperm-motility coverage

The earlier standalone NEW GO:0030317 proposal duplicated the same term already proposed as the replacement for the imported GO:0060285/NAS/PMID:9373155 annotation. The functional participation argument remains supported: DNAH8 is a force-generating component of the sperm outer dynein arm. This correction removes only the redundant authored proposal and consolidates its unique supporting citations into that existing MODIFY review. All 27 genuine source annotations, their original identities, every other review decision, the integrated core, products and reference list are preserved. No additional verbatim excerpts were introduced; the earlier proposal remains available in the append-only Git/history record.

The prior PR #5009 approval remains part of the provenance. This correction addresses duplicate coverage, not a withdrawal of the positive motility evidence or a new completion-credit decision.

## 2026-10-17 — evidence for the sperm-motility refinement

DNAH8 supplies the heavy-chain motor component of the sperm outer dynein arm, which performs the work of flagellar movement. This participation rationale is more specific than observing infertility alone. The human localization study found DNAH8 along sperm axonemes but not the examined respiratory cilia; its mutation subjects had DNAH17 variants, so their phenotype is not relabeled as a DNAH8-variant experiment [PMID:31178125](https://pubmed.ncbi.nlm.nih.gov/31178125/). Separate DNAH8 studies report human sperm abnormalities and a Dnah8-knockout mouse phenotype [PMID:32619401](https://pubmed.ncbi.nlm.nih.gov/32619401/), [PMID:32681648](https://pubmed.ncbi.nlm.nih.gov/32681648/). These phenotypes support the sperm-flagellar requirement but are not purified motor-kinetics measurements. This bounded follow-up read the complete cached abstracts of these papers and the original NAS reference, without claiming a new reading of their full Methods [PMID:9373155](https://pubmed.ncbi.nlm.nih.gov/9373155/).

The previously stated comparator check is now supported by a genuine [QuickGO exact-term mouse query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO%3A0030317&goUsage=exact&taxonId=10090&limit=200&page=1), captured on 2026-10-17 and reused from the adjacent DNAH17 assessment. The first 200 of 458 records contain all five named examples. Dnah1 (E9Q8T7) and Dnah11 (E9Q7N9) include IMP records, whereas the recovered Dnah7a (E9Q0T8), Dnah7b (A0A571BD48/L7N1Y0), and Dnah7c (A0A087WR13) records are electronic. These establish positive annotation examples in the same motor-subunit role, not equally strong experimental support for every comparator or an independent proof of the human function. The remaining query pages and comparator primary papers were not inspected for this check.

The specific GO:0030317 process remains the replacement for the imported GO:0060285 NAS annotation, with the later human and mouse evidence attached explicitly to that review. A second authored NEW row would provide the same process coverage; removing it did not discard an imported experimental assertion or change the evidence code of the original NAS source. The GO:0060294 rationale now points to that existing replacement. The mouse knockout quotation has been moved from the broader row, and the prior human DNAH8 excerpt is restored at the specific process decision without repeating its separate findings excerpt. All prior journal text and histories are preserved.
