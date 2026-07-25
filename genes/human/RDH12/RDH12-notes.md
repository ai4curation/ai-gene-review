# RDH12 (Retinol dehydrogenase 12) — review notes

UniProt: Q96NR8 (RDH12_HUMAN). Gene: RDH12 (synonym SDR7C2). Human, 316 aa.
Source of truth used here: `genes/human/RDH12/RDH12-uniprot.txt`, `genes/human/RDH12/RDH12-goa.tsv`,
cached publications, and cached Reactome entries.

## Summary of biology

RDH12 is a member of the short-chain dehydrogenase/reductase (SDR) superfamily
(SDR family 7C member 2). It is a **microsomal (endoplasmic reticulum membrane)
retinoid dehydrogenase/reductase** expressed most notably in the retina, where the
protein localizes to **photoreceptor inner segments**.

- Enzymology: strong preference for **NADP(H)** over NAD(H); reduces
  9-cis-, 11-cis- and all-trans-retinaldehyde to the corresponding retinols, and
  (with lower affinity) reduces medium-chain lipid-peroxidation aldehydes such as
  4-hydroxynonenal (4-HNE) and trans-2-nonenal. EC 1.1.1.300.
- Physiological direction: in cells the enzyme "primarily contributes to the
  reduction of all-trans-retinaldehyde" (i.e. retinaldehyde -> retinol), and in
  photoreceptors under oxidative stress it also detoxifies lipid-peroxidation
  aldehydes.
- Disease: biallelic RDH12 variants cause **Leber congenital amaurosis 13 (LCA13)**
  and **autosomal-recessive retinitis pigmentosa 53 (RP53)**; most pathogenic
  missense variants cause profound loss of catalytic activity.

## Key provenance (verbatim quotes)

### Enzymatic function / substrate specificity

- [file:human/RDH12/RDH12-uniprot.txt "Retinoids dehydrogenase/reductase with a clear preference for"] and the
  continuation "NADP. Displays high activity towards 9-cis, 11-cis and all-trans-" retinal
  (UniProt FUNCTION comment; lines wrapped with `CC` prefix so not a single grep-able span).
- [file:human/RDH12/RDH12-uniprot.txt "EC=1.1.1.300"] with the catalytic-activity Rhea reaction
  "all-trans-retinol + NADP(+) = all-trans-retinal + NADPH".
- [PMID:12226107 "Members of the short chain alcohol \ndehydrogenase/reductase superfamily catalyze the transformation of retinol to \nretinal"] — establishes RDH12 as an SDR retinol dehydrogenase.
- [PMID:12226107 "three enzymes \nfrom a novel subfamily of four retinol dehydrogenases (RDH11-14) that display \ndual-substrate specificity, uniquely metabolizing all-trans- and cis-retinols \nwith C(15) pro-R specificity"] — dual (all-trans/cis) substrate specificity; source of the IDA MF annotations.
- [PMID:15865448 "RDH12 exhibits approximately 2000-fold lower K(m) values for NADP(+) \nand NADPH than for NAD(+) and NADH and recognizes both retinoids and lipid \nperoxidation products (C(9) aldehydes) as substrates"] — NADP(H) preference (basis for treating the NAD+ term as over-annotation).
- [PMID:15865448 "The enzyme exhibits the highest catalytic \nefficiency for all-trans-retinal"] — all-trans-retinal is the best substrate.
- [PMID:15865448 "in \nmost tissues, RDH12 primarily contributes to the reduction of \nall-trans-retinaldehyde"] — physiological reductive direction (retinaldehyde -> retinol).

### Aldehyde detoxification (BP: cellular detoxification of aldehyde)

