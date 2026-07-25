# Manual literature synthesis for human ITIH4 (Q14624)

Automated deep-research providers were attempted on 2026-07-18. Falcon failed with HTTP 402 (Edison payment required), and the Perplexity Lite fallback failed with HTTP 401 (quota exceeded). This file records the manual synthesis from reviewed UniProtKB, cached primary publications, GOA, and the Reactome source record.

## Standalone biological summary

ITIH4 is a liver-produced, secreted 930-amino-acid plasma glycoprotein of the inter-alpha-inhibitor heavy-chain family. It contains VIT and von Willebrand factor A domains plus an H4-specific C-terminal region with a proline-rich protease-susceptible segment. Plasma kallikrein and other serine proteases cleave this segment into defined fragments.

Unlike ITIH1, ITIH2, and ITIH3, ITIH4 is not a bikunin-linked heavy chain of an inter-alpha-inhibitor proteoglycan. Purified human ITIH4 lacks bikunin, and a modern mechanistic analysis shows that H4 lacks the conserved C-terminal sequence needed for covalent bikunin-heavy-chain complex formation [PMID:7541790, "we concluded that GP120 was not a complex with bikunin"; PMID:33523981, "ITIH4 is not incorporated into proteoglycan complexes and presumably functions independently of the other protein family members"]. Consequently, family propagation to hyaluronan metabolism is not justified for ITIH4.

The core demonstrated molecular function is extracellular serine-type endopeptidase inhibition. ITIH4 acts as a cleavage-sensitive bait: after cleavage, its VWA domain mediates a divalent-cation-dependent, noncovalent complex with MASP-1, MASP-2, or plasma kallikrein. The complex sterically prevents large protein substrates from reaching the protease active site while leaving activity against small substrates [PMID:33523981, "This complex formation leads to protease inhibition by physically preventing cleavage of larger substrates, although the catalytic sites of the proteases remain active."]. Direct assays show inhibition of MASP-dependent C2/C4 cleavage, kallikrein-dependent high-molecular-weight kininogen cleavage, and lectin-pathway C4/C3 deposition in serum [PMID:33523981, "ITIH4 efficiently and dose-dependently inhibited C4 and C3 deposition"].

ITIH4 is also a type II acute-phase protein. IL-6 increases ITIH4 mRNA and secreted protein in HepG2 cells, and circulating concentration changes during acute inflammatory conditions [PMID:10486281, "HepG2 cell line we have observed up-regulation of ITIH4 mRNA expression upon dose-response treatments with interleukin-6 (IL-6)."]. This regulation is biologically important but is distinct from the protein's direct inhibitor activity.

ITIH4 is present in plasma and is detected by ECM-, exosome-, platelet-, and blood-microparticle datasets. The robust core functional location is extracellular space. Vesicle/ECM detections are contextual rather than evidence that ITIH4 is a structural HA-matrix component; exosome preparations can include soluble proteins [PMID:23533145, "some of these proteins could also exist as a soluble form."].

## Evidence synthesis by question

### What does ITIH4 directly do?

- Inhibits the serine endopeptidases MASP-1, MASP-2, and plasma kallikrein after cleavage-triggered complex formation [PMID:33523981, "Here, we show that ITIH4 is cleaved by several human proteases within a protease-susceptible region, enabling ITIH4 to function as a protease inhibitor."].
- Restricts cleavage of large physiological protein substrates without abolishing catalysis toward small peptide substrates [PMID:33523981, "ITIH4 inhibited the activity of both MASP-1 and MASP-2 against two distinct, highly-relevant protein substrates but not against smaller peptide substrates."].
- Inhibits lectin-pathway complement activation in human serum [PMID:33523981, "ITIH4 efficiently and dose-dependently inhibited C4 and C3 deposition"].

### What distinguishes H4 from other ITIH heavy chains?

- The C-terminal 300 residues are H4-specific rather than homologous to the other heavy chains [PMID:7775381, "the C-terminal 300 residues showed no homology with the heavy chains"].
- ITIH4 is a single plasma glycoprotein without bikunin or a chondroitin-sulfate linkage [PMID:7541790, "Since GP120 showed no bikunin sequence, and chondroitinase treatment and alkaline treatment of GP120 did not affect its molecular weight"].
- It lacks the C-terminal consensus needed for bikunin-heavy-chain complex formation [PMID:33523981, "ITIH4 lacks a C-terminal consensus sequence, which is present in all other ITIHs, that is required for the formation of bikunin-ITIH complexes."].

### Where and when does ITIH4 act?

- The N-terminal signal peptide and direct plasma purification establish secretion [PMID:7775381, "The N-terminal 28 residues corresponded to a signal peptide for secretion."; PMID:7947966, "A 120 kDa plasma protein, which is susceptible to plasma kallikrein, was purified from human plasma"].
- IL-6 induces hepatic-cell expression/secretion, consistent with acute-phase deployment [PMID:10486281, "The results presented here indicate that ITIH4 is a type II acute-phase protein in humans."].
- Its direct targets are intravascular host-defense proteases, placing its core inhibitor action in extracellular/plasma space [PMID:33523981, "MASP-1, MASP-2, and plasma kallikrein, which are key proteases for intravascular host defense"].

## Curation boundaries

- Do not infer hyaluronan metabolism or bikunin-containing complex membership for ITIH4.
- Do not treat proteolytic cleavage as evidence that ITIH4 is merely a passive substrate; direct experiments show that cleavage initiates inhibition.
- Do not treat generic protein binding as a core molecular function. The DNAJC1 interaction is specific but ancillary.
- Do not interpret acute-phase abundance changes or biomarker associations as a separate catalytic activity.
- Keep ECM and extracellular-vesicle proteomics as non-core localization contexts unless direct partitioning demonstrates functional incorporation.
