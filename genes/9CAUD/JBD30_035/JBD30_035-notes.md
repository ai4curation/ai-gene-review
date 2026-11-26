# JBD30_035 (UniProt L7P7M1) — AcrIF1 / AcrF1 of Pseudomonas phage JBD30

## Provenance note on this file

Deep research was **unavailable** for this review: no deep-research API keys exist in
this container, so `just deep-research` was not run and no `-deep-research-<provider>.md`
file exists or was fabricated. The literature below was assembled by hand from the
cached publications in `publications/`, the UniProt record, QuickGO and the primary
papers.

The GONUTS wiki (`gowiki.tamu.edu`), the source of the CACAO annotation and the usual
fallback for abstract-only CACAO rows, is **no longer merely offline: it has been
retired**. As of 2026-11-01 `https://gowiki.tamu.edu/wiki/index.php/Main_Page` returns
**HTTP 410 Gone** with the page "GONUTS, the GO wiki, has been retired" ("The GO wiki
that was at gowiki.tamu.edu is no longer online"), pointing visitors to
geneontology.org and noting that EcoliWiki and OMP remain. `web.archive.org` is
blocked by this container's egress policy, so no snapshot of the GONUTS page for
L7P7M1 could be retrieved either. The CACAO project page records the earlier
"temporarily offline while we perform upgrades" message (2026-10-29); the status has
changed from temporary to permanent, which means the per-paper and per-protein GONUTS
pages are not a recoverable evidence source for any future CACAO batch.

## Identity: this entry is AcrF1 (AcrIF1)

L7P7M1 is the product of gene 35 of *Pseudomonas* phage JBD30, 78 residues, and is the
founding type-I-F anti-CRISPR protein AcrF1/AcrIF1:

- UniProt cross-references the entry to CDD `cd22279` named `AcrIF1` and to Pfam
  `PF20829` `Acr30-35_AcrF1` [file:9CAUD/JBD30_035/JBD30_035-uniprot.txt
  "DR   CDD; cd22279; AcrIF1; 1."].
- The NMR structure PDB 2LW5 (chain A, residues 1-78) of this entry was deposited under
  the title "Discovery of phage genes that allow evasion of the CRISPR/Cas bacterial
  immune system" by Bondy-Denomy, Maxwell, Pawluk and Davidson, the authors of the
  discovery paper.
- The discovery paper identifies JBD30 gene 35 as the phage's anti-CRISPR gene
  [PMID:23242138 "We addressed this issue by performing experiments on JBD30 gene 35."]
  and shows the gene is required for the phage to grow on a CRISPR-proficient host
  [PMID:23242138 "a frameshift mutation was introduced into the phage JBD30 anti-CRISPR
  gene (gene 35). This mutant phage was unable to replicate on wild-type PA14 but still
  replicated robustly on the ΔCR/cas strain, demonstrating the requirement of the
  anti-CRISPR gene for replication"].
- The size matches: [PMID:28340349 "AcrF1 is a small protein (78 residues) composed of a
  four-stranded antiparallel β-sheet, flanked on one side by two α-helices"].

Host: *Pseudomonas aeruginosa* UCBPP-PA14, which carries a type I-F (Csy) CRISPR-Cas
system.

## Mechanism: AcrF1 itself inactivates the host surveillance complex

- Discovery/phenotype: five distinct anti-CRISPR genes in *P. aeruginosa* phages
  [PMID:23242138 "Mutation of the anti-CRISPR gene of a phage rendered it unable to
  infect bacteria with a functional CRISPR/Cas system"]. Expression of the gene does
  not reduce crRNA levels or cas gene expression, so the mechanism is post-expression.
- Biochemistry: AcrF1 is one of the two Acrs that block the DNA-binding step
  [PMID:26416740 "Two block the DNA-binding activity of the CRISPR-Cas complex, yet do
  this by interacting with different protein subunits, and using steric or non-steric
  modes of inhibition."] (abstract-only cache; the two are AcrF1 and AcrF2, the third is
  AcrF3 acting on Cas3).
- Structure: [PMID:28340349 "AcrF1 binds to the Cas7f backbone and prevents target
  binding"], and [PMID:28340349 "The structure presented here explains how two AcrF1
  proteins (i.e. AcrF1.1 and 1.2) bind to one Csy complex through interactions with four
  of the six Cas7f subunits"]; sterically, [PMID:28340349 "AcrF1 proteins sits on top of
  the Cas7.6f and Cas7.4f thumbs, blocking the transition of target DNA from 1 to 2 and
  segment 3 to 4, respectively."]. Cas7f is Csy3 (UniProtKB:Q02MM1 in PA14). Independent
  structures: PMID:28985564, PMID:28574055 (not cached), both cross-referenced from the
  UniProt entry (PDB 6ANV/6B46 and 5XLO/5XLP).

So AcrF1 is not a regulator acting upstream of suppression: it is the physical agent of
suppression, a stoichiometric binder that occludes the target-DNA path on the Csy
surveillance ribonucleoprotein.

## The CACAO row's paper: PMID:26586803 (Vorontsova et al. 2015)

Full text cached. The paper's subject is type I-F **adaptation** (spacer acquisition),
reconstituted in *E. coli* carrying plasmids for the PA14 cas and csy genes, and shows
acquisition needs the whole interference machinery. The AcrF1-relevant experiment:

- [PMID:26586803 "To determine if anti-CRISPR proteins also affect spacer acquisition we
  transformed E. coli (KD604) cells harboring pCas and pCsy plasmids with compatible
  plasmids expressing distinct anti-CRISPR proteins and monitored spacer acquisition
  (Figure 4)."]
- [PMID:26586803 "Spacer acquisition was inhibited in the presence of each of the five
  different anti-CRISPR proteins tested (acrF1–5, Figure 4)."]
- Mutant control, which is what makes IMP defensible: [PMID:26586803 "A plasmid bearing a
  frame-shift mutation in the beginning of the acrF1 anti-CRISPR gene that inactivates its
  anti-interference function (40) also inactivated the anti-acquisition function."]
- Conclusion: [PMID:26586803 "We conclude that anti-CRISPR proteins that inhibit CRISPR
  interference in P. aeruginosa by targeting either the Csy complex or Cas3, also inhibit
  spacer acquisition."]

Two caveats worth recording but not disqualifying: the assay is a heterologous
reconstitution in *E. coli* rather than the natural PA14 host, and the arm of the system
measured is adaptation rather than interference. GO:0098672 is the generic term for a
symbiont inhibiting or disrupting its host's CRISPR-Cas system, so it covers both arms;
its own definition is cited to PMID:23242138 and PMID:26416740, i.e. to this very
protein's discovery and mechanism papers.

## Qualifier assessment (the shape this gene was screened for)

The CACAO row carries `acts_upstream_of_or_within_positive_effect`. That relation is a
legal GAF qualifier for a biological-process term and is the conventional hedge for a
mutant-phenotype annotation where it is unknown whether the gene product is part of the
process. It is wrong here on the biology: AcrF1 binds Cas7f/Csy3 inside the host and
blocks target-DNA engagement by the Csy complex, which *is* the suppression, so the
product executes the process rather than influencing it from outside. `involved_in` is
the correct relation. This is the same defect shape already catalogued for AcrIIA5
(genes/9CAUD/acrIIA5), recorded as a `source_defects` entry rather than an action
change, since the term, reference and evidence code are all sound.

QuickGO (2026-11-01) reports GO:0098672 as non-obsolete, with no children and usage
"Unrestricted", so nothing in the ontology constrains the qualifier; the constraint is
GO's own relation guidance plus the biology.

## Open questions

- No cryo-EM or crystal structure of the Csy complex *without* bound Acrs was available
  when PMID:28340349 was solved, so whether the Cas7f web shift is caused by AcrF1 is
  stated as an inference there, not a result.
- Why AcrF1 binding to the interference complex also blocks adaptation is explained by
  the paper's own genetics (adaptation requires the Csy complex), but whether AcrF1
  additionally touches Cas1/Cas2-3 during adaptation has not been tested.
