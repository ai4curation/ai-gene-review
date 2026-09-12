# LOXL1 review notes

## Evidence blockers and provenance

- Automated Falcon deep research timed out. The Perplexity fallback failed with HTTP
  401. Per project policy, no `LOXL1-deep-research-{provider}.md` file was created; this
  manual journal records the fallback review.
- PMID:37602378 is a decisive citation blocker for the seeded IDA extracellular-region
  annotation: the verified record is a HELZ2 exoribonuclease paper and contains no LOXL1
  result [PMID:37602378 "Database searches identified a new RNB domain-containing protein in human: HELZ2."].
  This is flagged as `WRONG_IDENTIFIER` at reference level. Because extracellular
  localization is independently correct but the provenance of this experimental row
  cannot be reconstructed, its action is `UNDECIDED` under curator-deference rather than
  removal. The cause of the citation mismatch is unknown.
- Direct catalytic evidence is species-bounded. The strongest LOXL1-specific in vivo
  evidence is mouse, and the direct purified-enzyme activity evidence is bovine. The
  current human UniProt function statement is explicitly by similarity to mouse. Do not
  present the human protein-lysine 6-oxidase assignment as if a purified human LOXL1
  catalytic assay were available in this cache.
- Human LOXL1 processing is experimentally mapped, but processing is not equivalent to a
  direct activity assay. The 2022 human study mapped BMP1 and ADAMTS14 cleavage, while
  noting that the older bovine cleavage-site assignments disagree. The safest conclusion
  is that human LOXL1 is secreted and proteolytically diversified, not that every observed
  processed species is catalytically activated.
- Three HDA ECM citations (PMID:27068509, PMID:28327460, PMID:28675934) do not name LOXL1
  in the cached narrative text. Their annotation support may reside in supplements or
  deposited proteomics tables. Treat them as `UNVERIFIED`, not false.

## Identity and molecular boundaries

LOXL1 (Q08397) is the short-subfamily paralog most closely related to canonical LOX, not
an alternate name for LOX/P28300 and not one of the SRCR-domain LOXL2/3/4 proteins. The
original human cDNA paper established homology only to the carboxyl end of lysyl oxidase
[PMID:7689553 "A novel human cDNA with a predicted protein homologous to the carboxyl end of lysyl oxidase, an extracellular enzyme involved in the maturation of collagen and elastin, has been isolated."].

The reviewed human record defines a signal peptide (residues 1-25), propeptide (26-95),
and mature chain (96-574), but newer proteomics demonstrates a more complex processing
landscape. In human cellular models, BMP1 cleavage was mapped to 151-152, whereas
ADAMTS14 sites were mapped to 216-217, 292-293, and 375-376
[PMID:35328709 "The analysis resulted in one single processing site at 151–152 (RH/GG) for BMP1 and three distinct cleavage sites for ADAMTS14 at positions 216–217 (GA/AA), 292–293 (PD/PG), and 375–376 (PD/PN)"].
Therefore, avoid treating a single N-terminal fragment as a uniquely defined LOXL1
propeptide with an independently established function, and avoid transferring canonical
LOX's Gly168-Asp169 processing scheme to LOXL1.

## Prioritized functional synthesis

1. **Elastic-fiber homeostasis and elastin cross-linking are the best-supported core.**
   Loxl1-null mice fail to deposit normal postpartum uterine elastic fibers and show lung,
   skin, and vascular abnormalities with tropoelastin accumulation
   [PMID:14745449 "Here we show that mice lacking the protein lysyl oxidase-like 1 (LOXL1) do not deposit normal elastic fibers in the uterine tract post partum and develop pelvic organ prolapse, enlarged airspaces of the lung, loose skin and vascular abnormalities with concomitant tropoelastin accumulation."].
   The same abstract distinguishes LOXL1 from LOX and assigns spatially targeted elastin
   deposition to LOXL1 [PMID:14745449 "Distinct from the prototypic lysyl oxidase (LOX), LOXL1 localizes specifically to sites of elastogenesis and interacts with fibulin-5."].
   This supports elastic-fiber assembly/homeostasis more strongly than a broad claim that
   LOXL1 is a general collagen-fibril organizer.

