# SLC35B2 (PAPS transporter 1 / PAPST1) — review notes

UniProt: Q8TB61 (S35B2_HUMAN), 432 aa. Gene HGNC:16872. Chromosome 6.

## Identity and family
- RecName: "Adenosine 3'-phospho 5'-phosphosulfate transporter 1" (PAPS transporter 1, PAPST1)
  [file:human/SLC35B2/SLC35B2-uniprot.txt "RecName: Full=Adenosine 3'-phospho 5'-phosphosulfate transporter 1"].
- Belongs to the nucleotide-sugar transporter family, SLC35B subfamily
  [file:human/SLC35B2/SLC35B2-uniprot.txt "Belongs to the nucleotide-sugar transporter family. SLC35B"].
- Multi-pass Golgi membrane protein; UniProt models 9 TM helices (ECO:0000255)
  [file:human/SLC35B2/SLC35B2-uniprot.txt "Multi-pass\nCC       membrane protein"].
- Legacy alternative names reflect an overexpression cDNA screen artifact:
  "Putative MAPK-activating protein PM15" and "Putative NF-kappa-B-activating protein 48"
  [file:human/SLC35B2/SLC35B2-uniprot.txt "AltName: Full=Putative NF-kappa-B-activating protein 48"].

## Molecular function (core)
- PAPS:PAP antiporter at the Golgi membrane. UniProt FUNCTION:
  "Probably functions as a 3'-phosphoadenylyl sulfate:adenosine 3',5'-bisphosphate antiporter
  at the Golgi membranes. Mediates the transport from the cytosol into the lumen of the Golgi of
  3'-phosphoadenylyl sulfate/adenosine 3'-phospho 5'-phosphosulfate (PAPS), a universal sulfuryl
  donor for sulfation events that take place in that compartment."
  [file:human/SLC35B2/SLC35B2-uniprot.txt "a universal sulfuryl"].
- CATALYTIC ACTIVITY (Rhea:RHEA:76063): 3'-phosphoadenylyl sulfate(in) + adenosine 3',5'-bisphosphate(out)
  = 3'-phosphoadenylyl sulfate(out) + adenosine 3',5'-bisphosphate(in) — i.e. imports PAPS in exchange
  for PAP (adenosine 3',5'-bisphosphate) [file:human/SLC35B2/SLC35B2-uniprot.txt "3'-phosphoadenylyl sulfate(in) + adenosine 3',5'-"].
- KM = 0.8 uM for PAPS [file:human/SLC35B2/SLC35B2-uniprot.txt "KM=0.8 uM for 3'-phosphoadenylyl sulfate"].
- Original cloning/functional paper: PAPST1 was cloned and shown to be a Golgi PAPS transporter;
  expression in yeast increased PAPS transport into the Golgi membrane fraction
  [PMID:12716889 "The expression of PAPST1 and SLL in yeast Saccharomyces cerevisiae significantly increased the transport of PAPS into the Golgi membrane fraction"].
  Abstract also: "a specific PAPS transporter is present in Golgi membrane"; "PAPST1... a universal sulfuryl donor for sulfation"
  [PMID:12716889 "3'-phosphoadenosine 5'-phosphosulfate (PAPS), is a \nuniversal sulfuryl donor for sulfation"].

