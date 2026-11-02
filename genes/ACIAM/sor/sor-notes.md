# sor (P29082, SOR_ACIAM) – Acidianus ambivalens sulfur oxygenase/reductase

## Provenance note

Automated deep research was unavailable for this review (falcon and openai providers
both failed authentication). No `-deep-research-*.md` file exists. The notes below were
compiled manually from PubMed searches (NCBI E-utilities, query "sulfur oxygenase reductase
Acidianus ambivalens" / "... Desulfurolobus") and the cached publications in
`publications/`. Most cached papers are abstract-only; PMID:21747782 (Veith et al. 2011)
and PMID:36191023 (cryo-EM, 2022) have full text.

## Identity

- 309 aa (308 after Met removal) homo-24-mer, ~871 kDa; Pfam PF07682 (SOR), dimeric
  alpha/beta-barrel fold. Organism formerly *Desulfurolobus ambivalens*; facultatively
  anaerobic, chemolithoautotrophic thermoacidophile (Sulfolobales).
- EC 1.13.11.55; Rhea:13957 (4 S + O2 + 4 H2O = 2 H2S + 2 sulfite + 6 H+).

## Activity

- Purified from aerobically grown cells; absent from anaerobic cells. "In the presence of
  oxygen but not under a hydrogen atmosphere, the enzyme simultaneously produced sulfite,
  thiosulfate, and hydrogen sulfide from sulfur" [PMID:2493451]. Thiosulfate is mostly a
  non-enzymatic product: "thiosulfate was produced mainly in a chemical reaction between
  sulfite and sulfur" [PMID:2493451]. Optimum 85 C, range 50-108 C.
- sor transcript 38-42x higher in aerobically grown cells [PMID:1522063 "The transcript of
  the sor gene in aerobically grown cells was amplified 38- to 42-fold relative to that in
  anaerobically grown cells"].
- Described as "the initial enzyme in the sulphur-oxidation pathway of Acidianus
  ambivalens" [PMID:15030315]; same framing in [PMID:21747782 "The sulfur oxygenase
  reductase (SOR) is the initial enzyme of the sulfur oxidation pathway in the
  thermoacidophilic Archaeon Acidianus ambivalens."].
- Physiological role debate: [PMID:31188531 "Initial studies indicated SOR catalyses the
  essential first step in oxidation of elemental sulphur, but an ancillary role for SOR as
  a 'recycle' enzyme has also been proposed."] Heterologous SOR + TQO restored sulfur
  oxidation in *S. acidocaldarius* DSM639 (but not autotrophy).

## Iron centre and active site

- One Fe per subunit, high-spin ferric EPR g=4.3, Em -268 mV; "mononuclear iron centre"
  [PMID:15030315 "Iron was found in the wild-type enzyme at a stoichiometry of one iron
  atom/subunit."].
- Mutagenesis: H86A, H90A, E114A inactive with no iron; C31A/S inactive with normal iron
  [PMID:15970399 "It was concluded that the Fe site with H86, H90 and E114 as ligands and
  C31 constitute the core active site whereas C101 and C104 optimize reaction conditions."].
- 1.7 A crystal structure [PMID:16484493 "A cysteine persulfide and a low-potential
  mononuclear non-heme iron site ligated by a 2-His-1-carboxylate facial triad in a pocket
  of each subunit constitute the active sites, accessible from the inside of the sphere.
  The iron is likely the site of both sulfur oxidation and sulfur reduction."].
- Zn2+ inhibits by binding a His in a side channel, Hg2+/IAA bind active site cysteines
  [PMID:21747782].

## Quaternary structure / localization

- Icosatetramer, 432 symmetry, hollow sphere with internal nanocompartment
  [PMID:15698962; PMID:16484493 "Twenty-four monomers form a large hollow sphere enclosing
  a positively charged nanocompartment."].
- Cytoplasmic: [PMID:21747782 "The spherical, hollow, cytoplasmic enzyme is composed of 24
  identical subunits"]. Kletzin 1989 called it a "soluble" enzyme [PMID:2493451]. Note that
  in *Acidianus tengchongensis* the orthologous SOR was also found associated with the
  cytoplasmic membrane [PMID:15691910 "SOR is not only present in the cytoplasm but also
  associated with the cytoplasmic membrane of A. tengchongensis"]; not shown for
  *A. ambivalens*.

## GO considerations

- GO:0033755 sulfur oxygenase/reductase activity (IEA, EC mapping) – correct, core.
- GO:0005737 cytoplasm (IEA SubCell) – correct.
- Missing: GO:0019417 sulfur oxidation (definition "addition of oxygen to elemental
  sulfur" – exactly the oxygenase half-reaction SOR performs). Comparator check: GO:0019417
  is carried by >2000 sulfur-oxidizing enzymes (e.g. SoxA family, by IEA), so the term is
  used for the enzymes performing sulfur oxidation steps; SOR itself catalyses the step.
- NOT GO:0070220 aerobic sulfur oxidation: its definition ties it to the sulfur
  dioxygenase reaction (a distinct enzyme, EC 1.13.11.18), so although SOR-dependent sulfur
  oxidation is O2-dependent, the term does not fit. Ontology pitfall for archaeal SORs.
- Missing: GO:0005506 iron ion binding – crystal structure + mutagenesis (IDA). The UniProt
  entry carries KW Iron / Metal-binding and FT BINDING Fe (86, 90, 114) but no KW2GO or
  UniRule metal-binding row was propagated into GOA.
- Only 5 proteins in all of GOA carry GO:0033755 (all IEA); no experimental GO annotations
  for any SOR despite four decades of biochemistry and multiple structures – archaeal
  under-annotation pattern.