2. **LOXL1 is targeted to an elastogenic scaffold through fibulin-5.** Human recombinant
   binding experiments detected LOXL1-fibulin-5 interaction and localized the major
   binding contribution to the fibulin-5 C-terminal domain
   [PMID:17371835 "As shown in Fig. 7 B, we detected the specific interaction of LOXL1, 2, and 4 proteins with fibulin-5 protein (top, lanes 1, 7, and 13)."].
   The interaction is mechanistically informative but not unique to LOXL1, because LOXL2
   and LOXL4 also bound, and it does not establish one stable macromolecular complex.
   Fibulin-4 binding is also reported [PMID:27339457 "We show that fibulin-4 binds stronger than fibulin-3 and -5 to LTBP1s, 3, and 4s, and to the lysyl oxidases LOX and LOXL1"],
   but that paper is centered on fibulin-4 variants and should be treated as supporting,
   not defining, evidence.

3. **The mature catalytic chain is extracellular and generated through regulated
   proteolysis.** Human Tenon's-capsule fibroblasts and engineered human LOXL1 expression
   models produced multiple extracellular LOXL1 species
   [PMID:35328709 "The presence of this complex array of LOXL1 species in the extracellular medium suggests that LOXL1 protein is the subject of specific post-translational modifications, likely including proteolysis by endogenous proteases."].
   Direct activation evidence comes from bovine LOXL1: the purified precursor was largely
   inactive and BMP1 processing yielded activity on elastin and collagen
   [PMID:11684696 "The immunopurified protein was largely inactive, but further processing in vitro by bone morphogenetic protein-1 led to an enzyme that was active on elastin and collagen substrates."].
   This supports a conserved processing-to-activity model with an explicit bovine-to-human
   inference boundary.

4. **Human tissue evidence supports extracellular-matrix/elastic-tissue deployment, not
   direct catalytic specificity.** LOXL1 was detected in an extracellular-space-enriched
   guanidine fraction from human aorta [PMID:20551380 "Lysyl oxidase homolog 1bLOXL1_HUMAN6312127.323"].
   In human ocular tissues, LOXL1 RNA was present broadly except in retina, and protein was
   detected in relevant tissues [PMID:18037624 "LOXL1 was found to be expressed by reverse transcription-polymerase chain reaction in all ocular tissues examined except retina. The presence of LOXL1 protein in ocular tissues of interest was demonstrated by western blotting."].
   These localization data are compatible with an extracellular elastogenic role, but the
   ocular paper is a disease-association study and does not assay catalysis.

## Annotation-facing cautions

- Favor the specific molecular function `protein-lysine 6-oxidase activity` over the broad
  parent oxidoreductase term, while documenting that human assignment is substantially
  orthology-supported.
- Elastic-fiber assembly/homeostasis is the strongest biological-process axis. Collagen
  oxidation is biochemically plausible and directly demonstrated for processed bovine
  LOXL1, but human LOXL1-specific collagen-fibril organization evidence is weaker than the
  elastin evidence.
- Copper binding and the lysine-tyrosylquinone cofactor are conserved-family catalytic
  requirements in the reviewed UniProt record; they are not independently established by
  the LOXL1 primary papers reviewed here.
- Acrosomal-vesicle, basement-membrane, aorta-development, LPS-response, and generic
  collagen-fibril annotations are largely electronic transfers from rodent orthologs and
  should not be promoted into the core without LOXL1-specific corroboration.
- Reactome R-HSA-2002466, R-HSA-2022141, and R-HSA-2395340 explicitly describe canonical
  LOX. R-HSA-2129375 supplies general lysyl-oxidase/elastin pathway context but is not
  independent LOXL1-specific evidence.

## Manual source audit

Primary records were checked against PubMed/PMC and then fetched through `just fetch-pmid`
so that all YAML supporting text could be validated against repository-local sources.
New decisive caches are PMID:14745449, PMID:35328709, PMID:17371835, PMID:11684696, and
PMID:18037624. No finding was imported from an LLM-generated research summary.
