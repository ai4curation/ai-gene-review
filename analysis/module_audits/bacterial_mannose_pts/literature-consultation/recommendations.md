# Mannose-PTS literature and taxon consultation

The supported reusable mechanism is a matched, mannose-active EIIA/EIIB relay coupled to EIIC/EIID group translocation. Its input is phospho-HPr plus extracellular mannose and its output is intracellular mannose phosphate. EI/HPr supply, later metabolism, global transcriptional regulation, bacteriophage entry and bacteriocin receptor functions are neighboring biology. The machinery can also accept other sugars, but that spectrum must be attached to the measured species/system rather than inferred from the family name.

Three full reviews were manually read in the relevant sections: PMID17158705 (2006 MMBR), PMID16339738 (2005 MMBR, a PubMed-indexed review with substantial comparative analysis), and PMID18647176 (2008 FEMS). Their access and findings are recorded in `evidence-ledger.yaml`. The normal caches for the first and third remain abstract-only; actual full-text acquisitions and checked excerpts are recorded separately. PMID16006479 is original comparative phylogenetic research, not a fourth review. The 2020 review PMID32710850 was accessible only as an abstract; the attempted Elsevier full text returned403. The 2019 chapter PMID31214989 yielded a subscription preview, not full text. Neither is represented as fully read. The module's genuine Falcon403 attempt is preserved in the parent audit's `provider-attempt.json`; this consultation is manual literature work, not a fabricated provider report.

## Architecture and assay boundaries

- Model the four functional roles, allowing fused IIAB and split IIA/IIB realizations. The supported E. coli relay includes intra- and intersubunit transfer (PMIDs2681202/8262947). A fused chain does not make phosphorylation strictly intramolecular.
- The 2019 structure is a trimer of ManYZ pairs (PMID31209249). The older soluble ManX dimer experiments concern a different subsystem. Neither establishes a fixed whole-ManXYZ stoichiometry. Its counterflow experiment does not independently demonstrate a complete PEP/HPr/ManX transport cycle.
- Require positive mannose-specific and compatible-partner evidence in addition to family classification. Bacillus subtilis LevDEFG is the important negative control: primary2117666 explicitly excludes mannose uptake while establishing fructose PTS function. The broader wording in the 2006 review cannot override that primary.
- IID is a supported membrane partner, not merely an optional historical annotation. An isolated relay, isolated C/D receptor pair, generic PTS member, alternate-cargo system or cross-species mixture is not a complete supported mannose circuit.
- Bacteriocin susceptibility measures a distinct interaction. C/D can provide this property without IIAB; this does not show complete sugar group translocation. Receptor-rescue figures must not be relabeled as uptake reconstitution.
- Alternative uptake can mask a native deletion phenotype. Complete module capacity and sole-route physiological necessity are different claims.

## Positive exact panels

`identity-proof.json` checks current official UniProt taxon, locus, EMBL protein/genome cross-reference and PANTHER classification for six proteins. It reports the actual sequence lengths and hashes. No experimental construct is claimed to have been independently sequenced.

| Source strain | Paper names | Official protein accessions | Scope |
|---|---|---|---|
| Lactococcus lactis IL1403 | ptnAB / ptnC / ptnD | Q9CEX8 / Q9CEX7 / Q9CEX6 | Primary17284603 names these genes and genomeAE005176; native deletion reduces mannose/glucose growth. Primary38047704 gives native C/D variant growth phenotypes, with substrate controls and exceptions. |
| Streptococcus mutans UA159 | manL / manM / manN | Q8DSC4 / Q8DSC3 / Q8DSC2 | Official lociSMU_1877/1878/1879, respectively. Current UniProt calls them ptnA/ptnC/unnamed; these are aliases of the paper's manLMN region, not a different cassette. |

For UA159, primary12902269 Fig1 shows the manLMN operon between SMU.1876 and comA/SMU.1882c, and gives a0.99kb manL. Independent primary17951382 explicitly equates manL and manM with SMU.1877 and SMU.1878. Official genome/protein cross-references provide the adjacent third locus. The figure image and full-text acquisition are in the ignored cache; `acquisition.json` and `source-sha256.json` preserve their provenance. The source supports ManL participation through PEP-dependent uptake measurements, yet the mutant grows faster on mannose and an alternative mannose-inducible route is implicated. Do not describe this system as the only native mannose uptake route. Primary24928869 extends amino-sugar scope and ManO modulation without establishing ManO as universally required.

Both panels have IIAB PTHR33799:SF1, IIC PTHR32502:SF25, and IID PTHR32502:SF27. These are official memberships, not substrate grants or interchangeable-interface guarantees. E. coli uses different C/D subfamilies; root/family consultation owns those selectors.

## Split comparator and unresolved identities

The full primary9004509 explicitly studies Lactobacillus curvatus CECT904. The official sequence deposit U28163 has separate complete manA, manB and manC, followed by a partial manD (87 amino acids). The four archived UniProt cross-references Q48519/Q48520/Q48521/Q48522 now return inactive/deleted records. This supports a split architecture and a bounded experimental comparator, but not a fabricated complete active quartet.

The official CECT catalogue identifies CECT904 with ATCC25601, DSM20019 and JCM1096. That catalogue establishes strain synonyms, not sequence identity. A current UniProt species query returned a WDN19 reference proteome (UP000825100; official proteome metadata confirms WDN19), which is not the assayed type strain; it was explicitly rejected as a substitute. Full IID sequence and an exact active-record bridge remain unresolved. There is no reason to import WDN19's fused relay as if it were the split CECT904 system.

Primary40135874 supplies a native MGAS8232 whole-operon versus ManL-only complementation comparison for mannose utilization. It is useful comparative evidence with explicit additional-mutation and native-context caveats; this consultation did not establish exact protein accessions, so no representative IDs are proposed. Host colonization and antimicrobial phenotypes are downstream context. The newer Enterococcus lactis primary41432198 was discovered and normally cached, but only its abstract was available here; it is not a reviewed exact transport panel.

## Validation limits and preservation

`build_evidence.py` verifies14 short exact excerpts against the texts actually read, six official current identity bridges, the four archived split components, and all31 protected original source hashes. This is a reproducibility and provenance check, not a substitute for scientific review or independent assay replication. No gene, module, family, provider output or original publication cache was edited. New publication caches were obtained through the normal fetch command. Existing E. coli structural-source acquisitions belong to the released Ecoli consultation and are referenced read-only.
