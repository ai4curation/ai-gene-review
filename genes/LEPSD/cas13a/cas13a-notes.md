# LshCas13a (C2c2), *Leptotrichia shahii* — curation notes

UniProt P0DOC6 (CS13A_LEPSD), 1389 aa, reviewed. Type VI-A, uridine-preferring CRISPR-Cas system.
UniProt EC: **3.1.-.-** only (`ECO:0000269|PubMed:27256883`) — no complete EC class exists for this
chemistry.

**GOA holds zero annotations for this entry.** The `cas13a-goa.tsv` file is a header row and nothing
else. So the entire review is `NEW` rows plus `core_functions`, and the project's high bar for `NEW`
applies throughout. No deep-research provider was available (no API keys), so this file is the
research journal; provenance is inline from cached publications.

## 1. Why this protein is a special case among Cas effectors

Cas13a is the only single-protein CRISPR effector class whose target is **RNA**. That is not a
side-activity; it is the defining property, and it was established by exclusion as well as by
demonstration. Abudayyeh et al. tested DNA explicitly and found nothing:
[PMID:27256883 "When incubated with LshC2c2 protein and a crRNA complementary to protospacer 14, no
cleavage of the dsDNA plasmid library was observed (fig. S10C). We also did not observe cleavage when
targeting a ssDNA version of ssRNA target 1"]. UniProt records the same negative result ("has no
activity on partially dsRNA, ssDNA or dsDNA").

Catalysis is by two HEPN domains that come together to form one composite active site, not by a
RuvC- or HNH-type nuclease centre:
[PMID:27256883 "Cleavage is mediated by catalytic residues in the two conserved Higher Eukaryotes
and Prokaryotes Nucleotide-binding (HEPN) domains, mutations of which generate catalytically inactive
RNA-binding proteins."] All four single alanine substitutions of the two R-H dyads kill the activity,
and neither HEPN domain can compensate for loss of the other, which is why this counts as one site
rather than two.

Target recognition uses a 3' **protospacer flanking site** rather than a PAM, and the distinction is
substantive rather than terminological — in an RNA-targeting system there is no self/non-self
discrimination problem for a PAM to solve:
[PMID:27256883 "spacers with a G immediately flanking the 3’ end of the protospacer were less fit
relative to all other nucleotides at this position (i.e. A, U, or C), suggesting that the 3′
protospacer flanking site (PFS) affects the efficacy of C2c2-mediated targeting"].

## 2. The two RNase activities, at two separate sites

This is a real two-site enzyme, unlike Cas12a where cis and trans cleavage share the RuvC site.

### 2a. Target ssRNA cleavage + collateral cleavage — HEPN composite site

Specific, crRNA-directed cleavage of a complementary single-stranded transcript, preferentially
before U residues (hence "uridine-preferring"). Unusually, the cut falls *outside* the crRNA-pairing
region, in exposed single-stranded loops, so the cleavage position depends on target secondary
structure (UniProt FUNCTION, from PMID:27256883).

Binding a viable target then switches the same HEPN site into a substrate-non-specific RNase:
[PMID:27256883 "whereas the LshC2c2-crRNA complex did not mediate cleavage of any of the four
collateral RNAs in the absence of the target RNA, all four were efficiently degraded in the presence
of the target RNA"]. The HEPN mutants R597A and R1278A also lose collateral cleavage, which is the
evidence that it is the same catalytic centre. UniProt's ACTIVITY REGULATION block states it plainly:
"Target RNA acts as an activator for non-specific ssRNA degradation".

### 2b. pre-crRNA processing — a distinct, non-HEPN site

Cas13a matures its own guide (optimally a 28-nt spacer here), cleaving one nucleotide upstream of the
pre-crRNA stem-loop. The structure of this protein localises the two catalytic pockets to different
domains:
[PMID:28086085 "The two RNase catalytic pockets responsible for cleaving pre-crRNA and target RNA are
independently located on Helical-1 and HEPN domains, respectively."] and
[PMID:28086085 "C2c2, the effector of type VI CRISPR-Cas systems, has two RNase activities-one for
cutting its RNA target and the other for processing the CRISPR RNA (crRNA)."]

The mechanistic separation was shown on the *L. buccalis* ortholog, where HEPN mutants keep
processing and an R1079A mutant loses processing while keeping target cleavage
[PMID:27669025 "Double and quadruple mutants of conserved HEPN residues (R472A, R477A, R1048A and
R1053) retained robust pre-crRNA cleavage activity (Fig. 3c). By contrast, all HEPN mutations
abolished RNA-guided cleavage activity while not affecting crRNA or ssRNA-binding ability"].

Cross-ortholog note worth recording: this enzyme cleaves *L. buccalis* and *L. wadei* pre-crRNA at a
site 3 nt different from where those enzymes cut their own (UniProt FUNCTION, from PMID:28475872),
which is why the family splits into two functional groups
[PMID:28475872 "we show that the Cas13a enzyme family comprises two distinct functional groups that
recognize orthogonal sets of crRNAs and possess different ssRNA cleavage specificities"]. Those
groups "could not be bioinformatically predicted", which is a direct warning against propagating
substrate specificity across the family by similarity.

## 3. Native biological role: RNA phage immunity, and what follows the cleavage

The in vivo demonstration is for **this** ortholog and it is strong. A tiled spacer library against
the ssRNA phage MS2 was screened in *E. coli* carrying the reconstituted *L. shahii* locus
[PMID:27256883 "We explored whether LshC2c2 could confer immunity to MS2 (25), a lytic single-stranded
(ss) RNA phage, without DNA intermediates in its life cycle, that infects E. coli."], enriched
spacers were individually validated
[PMID:27256883 "To validate the interference activity of the enriched spacers, we individually cloned
four top-enriched spacers into pLshC2c2 CRISPR arrays and observed a 3- to 4-log10 reduction in plaque
formation"], and the requirement for catalysis was established by mutagenesis
[PMID:27256883 "We mutated each of these putative catalytic residues separately to alanine (R597A,
H602A, R1278A, H1283A) in the LshC2c2 locus plasmids and assayed for MS2 interference. None of the
four mutant plasmids were able to protect E. coli from phage infection"].

That is loss-of-function plus rescue-by-wild-type for a 3-4 log phenotype, with the catalytic residues
identified — about as good as IMP evidence gets for a heterologously reconstituted defence system.

**The downstream outcome.** Abudayyeh et al. already proposed that the collateral cleavage, rather
than clean clearance of the invader, is the protective mechanism:
[PMID:27256883 "We therefore surmised that, in addition to the cleavage of the target RNA, C2c2 CRISPR
systems might prevent virus reproduction also via non-specific cleavage of cellular mRNAs, causing
programmed cell death (PCD) or dormancy"]. UniProt carries this as a suggestion, correctly hedged.

It was later demonstrated, though on the *Listeria seeligeri* ortholog rather than this one:
[PMID:31142834 "Here we show that trans-cleavage of transcripts halts the growth of the host cell and
is sufficient to abort the infectious cycle."] and
[PMID:31142834 "we believe that the fundamental feature of type VI-A immunity is the dormancy of the
host cell produced by the destruction of host transcripts. This is similar to other phage defense
strategies known as abortive infection"]. That paper also showed type VI-A spacers in nature match
dsDNA phages, not RNA phages, which reframes the MS2 result as a proof of mechanism rather than a
picture of the natural invader.

Because the dormancy demonstration is on a different ortholog, it is cited here as MEDIUM-relevance
context and is **not** turned into an annotation on P0DOC6.

## 4. Annotations asserted, and why each clears the `NEW` bar

| term | evidence | ref | the entity that performs the step |
|---|---|---|---|
| GO:0004521 RNA endonuclease activity | IDA | PMID:27256883 | LshCas13a itself; purified protein + crRNA cleaves target and collateral RNA, abolished by four point mutants |
| GO:0099048 CRISPR-cas system | IMP | PMID:27256883 | LshCas13a performs two of the three stages the term names: crRNA biogenesis and target interference |
| GO:0051607 defense response to virus | IMP | PMID:27256883 | 3-4 log10 reduction in MS2 plaque formation, abolished in each of four catalytic point mutants |

On the choice of `GO:0004521 RNA endonuclease activity` rather than a child: the children
`GO:0016891` and `GO:0016892` each stipulate a *hydrolytic mechanism* and specify the product
phosphomonoester. For LshCas13a the target-cleavage reaction is Mg2+-dependent (UniProt COFACTOR) but
the end-group chemistry is not established in the cached literature, and the pre-crRNA reaction is
metal-independent with a 2',3'-cyclic phosphate product in the *L. buccalis* ortholog. Asserting
either child would be asserting mechanism the data do not establish for this protein.
`GO:0004521` is defined mechanism-agnostically and sits under `GO:0004519`/`GO:0004540` rather than
under a hydrolase parent, so it is the correct stopping point.

One `GO:0004521` row covers both activities, because GO cannot presently distinguish them: both are
RNA endonuclease activity, and the thing that separates them — guide dependence for one, structural
recognition of the repeat for the other — is exactly what the ontology lacks terms for. The
distinction is carried in two separate `core_functions` entries instead, which is where it belongs.

## 5. What is deliberately NOT asserted

- **Nucleic-acid diagnostics.** Cas13a's collateral cleavage is the basis of a large family of
  detection methods. That is a reagent application, not a function of the gene in *L. shahii*, and it
  is excluded from `description` and `core_functions` entirely. UniProt's own BIOTECHNOLOGY block
  ("Can be reprogrammed to target specific mRNAs in an E.coli system") is likewise excluded.
- **Any DNA-directed activity.** Explicitly tested and negative for this protein (§1). Note that a
  2025 paper reports DNA targeting by the *L. buccalis* ortholog (PMID:40542106, cited on that
  entry); nothing comparable is reported for LshCas13a, and the published negative result stands.
- **A dormancy / abortive-infection process annotation.** The outcome is real but was demonstrated on
  the *L. seeligeri* ortholog, and GO has no term for it. Raised as a `proposed_new_terms` entry and a
  `suggested_question`, not asserted. See §6 for the reasoning.
- **`GO:0003723 RNA binding`.** True — UniProt keywords it, and the HEPN mutants are specifically
  described as "catalytically inactive RNA-binding proteins" — but uninformative, since it does not
  distinguish a programmable guide-loaded surveillance complex from any RNA-binding protein. The
  informative version is the missing guide-dependence term.
- **`GO:0022611` / `GO:0097436` dormancy terms.** These sit under `GO:0032502 developmental process`
  and describe a developmental programme; using them for phage-induced bacterial growth arrest would
  be a branch error, not merely a stretch.

## 6. The dormancy term request, and the `NEW`-bar reasoning behind it

Asking the right question — *which entity performs the step?* — gives a favourable answer here, unlike
the Cas12a trans-cleavage case. Cas13a itself degrades the host transcripts; the arrest is the direct
consequence of that degradation, not a separate process carried out by something else, and
PMID:31142834 shows trans-cleavage alone is sufficient to abort the infectious cycle.

Reading candidate parents: `GO:0051607 defense response to virus` is the right parent. It is already
asserted for this gene, so a child is additional specificity rather than redundancy. The existing
dormancy terms are in the wrong branch (§5).

Comparator check: GO annotates no gene product to any abortive-infection or
defence-by-growth-arrest term, because no such term exists — this is a genuine ontology gap rather
than a convention I have failed to identify, and the gap affects a whole class of bacterial defence
systems (toxin-antitoxin-based abortive infection, retrons, Thoeris) and not just Cas13a. That is an
argument for requesting the term, and simultaneously an argument for *not* asserting an annotation to
a nonexistent id on this entry, which is why only the term request appears.

## 7. Open questions recorded in the review

- What do the native *L. shahii* spacers match? PMID:31142834 found type VI-A spacers matching dsDNA
  phages rather than RNA phages, which would make the MS2 experiment a proof of principle rather than
  a model of the natural threat.
- Does LshCas13a induce dormancy in a host, as the *L. seeligeri* ortholog does, and is the arrest
  reversible?
- What are the end-group products of LshCas13a target cleavage? Needed before any `GO:0016891`/
  `GO:0016892`-level term could be justified.
- The functional split in the Cas13a family (PMID:28475872) could not be predicted
  bioinformatically. What determines which crRNAs and which ssRNA cleavage specificities an ortholog
  has?
