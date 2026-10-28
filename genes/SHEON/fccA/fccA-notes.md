# fccA (SO_0970, UniProtKB:P83223) notes

No provider deep research was run (no API keys available); compiled manually from the
cached publications, the UniProt record, and PubMed searches ("fccA AND Shewanella",
"flavocytochrome c3 AND Shewanella oneidensis").

## Identity

Swiss-Prot FCCA_SHEON, 596 aa precursor, signal peptide 1-25, mature chain 26-596.
N-terminal tetraheme cytochrome c domain (Pfam PF14537) plus FAD-binding flavoprotein
domain (PF00890) and a flexible capping domain. PANTHER PTHR43400:SF7. Older names:
flavocytochrome c, Fcc3, flavocytochrome c3. Early structural work calls the strain
"Shewanella putrefaciens MR-1", the same strain now named S. oneidensis MR-1.

## Fumarate reductase activity and cofactors

- Crystal structures (PDB 1D4C/1D4D/1D4E) with fumarate and with succinate bound
  [PMID:10581551 "The soluble fumarate reductase of Shewanella putrefaciens MR-1 is a
  periplasmic tetraheme flavocytochrome c."], with all redox centres in van der Waals
  contact [PMID:10581551 "efficient conduit of electrons from the hemes via the FAD to
  fumarate"].
- UniProt COFACTOR (ECO:0000269|PubMed:10581551): one non-covalent FAD per subunit and
  four covalently bound heme c per monomer; SUBUNIT: monomer. The flavin is FAD, not FMN.
- UniProt CATALYTIC ACTIVITY: 2 Fe(III)-[cytochrome c] + succinate = fumarate + 2
  Fe(II)-[cytochrome c] + 2 H(+) (RHEA:77903, EC 1.3.2.4), run physiologically in the
  fumarate-reducing direction.
- Electron donor is the inner-membrane menaquinol dehydrogenase CymA
  [PMID:12899636 "CymA(sol) efficiently reduces S. oneidensis fumarate reductase"];
  [PMID:22458729 "the reduced enzyme forms a 1:1 complex with its redox partner Fcc3"].
  Complex formation biases CymA catalysis toward menaquinol oxidation
  [PMID:23799249 "CymA alone could only reduce MQ-7, while the CymA-Fcc3 complex
  catalyzed the reaction required to support anaerobic respiration"].
- Terminal fumarate reductase, maturated by periplasmic FAD loading
  [PMID:31175188 "uses a periplasmic flavocytochrome, FccA, both as a terminal fumarate
  reductase and as a periplasmic electron transfer hub for extracellular respiration"].

GO has no term for EC 1.3.2.4 (fumarate reductase (cytochrome)). Nearest existing terms
are GO:0000104 succinate dehydrogenase activity (generic acceptor; the parent GO places
fumarate reductase (NADH) under) and GO:0016632 oxidoreductase activity, acting on the
CH-CH group of donors, cytochrome as acceptor. A new term is proposed in the review.

## Periplasmic electron-transfer hub and electron storage

- Abundant in the periplasm of anaerobic/ferric-citrate-reducing cells; reduced by CymA
  and able to exchange electrons bidirectionally with MtrA
  [PMID:19837833 "Further experiments showing a bidirectional electron transfer between
  FccA and MtrA provided evidence for an electron transfer network in the periplasmic
  space"], and the deletion mutant suggests electron storage
  [PMID:19837833 "suggest a role of FccA as a transient electron storage protein"].
- NMR mapping shows single-heme, transient interactions with both partners
  [PMID:23067389 "interact with their redox partners, CymA and MtrA, through a single
  haem"], with FccA and STC competing for MtrA but FccA not interacting with MtrD or
  DmsE [PMID:26175726 "neither STC nor FccA interact with MtrD"].
- FccA and STC are functionally redundant hubs; single mutants are near-normal
  [PMID:25635641 "Single mutants of either of these two cytochromes show only minor
  phenotypic changes, if at all."], while double mutants are impaired for Fe(III),
  nitrate, DMSO and fumarate respiration [PMID:25635641 "Double deletion mutants showed
  either delayed growth or no growth with ferric iron, nitrate, dimethyl sulfoxide or
  fumarate as electron acceptor."].

## Selenite reduction (the CMMMech-relevant role)

- In non-growing MR-1 suspensions, selenite reduction is strongly fccA-dependent
  [PMID:24435070 "selenite reduction by ΔfccA was severely suppressed, with a 60%
  decrease in the reduction rate within the initial 12 h"], while ΔnapA and ΔnrfA behave
  like wild type and the Mtr pathway contributes little. Added fumarate competes with
  selenite, consistent with reduction occurring at FccA itself.
- The reduction product is cell-associated Se(0); the authors place the reduction in the
  periplasm [PMID:24435070 "we identify fumarate reductase FccA as the terminal reductase
  of selenite in periplasm"], and selenite reduction depends on CymA as the upstream
  electron donor.

### Where CMMMech is stronger than the evidence

`/home/user/CMMMech/data/records/selenium.yaml` (node `fcca_fumarate_reductase`, and the
matching `protein_examples` entry) states that FccA is "the principal periplasmic
selenite Se(IV) reductase" and that it is a "fumarate/selenite reductase" catalysing
reduction of selenite to elemental selenium. The published evidence is a single
deletion-mutant rate experiment (PMID:24435070): ΔfccA retains ~40% of the wild-type
initial rate and substantial later reduction, there is no complementation, and no
purified-FccA selenite-reduction assay has been reported. So "FccA is required for most
of the early periplasmic selenite reduction under these conditions" is supported;
"FccA is a selenite reductase" (a direct catalytic claim) is an inference from genetics
plus the fumarate-competition experiment, not a demonstrated enzymatic activity. The
review therefore records no selenite-reductase molecular function and keeps the selenite
role as an involvement statement. (CMMMech was not edited.)

Note also that CMMMech's `protein_examples` entry for P83223 lists InterPro:IPR010960
etc. correctly but gives the EC as 1.3.2.4, which matches UniProt; no identifier error
was found for this accession.

## Localization

Periplasm, UniProt ECO:0000269|PubMed:19837833 and the structural/purification work;
no evidence for a cytoplasmic pool. The IBA cytoplasm annotation derives from eukaryotic
and archaeal soluble fumarate reductases in PANTHER node PTN000180369 and does not hold
for this signal-peptide-bearing periplasmic protein.
