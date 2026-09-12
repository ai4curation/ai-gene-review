# ITIH4 review notes

## Scope and provenance

- Target: human ITIH4, UniProtKB Q14624.
- `just fetch-gene human ITIH4` seeded 15 GOA annotation groups and 13 source references.
- `just fetch-gene-pmids human ITIH4` cached all 10 PMID sources named by GOA.
- Automated deep research was attempted with Falcon and the configured Perplexity Lite fallback. Falcon failed with HTTP 402 (Edison payment required), and the fallback failed with HTTP 401 (quota exceeded). No provider-named research file was produced; the manual synthesis is in `ITIH4-deep-research-manual.md`.
- Reviewed evidence: the Q14624 UniProtKB record, all GOA source publications, the Reactome event, and additional direct biochemical papers (especially PMID:33523981).

## Protein identity and architecture

ITIH4 is a 930-aa liver-produced secreted plasma glycoprotein. The original cDNA study identifies a 28-residue signal peptide and liver-restricted transcript [PMID:7775381, "The N-terminal 28 residues corresponded to a signal peptide for secretion."] The reviewed UniProt record assigns a signal peptide at residues 1-28, a VIT domain at 29-148, a von Willebrand factor A domain at 272-432, a proline-rich kallikrein-sensitive region, and mature 70-kDa and 35-kDa chains [file:human/ITIH4/ITIH4-uniprot.txt, "FT   SIGNAL          1..28"; "FT   DOMAIN          272..432"; "FT   CHAIN           689..930"].

The H4 member differs functionally from the bikunin-linked ITIH1/2/3 heavy chains. Purified GP120/ITIH4 contains no bikunin sequence, and neither chondroitinase nor alkaline treatment changes its mass [PMID:7541790, "Since GP120 showed no bikunin sequence, and chondroitinase treatment and alkaline treatment of GP120 did not affect its molecular weight, we concluded that GP120 was not a complex with bikunin."]. The modern mechanistic study explains that ITIH4 lacks the C-terminal consensus required for bikunin-heavy-chain complex formation and therefore is not incorporated into proteoglycan complexes [PMID:33523981, "ITIH4 lacks a C-terminal consensus sequence, which is present in all other ITIHs, that is required for the formation of bikunin-ITIH complexes. Consequently, ITIH4 is not incorporated into proteoglycan complexes and presumably functions independently of the other protein family members"]. This directly argues against transferring hyaluronan-metabolism biology from other ITIH heavy chains to ITIH4.

## Core molecular function

The strongest direct evidence is PMID:33523981. ITIH4 is cleaved in a protease-susceptible region by MASP-1, MASP-2, plasma kallikrein, and other proteases. Cleaved ITIH4 forms divalent-cation-dependent, noncovalent inhibitory complexes through its VWA domain. These complexes sterically restrict access of large protein substrates while leaving small-substrate catalysis possible [PMID:33523981, "This complex formation leads to protease inhibition by physically preventing cleavage of larger substrates, although the catalytic sites of the proteases remain active."]

The paper directly demonstrates serine-type endopeptidase inhibition: ITIH4 suppresses MASP-1/2 cleavage of protein substrates, MASP-2 cleavage of C2 and C4, and kallikrein cleavage of high-molecular-weight kininogen [PMID:33523981, "In summary, ITIH4 inhibited the activity of both MASP-1 and MASP-2 against two distinct, highly-relevant protein substrates but not against smaller peptide substrates."; "ITIH4 inhibits cleavage of HMWK by plasma kallikrein."]. The MF term GO:0004867 is therefore correct even though its current GOA evidence is an InterPro IEA.

ITIH4 also directly inhibits lectin-pathway complement activation in serum [PMID:33523981, "ITIH4 efficiently and dose-dependently inhibited C4 and C3 deposition"]. This supports new BP annotations GO:0001869 (negative regulation of complement activation, lectin pathway) and GO:1900004 (negative regulation of serine-type endopeptidase activity).

Earlier work correctly characterized ITIH4 as a kallikrein substrate rather than as the bikunin-containing inter-alpha inhibitor complex [PMID:7947966, "A 120 kDa plasma protein, which is susceptible to plasma kallikrein, was purified from human plasma"]. Being a substrate does not contradict the later bait-and-trap inhibitory mechanism; cleavage is required for inhibitory complex formation.

## Regulation and contextual biology

ITIH4 is a type II acute-phase protein. Its serum concentration rises 1.4- to 3-fold in several acute-phase settings, and IL-6 induces ITIH4 mRNA and secreted radiolabeled protein in HepG2 cells [PMID:10486281, "The results presented here indicate that ITIH4 is a type II acute-phase protein in humans."]. This supports the existing response-to-cytokine and acute-phase-response annotations as real but non-core regulatory/context annotations.

