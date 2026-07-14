# SLC25A21 (ODC) — review notes

UniProt: Q9BQT8 (ODC_HUMAN). HGNC:14411. Chromosome 14q11.2. 299 aa.
Gene name SLC25A21; synonym ODC (mitochondrial 2-oxodicarboxylate carrier / 2-oxoadipate carrier).

## Identity and family

- RecName in UniProt: "Mitochondrial 2-oxodicarboxylate carrier"; AltName "Mitochondrial
  2-oxoadipate carrier"; AltName "Solute carrier family 25 member 21"
  [file:human/SLC25A21/SLC25A21-uniprot.txt "RecName: Full=Mitochondrial 2-oxodicarboxylate carrier"].
- Member of the mitochondrial carrier (SLC25) family, TC 2.A.29
  [file:human/SLC25A21/SLC25A21-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family."].
  TCDB DR is 2.A.29.2.4.
- Structure: canonical tripartite Solcar fold — three Solcar repeats (11-100, 107-196, 205-294)
  and six transmembrane helices (TRANSMEM 17-37, 70-89, 113-133, 167-187, 205-225, 277-297);
  multi-pass inner-membrane protein
  [file:human/SLC25A21/SLC25A21-uniprot.txt "Mitochondrion inner membrane; Multi-pass membrane"].
- Two alternatively spliced isoforms (Q9BQT8-1 displayed; Q9BQT8-2 = VSP_046690, Missing at 299).

## Molecular function — transporter (NOT an enzyme)

SLC25A21 is a transporter/antiporter, not a catalytic enzyme. The "CATALYTIC ACTIVITY" Rhea
reactions in UniProt are transport reactions (substrate(in) + 2-oxoglutarate(out) = ...), i.e.
counter-exchange, not chemical transformation.

- FUNCTION (UniProt): "Transports dicarboxylates across the inner membranes of mitochondria by a
  counter-exchange mechanism (PubMed:11083877)."
  [file:human/SLC25A21/SLC25A21-uniprot.txt "mitochondria by a counter-exchange mechanism (PubMed:11083877). Can"].
- Substrate range (Fiermonte 2001): transports 2-oxoadipate (2-oxohexanedioate), 2-oxoglutarate,
  adipate, glutarate, and to a lesser extent pimelate, 2-oxopimelate, 2-aminoadipate, oxaloacetate,
  and citrate. Notably 2-aminoadipate is transported by human ODC but not by yeast ODC, whereas
  malate is transported by yeast ODC but NOT the human ortholog — so human SLC25A21 is NOT an
  oxoglutarate/malate carrier (that is SLC25A11)
  [PMID:11083877 "differences between the human and yeast ODCs are that 2-aminoadipate is"],
  [PMID:11083877 "by the yeast ODCs but not by the human ortholog."].
- Direct experimental characterization: recombinant human ODC expressed in E. coli, purified,
  reconstituted into liposomes; catalyzed counter-exchange of 2-oxoadipate and 2-oxoglutarate
  [PMID:11083877 "Both the human and yeast ODCs catalyzed the transport of the oxodicarboxylates"],
  [PMID:11083877 "2-oxoadipate and 2-oxoglutarate by a counter-exchange mechanism. Adipate,"].

### GO MF term choice

There is NO GO term for "2-oxoadipate", "oxodicarboxylate", or "2-oxodicarboxylate" transmembrane
transporter activity (confirmed via OLS search — no hits). GOA therefore uses **GO:0015139
alpha-ketoglutarate (= 2-oxoglutarate) transmembrane transporter activity** (IDA PMID:11083877;
IMP PMID:29517768; TAS Reactome). This is the closest available MF and is directly supported by the
reconstitution and L. lactis transport assays (both used 2-oxoglutarate). It is used for
core_functions. GO:0015367 oxoglutarate:malate antiporter activity is WRONG for this gene (human
ODC does not transport malate). No oxodicarboxylate-specific antiporter MF exists; proposed as a new
term. GO:0015297 antiporter activity (UniProtKB-KW in the UniProt DR block) is a correct but generic
parent and is not separately in the GOA TSV.

## Biological process

- 2-oxoadipate is the common catabolic intermediate of lysine, hydroxylysine and tryptophan
  degradation; SLC25A21 imports cytosolic 2-oxoadipate into the matrix (in exchange for
  2-oxoglutarate) where it is oxidatively decarboxylated (by the DHTKD1/OGDH-complex axis) and
  ultimately yields acetyl-CoA feeding the TCA cycle
  [PMID:11083877 "common intermediate in the catabolism of lysine, tryptophan, and hydroxylysine."],
  [file:human/SLC25A21/SLC25A21-uniprot.txt "a central role in catabolism of lysine, hydroxylysine, and tryptophan,"].
- GOA BP annotations: GO:1990550 mitochondrial alpha-ketoglutarate transmembrane transport (IC from
  MF; IMP PMID:29517768) — the specific transport process. GO:0019477 L-lysine catabolic process
  (TAS Reactome R-HSA-71064) — SLC25A21 supplies the mitochondrial transport step of lysine
  catabolism; KEEP_AS_NON_CORE (it is a carrier, not a lysine-catabolic enzyme; its role is the
  transport step feeding this pathway). GO:0055085 transmembrane transport (IEA InterPro) — correct
  but generic parent of the specific term.

## Subcellular location

- Mitochondrial inner membrane, multi-pass. GOA: GO:0005743 mitochondrial inner membrane
  (IEA SubCell SL-0168; ISS from yeast ODC UniProtKB:Q99297; TAS Reactome) and GO:0005739
  mitochondrion (HTP PMID:34800366, high-confidence mitochondrial proteome). All consistent with
  UniProt
  [file:human/SLC25A21/SLC25A21-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane; Multi-pass membrane"].

## Disease

- Mitochondrial DNA depletion syndrome 18 (MTDPS18; MIM:618811), autosomal recessive; SMA-like
  distal weakness, clawed hands, scoliosis, mtDNA depletion with complex I/IV deficiency
  [file:human/SLC25A21/SLC25A21-uniprot.txt "Mitochondrial DNA depletion syndrome 18 (MTDPS18)"].
- Boczonadi et al. 2018 (PMID:29517768): homozygous c.695A>G p.(Lys232Arg); transport assays show
  the variant "cannot transport substrates"; Lys232 forms a matrix salt-bridge (with Glu130) needed
  for the alternating-access mechanism. Metabolomics of patient urine: raised 2-oxoadipate,
  quinolinic and pipecolic acid, matching MitoCore flux modelling. Neuronal (SH-SY5Y) exposure to
  2-oxoadipate + quinolinic acid reduced respiratory-chain complexes and caused apoptosis — proposed
  neurotoxic mechanism for the SMA-like phenotype
  [PMID:29517768 "the p.(Lys232Arg) variant of SLC25A21 did not transport 2-oxoglutarate above background levels"],
  [PMID:29517768 "increased 2-oxoadipate, quinolinic and pipecolic acid levels in urine"].
- Note: DHTKD1 (2-oxoadipate dehydrogenase E1) is the upstream enzyme; DHTKD1 defects cause
  2-aminoadipic/2-oxoadipic aciduria and a similar dSMA phenotype — the paper compares SLC25A21 and
  DHTKD1 patients [PMID:29517768 "DHTKD1 is upstream from SLC25A21 in the tryptophan and lysine amino acid degradation pathways"].

## Curation summary (actions)

- GO:0015139 alpha-ketoglutarate transmembrane transporter activity — CORE MF.
  - IDA PMID:11083877: ACCEPT (direct reconstitution assay).
  - IMP PMID:29517768: ACCEPT (loss-of-function variant abolishes transport).
  - TAS Reactome R-HSA-372480: ACCEPT.
- GO:1990550 mitochondrial alpha-ketoglutarate transmembrane transport — CORE BP.
  - IC PMID:11083877: ACCEPT. IMP PMID:29517768: ACCEPT.
- GO:0019477 L-lysine catabolic process (TAS Reactome): KEEP_AS_NON_CORE (pathway context; carrier
  supplies the transport step, is not itself a lysine-catabolic enzyme).
- GO:0055085 transmembrane transport (IEA): KEEP_AS_NON_CORE (correct generic parent).
- GO:0005743 mitochondrial inner membrane — CORE CC (IEA SubCell, ISS, TAS Reactome all ACCEPT).
- GO:0005739 mitochondrion (HTP): KEEP_AS_NON_CORE (correct but less specific than inner membrane).

No experimental annotation is removed. No enzymatic/catalytic MF is assigned (it is a transporter).
