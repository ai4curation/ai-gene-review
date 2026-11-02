# cas3 (Cas2-3, Q02ML8) — Pseudomonas aeruginosa UCBPP-PA14 — curation notes

Deep research was unavailable in this environment (no provider API keys), so this file
is my own literature journal. Every assertion carries an inline PMID plus a verbatim
quote from the cached record in `publications/`.

## What this protein is

PA14_33340, 1076 aa, UniProt name "CRISPR-associated nuclease/helicase Cas3 subtype
I-F/YPEST". It is a **Cas2-Cas3 fusion**, not a bare Cas3:
[PMID:26586803 "A specific feature of type I-F systems is a fusion of cas2 and cas3
homologs, which are encoded on separate genes in other CRISPR"]. The InterPro
complement reflects this (IPR048823 `Cas3_I-F_Cas2`, IPR006483 Cas3-HD,
IPR027417 P-loop NTPase), and UniProt places an HD Cas3-type domain at 102–318 and a
DEAD-box motif at 576–579.

GOA for Q02ML8 is strikingly thin: **only** the CACAO IMP rows on
`GO:0043571`. No IEA at all — no InterPro2GO, no UniRule — even though the orthologue
P38036 (E. coli Cas3) carries nine molecular-function annotations. The most likely
reason is that the fused Cas2-3 architecture does not match the signatures the
pipelines key on. That is a curation gap, not a biological absence, and it is the main
thing this review has to fix.

## Role in the pathway

Cas3 is the destruction step: the Csy complex finds and verifies the target, then
recruits Cas3.
[PMID:28985564 "Formation of the R-loop in both Csy and the related Type I-E Cse
complexes triggers recruitment of the endonuclease Cas3, which degrades the target
dsDNA"]. The docking site is the Csy large subunit:
[PMID:32170016 "The Cas3 protein (P. aeruginosa) was proposed to interact with the
C-terminal helical bundle of Cas8f"].

This recruitment step is the target of the anti-CRISPR AcrIF3:
[PMID:26416740 "The third anti-CRISPR protein operates by binding to the Cas3
helicase-nuclease and preventing its recruitment to the DNA-bound CRISPR-Cas complex"].
The mechanism is structurally resolved on **this** protein:
[PMID:27455460 "we report the crystal structure of the anti-CRISPR protein AcrF3 in
complex with Pseudomonas aeruginosa Cas3 (PaCas3)"] and
[PMID:27455460 "locks PaCas3 in an ADP-bound form, blocks the entrance of the
DNA-binding tunnel in the helicase domain, and masks the linker region and C-terminal
domain of PaCas3, thereby preventing recruitment by Cascade and inhibiting the type I-F
CRISPR-Cas system"].

## Direct evidence for activities, in this protein

**DNA nuclease activity (IDA).** The cryo-EM/biochemistry study of the type I-F complex
reconstituted Csy + Cas3 + dsDNA in vitro with ATP and Mg(2+), and read out DNA
cleavage that is strictly Cas3-dependent — the no-Cas3 lane is the negative control:
[PMID:32170016 "WT AcrF9 inhibits the DNA binding and subsequent Cas3 recruitment of
the Csy complex, suppressing DNA degradation"] and, on relief of inhibition,
[PMID:32170016 "We found that these mutations result in much stronger DNA cleavage
activities of Cas3 compared to the WT AcrF6"]. The Csy complex came from the PA14
expression plasmid and the paper identifies the Cas3 as *P. aeruginosa* (quote above),
so this is direct evidence on the gene product being reviewed.

**ATP binding (IDA).** PaCas3 was crystallised with nucleotide bound — "locks PaCas3 in
an ADP-bound form" (quote above) — placing a bound adenine nucleotide in the helicase
domain of this protein.

**Both catalytic centres are required in vivo (IMP).** Point mutants in each domain
abolish function:
[PMID:26586803 "Point mutations introducing single amino acid substitutions in the
endonuclease (D124A) and helicase (D576N) domains of the Cas3 protein also prevented
spacer acquisition"], and independently
[PMID:21398535 "the core Cas protein Cas3 functions downstream of small crRNA
production and that this protein requires functional HD (predicted phosphohydrolase)
and DEXD/H (predicted helicase) domains to suppress biofilm formation in DMS3
lysogens"]. The Cas2 moiety is separately required:
[PMID:26586803 "A D124Oc mutation in the cas2+cas3 gene that introduced an ochre stop
codon instead of aspartate codon at position 124, after the cas2 portion of the fused
gene, abolished spacer acquisition"].

## Curation decisions

- `GO:0043571 maintenance of CRISPR repeat elements`, IMP,
  `acts_upstream_of_or_within_positive_effect` → ACCEPT. Well grounded: the Cas2-moiety
  truncation and both catalytic-domain point mutants abolish spacer acquisition. The
  hedged qualifier is the right one, because in type I-F the adaptation requirement is
  partly carried by the fused Cas2 domain and partly indirect (via the Csy complex and
  crRNA).

## Gaps identified (missing annotations)

Comparator check against E. coli Cas3 (P38036, `genes/ECOLI/ygcB/ygcB-goa.tsv`): it
holds `GO:0000014`, `GO:0008296`, `GO:0033677`, `GO:0003690`, `GO:0000287`,
`GO:0003724` and `GO:0005524`, all by IDA/EXP/IBA. PA14 Cas3 holds none. Every type I
system's Cas3 is the degradation nuclease, so a systematic absence here is one-protein
pipeline failure, not an ontology convention. Proposing, conservatively:

- `GO:0004536 DNA nuclease activity` (NEW, IDA, PMID:32170016). Deliberately the
  moderately specific term, not E. coli's `GO:0000014 single-stranded DNA endonuclease
  activity` or `GO:0008296 3'-5'-DNA exonuclease activity`: the in vitro assay used
  dsDNA presented by the Csy complex and did not resolve exo- versus endonucleolytic
  mode or strand preference **for this orthologue**. Asserting the E. coli-specific
  children would be transferring a result I cannot cite for PaCas3.
- `GO:0004386 helicase activity` (NEW, IMP, PMID:26586803 + PMID:21398535, with
  PMID:27455460 for the structure). The DEAD-box point mutant D576N abolishes function
  in vivo and the AcrF3 co-crystal shows a nucleotide-bound helicase domain with a
  DNA-binding tunnel. Again the generic term rather than E. coli's `GO:0033677 DNA/RNA
  helicase activity`: no unwinding assay on PaCas3 has established the substrate pairing.
- `GO:0005524 ATP binding` (NEW, IDA, PMID:27455460).
- `GO:0099048 CRISPR-cas system` (NEW, IMP, PMID:26586803). The term's definition names
  "target interference" as one of its three stages, which is the step Cas3 performs.
  Checked via QuickGO: not an ancestor or descendant of `GO:0043571`.

## Not proposed, and why

- `GO:0051607 defense response to virus`. E. coli Cas3 carries it by IMP and IDA, but
  the PA14-specific phenotype runs the other way:
  [PMID:21398535 "the Yersinia-subtype CRISPR region of Pseudomonas aeruginosa strain
  UCBPP-PA14 plays no detectable role in viral immunity but instead is required for
  bacteriophage DMS3-dependent inhibition of biofilm formation"]. Later work shows the
  locus *does* restrict other phages
  [PMID:23242138 "The CRISPR-sensitive phages fail to replicate on PA14 due to the
  action of the CRISPR/Cas system14, but are able to replicate on PA14"], but that is a
  whole-locus (ΔCR/cas) deletion, not a `cas3` allele. With a published negative result
  for this gene and no gene-specific positive one, I leave the term off and raise it as
  a question. `GO:0099048` carries the immunity role without the contested claim.
- `GO:0046872 metal ion binding` / `GO:0000287 magnesium ion binding`. UniProt's Mg(2+)
  sites at 124 and 220 are `ECO:0000255` (sequence-model) only, and I have no direct
  metal-binding measurement for PaCas3.
- The biofilm phenotype (DMS3-dependent loss of biofilm formation) is a strain- and
  prophage-specific downstream consequence of target recognition, not a function of
  Cas3. Recorded here, not annotated.
