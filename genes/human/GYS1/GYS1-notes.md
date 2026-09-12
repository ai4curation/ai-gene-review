# GYS1 (human) review notes

UniProtKB:P13807 — Glycogen [starch] synthase, muscle. HGNC:4706. 737 aa. Chr 19.
EC 2.4.1.11. CAZy GT3 (glycosyltransferase family 3). Reactome R-HSA-3322077 (Glycogen synthesis).

## Core biology (verified)

- GYS1 is the muscle (and general non-hepatic) isoform of glycogen synthase; GYS2 is
  the liver isoform (~69% identity). GYS1 is expressed in most tissues including muscle
  and brain [PMID:35835870, "GYS1 is expressed in most tissues including the muscle and brain7, whereas GYS2 is expressed only in the liver."].
- Committed/rate-limiting elongation enzyme of glycogen biosynthesis. It uses UDP-glucose
  as glucosyl donor and adds glucose in alpha-1,4-glycosidic linkage to the non-reducing
  end of a growing chain [PMID:35835870, "GYS, a retaining glycosyltransferase (GT) belonging to the GT3 superfamily, catalyzes successive addition of α-1,4-linked glucose residues to the nonreducing end of a growing polysaccharide chain, using UDP-glc as the sugar donor with the release of UDP5."].
- Works together with glycogenin (GYG1, primer) and glycogen branching enzyme (GBE1,
  alpha-1,6 branches) [PMID:35835870, "Glycogen synthesis is a multistep process consisting of a priming step by GYG followed by an elongation step carried out by GYS and then a branching step by GBE."; UniProt FUNCTION].
- Forms a physical complex with glycogenin GYG1 (GYS1 tetramer + 2 GYG1 dimers,
  heterooctamer) [UniProt SUBUNIT; PMID:17055998; PMID:35835870 cryo-EM]. GYG1 interaction
  established by Y2H and structurally [PMID:17055998, "Two glycogen synthase-interacting proteins were identified in human skeletal muscle, glycogenin-1 and nebulin."].

## Regulation

- Allosterically activated by glucose-6-phosphate; inhibited by multi-site phosphorylation
  (GSK3, AMPK, CK2, PASK, DYRK2, phosphorylase kinase); dephosphorylation by PP1 (recruited
  by PPP1R3 subunits e.g. PTG/PPP1R3C) activates it [PMID:35835870; UniProt ACTIVITY REGULATION/PTM].
- "activation by the effector Glc6P8,9 and inhibition by reversible phosphorylation10"
  [PMID:35835870].

## Catalytic-error / phosphate incorporation (Lafora relevance)

- GYS1 can incorporate the beta-phosphate of UDP-glucose into glycogen at ~1 per 10,000
  glucoses (C2/C3 phosphomonoesters), a rare "catalytic error"; laforin (EPM2A) removes it.
  [PMID:21356517, "the biosynthetic enzyme glycogen synthase, which normally adds glucose residues to glycogen, is capable of incorporating the β-phosphate of its substrate UDP-glucose"].
- NOTE on GO:0061547 "glycogen synthase activity, transferring glucose-1-phosphate":
  this term describes the phosphate-transferring side reaction, which PMID:21356517 shows
  is a low-frequency side activity (~10^-4), NOT the physiological function. The
  canonical, physiological activity is GO:0004373 (UDP-glucose -> alpha-1,4 elongation).

## Localization

- Cytosolic; associates with glycogen particles. UniProt/GOA: cytoplasm (IBA), cytosol
  (IEA/TAS). Membrane HDA (PMID:19946888) is from an NK-cell membrane-proteome screen that
  itself flags most non-integral hits as transiently membrane-associated; GYS1 has no TM
  region (UniProt) — treat membrane as over-annotation. "inclusion body" (IEA from mouse
  ortholog) likely reflects glycogen/Lafora-body-type aggregates, non-core.

## Disease

- Muscle glycogen storage disease 0 (GSD 0b, MIM:611556): fasting hypoglycemia, cardiomyopathy,
  exercise intolerance, risk of sudden cardiac death [UniProt DISEASE; PMID:17928598;
  PMID:19699667 case of homozygous GYS1 deletion causing sudden cardiac death].

## Annotation review decisions (summary)

- MF GO:0004373 (alpha-1,4-glucan glucosyltransferase, UDP-glucose donor): ACCEPT (core;
  IBA, IEA, EXP x2). This is the canonical activity.
- MF GO:0061547 (glycogen synthase activity, transferring glucose-1-phosphate): the EXP
  (PMID:21356517) supports a low-frequency side reaction; keep as non-core / over-annotated.
- BP GO:0005978 (glycogen biosynthetic process): ACCEPT core (IBA/IEA/TAS/IDA).
- BP GO:0005977 (glycogen metabolic process): broader parent, KEEP_AS_NON_CORE.
- CC cytosol GO:0005829 / cytoplasm GO:0005737: ACCEPT (cytosol is the informative one).
- CC membrane GO:0016020 (HDA): MARK_AS_OVER_ANNOTATED (proteomics artifact; no TM).
- CC inclusion body GO:0016234 (IEA, mouse): KEEP_AS_NON_CORE.
- CC catalytic complex GO:1902494 (IDA, ComplexPortal): ACCEPT (GYS1-GYG1 complex).
- MF D-glucose binding GO:0005536 (IEA): KEEP_AS_NON_CORE (substrate-binding aspect of catalysis).
- All GO:0005515 protein binding IPIs (bare "protein binding"): MARK_AS_OVER_ANNOTATED per
  curation guideline (uninformative); several are high-throughput interactome screens
  (HuRI/BioPlex/OpenCell). GYG1, PPP1R3C, GSK3B partners are functionally meaningful and
  could support more specific terms.
- Reactome TAS cytosol/glycogen-biosynthesis entries: ACCEPT / KEEP (localization + process).
