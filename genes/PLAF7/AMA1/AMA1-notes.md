# AMA1 (apical membrane antigen 1, PF3D7_1133400, UniProt Q7KQK5) notes

**Automated deep research was unavailable in this environment** (Falcon auth failure,
invalid OpenAI key). These notes are a manual literature review based on the UniProt
record, the cached publications cited in GOA, and one additional primary paper
(PMID:21788485) fetched for this review. No `-deep-research-*.md` file was created.

## Identity and structure

- UniProt Q7KQK5 (TrEMBL, unreviewed; no gene symbol, ORF PF3D7_1133400), 622 aa,
  single-pass type I membrane protein of the apicomplexan AMA1 family.
- Many crystal structures of the ectodomain (residues ~97-442), e.g. PDB 1Z40, 3ZWZ
  (with a PfRON2 peptide), 3SRJ (with R1 peptide).
- Cloned in 1989 and named for its apparent apical localization
  [PMID:2701947 "This antigen is designated apical membrane antigen 1 because it appears to be located in the apical complex."]
  and transport to the merozoite surface
  [PMID:2701947 "Apical membrane antigen 1 appears to be transported to the merozoite surface near the time of schizont rupture."]

## Localization

- Microneme: unprocessed precursor resides in micronemes of schizonts
  [PMID:12228305 "We localized unprocessed PfAMA1 to the microneme organelles of the intraerythrocytic schizont."]
  [PMID:12228305 "AMA1 is synthesized as an 83-kDa precursor protein that traffics to and is N-terminally processed within the micronemes."]
- Merozoite surface after prodomain removal
  [PMID:12228305 "Apical membrane antigen 1 of Plasmodium falciparum (PfAMA1) contains an N-terminal propeptide that is removed prior to the translocation of the mature protein onto the merozoite surface."]
- Moving/tight junction during invasion, with RON complex
  [PMID:22737069 "The MJ contains two key parasite components: the surface protein Apical Membrane Antigen 1 (AMA1) and its receptor, the Rhoptry Neck Protein (RON) complex, which is targeted to the host cell membrane during invasion."]
  No GO CC term exists for the moving junction (OLS search returned nothing).
- GOA `membrane` (IEA) is correct but too general; plasma membrane (merozoite surface)
  plus microneme is more informative.
- `apical complex` (TAS, 1989): true but general; micronemes are apical complex
  organelles and `microneme` is already annotated by IDA.

## Molecular function: RON2 binding

- AMA1 binds directly to RON2, a rhoptry-neck protein that the parasite inserts into the
  host erythrocyte membrane
  [PMID:22737069 "In particular, RON2, a transmembrane component of the RON complex, interacts directly with AMA1."]
  [PMID:22737069 "The receptor-binding site of PfAMA1 comprises the hydrophobic groove and a region that becomes exposed by displacement of the flexible Domain II loop."]
  [PMID:22737069 "Mutations of key contact residues of PfRON2 and PfAMA1 abrogate binding between the recombinant proteins."]
- Binding of RON2 to the AMA1 hydrophobic pocket commits the merozoite to invasion
  [PMID:21788485 "Collectively, these results identify the binding of RON2 to the hydrophobic pocket of AMA1 as the step that commits Plasmodium merozoites to RBC invasion and point to RON2 as a potential vaccine candidate."]
- PfAMA1 coimmunoprecipitates with PfRON4 (likely indirect, via the RON2/RON4/RON5
  complex)
  [PMID:16835460 "Plasmodium falciparum apical membrane antigen 1 (PfAMA1) coimmunoprecipitates with the Plasmodium homologue of TgRON4"]
- Because RON2 sits in the host membrane, AMA1-RON2 binding is effectively binding to a
  component exposed on the host cell surface, supporting `host cell surface binding`.
  However, RON2 is a parasite protein, so `host cell surface receptor binding`
  (GO:0046789; a host receptor) would be inaccurate.

## Biological process: erythrocyte invasion

- Conditional DiCre knockdown in P. falciparum
  [PMID:24571085 "These results show that PfAMA1 is an essential protein for merozoite invasion in P. falciparum and either directly or indirectly plays a role in resealing of the red blood cell at the posterior end of the invasion event."]
  [PMID:24571085 "The interaction between PfAMA1 and another parasite protein called rhoptry neck protein 2 (RON2) is essential for tight junction formation, which commits the merozoite for invasion (Srinivasan et al."]
- Dissenting genetic data (P. berghei and Toxoplasma knockouts): AMA1 is an adhesin that
  helps attachment but is dispensable for penetration
  [PMID:24108241 "Therefore, apical membrane antigen 1, rather than an essential invasin, is a dispensable adhesin of apicomplexan zoites."]
  [PMID:24108241 "Therefore, as with the Toxoplasma tachyzoite, AMA1 favours Plasmodium merozoite attachment to, but not internalization into, the host cell."]
  Note: the full text of PMID:24108241 uses P. berghei and T. gondii mutants; I found no
  P. falciparum experiment, so the IDA `host cell surface binding` on PfAMA1 is a
  cross-species inference from a knockout adhesion phenotype. The function is still
  plausible for PfAMA1 via RON2 binding and is supported by the P. falciparum
  structural work, so it is accepted as the core molecular function.
  Yap et al. discuss that residual AMA1 or compensation (e.g., by the paralog-like
  AMA1 homologues/MAEBL in the KO lines) may explain the discrepancy
  [PMID:24571085 "Since these merozoites could still invade despite not having any detectable AMA1 these authors concluded that AMA1 was not essential for tight junction formation or invasion (Bargieri et al."]
- GO term `symbiont entry into host` (GO:0044409) is appropriately parasite-side (the
  merozoite enters the host erythrocyte) but is less specific than the evidence supports.
  The child "symbiont entry into host cell" (GO:0046718) is defined around breaching the
  membrane and releasing the symbiont or its genome into the cytoplasm, which does not fit
  apicomplexan invasion. Its own descendant GO:0085017 "entry into host cell by a
  symbiont-containing vacuole" does: OLS gives its definition as invasion forming "a
  vacuole in which the symbiont resides", beginning with attachment to a host membrane
  that invaginates and ending when that membrane closes behind the new vacuole -- the
  moving junction AMA1 anchors, and the cited phenotype is precisely a failure to seal the
  parasitophorous vacuole. GOA already uses GO:0085017 for P. falciparum MSP1 (IDA) and
  CSP (IMP), so the GO:0044409 row is MODIFYed to GO:0085017 for accuracy and for
  consistency with the rest of the invasion machinery.
- `adhesion of symbiont to host cell` (GO:0044650) is supported by the Bargieri KO
  adhesion phenotypes in P. berghei/T. gondii but not tested directly in P. falciparum;
  not proposed as NEW (conservative).

## Decisions summary

| Term | Evidence | Action |
|---|---|---|
| protein binding (RON4) | IPI | MODIFY -> host cell surface binding |
| protein binding (RON2) | IPI | MODIFY -> host cell surface binding |
| membrane | IEA | MODIFY -> plasma membrane |
| apical complex | TAS | MODIFY -> microneme |
| microneme | IDA | ACCEPT |
| symbiont entry into host | IMP | ACCEPT |
| host cell surface binding | IDA | ACCEPT (core MF via RON2 binding at the host membrane) |

Also proposed a new cellular component term for the apicomplexan moving (tight)
junction, since OLS returned no GO term for it and it is the structure in which AMA1
actually acts.
