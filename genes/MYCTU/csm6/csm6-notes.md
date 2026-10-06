# Mycobacterium tuberculosis H37Rv Csm6 (P71635, Rv2818c) — curation notes

## Identity and context

- UniProt P71635, reviewed (Swiss-Prot), 415 aa, locus Rv2818c, inside the H37Rv type
  III-A CRISPR-Cas locus (cas6 to cas2, Rv2824c to Rv2816c). RecName "CRISPR system
  endoribonuclease Csm6", AltName "CRISPR type III-A associated protein Csm6", EC 3.1.-.-.
- **No GOA annotations exist at all** (`csm6-goa.tsv` is header-only).
- Domain architecture, assigned by similarity to the Thermus orthologue
  (ECO:0000250|UniProtKB:Q53W17): `REGION 1..148 CARF domain`,
  `REGION 149..415 HEPN domain`. Homodimer, with the composite ssRNase active site at the
  dimer interface, likewise by similarity to Q53W17.
- SEQUENCE CAUTION: CCP45618.1 has a truncated N-terminus (erroneous initiation). Relevant
  only in that CARF-domain boundaries depend on the correct start.

## Evidence status: this entry is almost entirely inferred

Unlike the Thermus (Q53W17) and Streptococcus (A0A0A7HIX6) Csm6 proteins, the M.
tuberculosis protein has not been assayed. Every functional statement in the UniProt entry
that concerns the protein itself is coded ECO:0000250:

> FUNCTION: ... This subunit is a single-strand-specific endoribonuclease (ssRNase) that is
> stimulated by cyclic oligoadenylates (cOA) produced by the Cas10 subunit of the Csm
> effector complex (By similarity). {ECO:0000250|UniProtKB:A0A0A7HIX6,
> ECO:0000269|PubMed:29979631, ECO:0000305|PubMed:29979631}

> ACTIVITY REGULATION: Non-specific ssRNase activity is allosterically activated by cyclic
> oligoadenylates (cOA), a second messenger produced by Cas10 of the ternary Csm effector
> complex in the presence of a cognate target RNA. {ECO:0000250|UniProtKB:A0A0A7HIX6}

> SUBUNIT: Homodimer; the composite ssRNase active site is formed at the dimer interface.
> {ECO:0000250|UniProtKB:Q53W17}

> DOMAIN: The N-terminal CRISPR-associated Rossman fold (CARF) probably binds the cOA
> effector. ssRNase activity resides in the C-terminal HEPN domain.
> {ECO:0000250|UniProtKB:Q53W17}

The single ECO:0000269 fact available for this entry is the whole-locus phenotype:

> DISRUPTION PHENOTYPE: Deletion of the entire CRISPR-Cas locus (cas6 to cas2, Rv2824c to
> Rv2816c) decreases resistance to plasmids encoding spacer elements about 6-fold.
> {ECO:0000269|PubMed:29979631}

[PMID:29979631 "we show it is active in invader defense and has features atypical of type
III-A systems"]

So every annotation in this review is coded **ISS**, with the characterised orthologues
named in `supporting_entities`. That is the honest reading of the entry and not a
downgrade: the inference is a sound one (the CARF-HEPN architecture is the family
signature, and the HEPN R-X4-6-H motif is what makes the enzyme an enzyme), but it is an
inference.

## The source of the inference

The functions transferred here were established on the orthologues, and the relevant
evidence is set out in `genes/THET8/csm6/csm6-notes.md`. In brief:

[PMID:26763118 "Here we report the crystal structure of Csm6 from Thermus thermophilus and
show that the protein is a ssRNA-specific endoribonuclease."]

[PMID:26763118 "HEPN domain dimerization leads to the formation of a composite ribonuclease
active site."]

[PMID:28722012 "Upon target RNA binding by the interference complex, its Cas10 subunit
converts ATP into a cyclic oligoadenylate product, which allosterically activates Csm6 by
binding to its CRISPR-associated Rossmann fold (CARF) domain."]

[PMID:28663439 "In addition, Csm6, a ribonuclease that is not part of the complex, is also
required to provide full immunity."]

[PMID:28663439 "Acting as signaling molecules, cyclic oligoadenylates bind Csm6 to activate
its nonspecific RNA degradation."]

Note that the locus contains the partner this inference requires: Rv2824c is cas6
(P9WPJ1, the processing endoribonuclease, reviewed separately in `genes/MYCTU/cas6/`), and
the locus is a complete type III-A system including a cas10, so the cOA source that would
activate Csm6 is present in the same organism rather than being assumed from elsewhere.

## Not a subunit of the effector complex

As in the Thermus case, the defining structural fact is a negative one. Csm6 is a free
homodimer, physically separate from the Csm effector complex that senses the invader, and
the only thing connecting the two is the diffusible cyclic oligoadenylate. The annotation
set reflects this: there is no complex-membership row, in deliberate contrast with cas10,
which does get one.

Equally, the review does not record Csm6 merely as "a ribonuclease". A constitutively
active non-specific RNase would be a suicide gene; what the protein is for is to be
*silent until signalled*, and the CARF domain's ligand recognition is therefore treated as
a core function in its own right rather than as a footnote to the nuclease.

## No defense-response-to-virus annotation

UniProt carries the Antiviral defense keyword, but the only immunity phenotype measured in
this organism is reduced resistance to transformation with spacer-matching plasmids, from a
whole-locus deletion. There is no phage-restriction experiment in M. tuberculosis and no
csm6-specific phenotype at all. `GO:0051607` is therefore not annotated here, which is the
same decision taken for the MYCTU cas6 entry and differs from the Thermus csm6 review,
where PMID:28663439's statement about preventing phage infection and propagation supports
an IC annotation. Consistency on this point matters more than matching the keyword.

## Ontology gap

Identical to the Thermus case and argued in full in `genes/THET8/csm6/csm6-notes.md`: GO
has terms for binding the two bacterial cyclic dinucleotides (`GO:0035438` cyclic-di-GMP
binding, `GO:0180001` cyclic-di-AMP binding) but none for cyclic oligoadenylate, the
ligand of every CARF-domain effector; the parent `GO:0030551` cyclic nucleotide binding
cannot stand in, because its definition requires the phosphate to be in diester linkage to
two positions on a *single* sugar. The same `proposed_new_terms` entry appears in both csm6
reviews. The activated state itself needs no term: the chemistry is ordinary RNA
endonuclease activity (`GO:0004521`), and allosteric activation is a property of the
regulation.

## Decisions

- GOA empty, so every row is `NEW`, and every row is `ISS` with Q53W17 and A0A0A7HIX6 as
  supporting entities, mirroring UniProt's own ECO:0000250 codes.
- Two core functions: the HEPN-domain ssRNase (`GO:0004521`) and the CARF-domain cOA
  sensor (`proposed_molecular_function`).
- No `GO:0051607`, no complex-membership row.
