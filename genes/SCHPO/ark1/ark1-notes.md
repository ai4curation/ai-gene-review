# ark1 (Aurora kinase, S. pombe) — review notes

UniProt: O59790 (AURK_SCHPO); PomBase SPCC320.13c; synonyms sex1, aim1.
Sole Aurora kinase of fission yeast; Aurora B/Ipl1 ortholog. Catalytic subunit of the
Chromosomal Passenger Complex (CPC) with Pic1 (INCENP), Bir1 (Survivin/Cut17) and Nbl1 (Borealin).
355 aa Ser/Thr kinase; protein kinase domain 89-340; ATP binding; catalytic Lys118 (K118R = kinase-dead);
EC 2.7.11.1. Essential gene.

## Core function & localization
- Single fission yeast aurora kinase; executes functions split between aurora A and B in metazoans
  [PMID:11792803 "this single kinase is executing functions that are separately implemented by distinct aurora A and aurora B kinases in higher systems"].
- Dynamic CPC localization: G2 nuclear foci → prophase chromatin → kinetochores/centromeres in early mitosis →
  along spindle in anaphase → small central midzone zone that enlarges as spindle extends
  [PMID:11792803 "Following commitment to mitosis Ark1 associated with chromatin and was particularly concentrated at several sites including kinetochores/centromeres. Kinetochore/centromere association diminished during anaphase A, after which it was distributed along the spindle. The protein became restricted to a small central zone that transiently enlarged as the spindle extended"].
- Localization depends on Bir1/Cut17 [PMID:11554922 "The proper location of Ark1 requires Bir1/Cut17"];
  Bir1 colocalizes with Ark1(Aim1) at kinetochores and spindle midzone [PMID:11861551 "Bir1p colocalizes with the S. pombe Aurora kinase homolog Aim1p ... at the kinetochores as well as the spindle midzone during mitosis, and functional Bir1p is essential for localization of Aim1p to the kinetochores and the spindle midzone"].

## Kinase activity / substrates
- protein Ser/Thr kinase; phosphorylates histone H3 Ser10 [PMID:11792803 "Ark1 immuno-precipitates phosphorylated serine 10 of histone H3 in vitro. This activity was highest in mitotic extracts"; "the absence of the histone H3 phospho-serine 10 epitope from mitotic cells in which the ark1(+) gene had been deleted ... all suggest that Ark1 phosphorylates serine 10 of histone H3 in vivo"].
- Phosphorylates Bir1 [PMID:11950927 "Purified Ark1p phosphorylates N-terminal Bir1p fragments in vitro"].
- Phosphorylates condensin kleisin Cnd2 (Barren) throughout mitosis → condensin loading
  [PMID:21540296 "the Cnd2 subunit of condensin (also known as Barren) is the target subunit of Aurora-B-like kinase Ark1 and that Ark1-mediated phosphorylation of Cnd2 occurred throughout mitosis"].
- Aurora-B-dependent phosphorylation of condensin promotes association with H2A/H2A.Z
  [PMID:21633354 "overall condensin association with chromatin is governed by the chromosomal passenger kinase Aurora B. Aurora-B-dependent phosphorylation of condensin promotes its association with histone H2A and H2A.Z"].
- Phosphorylates CENP-C (Cnp3) Thr28 → impairs Cnp3-Mis12 interaction → error correction
  [PMID:29180432 "Thr28 of Cnp3 is a substrate of Ark1 (the Aurora B homolog of S. pombe), and phosphorylation impairs the interaction between the Cnp3 and Mis12 complex"].
- Phosphorylates Polo kinase Plo1 linker → SPB recruitment, mitotic entry during TOR recovery
  [PMID:21965528 "Ark1 phosphorylation of polo kinase Plo1 within the linker region between the kinase domain and polo boxes drives Plo1 onto the spindle poles where it promotes mitosis"].
- Proteome-wide aurora substrates identified by phosphoproteomics in fission yeast (chromatin regulation)
  [PMID:21712547 "we classified 70 sites (on 42 proteins) as probable targets of Aurora ... The involvement of these Aurora substrates in diverse aspects of chromatin dynamics"].

## Error correction / biorientation
- Aurora B destabilizes erroneous (merotelic/syntelic) attachments; in fission yeast inhibition leads to merotelic/syntelic attachment [PMID:25778919 "Inhibition of Aurora B using a Shokat mutant leads to chromosome segregation defects (Koch et al., 2011), such as merotelic or syntelic attachment"].
- CENP-C/Cnp3 phosphorylation participates in error correction [PMID:29180432 "CENP-C-Mis12-facilitated kinetochore attachment error correction to ensure accurate chromosome segregation during mitosis"].
- Spindle elongation forces cooperate with Aurora for merotelic correction; IGI with klp9/cut7
  [PMID:22264609 "a proper force balance between kinesin motors on interpolar spindle microtubules is critical for correcting merotelic attachments"].
