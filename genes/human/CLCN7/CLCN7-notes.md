# CLCN7 (ClC-7) review notes

UniProt: P51798 (CLCN7_HUMAN), "H(+)/Cl(-) exchange transporter 7", 805 aa, gene on chr 16p13.

## Core molecular function: 2Cl-/1H+ antiporter (NOT a passive Cl- channel)

- ClC-7 is a member of the CLC family, which contains both true Cl- channels (ClC-0/1/2/Ka/Kb) and electrogenic Cl-/H+ antiporters (ClC-3 to ClC-7). [PMID:32851177 "The remaining CLC proteins (CLC-3 to CLC-7) are electrogenic Cl−/H+ antiporters ... that exchange Cl− and H+ with a stoichiometry of 2:1"].
- Direct functional demonstration that ClC-7 mediates lysosomal Cl-/H+ antiport: lysosomes have an anion transport pathway with the defining characteristics of a CLC Cl-/H+ antiporter; ClC-7 siRNA knockdown ablates this antiport and strongly diminishes lysosomal acidification in vivo. [PMID:18449189 "ClC-7 is a Cl-/H+ antiporter, that it constitutes the major Cl- permeability of lysosomes, and that it is important in lysosomal acidification"].
- Stoichiometry directly measured as 2Cl-/1H+ by tail-current reversal potentials. [PMID:21527911 "Reversal potentials of tail currents revealed a 2Cl(-)/1H(+)-exchange stoichiometry"].
- ClC-7 is "slowly voltage-gated"; voltage gating extends to ion exchangers, not just channels. [PMID:21527911 "ClC-7 is a slowly voltage-gated 2Cl(-)/1H(+)-exchanger"]. UniProt CATALYTIC ACTIVITY: Rhea:RHEA:29567, 2 chloride(in) + H(+)(out) = 2 chloride(out) + H(+)(in).
- The old "chloride channel" designation (e.g. AltName "Chloride channel 7 alpha subunit") and the 1995 cloning paper [PMID:8543009] reflect family-name convention; that paper actually found ClC-7 could NOT be expressed as a chloride channel in oocytes [PMID:8543009 "Both ClC-6 and ClC-7 cannot be expressed as chloride channels in Xenopus oocytes"]. Annotations of bare "chloride channel activity" (GO:0005254) are imprecise vs the verified antiporter activity GO:0062158.

## Obligate complex with OSTM1 (beta-subunit)

- ClC-7 forms an obligate heteromer with OSTM1; OSTM1 is required for ClC-7 protein stability and for transport activity. [PMID:21527911 "ClC-7 needs Ostm1 as β-subunit ... both the aminoterminus and transmembrane span of the Ostm1 β-subunit are required for ClC-7 Cl(-)/H(+)-exchange"]. UniProt SUBUNIT: heteromers of alpha (CLCN7) + beta (OSTM1).
- Cryo-EM of the human CLC-7/OSTM1 complex: 2 CLC-7 + 2 OSTM1, OSTM1 glycosylated "lid" over CLC-7, TMD-TMD interactions stabilize the complex. [PMID:32851177 "the highly glycosylated Ostm1 functions like a lid positioned above CLC-7 and interacts extensively with CLC-7 within the membrane"]. ComplexPortal CPX-6321 "CLCN7-OSTM1 chloride channel complex"; Reactome R-HSA-2730959.
- OSTM1 = UniProt Q86WC4. Most curated IPI "protein binding" annotations to Q86WC4 actually capture the OSTM1 interaction and could be a specific complex annotation, but as bare GO:0005515 they are uninformative.

## Subcellular localization

- Lysosomal / late-endosomal membrane; also osteoclast ruffled border (resorption lacuna). [PMID:32851177 "mainly resides in lysosomes and osteoclast ruffled membranes"]; UniProt SUBCELLULAR LOCATION: Lysosome membrane, multi-pass.
- Experimental localization to lysosomal membrane: [PMID:18449189] (EXP), [PMID:21527911] (IDA, ComplexPortal), plus large-scale lysosomal-proteome MS [PMID:17897319].
- Reactome TAS lysosomal membrane: R-HSA-2730959.

