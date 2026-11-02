# casB (Cse2), *Escherichia coli* K-12 — UniProt P76632

Curation journal. All assertions carry inline provenance as
`[PMID:xxxxxxx "verbatim supporting text"]`, copied verbatim from the cached records in
`publications/`.

## Session 1 (2026-10-01): initial full review

Reviewed together with casA, casC, casD and casE as one complex.

### Position in Cascade

CasB is present in two copies and forms a dimer that runs along the belly of the
complex, bridging the CasE-capped head and the CasA tail
[PMID:25103409 "The head and tail of the complex are connected along the belly by two Cse2 subunits and by a helical backbone of six Cas7 proteins"],
contacting the CasC (Cas7) backbone
[PMID:25103409 "The Cse2 proteins form a head-to-tail dimer that assembles along the belly of Cascade making contacts with the thumb and web of Cas7 proteins"].
UniProt P76632 SUBUNIT records the same: "Homodimer. Part of the Cascade
ribonucleoprotein complex ... Interacts directly with crRNA, CasA, CasC and CasE."

Note the discrepancy worth recording: the crystal structure explicitly states that CasB
does *not* touch the crRNA
[PMID:25103409 "Although the Cse2 subunits do not make direct contacts with the crRNA, electrostatic calculations show that both faces of the Cse2 dimer are positively charged, indicating a possible role for Cse2 in stabilizing the bound and displaced strands of the DNA target"],
whereas UniProt's SUBUNIT line (based on earlier biochemistry) says it interacts
directly with crRNA. I do not need to adjudicate this, because GOA holds no crRNA-binding
row for CasB; its nucleic-acid rows are about DNA and about generic nucleic acid.

### What CasB actually binds

The CasB-specific structural/biochemical paper assayed four CasB orthologues, including
*E. coli* P76632, by EMSA
[PMID:23079036 "All four CasB proteins were able to bind ds-DNA and ss-RNA."],
and found the binding to be non-selective
[PMID:23079036 "The lack of distinct banding pattern suggests that these four CasB proteins are best characterized as non-specific nucleic acid binding proteins."],
with a preference for duplex
[PMID:23079036 "In each case, CasB's affinity for ds-DNA appeared to be higher than ss-RNA, implying that CasB may have a preference for duplexed nucleic acid."].
The binding surface is a conserved basic patch, confirmed by mutagenesis
[PMID:23079036 "The ds-DNA binding affinity of TfuCasB2 mutants 1, 2 and 3 were reduced by approximately 32-fold"].

This is why I keep GOA's GO:0003676 **nucleic acid binding** at the parent level rather
than pushing it down to DNA binding: the experiment that supports it deliberately
establishes non-specificity across DNA and RNA, so the parent is the honest term. The
separate GO:0003677 DNA binding row rests on different, structural evidence and is kept
as well — the two rows are not redundant duplicates but complementary statements at
different levels from different experiments.

The structural DNA evidence is specific. In the target-bound complex CasB residues grip
individual displaced (non-target-strand) nucleotides
[PMID:25123481 "The second and fourth displaced DNA nucleotides (positions 12 and 24) stack with His123 and contact Arg101 from either Cse2.2 or Cse2.1, respectively"],
CasB lines the basic groove that accommodates the displaced strand
[PMID:25123481 "the groove is lined with conserved basic residues from Cas7 (Lys34, Lys299 and Lys301) and Cse2 (Arg53, Arg142, Arg143 and Arg110)"],
and the CasB dimer forms one wall of the channel the target sits in
[PMID:25123481 "The ssDNA target is juxtaposed to the guide region of the crRNA in a groove formed by the Cas7 filament, the four-helix bundle of Cse1, and the Cse2 dimer"].
So CasB's job is R-loop stabilisation: it holds the strand that crRNA invasion displaces.

### The structural-subunit problem, and how I resolved it

GOA gives CasB two `GO:0005515 protein binding` IDA rows (one from the Cascade
purification, one from the crystal structure) and nothing else about its role in the
complex. CLAUDE.md forbids treating `protein binding` as informative. The options were:

- **nucleic-acid-binding only** — loses the fact that CasB is two-thirds of the
  head-to-tail connection in the complex;
- **an explicit ontology gap** — overkill, because a fitting term does exist;
- **structural constituent** — GO:0005198 structural molecule activity, "The action of a
  molecule that contributes to the structural integrity of a complex". There is no child
  for a non-ribosomal RNP (the children are ribosome, proteasome, virion, chromatin,
  nuclear pore, etc.), so the parent is the correct level.

I took the third option, and applied the *same* replacement to the equivalent
intra-complex `protein binding` rows on casA, casC, casD and casE, so the five subunits
come out consistent. CasB's structural role is directly stated in the structure
[PMID:25103409 "The Cse2 proteins form a head-to-tail dimer that assembles along the belly of Cascade making contacts with the thumb and web of Cas7 proteins"].

I did **not** invent a term for crRNA-guided target recognition or for R-loop
stabilisation; those gaps are recorded in `suggested_questions` and in
`modules/crispr_cas_adaptive_immunity.yaml`.

### Requirement for immunity

CasB is essential for the pathway, not merely a passenger
[PMID:23079036 "deletion of E. coli CasB leads to the loss of resistance against phage λ infection"],
consistent with Cascade as a whole
[PMID:18703739 "The phage resistance phenotype was lost when Cascade was omitted"].
Brouns also noted that crRNA *accumulates* in the casB knockout
[PMID:18703739 "The same product was present in much higher amounts in the casA, casB, and casC knockout strains but absent from strains lacking the overlapping genes casD and casE"],
i.e. CasB is not needed for processing; it is needed for interference. That is why CasB
gets no crRNA-biogenesis process term here.

### Complex term

Same decision as the other four subunits: GO:0032991 is the bare root of the complex
branch, and Cascade is demonstrably a ribonucleoprotein
[PMID:23079036 "The E. coli Cascade complex is a 405 KDa ribonucleoprotein complex assembled from crRNA and five functionally essential Cse proteins"],
[PMID:25103409 "both assemblies consist of 11 protein subunits and a single 61-nt crRNA that traverses the length of the complex"],
so I MODIFY to GO:1990904 ribonucleoprotein complex. GO has no CC term for Cascade or
any CRISPR surveillance complex — a QuickGO ontology search for "CRISPR" returns five
terms, all biological_process — so I also propose the missing term.
