# BNIP3 (Drosophila melanogaster, CG5059, FBgn0037007, UniProt Q9VPD6) - review notes

## Identity and family

- 201-aa protein with a single C-terminal transmembrane helix (Phobius TM 166-188), so it is a
  tail-anchored protein. It is in the NIP3/BNIP3 family (InterPro IPR010548, Pfam PF06553,
  PANTHER PTHR15186:SF5) [file:DROME/BNIP3/BNIP3-uniprot.txt "Belongs to the NIP3 family."].
- It is the only fly ortholog of mammalian BNIP3 and BNIP3L/NIX
  [PMID:40801807 "BNIP3 is the sole fly ortholog of mammalian NIX and BNIP3."].
- Domain architecture is conserved: LIR, MER, TMD
  [PMID:40801807 "Drosophila BNIP3, the sole ortholog of NIX and BNIP3, contains LIR, MER, and TMD, similar to its mammalian counterparts."].
- My alignment (file:DROME/BNIP3/BNIP3-bioinformatics/RESULTS.md) maps the human LIR WVEL to fly
  WIEL (16-19) and the human TM to fly 169-189 without gaps. The human BH3 region (100-125)
  aligns only partly. The only shared feature is a W-rich DW-x-x-x-W segment (fly DWLKNW).
  There is **no recognisable BH3 consensus** in the fly protein. No fly paper describes a BH3 domain.

## Localization

- OMM: GFP-BNIP3 (fly protein) constructs localize to the outer mitochondrial membrane in larval muscle
  [PMID:40801807 "All BNIP3 constructs retain an intact TMD at the C-terminus, ensuring their localization to the outer mitochondrial membrane"].
- In the germline, BNIP3 is upregulated in differentiating cysts and associates with mitochondria
  [PMID:31092924 "BNIP3 is upregulated in differentiating cysts26 where it associated with mitochondria"].
- Mtch (MTCH2 ortholog) is needed for proper OMM insertion of (human) BNIP3 in fly enterocytes
  [PMID:41576035 "Our data support a model with Mtch functioning as a BNIP3 insertase that is required for mitophagy downstream of PINK1 and Parkin"].
  This is consistent with BNIP3 being a tail-anchored OMM protein.
- Nucleus: the only fly data is a high-throughput HDA from the CPTI YFP protein-trap screen in
  stage-5 embryos (PMID:25294944, Lye et al. 2014; FlyBase curation from the supplementary table).
  It has not been reproduced. Every targeted study shows mitochondrial/OMM localization. The
  nuclear signal may be real (a nuclear pool has been reported for mammalian BNIP3 in some
  contexts) or an artefact of the internal YFP insertion or embryonic overexpression.
  Treat as non-core.
- No fly data on ER localization or ER-phagy receptor activity. In fact, loss of BNIP3 in fly enterocytes
  **reduces** ER levels and **increases** ER-phagy flux
  [PMID:37633267 "In addition, ER-phagy flux is increased in BNIP3 mutant enterocytes compared to control intestine cells"].
  So, unlike human BNIP3, fly BNIP3 is not needed for developmental ER clearance. This is
  relevant to the PTHR15186 root-node (PTN000795991) ER / nuclear envelope IBDs, which FlyBase
  GOA does not propagate to the fly gene.

## Molecular function: mitophagy receptor (mitochondrion-autophagosome adaptor)

- Taoka et al. 2025 eLife (PMID:40801807), full text:
  - "Mechanistically, we found that BNIP3 recruits autophagic machinery to mitochondria through its LC3-interacting motif and minimal essential region, which interact with Atg8a and Atg18a, respectively."
  - "We confirmed that HA-tagged Drosophila Atg18a co-immunoprecipitated with GFP-tagged full-length Drosophila BNIP3, and that this interaction was attenuated by the deletion of the MER (residues 42–53)"
  - "Furthermore, the combination of ΔLIR and ΔMER resulted in mitochondria accumulation nearly identical to that observed in BNIP3 KO flies"
  - "From these results, we conclude that both MER and LIR motifs contribute to BNIP3-mediated mitophagy, with some redundancy in their contributions to selectivity."
  - Overexpression alone does not drive mitophagy; autophagy must also be induced:
    "BNIP3-mediated mitophagy likely requires not only BNIP3 expression but also autophagy induction."
- Wang et al. 2023 (PMID:37633267) showed the LIR residues are conserved:
  "BNIP3 is conserved in Drosophila, including two amino acids in the LIR motif that are required for BNIP3 to function as a mitophagy receptor"

## Biological process: mitophagy (several developmental and stress contexts, PINK1/Parkin-independent and -dependent)

- Muscle remodelling during metamorphosis (larval to adult abdominal DIOMs): BNIP3 KO blocks
  mitophagy flux and larval mitochondria accumulate [PMID:40801807 "In sharp contrast, BNIP3 KO blocked mitophagy flux at a comparable level with FIP200 RNAi"];
  "BNIP3 is required for mitophagosome formation."; the KO is viable
  [PMID:40801807 "BNIP3 KO was compatible with viability and did not markedly impair mobility"].
- Programmed germline mitophagy (PGM) / mtDNA selection in the ovary: needs BNIP3 and Atg1 but
  not PINK1/Parkin [PMID:36323236 "We show that PGM requires the mitophagy receptor BNIP3, mitochondrial fission and translation factors, and members of the Atg1 complex, but not the mitophagy factors PINK1 and Parkin."];
  [PMID:31092924 "Reducing BNIP3 expression inhibited selection"];
  [PMID:36803283 "Interestingly, PGM requires the general macroautophagy/autophagy machinery and the mitophagy adaptor BNIP3, but not the canonical mitophagy genes Pink1 and park (parkin), even though they are critical for germline mtDNA quality control."].
