# ALAS2 (human) — review notes

UniProtKB: P22557 (HEM0_HUMAN). Gene: ALAS2 (HGNC:397; synonyms ALASE, ASB). X chromosome (Xp11.21).
EC 2.3.1.37. Belongs to the class-II PLP-dependent aminotransferase family.

## Core biology (grounded in ALAS2-uniprot.txt + cached publications)

- ALAS2 is the **erythroid-specific 5-aminolevulinate synthase**, the **first and rate-limiting
  enzyme of heme biosynthesis** in erythroid cells.
  [PMID:32499479 "The first and rate-limiting step is carried out by 5′-aminolevulinate synthase (ALAS; EC 2.3.1.37) in the mitochondria"]
  [PMID:34492704 "itaconyl-CoA is a competitive inhibitor of the erythroid-specific 5-aminolevulinate synthase (ALAS2), the first and rate-limiting step in heme synthesis"]
- Catalyses the **PLP-dependent condensation of succinyl-CoA and glycine to form aminolevulinic acid
  (ALA), with CoA and CO2 as by-products.**
  [file:human/ALAS2/ALAS2-uniprot.txt "Catalyzes the pyridoxal 5'-phosphate (PLP)-dependent condensation of succinyl-CoA and glycine to form aminolevulinic acid (ALA), with CoA and CO2 as by-products"]
  [PMID:32499479 "ALAS catalyses the pyridoxal 5′-phosphate (PLP)-dependent condensation of succinyl-CoA and glycine to form aminolevulinic acid (ALA), with CoA and CO2 as by-products"]
  Rhea:RHEA:12921; EC=2.3.1.37.
- ALAS2 is **PLP-dependent**; PLP is covalently attached to active-site Lys391 as an internal aldimine
  [PMID:32499479 "PLP is covalently attached to the active site lysine (Lys391 in human ALAS2 (hsALAS2)) as an internal aldimine adduct"].
  UniProt: MOD_RES 391 N6-(pyridoxal phosphate)lysine; COFACTOR pyridoxal 5'-phosphate.
- Two isozymes: ALAS1 (housekeeping/ubiquitous, 3p21.2) and ALAS2 (erythroid, Xp11.21).
  [PMID:32499479 "ALAS1 (gene location 3p21.2) is the housekeeping enzyme ... ALAS2 (gene location Xp11.21) is predominantly expressed in erythroid progenitor cells, and synthesizes 85–90% of total body heme specifically for hemoglobin production during erythropoiesis"]
- **Homodimer** (obligate; each active site formed from both subunits).
  [PMID:32499479 "Like its orthologs, hsALAS2 is an obligate homodimer in that each active site is formed from both monomeric subunits, with one PLP molecule bound per active site"]
- **Localization: mitochondrion.** UniProt SUBCELLULAR LOCATION = Mitochondrion inner membrane,
  peripheral membrane protein; localizes to the **matrix side** of the inner membrane.
  [file:human/ALAS2/ALAS2-uniprot.txt "Localizes to the matrix side of the mitochondrion inner membrane"]
  Reactome (R-HSA-189442) and InterPro place it in the mitochondrial matrix. The N-terminal 49-aa
  transit peptide targets the protein to mitochondria.
- **Regulation:** IRE in the 5'UTR couples translation to iron availability
  [PMID:2050125 "An iron-responsive element (IRE) motif has been identified in the 5'-untranslated region of the human erythroid ALAS mRNA"];
  protein stabilized by hypoxia / proteasome inhibition (LXXLAP prolyl-hydroxylation/vHL pathway)
  [PMID:16234850 "Hypoxia (1% O2) and inhibition of the proteasome increased both the stability and the specific activity of ALAS2"];
  competitively inhibited by itaconyl-CoA [PMID:34492704]; C-terminal autoinhibitory loop
  [PMID:32499479 "C-terminus is a self-inhibitory loop"].
