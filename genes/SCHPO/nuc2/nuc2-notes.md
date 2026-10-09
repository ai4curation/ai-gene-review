# nuc2 (SPAC17C9.01c, UniProt P10505) — curation notes

## Identity

- Anaphase-promoting complex subunit 3 / Apc3; synonyms nuc2, apc3; "nuclear alteration protein 2",
  "nuclear scaffold-like protein p76". 665 aa, APC3/CDC27 family, TPR repeats (IPR019734, PF12895 ANAPC3)
  [file:SCHPO/nuc2/nuc2-uniprot.txt "Belongs to the APC3/CDC27 family."].
- Orthologue of budding yeast Cdc27 and human ANAPC3/CDC27. Comparator reviews: `genes/yeast/CDC16`
  (complete), `genes/human/CDC27` (complete); `genes/SCHPO/cut9` is still INITIALIZED.
- Cited as a fission yeast exemplar in `modules/metaphase_anaphase_transition_and_mitotic_exit.yaml`
  (APC/C TPR-subunit platform, PAINT node PTN000285286 "seeded by pombe nuc2 and budding-yeast CDC27").
- Not present in `gocams/index.tsv`.

## Literature timeline (cached publications; all abstract-only except PMID:15060174)

- PMID:3283148 (Hirano, Hiraoka, Yanagida 1988, J Cell Biol). Founding paper. nuc2-663 "specifically
  blocks mitotic spindle elongation at restrictive temperature so that nuclei in arrested cells contain a
  short uniform spindle (approximately 3-micron long), which runs through a metaphase plate-like structure
  consisting of three condensed chromosomes". Gene cloned; 665-residue internally repeating protein.
  Fractionation: "p67 cofractionates with nuclei and is enriched in resistant structure that is insoluble
  in 2 M NaCl". Source of the IDA nucleus row.
- PMID:2561424 (Yanagida 1989, review). "The roles of four representative genes, namely nda3+, nuc2+, top2+
  and dis2+ ... are discussed in regard to the mechanisms and control of chromosome separation." Source of
  one IMP mitotic sister chromatid segregation row; a review, but summarising the 1988 primary data.
- PMID:2297790 (Hirano et al. 1990, Cell). "The nuc2+ protein contains a domain, separated from ten 34
  amino acid repeat segments, that is capable of binding AT-rich DNA in vitro." The ts mutation lies in one
  repeat. The "snap helix" model is the pre-TPR description of the repeats. Proposed chromosome-scaffold
  model: "The nuc2+ protein may in one way bind to DNA and in another way mutually associate to form a part
  of the chromosome scaffold." Source of the IDA DNA binding row.
- PMID:7622618 (Kumada et al. 1995, J Cell Sci). "We previously showed that nuc2 is required for exit from
  the mitotic metaphase." "septation occurs in the absence of chromosome separation at the restrictive
  temperature" (cut phenotype). "The nuc2 mutant fails to arrest at the G1 phase upon nitrogen starvation at
  the permissive temperature which is a prerequisite for conjugation." "Ectopic overexpression of the nuc2+
  gene caused multiple rounds of S and M phases in the complete absence of septum formation." Three roles
  proposed: exit from mitosis, DNA replication restraint under starvation, inhibition of septation.
- PMID:9264466 (Yamada, Kumada, Yanagida 1997, J Cell Sci). "We show here that the fission yeast gene
  products Cut9 and Nuc2 are the subunits of the 20S complex, the putative APC (anaphase promoting
  complex)/cyclosome which contains ubiquitin ligase activity required for cyclin and Cut2 destruction."
  "The assembly of Cut9 into the 20S complex requires functional Nuc2, and vice versa." Key paper for the
  APC/C identity.
- PMID:9736616 (Kominami, Seth-Smith, Toda 1998, EMBO J; not cached, abstract read via Europe PMC). apc10,
  ste9/srw1 and rum1 mutants fail nitrogen-starvation G1 arrest and are sterile; Apc10 co-IPs with the APC;
  the deep research adds that nuc2-663 is synthetically lethal with apc10-27. Supports the interpretation
  of the "cell cycle switching, mitotic to meiotic" IMP row as an APC/C-Ste9 G1 function.
- PMID:12477395 (Yoon et al. 2002, Curr Biol). TAP/DALPC of both yeast APC/Cs: "Our data increase the total
  number of identified APC subunits to 13 in both yeasts". ComplexPortal source for the IPI/NAS rows.
- PMID:15060174 (Schwickart et al. 2004, MCB; cached full text). Cut9-TAP and Apc13-TAP from S. pombe:
  "Mass spectrometric analysis of the Cut9-TAP purification identified 10 proteins known or predicted to be
  APC/C subunits"; in budding yeast "The five proteins Cdc16, Cdc27, Apc9, Swm1/Apc13, and Cdc26 form a
  stable subcomplex". PomBase IDA APC/C row.
