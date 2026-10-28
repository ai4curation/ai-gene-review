# gsto-1 (C29E4.7, UniProt P34345) - manual literature review

No deep-research API was available in this session; this file records a manual
literature survey (PubMed search `(gsto-1 OR GSTO-1 OR C29E4.7) AND elegans`, six hits,
plus the GOA-cited papers). Provenance is given inline.

## Identity and family

- gsto-1 (ORF C29E4.7, WBGene00016204) encodes a 250-aa Omega-class cytosolic
  glutathione transferase. UniProt: "Belongs to the GST superfamily. Omega family."
  [file:worm/gsto-1/gsto-1-uniprot.txt]. InterPro IPR005442 (GST_omega), PANTHER
  PTHR43968:SF6.
- Omega GSTs were defined as a class in mammals and C. elegans by Board et al.
  [PMID:10783391 "Glutathione S-transferases (GSTs) of the new class, named Omega, exist
  in several mammalian species and Caenorhabditis elegans"]. Human GSTO1-1 "exhibits
  glutathione-dependent thiol transferase and dehydroascorbate reductase activities
  characteristic of the glutaredoxins" and has an active-site cysteine that can form a
  disulfide with glutathione [PMID:10783391].
- The predicted catalytic nucleophile is Cys33 (UniProt ACT_SITE, by similarity to
  human P78417).

## Biochemistry (Burmeister et al. 2008, FASEB J; abstract only cached)

- Recombinant GSTO-1 "had minimal catalytic activity toward classic GST substrates but
  displayed significant thiol oxidoreductase and dehydroascorbate reductase activity"
  [PMID:17901115].
- UniProt transcribes kinetics from this paper: KM 184.1 uM for dehydroascorbate, Vmax
  186 nmol/min/mg; KM 70.77 uM for 2-hydroxyethyl disulfide (thioltransferase assay),
  Vmax 192; KM 51.52 uM and Vmax 106 for CDNB; Vmax 32 nmol/min/mg towards cumene
  hydroperoxide [file:worm/gsto-1/gsto-1-uniprot.txt]. So DHA reduction and
  thioltransferase are the dominant activities; CDNB conjugation and peroxidase-like
  activity are measurable but low.
- Methylarsonate (MMA(V)) reductase: UniProt's CATALYTIC ACTIVITY block for EC 1.20.4.2
  cites ECO:0000269 PubMed:17901115, but its FUNCTION text says MMA reduction is "(By
  similarity)" and no MMA kinetics are listed. The abstract does not mention MMA. This
  is unresolved without the full text.
- C33A mutation: "Increased sensitivity to oxidative stress when exposed to cumene
  hydroperoxide" (UniProt MUTAGEN, from PMID:17901115; probably the E. coli disc assay).

## Expression

- Intestine-specific: "localized the protein exclusively in the intestine of all
  postembryonic stages of C. elegans" [PMID:17901115]. Expression depends on a GATA
  site and ELT-2 [PMID:17901115], and is stress-inducible.
- Hypoxia induces gsto-1 via TORC1/ELT-2 in the intestine [PMID:25284791 "Of particular
  interest was the identification of GSTO-1, an intestinal omega-class glutathione
  S-transferase (GST), whose induction under hypoxia was abrogated by ELT-2 RNAi"].
- Transcriptional induction is also reported by drug/probiotic studies (PMID:41414713,
  PMID:39825644); these are expression-only and not used for annotation.

## In vivo phenotypes

- Overexpression: increased resistance to juglone, paraquat and cumene hydroperoxide
  [PMID:17901115].
- RNAi: "increased sensitivity to several prooxidants, arsenite, and heat shock"
  [PMID:17901115].
- Luersen et al. 2013 RNAi screen of 67 GSH-metabolism genes: gsto-1 RNAi gave a
  moderate juglone sensitivity ("juglone survival rate 16.4±1.7, p<0.01") [PMID:23593298];
  in the same Table 2, gsto-1 RNAi arsenite survival was 86.5±9.0 versus 90.0±5.8 for the
  control vector, i.e. no arsenite effect under those conditions, in contrast with
  PMID:17901115. Juglone "generate[s] superoxide anion from molecular oxygen during
  metabolism" [PMID:23593298].
- GSTO-1 is required for lifespan extension after transient hypoxia [PMID:25284791
  "uncover that GSTO-1 is required for lifespan under hypoxia"] and "loss of GSTO-1
  increases the sensitivity of C. elegans to mitochondrial ROS generating agents, such
  as paraquat (PQ)" [PMID:25284791].

## Synthesis

GSTO-1 is an intestinal, cytoplasmic Omega-class GST whose best-supported catalytic
activities are glutathione-dependent dehydroascorbate reduction and thiol-disulfide
(thioltransferase/glutaredoxin-like) chemistry, with weak conventional GST conjugating
activity. In vivo it is a stress-inducible antioxidant enzyme required for full
tolerance of redox-cycling pro-oxidants and for hypoxia-induced longevity. Its role in
arsenic metabolism (MMA(V) reduction, arsenite tolerance) is inferred mainly from the
human ortholog and from conflicting RNAi data.
