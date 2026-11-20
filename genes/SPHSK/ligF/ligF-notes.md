# ligF evidence notes

## 2026-11-02 annotation review

Reviewed P30347 as the normally seeded SPHSK/ligF record. Machine-sourced identity, taxonomy, annotation rows and raw UniProt/GOA files are preserved. The annotation-reviewer workflow used gene-specific primary studies, independently assessed reference findings and live GO definitions. No new GO annotation rows were manufactured.

betaS-configured substrate yields betaR-configured GSH conjugate. GO:0004364 explicitly requires a halide leaving group and therefore does not exactly describe this reaction; the GST family name alone does not change that chemistry. No direct localization is assigned to the core activity.

- [PMID:12618439](https://pubmed.ncbi.nlm.nih.gov/12618439/): LigE and LigF convert opposite MPHPV enantiomers to guaiacol and a glutathione conjugate through nucleophilic attack by glutathione.
  > Based on the
identification of the reaction product by electrospray ionization-mass
spectrometry, a model compound of beta-aryl ether,
alpha-(2-methoxyphenoxy)-beta-hydroxypropiovanillone (MPHPV), was transformed by
LigF or LigE to guaiacol and alpha-glutathionyl-beta-hydroxypropiovanillone
(GS-HPV). This result suggested that LigF and LigE catalyze the nucleophilic
attack of glutathione on the carbon atom at the beta position of MPHPV.
- [PMID:24509858](https://pubmed.ncbi.nlm.nih.gov/24509858/): ligF is stereoselective for betaS alpha-carbonyl beta-aryl ether and yields a betaR glutathione conjugate by inversion.
  > β-etherase catalysis causes
stereochemical inversion of the chiral center, converting a β(R)-substrate to a
β(S)-product (LigE and LigP), and a β(S)-substrate to a β(R)-product (LigF).
- [PMID:8495726](https://pubmed.ncbi.nlm.nih.gov/8495726/): LigE and LigF belong to the GST superfamily; glutathione stimulates beta-etherase activity.
  > ligF and ligE
are homologous to glutathione-S-transferase, and upon addition of glutathione a
remarkable acceleration of beta-etherase activity was found in E. coli carrying
ligF.

## Annotation decisions and scope



The proposed molecular function is glutathione-dependent beta-aryl etherase activity. A specific supported proposed term is used instead of an ill-fitting current GO term. The evidence concerns lignin-derived model dimers and downstream intermediates; it does not by itself show attack on intact lignin polymer. The description is a biological summary independent of the module audit.

## Source and retrieval limits

The required `just deep-research-falcon SPHSK ligF` attempt failed with HTTP 403 authentication failure from Edison (exit 1). The actual command log is `.cache/module-audit-logs/beta-aryl-syk-review/falcon-ligF.log`; no provider-named research report was fabricated. Manual research and exact cached primary-source quotations supply the review. Abstract-only papers are identified in the YAML findings; no experimental claim was rejected because its full text was inaccessible.

Live QuickGO definitions were checked at https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004364,GO:0016846,GO:0016616,GO:0046274,GO:0018502,GO:0005886,GO:0005737 . The response and term searches are saved under `.cache/module-audit-logs/beta-aryl-syk-review/`. GO:0046274 names breakdown of lignin polymers; the bounded dimer mechanism is kept explicit. GO:0005886 includes membrane-associated proteins, so soluble purification cannot refute peripheral membrane association. GO:0005737 is a compartment assertion, not a synonym for a soluble GST fold.

## 2026-11-03 — shared proposed-term definition

PR5930 follow-up reconciles the shared proposed activity with the canonical definition, GO parent and chemistry-specific justification in `analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/canonical-proposed-terms.yaml`. Gene-specific evidence and stereoselectivity are retained. The broad parent is not substituted for the precise proposed activity; BaeAB subunits continue to contribute to the assembled complex rather than receiving standalone full activity.
