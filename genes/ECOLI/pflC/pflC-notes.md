# pflC (P32675, b3952, yijM) notes

Deep research was unavailable for this gene (falcon returns 403; asta gave nothing
useful in Phase 1 of the RADICAL_SAM project). These notes are built from UniProt,
cached primary papers, PubMed and a genome-context analysis
(`pflC-bioinformatics/RESULTS.md`).

## Identity and family

- 292 aa radical SAM protein in the PFL-activating-enzyme family (PANTHER PTHR30352:SF4;
  PIRSF000371; NCBIfam NF007483). The CX3CX2C radical SAM cysteines (C47, C51, C54) and
  the SAM-binding residues are annotated by similarity to PflA [file:ECOLI/pflC/pflC-uniprot.txt
  "/evidence=\"ECO:0000250|UniProtKB:P0A9N4\""]. Unlike PflA, it has one 4Fe-4S
  ferredoxin-type domain (62-96) [file:ECOLI/pflC/pflC-uniprot.txt "4Fe-4S ferredoxin-type"].
- UniProt names it "Pyruvate formate-lyase 2-activating enzyme" with EC 1.97.1.4. The
  function statement is by similarity only [file:ECOLI/pflC/pflC-uniprot.txt "Activation of
  pyruvate formate-lyase 2 under anaerobic conditions"; evidence ECO:0000250]. PE level 3.
- Most GRE activases have an auxiliary ferredoxin-like domain, whereas PFL-AE and the
  RNR activase have only the radical SAM domain [PMID:42361324 "Notably, PFL-AE and class III
  ribonucleotide reductase (RNR)-AE solely contain the RS domain."].

## Partner GRE: PflD (P32674, yijL), not a pyruvate formate-lyase

- pflC overlaps the 3' end of pflD by 35 bp on the same strand, inside the frw PTS
  cluster [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md]. The cluster was first described
  as encoding "homologues of pyruvate formate-lyase and its activating enzyme"
  [PMID:7773398, abstract].
- PflD is a C-O lyase of 1,5-anhydromannitol 6-phosphate, not a PFL [PMID:39283600 "YbiW and
  PflD catalyze ring-opening C-O cleavage of 1,5-anhydroglucitol-6-phosphate (AG6P) and
  1,5-anhydromannitol-6-phosphate (AM6P), respectively"]. The product
  1-deoxyfructose-6-phosphate is split by FsaA/FsaB and reduced by GldA ("anhydroglycolysis"),
  and the pathway supports anaerobic growth on AG and AM [PMID:39283600]. fsaB and gldA are
  divergently encoded 6-7 genes upstream of pflD-pflC
  [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md].
- In vitro radical loading of PflD was low [PMID:42361324 "the newly characterized C–O lyases
  YbiW and PflD (0.02 and 0.06 radicals per monomer, respectively)"]. The cached abstract and
  the review do not say which activase was used. The JACS full text was not accessible
  (publisher 403), so I could not verify whether PflC itself was tested.
- PflD and YbiW share the Gly-loop heptamer RVAGYSA. PFL and TdcE, the known PflA
  substrates, have RVSGYAV [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md]. Activase
  specificity tracks the Gly-loop sequence [PMID:42361324 "These results suggest that GRE-AE
  specificity for its partner GRE is dependent upon Gly loop sequence."].
- PflC and YbiY are each other's closest paralogs (37.3% identity), and PflD and YbiW
  likewise (41.3%) [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md].

## Assessment

- No activase activity has been shown for PflC itself. Glycyl-radical enzyme activating
  activity (GO:0043364) is well supported by family placement (IBA from the PflA/NrdG node),
  intact radical SAM motifs, and coupling with a GRE whose radical-dependent chemistry is
  established.
- The PFL-specific term GO:0043365 ([formate-C-acetyltransferase]-activating enzyme
  activity; EC 1.97.1.4; RHEA:19225) names the wrong substrate GRE: PflD is not a formate
  C-acetyltransferase. It should be generalised to GO:0043364. The UniProt EC 1.97.1.4 /
  RHEA:19225 assignment should become EC 1.97.1.- / RHEA:61976 (generic glycyl-[protein]),
  as UniProt already did for YjjW.
- For the generic radical SAM rows I used the project rule's "catalysis not established"
  branch, since no PflC catalysis has been shown. GO:0051539 is KEEP_AS_NON_CORE and no
  SAM-binding NEW row is added. GO:0003824 and GO:0016491 are MODIFY to GO:0043364, the
  specific activity the gene carries (GO:0043364 is_a GO:0016491, checked in QuickGO).
- I did not propose a BP term for anhydroglycolysis. PflC would act upstream, by activating
  PflD, and there is no evidence specific to PflC. Raised as a question instead.

## Open issues

- Was PflC (or YbiY, or PflA) the activase for PflD in Ma et al. 2024? Were pflC deletions
  tested for growth on AM?
- Can PflC and YbiY cross-activate PflD and YbiW, given the identical Gly loops?
- At the time of writing, the pflA reference review (genes/ECOLI/pflA) was still
  INITIALIZED, so term choices were not aligned with it.
