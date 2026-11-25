# Hes6 (mouse, Q9JHE6) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: mouse Hes6 is reviewed as the experimentally characterised reference for
the PANTHER PTHR10985:SF11 (TRANSCRIPTION COFACTOR HES-6) subfamily, which also
holds human HES6 (Q96HZ4), zebrafish hes6/her13.2 (Q6P0J1) and her13 (Q568A5).
No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon mouse Hes6 --fallback perplexity-lite` failed: falcon
returned "Edison API request failed: Failed to authenticate" (HTTP 403) and the
perplexity-lite fallback returned HTTP 401 "insufficient_quota". No deep-research
file exists. The review is built from primary literature cached in
`publications/` (PubMed search "Hes6[tiab]", 160 hits; mouse/mammalian
mechanistic papers fetched with `just fetch-pmid`).

### Evolutionary grounding

- UniProt Q9JHE6 carries PANTHER PTHR10985 (HES-related bHLH family). The
  subfamily placement PTHR10985:SF11 and pairwise identities were computed in
  `genes/DANRE/hes6/hes6-bioinformatics/RESULTS-rereview.md` (mouse vs human
  HES6 0.857 identity; vs zebrafish hes6 0.562; HES1, a different subfamily,
  about 0.36 to the zebrafish protein). All SF11 members end in WRPW.
- PAINT nodes reaching mouse Hes6 (`interpro/panther/PTHR10985/PTHR10985-paint.tsv`):
  PTN004213585 (eukaryote-level HES/HEY node: nucleus, GO:0000978, GO:0000981,
  GO:0000122; mouse Hes6 MGI:1859852 is itself a seed for GO:0000981 and
  GO:0000122) and PTN000105428 (GO:0009952 A/P pattern specification and
  GO:0050767 regulation of neurogenesis; mouse Hes6 is not a seed; zebrafish
  hes6 ZDB-GENE-030828-5 is a seed for GO:0009952). A NOT IRD for GO:0050767
  sits at PTN000105659 (taxon 9347), a different branch.
- The ISO homo/heterodimerization rows (PMID:11076679) come from chicken HES1
  (O57337, HES1_CHICK), a protein in a different PTHR10985 subfamily. The terms
  are nevertheless supported directly in mouse (below).

### What is experimentally established for mouse Hes6

1. Hes1 antagonist / transcription regulator inhibitor. Mouse Hes6 binds Hes1,
   "Hes6 alone does not bind to the DNA but suppresses Hes1 from repressing
   transcription", and relieves Hes1 inhibition of Mash1-E47 [PMID:10851137].
   Hes6 "inhibits the interaction of Hes1 with its transcriptional corepressor
   Gro/TLE. Moreover, it promotes proteolytic degradation of Hes1" [PMID:12972610].
   Sumoylation at K27/K30 modulates stability and derepression of Hes1 targets
   [PMID:26435136].
2. Dimerization. "Hes6 preferentially forms homodimers"; heterodimerization with
   Hes1 is restrained by an N-terminal acidic patch [PMID:17868320].
3. Groucho/TLE binding via WRPW and repression when tethered. Mouse HES6 (clone
   "identical to the published mouse HES6 cDNA but lacks the first 16 amino
   acids") "interacted with the corepressor transducin-like Enhancer of split 1
   in yeast and mammalian cells through its WRPW COOH-terminal motif" and
   "repressed transcription from an N box-containing template and also when
   tethered to DNA through the GAL4 DNA binding domain" [PMID:11551980].
4. DNA binding: contested. Bae 2000 reports no autonomous DNA binding
   [PMID:10851137]; Cossins 2002 reports ESE E-box binding and repression of an
   ESE reporter [PMID:11959828]; Gao 2001 infers N-box binding from a HES6-VP16
   reporter [PMID:11551980]; human HES6 has an HT-SELEX IDA (PMID:28473536,
   ARUK-UCL, source of the ISO GO:1990837 row). Crucially, the neural and
   myogenic activities do NOT require the basic DNA-binding arm
   [PMID:17065448; PMID:11959828; Xenopus PMID:22114720]. Zebrafish data show
   Hes6 homodimers bind weakly while Her7:Hes6 heterodimers bind strongly
   (family review PTHR10985). I keep DNA-binding terms as non-core.
5. Cortical neurogenesis / gliogenesis. Hes6 promotes cortical neuron
   differentiation [PMID:12972610]; knockdown makes progenitors adopt astrocytic
   fate and overexpression suppresses astrocyte differentiation, with separable
   mechanisms [PMID:17065448; PMID:17868320]. Retroviral misexpression in retina
   promotes rod differentiation [PMID:10851137]. Interacts with RelA-NF-kB in
   cortical progenitors [PMID:23689134, abstract only].
6. Myogenesis: conflicting overexpression results (Gao: induces
   differentiation via MyoR repression [PMID:11551980]; Cossins: impairs C2C12
   differentiation [PMID:11959828]); knockdown leaves differentiation markers
   intact but disrupts F-actin, motility and fusion [PMID:21501606].
   Hes6 is a direct MyoD/Myf5 target.
7. Loss of function in vivo: Hes6-null mice (tau-lacZ/lacZ replacement) show no
   detectable inner-ear defect, "similar to observations in other tissues"
   [PMID:16534784]; adult dentate gyrus shows reduced DCX+ neuroblasts but no
   proliferation or integration defect [PMID:26105991]. So Hes6 is largely
   dispensable in vivo; most functional data are gain-of-function or knockdown
   in culture.
8. Expression: induced by proneural bHLH proteins, not by Notch
   [PMID:10976052]; downstream of Math1 in inner-ear hair cells [PMID:16534784];
   embryonic nervous system, myotome, thymus, epithelia [PMID:10906477;
   PMID:11044617].
9. Peripheral reports: hepatic Pparg2 repression (adenoviral overexpression /
   shRNA in mouse liver) [PMID:29404444]; circadian LDLR promoter repression in
   HepG2 [PMID:22913986]; CBP/PML body interaction [PMID:18160400, abstract
   only]; WRPW acts as a proteasomal degron [PMID:15896295]. Not used for GO
   terms.

### Decisions

- Core MF: GO:0140416 transcription regulator inhibitor activity (Hes1
  antagonism), GO:0061629 binding Hes1, GO:0046982/GO:0042803 dimerization.
  NEW: GO:0001222 transcription corepressor binding (TLE1 via WRPW, mouse
  HES6, PMID:11551980).
- Core BP: positive regulation of neuron differentiation (MODIFY from nervous
  system development IMP), positive regulation of neurogenesis (MODIFY from
  IBA regulation of neurogenesis). NEW: GO:0048712 negative regulation of
  astrocyte differentiation (PMID:17065448 knockdown + overexpression; Hes6 is a
  nuclear transcription regulator acting in the progenitor itself, so this is a
  regulatory role, not a downstream phenotype).
- A/P pattern specification IBA: MARK_AS_OVER_ANNOTATED; no mouse evidence and
  Hes6-null mice are without reported patterning defects; the segmentation-clock
  role is established only for zebrafish hes6 (Her7:Hes6 heterodimer).
- For transfer to zebrafish hes6: transferable with confidence = Hes1/Hairy
  antagonism through heterodimerization, Groucho/TLE binding (WRPW conserved),
  nuclear location. Not transferable without care = DNA-binding repressor
  activity (contested in mouse, partner-dependent in fish).
