# HPRT1 (Hypoxanthine-guanine phosphoribosyltransferase, HGPRT) — review notes

UniProt: P00492 (HPRT_HUMAN); HGNC:5157; EC 2.4.2.8; 218 aa; gene on Xq26.

## Core function (well established)

HPRT1 is the cytosolic **hypoxanthine-guanine phosphoribosyltransferase** of the
purine **salvage** pathway. It transfers the 5-phosphoribosyl group from PRPP
(5-phospho-alpha-D-ribose 1-diphosphate) onto a 6-oxopurine base:
- hypoxanthine -> IMP (RHEA:17973)
- guanine -> GMP (RHEA:25424)

This recycles free purine bases into nucleotides, sparing the energetically costly
de novo pathway.

- UniProt FUNCTION: "Converts guanine to guanosine monophosphate, and hypoxanthine
  to inosine monophosphate. Transfers the 5-phosphoribosyl group from 5-
  phosphoribosylpyrophosphate onto the purine. Plays a central role in the generation
  of purine nucleotides through the purine salvage pathway."
- EC 2.4.2.8; catalytic activity confirmed experimentally
  [ECO:0000269|PubMed:10338013, ECO:0000269|PubMed:19527031].
- Two catalytic reactions (both right-to-left physiological direction):
  IMP + diphosphate = hypoxanthine + PRPP (RHEA:17973); GMP + diphosphate = guanine + PRPP (RHEA:25424).
- COFACTOR: Mg(2+); "Binds 2 magnesium ions per subunit."
- PATHWAY: "Purine metabolism; IMP biosynthesis via salvage pathway; IMP from
  hypoxanthine: step 1/1."
- SUBUNIT: **Homotetramer** [PubMed:10338013, 10360366, 15990111, 8044844].
- SUBCELLULAR LOCATION: **Cytoplasm** (cytosolic).

Kinetics (PMID:10338013): KM 5.4 uM IMP, 0.45 uM hypoxanthine, 25 uM PPi, 31 uM PRPP.

PMID:9521733 (Xu & Grubmeyer 1998): "Hypoxanthine-guanine phosphoribosyltransferase
(HGPRTase) catalyzes the reversible formation of IMP and GMP from their respective
bases hypoxanthine (Hx) and guanine (Gua) and the phosphoribosyl donor
5-phosphoribosyl-1-pyrophosphate (PRPP)." Asp137 = general acid/base; Lys165 ground-state
interactions. (Note: numbering differs from mature protein; ACT_SITE is residue 138 in
UniProt = proton acceptor.)

PMID:19527031 (Keough et al. 2009, J Med Chem): abstract foregrounds the *Plasmodium
falciparum* enzyme (antimalarial ANP inhibitors) but explicitly determined Ki values for
"the corresponding human enzyme, HGPRT" and reports "Structures of human HGPRT in complex
with three ANPs." This is a UniProt EC evidence source and validly supports human HPRT1
catalytic activity (HPX-PRT + GPRT). Do NOT remove.

## Structure

Crystal structures: with bound GMP (PMID:8044844, Cell 1994), with transition-state
analog immucillinGP + Mg2+-PPi (PMID:10360366), free apoenzyme showing conformational
plasticity (PMID:15990111), ternary complex with PRPP/Mg2+/HPP (PMID:10338013). Core
alpha/beta PRTase (type I) fold. Two Mg2+ ions sandwich the pyrophosphate.

## Disease

- **Lesch-Nyhan syndrome** (LNS, MIM:300322; MONDO:0010298): complete (<1.5% residual)
  HPRT deficiency -> hyperuricemia, choreoathetosis/dystonia, intellectual disability,
  compulsive self-injurious behavior. X-linked recessive.
  (dismech KB: Lesch-Nyhan_Syndrome.yaml; PMID:18067674, PMID:32310539)
- **HPRT-related hyperuricemia (HRH)** / Kelley-Seegmiller (MIM:300323): partial
  deficiency (1.5-8% residual) -> hyperuricemia, gout, renal stones, without the
  neurobehavioral phenotype.
- >300 disease-associated mutations reported (PMID:18067674). UniProt lists many LNS/HRH
  missense/deletion variants.
- Dopaminergic deficit in LND: PMID:8643611 — "50-63% reduction of the binding to DA
  transporters in the caudate, and a 64-75% reduction in the putamen of the LND patients."
  This is a downstream neurochemical consequence of the disorder, not a molecular
  function of HPRT1.

## Annotation review reasoning

- MF: GO:0004422 (hypoxanthine PRT activity) and GO:0052657 (guanine PRT activity) are the
  two core catalytic activities — ACCEPT (IDA + IBA + IEA all consistent; RHEA-backed).
- Mg2+ binding (GO:0000287) — ACCEPT (IDA PMID:10360366; 2 Mg2+ per subunit per UniProt).
- BP salvage terms: purine ribonucleoside salvage (GO:0006166), guanine salvage
  (GO:0006178), hypoxanthine salvage (GO:0043103), IMP salvage (GO:0032264), GMP salvage
  (GO:0032263) — all ACCEPT; these are the pathway roles.
- hypoxanthine metabolic process (GO:0046100), IMP metabolic process (GO:0046040),
  GMP catabolic process (GO:0046038) — the enzyme's physiological reactions are salvage
  (anabolic) but it is reversible; these broader metabolic-process terms are correct but
  less specific than the salvage terms; ACCEPT (metabolic-process framing) / the catabolic
  framing (GMP catabolic) reflects the reverse pyrophosphorolysis reaction assayed in
  PMID:19527031.
- purine nucleotide biosynthetic process (GO:0006164, IMP PMID:9824441) — correct broad
  parent (salvage produces IMP/GMP); KEEP but the salvage terms are more precise.
- AMP salvage (GO:0044209, IEA/Ensembl from mouse ortholog): HPRT does NOT act on adenine;
  AMP salvage is APRT's job. HPRT makes IMP (which can feed AMP synthesis downstream) but
  does not directly salvage AMP/adenine. Over-propagated electronic inference -> REMOVE.
- positive regulation of dopamine metabolic process (GO:0045964, IMP PMID:8643611): the
  cited paper measures reduced DA transporters in LND patients — a downstream disease
  phenotype, not a molecular activity of HPRT1 regulating dopamine metabolism. This is an
  over-interpretation/over-annotation of an indirect physiological consequence ->
  MARK_AS_OVER_ANNOTATED.
- CC: cytosol (GO:0005829) / cytoplasm (GO:0005737) — ACCEPT (multiple IDA/IBA/TAS/IEA).
- extracellular exosome (GO:0070062, HDA PMID:20458337): high-throughput proteomic
  detection in B-cell exosomes; a common HDA "sightings" location, not the site of
  catalytic function -> KEEP_AS_NON_CORE.
- protein binding (GO:0005515, bare IPI, many HT interactome papers): uninformative per
  curation guidelines; do not REMOVE experimental IPIs -> MARK_AS_OVER_ANNOTATED.
- identical protein binding (GO:0042802) + protein homotetramerization (GO:0051289):
  meaningful — the active enzyme is a homotetramer (structural papers). ACCEPT.
