# A0A1V2LT98 (Pichia kudriavzevii / Issatchenkia orientalis PYC) notes

No deep-research provider was available. This file is a manual literature and record review.

## Identity
- UniProtKB A0A1V2LT98_PICKU, TrEMBL, PE 4 (predicted). ORF C5L36_0A02450 (EMBL AWU73641.1), proteome UP000249293 (chromosome 1), 1180 aa. No gene symbol in UniProt; the literature calls it PYC.
- It is the only pyruvate carboxylase in the P. kudriavzevii reference proteome. The other two biotin enzymes there are urea carboxylase/amidolyase entries (UniProt REST query, 2026-10-28).
- Family: PANTHER PTHR43778:SF2, NCBIfam TIGR01235, PIRSF001594. Domains: biotin carboxylation 22-474, ATP-grasp 144-341, carboxyltransferase 560-827, biotinyl 1098-1173, predicted biotinyl-Lys1139. No N-terminal extension relative to S. cerevisiae Pyc1p.
- PTN placement: the TreeGrafter rows place this protein at PTN001447571 (Saccharomycetaceae-Candida). In the PANTHER 19 tree for PTHR43778 (PANTHER API `treeinfo?family=PTHR43778`, 2026-10-28) that node's ancestry is PTN001821692 (LUCA) > PTN000429426 (Eukaryota) > PTN008685058 (Unikonts) > PTN000429427 (Opisthokonts) > PTN001050931 (Fungi) > PTN001050932 (Dikarya) > PTN000429467 (Ascomycota) > PTN000429468 (Pezizomycotina-Saccharomycotina) > PTN001050933 (Saccharomycetales) > PTN001447571. So the protein descends from both PAINT IBD nodes, PTN001821692 (activity, gluconeogenesis) and PTN001050931 (cytosol).
- The subfamily PTHR43778:SF2 is named "PYRUVATE CARBOXYLASE, MITOCHONDRIAL". The name comes from the mammalian members and says nothing about where fungal members are located. The PAINT cytosol assertion at the Fungi node (taxon:4751) is the relevant statement for localization.

## Literature
- Oxalic acid engineering in I. orientalis SD108. Endogenous PYC was integrated into an oxaloacetate hydrolase (Pcoah) strain [PMID:41617712 "To enhance oxalic acid production, we expressed the endogenous pyruvate carboxylase (PYC) in the strain OA_Pcoah."], with the stated rationale [PMID:41617712 "PYC facilitates the conversion of pyruvate into oxaloacetate (OAA), a precursor of oxalate."]. Copy number had no further effect [PMID:41617712 "Strains with two and three copies of PYC produced a similar oxalic acid titer of 1.52 g·L-1"], compared with 1.28 g/L for the parent OA_Pcoah strain. The paper reports no enzyme assay and does not name the PYC locus.
- In succinic acid engineering of SD108, endogenous pyc was integrated together with mdh, fumr and a heterologous frd [PMID:25159171 "By integration of endogenous genes pyc, mdh, fumr and an exogenous gene frd driven by endogenous strong promoters, the resultant strain exhibited significant improvement of the titer, yield and productivity"]. This is a combined, multi-gene effect.
- Budding-yeast PC is cytosolic [PMID:2665820 "In contrast to the general situation in fungi, plants and animals, pyruvate carboxylase was found to be a cytosolic enzyme in both yeasts."; PMID:2039506 "showed the isozyme to be located exclusively in the cytoplasm"], and its main role is anaplerotic [PMID:2039506 "has an important anaplerotic role in the production of oxaloacetate from pyruvate"].

## Review decisions (8 IEA rows)
- Pyruvate carboxylase activity: ACCEPT. Catalytic activity: MODIFY to that term.
- Biotin carboxylase activity: KEEP_AS_NON_CORE, as a partial reaction.
- ATP binding: KEEP_AS_NON_CORE. Metal ion binding: MODIFY to manganese ion binding (GO:0030145), based on the four PIRSR001594-3 Mn(2+)-binding site features. Nucleotide binding: TOO_GENERAL.
- Cytoplasm: MODIFY to cytosol (GO:0005829), based on the yeast localization papers and the PAINT Fungi-node cytosol assertion; core_functions location set to cytosol. Gluconeogenesis: ACCEPT. No NEW rows. Source defects: none.
- I did not add an oxalate-biosynthesis process term. In the engineered strain, oxalate is made by heterologous Pcoah; PYC supplies its substrate, which is not participation in the oxalate-forming step.

## CMMMech cross-check (allanite-leachate.yaml)
- `reference_proteome_id: UP000249646` is wrong. UP000249646 is the Metamycoplasma auris proteome (UniProt proteomes API). A0A1V2LT98 belongs to UP000249293 (Pichia kudriavzevii).
- The locus `B5S52_g3644` is not in UniProt. It may be an SD108 annotation locus from the Lu et al. data, but the paper text does not state it. The correspondence to A0A1V2LT98, which comes from a different strain's assembly (C5L36), rests on single-copy orthology in the reference proteome, not on a stated identity.
- The functional_role says PYC converts "pyruvate into oxaloacetate, the immediate substrate cleaved to oxalic acid". That is accurate for the engineered JL04 strain, where heterologous Pcoah does the cleavage, but it is an engineered pathway, not native oxalate metabolism. The flux data (equal titer at 2 and 3 copies) is laboratory shake-flask and bioreactor scale only.
