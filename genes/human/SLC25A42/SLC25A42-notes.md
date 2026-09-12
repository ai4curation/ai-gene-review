# SLC25A42 review notes

## Identity and family
- UniProt **Q86VD7** (S2542_HUMAN), gene **SLC25A42**, HGNC:28380, 318 aa. RecName "Mitochondrial coenzyme A transporter SLC25A42" [file:human/SLC25A42/SLC25A42-uniprot.txt "RecName: Full=Mitochondrial coenzyme A transporter SLC25A42"].
- Member of the mitochondrial carrier (SLC25 / TC 2.A.29) family; three Solcar repeats and six predicted TM helices [file:human/SLC25A42/SLC25A42-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family"]. TCDB 2.A.29.12.2.
- Paralog: SLC25A16 (Graves disease carrier protein). Both are proposed human orthologs of yeast Leu5 [PMID:40925986 "proposed SLC25A16 (A16) and SLC25A42 (A42) as its human orthologs"].

## Core molecular function — CoA transporter (antiporter)
- Biochemically characterized as a mitochondrial carrier for CoA and adenosine 3',5'-diphosphate (PAP) [PMID:19429682 "SLC25A42 protein is a mitochondrial transporter for CoA and adenosine 3',5'-diphosphate"].
- Mechanism is strict counter-exchange (antiport), not uniport: [PMID:19429682 "SLC25A42 catalyzed only a counter-exchange transport, exhibited a high transport affinity for CoA, dephospho-CoA, ADP, and adenosine 3',5'-diphosphate"].
- Physiological direction: imports CoA into matrix in exchange for intramitochondrial (deoxy)adenine nucleotides and PAP [PMID:19429682 "The main physiological role of SLC25A42 is to import CoA into mitochondria in exchange for intramitochondrial (deoxy)adenine nucleotides and adenosine 3',5'-diphosphate"].
- UniProt CATALYTIC ACTIVITY entries (RHEA) list the exchange half-reactions: ADP(out)+CoA(in)=ADP(in)+CoA(out) (RHEA:72839); 3'-dephospho-CoA/ADP (RHEA:72843); PAP/ADP (RHEA:72847); AMP/ADP (RHEA:72851); dADP/ADP (RHEA:72855); ADP/ATP (RHEA:34999) [file:human/SLC25A42/SLC25A42-uniprot.txt "Reaction=ADP(out) + CoA(in) = ADP(in) + CoA(out)"].
- Km values (proteoliposomes): 71 uM CoA, 64 uM dephospho-CoA, 55 uM ADP, 50 uM PAP [file:human/SLC25A42/SLC25A42-uniprot.txt "KM=71 uM for CoA"].
- Best MF term: **GO:0015228 coenzyme A transmembrane transporter activity** (IDA PMID:19429682; IMP PMID:40925986). The antiport mechanism (GO:0015297) and specific nucleotide-transporter terms (ADP/ATP/AMP transmembrane transporter, ATP:ADP antiporter) are all supported by the same in-vitro exchange data.

## Physiological validation (2025)
- Liu et al. show that in human cells A16 and A42 are together required to establish the mitochondrial CoA pool: [PMID:40925986 "SLC25A16 and SLC25A42 are critical for mitochondrial import of free CoASH"].
- The mitochondrial CoA pool supports matrix CoA-dependent catabolism: [PMID:40925986 "This CoASH import process supports an enriched mitochondrial CoA pool and CoA-dependent pathways in the matrix, including the high-flux TCA cycle and fatty acid oxidation"].
- Direct import assay: [PMID:40925986 "M+4-labelled free CoASH was imported into A42WT-expressing mitochondria at a significantly higher level than into A42 KO mitochondria"].
- A42 single KO already causes a proliferation defect; A16/A42 DKO is most severe (synthetic sick) [PMID:40925986 "A42 single KO cells already exhibited a significant proliferation defect, and A16/A42 double KO (DKO) cells showed the most severe growth defect"].

## Localization
- Mitochondrial inner membrane, multi-pass [file:human/SLC25A42/SLC25A42-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane"]. IDA is_active_in GO:0005743 from PMID:19429682 (reconstitution + targeting).
- Bulk mitochondrion IDA from HPA (GO_REF:0000052) and HTP mito proteome (PMID:34800366) are consistent but less specific than the inner-membrane call.
- **Nucleus GO:0005634 (HDA, PMID:21630459)**: from a human sperm-nucleus proteome catalogue (403 proteins). This is a high-throughput proteomic co-purification, not evidence of a nuclear function for a polytopic inner-membrane CoA carrier; treat as over-annotation / likely contamination (sperm mitochondrial sheath). Keep evidence but MARK_AS_OVER_ANNOTATED.

## Disease
- Recessive MECREN (Metabolic crises, recurrent, with variable encephalomyopathic features and neurologic regression; MIM:618416); recurrent homozygous N291D variant [file:human/SLC25A42/SLC25A42-uniprot.txt "Metabolic crises, recurrent, with variable encephalomyopathic features"].
- N291D is loss-of-function for CoA transport, no effect on abundance [file:human/SLC25A42/SLC25A42-uniprot.txt "loss of function in coenzyme A transmembrane transport. No effect on protein abundance"]; corroborated functionally [PMID:40925986 "the human disease mutant A42N291D is a loss-of-function mutant that cannot import CoA"]. Original disease reports: PMID:26541337, 29327420, 29923093, 30237576.

## Annotation-specific judgments
- **GO:0043262 ADP phosphatase activity (IDA, PMID:19429682)**: The cited paper characterizes a counter-exchange *transporter*, not a hydrolase. The AMP(in)/ADP(out) exchange half-reaction (RHEA:72851) appears to have been miscurated as a phosphatase (ADP + H2O = AMP + Pi). No hydrolysis was assayed. Experimental IDA, so per policy MARK_AS_OVER_ANNOTATED rather than REMOVE — the underlying observation (AMP handling) is real but the phosphatase MF is a misclassification of the transport activity.
- **GO:0015297 antiporter activity (IBA, GO_REF:0000033)**: correct mechanism but generic; a specific solute-transporter term (GO:0015228) is more informative. KEEP_AS_NON_CORE.
- **GO:0015605 organophosphate ester / GO:0015932 nucleobase-containing compound transmembrane transporter (ARBA IEA)**: correct-branch parents of the substrate activities (CoA and adenine nucleotides are organophosphate esters / nucleobase-containing), but too general and machine-generated. KEEP_AS_NON_CORE.
- ADP/ATP/AMP transmembrane transporter activities and their BP transport terms (all IDA PMID:19429682): experimentally supported exchange substrates but represent the antiport counter-substrates, not the physiological cargo (CoA import). ACCEPT/KEEP_AS_NON_CORE.
- Reactome TAS pantothenate metabolic process (GO:0015939) and CoA transporter (GO:0015228) and inner-membrane location: pathway-level, consistent. KEEP_AS_NON_CORE / ACCEPT.
- IntAct GO:0005515 protein binding (IPI, PMID:32296183) with KRT31/KRT34/KRTAP10-8/MTUS2 — Y2H binary-interactome keratins are common sticky hits; uninformative. MARK_AS_OVER_ANNOTATED (never REMOVE a bare protein-binding IPI per policy).

## Core functions (summary)
1. MF **GO:0015228 coenzyme A transmembrane transporter activity** — the specific, best-supported molecular function (IDA + IMP).
2. BP **GO:1990559 mitochondrial coenzyme A transmembrane transport** (IMP) with **GO:0035349 coenzyme A transmembrane transport**.
3. Location **GO:0005743 mitochondrial inner membrane** (IDA).
