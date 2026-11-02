# GLN2 (At5g35630, Q43127) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are built only from cached publications (`publications/PMID_*.md`) and the UniProt record
(`GLN2-uniprot.txt`). No `-deep-research-*.md` file exists for this gene.

## Identity

- GLN2 / GS2 / GLN2;0, the sole plastid-type glutamine synthetase of Arabidopsis
  [PMID:28339983 "GS2, encoded by GLN2, is the only plastid-type GS in Arabidopsis thaliana."];
  [PMID:22303256 "Six Arabidopsis genes encode GS enzymes, but only GS2 (encoded by At5g35630) is targeted to the chloroplast"].
- Glutamine synthetase family (PROSITE GLNA_1/GLNA_ATP, Pfam Gln-synt_C); 45-aa transit
  peptide (UniProt TRANSIT 1..45).
- Leaf-specific, light-induced transcript (lambda Atgsl1) [PMID:1684022 "lambda Atgsl1, which represents the leaf-specific mRNA, is induced by light."].

## Activity

- Glutamine synthetase (EC 6.3.1.2): ATP + L-glutamate + NH4+ -> L-glutamine (UniProt,
  ECO:0000269 PubMed:15273293). GS activity measured in leaf mitochondria and attributed to GLN2
  [PMID:15273293 "we report glutamine synthetase (GS) activity in highly purified Arabidopsis thaliana mitochondria isolated from light-adapted leaf tissue."].
- Recombinant GS2 activity is increased by the ACT-domain protein ACR11 [PMID:28339983 "Here we showed that the recombinant ACR11 protein increased GS2 activity in vitro by reducing the Km values of its substrate glutamine."].

## Localization

- Chloroplast (stroma): many chloroplast/stromal proteomics datasets (PMID:16207701,
  PMID:18431481, PMID:20061580, PMID:18633119) plus transit peptide and targeting work.
- Mitochondria (disputed): GLN2::GFP in mitochondria and chloroplasts by microscopy and
  immunoblot [PMID:15273293 "In immunoblot experiments, a 41-kD chimeric GLN2::GFP protein was present in both leaf mitochondria and chloroplasts of these stably transgenic plants."];
  but GS was depleted from FFE-purified mitochondria [PMID:19223513 "However, GS is depleted from mitochondrial fractions highly purified by free-flow electrophoresis (FFE) relative to pre-FFE mitochondrial fractions, suggesting that it was primarily detected as a plastidic contaminant of incompletely purified mitochondrial fractions ( Eubel et al., 2007 )."]
  [PMID:22303256 "On the other hand, neither Fd-GOGAT nor GS have been identified in proteome analyses of the mitochondrial matrix ( Eubel et al., 2007 ; Jamai et al., 2009 )."].

## Physiological roles

- Photorespiratory ammonia refixation (with Fd-GOGAT GLU1) is the textbook role
  [PMID:22303256 "Re-assimilation of NH 3 takes place in the chloroplast through the sequential action of two enzymes, glutamine synthetase (GS; EC 6.1.3.2) and ferredoxin-dependent glutamine:oxoglutarate aminotransferase"].
- But GS2-deficient photorespiratory mutants come from barley (and Lotus), not Arabidopsis
  [PMID:22303256 "GS mutants have not been identified in Arabidopsis, but in barley ( Wallsgrove et al., 1987 )."].
- Arabidopsis gln2 T-DNA mutants are viable in air, smaller and slightly chlorotic, with
  impaired nitrogen metabolism [PMID:31622939 "It was shown that GS2 mutants although smaller, slightly chlorotic and with the nitrogen metabolism impaired, were able to grow and complete their life cycle under ordinary air conditions."].
  Redundancy with GS1 and GDH is proposed [PMID:34400629 "Thus, in A. thaliana, GLN2, GLN1s, and GDHs proteins could redundantly contribute to the re-assimilation of photorespiratory ammonia."].
- Primary nitrogen assimilation: gln2 mutants are impaired even at low photorespiration
  [PMID:34400629 "Even under conditions that lower photorespiration, the GLN2-deficient mutants show growth impairment, suggesting an important role of GLN2 in primary nitrogen assimilation."].
- GLN2 activity in shoots causes ammonium toxicity via acidification [PMID:34400629 "we show that ammonium assimilation by GLUTAMINE SYNTHETASE 2 (GLN2) localized in the plastid rather than ammonium accumulation is a primary cause for toxicity"].
- Review consensus [PMID:35279841 "there is no doubt that this enzyme has a central role in photorespiration."]
  with the Arabidopsis caveat [PMID:35279841 "Surprisingly, in Arabidopsis GS2 is not essential for plant survival"].

## Salicylic acid binding

- GS2 was a candidate in two SA-binding screens but **failed** validation in the same paper
  [PMID:25628632 "Analysis of protein phosphatase 2A (PP2A), GS2, and an α/β hydrolase superfamily member failed to meet the criteria for designation as SABPs (data not shown)."];
  [PMID:25628632 "However, while GS2 failed to exhibit binding to 3AESA in the SPR assay, GSR2 was found to be an SABP"].
  The HDA salicylic acid binding annotation is therefore contradicted by its own source.

## Curation decisions (summary)

- Core MF: glutamine synthetase activity (GO:0004356); core location chloroplast stroma.
- Core BP: ammonia assimilation cycle (GO:0019676, GS/GOGAT cycle) and L-glutamine
  biosynthesis; NEW photorespiration (GO:0009853) proposed because GS2 catalyses the
  ammonia-refixation step (participation test passed; GLU1, the partner enzyme in the same
  cycle, already carries photorespiration IMP; no GS2 ortholog in GOA carries any curated BP
  beyond IEA/IBA glutamine biosynthesis, so the absence reflects lack of curation rather than
  a convention). The non-essentiality of GS2 in Arabidopsis is recorded in the reason.
- Mitochondrion kept as non-core (disputed); thylakoid, envelope, ribosome, apoplast HDA
  marked over-annotated; SA binding removed; mRNA binding marked over-annotated.
