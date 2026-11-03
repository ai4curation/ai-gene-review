# ligD evidence notes

## 2026-11-02 annotation review

Reviewed Q01198 as the normally seeded SPHSK/ligD record. Machine-sourced identity, taxonomy, annotation rows and raw UniProt/GOA files are preserved. The annotation-reviewer workflow used gene-specific primary studies, independently assessed reference findings and live GO definitions. No new GO annotation rows were manufactured.

Both beta configurations are accepted within the alphaR class. Do not allocate one GGE diastereomer to each dehydrogenase. LigD supplies the major physiological alphaR oxidation activity in SYK-6: disruption prevents conversion of both alphaR GGE diastereomers under the tested conditions. The dichlorocyclohexadienediol ARBA prediction is not evidence for physiological chlorinated-substrate turnover.

- [PMID:19542348](https://pubmed.ncbi.nlm.nih.gov/19542348/): ligD oxidizes both beta configurations of alphaR GGE; the alpha configuration, rather than a unique alpha/beta pair per paralog, determines this substrate partition.
  > Chiral HPLC analysis indicated that LigL and LigN have the same stereospecificity and transformed (α S ,β R )-GGE and (α S ,β S )-GGE to (β R )-MPHPV and (β S )-MPHPV, respectively (Fig. 3 ; see Fig. S2 in the supplemental material). On the other hand, LigO converted (α R ,β S )-GGE and (α R ,β R )-GGE into (β S )-MPHPV and (β R )-MPHPV, respectively (see Fig. S3 in the supplemental material). These results indicated that LigO has the same stereospecificity as LigD.
- [PMID:26940872](https://pubmed.ncbi.nlm.nih.gov/26940872/): Structural and biochemical characterization establishes NAD+-dependent Calpha alcohol oxidation and the SDR catalytic mechanism.
  > The conversion from GGE to MPHPV during the Cα-dehydrogenase reaction is achieved by the loss of a proton and a hydride ion from the substrate, creating NADH from NAD+, and transfer of the proton to the bulk solvent (Fig. 1).
- [PMID:7764263](https://pubmed.ncbi.nlm.nih.gov/7764263/): LigD oxidation produces the alpha-carbonyl substrate required by beta-etherases.
  > C alpha-dehydrogenase catalyzes the oxidation of arylglycerol-beta-aryl ether at
the C alpha-position, and therefore this process produces the specific substrate
for beta-etherase, which cleaves beta-ary ethers (C alpha carbonyl type).

## Annotation decisions and scope

- GO:0046274: ACCEPT. The UniPathway mapping is consistent with the experimentally established participation of LigD in lignin-derived aromatic catabolism (PMID:19542348; PMID:7764263). LigD performs an actual catalytic step and its disruption blocks both alphaR GGE diastereomers. GO:0046274 refers to lignin polymer breakdown; this pathway-level annotation is retained in the established lignin-degradation usage, with the explicit limit that the experiments establish low-molecular-weight dimer conversion, not extracellular attack on intact lignin polymer. No broader polymer-depolymerase activity is inferred.

The proposed molecular function is arylglycerol-beta-aryl ether Calpha-dehydrogenase (NAD+) activity. A specific supported proposed term is used instead of an ill-fitting current GO term. The evidence concerns lignin-derived model dimers and downstream intermediates; it does not by itself show attack on intact lignin polymer. The description is a biological summary independent of the module audit.

## Source and retrieval limits

The required `just deep-research-falcon SPHSK ligD` attempt failed with HTTP 403 authentication failure from Edison (exit 1). The actual command log is `.cache/module-audit-logs/beta-aryl-syk-review/falcon-ligD.log`; no provider-named research report was fabricated. Manual research and exact cached primary-source quotations supply the review. Abstract-only papers are identified in the YAML findings; no experimental claim was rejected because its full text was inaccessible.

Live QuickGO definitions were checked at https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004364,GO:0016846,GO:0016616,GO:0046274,GO:0018502,GO:0005886,GO:0005737 . The response and term searches are saved under `.cache/module-audit-logs/beta-aryl-syk-review/`. GO:0046274 names breakdown of lignin polymers; the bounded dimer mechanism is kept explicit. GO:0005886 includes membrane-associated proteins, so soluble purification cannot refute peripheral membrane association. GO:0005737 is a compartment assertion, not a synonym for a soluble GST fold.

## 2026-11-02 PR #5930 reviewer follow-up

Addressed PR #5930 review items 1 and 4. GO:0046274 is now KEEP_AS_NON_CORE for the wider biological context of lignin-derived substrate utilization, not because a general term should merely be refined. Core activity remains dimer Calpha oxidation. Replaced the indirect LigL/LigN/LigO quotation in the LigD finding and core evidence with the direct LigD substrate/product sentence from PMID:19542348: These results clearly indicated that LigD converted (α R ,β S )-GGE and (α R ,β R )-GGE into (β S )-MPHPV and (β R )-MPHPV, respectively.

The proposed-term definitions, parents and justifications are unchanged in this follow-up; repository-wide canonicalization is handled separately. Raw sources and machine annotation fields are preserved.

## 2026-11-03 — shared proposed-term definition

PR5930 follow-up reconciles the shared proposed activity with the canonical definition, GO parent and chemistry-specific justification in `analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/canonical-proposed-terms.yaml`. Gene-specific evidence and stereoselectivity are retained. The broad parent is not substituted for the precise proposed activity; BaeAB subunits continue to contribute to the assembled complex rather than receiving standalone full activity.
