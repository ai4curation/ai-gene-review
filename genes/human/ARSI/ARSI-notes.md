# ARSI review notes

## Research scope and provenance

- Seeded the human Q5FYB1 review with just fetch-gene and refreshed all PMIDs with just fetch-gene-pmids on 2026-07-18.
- The required Falcon deep-research attempt failed with HTTP 402; the Perplexity-lite fallback failed with HTTP 401 (quota). No provider-named research file was retained. Manual synthesis is in ARSI-deep-research-manual.md.
- Reviewed the Swiss-Prot record, all 10 GOA rows, cached primary papers, Reactome R-HSA-1614362, and the accessible full-text preprint corresponding to the peer-reviewed 2026 Matrix Biology paper.

## Protein identity and isoforms

ARSI is a 569-residue class I sulfatase precursor with a predicted signal peptide (1-23), a conserved catalytic Cys93 that is converted by SUMF1 to formylglycine, and the other conserved sulfatase catalytic/substrate-binding residues. Isoform 2 lacks residues 1-143, including the signal peptide, catalytic Cys93, and much of the catalytic core, so it is unlikely to be a conventionally trafficked active sulfatase; this has not been tested experimentally.

The original family survey identified ARSI as one of four new human sulfatases and emphasized that the catalytic formylglycine mechanism is conserved [PMID:16174644 "four novel ones (ARSH, ARSI, ARSJ and ARSK)"] [PMID:16174644 "This unique modification mechanism, which is required for catalytic activity, has been highly conserved during evolution"].

## Direct biochemical function

The 2009 ARPE-19 overexpression study detected SUMF1-dependent activity against the artificial aryl substrate 4-methylumbelliferyl sulfate in conditioned medium at neutral pH. Cys93Ser abolished this activity, directly identifying the catalytic nucleophile [PMID:19262745 "the conditioned medium of the transfected cells showed arylsulfatase activity at a range of neutral pH"] [PMID:19262745 "This result confirms that the active site of ARSI is Cys93 and that it is activated by SUMF1 as well as other ARSs"].

The 2026 work resolves the physiological substrate and changes the localization model. Human ARSI gain-of-function, rat Arsi loss-of-function, and purified human protein assays identify ARSI as an acid-active chondroitin sulfatase selective for terminal GalNAc4S; no GalNAc6S activity was detected. The abstract summarizes the result as [PMID:41916471 "ARSI is a novel chondroitin endosulfatase, specifically desulfating chondroitin-4-sulfate at pH 4.5"]. Full-text inspection further showed purified human ARSI, coexpressed with SUMF1, converting GalNAc4S but not GalNAc6S and acting at the nonreducing end of CS/DS chains. GO:0003943 N-acetylgalactosamine-4-sulfatase activity is therefore the best available specific molecular-function term.

## Localization boundary

The older ARPE-19 FLAG study placed overexpressed ARSI in the ER and detected it in medium, leading to the proposal of extracellular function [PMID:19262745 "Transiently produced ARSI-FLAG was localized to the endoplasmic reticulum and was detected in the cellular fraction and the medium"] [PMID:19262745 "ARSI may be a secreted sulfatase and may function in the extracellular space"]. The same full text cautions that overproduced ARSI may be unstable, degraded, or retained in the ER.

The 2026 study instead colocalized fluorescently tagged human ARSI with LAMP1 and RAB5 and found altered lysosome homeostasis after Arsi loss in chondrocytes. Its abstract states [PMID:41916471 "Colocalization studies suggested that ARSI is lysosomal"]. Lysosome is treated as the core functional location. ER/ER-lumen annotations are retained as biosynthetic/formylglycine-maturation compartments. Extracellular annotations are retained as non-core because secretion was experimentally observed under overexpression, but they should not define the main physiological site after the lysosomal and acidic-substrate evidence.

## Biological role

ARSI expression rises in mature cartilage across chick and mouse systems. Arsi knockout in rat chondrocytes increased chondrocyte-maturation markers, including Col10a1 and Mmp13, before and after FGF18 induction; the paper concludes that ARSI normally inhibits chondrocyte maturation. For a human review this process is transferred conservatively as ISS, not as direct human IMP [PMID:41916471 "Finally, Arsi knockout in RCS chondrocytes caused increased expression of maturation genes, such as Col10a1 and Mmp13"] [PMID:41916471 "these data identify ARSI as a novel PG sulfatase regulating endochondral ossification"].

ARSI was nominated as one of several putative hereditary spastic paraplegia genes in a large exome study, but the cached abstract does not expose the family/variant-level evidence and current diagnostic panels describe the association as preliminary or low evidence. This review does not infer a GO process from that candidate disease association [PMID:24482476 "identified 18 previously unknown putative HSP genes"].

## Existing-annotation decisions

| GOA group | Decision | Rationale |
|---|---|---|
| GO:0008484 sulfuric ester hydrolase activity (IBA, IEA) | MODIFY | Correct but too broad after direct GalNAc4S specificity; replace with GO:0003943. |
| GO:0004065 arylsulfatase activity (IEA, TAS) | MODIFY | Artificial arylsulfatase activity is real, but the natural-substrate term is more informative. |
| GO:0005576 extracellular region (IEA, EXP) | KEEP_AS_NON_CORE | Direct overexpression secretion exists, but newer lysosomal localization and acidic activity define the core site. |
| GO:0005783 endoplasmic reticulum (IEA, EXP) | KEEP_AS_NON_CORE | Directly observed and required for SUMF1 maturation, but is mainly a biosynthetic/transit compartment. |
| GO:0005788 endoplasmic reticulum lumen (TAS) | KEEP_AS_NON_CORE | Formylglycine generation occurs in the ER lumen during biogenesis. |
| GO:0005515 protein binding (IPI; KRT40) | MARK_AS_OVER_ANNOTATED | Generic high-throughput binary interaction with no demonstrated physiological role; topology is also discordant. |

## New annotation candidates

- GO:0003943 N-acetylgalactosamine-4-sulfatase activity — IDA, PMID:41916471.
- GO:0005764 lysosome — IDA, PMID:41916471.
- GO:0030207 chondroitin sulfate proteoglycan catabolic process — IDA, PMID:41916471.
- GO:0032331 negative regulation of chondrocyte differentiation — ISS from rat Arsi loss-of-function, PMID:41916471.

## Open issues

- Determine whether endogenous human ARSI is predominantly lysosomal in primary cartilage and retinal pigment epithelium, and whether a regulated extracellular pool exists.
- Resolve whether ARSI acts only at nonreducing terminal GalNAc4S or also has internal/endosulfatase activity on particular native proteoglycans.
- Establish which chondroitin/dermatan sulfate proteoglycans are its principal in vivo substrates.
- Test whether isoform 2 is translated and whether it has any noncatalytic role despite loss of the signal peptide and catalytic core.
- Reassess the proposed SPG66 association with replicated pedigrees, segregation, functional variants, and disease-relevant models.