## Physiological role

- Provides counter-ion (Cl-) flux that permits V-ATPase-driven luminal acidification of lysosomes and the osteoclast resorption lacuna; loss reduces lysosomal acidification [PMID:18449189]. Note nuance: some studies report normal steady-state lysosomal pH in Clcn7-/- mice, suggesting the dominant role is raising luminal [Cl-] using the H+ gradient rather than a simple shunt [PMID:32851177 "lysosomal pH is normal in Clcn7−/− and Ostm1−/− mice ... the major role of CLC-7 is to increase the luminal Cl− concentration"]. The Y715C gain-of-function variant alters lysosomal pH, supporting a role in pH regulation [PMID:32851177].
- Loss-of-function → osteopetrosis (OPTB4 recessive, OPTA2/Albers-Schonberg dominant) and lysosomal storage / neurodegeneration. UniProt DISEASE. Gain-of-function de novo Y715C → hypopigmentation/organomegaly/delayed myelination (HOD), with increased lysosomal acidification [VARIANT 715 "increased voltage-gated chloride channel activity; increased lysosomal lumen acidification"].

## Annotation review reasoning

- GO:0005254 chloride channel activity (IBA, IEA-ARBA, TAS PMID:8543009): imprecise. ClC-7 is an antiporter, not a passive channel. MODIFY -> GO:0062158 chloride:proton antiporter activity (already in GOA, experimentally supported).
- GO:0062158 chloride:proton antiporter activity (IBA, IEA-InterPro): ACCEPT — core MF, matches measured 2Cl-/1H+ exchange.
- GO:0015108 chloride transmembrane transporter activity (IEA): correct but generic parent of the antiporter activity; KEEP_AS_NON_CORE.
- GO:0005765 lysosomal membrane (EXP/IDA/HDA/TAS + IBA/IEA): ACCEPT (core localization).
- GO:0005770 late endosome (IBA): plausible (endolysosomal system); KEEP_AS_NON_CORE.
- GO:0030321 transepithelial chloride transport (IBA + IDA-ComplexPortal): this is a phylogenetic/complex-portal transfer; ClC-7 is intracellular (lysosomal), not an epithelial plasma-membrane transepithelial transporter. MARK_AS_OVER_ANNOTATED.
- GO:0034707 chloride channel complex (IBA, IPI-ComplexPortal): captures the CLCN7-OSTM1 complex; ACCEPT (term name uses "channel" by family convention but the complex is real).
- GO:1902476 chloride transmembrane transport (IBA), GO:0006821 chloride transport (IEA), GO:0055085 transmembrane transport (IEA), GO:1902600 proton transmembrane transport (IEA): BP transport terms consistent with antiporter; keep generic ones as non-core, accept the chloride transmembrane transport as supported.
- GO:0016020 membrane (IEA, HDA): uninformative generic; MARK_AS_OVER_ANNOTATED.
- GO:0009268 response to pH (IEA, Ensembl ortholog transfer): weakly supported, no direct human evidence; KEEP_AS_NON_CORE.
- GO:0005515 protein binding (IPI x many): bare protein binding, uninformative. The OSTM1 (Q86WC4) interactions are biologically the key partner but are captured by the complex term; MARK_AS_OVER_ANNOTATED.

## Falcon deep research integration (2026-06-21)

The Falcon (Edison) report in `CLCN7-deep-research-falcon.md` is high quality and well-grounded; it strongly corroborates the existing review (2Cl-/1H+ antiporter, obligate OSTM1 complex, lysosomal + osteoclast ruffled-border localization, osteopetrosis/HOD disease spectrum) and adds mechanistic and physiological refinements rather than contradicting it. All Falcon-sourced citations below are not yet independently verified against full text.

