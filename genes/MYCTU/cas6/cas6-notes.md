# Mycobacterium tuberculosis H37Rv Cas6 (P9WPJ1, Rv2824c) — curation notes

## Identity and context

- UniProt P9WPJ1, reviewed (Swiss-Prot), 314 aa, locus Rv2824c, at one end of the H37Rv
  type III-A CRISPR-Cas locus (cas6 to cas2, Rv2824c to Rv2816c). RecName
  "CRISPR-associated endoribonuclease Cas6", EC 3.1.-.- (ECO:0000269|PubMed:29979631).
  SIMILARITY: Cas6/Cse3/CasE family.
- Primary characterisation: PMID:29979631 (Wei et al., FASEB J 2019). Cached record is
  **abstract-only**, so the biochemical detail below is taken from the UniProt entry's
  ECO:0000269 annotations, which were made by a curator who read the full text.
- Mutagenesis recorded by UniProt: `MUTAGEN 99 H->A: Incorrect processing of pre-crRNA,
  binds pre-crRNA` and `MUTAGEN 295..297 GMG->AMA: Incorrect processing of pre-crRNA, no
  longer binds pre-crRNA`. The pair separates catalysis from substrate binding, and the
  H99 assignment identifies the catalytic histidine typical of the family.

## What the protein does

A standalone pre-crRNA processing endoribonuclease. UniProt FUNCTION, ECO:0000269:

> Processes pre-crRNA into individual crRNA units; accurate cleavage of pre-crRNA depends
> on a 3' stem-loop and the sequence of the bases in the stem. The mature crRNA is unusual
> for type III-A systems as it does not undergo 3' processing after Cas6 cleavage. Mature
> crRNA is about 71 nucleotides (nt long) with an 8 nt 5' handle and 28 nt repeat with a 10
> nt stem-loop at the 3' end.

