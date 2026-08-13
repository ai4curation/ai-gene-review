# glgA curation notes

- Q88FN9 is a reviewed bacterial glycogen synthase assigned EC 2.4.1.21 and RHEA:18189. [file:PSEPK/glgA/glgA-uniprot.txt, "DE   RecName: Full=Glycogen synthase"]
- The record explicitly predicts ADP-glucose use, but this is HAMAP inference rather than a direct Q88FN9 assay. [file:PSEPK/glgA/glgA-uniprot.txt, "Synthesizes alpha-1,4-glucan chains using ADP-glucose."]
- Purified PAO1 GlgA produced linear alpha-glucan from UDP-glucose and showed highest activity with UDP-glucose. [PMID:33872310, "The highest polymerase activity was with UDP-glucose, as expected given the lack of the glgC gene coding for the enzyme responsible for the production of ADP-glucose in Pseudomonas spp."]
- The current PSEPK metadata contains no `glgC` or EC 2.7.7.27 candidate, but does contain GalU/Q88GA4. The same GalU-positive, GlgC-negative architecture supports UDP-glucose as the leading PSEPK hypothesis without proving Q88FN9 specificity.
- The independent annotation review accepts the UDP-glucose-specific term and removes the ADP-glucose-specific electronic prediction. This is a strong homolog-and-pathway-context inference; direct Q88FN9 donor assays remain the key experimental gap.
- Historical Asta curation from PR #2049 was inspected only as a lead; current UniProt/GOA evidence independently supports the donor-specific correction.
