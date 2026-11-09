# kek6 (Kekkon 6; A0A0B4KHL5, FBgn0039862, CG1804) curation notes

## Literature search (2026-11-06)

No deep-research API keys were available; no provider deep-research file was made.
PubMed query `kekkon-6 OR kek6 OR Kek-6 Drosophila` returned three papers: 39704728,
28846707, 15179511. All three are cached (15179511 abstract only, fetched with
`just fetch-pmid`). FlyBase hand-written description in `kek6-deep-research-flybase.md`.

## Protein

- Unreviewed TrEMBL entry (PE 4). LRR + LRRCT + one Ig domain ectodomain, signal peptide
  1..31, transmembrane segment 385..410 (UniProt features), no kinase domain.
  UniProt DR PANTHER: PTHR24366:SF87 (KEKKON 6, ISOFORM B), the same family as Toll-6 in
  UniProt's HMM classification.
- Kek family: [PMID:15179511 "Kek1 is the founding member of the Kek family, a group of
  six Drosophila transmembrane proteins that contain seven LRRs and a single Ig in their
  extracellular domains."]; Kek family members form homotypic and heterotypic complexes.

## Neurotrophin receptor function (PMID:28846707, Ulian-Benitez et al. 2017)

- Kek-6 binds DNT2 and DNT1 [PMID:28846707 "Kek-6 is expressed in the CNS, interacts
  genetically with DNTs and can bind DNT2 in signaling assays and co-immunoprecipitations."];
  [PMID:28846707 "Ligand binding is promiscuous, as Kek-6 can also bind DNT1, and Kek-2 and
  Kek-5 can also bind DNT2."].
- Presynaptic in motoneurons; DNT2 is muscle-derived retrograde factor [PMID:28846707
  "In vivo, Kek-6 is found presynaptically in motoneurons, and DNT2 is produced by the
  muscle to function as a retrograde factor at the NMJ."].
- Localization: [PMID:28846707 "Kek6GFP was present in motoneuron terminals at the neuro
  muscular junction (NMJ) of third instar larvae and not in the muscle"]; Kek-6>FlyBow along
  motoneuron axons and synaptic boutons.
- Epistasis: [PMID:28846707 "demonstrating that Kek-6 functions downstream of DNT2"];
  downstream partners CaMKII and VAP33A (co-IP; pull-down) [PMID:28846707 "DNT2 binds
  Kek-6, which functions via CaMKII and VAP33A downstream."].
- With Toll-6: [PMID:28846707 "Kek-6 and Toll-6 interact physically, and together regulate
  structural synaptic plasticity and homeostasis."]; [PMID:28846707 "Most likely Kek-6 and
  Toll-6 function as a DNT2 receptor complex (Fig 12C)."]; Kek-6 does not antagonise
  Toll-6.
- Phenotypes: kek6 mutants have smaller NMJs, fewer boutons, less branching, reduced
  pCaMKII; overexpression increases active zones but not NMJ size [PMID:28846707
  "Furthermore, whereas kek-6 cannot promote NMJ growth, DNT2 can."].

## Adult dopaminergic circuit (PMID:39704728, Sun et al. 2024)

- [PMID:39704728 "Loss of function for DNT-2 or its receptors Toll-6 and kinase-less
  Trk-like kek-6 caused DAN and synapse loss, impaired dendrite growth and connectivity,
  decreased synaptic sites, and caused locomotion deficits."]

## IBA rows

PAINT node PTN008615184; the only experimental donor is kek6 itself (FB:FBgn0039862).
That is the expected marker of target-side experimental grounding, not circularity.
`just paint-losses DROME kek6`: no IRD/IKR on the lineage.

## FlyBase description check

"co-receptor for spz5, its other receptor being Toll-6" - consistent with PMID:28846707
(the paper calls Kek-6 a receptor and proposes a Kek-6/Toll-6 DNT2 receptor complex).
"activating CaMKII" - supported (pCaMKII reduced in mutants, increased on
overexpression). "inducing synaptogenesis and axonal branching at the NMJ" - supported: kek6 is
required for bouton number and branching, and [PMID:28846707 "Over-expression of kek-6 in
motoneurons alone did not alter NMJ size, but increased branching (Fig 5A and S4A and S4B
Fig) and active zone density (Fig 5A, S1 Table)."]. All claims verified; the text omits
DNT1 binding and the adult dopaminergic-circuit role (PMID:39704728).
