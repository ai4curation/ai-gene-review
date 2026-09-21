# PP_0312 (Q88R22) curation notes — PSEPK second ETF alpha subunit

## Identity

- UniProt Q88R22, locus PP_0312, 410 aa, *Pseudomonas putida* KT2440
  (NCBITaxon:160488).
- SubName only: "Electron transfer flavoprotein, alpha subunit"
  [file:PSEPK/PP_0312/PP_0312-uniprot.txt] — no RecName, no FUNCTION line, no
  COFACTOR line. This is a thinly annotated protein.
- Family: ["Belongs to the ETF alpha-subunit/FixB family."] Domain support:
  Pfam PF00766 (ETF_alpha) + PF01012 (ETF), InterPro IPR001308 (ETF_a/FixB),
  IPR014731 (ETF_asu_C), IPR029035 (DHS-like NAD/FAD-binding domain).
- PANTHER PTHR43153 / PTHR43153:SF1, the same family as etfA/PP_4201
  [file:projects/P_PUTIDA/data/psepk_gene_list.tsv:307].
- The first review round confirmed that PP_0312 retains the ETF-alpha
  FAD-binding motifs, with an exact GISGAIQH match to the etfA BINDING 258-265
  region.

## The donor is not unknown — genomic context

The first draft of this review described the physiological donor as
unestablished. That understates what the repo's own project data already show.
`projects/P_PUTIDA/data/psepk_gene_list.tsv:305-306`:

- `dgcA` / PP_0310 (Q88R24) — "Dimethylglycine dehydrogenase subunit (EC 1.5.8.-)"
- `dgcB` / PP_0311 (Q88R23) — "Dimethylglycine dehydrogenase subunit (EC 1.5.8.-)"

EC 1.5.8.- is *oxidoreductase acting on the CH-NH group of donors, with a flavin
as acceptor* — that is, ETF-dependent by definition of the sub-subclass. These
two genes sit immediately upstream of PP_0312-PP_0313 in the same locus.

`projects/P_PUTIDA/data/psepk_pathway_buckets.tsv:6` independently groups all
four in KEGG ppu00260 (glycine, serine and threonine metabolism) alongside the
glycine-betaine and sarcosine oxidation genes:
`thrB;dgcA;dgcB;PP_0312;PP_0313;gbcA;gbcB;ltaE;soxB;soxD;soxA;soxG`.

So the locus points at methylated-glycine oxidation (betaine → dimethylglycine →
sarcosine → glycine) as the donor pathway for this ETF pair. Recorded as a
likely donor, not asserted as established: no experiment has paired
dgcAB with PP_0312/PP_0313.

## Curation decisions and why

### GO:0009055 electron transfer activity, `enables` — ACCEPT (was MARK_AS_OVER_ANNOTATED)

Same reasoning as for etfA/etfB: GO types obligate subunits of a multi-protein
carrier with the complex's activity and records the dependency as
`contributes_to_molecular_function`, which this review does. See
`genes/human/ETFA` and `genes/human/ETFB`, both of which ACCEPT the term.

### GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase — MARK_AS_OVER_ANNOTATED, reason strengthened

The genomic context does not merely fail to support this term; it argues against
it. The donor encoded next to this pair is a dimethylglycine dehydrogenase, and
KEGG places the operon in amino-acid metabolism, not fatty-acid degradation.
KT2440's fatty-acid beta-oxidation electrons are instead expected to reach the
quinone pool through the etfA-etfB-PP_4203 locus. The TreeGrafter term is a
family-level default that conflicts with the local evidence.

### GO:0050660 flavin adenine dinucleotide binding — ACCEPT

Direct predicted cofactor property, supported by the conserved ETF-alpha domain
architecture and the retained FAD-binding motifs.

## Open questions

- Does the dgcAB dimethylglycine dehydrogenase actually use the
  PP_0312/PP_0313 ETF pair as its electron acceptor? An in vitro reconstitution
  would settle both this review's donor question and dgcAB's own annotation.
- Which quinone-reducing partner reoxidises this second ETF pair — PP_4203, or
  a distinct ETF-QO? KT2440 encodes only one obvious ETF-QO, which would make
  PP_4203 the shared terminus for both pairs.