## Cellular location (core)
- Golgi apparatus membrane [file:human/SLC35B2/SLC35B2-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"].
- Transient expression of PAPST1 in SW480 cells localizes to the Golgi membrane
  [PMID:12716889 "The transient expression of PAPST1 in SW480 cells showed \na subcellular localization in Golgi membrane"].
- Guasto et al. confirmed Golgi localization and showed HLD26 variant causes partial mislocalization
  [file:human/SLC35B2/SLC35B2-uniprot.txt "partial mislocalization of the\nCC       protein, with diffuse signal in the cell and only partial"].

## Biological process
- Supplies the sulfonate (sulfuryl) donor PAPS to Golgi-lumenal sulfotransferases, driving
  glycosaminoglycan/proteoglycan sulfation (and tyrosine sulfation) downstream. Loss of function
  reduces proteoglycan/chondroitin sulfate sulfation.
- Guasto et al. 2022 (PMID:35325049): biallelic SLC35B2 variants cause hypomyelinating leukodystrophy
  with chondrodysplasia (HLD26, MIM:620269); patient fibroblasts show proteoglycan sulfation impairment
  [PMID:35325049 "we detected proteoglycan sulphation impairment in SLC35B2 patient \nfibroblasts and serum"];
  HLD26 variant caused "decreased chondroitin\nsulfate disaccharide sulfation in homozygous patient's skin\nfibroblasts"
  [file:human/SLC35B2/SLC35B2-uniprot.txt "decreased chondroitin"].
- Drosophila ortholog slalom (sll) is essential for viability (RNAi lethal), underscoring the pathway's importance
  [PMID:12716889 "An RNA interference fly of sll produced with a GAL4-UAS system revealed that the \nPAPS transporter is essential for viability"].

## Substrate note: APS vs PAPS (relevant to a GOA annotation)
- SLC35B2 transports **PAPS** = 3'-phosphoadenosine 5'-phosphosulfate = "3'-phospho-5'-adenylyl sulfate"
  (GO:1902559 / GO:0046963 / GO:0046964).
- **APS** = adenosine 5'-phosphosulfate = "5'-adenylyl sulfate" (GO:1902558) is the biosynthetic PRECURSOR to
  PAPS (APS + ATP -> PAPS), NOT the substrate of this Golgi antiporter. The Reactome-sourced TAS annotation to
  GO:1902558 (5'-adenylyl sulfate transmembrane transport) therefore uses the wrong metabolite; the Reactome
  reaction itself is about PAPS:PAP exchange
  [Reactome:R-HSA-741449 "Both proteins can transport PAPS from the cytosol to the Golgi lumen, simultaneously antiporting PAP back to cytosol"].
  Reviewed as MODIFY -> GO:1902559 (PAPS transmembrane transport).

## Interactions (protein binding annotations)
- IntAct/HuRI large-scale screens (PMID:32296183 reference interactome; PMID:40355756 SLC superfamily interactome)
  report physical partners (e.g. GOLM1/Q8NBJ4, AQP6, CREB3L1, ERGIC3, TMEM248, etc.)
  [file:human/SLC35B2/SLC35B2-uniprot.txt "Q8TB61; Q8NBJ4: GOLM1; NbExp=4"]. These are bare "protein binding"
  (GO:0005515) with no specific molecular-function meaning; treated as over-annotation (adapter/complex role
  not established). No specific MF term is warranted from these.

## NF-kappaB / MAPK annotation (over-annotation)
- The GO:0043123 (positive regulation of canonical NF-kappaB) annotation derives from a large-scale
  overexpression cDNA reporter screen (PMID:12761501), which flagged this clone as an NF-kappaB/MAPK
  activator (hence UniProt's "Putative ... PM15" / "Putative NF-kappa-B-activating protein 48" names).
  Evidence code is HMP (high-throughput). This is a screen artifact of forced overexpression, not a
  demonstrated physiological function of a Golgi PAPS antiporter; treated as over-annotation.
  [PMID:12761501 "we identified 299 \ncDNAs that activate the NF-kappaB pathway"].

## Disease
- HLD26 (Leukodystrophy, hypomyelinating, 26, with chondrodysplasia), autosomal recessive, MIM:620269
  [file:human/SLC35B2/SLC35B2-uniprot.txt "Leukodystrophy, hypomyelinating, 26, with chondrodysplasia"].

## Curation summary
- Core MF: GO:0046964 (PAPS transmembrane transporter activity) — IDA-supported (PMID:12716889) + IBA/TAS.
- Core BP: GO:0046963 / GO:1902559 (PAPS (transmembrane) transport).
- Core CC: GO:0000139 (Golgi membrane) / GO:0005794 (Golgi apparatus).
- Over-annotations: bare GO:0005515 protein binding (x2 refs); GO:0043123 NF-kB (overexpression screen);
  GO:0016020 membrane (uninformative general CC).
- MODIFY: GO:0005789 ER membrane IBA -> Golgi membrane (wrong compartment, family over-propagation);
  GO:1902558 APS transport TAS -> GO:1902559 PAPS transport (wrong metabolite).
- Non-core: GO:0055085 transmembrane transport (general parent); GO:0050650 chondroitin sulfate PG
  biosynthesis (downstream consequence of PAPS supply, not the direct transporter MF).
</content>
</invoke>
