# NDUFAF4 (Q9P032) — review notes

## Identity
- HGNC symbol NDUFAF4 (HGNC:21034); UniProt Q9P032 (NDUF4_HUMAN); 175 aa, ~20.3 kDa.
- Former names: C6orf66, HRPAP20 ("Hormone-regulated proliferation-associated protein of 20 kDa"), HRG-9-like; ORFNames HSPC125, My013.
- RecName: "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex assembly factor 4" — an *assembly factor*, NOT a structural subunit of complex I and no catalytic activity [file:human/NDUFAF4/NDUFAF4-uniprot.txt "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex assembly factor 4"].

## Core function: mitochondrial complex I assembly factor
- UniProt FUNCTION: "Involved in the assembly of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I)" [file:human/NDUFAF4/NDUFAF4-uniprot.txt "Involved in the assembly of mitochondrial NADH:ubiquinone"], cited to PubMed:18179882 and PubMed:28853723.
- Original identification as a complex I assembly factor: homozygosity mapping in a consanguineous family with infantile mitochondrial encephalomyopathy and isolated complex I deficiency identified a missense mutation in a conserved residue of C6ORF66; patient muscle showed markedly reduced C6ORF66 protein and reduced fully assembled complex I; transfection with WT cDNA restored complex I activity [PMID:18179882 "Transfection of the patients' fibroblasts with wild-type C6ORF66 cDNA restored complex I activity. These data suggest that C6ORF66 is an assembly factor of complex I"].
- Localization: mitochondrion / mitochondrial membrane (inner-membrane arm intermediate) [file:human/NDUFAF4/NDUFAF4-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion"].
- Membrane / lipid-anchor: N-myristoylated at Gly-2 after initiator-Met cleavage (PubMed:25255805); "Membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}" in UniProt, consistent with peripheral association with the membrane arm.

## Partnership with NDUFAF3
- NDUFAF4 tightly interacts with NDUFAF3 (C3ORF60); the two act together in complex I assembly. NDUFAF3 mutations cause fatal neonatal complex I deficiency [PMID:19463981 "NDUFAF3 tightly interacts with NDUFAF4 (C6ORF66), a protein previously implicated in complex I deficiency"].
- UniProt SUBUNIT: "Binds calmodulin. Interacts with NDUFAF3." [file:human/NDUFAF4/NDUFAF4-uniprot.txt "Binds calmodulin. Interacts with NDUFAF3."].
- Reactome model (Complex I biogenesis, R-HSA-6799198): the IP (matrix/peripheral) subcomplex binds NDUFAF3, NDUFAF4, TIMMDC1 to form an early "Intermediate 1" of the membrane arm (R-HSA-6799203), which later joins the HP subcomplex, etc. NDUFAF3/NDUFAF4/TIMMDC1 are transient assembly-factor components that dissociate from the near-mature complex.
- Blue-native/LC-MS profiling co-migrated C6ORF66 (and novel C3ORF60=NDUFAF3) with complex I subunits NDUFS2/3/7/8, implicating it in complex I biogenesis [PMID:19688755 "the recently implicated chaperone C6ORF66 and a novel candidate, C3ORF60"].
- Interaction proteomics of CI assembly factors (TIMMDC1/MCIA network) place NDUFAF4 in the MCIA-associated CI assembly machinery [PMID:24344204 "TIMMDC1 ... reciprocally associated with multiple members of the MCIA CI assembly factor complex and core CI subunits"].

## Disease
- Mitochondrial complex I deficiency, nuclear type 15 (MC1DN15; MIM:618237), autosomal recessive; phenotypes include Leigh syndrome, leukodystrophy, encephalopathy, cardiomyopathy [file:human/NDUFAF4/NDUFAF4-uniprot.txt "Mitochondrial complex I deficiency, nuclear type 15 (MC1DN15)"].
- Variants: L65P (PubMed:18179882), A3P (Leigh syndrome, causes a specific CI assembly defect; PubMed:28853723 — abstract not cached, but UniProt records "results in altered complex I assembly").

## Molecular function
- No catalytic (oxidoreductase/dehydrogenase) activity — it is an assembly factor, not a subunit of the NADH:ubiquinone oxidoreductase. Do NOT assign NADH-dehydrogenase MF terms.
- Honest MF-level role = binding: interacts with NDUFAF3 and with complex I subunits/intermediates during assembly; also binds calmodulin (UniProt KW-0112 Calmodulin-binding, from PubMed:17001319). There is no verified specific catalytic MF; core function is best framed around the assembly BP (GO:0032981) with binding as the mechanistic activity.

## Other / non-core activities
- Earlier "HRPAP20" literature (PubMed:14871833, PubMed:17001319 — abstracts not cached) reported hormone-regulated expression, phosphoprotein, calmodulin binding, and promotion of breast-cancer cell proliferation/invasion. UniProt keeps these as "May be involved in cell proliferation and survival ... May be a regulator of breast tumor cell invasion" — non-core, weakly supported.
- Defense response to virus (GO:0051607, IMP, PubMed:33635491): NDUFAF4 binds the VSV matrix (M) protein; overexpression inhibited and knockdown promoted VSV propagation, independent of type I IFN [PMID:33635491 "Overexpression of Ndufaf4 inhibited VSV propagation, and knockdown of Ndufaf4 by short hairpin RNA (shRNA) markedly promoted VSV replication"]. Single low-throughput study; a moonlighting/non-core process, kept as non-core.

## Annotation review summary
- ACCEPT: mitochondrial CI assembly BP (GO:0032981) IMP (PMID:18179882) and IBA; mitochondrion IDA (PMID:18179882); mitochondrial membrane IDA (PMID:19463981); mitochondrion IBA/IEA/IDA(HPA). NDUFAF3-binding IPI (PMID:19463981) is functionally meaningful but term is bare "protein binding".
- KEEP_AS_NON_CORE: defense response to virus IMP (GO:0051607, PMID:33635491).
- MARK_AS_OVER_ANNOTATED: bare GO:0005515 "protein binding" IPI from high-throughput interactome/proteomics screens (uninformative term; policy = never REMOVE IPI protein binding).
- REMOVE: GO:0016020 "membrane" IEA (GO_REF:0000044) — over-general SubCell mapping; the informative CC is mitochondrial (inner) membrane. (IEA electronic, allowed to REMOVE.)
- ACCEPT / KEEP: mitochondrial inner membrane TAS Reactome (GO:0005743) and InterPro IEA GO:0032981 — correct.
