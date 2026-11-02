# CG8915 evidence notes

Q9VX63 is the 976-residue native PA/PB sequence of [FBgn0030833](https://flybase.org/reports/FBgn0030833); the current two protein products are identical. All seven exact-accession GOA rows are reviewed. Original ProtNLM GO, name, score, and donor metadata are preserved in the source JSON.

The [sequence analysis](CG8915-bioinformatics/RESULTS.md) compares CG8915 with human YTHDC2/Q9H6S0 and the divergent fly Bgcn/Q9W1I2 control. CG8915 retains P-loop GATGSGKST and DEAH motifs, whereas Bgcn has different residues at both aligned regions. The analysis supports catalytic competence without conflating the two fly genes. It does not reconstruct their full phylogeny.

[PMID:29033321](https://pubmed.ncbi.nlm.nih.gov/29033321/) reports: “Our biochemical studies indicate that YTHDC2 is an RNA-induced ATPase with a 3'→5' RNA helicase activity.” This is mammalian evidence supporting the manual ISS transfer, not direct CG8915 enzymology. [PMID:29360036](https://pmc.ncbi.nlm.nih.gov/articles/PMC5832417/) is cached with full text. Its statement that Drosophila retained only Bgcn conflicts with the current CG8915/YTHDC2 database correspondence; its main text does not name CG8915. The preserved target motifs prevent simply assigning Bgcn's pseudohelicase mechanism to CG8915. A broader phylogenetic study would be needed to reconcile family sampling. No methyladenosine-reader, meiotic or nuclear-location annotation is adopted on this basis.

Falcon completed and was inspected. It found no target biochemical assay and emphasized broad helicase-domain inference, but did not inspect the exact motifs or the current target-specific manual ISS transfer. Those additional checks justify conserved catalytic-function inference. Its sensory-organ-precursor expression and wing-screen leads do not establish a separate molecular function. The ProtNLM nucleic-acid-binding claim is LSP independently of the finer catalytic or evolutionary uncertainties.

The PTHR18934 PAINT export places both broad RNA binding and broad helicase activity at PTN008360424. Both transfers are compatible with CG8915's retained helicase/RNA-binding architecture. The helicase row still merits MODIFY because the FlyBase ISS from human YTHDC2, CG8915's placement in PTHR18934:SF213 and the conserved CG8915 motifs support the more informative 3'-5' RNA helicase activity term; no PAINT node currently makes that exact assertion for CG8915.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: re-examined all seven GOA rows, the description and the core function against the cached literature (PMID:29033321 abstract; PMID:29360036 full text), the FlyBase report, the PTHR18934 PAINT export and new domain-level sequence analysis. No ProtNLM2 output was consulted.

Identity: Q9VX63 is the full-length canonical product of CG8915 (FBgn0030833; 976 aa; PA/PB identical). It is not a fragment, isoform or alternative gene model.

Evolutionary placement:
- UniProt and the PANTHER entry inventory place CG8915 in PTHR18934:SF213 ("3'-5' RNA HELICASE YTHDC2"). Human YTHDC2 (Q9H6S0), mouse Ythdc2 (B2RR83), Arabidopsis DExH6/HVT1 (F4INY4) and fly Bgcn (Q9W1I2) are in the same subfamily. FlyBase DIOPT gives YTHDC2 as the best bidirectional human ortholog (9/14 methods).
- PAINT: RNA binding and helicase activity are placed at PTN008360424, a deep DEAH node. Bgcn's NOT helicase activity is an IRD at its own node (PTN000433935, taxon 7227) and does not cover CG8915. No PAINT node places 3'-5' RNA helicase activity on SF213. GO:0034458 is placed only at PTN000433948, a different (splicing-helicase) branch.
- New analysis (`CG8915-bioinformatics/RESULTS-rereview.md`, `domain_coverage_rereview.py`; it reuses the existing alignments and changes no original file): CG8915 covers the YTHDC2 R3H (96%) and both helicase lobes (97-100%, about 43% identity). It covers only 12-21% of the YTHDC2 ankyrin-repeat insertion and none of the YTH domain. The CG8915 inter-lobe linker is about 60 aa, compared with about 240 aa in YTHDC2.
- PMID:29360036 describes, in non-Drosophila Schizophora, a "second YTHDC2 homolog that lacks the YTH domain but that, unlike Bgcn, has intact R3H and helicase motifs I and II". It states that Drosophila lacks this homolog. CG8915 has that architecture without the ARD, which the authors use as the family diagnostic. This probably explains why their search missed it. The paper's claim stays DISPUTED, not refuted, until a phylogeny that includes CG8915 is done.

Annotation decisions changed:
- GO:0016787 hydrolase activity (IEA): replacement changed from 3'-5' RNA helicase activity to GO:0016887 ATP hydrolysis activity. In current GO, GO:0034458 sits under helicase -> ATP-dependent activity and isomerase activity, not under hydrolase activity (checked with OLS hierarchicalAncestors), so the earlier replacement was not a refinement of the row.
- The other actions are unchanged: nucleotide binding -> ATP binding (MODIFY); nucleic acid binding -> RNA binding (MODIFY); RNA binding IBA (ACCEPT); helicase activity IBA -> 3'-5' RNA helicase (MODIFY); ATP binding (ACCEPT); 3'-5' RNA helicase ISS (ACCEPT, core). Their reasons were rewritten to state explicitly that no m6A-reader (YTH) or ARD-dependent (for example XRN1 or MEIOC-type partner) function is transferred.
- Not proposed: no localization, meiosis, germline-differentiation or m6A-related terms. YTHDC2's meiotic phenotypes and Bgcn's Bam-partnered translational repression depend on domains or partnerships that CG8915 has not been shown to share. Bgcn is also catalytically dead, so its mechanism cannot be transferred.
- The description now mentions maternal deposition and primordial-germ-cell expression (FlyBase, BDGP in situ). This is descriptive only, with no GO term.

Relative to review next: human YTHDC2 (Q9H6S0), in the same PANTHER subfamily SF213, is the ISS donor and the DIOPT best bidirectional ortholog. There is no review of it (human or mouse) in genes/. The family review interpro/panther/PTHR18934/PTHR18934-review.yaml agrees with SF213 placement; its only representative member is CG8915. No module covers this gene.
