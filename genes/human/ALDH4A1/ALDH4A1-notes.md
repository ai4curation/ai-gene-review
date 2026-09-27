# ALDH4A1 (P30038) review notes

Gene: ALDH4A1 (aka ALDH4, P5CDH). Human. UniProt P30038. 563 aa precursor;
N-terminal mitochondrial transit peptide (residues 1-24), mature chain 25-563.

## Core identity and function

ALDH4A1 is the **mitochondrial NAD+-dependent delta-1-pyrroline-5-carboxylate
dehydrogenase (P5CDH)**, an aldehyde dehydrogenase (ALDH superfamily, ALDH4
family). It catalyzes the **second (final) step of proline catabolism**:
oxidation of L-glutamate-5-semialdehyde (glutamate gamma-semialdehyde, GSA,
in spontaneous equilibrium with its cyclic tautomer delta-1-pyrroline-5-carboxylate,
P5C) to L-glutamate, using NAD+.

- EC 1.2.1.88 [file:human/ALDH4A1/ALDH4A1-uniprot.txt "EC=1.2.1.88"].
- Reaction [file:human/ALDH4A1/ALDH4A1-uniprot.txt
  "Reaction=L-glutamate 5-semialdehyde + NAD(+) + H2O = L-glutamate + NADH"].
- Function statement [file:human/ALDH4A1/ALDH4A1-uniprot.txt
  "Irreversible conversion of delta-1-pyrroline-5-carboxylate"] "(P5C), derived
  either from proline or ornithine, to glutamate. This is a necessary step in the
  pathway interconnecting the urea and tricarboxylic acid cycles."
- Pathway [file:human/ALDH4A1/ALDH4A1-uniprot.txt
  "Amino-acid degradation; L-proline degradation into L-"] "glutamate;
  L-glutamate from L-proline: step 2/2."
- Location [file:human/ALDH4A1/ALDH4A1-uniprot.txt "Mitochondrion matrix."].
- Homodimer [file:human/ALDH4A1/ALDH4A1-uniprot.txt "Homodimer."].

