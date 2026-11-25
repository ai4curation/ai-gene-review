# LATS2 notes

## Source scope

Deep-research providers were unavailable in this checkout, so this review was synthesized manually from the cached primary literature, Reactome Hippo events, UniProt/InterPro seed evidence, and the production GO-CAM model.

LATS2 was cloned as the human KPM kinase, a Warts/LATS-family Ser/Thr kinase with an immune-complex autophosphorylation activity [PMID:10871863, "Immune complex kinase assay of HA-tagged kpm showed that kpm had kinase activity and phosphorylated itself in vitro"]. A separate early characterization cloned the human and mouse genes and placed human HsLats2 in the nucleus by fractionation immunoblotting [PMID:10673337, "Immunoblotting analysis of fractionated cell lysates showed HsLats2 to be a nuclear protein"].

The core Hippo role is LATS2 phosphorylation of YAP/TAZ downstream of MST/SAV/MOB. Zhao et al. showed that LATS2, but not a kinase-inactive mutant, directly phosphorylates human YAP2, especially S127, and that endogenous Lats2 from high-density NIH3T3 cells has elevated YAP kinase activity [PMID:17974916, "Lats2 directly phosphorylates YAP2 on S127 and other serine residues in the HXRXXS motifs"]. Reactome captures the same cytosolic reactions for YAP S127 and TAZ S89 phosphorylation [Reactome:R-HSA-2028583, "Cytosolic phospho-LATS2, complexed with MOB1, catalyzes the phosphorylation of YAP on serine residue 127"; Reactome:R-HSA-2028661, "Cytosolic phospho-LATS2, complexed with MOB1, catalyzes the phosphorylation of WWTR1 (TAZ) on serine residue 89"]. Qi et al. added the WWC organizer mechanism in which WWC proteins bind LATS1/2 and SAV1 to bring MST1/2 to LATS for activation [PMID:35429439, "WWC proteins (WWC1/2/3) directly interact with LATS1/2 and SAV1"].

Other LATS2 functions look real but less central to the Hippo kinase module. Ectopic mouse Lats2 inhibited the G1/S transition and CDK2 activity in NIH3T3/v-ras cells, and the same abstract reports that LATS2 becomes localized to the mitotic apparatus during mitosis [PMID:12853976, "Cell cycle profile analysis demonstrated that ectopic expression of Lats2 inhibited the G1/S transition"]. An Ajuba paper supports centrosomal LATS2 and spindle organization through gamma-tubulin recruitment [PMID:16413547, "LATS2 was localized to the centrosomes throughout the cell cycle"]. The androgen receptor paper supports a non-core AR transcriptional modulation role [PMID:15131260, "LATS2 functions as a modulator of AR by inhibiting androgen-regulated gene expression"]. The 2024 inflammasome paper supports a non-core MTOC/NLRP3 activity [PMID:39173637, "where LATS1/2, pre-recruited to MTOC during priming, phosphorylates NLRP3"].

## GO-CAM 65a1f4f800003542

The GO-CAM activity for LATS2 in model `65a1f4f800003542` uses `GO:0004674` protein serine/threonine kinase activity, `GO:0035329` hippo signaling, and `GO:0005737` cytoplasm.

The gene review agrees with that activity. Reactome and the YAP phosphorylation literature support the more precise `GO:0005829` cytosol for the YAP/TAZ phosphorylation reactions, so the synthesized `core_functions` entry records cytosol; this is a child of the GO-CAM cytoplasm location rather than a contradiction.

## Main curation calls

- Accepted the serine/threonine kinase, Hippo signaling and contact-inhibition rows as LATS2's core function.
- Refined generic protein kinase and hormone-mediated signaling rows to protein serine/threonine kinase activity and androgen receptor signaling pathway.
- Kept nuclear, centrosomal/spindle, G1/S, organ-growth, apoptotic, and NLRP3 rows as non-core because they are supported but are peripheral relative to the conserved YAP/TAZ phosphorylation function.
- Left the Wnt/beta-catenin rows undecided because PMID:20412773 is abstract-only in the cache and the LATS2-specific experiment is unavailable.
- Removed all bare `GO:0005515` protein binding rows under the project policy for generic protein binding.
