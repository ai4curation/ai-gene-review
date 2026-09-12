# A4GNT review notes

## 2026-08-08 — primary-function synthesis

A4GNT encodes a 340-aa type-II Golgi membrane glycosyltransferase. The decisive human cloning paper showed that the enzyme transfers GlcNAc from UDP-GlcNAc in an alpha-1,4 linkage to terminal beta-linked galactose, with core-2-branched mucin O-glycans the best tested acceptors [PMID:10430883, "An in vitro GlcNAc transferase assay by using a soluble alpha4GnT revealed that alpha1,4-linked GlcNAc residues are transferred most efficiently to core 2 branched O-glycans"]. Core-1 was used less efficiently and core-3 barely, so the core description should not imply equal activity across all O-glycans [PMID:10430883, "The α4GnT was found to act more efficiently on core 2 branched O -glycans and less efficiently on core 1 oligosaccharide. However, this enzyme hardly transferred GlcNAc to core 3 oligosaccharide, GlcNAcβ1→3GalNAcα→ p NP (Fig. 5 )."].

The product is the terminal GlcNAc-alpha-1,4-Gal-beta-R structure characteristic of gastric gland/class III mucin. Ectopic expression in AGS cells produced class III mucin [PMID:10430883, "Transfection of alpha4GnT cDNA into gastric adenocarcinoma AGS cells produced class III mucin, indicating that alpha4GnT is responsible for the formation of class III Con A reactivity."]. Human tissue immunohistochemistry independently localized endogenous protein largely to the Golgi region of glandular mucous cells, and immunoprecipitation identified MUC5AC and MUC6 as glycan carriers [PMID:11304796, "Expression of alpha4GnT was largely associated with the Golgi region of mucous cells that produce the mucous glycoproteins having GlcNAcalpha1-->4Galbeta-->R, such as the glandular mucous cells of stomach and Brunner's gland."; PMID:11304796, "An immunoprecipitation experiment disclosed that two distinct mucin proteins, MUC5AC and MUC6 present in gastric mucin, carried the GlcNAcalpha1-->4Galbeta-->R structures."].

## Annotation strategy

- GO:0008375 acetylglucosaminyltransferase activity is the closest current molecular-function term. No current GO term encodes the alpha-1,4 linkage and terminal beta-galactoside acceptor; RHEA:85983 captures the generic reaction.
- GO:0016266 protein O-linked glycosylation via N-acetylgalactosamine is the most informative current biological-process term because its definition includes elongation of GalNAc-initiated O-glycans.
- GO:0000139 Golgi membrane is the appropriate core location.
- Broad ancestor annotations should be modified to the supported specific terms rather than retained as separate core functions.
- GO:0008194 is formally an ontology ancestor of GO:0008375 but its definition's "small hydrophobic molecule" acceptor does not describe A4GNT's glycan acceptors; treat this as term scoping/granularity, not as evidence that the enzyme lacks UDP-sugar transferase activity.
- Downstream antimicrobial, inflammatory, or tumor phenotypes of the alpha-GlcNAc-capped mucin product are context-specific consequences and should not be promoted into additional core A4GNT activities.

## Knowledge gap

GO lacks a reaction-specific molecular-function term for transfer of GlcNAc from UDP-GlcNAc to O-4 of terminal beta-D-galactose. An ontology request grounded in RHEA:85983 and PMID:10430883 would make the linkage and acceptor specificity explicit.

## Validation note

The local term validator initially added GO:0016266 under the exact synonym `protein O-linked glycosylation via N-acetyl-galactosamine`. Live QuickGO and the current GO source instead use `protein O-linked glycosylation via N-acetylgalactosamine`; that newly added cache row was changed to the authoritative primary label so the review's author-supplied replacement/core fields validate without adopting a stale synonym.

## PR follow-up

The terminal alpha-GlcNAc cap has biological effects beyond its biosynthesis. Human gastric mucin glycans inhibit H. pylori growth by blocking bacterial cholesteryl-alpha-D-glucopyranoside synthesis [PMID:15310903, "Here, we report that these O-glycans have antimicrobial activity against H. pylori, inhibiting its biosynthesis of cholesteryl-alpha-D-glucopyranoside, a major cell wall component."]. In mice, A4gnt loss removes gastric alpha-GlcNAc and causes spontaneous inflammation-associated gastric adenocarcinoma even without H. pylori [PMID:22307328, "A4gnt(-/-) mice showed complete lack of αGlcNAc expression in gastric gland mucin. Surprisingly, all the mutant mice developed gastric adenocarcinoma through a hyperplasia-dysplasia-carcinoma sequence in the absence of H. pylori infection."]. These are physiological consequences of the glycan product, not separate A4GNT molecular functions.
