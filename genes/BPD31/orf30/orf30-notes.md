# orf30 / gp30 = AcrF2 (Q6TM72, Pseudomonas phage D3112) — curation notes

## Identity

Reviewed Swiss-Prot entry, 90 aa, `RecName: Full=Anti-CRISPR protein 30`, `AltName:
gp30`. Taxon NCBITaxon:2907964 (Pseudomonas phage D3112); natural host *Pseudomonas
aeruginosa* (`OH NCBI_TaxID=287`). InterPro IPR057728 "AcrF2", Pfam PF25704, CDD cd22280
AcrIF2 — so UniProt, InterPro, Pfam and CDD agree this is the AcrF2 (AcrIF2) family
exemplar, which is what `modules/anti_crispr_suppression.yaml` annoton
`acrif2_csy_blocker` assumes. The UniProt FUNCTION line is curator-asserted from the
discovery paper with an experimental code (`ECO:0000269|PubMed:23242138`,
"Allows the phage to evade the CRISPR/Cas system type I-F").

Four PDB entries place this exact accession in complexes: 5UZ9 and 6B47 (Csy complex with
AcrF2, cryo-EM), 5YHR (AcrF2 alone, 1.34 Å), 8DFS (a type I-C Cascade with AcrIF2).
RCSB primary citations resolve 5UZ9 to PMID:28340349 and 6B47 to PMID:28985564.

## Discovery

One of the original five anti-CRISPR genes
[PMID:23242138 "Here we describe the first examples of genes that mediate the inhibition of a CRISPR/Cas system. Five distinct 'anti-CRISPR' genes were found in the genomes of bacteriophages infecting Pseudomonas aeruginosa."],
[PMID:23242138 "Remarkably, expression of seven of these genes (Supplementary Fig. 7) led to dramatic increases in the plaquing efficiency of the CRISPR-sensitive phages"].
Two negative results from that paper bound the function usefully. First, the inhibitors
act after the surveillance complex has assembled, not on its biogenesis
[PMID:23242138 "We conclude from these experiments that the anti-CRISPR genes exert their effects at a step occurring after formation of the crRNA-Cas complex, and that there is no effect on biogenesis of either the crRNA or Cas proteins."],
which rules out any transcriptional or RNA-processing mechanism. Second, the specificity
is for type I-F and does not extend even to the closest relative, type I-E
[PMID:23242138 "Finally, we found that the anti-CRISPR genes did not inhibit a Type I-E CRISPR/Cas system functioning in E. coli"].

## Mechanism: the module's AcrF2 assignment holds, and can be sharpened

The module places gp30 in the `csy_complex_blocker_variant` and deliberately asserts **no
molecular function**, saying "no molecular function is asserted here because the specific
blocked surface is not established from the local evidence." **That caution is no longer
necessary — the blocked surface is established, and it is the DNA-binding site.**

Bondy-Denomy et al. showed by biochemistry that two of the three inhibitors they studied
block the DNA-binding activity of the Csy complex by contacting different subunits
[PMID:26416740 "Two block the DNA-binding activity of the CRISPR-Cas complex, yet do this by interacting with different protein subunits, and using steric or non-steric modes of inhibition."]
(abstract-only in cache; which of the two is AcrF2 is not resolvable from the abstract
alone, so this is used as supporting rather than defining evidence).

The cryo-EM structure settles it. Chowdhury et al. have a results section titled
[PMID:28340349 "AcrF2 is a DNA mimic"],
locate the protein at the DNA-binding site
[PMID:28340349 "AcrF2 is a small acidic protein wedged between positively charged residues in the N-terminal hook of Cas8 and the thumb of Cas7.6f"],
describe the mimicry physically
[PMID:28340349 "we did noticed a pseudo-helical display of acidic residues on the surface of AcrF2 mimics the negative charge distribution on the helical backbone of a DNA duplex"],
and conclude with a competition statement
[PMID:28340349 "these results suggest that AcrF2 is a double-stranded DNA mimic that blocks target recognition by competing for a critical DNA binding site"].
Their introduction gives the mechanism in one clause
[PMID:28340349 "by inserting between the Cas8f and Cas7f subunits in the tail (AcrF2), which prevents interactions with the t"]
(truncated in cache). The complementary Guo et al. structures add the conformational
consequence
[PMID:28985564 "AcrF2 binding wrenches the hook outwards away from the closed state"].
Yang & Patel's AcrIIA4 paper independently describes AcrF2 the same way
[PMID:28602637 "AcrF2 contacts the PAM-interacting region of Csy cascade through its negatively charged surface"],
and the AcrIIA4 NMR paper cites AcrF2 as the precedent for the acidic-patch mimicry
[PMID:29497118 "which was also found in AcrF2 proteins inhibiting the subtype I-F effector complex"].

**Consequence for the module.** The AcrF2 annoton should be moved from "mechanism not
established" to the same mimicry mechanism as AcrIIA4 and AcrIIA2, with the caveat that
the mimicked ligand is a dsDNA duplex approaching a multi-subunit surveillance complex
rather than a PAM duplex approaching a single effector. This is the strongest available
case that mechanism and not family is the right decomposition axis, since AcrF2 and
AcrIIA4 share no sequence relationship and attack different CRISPR classes, yet both work
by presenting acidic pseudo-DNA to a lysine-rich nucleic-acid-binding pocket.

## GOA rows and adjudication

Three IEA rows, all from `GO_REF:0000043` (Swiss-Prot keyword mapping), each traceable to
a specific keyword:

| term | keyword | adjudication |
|---|---|---|
| GO:0098672 symbiont-mediated suppression of host CRISPR-cas system | KW-1257 | **ACCEPT** — correct and maximally specific |
| GO:0052031 symbiont-mediated perturbation of host defense response | KW-0899 | **MODIFY** → GO:0098672 — redundant ancestor |
| GO:0039504 symbiont-mediated suppression of host adaptive immune response | KW-1080 | **MODIFY** → GO:0098672 — wrong branch |

GO:0052031 is a confirmed ancestor of GO:0098672. QuickGO ancestor query for GO:0098672
returns `["GO:0008150","GO:0098672","GO:0044419","GO:0044003","GO:0052031","GO:0044403","GO:0051701","GO:0035821"]`,
so the GO:0052031 row adds nothing the GO:0098672 row does not already imply. This is the
same call the completed AcrF8 review made when it modified the over-general GO:0052170 to
GO:0098672.

GO:0039504 is **not** an ancestor of GO:0098672, and its definition is squarely about
metazoan adaptive immunity — "an immune response based on directed amplification of
specific receptors for antigen produced through a somatic diversification process, and
allowing for enhanced response to subsequent exposures to the same antigen (immunological
memory)". *Pseudomonas aeruginosa* has no antigen receptors and no somatic
diversification. CRISPR-Cas is routinely called an adaptive immune system in the
literature, including in the papers cited here, and that loose usage is what the
Swiss-Prot keyword KW-1080 encodes; but the GO term means the vertebrate-style thing, so
the keyword-to-term mapping is a definitional mismatch rather than a biological
disagreement. MODIFY rather than REMOVE, because the essence (suppression of host
immunity by a symbiont) is sound and the correct term exists.

Note the module asserts both GO:0098672 and GO:0039504 for this annoton, citing GOA. The
GO:0039504 assertion should be dropped from the module on the above grounds.

## Not annotated

The module's parts 4 (Aca autoregulation) is not asserted for this gene: no *aca* gene has
been assigned to the D3112 locus in the evidence reviewed here, and the AcrF8-style
promoter-burst-then-repression regime is documented for the ZF40 locus, not this one.
