# LCI5 / EPYC1 (Chlamydomonas reinhardtii, UniProt Q94ET8) - curation notes

## Identity

- UniProt Q94ET8 (gene name Lci5, 321 aa, TrEMBL) is the same protein as
  **EPYC1, Essential Pyrenoid Component 1**, locus **Cre10.g436550**.
  - [PMID:27166422 "Strikingly, a fourth protein, previously identified as a low-CO 2 –induced nuclear-encoded protein (LCI5; Cre10.g436550) ( 24 ), was found in the low-CO 2 pyrenoid fraction with comparable abundance to Rubisco"]
  - [PMID:28938114 "a protein called Essential Pyrenoid Component 1 (EPYC1; also known as LCI5) links Rubisco holoenzymes together to form the pyrenoid matrix"]
  - The UniProt entry cross-references PDB 7JFO (EPYC1 residues 49-72 bound to Rubisco) from He et al. 2020 (PMID:33230314), and CD-CODE lists it as a pyrenoid condensate component.
- The folder and `gene_symbol` stay as LCI5 (the UniProt gene name). EPYC1 is recorded under `aliases`.

## Molecular function: multivalent Rubisco linker / condensate scaffold

- The protein is disordered and made of repeats [PMID:27166422 "Here we find that Rubisco accumulation in the pyrenoid of the model alga Chlamydomonas reinhardtii is mediated by a disordered repeat protein, which we term Essential Pyrenoid Component 1 (EPYC1)."]
- Four ~60-aa repeats were originally described. Later structural work defines five Rubisco-binding regions [PMID:33230314 "We find that EPYC1 consists of five evenly spaced Rubisco-binding regions that share sequence similarity."]
- The binding site is the pair of alpha-helices on the Rubisco small subunit [PMID:33230314 "Together, our data demonstrate that EPYC1’s Rubisco-binding regions bind to the Rubisco small subunit α-helices via salt-bridge interactions and a hydrophobic interface, enabling the condensation of Rubisco into the phase separated matrix."]. This explains the older result that the SSU helices are needed for a pyrenoid [PMID:23112177 "higher plant-like helices knock out the pyrenoid, whereas native algal helices establish a pyrenoid"].
- Each repeat adds binding strength, so the protein is modular [PMID:31504763 "each repeat has an additive effect on SSU interaction"].
- Rubisco and EPYC1 alone are enough for phase separation [PMID:30498228 "Here we use biochemical reconstitution to demonstrate that Rubisco and EPYC1 are the two components necessary and sufficient to bring about a liquid-liquid phase separation (LLPS) that recapitulates the liquid-like behavior reported for the microalgal pyrenoid"]
- The condensate is a codependent network, not an EPYC1 lattice [PMID:33230314 "Cryo-electron tomography supports a model in which EPYC1 and Rubisco form a codependent multivalent network of specific low-affinity bonds, giving the matrix liquid-like properties."]. Wunder et al. explicitly reject a homotypic "scaffold hypothesis" [PMID:30498228 "In contrast to the scaffold hypothesis we find EPYC1 is relatively soluble and only homotypically phase separates at concentrations of 100 µM or more in the presence of a crowding agent."]. This does not argue against GO:0140693 *molecular condensate scaffold activity*. That GO term is defined as "binding and bringing together two or more macromolecules in contact, permitting those molecules to organize as a molecular condensate", and it does not require EPYC1 to self-assemble.
- Interface mutations block binding, phase separation and pyrenoid formation [PMID:33230314 "Interface mutations disrupt binding, phase separation and pyrenoid formation."]
- EPYC1 is sufficient to condense Rubisco in a heterologous host, an Arabidopsis line with a Chlamydomonas-type SSU [PMID:33298923 "Expression of EPYC1 in the Arabidopsis line S2Cr results in condensate formation."]
- Condensation does not change Rubisco's catalytic activity [PMID:30498228 "Rubisco enzyme activity (indicated as 3PG production) is unaffected by droplet formation."]. EPYC1 is therefore not a Rubisco activator and has no catalytic role in carbon fixation.
- EPYC1 and Rubisco also form complexes in the dilute phase [PMID:36611062 "The majority of these complexes contain exactly one Rubisco molecule."]
- Extant and ancestral EPYC1 homologues were tested for their effect on carboxylation in reconstituted synthetic pyrenoids [PMID:42601498 "In the following, we tested all extant and ancestral sequences with respect to carboxylation rate enhancement and maximum amount of 3-PG produced using the radioisotope assay described above."]

## Localization

