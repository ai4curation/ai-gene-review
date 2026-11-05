# PP_4575 (Q88E91) curation notes

Reached from KBase gene-annotate dashboard protein
[NZ_MINF01000031.1_4082](https://gene-annotate-dashboard.kbase.us/review/NZ_MINF01000031.1_4082)
(P. putida, tier A). The query is 94.1% identical over 305/305 residues to KT2440 PP_4575 (final
mapping run `20261030T210853Z-final-putida-mapping`; 94.4% over 304 aligned pairs by local alignment
in `PP_4575-bioinformatics/homology_results.json`). The exact-match UniParc entries were deleted ("Not
part of a reference proteome"), so the review is filed on reference-proteome entry Q88E91, with the
dashboard ID as an alias.

## Conclusion

PP_4575 is **PxpC**, the C subunit of the three-subunit ATP-dependent prokaryotic 5-oxoprolinase
PxpABC (Niehaus et al. 2017, PMID:28830929). It works with PP_4576 (PxpB) and PP_4577 (PxpA2), and
the complex converts 5-oxo-L-proline (L-pyroglutamate) to L-glutamate. It is not an allophanate
hydrolase or a urea amidolyase. Those names come from domain homology (Pfam CT_A_B, SMART AHS2).

- **Homology** (BERIL run `20261030T215247Z-pp4575-homology`):
  - PP_4575 vs B. subtilis PxpC/KipA (Q7WY77): 35.6% identity.
  - PP_4575 vs E. coli PxpC/YbgK (P75745): 38.7% identity. Both alignments cover about 90% of each
    sequence.
  - PP_4576 vs PxpB: 37.5% (B. subtilis) and 44.6% (E. coli).
  - PP_4577 vs PxpA: 46.5% (B. subtilis) and 39.1% (E. coli).
  - KT2440 has a second set, PP_2920 (PxpA1), PP_2921 (PxpB-like, 313 aa) and PP_2922 (PxpC-like),
    which is 35.0% identical to PP_4575.
- **Locus.** The genes run PP_4575 (PxpC), PP_4576 (PxpB), PP_4577 (PxpA2), PP_4578 (MFS transporter)
  and PP_4579 (divergent LysR regulator), all on the minus strand except PP_4579. PxpC-B-A
  co-localize in the four other Pseudomonas genomes the dashboard showed.
- **KT2440 fitness** (BERDL `kescience.fitnessbrowser`, run `20261030T214253Z-pp4575-pp4572-fitness`):
  - **Pyroglutamate.** On L-pyroglutamate as nitrogen source, PP_4575 fitness is -4.19 (t -6.4) and
    -3.78 (t -6.1). These are its only strong phenotypes apart from milder ones on L-lysine and
    L-glutamate as carbon source (about -1.2 to -1.5).
  - **Neighbours.** PP_4576, PP_4577, PP_4578 and PP_4579 all have specific pyroglutamate phenotypes
    (fitness -2.7 to -3.8). They are PP_4575's top cofitness hits: 0.81, 0.75, 0.65 and 0.58.
    The transporter PP_4578 and regulator PP_4579 sharing the phenotype suggests they are a
    pyroglutamate uptake/induction unit. That is an inference.
  - **Urea.** On urea as nitrogen source PP_4575 shows no phenotype (-0.11, -0.17). KT2440 encodes
    urease (PP_2842-PP_2849) and has no urea carboxylase.
  - **Paralogous cluster.** PP_2922 (PxpC-like) has strong phenotypes on **butyrolactam**
    (2-pyrrolidone) as nitrogen source (-5.06, -3.80) and only a weak one on pyroglutamate (-0.65,
    -0.40). PP_4575 has none on butyrolactam (-0.04, -0.09). The two Pxp systems therefore look
    substrate-specialized, not redundant.
  - **Eukaryote-type OPase homologs.** The "5-oxoprolinase A/B" genes PP_3514/PP_3515 are needed on
    valerolactam, not pyroglutamate.
- **Allophanate hydrolase vs 5-oxoprolinase.**
  - PxpB/PxpC are homologous to the "allophanate hydrolase subunit 1/2" domains.
  - Allophanate hydrolase activity has been shown only for a fused PxpBC homolog that clusters with
    urea carboxylase (as stated in PMID:28830929).
  - The fused PxpBC TTHA0988 was "incorrectly annotated as an allophanate hydrolase" (PMID:21245531).
  - PP_4575 has no biotin carboxylase or biotin-carrier domain.
  - The context (pxpA neighbour, pyroglutamate phenotype, no urea phenotype, no urea carboxylase in
    KT2440) all points to 5-oxoprolinase.

## Dashboard verdict

**Recommended verdict: supported.**

Corrected annotation: "5-oxoprolinase subunit C (PxpC) of the PxpABC ATP-dependent 5-oxoprolinase
(with PP_4576 PxpB and PP_4577 PxpA2); required for L-pyroglutamate utilization as nitrogen source in
KT2440; not an allophanate hydrolase/urea amidolyase."

| GO term | Assessment |
|---|---|
| GO:0017168 5-oxoprolinase (ATP-hydrolyzing) activity | **COR** (2). Novel, since GOA for Q88E91 is empty. The precise gene-level qualifier is contributes_to. |
| GO:0005524 ATP binding | **UNC** (1). Taken from "ATP-dependent". No ATP site is assigned to PxpC; the PxpB/C phosphorylation role is assumed (PMID:42212642). |
| GO:0097054 L-glutamate biosynthetic process | **COR** (2). It is the closest GO process, since GO has no 5-oxoproline catabolic process term. Physiologically the role is damage-metabolite salvage and nitrogen scavenging. |

The annotator's reasoning was accurate: it used PANTHER, the 94%-identity KT2440 pyroglutamate fitness
and pxpA2 neighbourhood/STRING, and it rejected the allophanate hydrolase and urea carboxylase labels.
It did not see Niehaus et al., and the PaperBLAST panel offered only urea/allophanate snippets.

## Caveats

- No P. putida Pxp protein has been purified or assayed. A classical P. putida three-component OPase
  (Seddon/Meister, 1980s) was never cloned. Niehaus et al. argue that it is the PxpABC enzyme.
- The fitness data are transposon-insertion phenotypes. Polar effects within the operon cannot be
  excluded for PP_4575 alone, though PxpB and PxpA give the same phenotype independently.
- The subunit roles (which subunit binds ATP, which opens the ring) are not experimentally assigned.

## Tooling

- **`just fetch-gene`** failed on its first try with an EBI OLS read timeout. A retry a few minutes
  later succeeded.
- **`just fetch-fitness`** failed (no local FEBA data; the Fitness Browser returns 403). The fitness
  data were read from the BERDL lakehouse through the MCP REST query endpoint, using a curl
  User-Agent and limit 1000 (`PP_4575-bioinformatics/fb_fitness.py`).
  - Without an ORDER BY, offset pagination over joins returned duplicated and missing rows. In the
    first run PP_2922 was dropped entirely.
  - The script now orders every paginated query and records the number of unique experiments per
    locus (300 each).
- **`fetch-gene-pmids`** found no PMIDs, because GOA is empty. Papers were fetched manually.
- **Deep research** used the `claude-code` provider.
