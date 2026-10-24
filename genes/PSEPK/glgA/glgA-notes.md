# glgA curation notes

- Q88FN9 is a reviewed bacterial glycogen synthase assigned EC 2.4.1.21 and RHEA:18189. [file:PSEPK/glgA/glgA-uniprot.txt, "DE   RecName: Full=Glycogen synthase"]
- The record explicitly predicts ADP-glucose use, but this is HAMAP inference rather than a direct Q88FN9 assay. [file:PSEPK/glgA/glgA-uniprot.txt, "Synthesizes alpha-1,4-glucan chains using ADP-glucose."]
- Purified PAO1 GlgA produced linear alpha-glucan from UDP-glucose and showed highest activity with UDP-glucose. [PMID:33872310, "The highest polymerase activity was with UDP-glucose, as expected given the lack of the glgC gene coding for the enzyme responsible for the production of ADP-glucose in Pseudomonas spp."]
- The current PSEPK metadata contains no `glgC` or EC 2.7.7.27 candidate, but does contain GalU/Q88GA4. The same GalU-positive, GlgC-negative architecture supports UDP-glucose as the leading PSEPK hypothesis without proving Q88FN9 specificity.
- The UDP-glucose-specific term is accepted by transfer from the assayed PAO1 ortholog in the same PTHR45825:SF8 subfamily and the shared GlgC-negative pathway architecture. The incompatible ADP-glucose-specific electronic prediction is removed; direct Q88FN9 kinetics remain a knowledge gap.
- PAO1 GlgB can branch GlgA-derived alpha-glucan when overexpressed in a sensitized background, but the paper concludes that physiological GlgA flux is primarily directed through TreY/TreZ toward trehalose or maltose. [PMID:33872310, "the cluster of genes including glgA is entirely geared towards the production of either trehalose or maltose in vivo."]
- Historical Asta curation from PR #2049 was inspected only as a lead; current UniProt, GOA, and literature evidence independently support the present donor-specific assessment.