The substrate P5C/GSA is generated from proline by proline dehydrogenase (PRODH),
and from ornithine by ornithine aminotransferase; thus P5CDH sits at the node
interconnecting the urea and TCA cycles (glutamate is fed into central metabolism)
[PMID:22516612 "GSA is the hydrolysis product of Δ1-pyrroline-5-carboxylate (P5C),
which is generated from proline by proline dehydrogenase (PRODH)"; "GSA is also
produced from ornithine by ornithine aminotransferase"].

Cloning/characterization: two full-length human P5CDh cDNAs encode a 563-residue
protein; expression in P5CDh-deficient yeast confers P5CDH activity and growth on
proline [PMID:8621661 "a mitochondrial matrix NAD(+)-dependent dehydrogenase,
catalyzes the second step of the proline degradation pathway"; "Both conferred
measurable P5CDh activity and the ability to grow on proline as a sole nitrogen
source"]. (Note: this 1996 paper used the older EC 1.5.1.12; current EC is 1.2.1.88.)

## Dual substrate specificity: hydroxyproline catabolism

Human P5CDH is **also the second enzyme of hydroxyproline (4-Hyp) catabolism**.
By analogy to proline, trans-4-hydroxy-L-proline is oxidized to
1-pyrroline-3-hydroxy-5-carboxylate (3OH-P5C) by hydroxyproline oxidase; the
nonenzymatic hydrolysis product 4-hydroxyglutamate semialdehyde (OH-GSA) is then
oxidized by P5CDH to 4-erythro-hydroxy-L-glutamate (OH-Glu)
[PMID:22516612 "P5CDH is also the second enzyme of hydroxyproline catabolism in
humans"; "which is oxidized to 4-erythro-hydroxy-L-glutamate (OH-Glu) by P5CDH"].
The GO term GO:0003842 explicitly covers this dual activity ("The activity can also
oxidize other 1-pyrrolines, e.g. oxidation of 3-hydroxy-1-pyrroline-5-carboxylate to
4-hydroxyglutamate") per its OLS definition.

PMID:21998747 (Riedel et al. 2011) is primarily about HOGA1 (4-hydroxy-2-oxoglutarate
aldolase), the terminal enzyme of the 4-Hyp pathway, but its Figure 1 / pathway
description places 1P5CDH as the second of four mitochondrial 4-Hyp-degrading enzymes
[PMID:21998747 "the step-wise action of four mitochondrial enzymes: hydroxyproline
oxidase (HPOX), Δ1-pyrroline-5-carboxylate dehydrogenase (1P5CDH), aspartate
aminotransferase (AspAT), and 4-hydroxy-2-oxoglutarate aldolase (HOGA"]. This supports
GO:0019470 (trans-4-hydroxy-L-proline catabolic process) TAS for ALDH4A1.

## Structure and mechanism

First human P5CDH crystal structure solved by Srivastava et al. 2012 (PMID:22516612).
Classic ALDH fold: N-terminal NAD+-binding (Rossmann-like) domain, C-terminal
catalytic domain furnishing the essential cysteine nucleophile Cys348 and
substrate-binding Ser349, plus an oligomerization domain. Homodimer (domain-swapped),
~122 kDa in solution [PMID:22516612 "This domain furnishes the essential cysteine
nucleophile (Cys348) and several residues that bind GSA, including Ser349";
"The molar mass is estimated to be 122 kDa"]. Kinetics: Km(NAD+)=100 uM,
Km(L-P5C)=32 uM, kcat=10 s-1 for wild-type HsP5CDH.

Mechanism (general ALDH): nucleophilic attack by conserved Cys on the aldehyde C to
form a hemithioacetal, hydride transfer to NAD+ giving a thioacyl intermediate and
NADH, then hydrolysis to the carboxylic acid product.

## Disease: type II hyperprolinemia (HYRPRO2)

Autosomal recessive; deficiency of P5CDH causes accumulation of P5C and proline
[file:human/ALDH4A1/ALDH4A1-uniprot.txt "Hyperprolinemia 2 (HYRPRO2)"; PMID:22516612
"Type II hyperprolinemia is an autosomal recessive disorder caused by a deficiency
in Δ(1)-pyrroline-5-carboxylate dehydrogenase (P5CDH; also known as ALDH4A1)"].
The disease mutation S352L abolishes catalytic activity and eliminates NAD+ binding
by inducing an ~8 Å rearrangement of the catalytic loop [PMID:22516612 "Mutation of
Ser352 to Leu is shown to abolish catalytic activity and eliminate NAD(+) binding"].
S352L and variant P16L were originally reported by Geraghty et al. 1998
(PubMed:9700195; not in local publications cache).

## Localization evidence

- Mitochondrion matrix (UniProt subcellular location, and TAS from Reactome + Hu 1996)
  [file:human/ALDH4A1/ALDH4A1-uniprot.txt "Mitochondrion matrix."].
- Mitochondrion IDA from HPA (immunofluorescence, GO_REF:0000052).
- Mitochondrion HTP from PMID:34800366 (quantitative high-confidence human
  mitochondrial proteome). Abstract-only in cache; consistent with all other evidence.
All localization evidence is mutually consistent; mitochondrial matrix is the specific,
authoritative location.

## Protein interactions

- Homodimer / identical protein binding (GO:0042802), IPI PMID:22516612 (self;
  With/From UniProtKB:P30038) — supported by the structural + AUC data showing a dimer.
- protein binding (GO:0005515), IPI PMID:32814053 with UniProtKB:Q09028 (RBBP4).
  PMID:32814053 is a large-scale Y2H neurodegenerative-disease interactome map
  (abstract-only in cache; does not describe ALDH4A1 specifically). UniProt records the
  RBBP4 interaction [file:human/ALDH4A1/ALDH4A1-uniprot.txt
  "P30038; Q09028: RBBP4"]. Bare "protein binding" is uninformative and this is a
  single high-throughput Y2H hit with no known biological role for ALDH4A1; keep as
  non-core.

## Annotations to watch (over-annotation / generality)

- GO:0016491 oxidoreductase activity (IEA, InterPro): correct but a very general
  parent of the specific catalytic term; over-annotation relative to GO:0003842.
- GO:0004029 aldehyde dehydrogenase (NAD+) activity (IDA, CACAO from PMID:4015840):
  a more general ALDH-family MF. PMID:4015840 (Hopkinson et al. 1985) is a biochemical-
  genetic survey of ALDH isozymes; its abstract discusses ALDH1/ALDH2/ALDH3 and does
  not mention ALDH4/P5CDH. Full text unavailable in cache; cannot verify it assays
  ALDH4A1. Per policy (experimental IDA, do not REMOVE), keep the correct-but-general
  GO:0004029 as non-core and defer to the curator; the specific activity GO:0003842 is
  the core MF.
- GO:0005739 mitochondrion (IDA/HTP): correct but less specific than the
  mitochondrial matrix (GO:0005759) location.

## Core function summary

1. MF: L-glutamate gamma-semialdehyde / 1-pyrroline-5-carboxylate dehydrogenase
   activity, NAD+-dependent (GO:0003842, EC 1.2.1.88).
2. BP: L-proline catabolic process to L-glutamate (GO:0006562) — 2nd/final step.
3. BP: trans-4-hydroxy-L-proline catabolic process (GO:0019470) — dual substrate.
4. CC: mitochondrial matrix (GO:0005759).

---

## 2026-09-17 update: the proposed ALDH4A1-MPC moonlighting role

### The claim

Hsu et al. 2025 (Nat Cell Biol) propose that ALDH4A1 is a third, catalysis-independent
component of the mitochondrial pyruvate carrier
[PMID:40355545 "Here we show that ALDH4A1, a proline-metabolizing enzyme localized in
mitochondria, serves as a previously unrecognized MPC component maintaining pyruvate
mitochondrial import and the TCA cycle independently of its enzymatic activity."].

Lines of evidence in that paper:

1. Loss-of-function in cells: ALDH4A1 loss impairs pyruvate entry into mitochondria and
   TCA cycle entry.
2. Complex formation: co-immunoprecipitation, sequential co-IP and gel filtration are
   reported to show a trimeric ALDH4A1-MPC1-MPC2 species of ~88-100 kDa.
3. Reconstitution: 14C-pyruvate transport into proteoliposomes
   [PMID:40355545 "Remarkably, wild-type ALDH4A1 or ALDH4A1(S352L) could markedly enhance
   pyruvate transport into proteoliposomes by MPC1–MPC2"].
4. Catalysis-independence: S352L is the type II hyperprolinemia substitution that
   abolishes P5C dehydrogenase activity and NAD+ binding (PMID:22516612), and it behaves
   like wild type in the transport assay. Tumour suppression is likewise enzyme-independent
   [PMID:40355545 "Collectively, our findings suggest that ALDH4A1 displays
   tumour-suppressive activity in a manner independent of its enzymatic activity."].
5. Framing [PMID:40355545 "In summary, our study identifies ALDH4A1 as the third component
   of MPC complex critical for constituting an active MPC trimeric complex consisting of
   ALDH4A1, MPC1 and MPC2 for mitochondrial pyruvate import for TCA cycle entry in
   mammalian cells"].

### The counter-evidence, weighed carefully

Three independent 2025 cryo-EM analyses of human MPC resolve only MPC1 and MPC2:

- Liang et al., Nature [PMID:40101766 "MPC is a heterodimer consisting of MPC1 and MPC2,
  with the transmembrane domain adopting pseudo-C2 symmetry."] — six structures across
  IMS-open, occluded and matrix-facing states, i.e. a complete alternating-access cycle.
- He et al., Nature [PMID:40044865 "Our structures show that MPC1 and MPC2 form a
  heterodimer with the substrate translocation pathway at the center of the dimer
  interface, defining the basic functional unit and architecture of this important
  transporter family."].
- Sun et al., Nat Commun [PMID:40691140 "Structural analysis shows that the transport
  channel of MPC is formed by the interaction of transmembrane helix (TM) 1 and TM2 of
  MPC1 with TM2 and TM1 of MPC2, respectively."].

**Important caveat that limits how much these structures can refute.** All three were
determined from heterologously co-expressed, tagged MPC1 and MPC2 only
[PMID:40044865 "We found that co-expressing MPC1 and MPC2 in HEK293 cells yielded the best
outcome and decided to focus on human MPC, given its direct medical relevance."]
[PMID:40691140 "We co-expressed the full-length human MPC1 with a C-terminal Flag tag and
full-length human MPC2 with a C-terminal 6xHis tag in HEK293 GnTI– cells and purified the
protein complex with anti-Flag affinity resin and size exclusion chromatography (SEC)."].
ALDH4A1 was therefore never in the sample. Not seeing a subunit you did not put in is not
evidence that the subunit is absent in vivo. The honest statement of what these structures
do establish is narrower but still relevant: the pyruvate permeation pathway and its
conformational cycle are fully contained within the MPC1-MPC2 heterodimer, so ALDH4A1
cannot be part of the translocation path itself.

Two further points cut against the "third component" framing:

- The long-standing position, restated by He et al., is that MPC1 and MPC2
  [PMID:40044865 "are essential and sufficient to give rise to MPC activity"].
- Hsu et al.'s own reconstitution agrees: MPC1 and MPC2 transport pyruvate without ALDH4A1
  [PMID:40355545 "While MPC1 alone or MPC2 alone displayed basal activity towards pyruvate
  transport in vitro compared with control empty liposome, adding MPC1 and MPC2 together
  further enhanced pyruvate transport in proteoliposomes"]. ALDH4A1 raises that activity.
  An enhancer/stabiliser is a different claim from a constituent subunit.
- Topology and oligomeric state. MPC1/MPC2 are inner-membrane proteins; ALDH4A1 is a
  soluble matrix protein whose catalytic form is an obligate domain-swapped homodimer of
  ~122 kDa [PMID:22516612 "The molar mass is estimated to be 122 kDa"]. A 1:1:1 trimer of
  ~88-100 kDa implies monomeric ALDH4A1 in the complex, which is not addressed.

### Curation decision

**Recorded, not annotated.** No GO annotation is proposed for the MPC role, for three
reasons: (i) it is a single-laboratory result with no independent replication; (ii) the
paper's own data show MPC1+MPC2 transporting without ALDH4A1, so a "component of the
pyruvate carrier" CC assertion would overstate what was shown; (iii) an `involved_in`
mitochondrial pyruvate transport BP annotation cannot presently be separated from the
indirect possibility that losing P5C dehydrogenase from the matrix perturbs pyruvate flux
metabolically. The claim is instead captured as a `knowledge_gap`, in `suggested_questions`
and `suggested_experiments`, and in the top-level `description` as a statement about the
state of the biology; PMID:40355545 is marked `correctness: DISPUTED` with the reasoning
recorded in `review_notes`.

This should be revisited if the native complex is isolated from mitochondria with a defined
stoichiometry, or if the proteoliposome stimulation is independently reproduced.

## 2026-09-27 ClinGen campaign re-review

This entry supersedes the earlier action recommendations and the 2026-09-17 MPC
interpretation above; the historical text is retained as provenance. HGNC:406 is
Approved ALDH4A1, with previous symbol ALDH4 and alias P5CDh. The immutable record
is human UniProt P30038. Parent preflight and an independent byte comparison found
all five canonical files identical to main
`ba3ff58d7d2de76dbe3c24b16e05e12369f463fc`; canonical and both alias PR searches
were empty. All 17 seeded source objects and all three alternative products remain
unchanged. This is a full audit despite the previous COMPLETE label.

### Research and source access

The genuine Falcon request used a 1200-second timeout and the configured
perplexity-lite fallback, concurrently with normal publication caching. Both
provider commands failed during retrieval of `deep-research-client` from PyPI
because DNS could not resolve the host, before either research provider was
contacted. No provider report was created. The normal gene-publication command
reused all ten requested canonical PMID records. The terminal logs are
`/tmp/ALDH4A1-provider.log` and `/tmp/ALDH4A1-fetch.log`; they are local operational
receipts, not independent biological evidence. The manual research is recorded
here rather than impersonating a provider artifact.

The notes-inclusive census also found the historical `PubMed:9700195` citation
above. A normal `fetch-pmid 9700195` attempt failed with the URL/DNS error
`nodename nor servname provided, or not known` and produced no cache
(`/tmp/ALDH4A1-extra-fetch.log`). That historical source remains an explicit
notes-only cache gate; it is not newly used to support a decision. All ten PMID
references in the YAML and all three cited Reactome records are cached. The
review remains DRAFT pending recovery of this notes citation.

The canonical full papers read were PMID:22516612, PMID:21998747,
PMID:34800366, PMID:40355545, PMID:40044865 and PMID:40691140. The local records for
PMID:8621661, PMID:4015840, PMID:32814053 and PMID:40101766 are abstract-only;
the metadata flags retain those distinctions. For the interaction-screen design,
the original full PMID:32814053 was additionally read at the
[MDC accepted-paper route](https://edoc.mdc-berlin.de/id/eprint/19322/1/19322oa.pdf),
previously downloaded as `/tmp/ACTA1-PMID32814053.pdf`. This does not imply recovery
of its ALDH4A1-specific supplementary interaction entry. The Nature primary
[PMID:40355545 article](https://www.nature.com/articles/s41556-025-01651-8) agrees
with the cached full paper. These external checks were performed on 2026-09-27.

### Catalysis, localization and source-specific judgments

PMID:22516612 directly measures recombinant human GSA/NAD+ turnover and human
apo/mutant structures. Human equilibrium analytical ultracentrifugation gives a
122 kDa dimer estimate, in agreement with its domain-swapped crystal dimer. The
ligand complexes used to analyze substrate recognition are mouse P5CDH; the
hydroxylated-substrate accommodation in Figure S8 is a structural model. The paper
states established hydroxyproline-pathway activity, but does not newly measure
human hydroxylated-GSA turnover. The current reference finding and hydroxyproline
reason now make that distinction. PMID:21998747 is a HOGA1 study whose introduction
and pathway diagram place P5CDH in the four-enzyme mitochondrial pathway, not a
new P5CDH enzyme assay. The preserved TAS process is supported as catalytic pathway
participation, with the corresponding cached Reactome reaction as corroboration.

Broad mitochondrial annotations retain ACCEPT at their original source resolution.
The generic oxidoreductase MF is refined by MODIFY to the directly measured
GO:0003842 subtype; the broad class remains biologically correct. Separate matrix
annotations supply compartment precision. Human homodimeric self-association is an established property of the
core enzyme and is also ACCEPT, without creating a separate binding core.
The live [HPA subcellular page](https://www.proteinatlas.org/ENSG00000159423-ALDH4A1/subcellular)
reports supported mitochondrial staining in HaCaT and Hep-G2 cells and cytosolic
staining in A-431. The mitochondrial HTP paper has cached full text; its exact
ALDH4A1 supplementary row was not independently recovered. Its broad curated
assignment is retained with independent localization support, not a claim that
all organellar assignments were individually remeasured in this audit.

The original [CACAO/GONUTS annotation record](https://gowiki.tamu.edu/wiki/index.php/HUMAN:AL4A1)
traces the broad NAD+-aldehyde-dehydrogenase assignment to CACAO8806 and Table 1 of
[PMID:4015840](https://gowiki.tamu.edu/wiki/index.php/PMID:4015840), with agar-overlay
staining using propionaldehyde or benzaldehyde. The full Table 1 was not recovered.
The abstract's emphasis on other ALDH forms therefore does not establish a wrong
protein assignment. The curated broad function is biologically sound; MODIFY refines it to the
independently measured human P5CDH reaction. This refinement does not claim that
the unread original table assayed GSA. The detailed original substrate assay
remains curator-deferred rather than independently verified.

The generic GO:0005515 record is REMOVE as uninformative, not because the
ALDH4A1-RBBP4 interaction is disproven. The immutable UniProt record lists three
experiments; the original screen performs repeated screens and pairwise retests.
The exact supplementary pair and a mechanistic RBBP4-dependent ALDH4A1 activity
remain unverified. No specific adaptor or scaffold function is substituted.

For propagation, PTN002684348 is the sole IBA source entity. Human self-evidence
is legitimate descendant grounding. The PAINT tree/node placement, ARBA internal
conditions and missing live InterPro entries were not reconstructed; their source
reviews explicitly retain UNRESOLVED internals where appropriate. Positive target
judgments rely on the independently established human reaction and location, not
fabricated verification of automated rules. The source mappings to EC:1.2.1.88,
RHEA:30235 and SL-0170 are consistent with the immutable human record.

### Accessory MPC activation: positive evidence and NEW audit

The current decision adds one source-specific IDA proposal for GO:0141109
transporter activator activity. It does not add a transport-process annotation,
a pyruvate-carrier molecular function or an obligate third-subunit complex term.
ALDH4A1 performs the proposed regulatory work by binding the carrier and enhancing
its measured transport. This assignment does not rest on knockout necessity.

PMID:40355545 Figure 5 reports binding of recombinant ALDH4A1 to MPC1 and MPC2,
with human-cell association and interaction-defective deletion/rescue experiments.
The deletion of residues 182–199 loses MPC association and pyruvate-import rescue
while retaining the measured cellular proline-regulation phenotype; this is not a
complete purified-enzyme kinetic characterization of that deletion. Figure 6 and
Extended Data Figure 8 report enhanced MPC association/oligomerization with added
ALDH4A1. Figure 7 compares empty proteoliposomes, individual MPC subunits,
MPC1+MPC2, and MPC1+MPC2 with WT or catalytic S352L ALDH4A1. MPC1+MPC2 already
transports; added WT or S352L increases transport over time. The source explicitly
states [PMID:40355545, Results, "In vitro binding assay demonstrated the direct
interaction of ALDH4A1 with both MPC1 and MPC2"] and [PMID:40355545, Results,
"Either wild-type ALDH4A1 or mutant ALDH4A1(S352L) further enhanced pyruvate
transport by MPC1–MPC2 in a time-dependent manner compared with MPC1–MPC2"].

The reconstitution Methods use purified recombinant proteins, phosphatidylcholine
and cardiolipin, detergent removal and radiolabeled uptake/filter washing. The
recovered description does not provide an ALDH4A1-alone transport arm. It also
does not settle matched incorporated MPC amount/orientation for every comparison,
or distinguish stabilization during reconstitution from an increase in turnover
per incorporated carrier. Thus the evidence supports a transporter-activating
contribution but does not establish standalone carrier activity or a universal
native stoichiometry. The paper's gel filtration, crosslinking and native-gel data
are positive complex evidence; the previously stated requirement for any native
isolation is outdated. Those data still do not quantify a unique native 1:1:1
stoichiometry. A peer independently read these Results/Methods and reached the
same bounded interpretation.

The live [GO:0141109 definition and parents](https://amigo.geneontology.org/amigo/term/GO:0141109)
were checked on 2026-09-27. The definition requires binding and increased
transporter activity; its is_a parents are transporter regulator activity and
molecular function activator activity. It is not a carrier-activity assertion.
The proposed term is not an ancestor or descendant of any retained seeded term,
and there is no second NEW term. The target accession/name search of the cached
`gocams/index.tsv` found no ALDH4A1/P30038 activity; it therefore supplied no
existing target model to resolve or contradict this role.

The comparator check considered transporter-associated proteins whose regulatory
role is distinct from substrate translocation. Primary UniProt annotation displays
show the same term on rat [Pdzk1/Q9JJ40](https://www.uniprot.org/uniprotkb/Q9JJ40/entry)
(source RGD), mouse [Cltrn/Q9ESG4](https://www.uniprot.org/uniprotkb/Q9ESG4)
(source GO_Central), and rat [Atp1b2/P13638](https://www.uniprot.org/uniprotkb/P13638/entry)
(source RGD). Their roles span a binding scaffold, a carrier-binding trafficking/
activity regulator, and a noncatalytic pump partner. They establish that GO uses
this MF for transporter-associated regulatory proteins; they do not transfer
those proteins' particular mechanisms to ALDH4A1. These were annotation-display
checks, not independent re-reviews of every donor experiment or exact evidence
chain. Local authored NEW proposals in other reviews were not treated as curated
comparator assertions. QuickGO API requests did not yield an independently
usable annotation export, so no comprehensive species-wide absence claim is made.

The MPC1-MPC2 structural papers constrain the translocation pathway to the
heterodimer. They do not refute accessory regulation. Co-expression of two tagged
subunits does not prove that endogenous host ALDH4A1 could never be present;
the previous categorical sample-exclusion sentence is withdrawn. PMID:40044865
and PMID:40691140 full Methods were read; PMID:40101766 remains limited to its
primary abstract/publisher record. PMID:40355545 is VERIFIED for the bounded
binding/activation claim, rather than DISPUTED merely for lacking an independent
replication. Native occupancy, stoichiometry, physiological distribution and the
precise activation mechanism remain explicit questions. The newer activity is
kept outside the integrated defining P5CDH catalytic core at this stage.

The current 18-entry review has 14 ACCEPT, two enzyme-specificity MODIFY actions,
one generic-binding REMOVE and one NEW. The catalytic core integrates proline and hydroxyproline degradation under
the same enzyme MF in the matrix. No second broad core duplicates that chemistry.

Validation note: live AmiGO labels GO:0003842 with an explicit `(NAD+)` suffix,
whereas the repository validator expects the shorter name already present in
the source snapshot. Authored labels use the validator-compatible name for the
same term ID; NAD+ chemistry remains explicit in the prose. No source term ID or
label was changed.

Final checks: targeted gene validation and rendering passed. All 35 attached
quotations matched the canonical sources under whitespace normalization. The
17 seeded source objects, 18 original reference identity/title pairs, three
alternative products, UniProt and GOA bytes were preserved. Parent independent
review accepted the biological decisions after the two enzyme-specificity
refinements and added core matrix evidence. The YAML validator has no curation
warnings; DRAFT is retained for the notes-only PMID:9700195 cache gate.


## 2026-09-27 source6 cache recovery

This entry supersedes the earlier PMID:9700195 cache gate. The source6 normal-fetch record was imported unchanged after archive/run and exact-byte verification; its SHA256 `aab24fdf9bae81f8c5361c73c65dc03a8a0b1f36d3b819ebc5a9853312aa9895` and Git blob `c3e6aee5591fcbf1f046e1469b8ebe4db25a6773` match `tmp/source6-canonical-import-receipt.json`. Before editing, all five local canonical gene files were matched to published PR #3271 head `8b86954c33fecbad3810eea861a2db0749e01c9d` through GitHub blob IDs.

The recovered **abstract**, not a full paper, was read. PMID:9700195 reports variants identified in four people and tests human P5CDH constructs in a deficient *Saccharomyces cerevisiae* strain. Wild-type human enzyme restores activity and growth on proline; S352L and G521fs(+1) do not. P16L produces functional enzyme and is interpreted as a population polymorphism. This corroborates the existing S352L catalytic-loss interpretation without converting the heterologous yeast host into a direct human-cell assay, generalizing inactivity to P16L, or changing the independently assessed MPC-regulatory evidence. No functional action, core, source assertion or reference identity is changed.

The recursive citation census covered all non-derived gene files and links, with the HTML treated as a derived duplicate. There is no provider or hypothesis report and no nested PDF artifact. The author-PDF link `https://edoc.mdc-berlin.de/id/eprint/19322/1/19322oa.pdf` is explicitly linked to the already cached PMID:32814053; it creates no separate unidentified source. All **11 PMIDs used by the authored review and notes as evidence/context** are now cached, as are the three authored Reactome reaction references. Fifteen normalized DOI strings were checked against publication metadata or the paired PMID/DOI in the immutable UniProt record. Six absent raw-UniProt bibliography records remain unused by the review: PMID:1395511, PMID:1286669, PMID:8493898, PMID:23186163, PMID:24275569 and PMID:25944712. They concern historical protein characterization or broad proteomics, but no reviewed assertion depends on their uninspected results. They remain inventoried raw-source provenance, rather than new evidence claims or completion gates. All raw Reactome cross-references are cached. Current-main presence checks were made at `30a9290881824baaacab2b681d7808f572c4cef6`; the newly recovered PMID:9700195 is explicitly included in this follow-up manifest.

The sole missing required cache is therefore resolved. Status is changed to COMPLETE subject to the final warning-free schema, ontology, reference and best-practices validation. All 17 seeded source objects, the one prior NEW assertion, all 18 decisions, the integrated catalytic core, three alternative products and protected UniProt/GOA bytes remain unchanged. No additional provider attempt, scientific claim or new annotation is introduced by this bounded follow-up. The earlier genuine provider/fetch failures remain historical provenance.

Final source6 follow-up checks: full gene validation passed with no curation warnings; all 35 case-sensitive source quotes and all preserved source/isoform/reference/core objects passed. COMPLETE records the closed cache gate and successful validation, without claiming that the open mechanistic questions have been experimentally resolved.
