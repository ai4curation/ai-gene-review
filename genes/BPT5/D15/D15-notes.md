# D15 (Escherichia phage T5 flap endonuclease / 5'-3' exonuclease, P06229) — curation notes

**Provenance note.** No deep-research provider was available in this container (no API
keys), so `just deep-research` was not run and no `-deep-research-<provider>.md` file
exists for this gene. The notes below were assembled by reading the cached publications
in `publications/`, the UniProt flat file (`D15-uniprot.txt`), and PubMed/PMC via the
PubMed MCP tools. Of the eleven cited papers only PMID:27273516 has
`full_text_available: true`; the rest are abstract-only in the cache. PMC holds scanned
images only for the three oldest papers (PMC427268, PMC515921, PMC15089 return empty
`full_text`), so for those the abstract is the whole readable record.
The GONUTS wiki (`gowiki.tamu.edu`), which would record the CACAO students' evidence,
was queried on 2026-10-29 for `PMID:6248541` and returned only
"This site is temporarily offline while we perform upgrades", matching the status
recorded in `projects/CACAO.md`.

## What the protein is

A 291-residue early phage protein, N-terminally processed by the host
(`FT INIT_MET 1 /note="Removed; by host"`, ECO:0000269|PubMed:2211703). It is the
founder-type member of the FEN / 5'-nuclease family (Pfam PF01367 `5_3_exonuc` +
PF02739 `5_3_exonuc_N`, HAMAP MF_04140 `FEN_T5`, InterPro IPR043666 `FEN_D15-like`),
homologous to the 5'-3' exonuclease domain of *E. coli* DNA polymerase I:

> [PMID:2211703 "shows a high degree of homology with the first 320 amino acid residues of Escherichia coli DNA polymerase I, the region containing the enzyme's 5'-3' exonuclease activity"]

Structurally it is a two-lobed PIN-like nuclease with a **helical arch** (residues
82–116) forming a hole over the active site and an H3TH DNA-binding motif (188–224).
Crystal structures of substrate and product complexes show single-stranded DNA
**threaded** through that hole:

> [PMID:27273516 "They reveal single-stranded DNA threading through a hole in the enzyme, which is enclosed by an inverted V-shaped helical arch straddling the active site."]

The same paper confirms the gene identity of the protein it crystallised:
> [PMID:27273516 "also known as the gene D15 product, accession number NC_005859.1"]

## Catalysis

Two activities in one active site, distinguishable by mutation, pH and metal occupancy.

1. **5'-3' exonuclease (EC 3.1.11.3)** on duplex and on single-stranded/denatured DNA:
   > [PMID:2211703 "The purified enzyme is active on both native and heat-denatured DNA"]
   > [PMID:17559871 "Flap endonucleases (FENs) catalyse the exonucleolytic hydrolysis of blunt-ended duplex DNA substrates"]
2. **Structure-specific (flap) endonuclease** at the junction of single- and
   double-stranded DNA:
   > [PMID:17559871 "the endonucleolytic cleavage of 5'-bifurcated nucleic acids at the junction formed between single and double-stranded DNA"]

The two are mechanistically separable:
> [PMID:9874768 "Biochemical analysis demonstrated that K83 is absolutely required for exonucleolytic activity on single-stranded DNA but is not required for endonucleolytic cleavage of flap structures."]
> [PMID:9874768 "The wild-type protein has different pH optima for endonuclease and exonuclease activities."]
> [PMID:15077103 "Mutation of crucial aspartates in site II abolished exonuclease action, but caused enzymes to retain structure-specific (flap endonuclease) activity."]

Metals are obligatory cofactors and their stoichiometry selects the reaction:
> [PMID:15077103 "Structure-specific endonuclease activity requires binding of a single metal ion in the high-affinity site, whereas exonuclease activity requires that both the high- and low-affinity sites be occupied by divalent cofactor."]
> [PMID:27273516 "A third magnesium ion (M3) was bound in Cat2."]
> [PMID:27273516 "A potassium ion was bound via backbone carbonyl oxygens within this motif."]

UniProt records the same, with the caveat that the endo/exo switching by metal
concentration is an in-vitro observation:
> [file:BPT5/D15/D15-uniprot.txt "In vitro low metal concentrations selectively stimulate the endonuclease reaction."]

## DNA binding is structure-selective, not generic

> [PMID:9380501 "Binding of T5 exonuclease to either blunt-ended duplexes or single-stranded oligonucleotides could not be detected by EMSA. However, duplexes with 5'-overhangs, flaps and pseudo-Y structures showed decreased mobility with added T5 exonuclease."]
> [file:BPT5/D15/D15-uniprot.txt "K->A: No exonuclease activity, retains full endonuclease activity on a flap structure. Binds DNA pseudo-Y substrates with a dissociation constant of 200 nM."]

This is why the bare `GO:0003677 DNA binding` IEA understates what is known: the
informative claims are Y-form (pseudo-Y) and 5'-flap-structured DNA binding.

## Role in the phage

- D15 is an **early** protein: [file:BPT5/D15/D15-uniprot.txt "Expressed in the early phase of the viral replicative cycle."]
- It is genetically **essential for T5 DNA replication**, and `D15` amber mutants also
  fail to make late proteins:
  > [PMID:4357874 "Amber mutants of bacteriophage T5 defective in gene D15, which codes for a 5'-exonuclease, do not express late genes."]
  > [PMID:4357874 "It is proposed that one requirement for the expression of late T5 genes is the introduction of gaps or nicks in the T5 DNA so that late transcription can occur."]
  The late-gene defect is therefore a **downstream consequence of a DNA-processing
  defect**, on the authors' own reading: the nuclease makes the template competent;
  transcription itself is carried out by host RNA polymerase with the phage gpC2
  controlling element. D15 performs no step of transcription.
