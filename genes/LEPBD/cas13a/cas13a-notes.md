# LbuCas13a (C2c2), *Leptotrichia buccalis* C-1013-b — curation notes

UniProt C7NBY4 (CS13A_LEPBD), 1159 aa, reviewed. Locus Lebu_1799. Type VI-A, uridine-preferring
CRISPR-Cas system. UniProt EC: **3.1.-.-** only (`ECO:0000269|PubMed:27669025`) — no complete EC
class fits.

**GOA holds zero annotations for this entry** (the `.tsv` is a header row only), so the whole review
is `NEW` plus `core_functions`, and the project's high bar for `NEW` applies throughout. No
deep-research provider was available (no API keys), so this is the research journal, with inline
provenance from cached publications.

## 1. Relation to the *L. shahii* entry

Same system, different ortholog, and the two differ in which claims have direct evidence. Keeping
them straight matters, because PMID:28475872 found the Cas13a family splits into two functionally
orthogonal groups whose specificities "could not be bioinformatically predicted" — i.e. this is a
family where propagating specificity by similarity is explicitly unsafe.

| | P0DOC6 (LshCas13a, 1389 aa) | C7NBY4 (LbuCas13a, 1159 aa) |
|---|---|---|
| in vivo phage immunity | **MS2, 3-4 log, 4 catalytic mutants** | not shown |
| pre-crRNA processing | shown | **shown, with mechanism and end groups** |
| two-site separation | shown structurally | **shown by mutagenesis (R1079A vs HEPN)** |
| target cleavage rate | — | **~80x faster than processing** |
| activation threshold | — | **10 fM target** |
| REC/NUC boundary | 1-498 / 499-1389 | 1-360 / 361-1159 |
| DNA | no cleavage of ssDNA or dsDNA | **binds DNA targets but does not cleave them** |

So: Lsh is the entry with the immunity phenotype, Lbu is the entry with the clean enzymology.
Consequence for curation: `GO:0051607 defense response to virus` is asserted for Lsh and **not**
for Lbu, because no phage-challenge experiment on LbuCas13a appears in the cached literature.

## 2. Two chemically and mechanistically distinct RNase activities