- [PMID:19686838 "We conclude that in \nmouse retina RDH12 reduces 4-HNE to a nontoxic alcohol, protecting cellular \nmacromolecules against oxidative modification and protecting photoreceptors from \nlight-induced apoptosis"] — IDA support for GO:0110095.
- [PMID:19686838 "we found that light-induced production of 4-HNE co-localized with RDH11 and RDH12 in mouse photoreceptors"] — inner-segment localization of activity.
- [PMID:15865448 "at saturating concentrations of peroxidic \naldehydes in the cells undergoing oxidative stress, for example, photoreceptors, \nRDH12 might also play a role in detoxification of lipid peroxidation products"].

### Localization

- [file:human/RDH12/RDH12-uniprot.txt "Endoplasmic reticulum membrane"] (SUBCELLULAR LOCATION, ECO:0000269|PubMed:15865448) — EXP support for GO:0005789.
- [PMID:19686838 "a microsomal retinoid dehydrogenase/reductase (RDH) located in photoreceptor inner segments"] — photoreceptor inner segment localization (mouse ortholog basis for the ISS/IEA human annotations).

### Visual cycle role (indirect/auxiliary)

- [PMID:19686838 "As both RDH11 and RDH12 are located in photoreceptor inner segments, and their loss-of-function in knockout mice does not limit chromophore synthesis, their contribution to visual cycle activity per se is likely to be indirect"] — RDH12's role in vision is auxiliary; supports KEEP_AS_NON_CORE for "visual perception".
- [PMID:12226107 "photoreceptor RDH12 could \nbe involved in the production of 11-cis-retinal from 11-cis-retinol during \nregeneration of the cone visual pigments"] — proposed (not proven) visual-cycle role.

### Disease

- [file:human/RDH12/RDH12-uniprot.txt "Leber congenital amaurosis 13 (LCA13)"] and
  [file:human/RDH12/RDH12-uniprot.txt "Retinitis pigmentosa 53 (RP53)"] — DISEASE comments (ECO:0000269 experimental variant references).
- Reactome R-HSA-2466861 "Defective RDH12 does not reduce atRAL to atROL" links loss-of-function variants (Y226C, H151N, A126V etc.) to LCA13/RP53.

## Protein-binding (IPI) annotations

Four GO:0005515 "protein binding" IPI annotations come from high-throughput
interactome/degradation studies with no RDH12-specific functional interpretation:
- PMID:20006610 (RDH12 disease-variant degradation; with UBC / ubiquitin, EBI IntAct)
- PMID:25416956 (proteome-scale interactome map; with RBPMS)
- PMID:25910212 (interaction perturbations in genetic disorders; with RBPMS-3)
- PMID:32296183 (HuRI reference binary interactome; with PLEKHA7)
These are uninformative for the molecular function (bare "protein binding") and are
marked as over-annotations rather than removed (experimental IPI). UniProt records the
same partners (PLEKHA7, RBPMS, UBC) in its INTERACTION section.

## Curation decisions (high level)

- Core MF: **GO:0052650 all-trans-retinol dehydrogenase (NADP+) activity** and
  **GO:0102354 11-cis-retinol dehydrogenase (NADP+) activity** (EXP/IDA), plus
  **GO:0050661 NADP binding** (cofactor, from KM data / NADP-binding motif).
- Core BP: **GO:0110095 cellular detoxification of aldehyde** (IDA) and
  **GO:0042572 retinol metabolic process** / retinoid metabolism.
- Core CC: **GO:0005789 endoplasmic reticulum membrane** (EXP) and
  **GO:0001917 photoreceptor inner segment**.
- GO:0008106 "alcohol dehydrogenase (NADP+) activity" (IEA/Rhea) is a correct but
  overly general parent — MODIFY to the specific retinol-dehydrogenase terms.
- GO:0004745 "all-trans-retinol dehydrogenase (NAD+) activity" — the NAD+-dependent
  version is a laboratory-detectable but physiologically minor activity (KM for NAD(H)
  ~2000-fold higher than NADP(H)); marked as over-annotation, not core.
- "visual perception" (GO:0007601) and "photoreceptor cell maintenance" (GO:0045494)
  are retained as non-core because RDH12's contribution to the visual cycle is indirect.
</content>
