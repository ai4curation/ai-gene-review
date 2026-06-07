# ase1 (Schizosaccharomyces pombe) - curation notes

UniProt: Q9HDY1 | PomBase: SPAPB1A10.09 | "Anaphase spindle elongation protein 1"
Family: MAP65/ASE1/PRC1 (Pfam PF03999 MAP65_ASE1; InterPro IPR007145).

## Summary of function
Ase1 is the fission-yeast member of the conserved Ase1/PRC1/MAP65 family of microtubule-associated
proteins. It is a homodimer that specifically crosslinks/bundles ANTIPARALLEL microtubules, defining
and stabilizing the spindle midzone (region of interdigitating antiparallel MT overlap) during anaphase B,
as well as antiparallel overlaps in interphase iMTOC bundles and the post-anaphase array (PAA).

[PMID:15689489 "We identify fission yeast ase1p, a member of the conserved ASE1/PRC1/MAP65 family of microtubule bundling proteins, which functions in organizing the spindle midzone during mitosis."]
[PMID:15689489 "ase1Delta mutants fail to form overlapping antiparallel microtubule bundles, leading to interphase nuclear positioning defects, and premature mitotic spindle collapse."]
[PMID:15689489 "ase1p functions to stabilize the antiparallel overlapping bundles of minus-ended microtubules associated with the iMTOCs during inter-phase, the overlapping cytoplasmic astral microtubule minus ends associated with the SPBs, and the plus-ended microtubule spindle midzone during mitosis."]

## Localization
- Microtubule overlap zones in interphase; spindle midzone in anaphase.
[PMID:15647375 "Ase1 localizes to microtubule overlapping zones and displays dynamic alterations of localization during the cell cycle. In particular, its spindle localization during metaphase is reduced substantially, followed by robust appearance at the spindle midzone in anaphase."]
[PMID:17254972 "the bundler ase1p localized all along the length of antiparallel MTs, whereas the motor klp2p (kinesin-14) accumulated only at MT plus ends."]
- Post-anaphase array (PAA) microtubules crosslinked by Ase1; PAA forms in plane of contractile ring.
[PMID:36980258 "The PAA microtubules form a dynamic polygon of Ase1p crosslinked microtubules inside the contractile ring."]

## Molecular function
- Microtubule binding; specifically lateral binding (binds along MT lattice / crosslinks MTs side-by-side).
[PMID:17254972 "the bundler ase1p localized all along the length of antiparallel MTs"]
- In vitro: Ase1 protein enables stable antiparallel overlaps; brakes kinesin-14-driven sliding (adaptive braking) - i.e. negatively regulates plus-end-directed sliding by accumulation in shrinking overlaps.
[PMID:21892183 "Ase1, a member of the conserved MAP65/PRC1 family of microtubule-bundling proteins, enables the formation of stable antiparallel overlaps through adaptive braking of Kinesin-14-driven microtubule-microtubule sliding."]
[PMID:21892183 "As overlapping microtubules start to slide apart, Ase1 molecules become compacted in the shrinking overlap and the sliding velocity gradually decreases in a dose-dependent manner."]

## Spindle midzone / anaphase B
[PMID:15647375 "Time-lapse imaging shows that elongating spindles collapse abruptly in the middle of anaphase B."]
[PMID:15647375 "Either absence or overproduction of Ase1 results in profound defects on microtubule bundling in an opposed manner, indicating that Ase1 is a dose-dependent microtubule-bundling factor."]
- Recruits kinesin-6 Klp9 to midzone at anaphase B onset (phospho-regulated by Cdc2/Clp1), driving spindle elongation velocity.
[PMID:19686686 "fission yeast kinesin-6 motor klp9p binds to the microtubule antiparallel bundler ase1p at the midzone at anaphase B onset."]
[PMID:19686686 "ase1Δ cells showed dispersed klp9p localization throughout the spindle (Fig. 3B), consistent with ase1p recruiting klp9p to the spindle midzone."]
[PMID:19686686 "Failure of klp9p-ase1p binding leads to decreased spindle elongation velocity."]
- Klp9 binds region ase1 416-639. Cdc2 phosphorylates ase1 (S640,S683,S688,S693); Clp1 dephosphorylates.

