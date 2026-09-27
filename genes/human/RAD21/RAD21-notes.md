# RAD21 (human, UniProt O60216) — curation notes

Working journal for the AI review of human RAD21 (cohesin alpha-kleisin SCC1).
Exemplar used: `genes/SCHPO/rad21/rad21-ai-review.yaml` (fission-yeast ortholog) for the
cohesin core-function framing; `genes/human/CDC20/CDC20-ai-review.yaml` and
`genes/human/ESPL1/ESPL1-ai-review.yaml` for style and for how the separase-substrate
relationship was handled on the enzyme side.

## 1. Identity and architecture

- 631-aa alpha-kleisin (Rad21/Rec8 family; InterPro IPR006910 N-terminal, IPR006909 C-terminal,
  IPR049589 NXP1_M-like central region). Not to be confused with the meiotic paralogs REC8 and RAD21L.
- N-terminal domain binds the SMC3 ATPase head; C-terminal winged-helix binds the SMC1A head
  [file:human/RAD21/RAD21-uniprot.txt "The C-terminal part associates with the ATPase head of SMC1A,
  while the N-terminal part binds to the ATPase head of SMC3."]; cryo-EM of human cohesin-NIPBL-DNA
  [PMID:32409525 "Cohesin and NIPBL interact extensively and together form a central tunnel to entrap a
  72-base pair DNA."].
- Central region 287-449 is the STAG (SA1/SA2) docking site, and WAPL/PDS5B bind the same region in the
  presence of SA1 [PMID:19696148 "a central region of hRad21 (amino acids 287–449) was required for its
  interaction with hSA1"; "hWapl and hPds5B bound to the same region in the presence of hSA1";
  "in the absence of hRad21, virtually no interaction was detectable between hWapl and hSA1"].
  Crystal structure of the SA2-Scc1 subcomplex [PMID:25173175 "Scc1 makes extensive contacts with SA2,
  with one binding hotspot."; "Sgo1 and Wapl compete for binding to a conserved site on SA2-Scc1."].
- RAD21 is non-catalytic; ATPase activity is in the SMC heads. The kleisin role is best captured by
  GO:0030674 protein-macromolecule adaptor activity (same resolution as in the S. pombe rad21 review).

## 2. Cohesion cycle

- Loading by NIPBL-MAU2 (Scc2-Scc4); replication stabilises loaded cohesin [PMID:22628566 "Replication
  of cohesin-loaded DNA, both in vitro and in vivo, markedly increased the stability of cohesin
  associated with DNA."].
- Scc1 RNAi abolishes cohesion [PMID:15855230 "Depletion of the cohesin subunit Scc1 by RNA interference
  leads to the assembly of chromosomes with severe cohesion defects."]; PDS5 chromatin association is
  cohesin-dependent [PMID:15855230 "Pds5 proteins physically interact with cohesin and associate with
  chromatin in a cohesin-dependent manner."].
- Sororin maintains cohesion by antagonising WAPL at PDS5 [PMID:21111234 "Sororin displaces Wapl from its
  binding partner Pds5"]; WAPL is the release factor [PMID:17112726 "reconstitution experiments using
  recombinant subunits demonstrate that Wapl binds to the two regulatory subunits of cohesin (Scc1 and
  SA1) and forms a stoichiometric, ternary complex"; PMID:17113138 "Wapl depletion also increases the
  residence time of cohesin on chromatin in interphase."].
- Localisation through mitosis [PMID:11073952 "hRad21 remains associated with prometaphase-like
  chromosomes along their entire lengths"; "hRad21 remains specifically at the centromeres but
  disappears from the arm regions on metaphase-like chromosomes"; "hRad21 at the metaphase centromeres
  appears to be present at the inner pairing domain where the two sister chromatids are supposed to be
  in intimate contact"]. Centromeric protection: phospho-SGO1-PP2A binds the Scc1-SA2 subcomplex
  [PMID:23242214 "Cdk1-phosphorylated GST-Sgo1 bound efficiently to the Scc1–SA2 complex expressed in
  Sf9 insect cells"].
- Separase cleavage at R172/R450 [PMID:11509732 "We have identified two separase cleavage sites in the
  human cohesin subunit SCC1 and have conditionally expressed noncleavable SCC1 mutants in human cells";
  "cohesin cleavage by separase is essential for sister chromatid separation and for the completion of
  cytokinesis"]. Scc1 phosphorylation enhances cleavability but is dispensable for prophase release
  [PMID:15737063 "Scc1 phosphorylation is dispensable for cohesin dissociation from chromosomes in early
  mitosis, but enhances the cleavability"]. Separase docking motifs on Scc1 [PMID:34290405 "the Scc1
  NHLEYE motif promotes Scc1 binding to separase"].
- Cleaved RAD21 fragments stay on cohesin until HDAC8 deacetylates SMC3 [PMID:22885700 "In HDAC8 mutant
  cells, RAD21-N co-immunoprecipitates with SMC1A, SMC3, STAG1, and STAG2"].

## 3. Loop extrusion / transcription

- [PMID:32409525 "As a ring-shaped adenosine triphosphatase (ATPase) machine, cohesin organizes the
  eukaryotic genome by extruding DNA loops and mediates sister chromatid cohesion by topologically
  entrapping DNA."]
- CTCF insulation [PMID:18235444 "Cohesin enables CTCF to insulate promoters from distant enhancers and
  controls transcription at the H19/IGF2 (insulin-like growth factor 2) locus."; "CTCF is dispensable for
  cohesin loading onto DNA, but is needed to enrich cohesin at specific binding sites."].
- CdLS transcriptional dysregulation with RAD21 ChIP-chip [PMID:19468298 "the binding sites are enriched
  within the promoter regions of the dysregulated genes and are significantly decreased in CdLS proband"].
- SA1 vs SA2 variants [PMID:29867216 "cohesin-SA2 promotes cell-type-specific contacts between enhancers
  and promoters independently of CTCF"].
- Deep research (falcon) summarises the 2023 Genome Biology RAD21-dosage study: RAD21 elevation increases
  loader binding and loading and rewires TAD/compartment contacts (not cached as a PMID here).

## 4. DNA damage

- [PMID:19629043 "Cohesin also becomes enriched at DNA double-strand break sites and facilitates
  recombinational DNA repair."; "Here, we report that cohesin is essential for the DNA damage-induced
  G2/M checkpoint."; "In contrast to cohesin's role in DNA repair, the checkpoint function of cohesin is
  independent of its ability to mediate cohesion."; Scc1-depleted mitotic cells: "almost all mitotic
  cells contained broken chromosomes, most of which were highly fragmented"].
- [PMID:17349791 "Like cohesin, sororin is also needed for efficient repair of DNA double-strand breaks
  in G2."]
- Reactome R-HSA-3108212: NSMCE2 SUMOylates RAD21; SUMOylation needed for sister chromatid recombination.
- The original human TAS annotations (DSB repair, DNA recombination, reciprocal meiotic recombination)
  come from the 1996 cloning paper, which only inferred function from S. pombe homology and expression
  [PMID:8812457 "Elevated expression of mHR21sp in testis and thymus supports a possible role for the
  rad21 mammalian homologs in V(D)J and meiotic recombination, respectively."].

## 5. Apoptosis and other locations

- Caspase-3/-7 cleavage at D279 produces a pro-apoptotic 64-kDa C-terminal fragment [PMID:11875078 "the
  partial removal of RAD21 from chromatin and the production of a proapoptotic carboxyl-terminal cleavage
  product that amplifies the cell death signal"; PMID:12417729 "hRad21 is a nuclear protein; however, the
  cleaved 64-kDa carboxy-terminal product is translocated to the cytoplasm early in apoptosis before
  chromatin condensation and nuclear fragmentation"]. This explains the UniProt-derived cytosol IEA.
- Nuclear matrix [PMID:10623634 "Western blot analysis with anti-NXP-1 polyclonal antibody showed nuclear
  matrix localization of NXP-1 in HeLa cells"; PMID:11590136 "a significant amount of cohesin was found
  to associate with the nuclear matrix"] and spindle poles [PMID:11590136 "we found that cohesin
  localizes to the spindle poles during mitosis and interacts with NuMA"] — both graded non-core.
- Membrane HDA (PMID:19946888) is an NK-cell membrane-proteome contaminant; REMOVE.

## 6. Curation decisions (summary)

- Protein binding IPIs (69 rows): partners SMC1A, SMC3, STAG2, PDS5A, PDS5B, WAPL -> MODIFY to
  GO:0030674 protein-macromolecule adaptor activity (kleisin bridging/docking role, structurally
  defined). ESPL1 (substrate relationship; captured on the ESPL1 side with RAD21 as input), CHTF18,
  mouse Cdca5, DDX11, SSU72, FHL3 -> REMOVE as uninformative generic protein binding, without disputing
  the interactions. Partner accessions resolved with the UniProt REST API.
- Rat-derived Ensembl-Compara IEAs (hypoxia, IL-1beta/TNF/IL-10 production, glial/neuron apoptosis,
  lncRNA binding) -> REMOVE (fail participation test; pleiotropic phenotypes from a single rat source).
  Positive/negative regulation of gene expression -> MODIFY to GO:0006357. DNA-binding TF binding ->
  MARK_AS_OVER_ANNOTATED (CTCF contact is via STAG2).
- Mouse-derived IEAs: cis-regulatory sequence-specific DNA binding -> MODIFY to chromatin binding;
  negative regulation of G2/M transition -> MODIFY to GO:0007095 mitotic G2 DNA damage checkpoint
  signaling (PMID:19629043); negative regulation of metaphase/anaphase transition -> REMOVE (RAD21 is the
  substrate, not the regulator).
- GO:0045876 positive regulation of sister chromatid cohesion (IMP) -> MODIFY to GO:0007064 (RAD21 is the
  structural mediator, not a regulator). GO:0007062 IEA -> MODIFY to GO:0007064; the IBA is ACCEPTED
  because its node includes meiotic kleisins.
- Meiotic cohesin complex (IBA seeded by mouse Rad21l; NAS) and establishment of meiotic cohesion (NAS)
  -> KEEP_AS_NON_CORE (RAD21-STAG3 complexes exist per UniProt; REC8/RAD21L are the main meiotic kleisins).
- Reciprocal meiotic recombination TAS -> REMOVE (speculative from expression); DNA recombination TAS ->
  MODIFY to GO:1990414.
- Comparator check for core-function terms: no human cohesin subunit (SMC1A, SMC3, STAG1, STAG2) carries
  GO:0140588 chromatin looping in GOA (QuickGO, 2026-09-25), although S. pombe rad21 carries it by IDA
  and the GO definition names SMC complexes as the extrusion motor. Kept in core_functions and raised as
  a suggested question rather than added as a NEW annotation, because the direct human RAD21 degron/Hi-C
  and single-molecule papers are not in the publication cache.
- GO:0000070 mitotic sister chromatid segregation is not listed in core_functions: human RAD21 has no
  such annotation (SMC1A carries a 1995 TAS), and on the participation test RAD21's contribution to
  segregation is the cohesion it provides (GO:0007064/GO:0034087, already listed) while the separating
  step at anaphase is performed by separase on RAD21 as substrate. QuickGO confirms GO:0007064 is not an
  ancestor/descendant of GO:0000070, so this is a scoping choice, not a redundancy fix.
