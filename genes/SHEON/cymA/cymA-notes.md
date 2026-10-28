# cymA (SO_4591, UniProtKB:Q8E8S0) review notes

No provider deep-research file was generated for this gene (no API keys in this
environment). These notes are a manual literature review; every assertion carries
an inline quote from a cached publication under `publications/`.

## Identity

- Swiss-Prot entry CYMA_SHEON, 187 aa, *Shewanella oneidensis* MR-1 (originally
  described as *S. putrefaciens* MR-1). NapC/NirT/NrfH family (IPR024717, PF03264,
  PIRSF000013), PANTHER PTHR30333:SF3.
- N-terminal single transmembrane helix (13-33) with a periplasmic tetraheme
  domain (34-187); UniProt topology rests on the soluble-domain work of Schwalb et al.
  [PMID:12899636 "It is located in the cytoplasmic membrane where the bulk of the protein is exposed to the periplasm, enabling it to transfer electrons to a series of redox partners."]

## Localization

- Cytoplasmic (inner) membrane, with a minor soluble pool after fractionation
  [PMID:9023196 "The CymA protein was found in the cytoplasmic membrane and soluble fraction of MR-1"];
  the full-text follow-up attributes the soluble pool to release during fractionation
  [PMID:10613864 "the subcellular fractionation process could cause the release of a small amount of CymA into the soluble fraction"].

## Cofactors and catalysis

- Four c-type hemes: three low-spin His/His and one high-spin His/H2O heme next to the
  quinol site [PMID:22458729 "identifies three low-spin His/His co-ordinated c-haems and a single high-spin c-haem with His/H(2)O co-ordination lying adjacent to the quinol-binding site"].
- Quinol dehydrogenase using menaquinol; menaquinone-7 is both substrate and a required
  cofactor [PMID:22393052 "vesicle-bound menaquinone-7 is not only a substrate for this enzyme but is also required as a cofactor when converting other quinones"].
- Monotopic membrane protein, "the smallest example of a quinol dehydrogenase in nature"
  [PMID:22393052 "CymA is a monotopic membrane tetraheme c-type cytochrome belonging to the NapC/NirT family"].
  There is no evidence that CymA itself pumps or translocates protons; the protons from
  quinol oxidation are released on the periplasmic side, and the protonmotive
  contribution belongs to the redox loop with the quinone-reducing dehydrogenases.
- Thermodynamics: reduction of CymA by menadiol needed the driving force from NADH
  oxidation [PMID:22458729 "CymA is reduced with menadiol (E(m) = -80 mV) in the presence of NADH (E(m) = -320 mV) and an NADH-menadione (2-methyl-1,4-naphthoquinone) oxidoreductase, but not by menadiol alone"].

## Redox partners (electron acceptors)

- Flavocytochrome c3 fumarate reductase FccA: direct electron transfer from purified
  soluble CymA [PMID:12899636 "by direct measurements of electron transfer between the purified proteins, that CymA(sol) efficiently reduces S. oneidensis fumarate reductase"];
  1:1 complex with reduced CymA [PMID:22458729 "the reduced enzyme forms a 1:1 complex with its redox partner Fcc3"].
- MtrA (periplasmic decaheme subunit of the MtrCAB conduit) and FccA reduced by CymA in vitro
  [PMID:19837833 "In vitro fumarate reductase FccA and c-type cytochrome MtrA were reduced by the cytoplasmic membrane-bound protein CymA."].
- Small tetraheme cytochrome (STC/CctA) as the main periplasmic shuttle
  [PMID:26175726 "It accepts electrons from CymA and distributes them to a number of terminal oxidoreductases involved in the respiration of various compounds."].
- Nitrate/nitrite: CymA replaces both NapC and NrfH
  [PMID:19387485 "CymA, a cytoplasmic membrane electron transport protein, is likely to be the functional replacement of both NapC and NrfH in S. oneidensis"].
- Heterologous: CymA expressed in *E. coli* is sufficient to confer Fe(III)-NTA
  reduction, and spheroplasts reduce Fe(III) citrate and AQDS
  [PMID:18394146 "expression of cymA was necessary and sufficient to convert E. coli into a DIR bacterium"].
  This is a ferric reductase activity of CymA in a heterologous membrane; in MR-1,
  electrons are routed to Fe(III) via MtrA/MtrCAB. I did not add a ferric-reductase MF
  row: the physiologically demonstrated acceptors are c-type cytochromes.

## Genetics (necessity, not by itself participation)

