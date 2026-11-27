# AsCas12a (AsCpf1), *Acidaminococcus* sp. BV3L6 — curation notes

UniProt U2UMQ6 (CS12A_ACISB), 1307 aa, reviewed. ORF HMPREF1246_0236. Type V-A CRISPR-Cas system.
UniProt EC numbers: **3.1.21.1** and **4.6.1.22**, both `ECO:0000250|UniProtKB:A0Q7Q2` — i.e. both
transferred by similarity from the *Francisella novicida* ortholog, not measured on this protein.

No deep-research provider was available (no API keys configured), so this file is the research
journal. Provenance is inline from cached publications in `publications/`.

## 1. Relationship to the Francisella entry

These two are the same enzyme family doing the same job in two organisms, and the reviews are
deliberately parallel. The differences that matter for curation:

| | A0Q7Q2 (FnCas12a) | U2UMQ6 (AsCas12a) |
|---|---|---|
| PAM | TTN | **TTTN** |
| overhang | 5-nt staggered | **4-nt staggered**, 19/22 nt from PAM |
| EC evidence | ECO:0000269 (experimental) | ECO:0000250 (by similarity) |
| crRNA processing | directly measured | **By similarity** in UniProt |
| phage immunity | not shown | **shown** (PMID:38261981) |
| trans-ssDNase | not shown | **shown** (PMID:30936531) |
| GOA | 1 EXP + 1 IEA row | 1 IEA + 1 **ISS** row |

So the *Acidaminococcus* entry is the weaker one for crRNA processing and the stronger one for
in vivo defence and for collateral ssDNA cleavage.

## 2. Structure and the single-vs-two-active-site question

