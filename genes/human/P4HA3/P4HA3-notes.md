# P4HA3 (Prolyl 4-hydroxylase subunit alpha-3) — gene review notes

UniProt: Q7Z4N8 (P4HA3_HUMAN), 544 aa precursor (signal 1-19; chain 20-544). Gene on human chr 11. EC=1.14.11.2.

## Core identity and function

P4HA3 is the third catalytic alpha subunit isoform (alpha(III)) of collagen prolyl 4-hydroxylase (C-P4H). The active enzyme is an alpha2-beta2 heterotetramer in which the beta subunit is protein disulfide isomerase (PDI / P4HB). It is an ER-lumenal, Fe(II)- and 2-oxoglutarate-dependent dioxygenase that hydroxylates proline in -X-Pro-Gly- triplets of procollagen to form trans-4-hydroxyproline, which is essential for the thermal stability of the collagen triple helix.

- Founding characterization: [PMID:14500733 "We report here on the cloning and characterization of a third vertebrate C-P4H alpha-subunit isoform, alpha(III)."]
- Tetramer subunit composition: [PMID:14500733 "The vertebrate enzymes are alpha 2 beta 2 tetramers, the beta-subunit being identical to protein-disulfide isomerase (PDI)."]
- Demonstrated catalytic activity on collagen: [PMID:14500733 "Coexpression of a recombinant human alpha(III) polypeptide with PDI in human embryonic kidney cells led to the formation of an active enzyme that hydroxylated collagen chains and a collagen-like peptide and appeared to be an [alpha(III)]2 beta 2 tetramer."]
- Reaction (UniProt): L-prolyl-[collagen] + 2-oxoglutarate + O2 = trans-4-hydroxy-L-prolyl-[collagen] + succinate + CO2; EC=1.14.11.2 [ECO:0000269|PubMed:14500733].
- Cofactors (UniProt): binds 1 Fe(2+) ion per subunit; requires L-ascorbate. Kinetics (PMID:14500733): KM 0.5 uM Fe(2+), 20 uM 2-oxoglutarate, 24 uM (Pro-Pro-Gly), 370 uM L-ascorbate.
- Catalytic domain: Fe2OG dioxygenase domain (422-529); Fe-binding residues 440, 442, 510; 2-oxoglutarate binding residue 520; TPR repeat (227-260) for peptide-substrate/PDI interaction.

## Subcellular location

ER lumen (UniProt: "SUBCELLULAR LOCATION: Endoplasmic reticulum lumen {ECO:0000305}"). Reactome curates ER-lumen localization (R-HSA-1650808, R-HSA-9918779). InterPro/IEA also assigns endoplasmic reticulum (GO:0005783). All consistent with a secreted-pathway, lumenal collagen-modifying enzyme.

## Tissue expression / context

Highly expressed in placenta, liver, and fetal skin; weakly in fetal epiphyseal cartilage, fetal liver, fibroblast, lung, skeletal muscle [PMID:14500733]. Also expressed in the fibrous cap of human atherosclerotic plaque / carotid lesions [PMID:12874193 cloned as the subunit "expressed in the fibrous cap of human atherosclerotic plaque"]. HPA: tissue-enhanced in blood vessel / smooth muscle. P4HA3 is frequently discussed in cancer contexts (proliferation/migration/EMT in various tumors) but those roles are downstream/contextual rather than the enzyme's core biochemical function.

## Annotation notes / GOA review reasoning

- GO:0004656 procollagen-proline 4-dioxygenase activity — core MF. EXP/PMID:14500733 (direct), plus IBA and IEA(EC/RHEA) support. ACCEPT.
- GO:0016222 procollagen-proline 4-dioxygenase complex (part_of, IBA) — the alpha2-beta2 (with PDI) tetramer. ACCEPT (the curated CC for the prolyl-4-hydroxylase complex).
- GO:0005506 iron ion binding (IEA, InterPro) — Fe(II) cofactor; correct, supports catalysis. ACCEPT.
- GO:0016705 oxidoreductase activity, acting on paired donors... O2 (IEA, InterPro) — parent dioxygenase MF; correct but generic relative to GO:0004656. ACCEPT (general MF).
- GO:0031418 L-ascorbic acid binding (IEA, keyword/InterPro) — ascorbate cosubstrate; correct. ACCEPT.
- GO:0005783 endoplasmic reticulum (IEA) and GO:0005788 ER lumen (IEA + 2x Reactome TAS) — correct compartment. ACCEPT.
- GO:0005515 protein binding (IPI x4 references) — all four references (PMID:25416956, 26871637, 31515488, 32296183) are large-scale binary interactome / Y2H reference maps. The partner lists are dominated by biologically unrelated proteins (KRTAPs, MAGEs, transcription factors, etc.); these are uninformative bare protein-binding captures, not the functional PDI/collagen interactions. Per curation guidance, keep as non-core. None elevated to core; do not REMOVE (real IntAct captures).
  - 25416956 = "A proteome-scale map of the human interactome network" (HuRI/Y2H) [PMID:25416956 "a systematic map of ?14,000 high-quality human binary protein-protein interactions"].
  - 26871637 = "Widespread Expansion of Protein Interaction Capabilities by Alternative Splicing" (Y2H isoform interactome).
  - 31515488 = "Extensive disruption of protein interactions by genetic variants..." (Y2H variant interactome).
  - 32296183 = "A reference map of the human binary protein interactome" (HuRI).
- No experimental cancer-context BP annotations are present in this GOA; GO:0030199 collagen fibril organization (IBA) appears in the UniProt DR cross-references but is NOT in the goa.tsv, so it is not part of existing_annotations here.

## Cited reference quality summary

- PMID:14500733 — HIGH relevance, VERIFIED (founding biochemical characterization; abstract-only cache but anchored by EC/Rhea reaction and EXP GOA evidence).
- PMID:25416956 / 26871637 / 31515488 / 32296183 — LOW relevance (bare protein binding from HT interactome screens), VERIFIED as correctly-cited interactome papers.
</content>
