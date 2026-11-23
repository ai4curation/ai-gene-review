# Ran (Drosophila melanogaster, Q9VZ23, FBgn0020255, CG1404) - manual literature synthesis

No deep-research API was available for this session. This file is a manual synthesis
from the cached publications in `publications/` and the UniProt record; every claim
carries its source.

## Identity and family

- Ran (Ran10A, CG1404) is the single canonical Ran GTPase of *D. melanogaster*, 216 aa,
  Swiss-Prot reviewed (Q9VZ23). UniProt: "Belongs to the small GTPase superfamily. Ran family."
  InterPro IPR002041 (Ran_GTPase), Pfam PF00071 (Ras), PANTHER PTHR24071:SF0
  (GTP-BINDING NUCLEAR PROTEIN RAN). [Ran-uniprot.txt]
- Mg2+ cofactor and nucleotide-binding residues are by similarity to human RAN (P62826).
  [Ran-uniprot.txt]

## Core biochemistry and nucleocytoplasmic transport (conserved, by similarity)

- UniProt FUNCTION (by similarity to P62826): Ran "Switches between a cytoplasmic GDP- and
  a nuclear GTP-bound state by nucleotide exchange and GTP hydrolysis"; import receptors
  release cargo on binding RanGTP, export receptors load cargo with RanGTP, so Ran
  "ensures the directionality of the transport". [Ran-uniprot.txt]
- Review: nuclear import is "a spatially and temporally organized cycle of interactions
  between cargoes, carriers and the Ran GTPase" [PMID:17287812, abstract only].
- Cesario & McKim summarise the fly pathway: RCC1 (the GEF) is chromatin bound, RanGAP
  cytoplasmic, and "Once inside the nucleus, RanGTP binds importin β, releasing importin α
  and NLS containing proteins" [PMID:22100918].
- Tamo, a Dorsal-binding protein, "binds the Ras family small GTPase, Ran"
  [PMID:12653959, abstract only]; Tamo modulates Dorsal nuclear import.

## Mitosis and spindle assembly

- Trieselmann & Wilde 2002: in syncytial embryos, RCC1 is on chromatin during mitosis while
  "Ran and RanL43E, an allele locked in the GTP-bound state, localize around the spindle"
  [PMID:12121620, abstract only].
- Silverman-Gavrila & Wilde 2006: "Ran is required before metaphase for spindle assembly and
  chromosome alignment and after metaphase for chromosome segregation and spindle midbody
  organization"; acts partly by targeting Aurora A, KLP61F and KLP3A to spindles
  [PMID:16481399, abstract only]. This paper is not cited in GOA.
- A ran mutation (G0075) is lethal [PMID:22100918, citing Peter et al. 2002].

## Female meiosis and early embryo

- Cesario & McKim 2011 expressed RanT24N (GDP-locked, dominant negative) and RanQ69L
  (GTP-locked) in the germline. "Females expressing a dominant-negative form of Ran have
  fertility defects", but RanGTP is not essential for acentrosomal meiotic spindle assembly;
  "the most important function of the Ran pathway in spindle assembly appears to be in the
  tapering of microtubules at the spindle poles". RanGTP also promotes sperm-aster
  microtubules needed for pronuclear fusion. Ran "was nuclear during interphase and then
  overlapped with the spindle during metaphase and anaphase" [PMID:22100918, full text].

## Spindle orientation (neuroblast pathway, S2 induced-polarity assay)

- Wee et al. 2011: "the Canoe RA domains can interact directly with GTP-loaded Ran" (GST
  pulldown with GMPPNP- vs GDP-loaded Ran). ran RNAi in S2 cells expressing Ed:PinsTPR+LINKER
  reduced spindle orientation; canoe+ran double RNAi resembled canoe alone (same pathway),
  whereas ran+dlg double RNAi was more severe (parallel pathways). "Mud failed to localize
  to Ed:PinsTPR+LINKER crescents after ran RNAi". Ran was recruited to cortical crescents
  formed by Ed:GFP:CnoRA (an engineered transmembrane tether), i.e. cortical Ran here is
  CanoeRA-dependent and artificially induced [PMID:22024168, full text].

## Oogenesis: nuclear pore / annulate lamellae biogenesis

- Hampoelz et al. 2019: Nups condense into granules transported on microtubules that give
  rise to annulate lamellae (AL) and NPCs. "RanT24N expression reduced both AL and Nup358
  condensates", whereas RanQ69L stimulated Nup358 condensation; the authors propose
  "Ran-regulated NTR chaperoning could spatially control Nup condensation in vivo, as a
  prerequisite for AL biogenesis" [PMID:31626769, full text].

## Points relevant to annotation

- Ran is a soluble shuttling GTPase, not a structural NPC subunit and not a subunit of the
  importin alpha/beta NLS-import heterodimer (RanGTP dissociates it).
- In metazoa bulk mRNA export uses NXF1/NXT1 (sbr/Nxt1 in flies) and is largely Ran
  independent; the poly(A)+ mRNA export IBA rests on yeast seeds (S. pombe spi1,
  S. cerevisiae GSP1). This is background knowledge, not a quoted fly experiment.
