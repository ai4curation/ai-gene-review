# RPE65 (human, Q16518) — review notes

## Identity and family
- RPE65 = **retinoid isomerohydrolase**, EC 3.1.1.64 (and a secondary EC 5.3.3.22, lutein → meso-zeaxanthin isomerase). RecName in UniProt: "Retinoid isomerohydrolase" [file:human/RPE65/RPE65-uniprot.txt "RecName: Full=Retinoid isomerohydrolase"].
- Member of the **carotenoid oxygenase family** [file:human/RPE65/RPE65-uniprot.txt "Belongs to the carotenoid oxygenase family"]; Pfam PF03055 (RPE65), InterPro IPR004294; PANTHER subfamily PTHR10543:SF57 "RETINOID ISOMEROHYDROLASE".
- 533 aa, RPE-specific 65 kDa protein. HGNC:10294, chromosome 1.

## Core molecular function
- The central enzyme of the **visual (retinoid) cycle**: converts **all-trans-retinyl ester (produced by LRAT) to 11-cis-retinol** in a coupled ester-hydrolysis + trans→cis isomerization. 11-cis-retinol is then oxidized (by 11-cis-RDH) to 11-cis-retinal, the chromophore that regenerates rod/cone opsins.
  - UniProt FUNCTION: "Critical isomerohydrolase in the retinoid cycle involved in regeneration of 11-cis-retinal, the chromophore of rod and cone opsins. Catalyzes the cleavage and isomerization of all-trans-retinyl fatty acid esters to 11-cis-retinol which is further oxidized by 11-cis retinol dehydrogenase to 11-cis-retinal for use as visual chromophore" [file:human/RPE65/RPE65-uniprot.txt].
  - Established as *the* isomerohydrolase of the visual cycle in [PMID:16116091 "RPE65 is the isomerohydrolase in the retinoid visual cycle"] (UniProt ref, not cited in GOA table but supports the core MF).
- Catalytic-activity Rhea reactions in UniProt:
  - RHEA:31771: "an all-trans-retinyl ester + H2O = 11-cis-retinol + a fatty acid + H(+)"; EC 3.1.1.64 (ECO:0000269|PubMed:29659842). → maps to GO:0052885 (all-trans-retinyl-ester hydrolase, 11-cis retinol forming activity).
  - RHEA:31775: "all-trans-retinyl hexadecanoate + H2O = 11-cis-retinol + hexadecanoate + H(+)"; EC 3.1.1.64 (ECO:0000269|PubMed:25112876). → maps to GO:0052884 (all-trans-retinyl-palmitate hydrolase, 11-cis retinol forming activity).
- **GO:0052885** ("all-trans-retinyl-ester hydrolase, 11-cis retinol forming activity") is the most precise GO MF for the primary activity; **GO:0052884** (palmitate-specific) is the more specific substrate variant. Both are directly supported by experimental annotations (IDA/EXP: PMID:25112876, PMID:29659842).

## Cofactor
- Iron-dependent: "Binds 1 Fe(2+) ion per subunit" [file:human/RPE65/RPE65-uniprot.txt]. Catalytic Fe-binding residues His-180, His-241, His-313, His-527 (BINDING "Fe cation ... catalytic"). Mutagenesis of His-180/His-241/His-313/Glu-469/His-527 abolishes isomerohydrolase activity (PMID:16198348, UniProt ref [8]).
- GOA has GO:0046872 (metal ion binding, IEA UniProtKB-KW). The more informative term is GO:0005506 (iron ion binding) — proposed in core_functions.

## Secondary function: lutein → meso-zeaxanthin isomerase
- RPE65 is also the **lutein → meso-zeaxanthin isomerase** in the vertebrate eye [PMID:28874556 "RPE65 ... is also the isomerase enzyme responsible for the production of meso-zeaxanthin in vertebrates"; "overexpression of either chicken or human RPE65 in cell culture leads to the production of meso-zeaxanthin from lutein"]. EC 5.3.3.22; UniProt reaction "lutein = (3R,3'S)-zeaxanthin".
- GOA captures this as GO:0016853 (isomerase activity, IDA) and GO:1901827 (zeaxanthin biosynthetic process, IDA), both PMID:28874556. The generic "isomerase activity" is an under-specific placeholder for this function.

## Membrane association / palmitoylation
- Palmitoylation at **Cys-112** (by LRAT) drives membrane association and is essential for isomerohydrolase activity: "the newly identified Cys-112 palmitylation site is essential for the membrane association and activity of RPE65" [PMID:19049981]; "C112A lost its enzymatic activity" [PMID:19049981]. Additional palmitoyl-Cys at 231, 329, 330 (by similarity).
- Membrane/soluble equilibrium: palmitoylated (membrane) form binds all-trans-retinyl esters; soluble (unpalmitoylated) form binds all-trans-retinol (vitamin A) [file:human/RPE65/RPE65-uniprot.txt "Palmitoylation by LRAT regulates ligand binding specificity"].