- **Interactions:** SUCLA2 (β subunit of ATP-specific succinyl-CoA synthetase; UniProt Q9P2R7) —
  physiologically meaningful (channels/supplies succinyl-CoA).
  [PMID:10727444 "mitochodrially expressed SCS-betaA associates specifically with ALAS-E and not with ALAS-N"]
  BANP (Q8N9N5) from a large-scale Y2H interactome map [PMID:25416956] — not functionally characterized.

## Disease
- Loss-of-function missense mutations → **X-linked sideroblastic anemia (XLSA / SIDBA1, MIM 300751)**;
  many characterized in vitro to reduce enzyme activity (K156E [PMID:21252495]; 10 missense in
  [PMID:21309041]).
- C-terminal frameshift/deletion **gain-of-function** mutations → **X-linked (dominant) protoporphyria
  (XLDPT/XLDPP, MIM 300752)**; can also aggravate other erythropoietic disorders (e.g. CEP modifier,
  Y586F [PMID:21653323]).

## GOA MF term
- GOA carries **GO:0003870 5-aminolevulinate synthase activity** (verified in ALAS2-goa.tsv).
  This is the exact current term; used for core_functions molecular_function.

## Annotation review disposition summary
- MF 5-aminolevulinate synthase activity (GO:0003870): core; multiple EXP/IDA/IMP + IBA/IEA → ACCEPT.
- BP heme biosynthetic process (GO:0006783): core; ACCEPT (IBA/IEA/ISS/NAS).
- BP heme B biosynthetic process (GO:0006785, IDA): more specific; ACCEPT (heme b is the product of the pathway ALAS2 initiates).
- CC mitochondrion / mitochondrial matrix / mitochondrial inner membrane: ACCEPT (matrix is most informative; IMM is where it sits peripherally on the matrix side).
- BP hemoglobin biosynthetic process (GO:0042541): keep as non-core (downstream physiological role; heme feeds hemoglobin).
- BP erythrocyte differentiation (GO:0030218): keep as non-core (heme flux governs erythroid maturation).
- BP protein binding (GO:0005515, IPI): uninformative MF term → MARK_AS_OVER_ANNOTATED (SUCLA2, BANP, vHL interactions are real but the bare term adds nothing).
- MF transferase activity (GO:0016740, IEA InterPro): too general vs the specific acyltransferase → MODIFY to GO:0003870.
- BP porphyrin-containing compound metabolic process (GO:0006778) / tetrapyrrole biosynthetic process (GO:0033014): broad IEA parents of heme biosynthesis → ACCEPT (correct but general).
- MF pyridoxal phosphate binding (GO:0030170): secondary MF, correct cofactor → ACCEPT.
- BP intracellular iron ion homeostasis (GO:0006879, ISS): mark as non-core (ALAS2 consumes iron pathway indirectly via heme; ISS from ALAS1 ortholog); KEEP_AS_NON_CORE.
- BP response to hypoxia (GO:0001666, IDA) / intracellular oxygen homeostasis (GO:0032364, NAS): O2-dependent stability regulation from PMID:16234850 → KEEP_AS_NON_CORE (regulatory response, not core catalytic function).

## 2026-09-27 — ClinGen Mendelian campaign re-review

This dated audit supersedes the disposition and mechanistic wording in the earlier
notes above; the earlier journal entry is retained as history. All 40 seeded
assertions, qualifiers and reference identities were preserved. The approved
symbol is ALAS2 (HGNC:397), UniProt P22557; ALAS-E / ALASE and the previous symbol
ASB were checked separately for directory and open-PR overlap. The coordinator
verified all five canonical files against main
`c7078166039c9abd5c62704489283403eb520007`; no overlapping PR was found.

The review and annotation-reviewer workflows were applied to every annotation,
all references and the core synthesis. A peer independently checked the two
oxygen/localization papers; the coordinator independently reviewed the final
biology. Exact local preflight hashes are in `/tmp/ALAS2-root-baseline.json` and
the final publication manifest records the changed-file hashes.

### Primary evidence and source boundaries

- The full cached human structure/kinetics study [PMID:32499479] supports the
  PLP-dependent reaction, homodimeric active sites and C-terminal regulation.
  Its structural constructs include human residues 79–587 and 143–587 expressed
  in insect cells, with additional bacterial expression for kinetics/mutagenesis.
  PLP binding belongs within the catalytic core, not in a second redundant core.