- A clean cymA replacement mutant with wild-type menaquinone levels cannot reduce
  Fe(III), Mn(IV) or nitrate, and cannot grow on fumarate; complementation restores all
  of it [PMID:10613864 "the knockout of cymA renders the cells unable to reduce nitrate, Fe(III), and Mn(IV) and unable to grow anaerobically with fumarate as the electron acceptor"].
  The earlier transposon mutant was in a rifampicin-resistant background that was itself
  menaquinone-depleted, which the 2000 paper corrects; this matters because it was the
  basis of the original claim [PMID:9023196 "This gene complemented a mutant which had a TnphoA insertion in cymA and which was deficient in the respiratory reduction of iron(III), nitrate, fumarate, and manganese(IV)."].
- Also required for DMSO growth and nitrite reduction
  [PMID:12899636 "We also demonstrate that CymA is essential for growth with DMSO (dimethyl sulfoxide) and for reduction of nitrite, implicating CymA in at least five different electron transfer pathways in Shewanella."].
- Not required for O2 or TMAO respiration (UniProt DISRUPTION PHENOTYPE), which places
  CymA in the branch leading to periplasmic and surface acceptors rather than in a
  general respiratory role.
- V(V): the cymA mutant shows essentially no reduction
  [PMID:15006760 "MR1-CYMA (which lacks the CM cytochrome CymA) showed essentially no V(V) reduction (Fig."].
- Selenite: rate drops to about a tenth of wild type
  [PMID:24435070 "The selenite reduction rate of \u0394cymA was only 9.6% of that of the wild-type strain (0.096 \u03bcmol h\u22121vs. 1.000 \u03bcmol h\u22121)."].

## Review decisions worth recording

- `GO:0019333 denitrification pathway` (IEA from InterPro IPR024717) is wrong for this
  protein and, as a blanket family mapping, for the family. Denitrification is defined
  as reduction of nitrate all the way to dinitrogen; *S. oneidensis* performs
  respiratory ammonification (nitrate to nitrite to ammonium) and has no NO or N2O
  reductase in this pathway [PMID:19387485 "we present evidence that reduction of nitrate to ammonium in S. oneidensis is carried out by these atypical systems in a two-step manner"].
  InterPro's own entry name is "Denitrification system component NapC/NirT/NrfH", but the
  family includes NrfH, a subunit of the ammonium-forming nitrite reductase complex.
  Recorded as a `source_defects` entry against the interpro2go mapping (DELETE_VALUE).
- `GO:1902600 proton transmembrane transport` is an inter-ontology inference from
  GO:0008121, which carries proton-transporter parentage because of the cytochrome bc1
  Q-cycle. CymA has no Q-cycle: it is a monotopic single-TM protein with the catalytic
  domain wholly periplasmic, so the protons released on quinol oxidation are released on
  the side they are already on. Marked MARK_AS_OVER_ANNOTATED rather than REMOVE,
  since the row is a mechanical consequence of a term the gene legitimately carries.
- `GO:0016020 membrane` is MODIFY to `GO:0005886 plasma membrane`, which the gene already
  carries by direct evidence.

## CMMMech cross-check

Ten CMMMech records ground mechanisms to Q8E8S0 (uraninite, selenium, rhodochrosite,
uranium, chlorite, montmorillonite, nontronite, silver, vanadium, chromium). Their
`functional_role` text ("inner-membrane tetraheme c-type menaquinol dehydrogenase CymA
(EC 7.1.1.8; SO_4591) transferring electrons from the menaquinol pool to periplasmic and
outer-membrane electron-transfer pathways") is accurate and matches Swiss-Prot.

Evidence levels look right as set:

- `selenium.yaml` marks CymA `supports: support`, which the mutant kinetics justify, and
  the record itself already flags that the reduction is not abolished.
- The other nine mark CymA `supports: partial`, with explanations saying the cited
  studies did not mutate cymA. That is the correct reading for uraninite, chromium,
  rhodochrosite, uranium, chlorite, montmorillonite, nontronite and silver.
- `vanadium.yaml` is the one case where the supporting literature is stronger than
  `partial` suggests: Myers et al. 2004 does test the cymA mutant directly and finds
  essentially no V(V) reduction [PMID:15006760 "MR1-CYMA (which lacks the CM cytochrome CymA) showed essentially no V(V) reduction (Fig."].
  The CMMMech record cites Wang et al. (2010) rather than that paper, so the `partial`
  label is right for the cited source; a curator adding PMID:15006760 could raise it.
  No CMMMech file was edited here.

Nothing in the CMMMech text overstates CymA. The general caution that applies across all
ten records is that CymA is upstream of the metal-reducing step: it is a menaquinol
dehydrogenase whose demonstrated acceptors are c-type cytochromes, so for each mineral
the terminal reductase (MtrC/OmcA, FccA, or another) does the metal chemistry and CymA
supplies the electrons.