[PMID:29979631 "Cas6 cleavage of repeat RNA is ion dependent, and accurate cleavage depends
on the presence of a 3' hairpin in the repeat RNA and the sequence of its stem base
nucleotides."]

[PMID:29979631 "crRNAs generated resemble mature crRNA in type I systems, having both 5' (8
nt) and 3' (28 nt) repeat tags."]

The enzyme has measured steady-state kinetics (UniProt BIOPHYSICOCHEMICAL PROPERTIES,
ECO:0000269): KM 8.395 µM for repeat pre-crRNA in 0.125 mM CaCl2, kcat 12.156 min-1. That
is a characterised enzyme, not a putative one.

**Standalone, not a retained subunit.** This is the point of contrast with the type I
enzymes in the same family. In *E. coli* K-12 the Cas6e orthologue (casE) is a structural
subunit of the Cascade surveillance complex and stays bound to the crRNA it made, and in
*P. aeruginosa* PA14 Cas6f/Csy4 likewise remains in the Csy complex. Here the mature crRNA
is handed to the Csm effector complex and Cas6 is not a component of it; UniProt also notes
for the Streptococcus system that Cas6 is "found associated with a subset of the Csm
complex", i.e. transiently rather than stoichiometrically.

Phenotypes, UniProt DISRUPTION PHENOTYPE, ECO:0000269|PubMed:29979631:

> Deletion of this gene alone blocks maturation of pre-crRNA. Deletion of the entire
> CRISPR-Cas locus (cas6 to cas2, Rv2824c to Rv2816c) decreases resistance to plasmids
> encoding spacer elements about 6-fold.

[PMID:29979631 "we show it is active in invader defense and has features atypical of type
III-A systems"]

Note carefully what the immunity phenotype is: resistance to *transformation with plasmids*
bearing matching spacers. It is not a phage-restriction assay, and it is a whole-locus
deletion rather than a cas6 deletion. So `GO:0051607` defense response to virus is **not**
annotated here, even though UniProt carries the Antiviral defense keyword; the cas6-specific
phenotype in this organism is loss of crRNA maturation, and the immunity phenotype is
anti-plasmid and locus-wide.

## The existing annotation and why it is modified

GOA holds exactly one row for P9WPJ1:

    GO:0016788  hydrolase activity, acting on ester bonds  IEA  GO_REF:0000002  InterPro:IPR010156

`GO:0016788` is defined as "Catalysis of the hydrolysis of any ester bond" and its only
parent is `GO:0016787` hydrolase activity. For a protein whose UniProt name is
"CRISPR-associated endoribonuclease Cas6", whose substrate, cleavage site, catalytic
histidine, kinetics and deletion phenotype are all known, that is several levels too
general — it does not even record that the substrate is a nucleic acid. The InterPro entry
that produced it, IPR010156, is itself named "CRISPR-associated endoribonuclease Cas6", so
the imprecision is in the InterPro2GO mapping rather than in the family assignment.

**Replacement: `GO:0004521` RNA endonuclease activity** — "Catalysis of the cleavage of
ester linkages within ribonucleic acid by creating internal breaks", with parents
`GO:0004519` endonuclease activity and `GO:0004540` RNA nuclease activity. It records
substrate class (RNA), mode (endonucleolytic) and chemistry, all three of which are
established for this protein.

Comparator check, which confirms this is the conventional term for the family rather than
an invention: *E. coli* K-12 casE (Cas6e) carries exactly `GO:0004521` by IDA
(PMID:18703739), alongside `GO:0003723` RNA binding (IDA, PMID:25103409), `GO:0099048`
CRISPR-cas system (IDA) and `GO:0006396` RNA processing (IMP). *P. aeruginosa* PA14 cas6f
carries `GO:0004519` endonuclease activity by the same InterPro route, i.e. one step more
specific than what MYCTU cas6 currently has.

Two more specific children were considered and rejected. `GO:0016891` (producing
5'-phosphomonoesters) and `GO:0016892` (producing 3'-phosphomonoesters, hydrolytic
mechanism) each assert a product chemistry; the cleavage products of M. tuberculosis Cas6
have not been characterised for their 5'/3' end chemistry in anything available here, and
Cas6-family enzymes typically leave a 2',3'-cyclic phosphate, which matches neither child
cleanly. Asserting either would state a result that has not been reported.

## Metal dependence: deliberately not annotated

Processing is ion dependent, Ca2+ and Mn2+ stimulate, and EDTA inhibits (UniProt COFACTOR
and ACTIVITY REGULATION, ECO:0000269). It is tempting to add `GO:0046872` metal ion binding,
but there is a competing explanation that the available evidence does not exclude: accurate
cleavage depends on a 3' hairpin and on its stem-base sequence, and divalent cations
stabilise RNA secondary structure. The ion requirement may therefore be a property of the
*substrate* rather than of the enzyme — which would be notable, since Cas6-family enzymes
are classically metal independent. Without a direct demonstration of metal binding by the
protein, no metal-binding annotation is made, and the question is raised in
`suggested_questions` instead.

## Ontology observation: no term for CRISPR RNA processing

The only available process term for what this enzyme does to RNA is the generic
`GO:0006396` RNA processing. `GO:0043571` maintenance of CRISPR repeat elements does mention
"transcription of the CRISPR repeat arrays into RNA and processing" in its definition, and
PA14 cas6f carries it, but it sits under `GO:0043570` maintenance of DNA repeat elements,
which is the wrong branch for an RNA-maturation step; using it for a processing
endoribonuclease asserts involvement in repeat-array maintenance. A specific "CRISPR RNA
processing" term as a child of GO:0006396 would resolve this, and GO already has
tRNA/rRNA/mRNA/snRNA processing children at that level. Raised as a question rather than
proposed as a term here, because the gap is not specific to this gene.

## Decisions

- `GO:0016788` → **MODIFY** to `GO:0004521`.
- Three `NEW` rows: `GO:0003723` RNA binding, `GO:0006396` RNA processing, `GO:0099048`
  CRISPR-cas system.
- No `GO:0051607` and no `GO:0046872`, for the reasons above.
