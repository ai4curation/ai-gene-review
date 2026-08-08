# RDH5 (Retinol dehydrogenase 5 / 11-cis retinol dehydrogenase) — review notes

UniProt: Q92781 (RDH5_HUMAN). HGNC:9940. 318 aa. Chromosome 12.
Gene synonyms: HSD17B9, RDH1, SDR9C5.

## Summary of function

RDH5 is a microsomal (endoplasmic-reticulum-membrane) NAD(H)-dependent short-chain
dehydrogenase/reductase (SDR family; SDR9C5) that oxidizes **cis-isomers of retinol**.
Its physiologically central role is in the **visual (retinoid) cycle** of the retinal
pigment epithelium (RPE), where it catalyzes the step following RPE65: oxidation of
**11-cis-retinol to 11-cis-retinal**, the chromophore that recombines with opsins to
regenerate rod and cone visual pigments.

- UniProt FUNCTION: "Catalyzes the oxidation of cis-isomers of retinol, including" ...
  "11-cis-, 9-cis-, and 13-cis-retinol in an NAD-dependent manner" ...
  "no activity towards all-trans retinal (By similarity). Plays a" ...
  "significant role in 11-cis retinol oxidation in the retinal pigment" ...
  "epithelium cells (RPE)." [file:human/RDH5/RDH5-uniprot.txt]
- Key point: **RDH5 does NOT act on all-trans-retinol/retinal** — so GO annotations to
  GO:0004745 "all-trans-retinol dehydrogenase (NAD+) activity" are the wrong-substrate
  term and should be replaced by GO:0106429 "11-cis-retinol dehydrogenase (NAD+) activity".
  The all-trans annotations are historical/family-level artifacts (SDR family default;
  Reactome models the reaction generically; PANTHER IBA family term).

## Catalytic activities (UniProt CATALYTIC ACTIVITY blocks) [file:human/RDH5/RDH5-uniprot.txt]

- 11-cis-retinol + NAD(+) = 11-cis-retinal + NADH + H(+)  (EC 1.1.1.315; RHEA:42060)
  Evidence: PubMed:10588954, 11675386, 9931293
- 9-cis-retinol + NAD(+) = 9-cis-retinal + NADH + H(+)  (RHEA:42052)
  Evidence: PubMed:9115228, 9931293
- 13-cis-retinol + NAD(+) = 13-cis-retinal + NADH + H(+)  (RHEA:42056)
  Evidence: PubMed:9931293
- androsterone + NAD(+) = 5alpha-androstan-3,17-dione + NADH + H(+) (EC 1.1.1.209; RHEA:20381)
  Evidence: PubMed:29541409, 9931293
- 5alpha-androstane-3alpha,17beta-diol + NAD(+) = 17beta-hydroxy-5alpha-androstan-3-one
  + NADH + H(+) (EC 1.1.1.53; RHEA:42004)  Evidence: PubMed:9931293

## Localization

- SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane" ; "Multi-pass membrane protein"
  ; "Lumenal side" [file:human/RDH5/RDH5-uniprot.txt]. IDA support (PubMed:11675386).
- ER membrane + ER lumen are both credible (multi-pass membrane protein with lumenal
  active site). GO:0044297 "cell body" is an Ensembl IEA projection from a rat ortholog
  (RGD) and is not supported by any RDH5 experimental data — over-annotation.

## Subunit / quaternary structure

- SUBUNIT: "Homodimer." (PubMed:11675386, cross-linking + molecular modeling).
  Abstract: "Cross-linking studies and molecular modeling showed that RDH5 is
  dimeric" [PMID:11675386]. Supports GO:0042803 protein homodimerization activity (IDA).

## Steroid / 3alpha-hydroxysteroid dehydrogenase activity (moonlighting)

- PubMed:9931293 (Wang et al. 1999, Biochem J, abstract): RDH5 "recognizes
  5alpha-androstan-3alpha,17beta-diol and androsterone as substrates
  (3alpha-hydroxysteroid dehydrogenase activity), but not testosterone,
  dihydrotestosterone, oestradiol and corticosterone". So both androsterone
  dehydrogenase (GO:0047023) and androstan-3alpha,17beta-diol dehydrogenase (GO:0047044)
  are directly supported (IDA).
- PubMed:29541409 (Fiandalo et al. 2018, Oncotarget, full text): RDH5 is one of four
  3alpha-oxidoreductases that convert 5alpha-androstane-3alpha,17beta-diol (DIOL) to DHT /
  androsterone (AND) to 5alpha-dione in the prostate "backdoor" androgen pathway; the
  catalytic Y175/K179 double mutant (Y->F,K->R) and Delta-cat abolish activity. Supports
  the EXP androsterone dehydrogenase annotation. This is a genuine secondary activity but
  extra-ocular / not the core evolved visual-cycle role — non-core.

## Biological process

- Visual perception (GO:0007601): TAS from PMID:10369264. RDH5 supplies 11-cis-retinal for
  visual pigment regeneration. PMID:10369264 abstract: "The metabolic pathways that produce
  11-cis retinal are important for vision because this retinoid is the chromophore residing
  in rhodopsin and the cone opsins." This is the core physiological process.
- retinoid metabolic process (GO:0001523) / retinol metabolic process (GO:0042572): both
  correct; retinol metabolic process is the more precise parent for the substrate class.
- steroid metabolic process (GO:0008202): correct (IDA, PMID:9931293) but non-core (the
  extra-ocular 3alpha-HSD activity).

## Disease

- Fundus albipunctatus (FALBI; MIM:136880): a fleck-retina form of congenital stationary
  night blindness with white dots and delayed dark adaptation. Caused by RDH5 loss-of-function
  variants. UniProt DISEASE block lists 13 PMIDs. PMID:10369264 (Nat Genet, first genetic
  demonstration) and PMID:11675386 (biochemical characterization of 11 FALBI mutants: "All
  RDH5 mutants showed decreased protein stability and subcellular mislocalization and, in
  most cases, loss of enzymatic activity in vitro and in vivo").

## GO annotation review decisions (see RDH5-ai-review.yaml)

- Core MF: GO:0106429 11-cis-retinol dehydrogenase (NAD+) activity (currently only IEA;
  promote via MODIFY of the all-trans annotations). NAD binding is a supporting sub-function.
- The many GO:0004745 all-trans-retinol dehydrogenase annotations (IBA, IEA-Ensembl, 4x
  Reactome TAS, 1x PINC TAS, 1x IDA) are MODIFY -> GO:0106429 (wrong substrate; RDH5 has no
  all-trans activity per UniProt). The IDA one (PMID:11675386) is an experimental annotation,
  so MODIFY (not REMOVE) — the enzyme is real, the substrate label is wrong.
- Steroid MFs (GO:0047023, GO:0047044) and steroid_metabolic_process: KEEP_AS_NON_CORE
  (real but extra-ocular moonlighting).
- GO:0004022 alcohol dehydrogenase (NAD+) — RHEA IEA; over-general parent; MARK_AS_OVER_ANNOTATED.
- GO:0016616 oxidoreductase (CH-OH...) — ARBA IEA; over-general; MARK_AS_OVER_ANNOTATED.
- GO:0044297 cell body — Ensembl IEA from rat ortholog; REMOVE (clearly-wrong IEA, no support).
- ER membrane / ER lumen: ACCEPT (IDA-backed; IBA/IEA duplicates KEEP/ACCEPT).