## Subcellular location
- UniProt: **Cytoplasm** (by similarity), **Cell membrane; Lipid-anchor** (EXP, PMID:19049981), **Microsome membrane** (by similarity). Attached to membrane via lipid anchor when palmitoylated; soluble when unpalmitoylated [file:human/RPE65/RPE65-uniprot.txt].
- GO IDA (PMID:29659842) places RPE65 at the **endoplasmic reticulum membrane** (GO:0005789) — consistent with the RPE smooth ER / microsomal localization where the visual-cycle machinery resides. This is the best-supported specific CC.
- GOA also has GO:0005886 (plasma membrane): EXP (PMID:19049981) + TAS Reactome + IEA. The EXP/PMID:19049981 evidence supports "cell membrane; lipid-anchor" association generally; the Reactome-modeled reaction places RPE65 at the RPE membrane. Plasma-membrane specificity is weakly supported vs the ER/microsomal membrane, but is an experimentally-anchored membrane call — keep as non-core.

## Interaction with MYO7A
- UniProt SUBUNIT: "Interacts with MYO7A; this mediates light-dependent intracellular transport of RPE65" (PMID:21493626). Light-dependent redistribution within RPE cells.
- GOA "protein binding" IPI annotations are to **CCT6B (Q92526)**, a CCT/TRiC chaperonin subunit, from BioPlex AP-MS ([PMID:28514442], [PMID:33961781]). These are generic high-throughput interactions (bait-prey AP-MS), likely reflecting chaperonin-assisted folding rather than a functionally informative partnership. Bare "protein binding" → mark as over-annotated (do not remove IPI per policy).

## Biological process
- **Visual perception** (GO:0007601, TAS PMID:9326941) and **retinoid/retinal/retinol/vitamin A metabolic process** are all well supported. RPE65 is essential for 11-cis-retinal production for both rods and cones [PMID:17848510 "Human cone photoreceptor dependence on RPE65 isomerase", UniProt ref].
- IMP annotations GO:0001895 (retina homeostasis) and GO:0050908 (detection of light stimulus involved in visual perception) from PMID:15557452: this is a homozygosity-mapping case report identifying the R515W RPE65 mutation "known to cause Leber's congenital amaurosis" in an arRP patient [PMID:15557452]. Human loss-of-function → visual/retinal phenotype; these BP terms are reasonable phenotype-derived annotations though downstream of the core enzymatic MF.

## Disease
- **Leber congenital amaurosis 2 (LCA2)** [MIM:204100] and **retinitis pigmentosa 20 (RP20)** [MIM:613794] — recessive; **RP87** [MIM:618697] — dominant (D477G, toxic gain-of-function; PMID:29659842). Many pathogenic variants documented [file:human/RPE65/RPE65-uniprot.txt].
- RPE65-associated LCA is the target of **voretigene neparvovec (Luxturna)** gene therapy (DrugBank DB13932 in UniProt DR lines).

## Over-annotation / questionable IEA calls
- **GO:0003834 (beta-carotene 15,15'-dioxygenase activity)** — IBA. This is the activity of the paralog BCO1/BCMO1, not RPE65. RPE65 is a non-oxygenase member of the carotenoid-oxygenase family; it isomerizes rather than cleaving β-carotene. Over-annotation from the family-level IBA. Mark as over-annotated.
- **GO:0016702 (oxidoreductase, incorporation of two atoms of oxygen)** — IEA/InterPro (family-level, dioxygenase). RPE65 is not a dioxygenase; it does not incorporate O2. Clearly-wrong IEA → REMOVE.
- **GO:0120254 (olefinic compound metabolic process)** — IEA/ARBA, extremely generic; grandparent-level. Over-annotation.
- **GO:0001786 phosphatidylserine binding / GO:0031210 phosphatidylcholine binding / GO:1901612 cardiolipin binding** — all ISS from bovine (Q28175). RPE65 is membrane-associated via palmitoyl anchor and its physiological ligands are retinoids/retinyl esters; specific phospholipid-headgroup binding is not an established function. These are weakly-supported ISS transfers; over-annotation of generic membrane-lipid affinity.
- **GO:0005634 nucleus / GO:0044297 cell body / GO:0007623 circadian rhythm / GO:0009416 response to light stimulus / GO:0003407 neural retina development / GO:0043010 camera-type eye development** — Ensembl orthology IEA (GO_REF:0000107) transferred from rodent orthologs. Nucleus is implausible for a microsomal/membrane isomerohydrolase; circadian rhythm / response to light / developmental terms are plausible-but-peripheral orthology transfers, not core. Keep developmental/process ones as non-core; nucleus is a clearly-wrong CC IEA → REMOVE.

## Proposed core functions (final)
- MF: GO:0052885 (all-trans-retinyl-ester hydrolase, 11-cis retinol forming activity) — primary isomerohydrolase.
- MF: GO:0052884 (all-trans-retinyl-palmitate hydrolase, 11-cis retinol forming activity) — specific substrate variant.
- MF: GO:0005506 (iron ion binding) — catalytic Fe(2+) cofactor.
- BP: GO:0007601 (visual perception).
- BP: GO:0001523 (retinoid metabolic process) [and GO:0042574 retinal metabolic process].
- Secondary MF/BP: GO:1901827 (zeaxanthin biosynthetic process) via lutein→meso-zeaxanthin isomerase activity — non-core, eye-specific carotenoid metabolism.
