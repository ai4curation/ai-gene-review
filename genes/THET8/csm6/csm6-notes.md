# Thermus thermophilus HB8 Csm6 (Q53W17) — curation notes

## Identity and context

- UniProt Q53W17, reviewed (Swiss-Prot), 464 aa, locus TTHB152, encoded on plasmid pTT27
  in the same type III-A CRISPR locus as cas10/TTHB147. RecName "CRISPR system
  endoribonuclease Csm6"; AltName "TtCsm6" (ECO:0000303|PubMed:26763118).
- **No GOA annotations exist at all** (`csm6-goa.tsv` is header-only), yet this is one of
  the best-characterised Csm6 proteins: crystal structures (PDB 5FSH, 8JBB), seven
  MUTAGEN features with ECO:0000269 evidence, and a measured ~1000-fold allosteric
  activation. The absence of GO rows reflects an uncurated entry, not unknown function.
- Two-domain architecture, both regions assigned from the crystal structure:
  `REGION 1..190 CARF domain` and `REGION 191..464 HEPN domain`
  (ECO:0000305|PubMed:26763118).

## Csm6 is NOT a subunit of the effector complex

This is the single most important fact about the protein and the thing most easily lost if
it is annotated simply as "a ribonuclease". UniProt is explicit, in the FUNCTION block:

> The type III-A Csm effector complex binds crRNA and acts as a crRNA-guided RNase, DNase
> and cyclic oligoadenylate synthase; binding of target RNA cognate to the crRNA is
> required for all activities. **This protein is not part of the Csm effector complex**
> (Probable). {ECO:0000305}

