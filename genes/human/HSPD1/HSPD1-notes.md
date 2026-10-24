# HSPD1 evidence notes

[PMID:1346131](https://pubmed.ncbi.nlm.nih.gov/1346131/) reconstitutes mammalian Hsp60/Hsp10 substrate folding with MgATP; [PMID:25918392](https://pubmed.ncbi.nlm.nih.gov/25918392/), DOI [10.1073/pnas.1411718112](https://doi.org/10.1073/pnas.1411718112), solves the human type I chaperonin complex. These establish the distinction from the cytosolic type II TRiC/CCT system, independently of an AI review or ARBA.

Horse F6Z587 has 541 residues versus 573 for human P10809, with an internal deletion of human 171–202. The N-terminal mitochondrial precursor and annotated ATP-binding positions are conserved. Broad ATP binding and mitochondrial targeting remain reasonable inferences, but full ATP-dependent folding competence is uncertain for this model. The existing horse ARBA GO:0005832 TRiC-complex annotation is wrong at family/complex level regardless of whether this deletion preserves Hsp60 activity.

[PMID:17823127](https://pubmed.ncbi.nlm.nih.gov/17823127/) shows that cytosolic Hsp60 can promote death or survival in different apoptotic systems, with different caspase-3 interactions. Do not remove opposing apoptotic-direction annotations solely because they share a reference. Immune responses to extracellular preparations require their own preparation/contamination and receptor-dependence controls; those rows remain UNDECIDED rather than being accepted as a universal Hsp60 cytokine activity or rejected from localization alone.

A completed human Falcon report has been inspected. The selected horse record is unreviewed; the initial literature search did not identify a targeted horse HSPD1 mechanistic experiment warranting a separate horse Edison report.

## Human structural research

The completed Falcon report identifies [PMID:32317635](https://pubmed.ncbi.nlm.nih.gov/32317635/), [DOI:10.1038/s41467-020-15698-8](https://doi.org/10.1038/s41467-020-15698-8), which establishes active single- and double-ring human Hsp60–Hsp10 assemblies. It also identifies [PMID:31444388](https://pubmed.ncbi.nlm.nih.gov/31444388/), [DOI:10.1038/s41598-019-48762-5](https://doi.org/10.1038/s41598-019-48762-5), on impaired client refolding by disease variants. These primary identities were independently verified. ATP turnover and productive folding are distinct readouts, strengthening the caution about the selected horse deletion. The earlier manual synthesis is retained as separately labeled primary-source analysis.

## Full-gene IBA re-review, 2026-09-20

All 178 annotation rows were screened. The previous blanket immune UNDECIDED rationale overlooked explicit primary controls: PMID:15371451 separates endotoxin-dependent macrophage TNF effects from retained T-cell costimulation using low-endotoxin human and eukaryotically expressed Hsp60; PMID:16148103 uses human Hsp60 on mouse B cells and reports TLR4/MyD88 dependence and LPS controls; PMID:17164250 directly tests LPS binding and distinguishes LPS-associated and IFN-alpha-associated immune effects; PMID:18256040 tests endotoxin-free costimulation. These support context-specific non-core immune annotations, not a universal cytokine activity. PMID:10663613 independently supports tumor-surface immune recognition. The vertebrate IBA node PTN002900230 includes human HSPD1 experimental grounding; that is not circular support. Detailed IgG-switch and stable LPS-receptor-complex claims remain UNDECIDED where the retrieved experiments do not resolve those precise assertions.

The ISS DNA-binding donor is yeast Hsp60/P19882, with real gel-shift/crosslinking evidence in PMID:10869431; human origin-specific/nucleoid conservation remains uncertain. The cold-response donor is chicken Q5ZL72 with PMID:23636703, not an unresolved horse experiment. The human RNA HDA observation is retained as non-core; the exact HSPD1 dsRNA entry from PMID:21266579 still needs table/supplement recovery and is not rejected from a Raftlin-focused title. Hsp60-p53/survivin statements now cite their own PMID:18086682 experiment.

The inner-membrane IBA PTN000143509 remains compatible with a principal matrix pool. The import IBA PTN000143510 is separately UNDECIDED: PMID:1347713 reports antifolding/export of cytochrome b2, whereas PMID:7911803 finds stop-transfer sorting of cytochrome-b2-presequence fusion proteins without Hsp60 exposure. A neutral OpenScientist request will assess substrate/route differences and human conservation. Neither matrix localization nor a single yeast donor refutes participation. Generic protein binding is removed for informativeness without denying its interaction evidence.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: all 178 GOA rows, description and core functions re-examined; no ProtNLM2 file or prediction-evidence folder was opened.

Identity: P10809 is the reviewed canonical human HSPD1 product (573 aa precursor, transit peptide 1-26, mature chain 27-573; isoform P10809-2 exists but the benchmark accession is isoform 1). It is not a fragment or alternative gene model. The earlier review text carried horse-specific caveats (F6Z587 internal deletion of human 171-202) into human rows; those have been removed from the human review because they do not apply to P10809. The horse deletion remains a question for genes/HORSE/HSPD1 only.

Evolutionary grounding: PANTHER PTHR45633 (60 kDa heat shock protein, mitochondrial), subfamily SF17 per the PANTHER 19.0 member index. PAINT nodes in the IBA rows: PTN000143677 (type I chaperonin root; GroEL, mycobacterial Cpn60, yeast HSP60, HSPD1 seeds; protein folding), PTN000143509 (mitochondrial Hsp60; matrix, inner membrane, Hsp10 binding), PTN000143510 (UPRmt from worm hsp-60; IMS import from yeast HSP60), PTN000888030 (apoptotic mitochondrial changes, rat), PTN002900230 (vertebrate immune terms, mouse + human seeds). PAINT placed GroEL-GroES complex (GO:1990220) and ATP binding only at the bacterial node PTN000143644, so the bacterial complex term is not transferred to HSPD1, which is correct (that GO term is defined as bacterial).

Key literature used: Viitanen 1992 [PMID:1346131 "facilitates the formation of catalytically active ribulose-bisphosphate carboxylase from an unfolded state in the presence of K+ and MgATP."]; Levy-Rimler 2001 [PMID:11422376 "Mitochondrial chaperonins are necessary for the folding of newly imported and stress-denatured mitochondrial proteins."]; Gomez-Llorente 2020 [PMID:32317635 "Refolding assays demonstrate obligate single- and double-ring mHsp60 variants are active"]; Wang 2019 disease variants [PMID:31444388 "unable to fold denatured substrates such as α-lactalbumin, malate dehydrogenase (MDH), and the β-subunit of ATP synthase"].

Main changes versus the previous version:
- Immune rows split by evidence quality. Kept (non-core): LPS binding, IFN-alpha induction, IFN-gamma, positive regulation of T cell activation, IL-12 (LPS-dependent), gamma-delta T-cell tumour recognition. Endotoxin-free Hsp60 costimulates T cells independently of TLR4 [PMID:18256040 "T cell co-stimulation induced by LPS-free Hsp60 was independent of TLR4"].
- MARK_AS_OVER_ANNOTATED: MyD88-dependent TLR signalling, B cell proliferation/activation, IL-10, IL-6 (IBA + IDA), macrophage activation, LPS receptor complex. Basis: [PMID:18256040 "LPS-free Hsp60 did not induce IL-6, IL-12 or tumor necrosis factor alpha production in APC"], [PMID:17164250 "Hsp60 exclusively binds to macrophages and DC but not to T or B lymphocytes"], [PMID:15371451 "The induction of tumor necrosis factor-alpha secretion in mouse macrophages is lost after endotoxin removal"]. Not removed, because PMID:16148103 reports LPS controls the curator saw in full text.
- T cell activation (IBA + 3 IDA) MODIFY to GO:0050870 positive regulation of T cell activation: Hsp60 is an extracellular costimulator, not activation machinery.
- ARBA positive regulation of cytokine production MODIFY to GO:0032727 IFN-alpha.
- Mitochondrion rows MODIFY to mitochondrial matrix (correct-but-general rule); cytoplasm and membrane TOO_GENERAL.
- Endocytic compartments from PMID:11807771 (exogenous Hsp60 internalised by DCs) MARK_AS_OVER_ANNOTATED; protein-containing complex (co-IP) MARK_AS_OVER_ANNOTATED.
- Response to cold (chicken expression change only) MARK_AS_OVER_ANNOTATED.
- Response to unfolded protein, mtUPR, chaperone-mediated complex assembly, protein maturation demoted to KEEP_AS_NON_CORE (effector/peripheral).
- IMS import IBA (GO:0045041) stays UNDECIDED: the yeast source biology is disputed (PMID:1347713 vs PMID:7911803). The phylogenetic placement is not at fault.
- DNA-binding ISS rows (yeast donor PMID:10869431) and dsRNA binding stay UNDECIDED.
- Protein binding: all REMOVE per policy.
- Core functions: ATP-dependent protein folding chaperone (matrix; folding and refolding) and Hsp10 co-chaperonin binding.

Relative chosen for next review: mouse Hspd1 (P63038), the closest experimentally characterised ortholog (same PTHR45633 family, a seed of the vertebrate PAINT node PTN002900230). No repo review exists. The yeast HSP60 (P19882) review exists at DRAFT status; E. coli GroEL has a COMPLETE review.

Family review interpro/panther/PTHR45633/PTHR45633-review.yaml lists P10809 under "Benchmark members without resolved subfamily placement". The member index places P10809 in PTHR45633:SF17. This is not a disagreement, only an unresolved placement there. Its UNRESOLVED scope for GO:0140662 (Tcm62 boundary) does not affect HSPD1, which sits squarely in the canonical Hsp60 branch.

No module includes HSPD1. Related modules: modules/mitochondrial_upr.yaml, modules/mitochondrial_protein_import.yaml, modules/bacterial_groel_groes_chaperonin_folding.yaml (bacterial homolog).