- Developmental mitochondrial clearance in the intestine (enterocytes at pupariation): BNIP3 mutant
  cells keep the mitochondrial protein ATP5A [PMID:37633267 "These results indicate that BNIP3 is required for mitophagy in the same cells where Rtnl1, Trp1 and Atl are specifically required for ER-phagy."].
  Here BNIP3 works in one genetic pathway with Mtch, Vps13D, PINK1 and Parkin
  [PMID:41576035 "These data indicate that Mtch and BNIP3 function in the same genetic pathway to control enterocyte mitophagy during intestine development."].
  So fly BNIP3 can work alongside PINK1/Parkin in the gut, but independently of them in the germline.
- Hypoxia-induced mitophagy in larval body-wall muscle (preprint, Res Sq 2026, PMID:42183378):
  "These results suggest that BNIP3 is an essential mediator of the hypoxia-induced mitophagy in the Dm larval muscles."
- Aging muscle (Deng et al. 2026 Aging Cell, PMID:42128879): uses a mito-SRAI reporter. Loss of BNIP3
  reduces IFM mitophagy, with ROS and Relish activation. Overexpression (mostly human BNIP3)
  extends lifespan. "Together, these results suggest that BNIP3 is essential for mitophagy."
- Aging brain (Schmid et al. 2022 Nat Aging, PMID:36213625): the mitophagy and lifespan-extension
  experiments used a **human** BNIP3 transgene ("UAS-hBNIP3-HA"). The only experiment on the fly gene
  was RNAi, which shortens lifespan ("Conversely, expression of BNIP3-RNAi ubiquitously or
  specifically in neurons in adult flies resulted in shortened lifespans compared to controls").
  So the FlyBase IMP to mitophagy from this paper rests on indirect evidence for the fly gene.
  The term is correct for the fly gene on other grounds.
- Zhang et al. 2016 (PMID:27528605) also used human BNIP3 in flies, to rescue PINK1-null
  muscle phenotypes. This is not direct evidence on the fly gene.

## Apoptosis / BH3: is fly BNIP3 pro-apoptotic?

- No fly study shows that fly BNIP3 promotes apoptosis, mitochondrial fragmentation during
  apoptosis, or MOMP. Evidence against, or at least neutral:
  - The BNIP3 KO is viable and moves normally (PMID:40801807). Overexpressing fly GFP-BNIP3 in
    larval muscle does not even induce mitophagy:
    [PMID:40801807 "Overexpression of BNIP3 in larval muscle cells did not significantly induce mitophagy (Figure 5—figure supplement 2), suggesting that BNIP3 expression alone is insufficient to drive mitophagy."].
    No cell-death phenotype was reported.
  - Neuronal overexpression of human BNIP3 in flies *reduced* apoptotic (cleaved caspase-3+)
    cells in the aged brain [PMID:36213625 "Importantly, neuronal BNIP3 induction was associated with fewer apoptotic cells in the aged brain as detected by cleaved caspase-3 staining"].
  - No BH3 consensus by alignment (bioinformatics folder). In Drosophila, apoptosis runs mainly
    through the RHG IAP-antagonists (Reaper/Hid/Grim) and is largely Bcl-2 independent. This is
    background knowledge, not cited here.
- Conclusion: the Bilateria-node (PTN001032684) IBDs for "positive regulation of apoptotic process"
  and "mitochondrial fragmentation involved in apoptotic process" rest only on vertebrate seeds
  (fragmentation: human BNIP3 alone). Both are unsupported in fly and probably reflect
  vertebrate-specific death functions. Marked as over-annotation, not removed, because a
  latent cell-death activity under strong overexpression is untested in fly.

## Interactions

- Rtnl1 (Q9VMV9) from the FlyBi binary Y2H network (PMID:37061542) and IntAct ("Q9VPD6; Q9VMV9: Rtnl1; NbExp=4").
  This is an uninformative protein-binding IPI. There is no functional follow-up; Rtnl1 is an
  ER-phagy receptor, and fly BNIP3 is not needed for ER-phagy (PMID:37633267).
- Atg8a (via LIR) and Atg18a (via MER) are functionally validated (PMID:40801807). They are captured
  by GO:0140580 mitochondrion autophagosome adaptor activity.

## Lifespan / physiology (non-core, phenotypic)

- RNAi shortens lifespan (PMID:36213625). Deng et al. 2026 (PMID:42128879) report shortened lifespan, ROS and Relish activation in BNIP3 loss-of-function flies. Taoka et al. measured KO survival and mobility (Fig 3-figure supplement 2) and found no marked mobility defect.
- These are downstream consequences of mitophagy defects. No GO annotation is proposed (necessity, not participation).

## Literature checked but not used as primary evidence

- Rana et al. 2017 Nat Commun (PMID:28878259, Drp1 midlife fission): about Drp1 with autophagy dependence.
  It does not test BNIP3, so it is not cited in the review.
- PMID:40618856 (GDAP1/CMT4A model, abstract only): fly neural Gdap1 knockdown raises BNIP3
  levels, and knocking down both genes is harmful. Supportive context only.
- PMID:38443598 (Mst1/2-BNIP3): mammalian cell work with a fly rotenone model of Mst. BNIP3
  experiments were done in mammalian cells. Low relevance.

## Deep research

- A falcon deep-research job was started separately. The file BNIP3-deep-research-falcon.md was
  not present when the review was written, so the review uses primary literature only.
