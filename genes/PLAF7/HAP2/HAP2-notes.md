# HAP2 (PfHAP2 / PfGCS1, PF3D7_1014200, UniProt Q8IJQ3) notes

**Automated deep research was unavailable for this gene** (Falcon authentication failed and the
OpenAI key was invalid). These notes are a manual literature review: the UniProt record, the
GOA file, and primary papers fetched into `publications/` and read directly. No
`-deep-research-*.md` file was created.

## Identity

- UniProt Q8IJQ3 (TrEMBL, unreviewed), "Male gamete fusion factor HAP2, putative", 889 aa,
  chromosome 10, ORF PF3D7_1014200. The UniProt entry carries no gene symbol, so the review keeps
  `gene_symbol: Q8IJQ3`; the folder uses the community name HAP2.
- HAP2/GCS1 family (InterPro IPR040326; PANTHER PTHR31764 "PROTEIN HAPLESS 2", subfamily SF0).
- Topology (UniProt features): signal peptide, large ectodomain, single helical transmembrane
  segment at 682-700, cytoplasmic tail 701-889 that is largely disordered and basic. A crystal
  structure of domain 3 (residues 500-620; PDB 9YC3) shows disulfides 515-525 and 548-594.
- Plasmodium has two HAP2/GCS1 genes: PfHAP2 (this gene) and the paralog PfHAP2p
  (PF3D7_0816300) [PMID:36241929 "This revealed two distinct HAP2/GCS1-encoding genes in all Plasmodium species, PfHAP2 (PlasmoDB ID PF3D7_1014200) and PfHAP2p (paralog of HAP2, PlasmoDB ID PF3D7_0816300)"].
  Care is needed not to conflate the two in annotation.

## Family-level biology

- HAP2 is the ancestral eukaryotic gamete fusogen and a class II fusion protein homologous to
  viral fusogens [PMID:28235200 "These results demonstrate that HAP2 is the gamete fusogen and suggest a mechanism of action akin to viral fusion"].
- In Chlamydomonas and P. berghei, hap2 mutant gametes still attach but cannot merge membranes
  [PMID:18367645 "Membrane dye experiments show that HAP2 is essential for membrane merger."];
  [PMID:18367645 "HAP2 disruption in Plasmodium blocked fertilization and thereby mosquito transmission of malaria."].
- P. berghei GCS1 knockout gives male sterility [PMID:18403203 "PbGCS1 knockout parasites show male sterility, resulting in unsuccessful fertilization."].

## P. falciparum-specific evidence

Kumar et al. 2022 (PMID:36241929) is the key primary paper on this gene.

- Expression/localization: male-specific; internal in stage V male gametocytes, then throughout
  the flagellum of the microgamete [PMID:36241929 "This revealed that PfHAP2 was expressed internally in male stage V gametocytes while in the microgametes, it was expressed throughout the flagellum (Fig. 2A)."];
  not seen in females [PMID:36241929 "PfHAP2 expression was not detected in female stage V gametocytes (Fig. 2B)."].
- Knockout: no asexual or gametocyte or exflagellation defect, but no zygotes and no oocysts
  [PMID:36241929 "These results indicate that both PfHAP2 and PfHAP2p are individually essential for zygote formation."].
- Genetic crosses: male-restricted function [PMID:36241929 "These results show that Pfhap2¯ males are sterile but females are fertile."].
- Fusogenic activity: expressed in BHK cells, PfHAP2 drives cell-cell fusion to a level similar
  to Arabidopsis HAP2, and fusion needs the protein in both cells in that heterologous system
  [PMID:36241929 "We found that both PfHAP2 and PfHAP2p induced cytoplasmic content mixing (i.e., cell fusion) to similar levels as the AtHAP2 (Fig. 5A–C)."];
  [PMID:36241929 "The proteins must be present in both fusing cells."].
  The authors propose a female-side partner may make fusion unidirectional in vivo; unresolved.
- Transmission-blocking target: anti-cd (fusion) loop antibodies against PfHAP2 reduced
  P. falciparum transmission in field membrane feeds [PMID:29212032 "A corresponding reduction in
  P. falciparum transmission (75.5%/36.4% reductions in intensity/prevalence) is
  observed in complimentary field studies."] (note: line break in cached text; quote in YAML uses
  a single-line substring). Recombinant PfHAP2 elicits IgG with strong SMFA activity
  [PMID:24042109 "all three IgGs showed 97 to
  100% inhibition in oocyst intensity compared to control IgG"].
- Surface exposure: HAP2 is accessible to antibodies on non-permeabilized male gametes (shown in
  P. berghei) [PMID:29212032 "Staining was absent in assays with HAP2-KO parasite lines, indicating the ability of these antibodies to recognize natively folded HAP2 on the gamete surface (Figures 2A and 2B)."].
- Structure: domain 3 crystal structure with nanobodies [PMID:41498187 "The crystal structure of one nanobody in complex with domain 3 of PfHAP2 provides the first structural insights into this transmission-blocking target in P. falciparum."].

## Annotation thinking

- GO:0005886 plasma membrane (IEA, SubCell): correct; the fusogen acts on the microgamete
  plasma membrane. ACCEPT.
- GO:0005783 endoplasmic reticulum (IBA, PTN000788722; donors Arabidopsis HAP2 F4JP36 with IDA
  ER, and T. brucei Q389Q2 with HTP/IDA ER): plausible as a pre-activation/biosynthetic pool (PfHAP2
  is "expressed internally" in gametocytes before activation), but not where the protein acts. No
  Plasmodium ER data. KEEP_AS_NON_CORE.
- Missing: no MF and no BP at all in GOA. Proposed NEW:
  - GO:0140522 fusogenic activity (IDA, PMID:36241929, BHK cell fusion). Participation test is
    trivially passed: HAP2 itself merges the bilayers.
  - GO:0007342 fusion of sperm to egg plasma membrane involved in single fertilization (IMP,
    PMID:36241929). Comparator check (QuickGO): P. berghei HAP2 Q4YCF6     carries GO:0007342 (IMP, PMID:21209845, PMID:29212032) and GO:0009566 fertilization (IMP, same
    papers), and Chlamydomonas HAP2 A4GRC6 carries GO:0007342 (IMP, PMID:25655701). So both the
    unicellular comparators in the same role carry the fertilization terms; the absence on PfHAP2
    is a curation gap for an unreviewed TrEMBL entry, not a convention.
  - Caveat: GO:0007342 is a child of GO:0022412 "cellular process involved in reproduction in
    multicellular organism", which is a poor taxonomic fit for a protist even though GO curators
    have used it for Chlamydomonas and P. berghei HAP2. For this review I propose the
    taxon-neutral GO:0009566 fertilization (also used for P. berghei HAP2) and raise the
    GO:0007342 taxon mismatch as a question for experts rather than asserting it here.
  - GO:0000755 cytogamy (fusion of the cytoplasm of two mating cells of a single-celled organism)
    was considered as the taxon-appropriate cell-fusion term. It sits under GO:0000747 conjugation
    with cellular fusion, which describes mating-type conjugation rather than anisogamous
    gamete fusion, so it is not a good fit and I did not propose it.
- Protist-specific checks performed: no plant/animal-only terms are present in GOA (both existing
  rows are generic compartments); no apicoplast, rhoptry, microneme, parasitophorous vacuole or
  digestive vacuole terms are involved; no host-vs-symbiont process terms (HAP2 acts on the
  parasite's own gametes inside the mosquito midgut, not on host cells); the one paralog risk
  (PfHAP2p, PF3D7_0816300) was checked and the evidence cited is explicitly PfHAP2-specific.
