# ygbF (cas2) — Escherichia coli K-12, UniProt P45956

Research journal for the gene review. Quotes are verbatim from the cached
publications in `publications/`.

## Identity

- UniProt primary gene name is **ygbF**; **cas2** is the functional synonym. GOA and
  EcoCyc use `ygbF` as the symbol, while UniProt's recommended protein name is
  "CRISPR-associated endoribonuclease Cas2" — a name I argue below is a family-level
  holdover and not a property of this protein. The gene is `b2754` / `JW5438`, the
  last gene of the `casABCDE-ygbT-ygbF` operon, immediately downstream of `ygbT`
  (cas1, Q46896).
- 94 residues. A homodimer with a ferredoxin-like (3.30.70.240) fold; 14 PDB entries,
  most of them Cas1-Cas2-DNA co-structures.
- Cas1 and Cas2 are the two universally conserved Cas proteins and together are the
  adaptation machinery:
  [PMID:27899566 "The universally conserved Cas1 and Cas2 form an integration complex that is known to mediate the protospacer invasion into the CRISPR array."]

## Cas2 is required in vivo, and is non-catalytic

Required:
[PMID:22402487 "Strains harboring plasmids encoding Cas1 or Cas2 alone (pCas1 and pCas2, respectively) did not show observable expansion of their array"]
and
[PMID:22402487 "Induced expression of E. coli Cas1 and Cas2 resulted in acquisition of spacers, as determined by PCR amplification of the repeat-spacer units adjacent to the leader terminus in CRISPR array I of both strains"]

Non-catalytic — this is the single most important adjudicated fact for this gene:
- [PMID:24793649 "In contrast, the catalytic activity of Cas2 is unnecessary for integration of sequences into the CRISPR locus in vivo."]
- [PMID:24793649 "Surprisingly, Cas2 mutated in the signature catalytic E9 residue to alanine or arginine supported spacer acquisition at frequencies similar to those observed in the presence of wild-type Cas2"]
- [PMID:25707795 "Consistent with these data, Cas1 active site mutants H208A and D221A were defective for protospacer integration in vitro, whereas the Cas2 E9Q active-site mutant supported integration"]
- [PMID:25707795 "Bacteria expressing Cas1 active-site mutants, but not active-site mutants of Cas2, are incapable of acquiring new spacers in vivo, demonstrating the catalytic role of Cas1 during spacer acquisition"]
- and Cas2 contributes nothing to the branched-DNA chemistry either:
  [PMID:26284603 "The activity was independent of the presence or absence of SsoCas2, suggesting that Cas2 is not involved in this nuclease activity in vitro."]
  [PMID:26284603 "Cas2 is not required for this activity and does not influence the specificity."]

## Adjudicating the UniProt name "CRISPR-associated endoribonuclease Cas2"

The recommended name asserts an endoribonuclease activity, with `EC=3.1.-.-` and the
keywords `Endonuclease`, `Hydrolase`, `Nuclease`. The provenance of that name is
*other organisms' Cas2 proteins*, not E. coli Cas2:

[PMID:26284603 "Initial biochemical analyses of a panel of archaeal Cas2 enzymes revealed an endonucleolytic activity against ssRNA substrates that could be abrogated by mutation of conserved residues"]

and even within the family the reported substrate is inconsistent:

[PMID:26284603 "In contrast, Cas2 from Bacillus halodurans has been shown to be specific for cleavage of dsDNA substrates"]

For E. coli Cas2 specifically: the only structure deposited for the isolated protein
is annotated by its depositors as a *putative* ssRNA endonuclease (UniProt Ref. 10,
PDB 4MAK, "Crystal structure of a putative ssRNA endonuclease Cas2"); no
ribonuclease assay on P45956 is reported in any of the cached papers; UniProt's own
FUNCTION block concedes "This subunit's probable nuclease activity is not required
for spacer acquisition"; and the E9 active-site mutants are fully functional (above).