PMID:19263524 reports that circulating ITIH4 was depleted in acute ischemic stroke and returned toward normal during recovery [PMID:19263524, "The ITIH4 protein was completely absent in AIS patients as compared to those in the control group, and serum levels returned to normal in AIS patients as their condition improved."]. Its conclusion that ITIH4 is anti-inflammatory is consistent with later complement/protease inhibition but is not itself a mechanistic demonstration.

PMID:16271702 directly shows binding of the ITIH4 C-terminal fragment to the SANT2 domain of DNAJC1/MTJ1, co-immunoprecipitation from liver, and protection against kallikrein processing in vitro [PMID:16271702, "ITIH4 and MTJ1 co-immunoprecipitate from total liver protein extracts and SANT2 protects the ITIH4(588-930) recombinant fragment from being processed by kallikrein in vitro."]. The generic GO:0005515 annotation is uninformative and should be marked over-annotated rather than used as a core function.

## Localization evidence

- Direct plasma purification, an N-terminal signal peptide, and increased labeled ITIH4 in HepG2 culture medium establish a soluble extracellular-space pool [PMID:7947966, "A 120 kDa plasma protein, which is susceptible to plasma kallikrein, was purified from human plasma"; PMID:10486281, "This effect correlates with the increase of radiolabeled ITIH4 in the cellular media"]. The three broad extracellular-region annotations should be modified to GO:0005615 extracellular space.
- Two ECM-enrichment proteomics studies detect ITIH4 in ECM-associated fractions. These HDA localizations are retained as non-core contexts, but ITIH4 is not a bikunin-linked structural HA heavy chain.
- Exosome and plasma-microparticle HDA annotations are retained as non-core proteomic detections. The EPS-urine exosome paper explicitly warns that some detected proteins may be soluble [PMID:23533145, "some of these proteins could also exist as a soluble form."]. This is particularly relevant for abundant plasma ITIH4.
- Reactome explicitly places residues 29-661 in the platelet dense-granule lumen and exports them to extracellular region in R-HSA-481009, but the cached event's literature does not document ITIH4-specific dense-granule evidence. The dense-granule localization remains undecided rather than being overruled.

## Annotation decisions

1. GO:0004867 serine-type endopeptidase inhibitor activity, IEA: **ACCEPT**, independently validated by direct biochemical evidence.
2. GO:0005576 extracellular region (IEA, TAS, NAS): **MODIFY** all three to GO:0005615 extracellular space.
3. GO:0030212 hyaluronan metabolic process, IEA: **REMOVE**; ITIH4 lacks the bikunin-linking C-terminal consensus and is not incorporated into HA/proteoglycan complexes.
4. GO:0031012 extracellular matrix (two HDA): **KEEP_AS_NON_CORE** as context-specific proteomic localizations.
5. GO:0031089 platelet dense granule lumen, TAS: **UNDECIDED** because the Reactome model is explicit but the accessible source record lacks gene-specific primary support.
6. GO:0070062 extracellular exosome (two HDA) and GO:0072562 blood microparticle (HDA): **KEEP_AS_NON_CORE** as vesicle-enriched proteomic detections, not a core functional compartment.
7. GO:0005515 protein binding, IPI: **MARK_AS_OVER_ANNOTATED**; direct DNAJC1 binding is real but the generic term conveys no specific activity.
8. GO:0034097 response to cytokine and GO:0006953 acute-phase response, IEP: **KEEP_AS_NON_CORE** as inducible/contextual biology.
9. GO:0004866 endopeptidase inhibitor activity, TAS to PMID:9756925: **MODIFY** to GO:0004867. The term's biological essence is correct, but the cited paper is an ITIH3 gene/promoter study and is miscited for ITIH4 inhibitor activity [PMID:9756925, "To understand more about the human inter-alpha-trypsin inhibitor heavy chain H3 (ITIH3) expression"]. PMID:33523981 supplies the correct direct evidence.
10. Add **NEW** GO:0001869 and GO:1900004 from PMID:33523981.

## Remaining uncertainties

- Physiological occupancy and lifetime of ITIH4-protease complexes in vivo remain incompletely quantified.
- The relative importance of MASP-1, MASP-2, plasma kallikrein, and other candidate proteases across tissues and inflammatory states is unresolved.
- The mechanism that stores or enriches the 70-kDa ITIH4 chain in platelet dense granules needs direct confirmation.
- The functions of the released proline-rich peptide and 35-kDa C-terminal chain remain uncertain.
