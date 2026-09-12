# LSS (Lanosterol synthase) — curation notes

UniProtKB:P48449 (LSS_HUMAN), HGNC:6708. EC 5.4.99.7. 732 aa. Chromosome 21.
Also known as OSC / 2,3-oxidosqualene-lanosterol cyclase (OSC).

## Core function
Lanosterol synthase (2,3-oxidosqualene-lanosterol cyclase) catalyses the
polycyclization of (S)-2,3-epoxysqualene (2,3-oxidosqualene) to lanosterol —
the reaction that forms the sterol nucleus, generating the first cyclic sterol
and the committed precursor of all downstream sterols including cholesterol.
It acts immediately after squalene epoxidase (SQLE). It is the final of three
steps in the "lanosterol from farnesyl diphosphate" sub-pathway (step 3/3).

- [PMID:7639730 "Lanosterol synthase [(S)-2,3-epoxysqualene mutase (cyclizing, lanosterol forming), EC 5.4.99.7] catalyzes the cyclization of (S)-2,3-oxidosqualene to lanosterol in the reaction that forms the sterol nucleus."] Human OSC cloned from liver cDNA; complemented yeast lanosterol-synthase-deficient mutant SMY8; cell-free homogenate converted 2,3-oxidosqualene to lanosterol (IGI with yeast ERG7 P38604).
- [PMID:14766201 "The monotopic integral membrane protein 2,3-oxidosqualene cyclase (OSC) catalyzes the formation of lanosterol the first sterol precursor of cholesterol in mammals."] Recombinant hOSC purified from Pichia; active as monomer; ER-membrane monotopic protein (EXP for MF and ER localization; direct protein sequencing 2-5).
- [PMID:15525992 "In a highly selective cyclization reaction OSC forms lanosterol with seven chiral centres starting from the linear substrate 2,3-oxidosqualene."] 2.1-2.2 Å crystal structures (PDB 1W6J, 1W6K) of human OSC with lanosterol and inhibitor Ro 48-8071; membrane-bound; active site (proton donor His455/Asp455 region; transition-state stabilizers).

Catalytic reaction (UniProt/Rhea): (S)-2,3-epoxysqualene = lanosterol; RHEA:14621; ChEBI:15441 -> ChEBI:16521; EC 5.4.99.7.
PATHWAY (UniProt): Terpene metabolism; lanosterol biosynthesis; lanosterol from farnesyl diphosphate: step 3/3.

## Localization
- Endoplasmic reticulum membrane; peripheral (monotopic) membrane protein.
  Strong experimental support: EXP PMID:14766201, EXP PMID:15525992, IDA PMID:30401459.
  UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Peripheral membrane protein".
- Lipid droplet: multiple proteomics/IDA annotations (PMID:14741744 HuH7 LD-enriched
  fraction proteomics; PMID:21498505 LPCAT1/2 LD study; IBA is_active_in). These are
  proteomic co-fractionation calls; LDs are contiguous with the ER and many ER lipid
  enzymes co-purify with the LD fraction. Real but secondary/non-core; keep as non-core.
- membrane (GO:0016020) HDA PMID:19946888 NK-cell membrane proteome — generic parent of
  ER membrane; redundant with the more specific ER-membrane calls.

## Disease (all recessive, loss of function / mislocalization)
- CTRCT44 congenital cataract (MIM:616509): W581R, G588S loss of LSS activity (PMID:26200341);
  I342S, W629C (PMID:29016354). Lanosterol reverses crystallin aggregation.
- HYPT14 hypotrichosis simplex (MIM:618275): L102V, L248P, F391S — protein present in ER
  but mislocalized to cytoplasm (PMID:30401459).
- APMR4 alopecia-intellectual disability syndrome 4 (MIM:618840) (PMID:30401459, PMID:30723320).
- PMID:26200341 IMP annotations: GO:0000250 (loss of LSS activity in mutants), GO:0006694
  steroid biosynthetic process, and GO:0031647 "regulation of protein stability" — the last
  reflects the paper's finding that lanosterol (the LSS product) prevents crystallin
  aggregation ("Engineered expression of wild-type, but not mutant, LSS prevents
  intracellular protein aggregation of various cataract-causing mutant crystallins").

## Downstream / regulatory
- PMID:17186944: OSC (LSS) inhibition diverts flux to 24(S),25-epoxycholesterol, an LXR
  agonist that up-regulates ABCA1/ABCG1/APOE. Supports LSS role in cholesterol
  biosynthetic process (IMP by inhibitor). Effect is on the pathway product, not a
  distinct MF; keep GO:0006695 (cholesterol biosynthetic process) as core.

## Interactions
- PMID:32296183 (HuRI): 7 binary interactors (YIF1A, AQP6, CIB1, SLC10A1, SLC10A6,
  TMEM167B, TMEM86B) — all bare GO:0005515 protein binding IPI. High-throughput Y2H;
  no functional interpretation. Uninformative MF; mark as over-annotated (do not REMOVE
  experimental IPI per policy). UniProt INTERACTION block lists the same 7 partners.

## Family / domain
- Terpene cyclase/mutase family (squalene/oxidosqualene cyclase). PANTHER PTHR11764:SF20
  LANOSTEROL SYNTHASE. InterPro IPR018333 Squalene_cyclase, IPR002365 Terpene_synthase_CS.
  PFTB (prenyltransferase-like) repeats x7. Monotopic α/α toroid fold.

## IEA/InterPro over-broad calls
- GO:0016866 intramolecular transferase activity (IEA InterPro) — a grandparent of the
  precise lanosterol synthase activity (GO:0000250, which is under isomerase/intramolecular
  transferase). Correct-branch but too general; modify to GO:0000250.
- GO:0016104 triterpenoid biosynthetic process (IEA InterPro) — squalene/oxidosqualene
  cyclase InterPro maps here for the whole cyclase family. Lanosterol IS a triterpenoid;
  in mammals LSS output feeds cholesterol biosynthesis. Correct but broad relative to the
  specific cholesterol/sterol process; keep as non-core.
</content>
</invoke>
