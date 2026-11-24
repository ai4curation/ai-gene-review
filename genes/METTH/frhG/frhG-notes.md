# frhG (P19498, MTH_1298) notes

Methanothermobacter thermautotrophicus Delta H, coenzyme F420-reducing [NiFe]-hydrogenase (Frh), gamma (small) subunit.
Sister reviews: genes/METTH/frhA (alpha, [NiFe] large subunit); genes/METTH/frhB (beta) not yet reviewed at time of writing.

## Literature search (2026-11-07)

Deep-research providers were unavailable, so no deep-research file exists. Literature is the set
already cached for the frhA review (web search plus UniProt citations):

- PMID:3663585 (Fox et al. 1987; purification of FRH from strain Delta H; abstract only)
- PMID:2207102 (Alex et al. 1990; cloning of frhADGB from strain Delta H; abstract only)
- PMID:23483797 (Mills et al. 2013; cryo-EM structure of Frh from M. marburgensis; full text)
- PMID:24569482 (Allegretti et al. 2014; 3.36 A cryo-EM structure of M. marburgensis Frh; full text)
- PMID:18487331 (Hendrickson & Leigh 2008; M. maripaludis fru/frc mutants; full text)

No FrhG-specific genetics or biochemistry beyond these was found.

## Subunit and cofactors

- Delta H enzyme: alpha, beta, gamma subunits [PMID:3663585 "composed of three subunits, alpha (Mr 47K), beta (Mr 31K), and gamma (Mr 26K)."]; cofactor set of the whole 115K unit [PMID:3663585 "The tightly associated redox cofactors per 115K species are 0.6-0.7 nickel atom, 0.8-0.9 flavin adenine dinucleotide (FAD), and 13-14 iron atoms in iron-sulfur centers."]. 13-14 Fe fits four [4Fe-4S] clusters (16 Fe would be expected, so slightly substoichiometric) plus the Fe of the [NiFe] site.
- Placement by subunit (M. marburgensis structure): [PMID:23483797 "the small subunit FrhG (26 kDa) with three [4Fe4S] clusters and the iron–sulfur flavoprotein FrhB (31 kDa) with a [4Fe4S] cluster and FAD, and the F420-binding site."]; confirmed at 3.36 A [PMID:24569482 "the 26 kDa subunit FrhG with three [4Fe4S] clusters"].
- Electron path: [PMID:23483797 "cluster in FrhA via the three Fe-S clusters in FrhG and one Fe-S cluster and FAD in FrhB to F420"] (the quote begins after "[NiFe]"). Functional unit is one heterotrimer [PMID:23483797 "indicating that the functional unit is one FrhABG heterotrimer and there is no cooperativity in the complex"].
- Domain structure:
  - N-terminal domain homologous to the [NiFe]-hydrogenase small subunit, holding the proximal cluster [PMID:23483797 "The fit of the small subunit of the group 1 enzyme reveals structural homology to the N-terminal domain of FrhG including the proximal Fe-S cluster."]. One Cys ligand is replaced by Asp [PMID:23483797 "In the primary structure of FrhG, one of the conserved cysteine residues for the coordination of this cluster is replaced by Asp60"].
  - C-terminal ferredoxin domain with the medial and distal clusters [PMID:23483797 "Instead, the sequence indicates a ferredoxin domain, with two CxxCxxCxxxC sequences coordinating two [4Fe4S] clusters"].
- Putative Zn at the FrhG-FrhG dimer interface: [PMID:24569482 "the density in between the four cysteine side chains is strongly suggestive of a coordinated ion"]; [PMID:24569482 "their tetrahedral arrangement suggests that it is a zinc ion"]. Structural inference only (cysteine side chains not fully resolved); not annotated.

## Sequence mapping to P19498 (my check)

M. marburgensis FrhG (UniProt D9PYF7, 275 aa genome model) starts at the GTG codon annotated as Val40 of D9PYF7
(the paper calls it Val39); residues 40-275 of D9PYF7 align ungapped with P19498 2-236 (P19498 Met1 = D9PYF7 Val40).
The mature chains differ at only four positions (P19498 I129L, A142T, E152D, T182I relative to D9PYF7). So
M. marburgensis residue n (paper numbering, genome model) = P19498 residue n-39:

- Asp60 (paper) = P19498 Asp21, the non-Cys proximal-cluster ligand. Present in P19498.
- Cys206/Cys208 (putative Zn site, 2014 paper) = P19498 Cys167/Cys169. Present in P19498.
- P19498 FT BINDING [4Fe-4S] features cover only the two ferredoxin-domain clusters (C181, C184, C187, C191, C210, C213, C216, C220; ECO:0000250); the proximal cluster is not annotated in UniProt.

Check done by aligning the two UniProt sequences (rest.uniprot.org; D9PYF7 sequence, P19498 sequence from frhG-uniprot.txt) in a one-off python comparison.

## Decisions on GOA rows (all IEA)

- GO:0016151 nickel cation binding (IPR017681): FrhG holds no nickel; Ni is in FrhA. REMOVE; pattern 18 (the FrhA cofactor copied onto the FrhG family entry).
- GO:0050660 FAD binding (IPR017681): FAD is in FrhB. REMOVE; pattern 18.
- GO:0051536 iron-sulfur cluster binding (IPR006137, IPR017681): true; three [4Fe-4S] clusters. MODIFY to GO:0051539 4 iron, 4 sulfur cluster binding. This is the one of the four copied terms that is right for IPR017681.
- GO:0050454 coenzyme F420 hydrogenase activity (EC-based combined IEA): whole-complex activity (pattern 16). MARK_AS_OVER_ANNOTATED, contributes_to in core functions, same as frhA.
- GO:0016491 oxidoreductase activity (ARBA): FrhG catalyses no redox reaction of its own; it relays electrons. Ancestor of the complex activity. MARK_AS_OVER_ANNOTATED (consistent with the GO:0050454 row).
- NEW GO:0009055 electron transfer activity (IC from the structure): FrhG's own activity, the relay between the [NiFe] site and FrhB. Comparator check (QuickGO, 2026-11-07): E. coli hydrogenase-1 small subunit HyaA (P69739) carries GO:0009055 by IDA (PMID:22431599) and IBA, and hydrogenase-2 small subunit HybO (P69741) by IBA, so the term is the convention for [NiFe]-hydrogenase small subunits.
- NEW GO:0005737 cytoplasm and GO:0019386 methanogenesis, from carbon dioxide: same reasoning as frhA (soluble cytoplasmic enzyme; FrhG performs the electron-relay part of the F420-reduction step).

## Physiology

- [PMID:23483797 "Four electrons are provided through the reduced form of the coenzyme F420, which is regenerated by Frh."]
- Redundancy with Hmd-Mtd in M. maripaludis [PMID:18487331 "Their analysis demonstrates that either pathway supports growth on H2 and CO2."]
