# pcs (PA3857, Q9HXE9) review notes

## A well-settled gene

This is the least contentious review in the batch. Pcs is a reviewed entry at `PE 1: Evidence at
protein level`, with `EC=2.7.8.24` carrying `ECO:0000269` from two publications, a catalytic
activity tied to RHEA:14597, eight transmembrane helices, and a dedicated NCBIfam model
(`NF045887; PhCholSynPs`). All five `GO:0050520` rows and all three `GO:0008654` rows say the
same correct thing by different routes.

The biology: bacteria make phosphatidylcholine by two routes, and
[PMID:14663079 "important pathogens such as Brucella melitensis, P. aeruginosa and Borrelia
burgdorferi seem to be exceptional as they possess only the PCS pathway for PC formation."] —
*P. aeruginosa* has no working methylation route, so Pcs is the organism's only way to make PC.
[PMID:12169604 "Although the pathway for synthesizing PC by use of Pcs is functional in P.
aeruginosa, it does not appear that this organism uses the PmtA pathway for PC synthesis."]

The genetics is equally clean:
[PMID:22363496 "The PAO1 and PA14 Δpcs mutants completely lacked PC, and these defects were
complemented by expression of the pcs gene from a separate genomic location (Fig."]

## Two things worth recording rather than acting on

**The enzyme depends on an exogenous substrate.** Pcs condenses choline directly with
CDP-diacylglycerol, and *P. aeruginosa* does not make choline:
[PMID:22363496 "In all the strains tested, PC synthesis occurred only when choline is provided
exogenously."] So the gene's product is an enzyme whose reaction only runs when the environment
supplies one of the substrates. That is unusual enough to be worth a question, and it is probably
why the mutant has no phenotype in the laboratory.

**The mutant has no phenotype.** PMID:22363496 looked hard and found nothing — antibiotic and
antimicrobial-peptide sensitivity, motility, biofilm formation, surface colonisation, a mouse
infection model, and a global phenotypic microarray all came out the same as wild type. The
authors' reading is that
[PMID:22363496 "Membrane PC may serve a highly specific role during P. aeruginosa interactions
with its eukaryotic hosts based on all the clinical strains tested retaining the ability to
synthesize it during availability of choline."] This is a genuine biological unknown — why a
conserved, functional pathway is retained with no measurable benefit — and is recorded as a
knowledge gap.

Neither observation bears on the annotations: a gene with no mutant phenotype can still have a
perfectly well-established molecular function, and here it does.

## Evidence-code note, not filed as a defect

PseudoCAP codes `GO:0050520` from PMID:12169604 as **IMP**, while UniProt codes the same term from
the same paper as **IDA**. The abstract of that paper describes cloning, heterologous expression
and lipid analysis rather than a *pcs* mutant, which would favour UniProt's reading, but the full
text is not cached (`full_text_available: false`) and the paper may well contain mutant work. Left
as an observation here rather than filed, since the unread text could settle it either way; the
later paper, PMID:22363496, supplies an unambiguous in-frame deletion with complementation, so an
IMP on this gene is in any case correct for that row.

## Granularity

- `GO:0016780` phosphotransferase activity, for other substituted phosphate groups is the CDP-alcohol
  phosphatidyltransferase class term, mapped from `IPR000462`. It is an ancestor of the accepted
  `GO:0050520`, and its supporting signature covers the whole class-I family — enzymes that
  transfer the phosphatidyl group to serine, glycerophosphate, inositol and choline alike. The
  specific acceptor is what the gene is about, so the class term is `TOO_GENERAL`.
- `GO:0016020` membrane, from the same signature, is the standard example of a term imprecise on
  its own: the entry places the protein in the inner membrane and `GO:0005886` is asserted on two
  other rows.
