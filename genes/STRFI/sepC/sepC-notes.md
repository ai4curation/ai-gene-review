# SepC review notes

## Identity and biochemical evidence

A0A2P1G6C1 matches AVM80386.1 from MF372757.1 over all 321 amino acids; current UniProt uses locus ACFPN6_36075. Purified recombinant SepC converts ADP-D-glycero-beta-D-manno-heptose into the L-glycero product, identified by HR-MS and chromatographic comparison against an HldD-generated standard (PMID:29483275, Results/Figure 3). The denatured protein extract contains tightly bound noncovalent NAD+. This target-specific cofactor result should not be replaced with NADP+ simply because a different HldD homolog uses NADP+.

The sepC deletion reduces but does not abolish septacidin in the heterologous S. albus cluster-expression host; the authors consider host epimerase compensation or downstream substrate tolerance. Thus a nonredundant essential role is not asserted.

PANTHER PTHR43103:SF3 is officially ADP-L-GLYCERO-D-MANNO-HEPTOSE-6-EPIMERASE; the parent PTHR43103 is NUCLEOSIDE-DIPHOSPHATE-SUGAR EPIMERASE. InterPro IPR001509, IPR036291 and Pfam PF01370 support the epimerase/NAD(P)-binding fold. Exact substrate and NAD+ assignment come from the experiment, not a domain label.

## Decisions and NEW participation check

The supported fetch produced zero seeded GO rows. Two conservative NEW annotations were added: the exact epimerase molecular function and ADP-L-glycero-beta-D-manno-heptose biosynthesis. The purified enzyme itself performs the final chemical step; it is neither a consumed substrate nor merely a factor necessary for another enzyme's activity. The process proposal rests on direct catalytic reconstitution, not on an argument that other module participants carry it. Its parents describe nucleotide-sugar biosynthesis rather than processing a protein substrate. No redundant ancestor/descendant process is proposed. One core function records the epimerase with its directly supported precursor process.

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

Comparator check: QuickGO annotation search on 2026-10-25 for exact GO:0097171 returned one annotation each for E. coli HldD P67910 and P. aeruginosa HldD Q9HYQ8. Both perform the same final epimerase role. Their annotation state checks the convention only; the SepC assay remains the evidence. The local GO-CAM index has no matching SepC accession entry.

## PR #5542 evidence follow-up, 2026-10-25

Added explicit family/domain support to both proposed annotation rows and the core function. The actual SepC record states `DR   PANTHER; PTHR43103:SF3; ADP-L-GLYCERO-D-MANNO-HEPTOSE-6-EPIMERASE; 1.` and `DR   Pfam; PF01370; Epimerase; 1.` The official subfamily label also matches the committed PANTHER ontology. These are independently computed classifications, not the unvetted submitter name or ARBA keywords.

The evidence chain has three distinct parts: full-length identity connects A0A2P1G6C1 to the deposited paper protein AVM80386.1; specific PANTHER membership and the broader Pfam epimerase domain support the enzyme-family assignment; the previously inspected full-paper reaction experiment supplies the direct substrate/product and cofactor interpretation. Neither sequence identity nor classification is relabeled as a direct assay. The cached abstract quotation still supports the SepB/SepL/SepC ensemble only; no body text was inserted into the publication cache or fabricated as a cached quote. The actions and two proposed GO terms are unchanged.
