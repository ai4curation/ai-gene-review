# ligL evidence notes

## 2026-11-02 annotation review

Reviewed C0SUJ9 as the normally seeded SPHSK/ligL record. Machine-sourced identity, taxonomy, annotation rows and raw UniProt/GOA files are preserved. The annotation-reviewer workflow used gene-specific primary studies, independently assessed reference findings and live GO definitions. No new GO annotation rows were manufactured.

Both beta configurations are accepted within the alphaS class. Do not allocate one GGE diastereomer to each dehydrogenase. LigL and LigN supply complementary capacity for alphaS GGE oxidation in SYK-6. The dichlorocyclohexadienediol ARBA prediction is not evidence for physiological chlorinated-substrate turnover.

- [PMID:19542348](https://pubmed.ncbi.nlm.nih.gov/19542348/): ligL oxidizes both beta configurations of alphaS GGE; the alpha configuration, rather than a unique alpha/beta pair per paralog, determines this substrate partition.
  > Chiral HPLC analysis indicated that LigL and LigN have the same stereospecificity and transformed (α S ,β R )-GGE and (α S ,β S )-GGE to (β R )-MPHPV and (β S )-MPHPV, respectively (Fig. 3 ; see Fig. S2 in the supplemental material). On the other hand, LigO converted (α R ,β S )-GGE and (α R ,β R )-GGE into (β S )-MPHPV and (β R )-MPHPV, respectively (see Fig. S3 in the supplemental material). These results indicated that LigO has the same stereospecificity as LigD.
- [PMID:26940872](https://pubmed.ncbi.nlm.nih.gov/26940872/): Structural and biochemical characterization establishes NAD+-dependent Calpha alcohol oxidation and the SDR catalytic mechanism.
  > The conversion from GGE to MPHPV during the Cα-dehydrogenase reaction is achieved by the loss of a proton and a hydride ion from the substrate, creating NADH from NAD+, and transfer of the proton to the bulk solvent (Fig. 1).

## Annotation decisions and scope

- GO:0018502: MARK_AS_OVER_ANNOTATED. GO:0018502 denotes oxidation of 2,5-dichloro-2,5-cyclohexadiene-1,4-diol to dichlorohydroquinone, not the GGE Calpha oxidation established for ligL in PMID:19542348 and PMID:26940872. Membership in the SDR superfamily supports general oxidoreductase chemistry but does not establish this precise chlorinated-substrate activity. The assays establish a different physiological substrate; they do not experimentally exclude all promiscuous activity on the chlorinated compound. Therefore the electronic specificity is marked over-annotated rather than claimed to be disproven. The supported specific GGE activity is represented as a proposed molecular function.

The proposed molecular function is arylglycerol-beta-aryl ether Calpha-dehydrogenase (NAD+) activity. A specific supported proposed term is used instead of an ill-fitting current GO term. The evidence concerns lignin-derived model dimers and downstream intermediates; it does not by itself show attack on intact lignin polymer. The description is a biological summary independent of the module audit.

## Source and retrieval limits

The required `just deep-research-falcon SPHSK ligL` attempt failed with HTTP 403 authentication failure from Edison (exit 1). The actual command log is `.cache/module-audit-logs/beta-aryl-syk-review/falcon-ligL.log`; no provider-named research report was fabricated. Manual research and exact cached primary-source quotations supply the review. Abstract-only papers are identified in the YAML findings; no experimental claim was rejected because its full text was inaccessible.

Live QuickGO definitions were checked at https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004364,GO:0016846,GO:0016616,GO:0046274,GO:0018502,GO:0005886,GO:0005737 . The response and term searches are saved under `.cache/module-audit-logs/beta-aryl-syk-review/`. GO:0046274 names breakdown of lignin polymers; the bounded dimer mechanism is kept explicit. GO:0005886 includes membrane-associated proteins, so soluble purification cannot refute peripheral membrane association. GO:0005737 is a compartment assertion, not a synonym for a soluble GST fold.

## 2026-11-02 PR #5930 reviewer follow-up

Addressed PR #5930 review item 3. GO:0018502 is now MODIFY with an NTR replacement matching the proposed arylglycerol-beta-aryl ether Calpha-dehydrogenase (NAD+) activity. This links the existing alcohol-oxidation assertion to the directly established physiological substrate. The original SUSPECTED WRONG_TERM/CHECK source defect is retained; the experiments are not treated as disproof of every possible promiscuous chlorinated-substrate activity.

The proposed-term definitions, parents and justifications are unchanged in this follow-up; repository-wide canonicalization is handled separately. Raw sources and machine annotation fields are preserved.

## 2026-11-03 — shared proposed-term definition

PR5930 follow-up reconciles the shared proposed activity with the canonical definition, GO parent and chemistry-specific justification in `analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/canonical-proposed-terms.yaml`. Gene-specific evidence and stereoselectivity are retained. The broad parent is not substituted for the precise proposed activity; BaeAB subunits continue to contribute to the assembled complex rather than receiving standalone full activity.