The 2.8 Å ternary structure is of this very protein:
[PMID:27114038 "The structure revealed that AsCpf1 adopts a bilobed architecture consisting of an
α-helical recognition (REC) lobe and a nuclease (NUC) lobe, with the crRNA–target DNA heteroduplex
bound to the positively charged, central channel between the two lobes"] and
[PMID:27114038 "AsCpf1 recognizes the crRNA scaffold and the 5′-TTTN-3′ PAM in structure- and
sequence-dependent manners."], with PAM readout by both base and shape:
[PMID:27114038 "AsCpf1 recognizes the 5'-TTTN-3' protospacer adjacent motif by base and shape
readout mechanisms."].

Yamano et al. proposed that RuvC and a second "Nuc" domain cut the two strands separately:
[PMID:27114038 "AsCpf1 contains the RuvC domain and a putative novel nuclease domain, which are
responsible for cleaving the non-target and target strands, respectively, and for jointly generating
staggered DNA double-strand breaks."]. UniProt's DOMAIN block for U2UMQ6 still follows that reading
("One nuclease site is found in the discontinuous RuvC domain ... the other in the NUC domain").

The field has since converged on a single RuvC site that cuts both strands sequentially, on the
basis of FnCas12a mutagenesis [PMID:28431230 "we hypothesized that Cas12a also cleaves both the
target and non-target DNA strands using a single active site."] and the E1006Q result
[PMID:28431230 "The complete loss of target strand DNA cleavage observed for the E1006Q mutant
(Figure 5B) suggests that the RuvC domain is not simply required for proper coordination of target
strand, but that instead it directly catalyzes target strand cleavage."], and this is how reviews
now state it [PMID:30936531 "Cas12a possesses a single nuclease domain (RuvC) that is activated upon
a crRNA targeting sequence (or spacer) binding to a complementary single-stranded DNA (ssDNA) or"].

**Curation consequence: one DNase molecular function, not two.** The cis dsDNA break and the trans
ssDNA cleavage come from the same site and are distinguished by substrate and by activation state,
not by catalytic machinery — which is exactly why they are recorded as two `core_functions` entries
rather than two independent active sites.

## 3. The three activities, for this ortholog

### 3a. cis crRNA-guided dsDNA cleavage

UniProt FUNCTION (ECO:0000269|PubMed:26422227): "Has dsDNA endonuclease activity, results in
staggered 4-base 5' overhangs 19 and 22 bases downstream of the PAM on the non-targeted and targeted
strand respectively." This ortholog is one of the two of sixteen screened that worked:
[PMID:26422227 "However, when tested in human embryonic kidney 293FT (HEK 293FT) cells, only 2 out of
the 8 Cpf1-family proteins (7 – AsCpf1 and 13 – LbCpf1) exhibited detectable levels of
nuclease-induced indels"] — a biotechnology result, recorded here only as the reason this ortholog
is so well studied, and deliberately kept out of the review's `description` and `core_functions`.

### 3b. trans (collateral) ssDNase, same RuvC site

This is the one activity better documented for As than for Fn. The general phenomenon:
[PMID:29449511 "Here we show that RNA-guided DNA binding unleashes indiscriminate single-stranded DNA
(ssDNA) cleavage activity by Cas12a that completely degrades ssDNA molecules."] (abstract-only
cache). The As-specific evidence is in the AcrVA1 paper, which assayed Mb, Lb and AsCas12a side by
side on both substrates:
[PMID:30936531 "AcrVA1 blocked dsDNA cleavage by all three Cas12a orthologs, whereas AcrVA4 and
AcrVA5 were effective against Moraxella bovoculi (Mb) Cas12a and LbCas12a but not Acidaminococcus
sp. (As) Cas12a"] and
[PMID:30936531 "The pattern of inhibition was generally the same for Cas12a-mediated ssDNA cleavage
but activity was not completely abolished by any inhibitor"]. The second sentence presupposes
measurable AsCas12a ssDNA cleavage, and the framing sentence of the same paper states that the RuvC
site is activated on ssDNA or dsDNA targets. Asserted as `NEW` with `GO:0000014 single-stranded DNA
endonuclease activity`.

Note what is *not* asserted: nothing about collateral-cleavage-based nucleic-acid detection. DETECTR
and its descendants are reagent uses, not functions of the gene in *Acidaminococcus*.

### 3c. pre-crRNA processing

For this entry UniProt says "In this CRISPR system correct processing of pre-crRNA requires only this
protein and the CRISPR locus (By similarity)", and both ECs carry `ECO:0000250|UniProtKB:A0Q7Q2`.
The activity is a family-level property of Cas12a — stated generally in
[PMID:30936531 "After expression of the CRISPR array and Cas proteins, Cas12a catalyzes precursor
CRISPR-RNA (pre-crRNA) processing to form a Cas12a-crRNA complex (or ribonucleoprotein, RNP)"] — and
directly measured on the Francisella ortholog
[PMID:27096362 "We show that type V-A Cpf1 from Francisella novicida is a dual-nuclease that is
specific to crRNA biogenesis and target DNA interference."]. Asserted as `NEW` with evidence code
**ISS** and a WITH entry of UniProtKB:A0Q7Q2, matching the basis UniProt itself used, rather than
claiming direct evidence this entry does not have.

## 4. Native biological role

Unlike the Francisella entry, this one has phage-challenge data, from a Cas12m paper that used
AsCas12a as its positive control:
[PMID:38261981 "the AsCas12a effector provided a reduction in plaque formation with variable
efficiency for almost all phages tested except T4 (WT)"], with the T4 exception explained by DNA
modification [PMID:38261981 "The limited AsCas12a immunity against T4 (WT) is most likely due to the
naturally occurring glycosylation of cytosines, as the T4 phage variants containing hydroxymethyl or
unmodified cytosines were efficiently targeted."]. UniProt records the same: "Protects E.coli against
plasmids and bacteriophage M13mp18, phage T4 with hydroxymethyl or unmodified (but not glycosylated)
cytosines and to a lesser extent against lambda and VpaE1 phage".

That supports both `GO:0099048 CRISPR-cas system` and `GO:0051607 defense response to virus` for
this entry. Both are `NEW`, since GOA holds no BP annotation at all.

The glycosylated-T4 escape is worth recording as biology rather than as a caveat: it shows that
interference depends on the chemical accessibility of the invader's DNA, which is a genuine limit on
the system and the reason phages carrying hypermodified genomes are resistant.

## 5. GOA adjudication

Two rows, both `GO:0004530 deoxyribonuclease I activity`:

| evidence | reference | WITH |
|---|---|---|
| IEA | GO_REF:0000003 | EC:3.1.21.1 |
| ISS | GO_REF:0000024 | UniProtKB:A0Q7Q2 |

Both are MODIFY → `GO:1990238 double-stranded DNA endonuclease activity`, for the same reason as in
the Francisella review: `GO:0004530` is the GO rendering of **EC 3.1.21.1, deoxyribonuclease I**, a
non-specific nuclease, and its definition carries DNase I's product specification
("5'-phosphodinucleotide and 5'-phosphooligonucleotide end products") rather than anything true of
Cas12a. `GO:1990238` says what Cas12a does to a duplex target and says nothing false.

The ISS row is not challenged as a propagation — A0Q7Q2 is the right source and the orthology is not
in doubt, and the project rule is to keep a legitimate transfer. What is wrong is only the term, and
it is wrong at the source as well as at the target.

EC **4.6.1.22** has again produced no GOA row, so the crRNA-processing activity is missing entirely;
added as `NEW` with `GO:0004521 RNA endonuclease activity`. Rationale for that term rather than
`GO:0016891`/`GO:0016892`: those two stipulate a hydrolytic mechanism and this reaction is a
metal-independent transesterification leaving a 2',3'-cyclic phosphate
[PMID:28431230 "Combined, these results demonstrate that pre-crRNA processing by FnCas12a proceeds
through a metal-independent catalytic mechanism involving a nucleophilic attack on the scissile
phosphate by the 2’-hydroxyl of the upstream ribonucleotide."]. `GO:0004521` is mechanism-agnostic
and sits under `GO:0004519`/`GO:0004540`, not under a hydrolase parent.

## 6. What is deliberately NOT asserted

- **Genome editing.** UniProt's BIOTECHNOLOGY block is long and the engineered PAM variants
  (PMID:28595896) are a large part of this entry's literature. None of it is a function of the gene
  in its own organism.
- **A guide-RNA-recognition molecular function.** No such GO term exists; verified against the
  current GO release (no MF label contains "RNA-guided", "guide RNA" or "CRISPR"). Raised in
  `proposed_new_terms`, with text identical to the Francisella review so the two requests can be
  merged rather than duplicated.
- **`GO:0003677 DNA binding` / `GO:0003723 RNA binding`.** True, keyworded in UniProt, and
  uninformative: they do not separate Cas12a from any nucleic-acid-binding protein. The informative
  version of the claim is the missing guide-dependence term.
- **A trans-cleavage-specific process term.** Considered and rejected. Asking which entity performs
  the step gives the right answer here — Cas12a does the cleaving — but the step is already named by
  the molecular function `GO:0000014`, and there is no demonstration that collateral ssDNA cleavage
  produces any distinct cellular outcome in a Cas12a host. (It does in Cas13a hosts, where dormancy
  is measurable; see the Cas13a notes.) Proposing a process term for an activity whose physiological
  consequence has not been observed would be asserting a pathway from an in vitro property.

## 7. Open questions recorded in the review

- Is the *Acidaminococcus* BV3L6 type V-A system active in its own host, and what are its native
  spacers? All interference data are heterologous.
- Does target-activated trans-ssDNase cleavage contribute to immunity in vivo, or is it only a
  consequence of an exposed RuvC site in vitro? The honest test is a separation-of-function mutant,
  which may not exist given that cis and trans share the site.
- Why does AcrVA4/AcrVA5 inhibition spare AsCas12a while AcrVA1 does not? PMID:30936531 reports the
  specificity difference but the structural basis for the As resistance is unresolved.