This is the entry on which the two-activity model was established:
[PMID:27669025 "Here we show that bacterial C2c2 possesses a unique RNase activity responsible for
CRISPR RNA maturation that is distinct from its RNA-activated single-stranded RNA degradation
activity. These dual RNase functions are chemically and mechanistically different from each other"].

### 2a. pre-crRNA processing — metal-independent, non-HEPN site

[PMID:27669025 "Mechanistic studies of LbuC2c2 revealed that processing activity was unaffected by
the presence of divalent metal ion chelators EDTA or EGTA (Fig. 2c), indicative of a metal
ion-independent RNA hydrolytic mechanism."] Products were established by end-group chemistry: the
5' flanking product carries a 2',3'-cyclic phosphate (removable by T4 PNK) and the 3' product a
5'-hydroxyl. UniProt records this as "pre-crRNA processing yields a 5'-OH and probably a 2',3'-cyclic
phosphate".

Recognition is structural, not sequence-based in the spacer: the repeat hairpin and the regions
flanking it are required, while "there was no dependence on the spacer sequence for kinetics of
processing".

### 2b. target and collateral ssRNA cleavage — composite HEPN site

The site separation was proved both ways round, which is why this is a genuinely two-site enzyme
rather than one site with two substrate preferences:
- HEPN mutants lose target cleavage, keep processing:
  [PMID:27669025 "Double and quadruple mutants of conserved HEPN residues (R472A, R477A, R1048A and
  R1053) retained robust pre-crRNA cleavage activity (Fig. 3c). By contrast, all HEPN mutations
  abolished RNA-guided cleavage activity while not affecting crRNA or ssRNA-binding ability"]
- R1079A loses processing, keeps target cleavage:
  [PMID:27669025 "We identified an arginine residue (R1079A) that upon mutation resulted in severely
  attenuated pre-crRNA processing activity (Fig. 3c). This C2c2 mutant enzyme retained crRNA-binding
  ability as well as RNA target cleavage activity"]
- conclusion stated explicitly:
  [PMID:27669025 "Taken together, our results show that distinct active sites within the C2c2 protein
  catalyze pre-crRNA processing and RN"] (quotation truncated at a page break in the cached text)

Target binding then unleashes indiscriminate cleavage of bystander RNA, with enormous turnover:
[PMID:27669025 "the activation of C2c2 to cleave thousands of trans-RNAs for every target RNA
detected enables potent signal amplification"]. UniProt adds the quantitative details: target
cleavage is ~80-fold faster than processing and uses a different active site; activation occurs with
10 fM target RNA (PMID:28475872); and crRNA maturation is not required for activation, though its
absence lowers it.

The structural mechanism of activation is an induced-fit assembly of the HEPN site:
[PMID:28757251 "The guide-target RNA duplex formation triggers HEPN1 domain to move toward HEPN2
domain, activating the HEPN catalytic site of Cas13a protein, which subsequently cleaves both
single-stranded target and collateral RNAs in a non-specific manner."] This also explains the 20-nt
minimum duplex length UniProt records for activation. Structures are of this protein:
[PMID:28757251 "we have determined the crystal structure of Leptotrichia buccalis (Lbu) Cas13a bound
to crRNA and its target RNA, as well as the cryo-EM structure of the LbuCas13a-crRNA complex"].

## 3. The DNA-targeting report, and why it changes nothing in the annotations

UniProt's FUNCTION block ends with "Also targets DNA (PubMed:40542106)", which reads at first glance
as a DNase claim. The abstract says the opposite about cleavage:
[PMID:40542106 "We discover the ability of Leptotrichia buccalis Cas13a (LbuCas13a) to directly
target DNA without the restrictions of protospacer flanking sequence and protospacer adjacent motif
sequences, coupled with robust trans-cleavage activity."] and, decisively,
[PMID:40542106 "Contrary to conventional understanding, LbuCas13a does not degrade DNA targets."]

So: a DNA target can *bind* the crRNA and *activate* the HEPN site, whose trans activity then
destroys RNA — but the DNA itself is not cleaved. No DNA nuclease function is asserted. Two further
reasons for caution: the paper is abstract-only in the cache, and its purpose is to build a
genotyping platform (SUREST), so the DNA-recognition observation is made in a reagent context with
no claim about *L. buccalis* biology. Recorded in the review as a reference with a
`reference_review` noting all of this.

## 4. Annotations asserted, and how each clears the `NEW` bar

| term | evidence | ref | the entity that performs the step |
|---|---|---|---|
| GO:0004521 RNA endonuclease activity | IDA | PMID:27669025 | LbuCas13a itself; purified protein cleaves pre-crRNA and, once target-bound, trans-RNA, with reciprocal mutants separating the two sites |
| GO:0099048 CRISPR-cas system | IC | PMID:27669025 | LbuCas13a performs two of the three stages the term names; inferred by curator because the demonstrations are in vitro |

On `GO:0099048` with **IC** rather than IMP: the activities are directly measured but no interference
phenotype has been measured for this ortholog. IC is the honest code — the process assignment is a
curator's inference from the two in vitro activities plus the locus context (UniProt MISCELLANEOUS:
"Part of a type VI-A uridine-preferring CRISPR-Cas system"), not an experiment. Deliberately not ISS
from P0DOC6 either, since PMID:28475872 is an explicit warning against propagating specificity within
this family; the generic *process* is safe to infer, the specificity is not, and IC says exactly that.

On `GO:0004521` rather than `GO:0016891`/`GO:0016892`: here the mechanism *is* partly known —
processing is metal-independent and yields a 2',3'-cyclic phosphate and a 5'-OH, which is not a
hydrolysis to a 3'- or 5'-phosphomonoester, so both children are wrong for that activity. (Note the
cached paper calls it a "RNA hydrolytic mechanism" in the same sentence as the metal-independence
result; the end-group evidence in the same figure is what settles the chemistry.) For the HEPN target
reaction the end groups are not established in the cached literature. `GO:0004521` is
mechanism-agnostic and descends from `GO:0004519`/`GO:0004540`, not from a hydrolase parent, so it is
the correct stopping point for both.

One GOA-style row covers both activities because GO cannot distinguish them; the distinction is
carried in two `core_functions` entries, which is where it belongs.

## 5. What is deliberately NOT asserted

- **Nucleic-acid diagnostics.** The majority of the literature on LbuCas13a is detection technology
  (SHERLOCK, SUREST and relatives), and UniProt's BIOTECHNOLOGY block ("Can be used to detect low
  levels of cellular transcripts") is in that register. None of it is a function of the gene in
  *L. buccalis*; excluded from `description` and `core_functions`.
- **Any DNA nuclease activity.** See §3. The one paper reporting DNA targeting states explicitly that
  the DNA is not degraded.
- **`GO:0051607 defense response to virus`.** No phage-challenge data for this ortholog. Asserted on
  P0DOC6 instead, where there is a quantitative phenotype with four catalytic mutants.
- **A dormancy / abortive-infection process annotation.** The outcome is established for type VI-A
  (PMID:31142834, on the *Listeria seeligeri* ortholog) and GO has no term for it. Raised as a
  `proposed_new_terms` entry, identical to the one in the *L. shahii* review so the two can be merged.
- **`GO:0003723 RNA binding`.** True and keyworded, and the HEPN mutants retain crRNA and ssRNA
  binding, which makes it a measured property rather than an inference — but it does not distinguish a
  programmable guide-loaded surveillance enzyme from any RNA-binding protein. The informative version
  of the claim is the missing guide-dependence term.
- **A multimeric assertion.** UniProt's SUBUNIT block reports crystal contacts between the target
  RNA 3' end and an adjacent protein molecule, with mutagenesis effects, but flags that "it is not
  clear if this is physiological" (ECO:0000303). No complex or oligomerisation claim is made.

## 6. Open questions recorded in the review

- Is the *L. buccalis* type VI-A system functional as immunity in its own host, and what do its
  native spacers match? No interference experiment on this ortholog exists in the cached literature.
- What are the end-group products of LbuCas13a *target* cleavage, as opposed to pre-crRNA cleavage?
  Required before any term below `GO:0004521` could be justified for the HEPN activity.
- Does target-activated trans cleavage arrest an *L. buccalis* host, and is the arrest reversible?
- Does the reported ability to activate on a DNA target without a PFS or PAM requirement happen at
  physiological crRNA and target concentrations, and does it have any consequence for a cell carrying
  this locus, given that the DNA is not cleaved?
- What explains the ~80-fold rate difference and the 10 fM activation threshold — i.e. what keeps the
  HEPN site off in the loaded, unengaged state?
