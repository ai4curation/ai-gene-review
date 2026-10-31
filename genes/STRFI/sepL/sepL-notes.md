# SepL review notes

## Identity and biochemical evidence

A0A2P1G6D3 matches AVM80395.1 from MF372757.1 over all 287 amino acids. The original name and cluster cross-reference remain present in UniProt. SepL plus SepB makes ADP-D-glycero-beta-D-manno-heptose, and SepL substitutes for E. coli GmhB with GmhA/HldE in the reciprocal assay. That establishes beta-heptose 1,7-bisphosphate C7 phosphatase function. It does not establish alpha-anomer phosphatase activity or a GDP-heptose pathway. sepL deletion reduces septacidin production in the heterologous cluster-expression host.

InterPro IPR004446 is the heptose-bisphosphate phosphatase signature; IPR036412/IPR006549/IPR023214 and Pfam PF13242 describe the HAD-family fold. IPR006543/NCBIfam Histidinol-ppas names do not override the assayed heptose substrate. PANTHER PTHR42891:SF1 is officially D-GLYCERO-BETA-D-MANNO-HEPTOSE-1,7-BISPHOSPHATE 7-PHOSPHATASE.

## Decisions

Three seeded rows: two MODIFY (specific precursor process and beta-C7 phosphatase) and one UNDECIDED (cytoplasm). The localization statement is ARBA-only in UniProt and the primary study assays recombinant protein, not native localization. No location is asserted in the core function. The broader phosphatase term remains true but is refined rather than removed. One core function represents the measured hydrolysis reaction.

## Research and source access

Manual primary-literature review on 2026-10-25. Falcon authentication failure and Perplexity/fallback exhausted credits were already established during this audit sequence; no redundant provider retries were made and no provider-branded research file was fabricated. The supported fetch pipeline seeded the review and publication caches. FEBA fitness lookup found no organism mapping/data for STRFI.

PMID:29483275, Tang et al. 2018, [publisher PDF](https://www.pnas.org/content/pnas/115/11/2818.full.pdf), was read in full through the web PDF reader, particularly Results pp. 2820–2821/Figures 3–4. The local cache remains abstract-only after supported refresh and warm attempts. Accordingly the YAML's verbatim quotation comes from the cached abstract; body-specific interpretation is explained in prose rather than represented as a cached quotation. The full_text_unavailable flag describes local cache availability, not absence of external inspection.

The study identifies the S. fimbriatus CGMCC 4.1598 cluster deposited as MF372757 and reconstructs its heptose precursor chemistry. Original gene deletions were tested in a heterologous S. albus J1074 host carrying the cluster, not automatically in the native producer. The enzyme reactions use recombinant purified proteins expressed in E. coli. Both systems must be distinguished from the organism of origin.

The original deposited CDS translations and current UniProt proteins were compared in [the reproducible identity analysis](../sepB/sepB-bioinformatics/RESULTS.md). This supports applying the primary assay to the exact accession despite current genome/gene relabeling. It does not independently verify the contents of physical assay plasmids.

## Pathway and stereochemistry

The experimentally reconstructed order is SepB isomerase → SepB kinase → SepL C7 phosphatase → SepB adenylyltransferase → SepC C6 epimerase. SepB/SepL generate ADP-D-glycero-beta-D-manno-heptose; SepC supplies ADP-L-glycero-beta-D-manno-heptose. This is precursor synthesis for the secondary metabolite septacidin in a Gram-positive actinobacterium, not evidence that this organism makes LPS.

The original paper's HygP result is distinct: HygP controls C2 and C3 stereochemistry and, with E. coli GmhB and HldE, produces the D-altro C3 epimer. The primary abstract names GmhA in that hybrid mixture, whereas the Results/Figure 4 show GmhB; the Results are followed here. Do not propagate the manno-specific SepB role to HygP or count HygP as an ordinary GmhA substitute.

PMID:32567317 (abstract inspected) demonstrates the downstream use of ADP-L-glycero-beta-D-manno-heptose by SepE in N6 glycosylation of AMP. This independently confirms the product's secondary-metabolite context, without substituting for evidence about the upstream enzymes.

## Ontology and curation scope

QuickGO term definitions were checked on 2026-10-25 for GO:0008968, GO:0033785, GO:0033786, GO:0034200, GO:0008712, GO:0097171, GO:0030246 and GO:0097367. GO:0097171 has nucleotide-sugar/carbohydrate-derivative biosynthesis ancestors, not an LPS-process ancestor. Its definition mentions the familiar LPS use of the same product but the named chemical biosynthetic process applies to the reconstituted septacidin precursor pathway. No LPS process is asserted.

No new broad downstream antibiotic biosynthesis term is proposed. Only the chemically established precursor pathway and exact enzyme functions are represented. Substrate use does not create an independent sugar-transport, lectin or host immune function.
