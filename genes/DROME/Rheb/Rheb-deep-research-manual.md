# Rheb (Drosophila melanogaster, Q9VND8) - manual literature research

No deep-research provider was available for this review; this summary was compiled
manually from cached publications (`publications/PMID_*.md`) and the UniProt record
(`Rheb-uniprot.txt`). Each statement carries inline provenance.

## Identity and family

- Rheb (CG1081, FBgn0041191) encodes a 182-aa Ras-superfamily small GTPase; the C-terminal
  CaaX box (Cys179, farnesylated; residues 180-182 removed) anchors it to membranes
  [Rheb-uniprot.txt "Belongs to the small GTPase superfamily. Rheb family."].
- UniProt: "Activates the protein kinase activity of TORC1, and thereby plays a role in the
  regulation of apoptosis (PubMed:22493059)" [Rheb-uniprot.txt].

## Discovery and core pathway position

- Identified in a growth screen; "Rheb functions in the insulin signalling pathway downstream
  of Tsc1-Tsc2 and upstream of TOR" [PMID:12766776]. "Mutation of Rheb suspends larval growth
  and prevents progression from first to second instar" [PMID:12766776]. "Levels of rheb mRNA
  are rapidly induced in response to protein starvation" [PMID:12766776].
- Independently identified in a hindgut screen; "dRheb is required in the whole organism for
  viability (growth) and for the growth of individual cells. Inhibition of dRheb activity in
  cultured cells results in their arrest in G1 and a reduction in size" [PMID:12893813].
  Rapamycin blocked the overexpression phenotype [PMID:12893813].
- The Tsc1/Tsc2 complex is the Rheb GAP: "Tsc1 and Tsc2 (which together form a Rheb GAP)"
  [PMID:19216764].
- TCTP is a positive regulator: "dTCTP directly associates with dRheb and displays guanine
  nucleotide exchange activity with it in vivo and in vitro" [PMID:17301792]. Note that the
  GEF function of TCTP has been disputed in mammalian systems (general knowledge; not
  verified from cached text).

## TORC1 vs TORC2

- In S2 cells "dRheb has an inhibitory effect on dTORC2 activity ... This negative effect of
  dRheb on dTORC2 is possibly due to a feedback mechanism involving dTORC1 and dS6K"
  [PMID:16627617]. So TORC2 inhibition is indirect.
- In lst8 mutants, "expression of TOR and RAPTOR, together with their upstream activator Rheb,
  was sufficient to provide TORC1 activity" [PMID:22493059].
- Neuronal Rheb overexpression drives TOR-dependent axon misrouting (TORC1) and NMJ synapse
  overgrowth (TORC2-dependent) [PMID:22319582 "Synaptic phenotypes responded differently
  compared to axon guidance and behavioral phenotypes, and we show that this is due to a
  dependence on different downstream Tor complexes."].
- Spatially restricted TORC1 activation in the eye second mitotic wave is driven by Hh/E2F1/
  CycD-Cdk4 [PMID:28829944], with Rheb as a TORC1 activator (abstract-only).

## Downstream outcomes (indirect, via TOR)

- Protein synthesis and ribosome biogenesis: "Fed larvae overexpressing Rheb showed an increase
  in protein synthesis of 140-180% relative to controls" and "Rheb and TOR regulate ribosome
  biogenesis in Drosophila S2 cells, and do so independently of PI3K and Akt" [PMID:17371599].
- Cell size: "Silencing positive regulators of the pathway (Rheb, Tor, Raptor and S6k) led to
  a significant decrease in cell size" [PMID:19216764].
- Myc accumulation through GSK3beta [PMID:21951762].
- Autophagy: Rheb overexpression in muscle blocks autophagosome formation [PMID:24265594
  "the localization of GFP–Atg8 to autophagosomes in starved/CQ-treated muscles was completely
  blocked by Rheb overexpression compared to controls"]; in fat body, Rheb overexpression
  diminished starvation-induced GFP-2xFYVE punctae [PMID:18474623]. In the p62 assay, Rheb
  overexpression increased p62 dot number but not significantly [PMID:22952930 "Enhancing TOR
  signaling by overexpression of its activator Rheb or knockdown of the Rheb inhibitor Tsc2
  also increased p62 dot number, although in case of Rheb the phenotypes were so variable that
  the change was not statistically significant"]. Increased p62 dots indicate reduced
  autophagic flux, i.e. inhibition.
- Metabolism: hypomorphic Rheb alleles altered carbohydrate content (direction varies by
  allele) and mostly did not affect lipids [PMID:21464442 "No significant differences were
  found for Dp1105W3/5W3 or for three of four mutant combinations for Rheb."].
- Neural stem cell reactivation: Rheb overexpression promotes NSC exit from quiescence
  [PMID:31167138].
- Mushroom body: Rheb overexpression enlarges Kenyon cells and axonal lobes and impairs
  3-hour appetitive memory [PMID:23028662]. Overexpression-only; not used for new annotations.

## Localization

- Drosophila Rheb localizes to Golgi stacks of primary spermatocytes (co-staining with Lava
  lamp), and this depends on dGOLPH3 (sau) [PMID:36435842 "we observed that Rheb localized to
  Golgi stacks of primary spermatocytes, as assessed by co-staining with the Golgi marker Lava
  lamp"].
- No Drosophila evidence for plasma membrane localization was found in cached literature.

## Interactors

- Tctp (PMID:17301792, PMID:36435842), Cln7 (PMID:31666534, co-IP in S2 cells), GOLPH3/sau
  (PMID:36435842).
