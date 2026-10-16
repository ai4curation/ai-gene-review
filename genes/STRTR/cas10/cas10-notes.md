# Streptococcus thermophilus Cas10/Csm1 (A0A0A7HFE1) — curation notes

## Identity and context

- UniProt A0A0A7HFE1, reviewed (Swiss-Prot), 758 aa. RecName "CRISPR system
  single-strand-specific deoxyribonuclease Cas10/Csm1 (subtype III-A)", short name
  StCas10, AltName "Cyclic oligoadenylate synthase" (EC 2.7.7.-, ECO:0000269).
- **No GOA annotations exist at all.** The entry is nonetheless the best-characterised
  Cas10 in UniProt: three of its four FUNCTION blocks, its COFACTOR block, its ACTIVITY
  REGULATION block, its SUBUNIT block, its DOMAIN block and two MUTAGEN features all
  carry ECO:0000269 experimental evidence.
- Domains: `REGION 1..82 HD domain` (ECO:0000305|PubMed:27105119) and
  `DOMAIN 509..647 GGDEF` (PROSITE-ProRule:PRU00095, ECO:0000305|PubMed:27105119).

**This is the orthologue in which cyclic oligoadenylate synthesis was demonstrated.**
It must not be conflated with Q53W19 (THET8, *Thermus thermophilus* HB8), where the same
activity is a curator inference coded ECO:0000305. The two reviews cite each organism's
own work; the mnemonics STRTR and THET8 are easy to transpose and the species names
differ by one letter.

## Demonstrated activities

### HD-domain single-stranded DNase (PMID:27105119)

[PMID:27105119 "base-pairing between crRNA and target RNA activates single-stranded DNA
(ssDNA) degradation by StCsm"]

[PMID:27105119 "ssDNase activity is confined to the HD-domain of Cas10"]

The activity is under two layers of control, both demonstrated in this organism. Temporal:
[PMID:27105119 "target RNA cleavage by the Csm3 RNase suppresses Cas10 DNase activity,
ensuring temporal control of DNA degradation"]. Self/non-self:
[PMID:27105119 "base-pairing between crRNA 5'-handle and target RNA 3'-flanking sequence
inhibits Cas10 ssDNase to prevent self-targeting"]. And spatial:
[PMID:27105119 "crRNA-guided StCsm binding to the emerging transcript recruits Cas10 DNase
to the actively transcribed phage DNA, resulting in degradation of both the transcript and
phage DNA, but not the host DNA"].

UniProt adds, with experimental evidence from the same paper, that the activity requires
Mn2+, Co2+ or Ni2+ and is not supported by Mg2+, Ca2+ or Zn2+, that it is inhibited by
EDTA, and that activity on dsDNA is low and not stimulated by the complex. The
single-strand specificity plus the demonstrated digestion of circular as well as linear
ssDNA (ECO:0000250|UniProtKB:B6YWB8) is what makes both an endonuclease and an
exonuclease term applicable.

### Palm/GGDEF-domain cyclic oligoadenylate synthase (PMID:28663439)

[PMID:28663439 "target RNA binding by the Csm effector complex of Streptococcus
thermophilus triggers Cas10 to synthesize cyclic oligoadenylates"]

[PMID:28663439 "Acting as signaling molecules, cyclic oligoadenylates bind Csm6 to
activate its nonspecific RNA degradation."]

UniProt records for this entry, with ECO:0000269|PubMed:28663439 throughout:

> FUNCTION: When associated with the ternary Csm effector complex ... synthesizes cyclic
> oligoadenylates (cOA) from ATP, producing cyclic triadenylate (cA3) up to cyclic
> hexaadenylate (cA6), which is the active cOA. The enzyme is also able to cyclize pppA3
> up to pppA6. ... Synthesis of cOA can occur with AMP plus ATP, 2'dATP or 3'dATP (but no
> other nucleotides), and requires a free 3'-OH ribose moiety.

> CATALYTIC ACTIVITY: Reaction=6 ATP = cyclic hexaadenylate + 6 diphosphate;
> Xref=Rhea:RHEA:58276 ... Evidence={ECO:0000269|PubMed:28663439}

The free-3'-OH requirement is itself the chemical signature that distinguishes this
reaction from the metazoan 2'-5'-OAS reaction, which links the 2'-OH.

### The two activities are genetically separable

UniProt's MUTAGEN features (both ECO:0000269|PubMed:27105119 and
ECO:0000269|PubMed:28663439) are the cleanest evidence that one protein carries two
independent catalytic centres:

> MUTAGEN 16: D->A: Dramatically decreased ssDNase activity. Wild-type synthesis of cOA.
> MUTAGEN 575..576: DD->AA: Wild-type ssDNase activity. No synthesis of cOA.

That reciprocal pattern is why this review records two separate core functions rather
than one composite activity.

### Complex membership (PMID:25458845, PMID:27105119, PMID:28663439)

UniProt SUBUNIT, ECO:0000269 from all three papers: "Part of the Csm effector complex that
includes at least Cas10(1), Csm2(3), Csm3(5), Csm4(1), Csm5(1) and mature crRNA", with
Cas10 and Csm4 capping one end of the Csm3 filament.

[PMID:25458845 "When expressed in Escherichia coli, two complexes of different
stoichiometry copurified with 40 and 72 nt crRNA species, respectively."]

[PMID:25458845 "In the heterologous E. coli host, StCsm restricts MS2 RNA phage in a Csm3
nuclease-dependent manner."]

Note what that last result does and does not show: it establishes that the *system*
restricts phage, and it attributes the restriction in that assay to the Csm3 RNase. It is
not a demonstration that Cas10 is required for immunity in vivo, so GO:0051607 is coded
IC here rather than IMP.

## Ontology gap

Identical to the Thermus case and argued at length in
`genes/THET8/cas10/cas10-notes.md`: GO has no term for cyclic oligoadenylate synthase
activity, `GO:0001730` 2'-5'-oligoadenylate synthetase activity is the metazoan OAS enzyme
and is the wrong term, and the right placement is as a sibling of `GO:0106408` diadenylate
cyclase activity and `GO:0052621` diguanylate cyclase activity under `GO:0016779`
nucleotidyltransferase activity. The same `proposed_new_terms` entry appears in both cas10
reviews; this one carries the experimental support (ECO:0000269 / IDA), the Thermus one the
inferred support (ECO:0000305 / ISS).

## Decisions

- GOA empty, so every row is `NEW`. Unlike the Thermus entry these are coded IDA, because
  the activities were measured on this protein and complex.
- GO:0051607 defense response to virus is coded IC and explained, not IMP.
- Complex membership recorded at GO:0032991, matching the convention used for the curated
  *E. coli* Cascade subunits, because GO has no Csm-complex term.