**Verdict: the endoribonuclease activity is unsubstantiated for this protein and
irrelevant to adaptation.** The honest outcome is that it must not be annotated, and
GOA is already correct here — there is no nuclease, hydrolase, or RNA-binding row for
P45956 to act on. I record the adjudication in `suggested_questions` (so the UniProt
name is flagged rather than silently inherited) rather than inventing a `REMOVE`
target that does not exist in GOA. Anyone tempted to propagate `GO:0004521` or
`GO:0016788` onto E. coli Cas2 from the protein name should read this section first.

## What Cas2 *does* do — and why I partly disagree with the module

The module `crispr_cas_adaptive_immunity` asserts **no molecular function** for the
`cas2_adaptation_subunit` annoton, with `role_description` "Dimeric scaffold that
bridges two Cas1 dimers and measures the protospacer duplex; no catalytic activity is
asserted, which is why this annoton carries no molecular function," and books it as a
knowledge gap.

I agree with the premise and disagree with the conclusion.

The premise — no catalytic activity — is correct and well-evidenced (previous
section). But "no catalytic function" is not the same as "no molecular function". The
GO molecular-function branch is not restricted to catalysis; it includes structural
and adaptor activities, and `GO:0030674 protein-macromolecule adaptor activity` is
defined as "An adaptor activity that brings together two or more macromolecules in
contact, permitting those molecules to function in a coordinated way." That is a
description of what Cas2 does, and the literature says so in almost those words:

[PMID:26284603 "It is probable that Cas2 acts as an adaptor protein, either bringing two Cas1 dimers together or mediating interactions with other components necessary for spacer acquisition."]

The structural and functional support is at least as strong as the support for Cas1's
catalytic assignment:

1. **It is literally the bridge.**
   [PMID:24793649 "The overall architecture of the asymmetric unit is a heterohexameric complex consisting of two Cas1 dimers (Cas1a-b and Cas1c-d) that sandwich one Cas2 dimer"]
2. **The bridging is required for function, and the requirement maps to the
   interface rather than to Cas2's presence.**
   [PMID:24793649 "Mutations in either Cas1 or Cas2 that disrupt Cas1–Cas2 complex formation in vitro also interfere with spacer acquisition in vivo."]
   [PMID:24793649 "In addition to the catalytic function of Cas1, its ability to assemble with Cas2 is also essential for spacer acquisition."]
   The clean case is the beta6-beta7 deletion (residues 79-94): UniProt records "Loss
   of spacer acquisition, no Cas1-Cas2 complex formation, loss of CRISPR DNA-binding
   by complex" for that variant, i.e. removing the bridging element removes the
   function while leaving the putative active site intact.
3. **It measurably accelerates the reaction it is not catalysing** — so it is not a
   passive bystander:
   [PMID:25707795 "Although Cas1 alone catalyzed a low level of protospacer integration in the presence of Mn2+, the reaction was enhanced significantly by the presence of Cas2"]
   [PMID:25707795 "Cas1 is the catalytic subunit and Cas2 substantially increases integration activity."]
