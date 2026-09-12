# ABCD4 (O14678) review notes

Human ABCD4 / cblJ complementation group. ATP-binding cassette sub-family D member 4,
also historically PMP69 / P70R / PXMP1-L. HGNC:68. Chromosome 14q24.3, 606 aa.

## Verified biology (grounded in UniProt O14678 + cached PMIDs)

- **Molecular function**: ATP-dependent lysosomal cobalamin (vitamin B12) exporter.
  ABC transporter that hydrolyzes ATP and translocates cobalamin across the lysosomal
  membrane. EC 7.6.2.8; Rhea RHEA:17873 (R-cob(III)alamin(out) + ATP + H2O =
  R-cob(III)alamin(in) + ADP + Pi + H+). Km 426 uM cobalamin, Vmax 667 pmol/min/mg
  [PMID:33845046]. Reconstituted purified ABCD4 in liposomes transported cobalamin
  from inside to outside in an ATPase-dependent manner; the Walker A K427A mutant lost
  both ATPase and transport activity [PMID:33845046]. GOA current MF term:
  GO:0015420 "ABC-type vitamin B12 transporter activity" (EXP/IDA/IMP, PMID:33845046).

- **Biological process**: cobalamin transport (GO:0015889) / cobalamin metabolic
  process (GO:0009235). After transcobalamin-bound cobalamin is endocytosed and
  degraded in the lysosome, ABCD4 exports free cobalamin to the cytosol where MMACHC
  processes it into methylcobalamin (methionine synthase cofactor) and
  adenosylcobalamin (methylmalonyl-CoA mutase cofactor) [PMID:33845046, PMID:27456980].

- **Localization**: Lysosomal membrane (GO:0005765), multi-pass. Also ER membrane
  (GO:0005789) as biosynthetic intermediate — ABCD4 lacks its own peroxisomal
  targeting signal (no NH2-terminal hydrophilic region), is co-translationally
  inserted into the ER, and requires the escort protein LMBD1 (LMBRD1, Q9NUN5) to
  translocate to the lysosomal membrane [PMID:27456980, PMID:19010322, PMID:28572511].
  NOT peroxisomal — original peroxisomal assignment (PMID:9266848, PMID:9302272,
  PMID:14533738) was overturned; UniProt CAUTION note documents this. NOT|located_in
  peroxisome is experimentally supported [PMID:19010322, PMID:27456980].

- **Interactions**: LMBD1/LMBRD1 (Q9NUN5) escort/complex partner (functional, well
  supported); MMACHC (cytosolic B12 processing) forms trafficking complex
  [PMID:25535791]. Homodimer (self, O14678). High-throughput interactome hits:
  FAM234B (A2RU67), LMBRD1, self — from proteome-scale screens (PMID:28514442,
  PMID:33961781, PMID:40205054); these are bare "protein binding" and non-informative.

- **Disease**: Methylmalonic aciduria and homocystinuria type cblJ (MAHCJ, MIM:614857).
  Failure to release cobalamin from lysosomes; decreased AdoCbl and MeCbl
  [PMID:22922874, PMID:23141461, PMID:28572511].

## Curation decisions

Peroxisomal/fatty-acid IBA cluster (GO:0005778 peroxisomal membrane; GO:0005324
long-chain FA transmembrane transporter; GO:0006635 FA beta-oxidation; GO:0015910
LCFA import into peroxisome; GO:0042760 VLCFA catabolic process; GO:0007031
peroxisome organization) are propagated from peroxisomal ABCD1-3 paralogs and are
contradicted by ABCD4's demonstrated lysosomal localization and cobalamin (not fatty
acid) substrate. These are wrong for ABCD4 -> REMOVE (IBA over-propagation, arguable
on biological grounds per curation policy). GO:0005777 peroxisome IDA (PMID:14533738,
PMID:9302272) reflects the superseded early assignment; the NOT|peroxisome IDAs and
UniProt CAUTION overrule them.

Core: GO:0015420 (MF) + GO:0015889 cobalamin transport / GO:0009235 cobalamin
metabolic process (BP) + GO:0005765 lysosomal membrane (CC); ATP binding / ATP
hydrolysis secondary.

Deep research: falcon out of credits (HTTP 402); grounded in UniProt + GOA + cached PMIDs.
