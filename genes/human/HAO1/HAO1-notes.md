# HAO1 (Q9UJM8) review notes

## Identity
- HAO1 = hydroxyacid oxidase 1 = HAOX1 = glycolate oxidase (GO/GOX) = glyoxylate oxidase.
- HGNC:4809; chr 20; 370 aa; peroxisomal matrix; homotetramer; FMN-dependent.
- Member of the FMN-dependent alpha-hydroxy acid dehydrogenase family (TIM-barrel, PROSITE PRU00683).
- C-terminal PTS1 microbody targeting signal (residues 368-370, motif "SKI"-type).

## Verified function (grounded in UniProt Q9UJM8 + cached PMIDs)
- Broad-specificity **(S)-2-hydroxy-acid oxidase** that **preferentially oxidises glycolate -> glyoxylate**,
  using O2 as physiological electron acceptor and producing **H2O2** (EC 1.1.3.15; RHEA:16789 / RHEA:25311).
  [UniProt FUNCTION; PMID:10777549 abstract "most active on the two-carbon substrate, glycolate"].
- Also oxidises long-chain 2-hydroxy fatty acids (2-hydroxyhexadecanoate, 2-hydroxyoctanoate) with much
  lower efficiency -> contributes to fatty-acid alpha-oxidation [PMID:10777549; PMID:18215067].
- Can also oxidise glyoxylate -> oxalate (EC 1.2.3.5) in vitro, but PMID:18215067 explicitly states this
  is "most likely not relevant under normal conditions"; glycolate->glyoxylate is "the primary reaction".
- FMN is the cofactor [PMID:17669354, PMID:18215067]; product oxalate inhibits [PMID:17669354].
- Highly/tissue-enriched expression in **liver** (HPA: tissue-enriched liver); also pancreas/kidney [PMID:10777549].

## Physiology / disease
- Generates glyoxylate, the immediate precursor of oxalate. In primary hyperoxaluria (PH1: AGXT deficiency),
  glyoxylate is not detoxified to glycine and is converted to oxalate -> kidney stones/oxalosis.
- HAO1 (upstream of glyoxylate) is a validated therapeutic target: the siRNA drug **lumasiran** silences HAO1
  to reduce hepatic oxalate production. HAO1 loss is protective (substrate-reduction rationale), so there is
  no classic HAO1 loss-of-function Mendelian disease.
- PMID:10777549: HAOX1 in liver/kidney peroxisomes + ability to oxidise glyoxylate to oxalate implicate it in
  PH1 pathophysiology.

## Curation decisions (summary)
- Core MF in GOA and used here: **GO:0003973 (S)-2-hydroxy-acid oxidase activity** (verified label current).
- Core BP: **GO:0046296 glycolate catabolic process** (IDA PMID:18215067).
- Located in **peroxisome / peroxisomal matrix** (GO:0005777 / GO:0005782).
- FMN binding (GO:0010181) secondary (cofactor).
- glyoxylate oxidase (GO:0047969, glyoxylate->oxalate) = real IDA but non-core (not physiologically relevant).
- fatty acid alpha-oxidation (GO:0001561, IDA) + glycine biosynthetic process (GO:0006545, UniPathway) = non-core.
- oxidoreductase activity (GO:0016491), alcohol oxidase activity (GO:0047639), fatty acid oxidation (GO:0019395),
  cytosol (GO:0005829, import transit), response to oxidative stress (GO:0006979) = over-annotations.

## Publication cache status
- PMID:10777549 (Jones 2000), PMID:17669354 (Vignaud 2007), PMID:18215067 (Murray 2008): abstract-only cached
  (full_text_available: false; PMID:18215067 has abstract+partial discussion). PMID:10978532 (Williams 2000,
  glycolate oxidase cDNA) NOT cached — cited only via UniProt where relevant.
- supporting_text quotes below are verbatim substrings of the cached abstracts (grep-verified) or file: UniProt.