- [PMID:34492704] was read in its cached main full text. It reports recombinant
  ALAS2 inhibition and mouse erythroleukemia/macrophage experiments, including
  human ALAS2 overexpression in mouse cells. Detailed recombinant constructs
  remain in unrecovered supplementary Methods. Itaconyl-CoA inhibits ALAS2;
  it is not established as an alternative substrate. No claim of direct human
  erythroblast or patient testing is inferred from these experiments.
- Full publisher [PMID:10727444](https://www.jci.org/articles/view/6816) was read
  on 2026-09-27: Methods use mature human ALAS2 bait (residues 54–587) and human
  SUCLA2 in yeast, then tagged human proteins in CHO mitochondrial preparations.
  Physical association is established. The paper proposes efficient substrate
  use or import assistance; it does not demonstrate succinyl-CoA channeling.
  This corrects the categorical channeling statement in the earlier notes.
- [PMID:14643893](https://pubmed.ncbi.nlm.nih.gov/14643893/) remains locally
  abstract-only; a publisher preview was also read at
  [DOI 10.1016/s1357-2725(03)00246-2](https://www.sciencedirect.com/science/article/pii/S1357272503002462).
  It directly reports functional exon-4-skipped ALAS2, retained SUCLA2 binding
  and import dependent on the first 49 residues. Import across the inner
  membrane is not itself a membrane-residency assay. The seeded inner-membrane
  IDA is nevertheless retained by explicit curator deference to the established
  UniProt peripheral/matrix-face localization. Cached GO-CAM
  `67369e7600001710` repeats that PMID for the location; it is not an independent
  experimental confirmation. The question of the exact attachment assay remains.
- [PMID:16234850](https://pubmed.ncbi.nlm.nih.gov/16234850/) was independently
  verified from its primary abstract, but full Results/Methods were not
  recovered. K562 hypoxia, proteasome inhibition, proline-mutant stabilization,
  normoxic vHL co-immunoprecipitation and ubiquitination concern regulated ALAS2.
  The proposed hydroxylase pathway does not directly establish ALAS2
  hydroxylation or an oxygen-sensor function. The IDA response-to-hypoxia remains
  non-core. Intracellular oxygen homeostasis, GO:0032364, requires maintaining
  intracellular oxygen levels, so that NAS assertion is UNDECIDED pending the
  full source rather than being retained on the basis of a different observation.
- The human mutation studies [PMID:21252495], [PMID:21309041] and
  [PMID:21653323] were read at cached primary-abstract scope. Their actual
  enzyme assays support the activity. The ten-variant study does not show the
  same defect for every variant, and Y586F was assessed as a modifier of
  UROS-associated congenital erythropoietic porphyria. The IRE/promoter paper
  [PMID:2050125] is not treated as a direct assay of lineage specification.
- Cached full main texts [PMID:25416956] and [PMID:34800366] establish their
  interaction-map and MitoCoP designs, respectively. The exact ALAS2-BANP
  supplementary pair and ALAS2-specific MitoCoP entry were not independently
  recovered. No negative interaction result or contamination conclusion follows.
  Broad mitochondrial HTP remains ACCEPT with independent human localization.

### Transfer provenance and process scope

The actual ISS/Compara donor is **mouse Alas2 P08680**, not an ALAS1 ortholog.
The primary [UniProt donor record](https://www.uniprot.org/uniprotkb/P08680/entry)
and [MGI comparative graph](https://www.informatics.jax.org/homology/GOGraph/Alas2)
were read on 2026-09-27. The graph explicitly records its generation date as
2023-03-10; it is historical evidence provenance, not a freshly generated graph.
It links mouse heme synthesis, hemoglobin synthesis and erythrocyte
differentiation to IMP [PMID:9446639], and intracellular iron homeostasis to
IMP [PMID:10562540] with allele MGI:2180151.

[PMID:9446639](https://pubmed.ncbi.nlm.nih.gov/9446639/) was verified from the
primary abstract: mouse Alas2 disruption leaves early erythroid markers while
reducing heme, globin and hemoglobinized cells. Its full source was not recovered.
For [PMID:10562540](https://pubmed.ncbi.nlm.nih.gov/10562540/), the primary abstract
and then the [author-uploaded full original](https://www.researchgate.net/publication/12737746_Heme_deficiency_in_erythroid_lineage_causes_differentiation_arrest_and_cytoplasmic_iron_overload)
were read. Figure 4 distinguishes embryonic cytoplasmic iron deposits from
adult-chimera ring sideroblasts. Table II directly quantifies approximately
threefold higher iron per cell in null E10.5 embryos, not higher total iron per
embryo. Discussion leaves the intervening iron-import mechanism unresolved.
Thus iron homeostasis and late differentiation remain contextual NON_CORE
annotations; ALAS2 is not assigned iron transport or lineage transcription.

Live [GO:0042541](https://flybase.org/cgi-bin/cvreport.pl?childdepth=2&cvterm=GO%3A0042541)
includes pathways producing hemoglobin with its heme groups. ALAS2 catalyzes an
actual step in producing that component, a defining erythroid specialization.
The three seeded hemoglobin-biosynthesis assertions are ACCEPT. They do not
require that ALAS2 translate globin or assemble the final protein. The integrated
core covers heme B and hemoglobin biosynthesis using the same catalytic unit.
Live [GO:0032364](https://amigo.geneontology.org/amigo/term/GO%3A0032364) distinguishes
oxygen steady-state maintenance from oxygen-dependent stability.

IBA reviews preserve ancestral nodes PTN000343737 / PTN000343740 alone in
`source_entities`. The PAINT tree/MSA was not re-executed. The target's own
experimental evidence is legitimate descendant support, not circularity.
InterPro, EC, Rhea, UniProt subcellular mapping and the mouse ortholog sources
are separately described; ARBA00034153 internals remain UNRESOLVED while direct
human evidence establishes the target reaction. Cached human GO-CAM
`67369e7600001710` includes ALAS2 synthase activity and its heme B pathway role.
No NEW annotation is proposed; the existing catalytic/process coverage suffices.

The four generic GO:0005515 annotations now use REMOVE under the explicit
annotation-reviewer policy, replacing the earlier prohibited OVER decisions.
This removes an uninformative term, not the experimentally reported SUCLA2/vHL
associations or the unresolved BANP pair. No specific adaptor, substrate
channeling or regulatory MF is manufactured from binding alone.

### Research attempts and cache gates

Publication caching and default Falcon research were launched concurrently.
`just fetch-gene-pmids human ALAS2` succeeded, finding all 11 original records
already cached (`/tmp/ALAS2-fetch.log`); those bytes were preserved. The first
provider invocation inherited offline mode and could not resolve its uncached
client. A normal network-enabled attempt with a 1200-second timeout and
`--fallback perplexity-lite` was then made. Both client launches failed before
provider contact because PyPI DNS lookup failed (`/tmp/ALAS2-provider-online.log`).
No provider report was created, and these notes are manual research.

The two genuinely traced donor papers were requested normally using
`just fetch-pmid 10562540 9446639`. Both failed DNS; no records were fabricated
(`/tmp/ALAS2-donor-fetch.log`). Their verified primary identities/access routes
are recorded separately from cache availability. The notes-inclusive census is
13 PMIDs with exactly these two missing caches, plus one already-cached
Reactome record, R-HSA-189442. The review remains DRAFT pending those cache gates
after completed validation. No immutable source or prior history was edited.

Final checks: `just validate human ALAS2` passed with one aggregate warning
covering the two missing PMID caches; `just validate-history` and `just render`
passed. All 40 source objects, four alternative products and 19 original
reference identity pairs were asserted unchanged. Final actions are 29 ACCEPT,
five KEEP_AS_NON_CORE, four REMOVE, one MODIFY and one UNDECIDED. The multiline
UniProt matrix-face/peripheral quote was checked against exact source bytes.
