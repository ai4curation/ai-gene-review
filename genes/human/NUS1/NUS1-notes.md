# NUS1 (NgBR / Nogo-B receptor) — review notes

UniProt: Q96E22 (NGBR_HUMAN). Gene: NUS1 (HGNC:21042; synonyms C6orf68, NGBR).
293 aa, ER multi-pass membrane protein. EC 2.5.1.87.

## Core biology (from UniProt file + primary literature)

NUS1/NgBR is the **non-catalytic subunit of the human cis-prenyltransferase (cis-PT / cis-IPTase)
complex**, the obligate partner of the catalytic subunit **DHDDS** (hCIT). Together they form the
**dehydrodolichyl diphosphate synthase (DDS) complex**, which catalyzes the committed step of dolichol
biosynthesis: condensation of multiple isopentenyl diphosphate (IPP) units onto (2E,6E)-farnesyl
diphosphate (FPP) to make **dehydrodolichyl diphosphate (Dedol-PP)**, the precursor of dolichol
phosphate (Dol-P). Dol-P is the obligate glycosyl carrier lipid for N-linked protein glycosylation
in the ER.

- UniProt FUNCTION: "With DHDDS, forms the dehydrodolichyl diphosphate synthase (DDS) complex, an
  essential component of the dolichol monophosphate (Dol-P) biosynthetic machinery ... Both subunits
  contribute to enzymatic activity, i.e. condensation of multiple copies of isopentenyl pyrophosphate
  (IPP) to farnesyl pyrophosphate (FPP) to produce dehydrodolichyl diphosphate (Dedol-PP), a precursor
  of dolichol phosphate which is utilized as a sugar carrier in protein glycosylation in the
  endoplasmic reticulum (ER)" [file:human/NUS1/NUS1-uniprot.txt].
- UniProt SUBUNIT: "The active dehydrodolichyl diphosphate synthase complex is a heterotetramer
  composed of a dimer of heterodimer of DHDDS and NUS1" [file:human/NUS1/NUS1-uniprot.txt].
- UniProt DOMAIN / RXG motif: "Contains the RXG motif, which is important for substrate binding and
  prenyltransferase activity. The catalytic site at NUS1-DHDDS interface accomodates both the allylic
  and the homoallylic IPP substrates ... The beta-phosphate groups of IPP substrates form hydrogen
  bonds with the RXG motif of NUS1 and four conserved residues of DHDDS" [file:human/NUS1/NUS1-uniprot.txt].
  RXG motif is residues 290-292; BINDING sites at 291 and 292 (isopentenyl diphosphate). ComplexPortal
  CPX-6701 = Dehydrodolichyl diphosphate synthase complex.

## Catalysis is a shared property of the heterodimer

NUS1 alone lacks transferase activity; DHDDS carries the classic cis-PT catalytic residues, but NUS1
is strictly required and contributes to the active site via its C-terminal RXG motif.

- Miao et al. 2006 (PMID:16835300, not cached) originally showed partially purified NgBR "lacks
  cis-IPTase activity" (cited in PMID:19723497 full text: "Previous studies using partially purified
  NgBR showed that it lacks cis-IPTase activity (Miao et al., 2006)").
- PMID:28842490 (Grabinska 2017, abstract only in cache): "we establish the first purification system
  for heteromeric cis-PT and show that both NgBR and hCIT subunits function in catalysis and substrate
  binding. Finally, we identified a critical RXG sequence in the C-terminal tail of NgBR that is
  conserved and essential for enzyme activity across phyla" [PMID:28842490]. MUTAGEN G292A and K293
  deletion cause "Almost complete loss of catalytic activity" [file:human/NUS1/NUS1-uniprot.txt].
- PMID:32817466 (Edani 2020, abstract only in cache): crystal structure of NgBR/DHDDS; "The crystal
  structure sheds light on how NgBR stabilizes DHDDS through dimerization, participates in the enzyme's
  active site through its C-terminal -RXG- motif, and how phospholipids markedly stimulate cis-PTase
  activity" [PMID:32817466].
- PMID:25066056 (Park 2014, full text): both hCIT and NgBR necessary for dolichol biosynthesis in
  yeast/mice/man; only co-translation of Nus1 with Rer2/hCIT "formed an active cis-PTase complex ...
  indicating that both proteins are required for a functional enzyme" [PMID:25066056].

=> Model MF as `contributes_to_molecular_function: GO:0045547` (ditrans,polycis-polyprenyl diphosphate
synthase [(2E,6E)-farnesyl diphosphate specific] activity), i.e. the complex-level activity that NUS1
contributes to but does not perform independently. GOA has both `enables` (EXP/IEA/IDA) and
`contributes_to` (IDA) forms; the `contributes_to` framing is the biologically accurate one for a
subunit whose partner carries the catalytic machinery.

## Localization

ER membrane, multi-pass. UniProt SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Multi-pass
membrane protein" [file:human/NUS1/NUS1-uniprot.txt]. Confirmed experimentally by PMID:19723497
("NgBR localizes primarily to the endoplasmic reticulum (ER)"), PMID:21572394, and Reactome. Three
TRANSMEM helices annotated (1-23, 35-56, 117-135). NUS1 exists in two topological orientations
(minor luminal-C, major cytosolic-C) per UniProt MISCELLANEOUS.