- Maturation of replicated concatemers needs D15 for one specific step:
  > [PMID:904023 "The formation of unit-length, single-stranded DNA chains does not require the early T5 gene D15 nuclease: however, the subsequent formation of the single-stranded fragments does require that the D15 nuclease be functional."]
- Co-purifies with a large phage/host assembly containing host RNA polymerase, the T5
  DNA polymerase gpD9, the DNA-binding protein gpD5 and gpC2:
  > [PMID:6248541 "the proteins gpD5 (DNA-binding protein), and gpD15 (nuclease) which are both known to be essential for T5 DNA replication and for the initiation of late transcription"]
  The authors label it "putative" and it was isolated as a ~5 MDa species from infected
  cells; there is no reconstitution or stoichiometry, and no later confirmation that I
  could find. It is the only cellular-component evidence for this protein.

## A tension in the literature worth recording

Moyer & Rothe reported that purified D15 nicks duplex T5 DNA provided a single-strand
interruption is already present:
> [PMID:904023 "the enzyme can also introduce endonucleolytic scissions into mature T5 DNA in a reaction that requires duplex T5 DNA and preexisting, single-stranded interruptions"]

whereas Sayers & Eckstein, with homogeneous overexpressed enzyme, found none on either
closed-circular or nicked duplex:
> [PMID:2211703 "shows no endonuclease activity on either double-stranded closed-circular or nicked DNA"]

Both are consistent with a strictly structure-specific enzyme that needs a free,
single-stranded 5' end (a flap, a 5' overhang or a gapped/pseudo-Y junction) rather than
a nick as such — which is how UniProt states it:
> [file:BPT5/D15/D15-uniprot.txt "The substrates require a free, single-stranded 5' end, with endonucleolytic hydrolysis occurring at the junction of double- and single-stranded DNA"]

So a bare "double-stranded DNA endonuclease" claim (the CACAO `GO:1990238` row) is the
weakest form of the real finding and is partly contradicted by the 1990 study;
`GO:0017108 5'-flap endonuclease activity` is what the body of work supports.

## Reagent-versus-physiology caution

T5 exonuclease is a widely sold laboratory reagent (seamless-cloning/assembly mixes,
removal of linear or nicked DNA), and the FEN family's best-known member in
biotechnology is the Taq polymerase 5'-nuclease domain:
> [PMID:27273516 "FEN homologs such as Taq polymerase are also central to real-time quantitative PCR and clinical diagnostics"]

Nothing in the GOA set is sourced from a reagent datasheet, but two reagent-adjacent
framings do reach the annotations and were treated carefully in the review:
`GO:0033567 DNA replication, Okazaki fragment processing`, which arrives by HAMAP rule
and is hedged even in UniProt
([file:BPT5/D15/D15-uniprot.txt "This function may be used for example to trim such branched molecules generated by Okazaki fragments synthesis during replication."]),
and the habit of describing the enzyme generically as a "dsDNA exonuclease/endonuclease"
as the datasheets do, which loses the structure specificity that the mutagenesis and
structural work establish.

## Review tally

All 38 GOA rows reviewed: 16 ACCEPT (the six `GO:0017108` rows, the eight `GO:0051908`
rows, `GO:0035312` and `GO:0039693`), 13 MODIFY, 6 TOO_GENERAL (the `catalytic activity`
/ `nuclease` / `endonuclease` / `exonuclease` / `hydrolase` /
`catalytic activity, acting on DNA` ancestors), 2 MARK_AS_OVER_ANNOTATED
(`GO:0019086`, `GO:0033567`), 1 KEEP_AS_NON_CORE (`GO:0019034`). No REMOVE and no NEW
rows: nothing in the set is false, and nothing the literature supports is missing from it
once the generic terms are refined.

## CACAO rows (ASSIGNED BY = CACAO in the GOA file)

| Term | Evidence | PMID | Action | One-line reading |
|---|---|---|---|---|
| GO:0019034 viral replication complex | IMP | 6248541 | KEEP_AS_NON_CORE | One crude co-purification the authors themselves call "putative"; claim plausible, peripheral, and the evidence is co-isolation (IDA/IPI-shaped), not a mutant phenotype |
| GO:0019086 late viral transcription | IMP | 4357874 | MARK_AS_OVER_ANNOTATED | Phenotype read as process: amber mutant makes no late proteins, but the paper's own model is that D15 nicks the template; host RNAP transcribes |
| GO:0035312 5'-3' DNA exonuclease activity | IMP | 9874768 | ACCEPT | Exactly what the mutagenesis shows (K83A kills exonucleolysis); and it adds the ssDNA substrate range that the dsDNA-specific GO:0051908 rows do not cover |
| GO:1990238 double-stranded DNA endonuclease activity | IDA | 904023 | MODIFY → GO:0017108 | Right paper, right protein, but the term drops the structure specificity and the bare claim is contradicted by PMID:2211703 |

Two of the four are sound as claims (one accepted outright); the other two are the
project's known shapes — **phenotype read as process** and a **non-specific term for a
structure-specific activity** (a granularity failure, not a false claim). Note also an
evidence-code oddity in the `GO:0019034` row: `IMP` is used for what the cited paper
reports as a biochemical co-isolation; recorded as a `source_defects` entry rather than
argued in prose.
