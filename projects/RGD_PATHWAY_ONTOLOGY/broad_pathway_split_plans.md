# Split plans for the broad RGD pathways

Back to the project page: [RGD_PATHWAY_ONTOLOGY](../RGD_PATHWAY_ONTOLOGY.md).

Five RGD diagram pathways have more than 100 curated human genes and are flagged
`broad` by the triage. One module per pathway would be unreadable and could not
apply the house rules for parts, functions and evidence. This page proposes how
to split each into modules of ordinary size, before any is modelled. Two more
seeds reach `has_module` only by gene overlap and are covered at the end.

The plans follow the same rules as the two splits already done, chromatin
remodeling (by remodeler family) and calcium transport (by transport system):

- **One module per mechanism, not per gene list.** A module covers a complex or a
  defined step with its own GO process, and its parts do work in that step.
- **Every sub-module cites the broad PW id as an `evidence` source.** That is how
  the triage counts coverage, and it is true, because each covers part of the
  pathway. RGD's child pathway ids are cited as well where one exists, and are
  named in prose otherwise.
- **Membership is not participation.** RGD gene lists include genes that host a
  snoRNA or microRNA ("Small nucleolar RNA protein coding host genes",
  "MicroRNA protein coding host genes" in HGNC), and genes linked through a
  diagram's sub-pathway links. Each needs its own evidence of doing work in the
  step; a host gene is not a participant because its intron encodes a guide RNA.
- **Reuse before writing.** Several steps already exist as Drosophila modules
  (`dmel_*`), which are structural analogues, not human modules. A human module
  may follow their structure but must be grounded in human evidence.

