# SMPD1 (P17405) review notes

Human sphingomyelin phosphodiesterase 1 / lysosomal acid sphingomyelinase (ASM, aSMase).
UniProtKB P17405 (ASM_HUMAN), HGNC:11120, gene on chr 11p15.4.

Deep research provider note: falcon is out of credits (HTTP 402), so no
`-deep-research-falcon.md` was generated. This review is grounded in the seeded
UniProt record (`SMPD1-uniprot.txt`), the GOA TSV, and the 26 cached
`publications/PMID_*.md` files, all of which were present.

## Core biology (verified)

- **Molecular function**: sphingomyelin phosphodiesterase (EC 3.1.4.12); hydrolyses
  sphingomyelin + H2O -> ceramide + phosphocholine. UniProt CC FUNCTION:
  "Converts sphingomyelin to ceramide" (PubMed:12563314, 1840600, 18815062,
  25339683, 27659707, 33163980). Catalytic activity RHEA:19253 EC=3.1.4.12.
  Zn2+-dependent (2 Zn2+ per subunit; COFACTOR Name=Zn(2+)). Also has EC 3.1.4.3
  phospholipase C activity toward phosphatidylcholine (PubMed:25339683).
  GOA carries the primary MF as GO:0004767 (sphingomyelin phosphodiesterase
  activity) with many EXP/IDA/TAS lines, and GO:0061750 (acid sphingomyelin
  phosphodiesterase activity, a child) with IBA/IDA/IEA lines.
- **Biological process**: sphingomyelin/ceramide metabolism — sphingomyelin
  catabolic process (GO:0006685), producing ceramide. Note: GOA labels ceramide
  production as "ceramide biosynthetic process" (GO:0046513) as well as
  "sphingomyelin catabolic process" (GO:0006685) — same reaction, two aspects.
- **Localization**: lysosome / lysosomal lumen (GO:0005764 / GO:0043202),
  endolysosome (GO:0036019); also a secreted (Zn2+-activated) form in the
  extracellular region (GO:0005576), arising from alternative trafficking of the
  same precursor (PubMed:8702487, 9660788, 20807762, 21098024). Lysosomal
  targeting via M6P receptor and sortilin (PubMed:16787399).
- **Disease**: Niemann-Pick disease types A (NPDA, MIM:257200) and B (NPDB,
  MIM:607616) — acid sphingomyelinase deficiency, a lysosomal storage disorder
  from failure to hydrolyze sphingomyelin to ceramide (UniProt DISEASE;
  PubMed:1718266, 7670466, 15877209, 18815062, 27659707).

## Two enzymatic forms (one gene)

Lysosomal L-SMase (Zn2+-independent because Zn2+ acquired during trafficking) and
secretory S-SMase (Zn2+-dependent) arise from differential trafficking of a common
precursor, NOT alternative splicing (PubMed:8702487, 9660788, 20807762, 21098024).
Secreted form induced by IL1B/TNF/IFNG and by bacterial/viral infection; secretion
depends on Ser508 phosphorylation (PubMed:17303575, 20807762).

## Secondary/pleiotropic roles (real but non-core)

- Stress-induced apoptosis via ceramide (ionizing radiation, UV, TNF/CD95)
  (PubMed:8706124, 17303575, 20956541).
- Plasma-membrane repair: Ca2+-triggered lysosomal exocytosis releases ASM, which
  converts outer-leaflet SM to ceramide, promoting endocytosis of lesions
  (PubMed:20530211).
- Host defense / pathogen entry: ceramide-rich membrane platforms for P. aeruginosa
  (PubMed:12563314); ASM activity required for Ebola (PubMed:22573858) and
  SARS-CoV-2 (PubMed:33163980) entry.
- Cholesterol export from endolysosomes / NPC2-mediated transfer (PubMed:25339683).

## Annotation issues flagged

- **PMID:19279008 and PMID:19279011 are about acid beta-glucosidase 1 (GBA1), not
  SMPD1.** The BHF-UCL IMP annotations transferred to SMPD1 for GO:0043409
  (negative regulation of MAPK cascade), GO:0023021 (termination of signal
  transduction), and GO:0046513 (ceramide biosynthetic process) rest on papers
  whose experimental manipulations (siRNA/overexpression) target GBA1. 19279011
  mentions that acid sphingomyelinase "has been implicated, in part, in providing
  substrate" for the salvage pathway, but the IMP evidence is on GBA1. Per policy
  (do not REMOVE experimental annotations whose full text I cannot fully verify),
  these are marked MARK_AS_OVER_ANNOTATED / UNDECIDED rather than REMOVE, with the
  GBA1-vs-SMPD1 concern documented.
- GO:0034480 (phosphatidylcholine phospholipase C activity) IDA PMID:25339683 is a
  genuine in-vitro side activity (EC 3.1.4.3) but not the core/physiological
  function; kept as non-core. The FlyBase-assigned IDA line (row 31) for the same
  term against PMID:25339683 is a human enzyme paper; kept as non-core.
- Bare `protein binding` GO:0005515 IPIs (CASP7 PMID:21157428; NPC1 partner
  Q99523 PMID:16787399) are uninformative MF — MARK_AS_OVER_ANNOTATED per policy.
- IEA phosphatidylcholine phospholipase C (row 14) and hydrolase activity
  (row 13) are broad; PLC C activity accepted as non-core, generic hydrolase
  marked over-annotated (uninformative parent).