4. **It contributes directly to substrate binding and to the length measurement**, via
   its own residues, inside the complex:
   [PMID:26503043 "The Arginine Clamp interacts with the middle of the duplex region where four Arg residues coordinate each DNA strand: Cas1 R41 and Cas2 R16, R77, R78"]
   [PMID:26503043 "Reverse charge mutations of Cas1 R41 and Cas2 R16 and R78 drastically reduce spacer acquisition in vivo, whereas the Cas2 R77E mutant functions similar to wild-type (WT) Cas2"]
   [PMID:26503043 "Importantly, however, optimal substrates include a central 23 base pair helical region flanked by five single-stranded nucleotides on each 3′ end."]
   [PMID:26503043 "Our results uncover the structural basis for foreign DNA capture and the mechanism by which Cas1-Cas2 functions as a molecular ruler to dictate the sequence architecture of CRISPR loci."]
   Note the asymmetry in point 4 that argues against over-claiming: Cas2 alone does
   not bind DNA (UniProt FUNCTION, from PMID:24793649: "Cas2 not seen to bind DNA
   alone"), so DNA binding belongs in `contributes_to_molecular_function`, not in
   `molecular_function`.

**Recommendation to the module:** replace "no molecular function" with
`GO:0030674 protein-macromolecule adaptor activity`, and retain the molecular-ruler
behaviour as the genuine knowledge gap, since GO has no term for duplex-length
measurement and the ruler is a property of the Cas1-Cas2 assembly rather than of
Cas2 alone. The knowledge gap is real; it is just a narrower gap than the module
currently claims. I have raised the ruler term as a `proposed_new_terms` entry so the
gap is recorded rather than papered over with an ill-fitting id.

I note the competing view honestly: a curator could reasonably hold that `GO:0030674`
is a near-vacuous restatement of "it is a subunit", and that is why the term is used
sparingly. My answer is that Cas2's bridging is not incidental to the complex but is
the element whose removal abolishes the activity (point 2), which is exactly the
discriminating test `GO:0030674` is for.

## Annotation-by-annotation

Only five GOA rows exist for P45956.

- **`GO:0005515 protein binding`** (IPI, PMID:24793649, partner Q46896) and
  **`GO:0005515`** (IPI, PMID:26503043, partner Q46896). Both report the same
  structurally defined Cas1-Cas2 interface, from co-crystal structures. The essence is
  right; the term is the least informative one available, and the project guideline is
  explicit that `protein binding` should give way to a term that says what the protein
  does. **MODIFY** both to `GO:0030674 protein-macromolecule adaptor activity`, on the
  argument above.
- **`GO:0043571 maintenance of CRISPR repeat elements`** (IDA, PMID:27899566, from
  ComplexPortal CPX-996) — **ACCEPT**. The paper assays integration by the purified
  Cas1-2 complex at the leader-repeat junction
  [PMID:27899566 "Further, we show that the leader region abutting the first CRISPR repeat localizes IHF and Cas1-2 complex."]
  and states
  [PMID:27899566 "Cas1–2 complex alone is sufficient for the integration of protospacer elements"]
- **`GO:0043571`** (IMP, PMID:22402487) — **ACCEPT**. Directly supported by the
  Cas2-alone negative result quoted above. The `acts_upstream_of_or_within` qualifier
  is the appropriately cautious one for a knockout/overexpression phenotype.
- **`GO:0099048 CRISPR-cas system`** (IDA, PMID:27899566) — **ACCEPT**.

## `GO:0043571` vs `GO:0099048` placement across the pair

Checked against the ontology rather than assumed. The two terms are in **disjoint**
branches: `GO:0043571` descends from `GO:0043570` / `GO:0006259 DNA metabolic
process` / `GO:0051276 chromosome organization`, whereas `GO:0099048` descends from
`GO:0098542 defense response to other organism` / `GO:0006952 defense response`.
Neither is an ancestor of the other, so they are complementary (the DNA-level event
vs. the immune system it serves) and not redundant. Both genes legitimately carry
both, and nothing needs to move between ygbT and ygbF. ygbF's GOA is missing only the
IBA/IEA rows that ygbT has — an artefact of Cas2 being a short, poorly-conserved
family rather than a curation decision, and not something to fix by inventing `NEW`
rows.

## What I did not add

- No `NEW` molecular-function row for nuclease/ribonuclease activity: unsubstantiated
  for this protein (see adjudication above).
- No `NEW` row for `GO:0003677 DNA binding`: Cas2 does not bind DNA on its own, so a
  standalone `enables` assertion would be wrong. It appears only as
  `contributes_to_molecular_function` on the core function, which is what that slot is
  for.
- No `GO:0005737 cytoplasm` row: GOA has none for P45956, and while a cytoplasmic
  location is near-certain for an E. coli adaptation protein, none of the cached
  papers reports a localization experiment on Cas2. Asserting it would be inference
  dressed as evidence.
- No `GO:0051607 defense response to virus` row, for the same reason it is demoted on
  ygbT: for E. coli K-12 the native system is H-NS-silenced and no phage-protection
  phenotype has been shown for this gene.
