# Orai (Drosophila melanogaster, Q9U6B8) notes

## Identity
- Orai (olf186-F, CG11430) is the single fly Orai/CRACM family member; four-TM plasma membrane protein. UniProt: "Pore-forming subunit of inward rectifying Ca(2+) release-activated Ca(2+) (CRAC) channels."

## Discovery (S2 cell RNAi screens, 2006)
- Zhang et al. 2006: olf186-F knockdown abolished SOCE and I_CRAC; overexpression increased current [PMID:16751269 "one, olf186-F, that upon RNA interference-mediated knockdown exhibited a profound reduction of thapsigargin-evoked Ca(2+) entry and CRAC current"].
- Feske et al. 2006 used a Drosophila RNAi screen for SOCE and NFAT import [PMID:16582901 "a Drosophila RNA interference screen designed to identify regulators of store-operated Ca2+ entry and NFAT nuclear import"].
- Vig et al. 2006: CRACM1 identified as modulator of Drosophila CRAC currents [PMID:16645049 "A secondary patch-clamp screen identified CRACM1 and CRACM2 (CRAC modulators 1 and 2) as modulators of Drosophila CRAC currents."].

## Pore subunit
- E180D in the S1-S2 loop converts selectivity [PMID:16921385 "These results indicate that Orai itself forms the Ca2+-selectivity filter of the CRAC channel."]; Stim-Orai co-IP enhanced by store depletion [PMID:16921385 "interaction between wild-type Stim and Orai, assessed by co-immunoprecipitation, is greatly enhanced after treatment with thapsigargin"].
- Gwack et al. 2007: [PMID:17293345 "dOrai and its human homologue Orai1 are pore subunits of the Ca2+ release-activated Ca2+ channel"].
- Stoichiometry: dimers at rest that Stim converts to higher order [PMID:18820677 "Interaction with the C terminus of Stim thus induces Orai dimers to dimerize, forming tetramers that constitute the Ca(2+)-selective pore."]; crystal structure is hexameric [PMID:23180775 "the calcium channel is composed of a hexameric assembly of Orai subunits arranged around a central ion pore"; "A ring of glutamate residues on its extracellular side forms the selectivity filter."]. Open-state P288L structure [PMID:31009446 "6 transmembrane 1 (TM1) helices in the center form the ion-conducting pore"].

## Physiology
- Neuronal SOCE needed for flight [PMID:19515818 "activity of the recently identified store-operated channel encoded by dOrai and the endoplasmic reticulum Ca(2+) store sensor encoded by dSTIM are necessary for normal flight"].

## Curation thoughts
- ISS "calcium channel regulator activity" (with STIM1 Q13586) is a regulator (Stim-type) activity transferred to the pore; Orai is the channel, not its regulator -> REMOVE.
- Protein binding IPI (Stim, self) -> REMOVE (uninformative); identical protein binding reflects channel oligomerisation; keep as non-core.
