# IRAK3 notes


## 2026-09-08 paired human–horse review



IRAK3, also called IRAK-M, is an IRAK-family pseudokinase that regulates Toll-like and interleukin-1 receptor signaling. It participates in receptor-associated signaling assemblies and restrains inflammatory activation by stabilizing MyD88-associated IRAK complexes. Its death domain and kinase-like domain mediate protein interactions, and its effects depend on cellular context and stimulus history.

## Pseudokinase scaffolding and context-dependent signaling

The 1999 discovery study observed negligible autophosphorylation yet restoration of an IL-1 response in IRAK-deficient cells. The 2002 genetic study established physiological negative regulation: IRAK-M prevents IRAK/IRAK4 release from MyD88 and restricts cytokine induction and endotoxin sensitivity. The 2021 human structure explains a noncanonical inactive catalytic site, a distinctive homodimer and a possible IRAK4-interaction surface. ATP-pocket retention or weak nucleotide binding cannot establish active kinase catalysis. The positive cell-reconstitution result and inhibitory physiological feedback should coexist in the synthesis rather than being flattened into an unconditional activator or inhibitor. The selected horse N-terminal deletion reaches its death-domain start, so receptor-complex assembly needs specific checking.

## Decisive inspected evidence

From [PMID:12150927](https://pubmed.ncbi.nlm.nih.gov/12150927/):

> We show here that IRAK-M is induced upon TLR stimulation and negatively regulates TLR signaling. IRAK-M prevented dissociation of IRAK and IRAK-4 from MyD88 and formation of IRAK-TRAF6 complexes.

## Evidence inventory

- [PMID:10383454: IRAK-M is a novel member of the Pelle/interleukin-1 receptor-associated kinase (IRAK) family.](https://pubmed.ncbi.nlm.nih.gov/10383454/). [DOI:10.1074/jbc.274.27.19403](https://doi.org/10.1074/jbc.274.27.19403). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:12150927: IRAK-M is a negative regulator of Toll-like receptor signaling.](https://pubmed.ncbi.nlm.nih.gov/12150927/). [DOI:10.1016/s0092-8674(02)00827-9](https://doi.org/10.1016/s0092-8674(02)00827-9). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:33238146: Dimeric Structure of the Pseudokinase IRAK3 Suggests an Allosteric Mechanism for Negative Regulation.](https://pubmed.ncbi.nlm.nih.gov/33238146/). [DOI:10.1016/j.str.2020.11.004](https://doi.org/10.1016/j.str.2020.11.004). Full text is available in the repository cache.

## Transfer to the selected horse protein

The exact target is [A0A3Q2HDT6](https://www.uniprot.org/uniprotkb/A0A3Q2HDT6/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/IRAK3/IRAK3-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: cytokine-mediated signaling pathway, cytoplasm, magnesium ion binding, negative regulation of MAPK cascade, negative regulation of protein catabolic process, nucleus, plasma membrane, positive regulation of canonical NF-kappaB signal transduction, positive regulation of cytokine production, positive regulation of immune system process, protein binding, protein heterodimerization activity, protein phosphorylation, response to exogenous dsRNA, response to virus. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 outputs were not opened or used.

**Identity.** Benchmark accession Q9Y616 is the reviewed canonical human IRAK3 (IRAK-M), 596 aa, isoform 1 (displayed). It is not a fragment or alternative gene model: death domain (41-106), pseudokinase domain and C-terminal TRAF6-binding region are all present. PANTHER PTHR24419:SF7 (IRAK3 subfamily).

**Pseudokinase status.** The HRD catalytic motif is replaced by CGS (Ser-293) and the DFG by DFA, conserved across 134 vertebrate orthologues; MgCl2 and Mg-ATP give no thermal shift, ATP binds weakly (Kd ~196 uM) [PMID:33238146 "MgCl2 and ATP did not induce significant thermal shifts in IRAK3"]. The 1999 paper itself reports "only a negligible autophosphorylation activity" [PMID:10383454]. Kinase activity, protein phosphorylation and Mg binding rows were therefore REMOVED as contradicted (not merely unverified). ATP binding kept non-core. A guanylate cyclase activity has been proposed [PMID:31664109 "We demonstrate that wildtype IRAK3 is capable of producing cGMP."] but is not corroborated; recorded as a question, not annotated.

**Mechanism.** IRAK3 binds MyD88/IRAK-4 via death-domain Trp74 [PMID:38268724], transiently binds phosphorylated IRAK4 kinase domain via its pseudokinase domain [PMID:33238146], prevents IRAK1/IRAK4 release from MyD88 [PMID:12150927], and forms an IRAK-M myddosome driving MEKK3-dependent second-wave NF-kB that induces inhibitory genes (SOCS1, SHIP1, A20, IkBa) [PMID:23376919]. Net function: TLR/IL-1R negative feedback. IL-33/PIN1 context gives nuclear translocation and positive gene induction in DCs [PMID:29686383].

**Evolutionary grounding.** Mouse Irak3 (Q8K4B2; source of ISS/Compara rows) is the orthologue in the same PANTHER subfamily SF7, so the mouse knockout regulatory phenotypes transfer. Catalytic terms from IRAK1/IRAK4 subfamilies do not transfer. IBA node PTN000701353 (Pelle/Tube donors) gives GO:0008063 Toll signaling pathway, which is defined by the Drosophila Toll receptor: marked over-annotated (vertebrate TLR/IL-1R terms already present). Plasma membrane IBA from the same node kept non-core.

**Actions:** ACCEPT 31, KEEP_AS_NON_CORE 20, MODIFY 13, REMOVE 7, MARK_AS_OVER_ANNOTATED 4.

**Relative.** Closest experimentally characterised relative: mouse Irak3 (Q8K4B2), same PANTHER subfamily SF7; no review in repo (genes/mouse/Irak3 absent).

**Family review.** interpro/panther/PTHR24419 places Q9Y616 in SF7, consistent with UniProt; its protein kinase activity assessment is UNRESOLVED, which agrees with removing kinase activity for IRAK3. No placement disagreement.

**Modules.** No module lists IRAK3 as a part; relevant pathway modules: modules/il1_signaling.yaml, modules/toll_like_receptor_signaling.yaml, modules/tlr4_md2_lps_signaling.yaml, modules/tlr2_heterodimer_lipopeptide_signaling.yaml.