Gene counts below are RGD-curated human genes from the seed (which includes
genes RGD annotates to the pathway's sub-pathways and diagram links), with the
genes annotated directly to each PW child from `homo_genes_pw` where RGD has
children. HGNC gene-group counts are from `hgnc_complete_set.txt` and are only a
guide to where the complexes are.

## RNA polymerase II transcription (PW:0000127, 281 genes)

RGD divides this pathway itself: children for initiation (PW:0001274, 58 genes),
elongation (PW:0001331, 35) and termination (PW:0001332, 18), plus diagram links
to capping (PW:0001578), 3′-end processing (PW:0001579), the spliceosome
(PW:0001073) and chromatin modification (PW:0001337). The largest HGNC groups are
Mediator (33), TFIID (14), SAGA (17), ATAC (12) and the RNA polymerase subunits
(12).

Proposed modules, in order:

1. **`rna_polymerase_ii_core_and_initiation`**: the 12-subunit Pol II enzyme,
   written identically to the shared subunits in `rna_polymerase_i_transcription`
   and `rna_polymerase_iii_transcription`, and the general transcription factors
   TFIIA, TFIIB, TFIID, TFIIE, TFIIF and TFIIH assembling the preinitiation
   complex. Cites PW:0000127 and PW:0001274. Analogue:
   `dmel_rnapii_general_transcription_factors`. TFIIH is already a part of
   `nucleotide_excision_repair`; reference its node rather than re-modelling it.
2. **`mediator_complex`**: the head, middle, tail and CDK8 kinase modules.
   Cites PW:0000127. Analogue: `dmel_mediator_complex`.
3. **`rna_polymerase_ii_elongation_and_termination`**: promoter-proximal pausing
   (DSIF, NELF), release by P-TEFb, elongation factors (PAF1C, SPT6, FACT, the
   super elongation complex), and termination by the torpedo exonuclease XRN2.
   Cites PW:0000127, PW:0001331 and PW:0001332. Analogue:
   `dmel_rnapii_elongation_complexes`. The Pol I and III modules exclude FACT,
   PAF1C and DSIF as general elongation factors; this is where they belong.
4. **`pre_mrna_capping`** and **`pre_mrna_3prime_cleavage_polyadenylation`**:
   capping enzyme and cap methyltransferase; CPSF, CstF, CFIm, CFIIm and the
   poly(A) polymerase. Cite PW:0000127 with PW:0001578 or PW:0001579 in prose.
   Analogue: `dmel_cleavage_polyadenylation`.
5. **SAGA and ATAC** are coactivator acetyltransferase complexes and belong with
   histone modification below, not here; reference them from module 1.

The spliceosome is its own plan (below). With modules 1–4, the RNA polymerase
transcription seed (PW:0001275) would be covered for Pol I, II and III.

## Spliceosome (PW:0001073, 114 genes)

No PW children. The HGNC groups follow the spliceosome's assembly cycle: A
complex (7), B (10), Bact (16), C (29), P (24), plus the Sm (7) and LSm (7)
rings, SF3b (6), U5 snRNP (6), U4/U6 di-snRNP (5), the NineTeen complex (6) and
its associated proteins (7), and 18 hnRNPs and 11 SR proteins.

Proposed modules:

1. **`spliceosomal_snrnp_biogenesis`**: Sm-ring assembly by the SMN complex and
   snRNP maturation. Analogue: `dmel_smn_complex`.
2. **`major_spliceosome_cycle`**: one module for the U2-type spliceosome whose
   parts are the assembly states (E/A, B, Bact, C, P, ILS). Each part is a
   complex, and the snRNPs are units written once and reused across states. This
   is the shape of `dmel_spliceosome`. It is large but coherent, and splitting
   the cycle across modules would cut catalysis in half.
3. **`splice_site_selection_regulators`**: SR proteins and hnRNPs as the
   regulators of splice-site choice, modelled as variant sets of the
   activator/repressor families acting on the E/A step. This keeps their 29
   genes out of the core cycle.
4. **Minor (U12-type) spliceosome**: only if RGD's genes include U11/U12-specific
   proteins. Check before starting; otherwise note it as out of scope.

## Translation (PW:0000101, 180 genes) and ribosome biogenesis (PW:0001066, 138 genes)

These overlap heavily: all 78 genes RGD annotates directly to translation are
also annotated to ribosome biogenesis, and both seeds are dominated by the 81
ribosomal proteins (46 L, 35 S). Ribosomal
proteins are structural parts of the ribosome, so they should be modelled once,
in the ribosome, and referenced from biogenesis and translation.

RGD's translation children are initiation (PW:0000580, 34 genes), elongation
(PW:0000581, 3) and termination (PW:0000582, 5), with diagram links to the mRNA
decay pathways (nonsense-mediated PW:0000548, nonstop PW:0000549, no-go
PW:0001671), aminoacyl-tRNA biosynthesis (PW:0001159) and mRNA export
(PW:0001587, already `mrna_nuclear_export`).

Proposed modules:

1. **`cytoplasmic_ribosome`**: the 80S ribosome as a complex with 40S and 60S
   subunit parts and the ribosomal proteins as units. Cites PW:0000101 and
   PW:0001066. Analogue: `dmel_cytoplasmic_ribosome`. The rRNAs are not gene
   products in this model; state that in notes.
2. **`translation_initiation`**: eIF1, eIF1A, eIF2 (with eIF2B as its exchange
   factor), eIF3 (13 subunits), eIF4F, eIF5 and eIF5B, and scanning. Cites
   PW:0000101 and PW:0000580.
3. **`translation_elongation_and_termination`**: eEF1A, eEF1B, eEF2; eRF1-eRF3
   and ABCE1 recycling. Small in RGD (8 genes), so one module. Analogue:
   `dmel_erf1_erf3_termination_complex`.
4. **`nonsense_mediated_mrna_decay`**: UPF1-3, SMG1 and SMG5-7, with the exon
   junction complex. Cites PW:0000101 and PW:0000548 in prose. No-go and nonstop
   decay are smaller and could be variants of a ribosome-quality-control module
   later.
5. **`ribosome_biogenesis`**: Pol I transcription by reference to
   `rna_polymerase_i_transcription`; the SSU processome (12) with U3 snoRNP (4)
   and the MPP10 subcomplex (3); box C/D and H/ACA snoRNP modification (H/ACA 4);
   pre-rRNA processing nucleases (the exosome by reference, RNase MRP by analogy
   to `dmel_rnase_p_mrp`); 60S maturation factors; and nuclear export. Cites
   PW:0001066. This is the largest remaining module and may itself need two
   parts, 40S and 60S maturation, each a sub-module referenced from here.
6. **snoRNA and microRNA host genes** (41 and 15 in translation; 32 and 10 in
   ribosome biogenesis) are left out unless a host gene's protein does work in
   the step. Several are ribosomal proteins anyway, and are modelled there.

## Histone modification (PW:0001338, 173 genes)

No PW children and no GO process mapping (`no_specific_go_term`), because "histone
modification" names a class of reactions rather than a pathway. The HGNC groups
are enzyme and reader families: PHD finger (33), SET domain (24), histone lysine
methyltransferases (21), bromodomain (19), Tudor (12), sirtuins (7), arginine
methyltransferases (6), lysine acetyltransferases (6), chromobox (6),
ubiquitin-specific peptidases (6) and Polycomb group RING fingers (6).

A module per enzyme family would just restate the gene groups, so the proposal is
one module per complex or writer–eraser system, each a mechanism with its own GO
process:

1. **`polycomb_repressive_complexes`**: PRC2 (H3K27 methylation) and the canonical
   and variant PRC1 complexes (H2AK119 ubiquitylation). Analogue:
   `dmel_polycomb_group_complexes`.
2. **`compass_family_h3k4_methylation`**: SET1A/B and MLL1-4 COMPASS complexes.
   Analogue: `dmel_compass_family_complexes`.
3. **`histone_acetyltransferase_complexes`**: SAGA and ATAC (GCN5/PCAF), the
   MOZ/MORF and HBO1 complexes, and CBP/p300. TIP60 is already in
   `tip60_p400_complex`; reference it. Analogue:
   `dmel_gcn5_acetyltransferase_complexes`.
4. **`histone_deacetylation`**: class I HDAC complexes (Sin3, CoREST), class IIa
   HDACs, and the sirtuins that act on histones (SIRT1, SIRT6, SIRT7). NuRD is
   already `nurd_complex`; reference it.
5. **`histone_lysine_demethylation`**: LSD1/KDM1 and the JmjC KDM families,
   paired by the mark they erase.
6. **`histone_arginine_methylation`**: the PRMT family.
7. **Readers** (bromodomain, chromodomain, PHD, Tudor) are not a module of their
   own. A reader belongs to the complex that recruits it, and readers outside
   any modelled complex stay out.

Because the pathway has no specific GO process, each sub-module carries its own
process (for example histone H3K27 methylation) and cites PW:0001338 as evidence.

## Seeds that match only by gene overlap

- **Eukaryotic RNA polymerase transcription (PW:0001275).** Its children are the
  Pol I, II and III pathways. Pol I and III have modules; the Pol II plan above
  completes it. No separate module is needed.
- **Calcium/calcium-mediated signaling (PW:0001140).** Its RGD children are
  calcium/calmodulin-dependent signaling (no genes), CaSR signaling (modelled),
  and muscle contraction (no genes). Of its 90 directly annotated genes, 60 are in
  the ten calcium transport modules, `camkii_signaling`,
  `calcium_sensing_receptor_signaling` or `gpcr_plc_calcium_pkc_signaling`. The
  other 30 fall into three groups: EF-hand calcium sensors and buffers (CABP1/2/4,
  CALB2, S100A1/A4/B, KCNIP1-4, NCS1, RCVRN, GUCA1B, TNNC1/2, PVALB, OCM), the
  small-conductance calcium-activated potassium channels (KCNN1-4), and
  synaptotagmins 1/7/9, plus CALR, CASQ1, GUCA2B, CIMIP3 and SLC24A5. The SK
  channels would make a coherent small module (calcium-activated potassium
  conductance through calmodulin). The sensors and buffers are a family, not a
  pathway, and each belongs in the process it serves (troponin C in muscle
  contraction, recoverin and GCAPs in phototransduction), so the proposal is not
  to write a catch-all module. An index module of `module_ref`s would add nothing
  a reader cannot get from the project page.

## Suggested order

1. Pol II core and initiation, then Mediator: they unlock PW:0001275 and are well
   bounded.
2. Cytoplasmic ribosome, then translation initiation: the ribosome is referenced
   by three other plans.
3. Spliceosome cycle with snRNP biogenesis.
4. Polycomb and COMPASS, the best-characterised histone systems.
5. Ribosome biogenesis last: the largest and the most dependent on the others.

Each step is a tranche of about four to six modules, the same size as the
chromatin and calcium splits.
