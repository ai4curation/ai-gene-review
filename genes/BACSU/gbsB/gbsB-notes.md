# gbsB evidence notes

2026-11-06. Annotation-reviewer and core-function-synthesizer consultation.

Identity: P71017, Bacillus subtilis strain168. The normal fetch was performed before curation; all original row payloads, complete pristine seed document and raw hashes are frozen in `.cache/module-audit-logs/choline-betaine-20261106/bacillus-baseline.yaml`. The Falcon command was attempted and failed HTTP403. These are manual notes, not an invented provider report.

PMID8752328 (Boch et al.,1996), full author-hosted article inspected: the JH642 locus was cloned by heterologous complementation; radiolabeled choline conversion was examined in JH642, a gbsB deletion and a gbsAB deletion. The gbsB mutant still uses betaine aldehyde, distinguishing the first oxidation from the second. Uptake remains intact in the mutants. This combines catalytic-family evidence, pathway dissection and flux, not necessity alone. Source: https://www.uni-marburg.de/de/fb17/fachgebiete/mikrobiologie/ag-bremer/pdf-fuer-publikationen/046.pdf.

The original U47861.1 record is explicitly JH642. Deposited GbsA/AAC44364.1 matches the entire frozen P71016 sequence. GbsB/AAC44365.1 is the393-aa short form, matching frozen P71017 after its first9 residues; translation of the same original DNA from the experimentally observed upstream start yields the entire402-aa canonical P71017. Both starts were observed in heterologous expression. This is a documented alternative initiation boundary, not evidence that the frozen canonical sequence has a wrong start. The original GenBank record, mapping and verification script are in gbsB-source-analysis.

PMID9297465 (Boch et al.,1997), full author PDF inspected: purified GbsA uses the original pJB009 JH642 clone in E.coliPD141, whose bet locus deletion avoids host BetB contamination. It directly oxidizes betaine aldehyde; NAD+ is strongly preferred over NADP+. Native homodimer assignment and soluble purification support cytoplasmic enzyme architecture. Source: https://www.uni-marburg.de/de/fb17/fachgebiete/mikrobiologie/ag-bremer/pdf-fuer-publikationen/051.pdf.

New GO0031456 glycine-betaine biosynthesis is justified because these proteins perform the oxidation chemistry. The term is a biosynthetic process and the local GO-CAM index contains neither accession. QuickGO comparator search found a current GO0031456 IBA for E.coliBetB/P17445 and none for BetA/P17444; the latter's older choline-specific process is discussed in its existing review. This is not a systematic absence across catalysts and is not the source of the biological claim. No redundant biosynthesis ancestor or generic osmotic-response BP is added. Cytoplasmic location is an explicit inference from soluble architecture and intracellular conversion, not a microscopy assay.

GbsB is a soluble typeIII alcohol-dehydrogenase-family protein, not a GMC/BetA homolog. QuickGO GO0008812 defines acceptor-unspecified choline oxidation (A + choline = AH2 + betaine aldehyde). RHEA33051 is the NAD-linked specialization and explicitly links to the more general RHEA17433. Therefore the same GO activity can cover structurally distinct BetA and GbsB implementations without asserting their electron acceptors are identical. Existing GO0004022 NAD-linked activity is accepted as a phylogenetic/curated inference, not a measured cofactor preference. The primary paper leaves the metal cofactor unclear and does not determine whether GbsB can also oxidize betaine aldehyde; neither specificity nor a second reaction is manufactured. The core uses acceptor-unspecified GO0008812.

## PR6108 round1 evidence and ontology follow-up

Replaced irrelevant GbsA support on GbsB core/process/location claims with the actual gbsB deletion precursor-rescue and radiolabeled-conversion passages, and the primary soluble-family statement. The reviewer suggested a GbsA homodimer quote for GbsB location; that would repeat the gene mismatch and is deliberately not used. Cytoplasmic localization remains an inference, not direct imaging. The metal uncertainty now quotes the primary sequence comparison and its explicit uncertainty. The description states the biology, while cofactor-evidence limits remain in review reasons and gaps.

All original machine and authored annotation payloads remain unchanged. Exact primary excerpts and source provenance are in BACSU/gbsB/gbsB-source-analysis/round1-primary-excerpts.txt; official term checks are in analysis/module_audits/bacterial_choline_to_glycine_betaine_biosynthesis/round1-ontology-evidence.yaml.

## PR6108 round2 follow-up

Remove one exact duplicate reference entry. Shorten five repeated native-genetics quotes to the operative differential precursor-rescue comparison. The complete original excerpt and its provenance remain unchanged at their existing shared path, preserving the radiolabeled-conversion context for both GbsA and GbsB. No biochemical or uncertainty judgment changes.