- CPC phosphorylation by Cdk1 (Survivin) promotes centromere targeting & biorientation
  [PMID:20739936 "the chromosomal passenger complex (CPC), composed of catalytic kinase Aurora B and regulatory components ... must be localized to centromeres to phosphorylate kinetochore substrates"].
- Clp1/Flp1 phosphatase works with Aurora at kinetochores in biorientation/repair of mono-orientation
  [PMID:15525536 "Clp1p/Flp1p functions together with Aurora kinase at kinetochores ... a role in repairing mono-orientation of sister kinetochores"].

## Spindle assembly checkpoint
- Ark1 required for the attachment response (unlike budding yeast Ipl1 = tension only)
  [PMID:12676091 "the single aurora kinase of fission yeast, Ark1, is required for the attachment response"; required for Mad2 kinetochore association and Mad2-Mad3 complex; "the loss of Ark1 from kinetochores ... overides the checkpoint response to microtubule depolymerization"].
- Ark1 kinase activity directly required to maintain SAC arrest; PP1(Dis2) silences
  [PMID:19592249 "Aurora (Ark1) kinase activity is directly required to maintain spindle checkpoint arrest, even in the presence of many unattached kinetochores"].
- Ark1 is high in the hierarchy of SAC protein recruitment (with Mph1)
  [PMID:22825872 "a three-layered hierarchy with Ark1 and Mph1 on top, Bub1 and Bub3 in the middle, and Mad3 as well as the Mad1-Mad2 complex at the lower end"].
- CPC relocalization (Clp1/Klp9) controls anaphase onset; ark1 IPI with Klp9
  [PMID:28178520 "relocalization of Aurora B kinase and other components of the chromosome passenger complex (CPC) from centromeres to the spindle midzone ... mediated by Clp1 phosphatase-dependent interaction of CPC with Klp9/MKLP2 (kinesin-6)"].

## Chromosome condensation / segregation
- ark1Δ cells: cut phenotype, DNA fragmentation, fail sister chromatid segregation; essential
  [PMID:11950927 "ark1(+) ... is an essential gene required for sister chromatid segregation. Cells lacking Ark1p exhibit the cut phenotype, DNA fragmentation, and other defects in chromosome segregation"].
- H3S10 phosphorylation & condensin recruitment lost when Ark1 compromised
  [PMID:12676091 "Neither the phosphorylation of histone H3 that accompanies chromosome condensation nor condensin recruitment to mitotic chromatin were seen when Ark1 function was compromised"].

## Cytokinesis
- Overexpression of kinase-dead Ark1 (K147R, later K118R) inhibits cytokinesis → multiseptate; requires Pic1 binding
  [PMID:11950927 "Overexpression of a kinase-defective version of Ark1, Ark1-K147R, inhibits cytokinesis, with cells exhibiting an elongated, multiseptate phenotype ... the formation of Ark1p-Pic1p complexes is required for the execution of cytokinesis"].
- K118R kinase-dead: no Bir1 phosphorylation, dominant-negative inhibits cytokinesis (UniProt MUTAGEN).
- Note: PMID:12676091 found cytokinesis NOT affected by Ark1 depletion/K118R; some role nuance, but regulation of cytokinesis well-supported by CPC biology and Nbl1/Clp1-CR link [PMID:19570910 "Clp1 requires CPC activity for proper accumulation at the contractile ring (CR) ... a previously unrecognized connection between the CPC and the process of cytokinesis"].

## Telomeres
- Aurora B promotes telomere dispersion (metaphase) and disjunction (anaphase), preventing arm separation defects; localizes to telomeres [PMID:25778919 "a new role for Aurora B in telomere dispersion and disjunction during fission yeast mitosis ... disjunction occurs at anaphase after the phosphorylation of condensin subunit Cnd2"].

## Meiosis
- Aurora B repositioning by chiasmata ensures sister kinetochore mono-orientation at meiosis I; localizes to meiotic spindle/centromere [PMID:21920317 "Repositioning of aurora B promoted by chiasmata ensures sister chromatid mono-orientation in meiosis I"; Aurora B is "a destabilizer of kinetochore-microtubule attachment"].
- Bub1-H2A-S121 / shugoshin axis context for meiotic spindle localization [PMID:19965387].
- Autophagy regulates Aurora kinase levels at centromere/spindle in meiosis [PMID:26696398 "Aurora kinase ... is significantly increased at the centromere and spindle in the mutant cells"].

## Other
- Midzone: spindle disassembly study, ark1 at mitotic spindle midzone [PMID:25963819].
- Heat stress: nuclear/nucleolar proteins (including ark1 per PomBase IDA) aggregate into nucleolar rings [PMID:33176152].

## IPI partners (avoid bare protein binding; map to functional partner)
- PMID:11950927 WITH SPBC336.15 = pic1 (INCENP).
- PMID:28178520 WITH SPBC15D4.01c = klp9 (kinesin-6).
- PMID:15525536 WITH SPAC1782.09c = clp1/flp1 (Cdc14-like phosphatase).
