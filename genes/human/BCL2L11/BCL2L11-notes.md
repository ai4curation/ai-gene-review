# BCL2L11 / BIM manual curation notes

## 2026-09-30

Human BCL2L11 encodes BIM, a BH3-only BCL2-family protein with many splice
forms. The UniProt record keeps the three classical pro-apoptotic isoforms
BimEL, BimL, and BimS and a long tail of human splice products; only isoforms
that retain the BH3 region should be assumed to carry the canonical BCL2-family
death activity.

The core curation issue is directional. BIM donates a BH3 helix. When that
helix binds a BCL2, BCL2L1/Bcl-xL, MCL1, BCL2A1, BCL2L2/Bcl-w, or BCL2L10/Bcl-B
groove, the groove-side protein is doing `GO:0051434` BH3 domain binding; BIM is
inhibiting the pro-survival BCL2-family protein. Lee et al. describe the
functional side cleanly for MCL1: a Bim-derived BH3 ligand can antagonize MCL1
without driving MCL1 degradation, showing that "ligands that merely engage its
hydrophobic groove with high affinity are sufficient" [PMID:18209102]. Fire et
al. also solved the human MCL1-human BIM BH3 peptide structure and frame BIM
as the BH3 peptide ligand bound in the receptor groove [PMID:20066663,
"We report the crystal structure of human Mcl-1 bound to a BH3 peptide derived
from human Bim"]. Generic `GO:0005515` rows on BIM for these anti-apoptotic
partners should therefore not be mapped to BH3-domain binding.

BIM is also a direct activator BH3-only protein. Marani et al. found human BIM
splice variants, including BimS and BimAD, that can bind and activate BAX,
with the abstract stating that Bim can regulate apoptosis "through direct
activation of the Bax-mediated cell death pathway" [PMID:11997495]. Gavathiotis
et al. mapped a BIM BH3 interaction surface on BAX and concluded that "BIM SAHB
engagement directly triggers the functional activation of BAX" [PMID:18948948].
Those BAX-side rows need a direct-activator MF that does not exist in GO yet;
the same `pro-apoptotic BCL2 family effector activator activity` NTR used for
BID fits BIM.

Several apoptosis process rows can be tightened from `GO:0006915` or
`GO:0043065` to positive regulation of MOMP or release of cytochrome c.
BCL2L11 is upstream of the pore in the sense that BAX/BAK oligomers perform
permeabilization, but BIM does real work in the step by neutralizing
pro-survival BCL2 proteins and directly activating BAX or BAK.

The ER-stress rows should be kept stimulus-specific. Ghosh et al. show that ER
stress in neuronal cells increases PUMA and BIM protein levels and that CHOP
knockdown decreases BIM activation [PMID:22761832], which supports BIM as a
BH3-only effector downstream of ER stress rather than a generic UPR sensor.
The `positive regulation of IRE1-mediated unfolded protein response` row is too
far upstream and has the direction backwards for BIM protein, so it should be
removed rather than retained as a response-to-ER-stress annotation.

The RACK1/CIS paper shows non-core regulation of BimEL degradation in cancer
cells; the RACK1-BIM interaction itself should not stay as generic protein
binding [PMID:18420585, "RACK1 formed a complex with DLC1 and Bim,
specifically BimEL, in the presence of apoptotic agents"]. Large interactome
imports from HuRI, cell-specific interactome maps, neurodegenerative-disease
interactome mapping, and the 2025 multimodal cell maps are lower-value
duplicates or off-pathway edges for BCL2L11 and should be removed instead of
inflating BIM's molecular-function record with generic binding.