New or refined findings beyond the existing notes/review:

- Cryo-EM at 2.8 A resolves the transport mechanism: "gating glutamate" Glu247 and "proton glutamate" Glu314, three anion binding sites, and divergent Cl-/H+ pathways; OSTM1 binds the dimer periphery via a single TM helix and its glycosylated N-terminus forms a luminal cap protecting ClC-7 from lumenal degradation [Schrecker, Korobenko & Hite, eLife 2020, doi:10.7554/elife.59555 (= PMID:32851177, already cited)].
- Direct inhibition of ClC-7 by the lysosomal lipid PI(3,5)P2 (made by PIKFyve); structural mechanism shows PI(3,5)P2 binding remodels the transporter by drawing the cytosolic CBS/C-terminal domains against the TMD, and the disease residue Y715 lies in this phosphoinositide-binding interface [Hilton et al., bioRxiv 2025, doi:10.1101/2025.10.01.679551 — PREPRINT, 0 citations; treat as provisional].
- HOD gain-of-function variants (Y715C, K285T) line the PI(3,5)P2 pocket, reduce lipid inhibition, and shift voltage gating to less positive potentials, causing excess transport and enlarged hyperacidified vacuoles — mechanistically linking the existing Y715C annotation note to loss of PI(3,5)P2 regulation [Polovitskaya et al., J Biol Chem 2024;300:107437, doi:10.1016/j.jbc.2024.107437].
- pH-independent role for luminal chloride: ClC-7 builds a ~2-4 fold lysosomal Cl- gradient, and luminal Cl- (not just pH) directly activates cathepsins B/L; loss reduces Cl- without abolishing acidification yet still impairs cargo degradation and causes lysosomal membrane rupture (shown via C. elegans clh-6 ortholog) [Zhang et al., J Cell Biol 2023, doi:10.1083/jcb.202210063; commentary Feng/Liu/Xu, J Cell Biol 2023, doi:10.1083/jcb.202305007]. This biochemically supports the notes' "raise luminal [Cl-]" interpretation over a pure acidification shunt.
- Role in phagolysosome resolution in macrophages and in autophagic flux/cargo degradation, again largely Cl--dependent and partly acidification-independent [Feng/Liu/Xu, J Cell Biol 2023, doi:10.1083/jcb.202305007; Rossler et al., J Bone Miner Res 2021, doi:10.1002/jbmr.4322].
- Patient iPSC-derived osteoclasts carrying CLCN7 mutations show complete loss of bone-resorption capacity, and CLCN7-ARO is frequently neuronopathic (neuronal lysosomal storage, neurodegeneration, retinal degeneration) unlike TCIRG1 osteopetrosis [Rossler et al., J Bone Miner Res 2021, doi:10.1002/jbmr.4322; Bose, He & Stauber, Front Cell Dev Biol 2021, doi:10.3389/fcell.2021.639231].

Discrepancies / annotations to revisit:

- No contradictions with the existing review; the Cl--dependent cathepsin-activation and phagolysosome/autophagy findings reinforce, not overturn, current ACCEPT/MODIFY calls.
- Possible additions to consider for the YAML (not required by GOA, would be NEW/proposed terms, all PI(3,5)P2/cathepsin claims pending full-text verification): a BP for autophagy/autophagosome-lysosome cargo degradation (e.g. GO:0006914 autophagy or GO:0061684 chaperone-mediated autophagy is NOT appropriate; rather GO:0007040 lysosome organization or GO:0007041 lysosomal transport), and a regulatory MF/process capturing direct inhibition by PI(3,5)P2 (e.g. phosphatidylinositol-3,5-bisphosphate binding, GO:0080025). The osteoclast bone-resorption role (GO:0045453 bone resorption / GO:0001503 ossification) is biologically central and currently not annotated in GOA for this gene — worth flagging as a candidate, though no experimental human GOA term exists to ACCEPT.
