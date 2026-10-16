# SULT1B1 (O43704) — review notes

Reviewed as part of the contested-functions batch. **Headline finding: GO got this one right.**
The contested claim (histone tyrosine sulfotransferase activity) never entered GOA, and nothing
in the existing annotation set needs to change because of the dispute.

## 1. Established function

SULT1B1 is one of the ~13 human cytosolic (SULT-family) sulfotransferases. It transfers the
sulfonate group of PAPS to small phenolic acceptors and to iodothyronines.

- Cloning/characterization, human "hST1B2" (= SULT1B1):
  [PMID:9463486 "Expressed hST1B2 sulfates small phenols such as 1-naphthol and p-nitrophenol and
  thyroid hormones, including 3,3'-diiodothyronine, triiodothyronine, reverse triiodothyronine, and
  thyroxine."]
- Substrate exclusions in the same paper:
  [PMID:9463486 "No activity was detected when several steroids or dopamine were tested as
  substrates."]
- Parallel cloning of rat ST1B1 / human ST1B2:
  [PMID:9443824 "The recombinant forms catalyzed sulfation of p-nitrophenol, 3,3',5-triiodothyronine
  (T3) and dopamine, but not of beta-estradiol and dehydroepiandrosterone."]
  and [PMID:9443824 "These data indicate that the newly characterized sulfotransferases constitute a
  distinct ST1 subfamily of enzymes catalyzing the sulfation of T3 as a typical endogenous substrate
  in rats and humans."]
- Note the **direct conflict on dopamine** between the two founding papers: 9443824 reports dopamine
  sulfation, 9463486 reports none. UniProt's FUNCTION line follows 9443824. This is the only reason
  the `GO:0006576 biogenic amine metabolic process` (TAS) annotation is kept rather than accepted
  outright.
- Phenolic/PAH substrate preference and the common L145V variant:
  [PMID:28084139 "Human cytosolic sulfotransferase 1B1 (SULT1B1) sulfates small phenolic compounds
  and bioactivates polycyclic aromatic hydrocarbons."]
  [PMID:28084139 "SULT1B1, initially termed iodothyronine sulfotransferase, is the focus of this
  manuscript and is classically associated with the sulfation of thyroid hormones as indicated by its
  alternative name"]
  [PMID:28084139 "SULT1B1 is expressed at highest levels throughout the human colon and small
  intestine but can also be found at moderate levels in human liver, kidney, and white blood cells"]
- Flavonoid (hesperetin) conjugation, 12-SULT panel:
  [PMID:20056724 "Based on expression levels SULT1A3 and SULT1B1 also will probably play a role in the
  sulfo-conjugation of hesperetin in vivo."]
- Inhibitor pharmacology (kynurenic acid and derivatives):
  [PMID:19548878 "KYNA also exerted an inhibitory activity towards hSULT1A1 and hSULT1B1."]
  [PMID:19548878 "Interestingly, gavestinel, another KYNA derivative, was found to be an extremely
  potent inhibitor of hSULT1B1."]
- Localization: UniProt SUBCELLULAR LOCATION is `Cytoplasm` with ECO:0000269 from both founding
  papers. The Reactome `cytosol` TAS annotations are the more informative form.

### Where I disagree with a GOA row

`GO:0006068 ethanol catabolic process` (IDA, PMID:23207770, assigned by CAFA). The cited paper's own
abstract positively **excludes** SULT1B1 from the set of ethanol-sulfating enzymes:
[PMID:23207770 "A systematic analysis revealed four ethanol-sulfating SULTs, SULT1A1, SULT1A2,
SULT1A3, and SULT1C4, among the eleven human SULT enzymes previously prepared and purified."]
SULT1B1 was one of the eleven assayed and was a negative. I have marked this
`MARK_AS_OVER_ANNOTATED` rather than `REMOVE` (project rule: do not remove an experimental
annotation whose full text I have not read), but I regard it as a probable mis-transfer of the
paper's panel result. The sibling annotations from the same paper (`GO:0004062`, `GO:0051923`,
`GO:0050427`) are fine — SULT1B1 genuinely was a purified, PAPS-using enzyme in that panel.

`GO:0030855 epithelial cell differentiation` (IEP, PMID:21492153) comes from a 2-D gel proteomic
comparison of proliferating vs differentiated Caco-2 cells. That is an expression correlation, not a
role in the process; over-annotated.

## 2. The contested claim: histone tyrosine sulfation

### The original report (2023)

[PMID:36805701 "Here we report that SULT1B1 is a histone sulfotransferase that can sulfate the
tyrosine 99 residue of nascent histone H3 in cytosol."]
[PMID:36805701 "Tyrosine sulfation is a common posttranslational modification in mammals. To date, it
has been thought to be limited to secreted and transmembrane proteins, but little is known about
tyrosine sulfation on nuclear proteins."]

### The refutation (2025, formal Matters Arising, Nat Chem Biol)

Youssef et al. reannotated the original raw MS data (PRIDE PXD043754), ran synthetic-sulfopeptide
controls, repeated the enzyme assay, and blotted with an anti-sulfotyrosine antibody.

- Prior expectation about where tyrosine sulfation happens:
  [PMID:40890505 "Tyrosylprotein sulfotransferases are only known to exist in the Golgi, consistent
  with tyrosine sulfation occurring in secretory and membrane proteins1."]
- Gas-phase argument — sulfotyrosine does not survive HCD:
  [PMID:40890505 "First, it is well established that tyrosine sulfation is extremely labile in the gas
  phase3–8. Typically, sulfate-retaining fragment ions are entirely absent following collisional
  activation such as HCD. Yet, the presumed sulfopeptide HCD MS/MS spectra (Yu et al., Fig. 1a and
  Extended Data Fig. 2g) show 100% sulfate retention, which would be remarkable."]
- Mass accuracy favours **phospho**tyrosine, not sulfotyrosine:
  [PMID:40890505 "the mass errors for phosphate-retaining b-type fragments are less than 3 ppm,
  whereas they range from 12.5 to 31.5 ppm for the annotated sulfate-retaining b ions"]
- Direct enzyme assay with recombinant SULT1B1 — **negative on histone H3, positive on T3**:
  [PMID:40890505 "Furthermore, we subjected rh-histone H3.2 to an rhSULT1B1 sulfation assay with PAPS.
  This assay was optimized with the SULT1B1 substrate, 3,3′,5-triiodo-L-thyronine, showing a high
  degree of sulfation (Extended Data, Figure 4). By contrast, no evidence of rh-histone H3.2 sulfation
  was observed."]
- Antibody caveat (relevant to every downstream paper that uses the anti-H3Y99sulf reagent):
  [PMID:40890505 "Additionally, Yu et al. generated an anti-H3Y99sulf antibody, validated with the
  MODified Histone Peptide Array. However, this assay only validates N-terminal histone binding.
  Because Y99 is near the C-terminus, additional validation of this antibody seems warranted.
  Therefore, it is possible that the CUT&Tag results presented in Yu et al. may be due to
  phosphorylation rather than sulfation."]
- Bottom line:
  [PMID:40890505 "Taken together, our new results along with reannotation of MS raw data from Yu et al.
  do not support the presence of histone H3 sulfation."]

### Status of the dispute

- The original paper's authors published a Reply the same day (PMID:40890506, Nat Chem Biol
  2025;21:1671-1674). Abstract-only in the cache, so I could not read their counter-arguments.
- An Author Correction to the 2023 paper appeared in Nat Chem Biol 2025;21:2014 (PMID:40890508).
  Abstract-only; its content could not be determined from the cache. (There is also an earlier
  2023 erratum, Nat Chem Biol 2023;19:1286.)
- **Neither the original nor the Reply has been retracted.** The dispute is live.

### The 2026 GAL3ST1 complication

A gastric-cancer paper attributes the *same* H3Y99sulf mark to a *different* enzyme, GAL3ST1:
[PMID:41686426 "Mechanistically, GAL3ST1 functioned as a histone sulfotransferase to sulfate nascent
histone H3 at tyrosine 99 (H3Y99sulf) in the cytosol of gastric cancer cells."]
It cites the 2023 SULT1B1 paper as established background and explicitly proposes an enzyme swap:
[PMID:41686426 "SULT1B1 in gastric cancer cells remained unchanged after coculture with CAFs,
suggesting that H3Y99sulf in gastric cancer cells might be regulated by alternative
sulfotransferases."]
I searched the full text of PMID:41686426 for "Youssef" and "refute": **the refutation is not cited**.
That paper's H3Y99sulf readouts rest on the anti-H3Y99sulf antibody and immunoblotting — exactly the
reagent and readout the refutation says need independent validation. See the GAL3ST1 notes.

## 3. Does GO even have a term for this?

Yes. `GO:0008476 protein-tyrosine sulfotransferase activity` exists
("3'-phosphoadenosine 5'-phosphosulfate + protein tyrosine = adenosine 3',5'-bisphosphate + protein
tyrosine-O-sulfate"), and `GO:0006478 peptidyl-tyrosine sulfation` exists on the BP side. A QuickGO
annotation query (goId=GO:0008476, goUsage=exact, taxonId=9606, retrieved 2026-09-17) returns 24 rows,
**all of them TPST1 (O60507) or TPST2 (O60704)** plus their isoform accessions — the two Golgi
tyrosylprotein sulfotransferases. Neither SULT1B1 nor GAL3ST1 appears.

So the ontology is fully capable of expressing the disputed claim; GO simply has not asserted it for
either enzyme. That is the correct outcome for a contested finding, and it is the finding of this
review.

## 4. Review decisions summary

Core: cytosolic aryl/phenol sulfotransferase (GO:0004062) acting in the cytosol (GO:0005829) on
small phenols and iodothyronines. Non-core: PAPS metabolism, flavonoid metabolism, biogenic amine
metabolism (conflicting evidence). Over-annotated: bare `protein binding` (5 IPI rows from
high-throughput interactome screens), `ethanol catabolic process`, `epithelial cell differentiation`.
Generalized parents (`GO:0008146`, `GO:0006790`) modified to the specific terms.
**No annotation action was changed on account of the histone-sulfation dispute, because GOA carries
no histone-sulfation annotation for this gene.**