- PMID:16823372 (Matsuyama et al. 2006, Nat Biotechnol). ORFeome YFP localisation screen (4,431 proteins);
  PomBase HDA "cell division site" row. No Nuc2-specific text in the abstract.
- PMID:18208358 (Chew & Balasubramanian 2008, PLoS Genet; NOT cached, so not quotable in supported_by; read
  via the PLoS full text and summarised in the deep research). nuc2-663: Cdc7p and Sid1p persist at SPBs
  after septation, Sid2p persists at the division site, ~28% of cells have multiple septa. Nuc2p
  overproduction: rings form but collapse in late anaphase, Cdc7p/Sid1p fail to localise to SPBs
  (12/61 and 6/71 vs >=80% in controls). nda3-KM311 cut9-665 and nda3-KM311 lid1-6 do not accumulate
  multiple septa, so the SIN-inhibitory role appears not to require the rest of the APC/C; proposed
  mechanism via Spg1p nucleotide state / Byr4p-Cdc16p. Deep research quotes used instead:
  [file:SCHPO/nuc2/nuc2-deep-research-falcon.md "Loss of Nuc2 activity caused persistent SPB localization of
  Cdc7 and Sid1, persistent Sid2 at the division site, and formation of multiple actomyosin rings and septa."].

## Structural picture (from comparators and deep research)

- TPR lobe order Cdc23(innermost)-Cdc16-Cdc27(outermost); Apc3 is the subunit whose TPR groove binds the
  C-terminal IR tails of Cdc20/Cdh1 and of Apc10 [file:SCHPO/nuc2/nuc2-deep-research-falcon.md "Repeated
  TPR-lobe binding sites engage short linear motifs, including C-box and isoleucine–arginine tails on APC/C
  coactivators or associated subunits."]. Catalysis is Apc2-Apc11; degron reading is coactivator + Apc10
  [file:SCHPO/nuc2/nuc2-deep-research-falcon.md "Catalysis must be attributed to the holoenzyme rather than
  Nuc2."].
- Human APC3 has a flexible loop that binds the nucleosome acidic patch (Cirillo 2024; Skrajna 2025);
  untested for Nuc2 [file:SCHPO/nuc2/nuc2-deep-research-falcon.md "No direct S. pombe experiment establishes
  Nuc2 binding to nucleosomes or chromosomes through the same motif."].

## Curation decisions

- ACCEPT (15): both IMP sister chromatid segregation rows; nucleus IDA + IEA; all five APC/C rows
  (IBA, IDA x2, IEA, IPI); IBA metaphase/anaphase transition; IBA protein ubiquitination; IBA + NAS
  APC/C-dependent catabolic process; IBA cell division; IC mitotic sister chromatid separation.
- KEEP_AS_NON_CORE (3): IBA cytoplasm (open-mitosis seeds; nucleus is the primary site, but the SIN role
  and APC/C-Ste9 G1 role are cytoplasmic); HDA cell division site (single high-throughput observation,
  plausible given the septation-inhibitor role); IMP cell cycle switching mitotic->meiotic (APC/C-Ste9
  nitrogen-starvation G1 arrest, a real but non-core deployment).
- MARK_AS_OVER_ANNOTATED (1): IDA DNA binding from the 1990 in vitro AT-rich DNA binding of an isolated
  fragment; the chromosome-scaffold model was superseded by APC/C identification and no in vivo DNA binding
  has been shown. Not REMOVE, because the experimental observation is real and a chromatin-tethering loop
  exists in human APC3.
- MODIFY (1): IBA enzyme-substrate adaptor activity (GO:0140767, ANAPC7-seeded PTN002649387) ->
  ubiquitin ligase complex scaffold activity (GO:0160072), consistent with the CDC27 and CDC16 reviews.
- No NEW. Chew 2008 would support "negative regulation of septation initiation signaling" (GO:0031030)
  on nuc2, but GOA/QuickGO carry no annotation from PMID:18208358 on P10505, which suggests PomBase captured
  the observations as FYPO phenotypes rather than GO process annotations (the PomBase gene page is
  JS-rendered and the JSON API endpoints tried did not respond, so this could not be confirmed). Raised in
  suggested_questions instead; the term is used in core_functions[1] (validator warning accepted).
- Core functions: (1) APC/C TPR-lobe scaffold docking the coactivator/Apc10 IR tails (GO:0160072,
  contributes to GO:0061630; in APC/C; nucleus). (2) APC/C-independent SIN inhibition after cytokinesis
  (no MF asserted; GO:0031030 + cell division; cell division site).

## Validation

- `just validate SCHPO nuc2`: valid, 2 warnings (core_functions[1] cell division site and GO:0031030 not
  reflected as ACCEPT/NEW in existing_annotations). Rendered to nuc2-ai-review.html.
