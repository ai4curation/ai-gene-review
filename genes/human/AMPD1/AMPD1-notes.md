# AMPD1 review notes

Gene: AMPD1 (AMP deaminase 1, muscle isoform "M" / myoadenylate deaminase)
UniProt: P23109 (human), 747 aa, EC 3.5.4.6
HGNC:468; taxon NCBITaxon:9606

Falcon deep research was OUT OF CREDITS (HTTP 402) at review time; no
`-deep-research-falcon.md` was generated. Review grounded in
`AMPD1-uniprot.txt`, the seeded GOA (`AMPD1-goa.tsv`), and cached
`publications/PMID_*.md` + `reactome/R-HSA-76590.md`.

## Core biology (verified)

- Catalyses hydrolytic deamination of AMP -> IMP + NH4+ (ammonia).
  UniProt CATALYTIC ACTIVITY: "AMP + H2O + H(+) = IMP + NH4(+)" RHEA:14777,
  EC=3.5.4.6, ECO:0000269|PubMed:11102975.
- Zinc metalloenzyme (metallo-dependent hydrolase superfamily; adenosine and
  AMP deaminase family). Binds 1 Zn(2+) per subunit (COFACTOR note; catalytic
  Zn-binding residues H303, H305, H572, D649 in FT BINDING). Homotetramer.
- Muscle isoform (AltName "AMP deaminase isoform M"; "Myoadenylate deaminase").
  HPA: group-enriched in skeletal muscle and tongue. Cytosolic (Reactome
  R-HSA-76590 places AMPD in cytosol; classically associated with the
  myofibrillar/contractile apparatus in skeletal muscle).
- Committed step of the purine nucleotide cycle in skeletal muscle:
  AMP --(AMPD1)--> IMP; IMP --(ADSS1)--> adenylosuccinate;
  adenylosuccinate --(ADSL)--> AMP + fumarate. The cycle regenerates AMP,
  buffers the adenylate energy charge during intense exercise, releases
  fumarate (TCA anaplerosis) and ammonia. UniProt FUNCTION: "AMP deaminase
  plays a critical role in energy metabolism."
- UniProt PATHWAY: "Purine metabolism; IMP biosynthesis via salvage pathway;
  IMP from AMP: step 1/1" == UniPathway UPA00591 (== GO:0032264 IMP salvage).

## Disease

- Myopathy due to myoadenylate deaminase deficiency (MMDD) [MIM:615511] /
  AMP deaminase deficiency: one of the most common inherited muscle enzyme
  defects. Often benign/asymptomatic; can cause exercise-induced myalgia,
  cramps, early fatigue. First described as a distinct muscle disease by
  Fishbein et al. 1978 (PMID:644316). First AMPD1 missense mutations causing
  detectable deficiency (R388W, R425H) shown to abolish AMPD activity in a
  Japanese myopathy patient (PMID:11102975).

## Annotation-by-annotation reasoning

MF:
- GO:0003876 AMP deaminase activity — core MF. Supported experimentally
  (IMP PMID:11102975: R388W/R425H abolish AMPD activity; TAS PMID:644316;
  ISS from rat P10759; IBA; IEA). All ACCEPT (multiple redundant evidence
  lines are fine).
- GO:0019239 deaminase activity (IEA, InterPro) — parent of GO:0003876; too
  general -> MODIFY to GO:0003876.
- GO:0005515 protein binding (IPI x2, PMID:32296183/HuRI) — uninformative bare
  term; interactions are AMPD1-AMPD2 and AMPD1-AMPD3 (IntAct). Do NOT REMOVE
  (experimental IPI); MARK_AS_OVER_ANNOTATED per curation policy.
- GO:0042802 identical protein binding (IPI, PMID:32296183; with/from P23109
  self) — corresponds to the real homotetramer (UniProt SUBUNIT). ACCEPT.

BP:
- GO:0046033 AMP metabolic process (IBA) — accurate, core substrate metabolism.
  ACCEPT.
- GO:0032264 IMP salvage (IEA, UniPathway UPA00591) — matches UniProt PATHWAY
  "IMP from AMP: step 1/1". ACCEPT (core; the direct product-forming process).
- GO:0006188 IMP biosynthetic process (IBA) — IMP is the product; reasonable,
  though "salvage" (GO:0032264) is more precise. KEEP_AS_NON_CORE (accurate
  but a de-novo-flavoured parent-ish framing; the salvage term is the precise
  one). ACCEPT-level correctness but not the most precise; keep.
- GO:0009168 purine ribonucleoside monophosphate biosynthetic process (IEA,
  InterPro) — generic biosynthetic framing; the reaction is better described
  as AMP catabolism / IMP salvage. Keep as broadly correct IEA
  (KEEP_AS_NON_CORE).
- GO:0006753 nucleoside phosphate metabolic process (IEA, ARBA) — very general
  parent; correct but uninformative. KEEP_AS_NON_CORE.
- GO:0032263 GMP salvage (IDA, PMID:29079593, assigned by MGI) — PMID:29079593
  is a red-blood-cell storage metabolomics study centred on the erythrocyte
  purine salvage/deamination pathway (AMPD3 context). AMP deaminase produces
  IMP + NH3 from AMP; it does not act on guanine nucleotides, so "GMP salvage"
  is not the direct biochemistry of this enzyme. Experimental IDA -> do NOT
  REMOVE per policy; MARK_AS_OVER_ANNOTATED (pathway-level co-annotation, not
  AMPD1's direct function). Two rows (acts_upstream_of_or_within + involved_in)
  both from same PMID.

CC:
- GO:0005829 cytosol (TAS, Reactome R-HSA-76590) — correct; AMPD is cytosolic.
  ACCEPT.

## core_functions (author-supplied, strictly validated)
- MF GO:0003876 AMP deaminase activity
- directly_involved_in GO:0032264 IMP salvage (AMP -> IMP, step 1/1; == UniProt
  PATHWAY / UPA00591) and GO:0046033 AMP metabolic process
- located_in GO:0005829 cytosol
