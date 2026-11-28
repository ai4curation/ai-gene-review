# mvpB (P54659, Major vault protein beta) notes

## Literature search (2026-11-07)

Deep-research providers have no API keys in this environment, so no `-deep-research-*.md` file was generated.
`just mod-description-deep-research DICDI mvpB` was run and skipped ("no MOD provider configured for organism 'DICDI'").

PubMed E-utilities queries (esearch, db=pubmed):

| Query | Hits |
|---|---|
| `vault AND Dictyostelium` | 42014721, 37779900, 16689703, 15157468, 8774142, 7622465, 7828886, 8270627, 8340365, 1691193, 1694556 |
| `major vault protein AND Dictyostelium` | 15157468, 8774142, 7622465, 7828886, 8340365, 1691193 |
| `mvpA OR mvpB AND Dictyostelium` | 7622465, 7828886, 8340365 |
| `vault particle AND discoideum` | 42014721, 8774142, 7622465, 7828886, 8340365, 1691193 |

Relevant and cached: PMID:8340365, PMID:7622465, PMID:1691193, PMID:8270627, PMID:42014721 (full text),
PMID:15157468 (review), PMID:16926386, PMID:19482547, PMID:16512674 (proteomics). Not relevant: PMID:37779900
(Vwa1/Vwa2 VIT-vWFA proteins, not MVPs), PMID:16689703 (RNA motif search tool), PMID:8774142 and PMID:7828886
(human/rat MVP). PMID:8270627 is abstract-only; the abstract does not state the species. A web search found no
full text, so it could not be checked whether Dictyostelium nuclei were assayed.

## Key findings

- Dictyostelium vaults contain two major proteins, MvpA (94 kDa) and MvpB (92 kDa), 60% identical
  [PMID:8340365 "Dictyostelium vaults contain two major proteins, MVP alpha (94.2 kDa) and MVP beta (approximately 92 kDa)"];
  [PMID:7622465 "MvpB shares 60% identity with MvpA at the amino acid level"].
- mvpA disruption: MvpB still made, but no characteristic vault particles
  [PMID:8340365 "Although the cells still produce MVP beta, they do not contain characteristic vault particles, suggesting that MVP alpha is required for normal vault structure"].
- Single and double mutants are viable; they grow poorly under nutritional stress, reaching one third of the
  wild-type stationary density in suspension; ovoid remnants persist; the double mutant's remnants copurify with MvpC
  [PMID:7622465 "loss of MvpA and/or MvpB interferes with vault function sufficiently to impede growth under conditions of nutritional stress"].
- In situ cryo-ET (2026): Dictyostelium vaults resemble metazoan vaults; 1.4% (14/999) associate with ER and
  nuclear envelope membranes; about 8% of cytosolic vaults and 4/14 membrane-bound vaults enclose 80S ribosomes
  in defined orientations. MvpA-TurboID labels untagged MvpB in the shell, suggesting at least partly
  heterooligomeric vaults, and enriches PARP orthologues and TEP1 [PMID:42014721].
- Vaults occur in Dictyostelium and the anti-rat-vault antibody recognises its major vault protein [PMID:1691193].

## Decisions

- Nucleus rows: KEEP_AS_NON_CORE (same reasoning as mvpA and human MVP). The mvpB IDA (PMID:8270627) also seeds PTN000366423.
- NEW nuclear envelope and endoplasmic reticulum from cryo-ET (PMID:42014721), non-core. Cryo-ET identifies vaults by shape; MvpB is in the shell (TurboID biotinylation).
- Signal transduction IBA, phagocytic vesicle HDA x2, extracellular matrix HDA (slime-sheath proteomics, which also picked up ribosomal and nuclear proteins): MARK_AS_OVER_ANNOTATED.
- Core MF: structural molecule activity (NEW). MvpB is biotinylated by MvpA-TurboID within the shell, so it co-assembles with MvpA. mvpB-null cells keep only ovoid vault remnants (PMID:7622465). The abstract does not separate mvpB-single from mvpA-single phenotypes beyond "mvp- single mutant lines".
- There is no process annotation for the growth defect under nutritional stress (necessity evidence, indirect).
