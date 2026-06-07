# CLGN (Calmegin) — Gene Review Notes

UniProt: O14967 (CLGN_HUMAN), 610 aa, gene HGNC:2060, chromosome 4. Precursor with N-terminal signal peptide (1–19); single-pass type I ER membrane protein (lumenal 20–471, TM 472–492, cytoplasmic 493–610).

## Identity and family
- Calmegin is a **testis-specific ER membrane molecular chaperone homologous to calnexin**. UniProt SIMILARITY: "Belongs to the calreticulin family" [file:human/CLGN/CLGN-uniprot.txt]. InterPro/Pfam signatures: IPR001580 (Calreticulin/calnexin), Calreticulin Pfam PF00262, ConA-like lectin domain (SSF49899), and the calnexin/calreticulin P-domain (Gene3D 2.10.250.10, SSF63887). PANTHER subfamily PTHR11073:SF7 = CALMEGIN; parent PTHR11073 = CALRETICULIN AND CALNEXIN.
- Like calnexin, it is a calcium-binding, lectin-type ER chaperone. KW: Calcium, Chaperone, Endoplasmic reticulum, Membrane, Signal, Transmembrane.

## Function (UniProt FUNCTION)
"Functions during spermatogenesis as a chaperone for a range of client proteins that are important for sperm adhesion onto the egg zona pellucida and for subsequent penetration of the zona pellucida. Required for normal sperm migration from the uterus into the oviduct. Required for normal male fertility. Binds calcium ions (By similarity)." [file:human/CLGN/CLGN-uniprot.txt]

## Key experimental evidence
- [PMID:9177349 "Calmegin is a testis-specific ER protein that is homologous to calnexin. Here we show that calmegin binds to nascent polypeptides during spermatogenesis... Homozygous-null male mice are nearly sterile even though spermatogenesis is morphologically normal and mating is normal. In vitro, sperm from homozygous-null males do not adhere to the egg extracellular matrix (zona pellucida)... calmegin functions as a chaperone for one or more sperm surface proteins that mediate the interactions between sperm and egg."] — Mouse Clgn knockout; the foundational functional paper. Establishes ER localization, chaperone binding to nascent polypeptides, and essential role in sperm–zona adhesion / fertilization. This is the basis for the TAS annotations to ER (GO:0005783) and single fertilization (GO:0007338).
- Mouse work (Ikawa et al.) showed calmegin is required for maturation/heterodimerization of sperm ADAM proteins fertilin (ADAM1/ADAM2) and ADAM3; loss disrupts sperm migration into the oviduct and zona binding (biological hint, consistent with UniProt FUNCTION). UniProt SUBUNIT: "Interacts with ADAM2 (By similarity)."

## Interactions
- UniProt SUBUNIT: "Interacts with PPIB. Interacts with ADAM2 (By similarity). Interacts with PDILT." [file:human/CLGN/CLGN-uniprot.txt]
- [PMID:17507649 "A developmentally regulated chaperone complex for the endoplasmic reticulum of male haploid germ cells."] — Calmegin interacts with PDILT (testis-specific protein disulfide isomerase-like protein), forming a germ-cell ER chaperone complex (analogous to the calnexin–ERp57 complex). Supports ER-membrane chaperone function.
- Region 317–350 = interaction with PPIB (peptidyl-prolyl cis-trans isomerase B); Region 521–610 disordered cytoplasmic tail.

## Localization
- ER membrane, single-pass type I (UniProt SUBCELLULAR LOCATION). HPA IDA also localizes to ER (GO:0005783, GO_REF:0000052). TAS ER from PMID:9177349.
- Nuclear envelope (GO:0005635) annotation is IEA from mouse ortholog (Ensembl GO_REF:0000107); the NE is continuous with the ER, so this is a low-value over-transfer, not a distinct biological site.

## Tissue specificity
- Testis-specific (at protein level) [PMID:9434179 cloning paper; UniProt TISSUE SPECIFICITY ECO:0000269|PubMed:9434179]. HPA: tissue enhanced (heart muscle, testis).

## Annotation assessment summary
- Core MF: lectin/calcium-binding ER molecular chaperone (calnexin family). protein folding chaperone (GO:0044183), unfolded protein binding (GO:0051082), calcium ion binding (GO:0005509) — all supported.
- Core CC: ER membrane (GO:0005789) / ER (GO:0005783).
- Core BP: protein folding (GO:0006457) during spermatogenesis; role in fertilization/sperm–zona binding (GO:0007338 single fertilization; GO:0007339 binding of sperm to zona pellucida).
- ERAD pathway (GO:0036503) IBA: generic transfer from calnexin/calreticulin family; calmegin's documented role is folding/assembly of spermatogenic clients (notably ADAMs), not demonstrated ERAD. Over-annotated phylogenetic transfer.
- Nuclear envelope (GO:0005635) IEA: low-value over-transfer (NE continuous with ER). Mark over-annotated / keep non-core.
