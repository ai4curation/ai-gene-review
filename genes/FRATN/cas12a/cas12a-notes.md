# FnCas12a (Cpf1), *Francisella tularensis* subsp. *novicida* U112 — curation notes

UniProt A0Q7Q2 (CS12A_FRATN), 1300 aa, reviewed. Locus FTN_1397. Type V-A CRISPR-Cas system.
EC numbers assigned by UniProt: **3.1.21.1** and **4.6.1.22**, both with experimental evidence
`ECO:0000269|PubMed:28431230`.

No deep-research provider was available in this environment (no OpenAI/Perplexity keys), so this
file is the research journal. All assertions carry inline provenance from cached publications in
`publications/`.

## 1. What the protein is

FnCas12a is the single-protein effector of a class 2, type V-A CRISPR-Cas system. It is the
founding Cpf1 ortholog: the system was first shown to be a functional defence system in
[PMID:26422227 "Here we show that Cpf1-containing CRISPR-Cas loci of Francisella tularensis subsp.
novicida U112 encode functional defense systems capable of mediating plasmid interference in
bacterial cells guided by the CRISPR spacers."].

Architecture: bilobed, REC lobe (25–591) plus NUC lobe (662–1300) joined by a discontinuous WED
domain; the crRNA and the crRNA–target DNA heteroduplex sit in the channel between the lobes
(UniProt DOMAIN, from PMID:28431230 and PMID:28562584). The catalytic machinery is a single
**RuvC**-like domain, assembled from three dispersed motifs, plus an inserted **Nuc** domain. Unlike
Cas9 it has no HNH domain: [PMID:26422227 "The Cpf1 protein contains a predicted RuvC-like
endonuclease domain that is distantly related to the respective nuclease domain of Cas9. However,
Cpf1 differs from Cas9 in that it lacks a second, HNH endonuclease domain"].

## 2. Three distinguishable activities

### 2a. pre-crRNA processing (endoribonuclease; EC 4.6.1.22)

Cas12a needs no tracrRNA and no Cas6: it matures its own guide.
[PMID:26422227 "indicating that FnCpf1 and its CRISPR array are the only elements required from the
FnCpf1 locus to achieve crRNA processing"]. Established as a second, separable nuclease activity by
[PMID:27096362 "We show that type V-A Cpf1 from Francisella novicida is a dual-nuclease that is
specific to crRNA biogenesis and target DNA interference."] and
[PMID:27096362 "Cpf1 uses distinct active domains for both nuclease reactions and cleaves nucleic
acids in the presence of magnesium or calcium."].

The chemistry is **not hydrolysis**. Swarts et al. showed the reaction is an intramolecular
transesterification that leaves a 2',3'-cyclic phosphate:
[PMID:28431230 "Combined, these results demonstrate that pre-crRNA processing by FnCas12a proceeds
through a metal-independent catalytic mechanism involving a nucleophilic attack on the scissile
phosphate by the 2’-hydroxyl of the upstream ribonucleotide."]. That is exactly why UniProt carries
**EC 4.6.1.22** (a phosphorus–oxygen lyase, reaction `RNA = a 5'-hydroxy-ribonucleotide + n
nucleoside-2',3'-cyclophosphates`) in addition to the DNase EC — the two ECs are two different
activities of one protein, not two descriptions of one activity.

Note a literature conflict on the metal requirement: PMID:27096362 reports cleavage "in the presence
of magnesium or calcium", and UniProt's COFACTOR note says a divalent cation (bound by the crRNA) is
required, while PMID:28431230 reports the catalytic step itself to be metal-independent. The
resolution offered in PMID:28431230 is that the cation orders the crRNA pseudoknot rather than
participating in catalysis. Both readings agree the chemistry yields a 2',3'-cyclic phosphate.

Recognition is structure- rather than sequence-driven:
[PMID:27096362 "The RNase and DNase activities of Cpf1 require sequence- and structure-specific
binding to the hairpin of crRNA repeats."]

### 2b. cis crRNA-guided cleavage of double-stranded target DNA (EC 3.1.21.1 in UniProt)

Requires a 5' T-rich PAM (TTN for FnCas12a) and makes a staggered, not blunt, break:
[PMID:26422227 "Cpf1 is a single RNA-guided endonuclease lacking tracrRNA, and it utilizes a T-rich
protospacer-adjacent motif. Moreover, Cpf1 cleaves DNA via a staggered DNA double-stranded break."]
and [PMID:26422227 "Third, Cpf1 introduces a staggered DNA double stranded break with a 4 or 5-nt 5′
overhang."]. Sufficiency of protein + crRNA shown in vitro:
[PMID:26422227 "We found that FnCpf1 along with an in vitro transcribed mature crRNA targeting
protospacer 1 was able to efficiently cleave the target plasmid in a Mg2+- and crRNA-dependent
manner"].

**How many active sites?** The literature disagrees, and the disagreement matters for how many
molecular functions to assert.
- Yamano et al., on the Acidaminococcus ortholog, proposed two: [PMID:27114038 "AsCpf1 contains the
  RuvC domain and a putative novel nuclease domain, which are responsible for cleaving the
  non-target and target strands, respectively, and for jointly generating staggered DNA
  double-strand breaks."]
- Swarts et al., on FnCas12a itself and with mutagenesis, concluded one:
  [PMID:28431230 "we hypothesized that Cas12a also cleaves both the target and non-target DNA strands
  using a single active site."] and
  [PMID:28431230 "The complete loss of target strand DNA cleavage observed for the E1006Q mutant
  (Figure 5B) suggests that the RuvC domain is not simply required for proper coordination of target
  strand, but that instead it directly catalyzes target strand cleavage."]
- The single-RuvC reading is now the standard one:
  [PMID:30936531 "Cas12a possesses a single nuclease domain (RuvC) that is activated upon a crRNA
  targeting sequence (or spacer) binding to a complementary single-stranded DNA (ssDNA) or"]

Curation consequence: **one** DNase molecular function, not one per strand.

### 2c. trans (collateral) ssDNA cleavage — same RuvC site

Target binding switches the RuvC site into a substrate-nonspecific ssDNase:
[PMID:29449511 "Here we show that RNA-guided DNA binding unleashes indiscriminate single-stranded DNA
(ssDNA) cleavage activity by Cas12a that completely degrades ssDNA molecules."] and
[PMID:29449511 "We find that target-activated, nonspecific single-stranded deoxyribonuclease
(ssDNase) cleavage is also a property of other type V CRISPR-Cas12 enzymes."]. That paper is
abstract-only in the cache, and its named orthologs are not FnCas12a; the activity is therefore
asserted here for the Acidaminococcus entry (where PMID:30936531 provides full-text, As-specific
evidence) and left unasserted for FnCas12a. See §5.

## 3. Native biological role

Plasmid immunity, formally demonstrated by heterologous reconstitution in *E. coli*:
[PMID:26422227 "the results of the depletion assay clearly indicate that heterologously expressed
Cpf1 loci are capable of efficient interference with plasmid DNA"]. UniProt's FUNCTION block
records the same ("When this protein is expressed in E.coli it prevents plasmids homologous to the
first CRISPR spacer from transforming, formally showing it is responsible for plasmid immunity").

No phage-challenge data for **FnCas12a** is present in the cached literature. Anti-phage immunity is
documented for the Acidaminococcus ortholog (PMID:38261981, see that gene's notes), so for this
entry the defensible process term is the system-level `GO:0099048 CRISPR-cas system` rather than
`GO:0051607 defense response to virus`.

## 4. GOA adjudication

GOA holds two rows, both `GO:0004530 deoxyribonuclease I activity`:

| evidence | reference | basis |
|---|---|---|
| EXP | PMID:28431230 | the dsDNase activity measured by Swarts et al. |
| IEA | GO_REF:0000003 | EC 3.1.21.1 → GO mapping |

`GO:0004530` is the GO term for **EC 3.1.21.1, deoxyribonuclease I** — a non-specific, secreted,
metazoan-type nuclease. Its definition is the generic EC reaction: *"Catalysis of the endonucleolytic
cleavage of DNA to 5'-phosphodinucleotide and 5'-phosphooligonucleotide end products."* Nothing
about that term says double-stranded, programmed, PAM-dependent, or staggered, and the
dinucleotide-product clause is an artefact of the DNase I reaction rather than a property of Cas12a.
The underlying biology — endonucleolytic cleavage of both strands of a duplex DNA target — is
captured exactly by `GO:1990238 double-stranded DNA endonuclease activity` ("Catalysis of the
hydrolysis of ester linkages within a double-stranded DNA molecule by creating internal breaks").
Both rows are therefore MODIFY → `GO:1990238`.

The EXP row's own reference supports the replacement, not the DNase I framing:
[PMID:28431230 "the R-loop complex structure reveals the strand displacement mechanism that
facilitates guide-target hybridization and suggests a mechanism for double-stranded DNA cleavage
involving a single active site"].

The second UniProt EC, **4.6.1.22**, has produced no GOA row at all — a real gap, since it is the
crRNA-maturation activity that makes type V-A "the most minimalistic of the CRISPR-Cas systems so
far described" (PMID:27096362). Added as `NEW` with `GO:0004521 RNA endonuclease activity`, which is
the right level: `GO:0004521` is defined mechanism-agnostically ("Catalysis of the cleavage of ester
linkages within ribonucleic acid by creating internal breaks") and sits under
`GO:0004519 endonuclease activity` → `GO:0004518 nuclease activity` → `GO:0140640`, *not* under
hydrolase. Its children `GO:0016891`/`GO:0016892` would be wrong, since both stipulate a "hydrolytic
mechanism" and the Cas12a reaction is a metal-independent transesterification.

## 5. What is deliberately NOT asserted

- **Genome editing / biotechnology.** UniProt has a long BIOTECHNOLOGY block, and most of the
  literature on this protein is about editing rice, tobacco and human cells. None of it is a
  biological function of the gene in *F. novicida*; it is excluded from `description` and
  `core_functions` entirely.
- **trans-ssDNase for this ortholog.** See §2c. Raised in `suggested_experiments` instead.
- **A guide-RNA-recognition molecular function.** GO has no such term; checked against the local GO
  release, where no MF label contains "RNA-guided", "guide RNA" or "CRISPR". Raised as a
  `proposed_new_terms` entry and in `suggested_questions`.
- **`GO:0003677 DNA binding` / `GO:0003723 RNA binding`.** UniProt carries both keywords and several
  DNA_BIND features. They are true but uninformative — they do not distinguish Cas12a from any
  generic nucleic-acid-binding protein, and the project guidance is to prefer a term that says what
  the protein does. The informative version of this claim is precisely the missing guide-recognition
  term.
- **`GO:0051607 defense response to virus`.** No phage data for FnCas12a in the cached literature.

## 6. Open questions recorded in the review

- Is the native *F. novicida* CRISPR array ever loaded with phage-derived spacers, or is this system
  predominantly anti-plasmid? The only interference data are heterologous.
- Does FnCas12a show the target-activated trans-ssDNase that As/Lb/Mb Cas12a show, and does trans
  cleavage contribute to immunity in a native host at all, or is it only detectable in vitro?
- The metal-dependence conflict in §2a is unresolved between PMID:27096362 and PMID:28431230.
