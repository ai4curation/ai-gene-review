# sup-17 (C. elegans) review notes

- UniProt: G5EFD9 (ADA10_CAEEL), "Disintegrin and metalloproteinase domain-containing protein 10 homolog"; ORF DY3.7; 922 aa, single-pass type I membrane protein.
- PANTHER: PTHR45702 (ADAM10/ADAM17 METALLOPEPTIDASE FAMILY MEMBER); subfamily PTHR45702:SF2 (KUZBANIAN, ISOFORM A).
- Domains: Peptidase M12B (242-480) with HExxH active site (E427; zinc ligands H426, H430, H436), disintegrin (511-615), ADAM10-type Cys-rich domain.
- IBA nodes in GOA: PTN005236519 (metalloendopeptidase activity, plasma membrane, membrane protein ectodomain proteolysis); PTN001374824 (Notch signaling pathway; sources include sup-17 WBGene00006324 and adm-4 WBGene00000075).

## Notch role (S2 / ectodomain-shedding protease)
- sup-17 encodes an ADAM protease similar to Kuzbanian and ADAM10 [PMID:9428412 "Here, we show that sup-17 encodes a member of the ADAM family of metalloproteases."]
- Acts upstream of / at the receptor ectodomain, cell autonomously [PMID:9428412 "the extracellular domain of LIN-12 appears to be necessary for sup-17 to facilitate lin-12 signalling and that sup-17 does not act downstream of lin-12."; "sup-17 can act cell autonomously to facilitate lin-12 activity."]
- Redundant with ADM-4 (TACE/ADAM17 ortholog); double reduction gives 2 ACs; sterility rescued by truncated LIN-12 mimicking ectodomain shedding [PMID:16197940 "Expression of a truncated form of LIN-12 that mimics the product of ectodomain shedding rescues this fertility defect, suggesting that sup-17 and adm-4 may mediate ectodomain shedding of LIN-12 and/or GLP-1."]
- Identified as a lin-12(gf) suppressor; null alleles lethal [PMID:9409830 "we present evidence that null mutations in these two genes cause lethality."]
- No biochemical detection of the SUP-17-generated S2 product in worms found in cached literature: role inferred from genetics + orthology.

## Non-Notch roles
- Promotes BMP-like Sma/Mab signaling with TspanC8-like tetraspanins TSP-12/TSP-14, which bind SUP-17 and promote its surface localization; UNC-40/DCC is a genetic substrate; Notch-independent; presenilins not required [PMID:28068334].
- SDQL axon guidance via EFN-4 shedding [PMID:26903502 "SDQL-specific expression of EFN-4ΔGPI but not full-length EFN-4 rescued abnormal SDQL defects in sup-17 hypomorphic animals."]
- Localization: cell surface (basolateral in embryos) and cytoplasmic puncta [PMID:28068334].

## Review decisions (summary)
- Core MF: metalloendopeptidase activity (GO:0004222); BP: membrane protein ectodomain proteolysis, Notch receptor processing (added NEW, IGI PMID:16197940; comparator: mouse Adam10 NAS, human PSEN1 IDA carry GO:0007220).
- REMOVE: protein binding (TSP-12/TSP-14 IPI; uninformative).
- MODIFY: positive regulation of TGF-beta receptor signaling -> positive regulation of BMP signaling pathway (GO:0030513).
- MARK_AS_OVER_ANNOTATED: cytoplasm, organelle (ARBA IEAs).
- Pathway variant notes: S2 cleavage is shared/redundant between ADAM10 (SUP-17) and ADAM17 (ADM-4) orthologs in worm, unlike the stronger Kuz dependence in fly.

## Deep research
- Falcon deep research completed (sup-17-deep-research-falcon.md, 2026-09-30). Consistent with the above: "In the context of Notch signaling, SUP-17 participates in ligand-induced proteolytic processing of Notch receptors (LIN-12 and GLP-1), performing the S2 cleavage..."
