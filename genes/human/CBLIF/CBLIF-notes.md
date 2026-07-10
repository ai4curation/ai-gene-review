# CBLIF (Gastric intrinsic factor / GIF) — review notes

UniProtKB:P27352 (IF_HUMAN). HGNC:4268. Synonyms: GIF, IFMH. NCBITaxon:9606.

## Summary of function

CBLIF is the secreted **cobalamin (vitamin B12)-binding glycoprotein** produced by
gastric parietal cells (and, at anatomical margins, some chief/enteroendocrine cells).
Its core function is to **bind dietary cobalamin** in the small intestine and to **mediate
its receptor-dependent absorption in the distal ileum**. The IF–cobalamin complex is taken
up by the ileal **cubam receptor** (cubilin/CUBN + amnionless/AMN) via receptor-mediated
endocytosis; the complex is delivered to lysosomes where Cbl is released. CBLIF is NOT an
enzyme. Loss of function causes **hereditary intrinsic factor deficiency (IFD, MIM:261000)**,
a form of juvenile/congenital pernicious anemia presenting as megaloblastic anemia from B12
malabsorption.

## Key provenance

- FUNCTION: [file:human/CBLIF/CBLIF-uniprot.txt "Promotes absorption of the essential vitamin cobalamin (Cbl) in the ileum. After interaction with CUBN, the CBLIF-cobalamin complex is internalized via receptor-mediated endocytosis."]
- SUBUNIT: [file:human/CBLIF/CBLIF-uniprot.txt "Interacts with CUBN (via CUB domains)."]
- SUBCELLULAR LOCATION: Secreted [file:human/CBLIF/CBLIF-uniprot.txt "SUBCELLULAR LOCATION: Secreted."]
- TISSUE SPECIFICITY: Gastric mucosa [file:human/CBLIF/CBLIF-uniprot.txt "TISSUE SPECIFICITY: Gastric mucosa."]
- DISEASE IFD: megaloblastic anemia [file:human/CBLIF/CBLIF-uniprot.txt "Autosomal recessive disorder characterized by megaloblastic anemia."]
- SIMILARITY: eukaryotic cobalamin transport proteins family (with TCN1 haptocorrin / TCN2 transcobalamin).
- Cbl-binding residues (BINDING features): 171, 222, 270, 365-370, 386-395; C-terminal beta-domain essential for retention.

## Literature

- **PMID:17954916** (Mathews et al. 2007, PNAS) — crystal structure of human IF:Cbl at 2.6 Å; alpha6/alpha6 barrel two-domain protein; Cbl bound base-on at domain interface. Basis of Reactome's EXP `cargo receptor ligand activity` and `cobalamin binding` calls. [PMID:17954916 "The structure of intrinsic factor (IF) in complex with cobalamin (Cbl) was determined at 2.6-A resolution."] and [PMID:17954916 "the Cbl is bound at the interface of the domains in a base-on conformation"]. Also describes the CUB(N) receptor recognition: [PMID:17954916 "CUB recognizes both the full-length Cbl-saturated IF complex and the Cbl-saturated cleaved IF complex but not the isolated α- or β-domains, even if they are saturated with Cbl"].

- **PMID:20237569** (Andersen et al. 2010, Nature) — crystal structure of IF:Cbl bound to cubilin CUB(5-8); defines how the cubam receptor recognizes the IF-Cbl complex. Source of the CUBN IPI (IntAct O60494). Abstract-only in cache. Abstract: [PMID:20237569 "This occurs by the combined action of the gastric intrinsic factor (IF) and the ileal endocytic cubam receptor formed by the 460-kilodalton (kDa) protein cubilin and the 45-kDa transmembrane protein amnionless."] and [PMID:20237569 "how two distant CUB domains embrace the Cbl molecule by binding the two IF domains in a Ca(2+)-dependent manner"].

- **PMID:15738392** (Tanner et al. 2005, PNAS) — biallelic GIF mutations (nonsense/missense) cause hereditary IF deficiency; distinct from Imerslund-Grasbeck (CUBN/AMN). IMP evidence for role in cobalamin transport/absorption. [PMID:15738392 "The gastric IF (GIF) gene located in this region harbored homozygous nonsense and missense mutations in these four families and in three additional families. The disease in these cases therefore should be classified as hereditary IF deficiency."]

- **PMID:14695536** (Gordon et al. 2004, Hum Mutat) — Gln5→Arg (mature Q23R) coding polymorphism associated with congenital IF deficiency; recombinant IF expressed/secreted from COS-7 with native size, secretion rate, pepsin sensitivity. Supports secreted localization and Cbl binding of the expressed protein. [PMID:14695536 "The apparent size, secretion rate, and sensitivity to pepsin hydrolysis of the expressed IF were similar to native IF."]

- **PMID:8886952** (Howard et al. 1996, J Anat) — immuno-localization of human IF; parietal cells are the main source but expression is not restricted to them. Immunoelectron microscopy: highest antigen density on endocytic and apical membranes of parietal cells; also secretory granules. IDA support for endosome / microvillus / apical plasma membrane localization in the producing cell. [PMID:8886952 "Immunoelectron microscopy demonstrated the highest antigen density on endocytic and apical membranes of parietal cells."]

- **PMID:32296183** (Luck et al. 2020, Nature) — HuRI high-throughput binary (Y2H) interactome. Source of several IPI `protein binding` calls (FFAR2, SLC13A4, SLC22A23, SLC7A1, SLC7A14, TMEM237). These are large-scale screen hits with no established biological role for a secreted Cbl-binding protein; treat as uninformative `protein binding` over-annotations, not true partners.

## Curation decisions (high level)

- MF cobalamin binding (GO:0031419): CORE. Multiple lines (IDA/IBA/IEA, crystal structures). ACCEPT.
- BP cobalamin transport (GO:0015889): CORE. IMP (disease), IBA, TAS(Reactome), IEA. ACCEPT.
- CC extracellular region (GO:0005576): CORE (secreted). ACCEPT IBA/IDA; IEA/TAS ACCEPT.
- MF cargo receptor ligand activity (GO:0140355) EXP/Reactome: the IF-Cbl complex is the ligand recognized by the cubam cargo receptor — biologically apt; ACCEPT (this is essentially the receptor-recognition facet of its transport role).
- CC endosome / microvillus / apical plasma membrane (IDA, PMID:8886952): localizations in the producing parietal cell / uptake compartments; not the core secreted function but real. KEEP_AS_NON_CORE.
- CC lysosomal lumen (TAS Reactome): the IF-Cbl complex is delivered to lysosomes in the enterocyte for degradation/Cbl release; real trafficking endpoint, non-core. KEEP_AS_NON_CORE.
- MF protein binding (GO:0005515) IPI: CUBN (PMID:20237569) is the real, functionally central partner but the bare `protein binding` term is uninformative → MARK_AS_OVER_ANNOTATED (per policy, not REMOVE). HuRI hits (PMID:32296183) → MARK_AS_OVER_ANNOTATED (uninformative screen hits).
</content>
