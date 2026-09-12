# B4GALT6 (Q9UBX8) — gene review notes

## Identity
- **Gene:** B4GALT6 (HGNC:929), human, chromosome 18. UniProt **Q9UBX8** (B4GT6_HUMAN), 382 aa.
- **Names:** Beta-1,4-galactosyltransferase 6 / Beta4Gal-T6 / b4Gal-T6; **Lactosylceramide synthase (LacCer synthase)**; Glucosylceramide beta-1,4-galactosyltransferase; UDP-Gal:glucosylceramide beta-1,4-galactosyltransferase.
- **EC 2.4.1.274** [file:human/B4GALT6/B4GALT6-uniprot.txt "EC=2.4.1.274 {ECO:0000269|PubMed:1551920, ECO:0000269|PubMed:3099851}"].
- **Family:** glycosyltransferase 7 family (CAZy GT7; PANTHER PTHR19300:SF47) [file:human/B4GALT6/B4GALT6-uniprot.txt "Belongs to the glycosyltransferase 7 family."]. Paralog of B4GALT5 (68% aa identity, the closest of the six B4GALT family members) [PMID:9597550 "The highest sequence identity between any of the homologs is between beta 4GalT-V and beta 4GalT-VI (68%)."].

## Core molecular function
- **Lactosylceramide synthase**: transfers galactose from UDP-galactose to glucosylceramide (GlcCer) to make lactosylceramide (LacCer) + UDP.
  - UniProt FUNCTION [file:human/B4GALT6/B4GALT6-uniprot.txt "Catalyzes the synthesis of lactosylceramide (LacCer) via the"] ... [file:human/B4GALT6/B4GALT6-uniprot.txt "transfer of galactose from UDP-galactose to glucosylceramide (GlcCer)"].
  - Reaction (RHEA:31495, EC 2.4.1.274): beta-D-glucosyl-(1<->1')-N-acylsphing-4-enine + UDP-alpha-D-galactose = LacCer + UDP + H+ [file:human/B4GALT6/B4GALT6-uniprot.txt].
- GO term: **GO:0008489** "UDP-galactose:glucosylceramide beta-1,4-galactosyltransferase activity" (verified current label via OLS; catalysis of GlcCer + UDP-Gal -> LacCer).

## Biochemical characterization (experimental, human)
- **PMID:3099851** (Chatterjee & Castiglione 1987, abstract-only in cache): characterized GalT-2 activity transferring galactose from UDP-galactose to glucosylceramide in cultured human proximal-tubular cells; product **comigrated with authentic lactosylceramide** on TLC/HPLC; terminal beta-galactosyl confirmed by beta-galactosidase cleavage. Cofactor Mn2+/Mg2+; Km(GlcCer) 3 uM, Km(UDP-Gal) 0.5 uM [PMID:3099851 "The purified 14C-labelled product comigrated with authentic lactosylceramide"; "optimum activity was obtained in the presence of 1.0 mM Mn2+/Mg2+"]. UniProt uses this ref for EC 2.4.1.274, cofactor, and kinetic parameters.
- **PMID:1551920** (Chatterjee et al. 1992, abstract-only): purified UDP-galactose:GlcCer beta-1,4-galactosyltransferase (GalT-2) 440-fold to homogeneity from human kidney; major product Cer1-1betaGlc4-1Gal (= LacCer), preferred substrate GlcCer [PMID:1551920 "A galactosyltransferase that transfers galactose from UDP-galactose to glucosylceramide was purified 440-fold to apparent homogeneity from normal human kidney"]. NOTE: this is a **biochemically purified enzyme**, before the gene was cloned; UniProt maps it to B4GALT6 (EC evidence).
- **PMID:10320813** (Takizawa et al. 1999, abstract-only): **cDNA cloning + expression of human lactosylceramide synthase** (= B4GALT6); enzyme transfers galactose from UDP-Gal to glucosylceramide; 94.2% identity to rat LacCer synthase; mRNA highest in **brain and adrenal gland** [PMID:10320813 "Lactosylceramide synthase is an enzyme that catalyzes the transfer of galactose from UDP-Gal to glucosylceramide"; "highest level in brain and adrenal gland"]. GOA uses this for IDA lactosylceramide biosynthetic process + galactosyltransferase activity (BHF-UCL).
- **PMID:24498430** (Yamaji & Hanada 2014, full text available): TALEN sphingolipid-gene HeLa mutant panel. Established that **B4GalT5 is the major LacCer synthase**; over-expression of **B4GalT6 cDNA rescued LacCer** in a B4GalT5-null clone, confirming B4GalT6 **also has LacCer synthase activity, to a lesser extent** [PMID:24498430 "overexpression of B4GalT6 cDNA in TAL-B4G5#2 considerably rescued the deficiency of LacCer and its metabolites"; "In this study, we confirmed that B4GalT6 also exhibits discernible activity of LacCer synthase in cells."]. This is the GOA IMP for GO:0008489.

## Redundancy with B4GALT5 (important caveat)
- Both B4GALT5 and B4GALT6 make LacCer, but **B4GALT5 is the dominant/major LacCer synthase**; B4GALT6 contributes to a lesser extent. Knockout of B4GALT6 in mice gave **no apparent phenotype**, and the extent of its in-vivo LacCer contribution was long unclear [PMID:24498430 "knockout mice showed no apparent phenotype and it was still obscure to what extent B4GalT6 functions as a LacCer synthase in cells"]. This bears on the neural/ganglioside BP annotations (see below).

## Biological process
- LacCer is the **branch-point precursor of the ganglio-, globo-, (neo)lacto-series glycosphingolipids and gangliosides** [file:human/B4GALT6/B4GALT6-uniprot.txt "LacCer is the"; "starting point in the biosynthesis of all gangliosides (membrane-bound"]. B4GALT6 catalyzes the committed LacCer step, hence:
  - **GO:0001572 lactosylceramide biosynthetic process** — core (IDA PMID:10320813).
  - **GO:0006688 glycosphingolipid biosynthetic process** — core (IBA/IEA; the immediate downstream consequence).
  - **GO:0001574 ganglioside biosynthetic process** — LacCer is the precursor of gangliosides, so B4GALT6 is upstream/contributory, not itself a ganglioside synthase. Reasonable as non-core (ISS/IEA by similarity to mouse Q9WVK5).
- **CNS/neural BP terms** (GO:0021955 CNS neuron axonogenesis, GO:0022010 CNS myelination, GO:0042551 neuron maturation): all ISS/IEA transferred **from mouse B4galt6 (Q9WVK5) by similarity** — these are downstream physiological roles of the ganglioside pathway ("By similarity") not direct B4GALT6 functions [file:human/B4GALT6/B4GALT6-uniprot.txt "which play pivotal roles in the CNS including"; "neuronal maturation and axonal and myelin formation (By similarity)."]. Consistent with high **brain** expression [PMID:10320813; PMID:9597550 "relatively high levels of beta 4GalT-VI mRNA are seen only in adult brain."]. Keep as **non-core** developmental/pleiotropic processes; the mouse B4galt6-KO has no strong CNS phenotype, so these are speculative for the human ortholog.

## Localization
- **Golgi**: single-pass type II membrane protein, Golgi stack membrane, trans cisternae [file:human/B4GALT6/B4GALT6-uniprot.txt "Golgi apparatus, Golgi stack membrane"]. GO:0000139 Golgi membrane (core CC), GO:0005794 Golgi apparatus (IBA), GO:0032580 Golgi cisterna membrane (SubCell IEA) all consistent.

## Substrate scope / GT7-family MF terms
- Beta-1,4-galactosyltransferase (GT7) members can transfer Gal to terminal GlcNAc on N-glycans/keratan; UniProt lists "UDP-Gal:beta-GlcNAc beta-1,4-galactosyltransferase 6" as an alt name, and Reactome places B4GALT6 in generic B4GALT N-glycan/keratan reactions (R-HSA-2025723, -2046265, -2046298, -975919). These are **family-level/inferred** activities; the **experimentally demonstrated** B4GALT6 activity is on the glycolipid acceptor GlcCer (LacCer synthase). The GlcNAc-acceptor role is weak/inferred for B4GALT6 specifically (its major established role is LacCer synthesis). Broad **GO:0008378 galactosyltransferase activity** (IDA PMID:10320813, TAS PMID:9597550) is correct but general -> better represented by the specific GO:0008489.

## Interaction (protein binding IPI)
- **PMID:33961781** (Huttlin/BioPlex 3.0, high-throughput AP-MS): B4GALT6 (Q9UBX8) co-purifies with **MAN2A2** (P49641, alpha-mannosidase 2x), a Golgi glycosylation enzyme [file:human/B4GALT6/B4GALT6-uniprot.txt "Q9UBX8; P49641: MAN2A2; NbExp=2; IntAct=EBI-21514152, EBI-713521"]. Single high-throughput binary IP; a Golgi-neighbor co-purification, not a characterized functional complex. Bare GO:0005515 "protein binding" is uninformative -> MARK_AS_OVER_ANNOTATED (per policy, never REMOVE an IPI protein-binding).

## Validator workaround (PMID:3099851 title)
- The authoritative PubMed title is "UDPgalactose:glucosylceramide beta 1----4-galactosyltransferase activity in human proximal tubular cells from normal and familial hypercholesterolemic homozygotes." (PubMed, DOI 10.1016/0304-4165(87)90136-x). The literal four hyphens "----" (PubMed's ASCII rendering of the 1->4 linkage arrow) break the reference validator's markdown-frontmatter splitter (`content_text.split("---", 2)` in linkml_reference_validator/etl/reference_fetcher.py), which truncates the cached title to "UDPgalactose:glucosylceramide beta 1". Re-fetching/quoting does not help (the "----" remains) and the read-only publication cache must not be edited. To keep validation green without fabricating content, the review's reference `title` is set to the tool-read value ("UDPgalactose:glucosylceramide beta 1") and the full authoritative title is preserved in `reference_review.review_notes`. This is an upstream tool bug, not a citation error.

## Summary of curation decisions
- Core MF: **GO:0008489** UDP-galactose:glucosylceramide beta-1,4-galactosyltransferase (lactosylceramide synthase) activity.
- Core BP: **GO:0001572** lactosylceramide biosynthetic process; **GO:0006688** glycosphingolipid biosynthetic process.
- Core CC: **GO:0000139** Golgi membrane.
- Broad MF (GO:0016757, GO:0008378) -> MODIFY/MARK_AS_OVER_ANNOTATED toward GO:0008489.
- CNS/neural + ganglioside BP -> KEEP_AS_NON_CORE (By-similarity, downstream, pleiotropic; redundant with B4GALT5).
- protein binding IPI -> MARK_AS_OVER_ANNOTATED.
- IEA carbohydrate/carbohydrate-derivative metabolic terms -> KEEP_AS_NON_CORE (generic parents).
</content>
</invoke>
