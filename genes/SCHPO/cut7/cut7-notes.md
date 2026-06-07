# cut7 (kinesin-5) — S. pombe — review notes

UniProt P24339 / SPAC25G10.07c. Sole kinesin-5 (BimC/Eg5 family) in fission yeast. Essential for mitosis.

## Identity / family
- Kinesin-like protein; N-terminal kinesin motor domain (UniProt FT DOMAIN 72..421), ATP-binding P-loop (BINDING 159..166). BimC subfamily (UniProt SIMILARITY: "Belongs to the TRAFAC class myosin-kinesin ATPase superfamily. Kinesin family. BimC subfamily.").
- 1085 aa; coiled-coil regions (436..604, 715..740, 897..955) consistent with homotetramer formation. CDC2 phosphosite Thr1011 (by similarity).

## Discovery / core phenotype
- [PMID:2145514 "The predicted product of one of these genes, cut7+, contains an amino-terminal domain similar to the kinesin heavy chain head domain, indicating that the cut7+ product could be a spindle motor."] and "Mutations at cut7 block spindle formation" (UniProt). cut7 resembles A. nidulans bimC; mutants form two unconnected half spindles, chromosome separation fails.
- [PMID:1538784 "cut7 protein concentrates on or near the spindle pole bodies throughout mitotic and meiotic nuclear division and associates with mitotic spindle microtubules in a stage-specific manner, associating with the mid-anaphase B midzone. In cut7ts mutants, spindle pole bodies stain but mitotic microtubules do not."] — localization to SPB, mitotic+meiotic spindle, anaphase B midzone.

## Motor activity / direction
- [PMID:27834216 "Cut7, the sole kinesin-5 in Schizosaccharomyces pombe, is essential for mitosis."]; bidirectional motor — "the key determinant of stepping direction is the degree of motor crowding on the microtubule lattice, with greater crowding converting the motor from minus end-directed to plus end-directed stepping." Plus- AND minus-end-directed motor activity directly demonstrated. "the Cut7 N terminus increases Cut7 occupancy by binding directly to microtubules" (microtubule binding).
- [PMID:30659798 "Kinesin-5s are microtubule-dependent motors that drive spindle pole separation during mitosis."]; "Cut7, the sole kinesin-5 in fission yeast, was among the first mitotic kinesins to be identified and is essential for spindle pole body separation." Motor domain (residues 67–432) ATPase measured: "Cut7MD has a very slow ATPase activity in vitro" with Vmax ~1.14 ATP/s; "the C-terminal neck linker ... docking along the length of the motor domain and directed toward the MT plus end" = plus-end directed; binds MT via helix-α4. Forms "dumbbell shaped antiparallel tetramers that support spindle MT cross linking and sliding." Cut7 is STLC-resistant (not inhibited by human kinesin-5 inhibitor).

## Spindle force balance / antagonism
- [PMID:24239120 "Kinesin-5 cut7p is reported to play a role in biopolar spindle formation, by organizing and sliding apart antiparallel MTs from opposite poles"]; "Upon inactivation of cut7p at the non-permissive 35°C, the metaphase spindle immediately shortened until the spindle became a focused monopolar structure ... cut7p being the major contributor to the outward pushing force." cut7 phase-one mitotic spindle formation IMP.
- [PMID:28513584 "Kinesin-5 family members are plus-end directed motors organized as homo-tetramers that crosslink antiparallel MTs and slide them apart, pushing on the spindle poles, and therefore promoting spindle bipolarity and elongation"]; cut7Δpkl1Δ rescues bipolarity (force balance restored); "spindle elongation velocity during anaphase B was reduced in cut7Δpkl1Δ cells (30% reduction ...), suggesting that Cut7 participates in anaphase spindle elongation in addition to its established function in spindle bipolarity." — supports phase-three elongation role.
- [PMID:18418055] cut7-22(ts) bipolarity defects rescued by stabilizing MTs / deleting kinesin-14 pkl1; "the conditional allele cut7-22(ts), encoding fission yeast mitotic Kinesin-5, essential for bipolarity." Genetic interaction with MTOC/pkl1 — basis of IGI mitotic spindle midzone assembly.

## Kinetochore / chromosome congression (Mad1)
- [PMID:26258632 "fission yeast Mad1 binds the plus-end-directed kinesin-5 motor protein Cut7 (Eg5 homologue)"]; "Mad1 recruits Cut7 to kinetochores of misaligned chromosomes and promotes chromosome gliding towards the spindle equator." — basis of kinetochore localization (IDA), Mad1 (P87169 / SPBC3D6.04c) interaction (IPI), and microtubule plus-end directed mitotic chromosome migration (IGI). Note: this is a context-specific (misaligned chromosome) role, not the core bipolar-spindle function.

## Meiosis
- [PMID:32327557 "Spindle bipolarity is achieved when interdigitating MTs are crosslinked and organized into antiparallel arrays by the kinesin-5 family protein Cut7 ..., inducing the separation of spindle poles."]; Cut7-GFP "localized to the spindle and spindle poles from spindle assembly to spindle disassembly during both mitosis and MI." cut7Δpkl1Δ zygotes fail MI bipolar spindle (meiosis-specific requirement; kinesin-14 Klp2 and MT dynamics also antagonize Cut7 in MI). Supports meiotic spindle / meiotic spindle pole localization and meiotic spindle assembly. Polar microtubule IDA also from this paper (PMID:32327557).

## Localization (high-throughput)
- [PMID:16823372] genome-wide YFP localization (ORFeome). Supports HDA nucleus, microtubule cytoskeleton, mitotic SPB localizations (consistent with directed-evidence localizations).

## Interaction partners (IPI, PMID:30659798 listed PomBase IDs)
- SPBC16A3.15c, SPBC26H8.07c, SPBC800.05c — partners reported with cut7; these are listed as protein-binding IPIs. (Use of bare "protein binding" is uninformative per guidelines; better captured by MF microtubule motor activity / specific complex terms, but the experimental interaction itself is sound.)

## Summary of core functions
- MF: plus-end-directed (and context-dependent minus-end-directed) microtubule motor activity; ATP binding / ATP hydrolysis; microtubule binding.
- BP: mitotic bipolar spindle assembly / initial SPB separation (phase one); spindle elongation (phases two/three); meiotic spindle assembly. Outward pushing force; antagonizes kinesin-14 Pkl1/Klp2.
- CC: spindle pole body (mitotic + meiotic), spindle microtubule / polar microtubule, spindle midzone, kinetochore (Mad1-dependent, context-specific).