## Disease

- CDG1AA [MIM:617082], autosomal recessive congenital disorder of glycosylation. Homozygous R290H
  (in the conserved C-terminal RXG region) is loss-of-function: "the NgBR R290H mutant is a loss of
  function mutation that affects cis-PTase function of NgBR without disrupting complex formation with
  hCIT" [PMID:25066056]. Patients: congenital scoliosis, severe neurological impairment, refractory
  epilepsy, hypotonia, visual/hearing impairment (PMID:25066056).
- MRD55 [MIM:617831], autosomal dominant intellectual disability with seizures; de novo variants
  (PMID:29100083, cited in UniProt; not cached). Progressive myoclonus epilepsy truncating variant
  V104-K293del (PMID:33798445, cited in UniProt).

## Non-core / accessory roles

- Cholesterol trafficking / NPC2: NgBR binds and stabilizes NPC2, regulating LDL-derived cholesterol
  trafficking (PMID:19723497, full text). "NgBR enhances NPC2 protein stability ... loss of NgBR ...
  lead to a decrease in NPC2 levels, increased intracellular cholesterol accumulation" [PMID:19723497].
  This is a real, experimentally-supported accessory function but not the core evolved cis-PT function;
  and it is partly downstream of the cis-PTase/glycosylation defect (mutant NgBR can influence NPC2
  glycosylation via reduced cis-PTase activity, per PMID:25066056 discussion). Keep as non-core.
- Nogo-B receptor / vascular / angiogenesis: originally identified as the receptor for the N-terminus
  of Nogo-B (reticulon-4B) in endothelial cells (Miao 2006, PMID:16835300; UniProt AltName "Nogo-B
  receptor"). PMID:28602162 (BMB Rep 2017, a review/News-type article; publication_type
  COMMENT_EDITORIAL) reports miR-26a regulates VEGF-NgBR-mediated angiogenesis; the NgBR IMP data
  concern EC migration/proliferation/tube formation downstream of VEGF via eNOS. These vascular/VEGF
  roles are physiological but represent a distinct, tissue-specific signaling context rather than the
  gene's conserved molecular function; treat as non-core (KEEP_AS_NON_CORE). Note PMID:28602162 in
  the cache is annotated as a News/comment item — its NgBR knockdown migration data are experimental
  (BHF-UCL IMP), so I retain the annotations as non-core rather than removing.

## Interactions (IPI protein binding annotations)

- PMID:21572394 with UniProtKB:Q9H7T3 — that accession is C10orf95 (per UniProt INTERACTION block:
  "Q96E22; Q9H7T3: C10orf95"), an IntAct interaction. Bare protein binding; MARK_AS_OVER_ANNOTATED
  per policy (keep, uninformative MF).
- PMID:32817466 with UniProtKB:Q86SQ9 — that accession is DHDDS (UniProt INTERACTION: "Q96E22; Q86SQ9:
  DHDDS"). This is the obligate catalytic partner; the specific, informative capture is complex
  membership (GO:1904423), which is separately annotated. Bare protein binding here is
  over-annotated (uninformative) even though the interaction is central.
- PMID:33961781 with UniProtKB:Q86SQ9 (DHDDS) — BioPlex/Huttlin high-throughput AP-MS interactome;
  same DHDDS interaction. Bare protein binding; MARK_AS_OVER_ANNOTATED.

## Term id / label checks (OLS REST, go, 2026-07)

- GO:0045547 = "ditrans,polycis-polyprenyl diphosphate synthase [(2E,6E)-farnesyl diphosphate specific]
  activity" — MF, current.
- GO:0006489 = "dolichyl diphosphate biosynthetic process" — BP, current.
- GO:0043048 = "dolichyl monophosphate biosynthetic process" — BP, current.
- GO:1904423 = "dehydrodolichyl diphosphate synthase complex" — CC, current.
- GO:0005789 = "endoplasmic reticulum membrane" — CC, current.
- GO:0004659 = "prenyltransferase activity" — MF, current (broad parent).
- GO:0009101 = "glycoprotein biosynthetic process" — BP, current.
- GO:0016765 = "transferase activity, transferring alkyl or aryl (other than methyl) groups" — MF (broad).
- Note: GO:0019408 "dolichol biosynthetic process" and GO:0006486 "protein glycosylation" are now
  OBSOLETE in current GO — do NOT use these; use GO:0006489 / GO:0043048 / GO:0009101 instead.

## Core function decision

- contributes_to_molecular_function: GO:0045547 (cis-PT/DDS complex catalytic activity; NUS1 contributes
  via RXG motif, does not catalyze alone).
- directly_involved_in: GO:0006489 (dolichyl diphosphate biosynthetic process) and GO:0043048 (dolichyl
  monophosphate biosynthetic process); glycoprotein biosynthetic process (GO:0009101) is the downstream
  purpose captured as a non-core BP.
- in_complex: GO:1904423 (dehydrodolichyl diphosphate synthase complex).
- locations: GO:0005789 (endoplasmic reticulum membrane).
