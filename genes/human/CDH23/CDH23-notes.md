# CDH23 notes

## 2026-06-02

PITA context: CDH23 corresponds to PITA5 / pituitary adenoma 5, multiple types. UniProt notes that PITA5 includes GH-, PRL-, ACTH-, TSH-secreting and plurihormonal tumors and that familial transmission is consistent with autosomal dominant inheritance with reduced penetrance [file:human/CDH23/CDH23-uniprot.txt "PITA5 is consistent with autosomal dominant inheritance with reduced penetrance"].

Deep research status: `just deep-research-falcon human CDH23 --fallback perplexity-lite` timed out on Falcon after 600 seconds, and the fallback failed with a Perplexity quota error. I proceeded using fetched UniProt, GOA, and cached publications.

Functional summary: CDH23 is a cadherin-family adhesion protein whose best-supported normal function is in stereocilia/hair-bundle architecture. UniProt states that "Cadherins are calcium-dependent cell adhesion proteins" and that CDH23 is required for "proper organization of the stereocilia bundle" [file:human/CDH23/CDH23-uniprot.txt "Cadherins are calcium-dependent cell adhesion proteins."; file:human/CDH23/CDH23-uniprot.txt "proper organization of the stereocilia bundle of hair cells"]. Experimental evidence shows cadherin 23 is present in growing stereocilia and binds harmonin [PMID:12485990 "cadherin 23 are both present in the growing stereocilia and that they bind to each other"], and CDH23/PCDH15 maintain normal stereocilia bundle organization [PMID:15537665 "CDH23 and PCDH15 play an essential long-term role in maintaining the normal organization of the stereocilia bundle"].

Annotation decisions: I accepted cadherin adhesion, calcium binding, membrane/stereocilium localization, and sensory phenotypes as supported, with sensory phenotypes kept non-core where they are phenotype-level consequences. I removed the calcium ion transport annotation because the cited PMCA2 paper describes stereociliary calcium entry/export biology rather than CDH23 transporter activity [PMID:17234811 "Ca2+ enters the stereocilia of hair cells through mechanoelectrical transduction channels"; PMID:17234811 "exported back to endolymph by an unusual splicing isoform"].



## 2026-09-20 full annotation re-review

All 25 source rows, core functions and references were assessed; source fields were preserved. PTHR24026 IBDs were traced to PTN008601603 (adhesion, migration, beta-catenin binding, catenin complex, cadherin binding) and PTN004649584 (neuron-projection development). No matching repository or global OpenScientist report was found. Root received neutral questions for catenin interactions/complex, neuronal process and calcium processes; those require coordinated adjudication. No report was independently launched.

The old heterophilic-only/hair-cell-only exclusions are contradicted by target-cell studies. PMID:22413011 reports antibody and RNAi inhibition of human MCF-7 cell adhesion: “RNAi treatment significantly reduced the ability of MCF-7 cells to participate in homotypic adhesion.” Homotypic cells alone do not prove a homophilic molecular interface, but PMID:31729176 directly studies mouse NP_075859.2 EC1-2 trans-homodimers and a conserved binding interface, with human A549-cell adhesion tests. This ortholog construct scope is recorded explicitly. PMID:30747484 reports “silencing of Cdh23 expression resulted in decreased cell aggregation and enhanced cell migration.” These support restoring homophilic adhesion and retaining migration as secondary.

Beta-catenin remains a separate mechanistic question. PMID:12485990 reports absent consensus R1/R2 motifs and unpublished lack of catenin in growing hair bundles. PMID:22413011 and PMID:30747484 show beta-catenin-positive CDH23 cell contacts, but colocalization is not direct binding or proof of catenin-complex membership. These two IBAs are UNDECIDED; neuronal development is retained as non-core pending further mechanistic assessment because the inherited role is not refuted by sensory specialization.

The full PMID:17234811 results assay PMCA2 variants for calcium handling and examine CDH23 genetic variation in the deafness family. The paper states: “Whether the tripolar complex has any role in the function of PMCA2 is an open question.” The old claim that only a pump could participate in calcium transport was invalid; the two specific calcium processes are now UNDECIDED pending assessment of mechanical channel coupling and the original IMP interpretation.

PDZ2 binding is directly tested in PMID:12485990, supporting modification of generic protein binding to GO:0030165. PMID:22879593 explicitly describes exon68-dependent self-association and the C-terminal PDZ motif. Its full text remained unavailable after fetch and PMC browser attempts; only abstract-supported details are used. Human USH1 genetics (PMID:16679490) supports hearing, balance and retinal roles. The description and cores now distinguish extracellular cadherin interactions from intracellular PDZ-domain binding.

## Focused OpenScientist report incorporation (2026-09-20)

Read the complete catenin/neuronal/calcium report and checked its decisive claims against the already reviewed primaries. Its recurring statement that PMID:30747484 contains “zero occurrences” of catenin is false. The full Results describe puncta colocalizing with β-catenin; the Discussion states: “Using HEK293T cells expressing GFP‐labeled Cdh23, we demonstrated the formation of a homogeneous and continuous cell–cell junction by Cdh23 and its co‐localization with β‐catenin.” The same Discussion identifies a possible MAGI-1 bridge and reports no significant canonical β-catenin-pathway change after silencing (Fig. S8). None proves direct binding or a defined catenin complex; retain both UNDECIDED. The prior notes' attribution of colocalization to this paper was correct.

The report's missing classical motif/harmonin evidence remains a real mechanistic concern, but an alternate native linkage is not a universal negative binding assay. Its neuronal exclusion depends on missing target experiments and limited zebrafish retinal morphology/optokinetic assays, not a demonstrated loss of the human inherited developmental capacity; retain non-core. For calcium processes, the full PMID:17234811 PMCA2 assays and explicit open question remain decisive limitations; a structural component can do work in transport without being the pump. Both IMP process claims remain UNDECIDED. Mark the report DISPUTED, preserve its substantive evidence and require human source/mechanism follow-up rather than another duplicate report.


## Recovery PR localization follow-up (2026-09-22)

Preserve superseded donor-specific analysis where present, replace rebutted report passages with actual supporting evidence, and clarify location or process scope. PAINT rows support inherited assertions as phylogenetic judgments, not direct target experiments.