## Metaphase spindle length / force balance
[PMID:24239120 "the spindle midzone proteins kinesin-5 cut7p and MT bundler ase1p contribute to outward-pushing forces"]
- Kinesin-5-independent spindle assembly requires Ase1 to recruit CLASP/Cls1.
[PMID:28513584 "cut7Δpkl1Δ spindle bipolarity requires the microtubule antiparallel bundler PRC1/Ase1 to recruit CLASP/Cls1 to stabilize microtubules."]
[PMID:28513584 "Ase1 is a non-essential antiparallel MT bundler, whose deletion results in metaphase spindle instability"]

## Interactions
- Cls1/Peg1 (CLASP) - direct interaction targets Cls1 to antiparallel overlaps (PMID:18061564, IPI with SPAC3G9.12=cls1).
[PMID:18061564 "A direct interaction with ase1p (PRC1/MAP65) targets cls1p to regions of antiparallel MT overlap."]
- Klp9 (kinesin-6, SPBC15D4.01c) - direct (PMID:19686686, IPI).
- Dis1 (XMAP215) co-localizes with ase1 at overlaps; ase1 is major determinant of inter-MT spacing.
[PMID:21151990 "ase1p is the major determinant of inter-microtubule spacing in interphase bundles since ase1 deleted cells have an inter-microtubule spacing that differs from that observed in wild-type cells."]

## Interphase MT / nuclear positioning
[PMID:15689489 "ase1Delta mutants fail to form overlapping antiparallel microtubule bundles, leading to interphase nuclear positioning defects"]
- Interphase MT bundles push the nucleus to cell center (nuclear migration by MT-mediated pushing).

## Meiosis
[PMID:15647375 "During meiosis astral microtubules are not bundled and oscillatory nuclear movement is impaired significantly."]
- Meiotic spindle midzone / metaphase I stability requires Ase1 (synergy with Klp2/kinesin-14).
[PMID:32723864 "the maintenance of metaphase spindle stability during meiosis I requires the synergism between Klp2 and the conserved microtubule cross-linker Ase1"]
[PMID:34346498 "Loss of kinesin-8 improves the robustness of the self-assembled spindle in Schizosaccharomyces pombe" - reports Ase1/PRC1 as essential component of self-assembled (meiotic) spindle, meiotic spindle elongation/midzone. full_text not cached.]

## Cytokinesis coordination / checkpoint
[PMID:15647375 "Finally Ase1 acts as a regulatory component in the cytokinesis checkpoint that operates to inhibit nuclear division when the cytokinesis apparatus is perturbed."]
[PMID:15647375 "The Aurora kinase does not correctly localize to central spindles in the absence of Ase1."] (= ensures correct midzone positioning of Ark1; ark1 IGI = SPBC21.06c)
[PMID:15647375 "ase1 deletions are viable but defective in nuclear and septum positioning and completion of cytokinesis, which leads to diploidization and chromosome loss."]

## Nuclear envelope division
[PMID:32502403 "the microtubule bundler Ase1/PRC1 at the spindle midzone is required for the local concentration of nuclear pore complexes (NPCs) in the region of the NE in contact with the central spindle."] (= mitotic nuclear bridge organization GO:0140515)

## Spindle disassembly / nuclear localization (IC)
[PMID:25963819] Ase1 at midzone; midzone membrane domain controls disassembly. IC nucleus annotation derived from is_active_in midzone (Ase1 functions in nucleus since closed mitosis = intranuclear spindle).

## Quiescence
[PMID:26124291 "MTs are also stabilized and rearranged into a novel antiparallel bundle associated with the spindle pole body, named Q-MT bundle."] Ase1 in static (Q-MT) MT bundle (GO:0099070 static microtubule bundle).

## Phosphorylation
[PMID:18257517] Phosphoserine S537 identified by MS (UniProt MOD_RES 537).

## Curation decisions
- protein binding (GO:0005515 IPI) x3: replace with informative; but per guidelines avoid bare "protein binding". MARK as KEEP_AS_NON_CORE or note that adapter/recruitment function is core. The IPI to cls1 and klp9 underlie Ase1's scaffold/recruitment role. We keep but note; not core MF descriptor.
- IEA microtubule binding / MT cytoskeleton org / spindle / cytoskeleton / MT cytoskeleton: ACCEPT (supported by experimental data), but redundant with experimental.
- Core: MF microtubule binding + microtubule lateral binding (crosslinking); BP mitotic spindle midzone assembly + anaphase B spindle elongation (mitotic spindle elongation) + cytokinesis coordination; CC spindle midzone.