[PMID:28663439 "In addition, Csm6, a ribonuclease that is not part of the complex, is also
required to provide full immunity."]

[PMID:28722012 "The CRISPR-associated protein Csm6 additionally contributes to interference
by functioning as a standalone RNase that degrades invader RNA transcripts, but the
mechanism linking invader sensing to Csm6 activity is not understood."]

So Csm6 is physically uncoupled from the sensing machinery. It is a free homodimer in the
cytoplasm that has to be told, by a diffusible chemical signal, that a target has been
detected somewhere else in the cell.

## The intrinsic ribonuclease

PMID:26763118 is cached with full text and is the primary characterisation.

[PMID:26763118 "Here we report the crystal structure of Csm6 from Thermus thermophilus and
show that the protein is a ssRNA-specific endoribonuclease."]

[PMID:26763118 "HEPN domain dimerization leads to the formation of a composite ribonuclease
active site."]

[PMID:26763118 "In the TtCsm6 structure, the floor of the HEPN domain cleft is lined with
side chains of the invariant residues Arg415, Asn416, and His422 from the R-X4-6-H motif."]

[PMID:26763118 "Individual substitutions of the HEPN domain residues led to near-complete
loss of ribonuclease activity, whereas mutations in the CARF domain had little effect"]

Metal independence and cleavage chemistry:

[PMID:26763118 "ssRNA cleavage by TtCsm6 was not perturbed by the addition of EDTA,
indicating that the activity of TtCsm6 does not require divalent metals."]

[PMID:26763118 "the 3′ products of Csm6-catalyzed phosphodiester bond hydrolysis carry a
free 5′-hydroxyl group"]

[PMID:26763118 "The observation that TtCsm6 is a metal-independent ribonuclease that
generates products containing a free 5′-hydroxyl group suggests that RNA hydrolysis involves
a nucleophilic attack by the 2′-hydroxyl group to yield a 2′,3′ cyclic phosphate"]

**Consequence for term choice.** Because the products carry a free 5'-OH, `GO:0016891` "RNA
endonuclease activity producing 5'-phosphomonoesters, hydrolytic mechanism" is positively
excluded. The sibling `GO:0016892` (3'-phosphomonoesters) is also not a clean fit, since the
3' product is a 2',3'-cyclic phosphate rather than a 3'-phosphomonoester, and the mechanism
is transesterification by the ribose 2'-OH rather than attack by water. The honest choice
is therefore the parent, `GO:0004521` RNA endonuclease activity, with the chemistry recorded
in prose; forcing GO:0016892 would assert a product the paper does not report. This is
raised in `suggested_questions`.

## The CARF domain is a regulatory module, not a catalytic one

PMID:26763118 established the negative half of this directly: the CARF domain is
dispensable for catalysis. UniProt's MUTAGEN features record it as

> MUTAGEN 1..190 /note="Missing: Wild-type ssRNase activity."
> MUTAGEN 133 /note="T->A: Wild-type ssRNase activity."
> MUTAGEN 137 /note="K->A: Wild-type ssRNase activity."

against the HEPN-domain substitutions E332A, R415A, N416A and H422A, each "No ssRNase
activity". The paper also flagged what the domain is probably for:

[PMID:26763118 "The dimer interface of the CARF domains features a conserved electropositive
pocket that may function as a ligand-binding site for allosteric control of ribonuclease
activity."]

That prediction was confirmed the following year, and this is the gene-defining fact:

[PMID:28663439 "Acting as signaling molecules, cyclic oligoadenylates bind Csm6 to activate
its nonspecific RNA degradation."]

[PMID:28722012 "Upon target RNA binding by the interference complex, its Cas10 subunit
converts ATP into a cyclic oligoadenylate product, which allosterically activates Csm6 by
binding to its CRISPR-associated Rossmann fold (CARF) domain."]

UniProt quantifies the effect for *this* protein, with experimental evidence, and records
the specificity:

> ACTIVITY REGULATION: Non-specific ssRNase activity is allosterically activated about
> 1000-fold by cyclic tetraadenylate (cA4), which probably binds to its CARF domain.
> {ECO:0000269|PubMed:28663439, ECO:0000305|PubMed:28722012}

> FUNCTION: ... Activity is approximately 1000-fold stimulated by cyclic oligoadenylate
> (cOA); only cyclic tetraadenylate (cA4) stimulates the ssRNase activity while linear
> oligoadenylates do not activate the RNase (PubMed:28663439).

Two points worth keeping straight. First, the ring is required: linear oligoadenylates do
not work, so this is recognition of a cyclic ligand and not merely of adenylate. Second,
the ~1000-fold figure and the cA4 selectivity were measured on *TtCsm6 itself*
(PMID:28663439 assayed the Thermus protein with chemically defined cOA species), whereas
the assignment of the binding site to the CARF domain of this particular protein is
inferential (ECO:0000305). UniProt also notes a discordant observation worth not papering
over: PubMed:28722012 saw stimulation by *linear* tetraadenylate at very high
concentrations but did not test cA4, so the two papers are not in genuine conflict.

## Ontology gap: no term for cyclic oligoadenylate binding

GO discriminates cyclic-nucleotide ligands at exactly this granularity and already has the
two bacterial dinucleotide cases, both placed under `GO:0030551` cyclic nucleotide binding:
`GO:0035438` cyclic-di-GMP binding and `GO:0180001` cyclic-di-AMP binding. There is no
corresponding term for cyclic oligoadenylate (cA3-cA6), the ligand of every CARF-domain
effector in type III CRISPR systems. `GO:0030551` itself cannot simply be used: its
definition is "Binding to a cyclic nucleotide, a nucleotide in which the phosphate group is
in diester linkage to two positions on the sugar residue", which describes cAMP and cGMP —
one sugar, an intramolecular ring. In cA4 each phosphate bridges *two different* riboses,
so the molecule does not satisfy that definition any more than c-di-GMP does, which is
precisely why GO:0035438 had to be created as a term in its own right rather than annotated
at the parent.

A `cyclic oligoadenylate binding` term is therefore the missing third member of an existing
series, and it is proposed here. The *activated state* itself does not need a term: the
chemistry Csm6 performs when switched on is ordinary RNA endonuclease activity, and
"allosterically activated" is a property of the regulation rather than a distinct molecular
function, so it belongs in prose and in `ACTIVITY REGULATION`-style commentary. What is
genuinely unrepresentable in GO today is the ligand-recognition function of the CARF domain.

`modules/crispr_cas_adaptive_immunity.yaml` (annoton `csm6_coa_activated_rnase`) assigns
GO:0004521 for the catalysis and records the cOA-activated state among its knowledge gaps.

## Comparator check for the process terms

Csm6 performs chemistry that is part of target interference — it degrades invader RNA
transcripts — so it is a participant in the process and not merely required for it. Every
curated Cas protein of the *E. coli* K-12 type I-E system in this repository carries
`GO:0099048` CRISPR-cas system (casA, casB, casC, casD, casE, cas1/ygbT, cas2/ygbF; IDA,
PMID:18703739), and casA/casE additionally carry `GO:0051607` defense response to virus
(IMP). Csm6 is annotated on that pattern. Both are coded conservatively: the immunity
requirement has been demonstrated for Csm6 orthologues in other species (anti-plasmid
immunity in the type III-A systems of PMID:26763118's introduction, and the in vivo CARF
mutants of PMID:28722012), not in *T. thermophilus* HB8, so ISS and IC are used rather than
IMP.

## Decisions

- GOA empty, so every row is `NEW`. The catalytic rows are IDA (measured on this protein in
  PMID:26763118); the process rows are ISS/IC.
- `GO:0004521` RNA endonuclease activity, not GO:0016891 or GO:0016892, for the reasons
  above.
- A second core function records the CARF domain's cOA-sensing role via
  `proposed_molecular_function`, because the activation dependency is the point of the
  protein and annotating only "ribonuclease" would misrepresent it as a constitutive
  nuclease.
