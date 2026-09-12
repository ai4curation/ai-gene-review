# AMPD2 (AMP deaminase 2, liver-type) — review notes

UniProtKB: Q01433 (AMPD2_HUMAN). HGNC:469. Human, NCBITaxon:9606.
Deep research: falcon provider was OUT OF CREDITS (HTTP 402); no `-deep-research-falcon.md` generated.
This review is grounded in the cached UniProt record, the seeded GOA, and cached publications.

## Core biology

- AMPD2 is the **liver-type ("L") isoform** of AMP deaminase, one of three mammalian AMPD
  paralogs (AMPD1 muscle/"M", AMPD2 liver/"L", AMPD3 erythrocyte/"E"). It is **broadly/
  widely expressed** including brain and neurons, and is **highly expressed in cerebellum**
  [UniProt TISSUE SPECIFICITY; PMID:23911318 "AMPD2 and -3 with widespread expression"].
- **Molecular function:** hydrolytic deamination of AMP to IMP + ammonia (zinc metalloenzyme,
  binds 1 Zn2+ per subunit; homotetramer). EC 3.5.4.6.
  Reaction: AMP + H2O + H(+) = IMP + NH4(+) (RHEA:14777)
  [UniProt CATALYTIC ACTIVITY, COFACTOR, SUBUNIT].
- **Process role:** the AMP→IMP step is the entry into the purine nucleotide cycle / AMP
  catabolism; it regulates the adenylate energy charge (AMP/ADP/ATP) and, by controlling
  feedback inhibition of de novo purine synthesis by adenosine-derived nucleotides,
  maintains the **guanine nucleotide (GTP) pool** — important in neurons/neural progenitors
  for GTP-dependent translation
  [PMID:23911318 abstract + full text: "we identify AMPD2 as necessary for guanine nucleotide
  biosynthesis and protein translation"; "there was also corresponding decrease in guanine
  nucleotides"].
- **Localization:** cytosolic [Reactome R-HSA-76590 "Cytosolic AMP deaminase (AMPD)";
  GOA cytosol TAS].

## Disease

- **PCH9** (pontocerebellar hypoplasia type 9, MIM:615809) — recessive, five homozygous
  null/deleterious AMPD2 mutations; guanine-nucleotide depletion / translation-initiation
  defect; cellular phenotype rescuable by purine precursor (AICAr) supplementation
  [PMID:23911318].
- **SPG63** (autosomal recessive spastic paraplegia 63, MIM:615686) [UniProt DISEASE;
  PMID:24482476, INVOLVEMENT IN SPG63].

## Annotation review reasoning

- **AMP deaminase activity (GO:0003876)** — the well-established core MF. IBA, IEA, IGI,
  NAS all present. ACCEPT (IBA as core; IGI experimental yeast-complementation from
  PMID:23911318; NAS from the AMPD2 cloning paper PMID:8764830; IEA ARBA/EC mapping fine).
- **AMP metabolic process (GO:0046033)** and **AMP catabolic process** framing — the AMP→IMP
  reaction. IBA GO:0046033 ACCEPT as core process. Ensembl IEA GO:0046033 ACCEPT.
- **IMP biosynthetic process (GO:0006188)** — IMP is the direct product of the reaction; the
  UniProt PATHWAY line frames this as "IMP biosynthesis via salvage pathway; IMP from AMP:
  step 1/1". IBA + IEA + IGI. ACCEPT.
- **IMP salvage (GO:0032264)** / **purine ribonucleotide salvage (GO:0106380)** /
  **purine ribonucleoside monophosphate biosynthetic process (GO:0009168)** — IEA process
  terms consistent with UniProt UniPathway framing of AMP→IMP as part of IMP salvage.
  Reasonable, KEEP (accept, broader/context terms).
- **energy homeostasis (GO:0097009)** — AMPD sets the adenylate energy charge; abstract
  "essential for cellular energy homeostasis". IEA + IGI. ACCEPT (non-core / higher-level).
- **ATP metabolic process (GO:0046034)** / **GTP metabolic process (GO:0046039)** — Ensembl
  IEA (from mouse Q9DBT5). AMPD2 loss raises ATP and depletes GTP in PMID:23911318, so these
  are biologically supported downstream/indirect effects. KEEP_AS_NON_CORE (regulatory/
  indirect, not the direct catalyzed reaction).
- **cyclic purine nucleotide metabolic process (GO:0052652)** — IMP from PMID:23911318.
  The paper concerns purine (IMP/GTP) metabolism, not cyclic nucleotides (cAMP/cGMP)
  specifically; the term is a poor fit for the assay. Experimental IMP so do not REMOVE;
  MARK_AS_OVER_ANNOTATED (term mis-fit; better captured by AMP/IMP metabolic terms).
- **GMP salvage (GO:0032263)** — IDA, MGI, PMID:29079593. That paper is about **erythrocyte
  AMPD (AMPD3)** and the purine salvage pathway in stored RBC; it does not establish AMPD2
  in GMP salvage, and mechanistically AMPD produces IMP (not GMP). acts_upstream_of_or_within
  qualifier. Experimental (do not REMOVE per policy); MARK_AS_OVER_ANNOTATED.
- **deaminase activity (GO:0019239)** — InterPro IEA, broad parent of AMP deaminase activity.
  MARK_AS_OVER_ANNOTATED / MODIFY to the specific GO:0003876 (too general).
- **protein binding (GO:0005515)** — six IPI entries (TERF1, CCNDBP1 x2, HIRIP3 x3) from
  large-scale interactome/screen studies. Uninformative bare "protein binding"; no functional
  module established. MARK_AS_OVER_ANNOTATED (per policy, not REMOVE).
</content>