- The protein is in the pyrenoid matrix [PMID:27166422 "Venus-tagged EPYC1 showed clear colocalization with mCherry-tagged RBCS in the pyrenoid"]; [PMID:28938113 "essential pyrenoid component 1 (EPYC1), a Rubisco linker protein"]
- Part of it disperses into the stroma during division [PMID:28938114 "A portion of the RbcS1-Venus and EPYC1-Venus signals rapidly dispersed from the pyrenoid matrix into the stroma for ~20 minutes near the end of chloroplast and pyrenoid division"]
- **The 2006 thylakoid result needs reinterpreting.** Turkina et al. reported [PMID:16572472 "Immunoblotting with Lci5-specific antibodies revealed that Lci5 was localized in chloroplast and confined to the stromal side of the thylakoid membranes."]. That study predates the identification of the pyrenoid matrix and used fractionation. The pyrenoid is crossed by thylakoid-derived tubules, and EPYC1 has no transmembrane domain. Mackinder et al. selected EPYC1-like proteins in part for the "absence of transmembrane domains" (PMID:27166422). I treat the thylakoid membrane location as co-fractionation and do **not** propose GO:0009535. The earlier draft's NEW proposal for that term was dropped.

## Phenotype (necessity evidence)

- The epyc1 mutant cannot grow photoautotrophically at low CO2, and complementation rescues it [PMID:27166422 "the epyc1 mutant showed defective photoautotrophic growth in low CO 2 , which was rescued by high CO 2 and by reintroducing the EPYC1 gene"]
- The mutant mislocalizes Rubisco [PMID:27166422 "We conclude that EPYC1 is required for Rubisco localization to the pyrenoid not only at low CO 2 , but also at high CO 2 ."]
- The canonical matrix is absent in the mutant [PMID:33177094 "First, in a mutant lacking EPYC1, a pyrenoid-like structure still assembles around the tubules, containing some Rubisco enclosed by a starch sheath, although the canonical matrix is absent (13)."]

## Phosphorylation and regulation

- The protein is phosphorylated in its repeats at low CO2 [PMID:16572472 "The phosphorylation sites were mapped in the tandem repeats of Lci5 ensuring phosphorylation of four serine and three threonine residues in the protein."]; [PMID:16572472 "Phosphorylation of Lci5 and UEP occurred strictly at limiting CO2; it required reduction of electron carriers in the thylakoid membrane, but was not induced by light."]
- The interactome finds 14-3-3 proteins and a kinase with EPYC1 [PMID:28938113 "EPYC1 interacts with two 14-3-3 proteins FTT1 and FTT2."]
- KEY1 is the main kinase. It targets the Rubisco-binding regions and drives dissolution of the condensate [PMID:41845050 "these results establish that KEY1 is the primary kinase of EPYC1 and suggest that KEY1 preferentially phosphorylates the Rubisco-binding regions of EPYC1"]; [PMID:41845050 "We show that KEY1 localizes to the condensates and promotes their dissolution by disrupting interactions between their core constituents, the CO2-fixing enzyme Rubisco and its linker protein EPYC1, through EPYC1 phosphorylation."]
- Interpretation: the low-CO2 phosphorylation reported in 2006 is regulation of the scaffold activity. It is not evidence for a separate signalling or "response to CO2" function.

## Review decisions (2026-10 re-review)

GOA has no rows for Q94ET8, so every entry is a NEW proposal.

| Term | Decision | Rationale |
|---|---|---|
| GO:0140693 molecular condensate scaffold activity | NEW (IDA, PMID:30498228), core | Reconstitution, structure and mutagenesis |
| GO:1990732 pyrenoid | NEW (IDA, PMID:27166422), core location | Pyrenoid proteomics and live imaging |
| GO:0140694 membraneless organelle assembly | NEW (IMP, PMID:27166422), core BP | Passes the participation test as the scaffold case; comparator FUS/Wnk carry 0140693+0140694 |
| GO:0009570 chloroplast stroma | NEW (IDA, PMID:28938114), non-core | Dilute-phase pool seen during division |
| GO:0005515 protein binding | dropped | Uninformative; replaced by 0140693 |
| GO:0043169 cation binding | dropped | No evidence |
| GO:0009535 chloroplast thylakoid membrane | dropped | 2006 fractionation superseded by the pyrenoid matrix localization |
| GO:0015976 carbon utilization | dropped | Too broad and vague |
| GO:0015979 photosynthesis | dropped | Too broad; EPYC1 does not catalyse any photosynthetic step |
| GO:0071244 cellular response to carbon dioxide | dropped | Based only on expression induction |

Terms considered and rejected:

- GO:0015977 carbon fixation. Rubisco performs the carboxylation, and its activity is unchanged by condensation. EPYC1 only organises Rubisco, so the participation test fails.
- GO:0046863 Rubisco activator activity. Activity is unchanged by condensation.
- GO:0110102 ribulose bisphosphate carboxylase complex assembly. Holoenzyme assembly is normal without the EPYC1 interaction, as shown by the SSU helix-swap lines (PMID:27166422 discussion).

## Ontology gap

- GO has no "pyrenoid assembly" BP. GO:0140694 is the closest term. This is recorded as an ONTOLOGY knowledge gap.

## Other files

- `LCI5-deep-research.md` (OpenAI) is outdated. It does not recognise EPYC1 and claims that no mutant phenotype or structure exists. It is marked LOW_QUALITY in `reference_review` and is not used as evidence.
- `LCI5-pathway.md` predates this re-review and still describes LCI5 as a thylakoid phosphoprotein of unknown function. It should be regenerated.
