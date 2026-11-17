# tlr1902 cellulose comparative audit notes

## Shared source and scope audit (2026-11-05)

Applied annotation-reviewer and core-function-synthesizer guidance. The normal `fetch-gene` command seeded these reviews before curation. Symbol-only attempts failed with UniProt HTTP 429/timeouts; the normal retry used the independently resolved `--uniprot-id`. Pristine documents, every original non-review annotation field and raw SHA256 hashes are saved in `.cache/module-audit-logs/cellulose-20261105/cyanobacteria-baseline.json`. Raw files have not been refreshed after successful seeding.

Default Falcon was attempted through the standard gene recipe for each target and failed with HTTP 403 authentication error. Genuine logs are in `.cache/module-audit-logs/cellulose-20261105/`. These are manual notes; no provider report was fabricated.

The 2011 primary paper is PMID:21498404, DOI:10.1093/pcp/pcr047. A normal fetch supplies an abstract-only publication cache. The publisher abstract and indexed primary-paper text were examined; direct HTML/PDF downloads returned 403. The paper explicitly deposits Tvtll0007 as AB571479, encoding BAJ61012.1, which is the current E5RST0 protein. [PMID:21498404, "three candidate genes for cellulose synthase (Tvtll0007, Tvtlr1795 and Tvtlr1930-33) were cloned from T. vulcanus."]

The 2018 primary paper is PMID:29688612, DOI:10.1111/mmi.13977. The full publisher article was readable at https://onlinelibrary.wiley.com/doi/full/10.1111/mmi.13977 via web browsing, although the normal publication fetch remains abstract-only and direct publisher HTML/PDF and supplement retrieval returned 403. Quotes in review support blocks therefore use the genuinely cached abstract or independent source records; uncached full-text findings below are paraphrased with the publisher URL. No full text was manually manufactured in the publications cache.

The 2018 authors explicitly identify RKN as NIES-2134 and use BP-1 locus names for RKN orthologs (Figure 4 caption). Their native perturbations concern RKN. The one purified recombinant enzyme described is diguanylate cyclase Tlr1210 (cloned from T. elongatus genomic DNA), not XcsB, XcsC or TolC. They establish native necessity and overexpression phenotypes for the cellulose-associated genes and propose an XcsA-XcsB-TolC arrangement from architecture and homology models. Direct assembly and cellulose passage through TolC are not established; XcsC's GH10 endoglucanase chemistry is explicitly a proposal. Neither the term HlyD-like nor a knockout phenotype establishes a particular exported substrate. [PMID:29688612, "we propose that the cyanobacterial extracellular cellulose production is due to a novel variant of the bacterial tripartite secretion system."]

Exact strain distinction is consequential: the indexed 2011 discussion reports deficient induced cellulose/aggregation in BP-1 and an A654T synthase difference relative to RKN, while leaving causality unresolved versus other signaling/regulatory differences. This is not a loss-of-function conclusion about the accessory proteins. BP-1 homologs are comparative references, not demonstrated positive copies of the native RKN machinery.

Identity search: UniProt RKN query resolved E5RST0/Tvtll0007, E5RST1/Tvtlr1795 and E5RST2/Tvtlr1930-33 under Thermostichus vulcanus RKN, taxon1048443. Queries under the historical name Thermosynechococcus vulcanus missed these because the genus is now Thermostichus. The NIES-2134 genome is AP018202.2, now Thermostichus vulcanus NIES-2134, taxon2005468 (NCBI and KEGG tvn); current UniProt queries for that exact taxon returned no proteome entries. A different strain, Rupite, has A0ABT0 accessions that must not be substituted. No exact RKN XcsB/XcsC UniProt identity or cloned sequence was verified, so the BP-1 reference proteins are explicitly retained as homologs rather than silently renamed as RKN.

Primary identity endpoints: https://rest.uniprot.org/uniprotkb/E5RST0; https://rest.uniprot.org/uniprotkb/Q8DKF6; https://rest.uniprot.org/uniprotkb/Q8DHP3; https://www.ncbi.nlm.nih.gov/nuccore/AP018202; https://www.kegg.jp/kegg-bin/show_organism?org=tvn. The 2011 primary accession declaration is indexed at https://academic.oup.com/pcp/article-pdf/52/6/957/17910502/pcr047.pdf.

No matching accession was found in gocams/index.tsv. No generic binding, biofilm, stress-response or cell-aggregation BP was newly proposed. No PANTHER identifier was invented or a plausible family label substituted for its official name.

## Target assessment

Q8DHP3 maps to genomic BA000039/BAC09454.1, locus tlr1902, 385 aa, BP-1 (NIES-2133/IAM M-273), taxon197221. It is not the RKN XcsC perturbation target. The GH10 domain and curated ProRule/RuleBase classification support glycoside-hydrolase class membership. The historical label cellulase F is a family name, not an assay of cellulose hydrolysis.

UniRule UR000414746 version6 was retrieved from https://rest.uniprot.org/unirule/UR000414746.json and stored verbatim as UR000414746-source.json. Its conditions are a PS51760 profile in bacteria/fungi; an active-site feature group triggers EC3.2.1.8 and GO xylan-specific MF/BP. This establishes how the annotations arose, not that target substrate specificity has been measured.

The four seeded rows are reviewed: broad O-glycoside hydrolase and carbohydrate metabolism ACCEPT; xylanase activity and xylan catabolism UNDECIDED. The RKN endoglucanase proposal does not justify REMOVING the competing xylan predictions or substituting a cellulase term. No NEW cellulose-related process or export activity is added, and core_functions stays empty pending specific chemistry/native-role resolution.
