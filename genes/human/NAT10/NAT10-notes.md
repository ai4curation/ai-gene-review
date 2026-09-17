# NAT10 review notes

## Why this gene was selected

NAT10 is an epitranscriptomic "writer" whose *enzyme identity* is not in question but whose
*substrate class* is. GOA carries three cytidine-N4-acetyltransferase MF terms for the same
protein — one for 18S rRNA, one for tRNA, one for mRNA — and only the third is contested.
The task is to keep the rRNA/tRNA core intact, record the mRNA methodological dispute rather
than adjudicate it by fiat, and decide what is core.

## What is not in doubt: NAT10 is the eukaryotic ac4C writer for 18S rRNA and tRNA

NAT10 is the human ortholog of bacterial TmcA / yeast Kre33(Rra1p), an ATP-dependent RNA
cytidine acetyltransferase with an N-terminal helicase/ATPase module and a GNAT
N-acetyltransferase domain (UniProt Q9H0A0: DOMAIN 558..753 "N-acetyltransferase";
BINDING 287..296 and 470 = ATP; BINDING 629..631, 636..642, 725 = acetyl-CoA).

18S rRNA, direct biochemistry:
[PMID:25411247 "Here we report that NAT10 is an ATP-dependent RNA acetyltransferase responsible
for formation of N(4)-acetylcytidine (ac(4)C) at position 1842 in the terminal helix of
mammalian 18 S rRNA."] and, for the ATP requirement,
[PMID:25411247 "RNAi-mediated knockdown of NAT10 resulted in growth retardation of human cells,
and this was accompanied by high-level accumulation of the 30 S precursor of 18 S rRNA,
suggesting that ac(4)C1842 formation catalyzed by NAT10 is involved in rRNA processing and
ribosome biogenesis."]

Two rRNA sites plus the tRNA activity and its adaptor:
[PMID:25653167 "We demonstrate that yeast Kre33 and human NAT10 are RNA cytosine
acetyltransferases with, surprisingly, specificity toward both 18S rRNA and tRNAs. tRNA
acetylation requires the intervention of a specific and conserved adaptor: yeast Tan1/human
THUMPD1."] and
[PMID:25653167 "In budding and fission yeasts, and in human cells, we found two acetylated
cytosines on 18S rRNA, one in helix 34 important for translation accuracy and another in helix
45 near the decoding site."]

Structural context — NAT10 is a bona fide constituent of the nucleolar SSU processome
[PMID:34516797 "The human small subunit processome mediates early maturation of the small
ribosomal subunit by coupling RNA folding to subsequent RNA cleavage and processing steps."]

## The contested part: does human mRNA carry meaningful ac4C?

### Side A — yes (Oberdoerffer lab)
Antibody-based acRIP-seq, 2018:
[PMID:30449621 "Here, we describe N4-acetylcytidine (ac4C) as an mRNA modification that is
catalyzed by the acetyltransferase NAT10. Transcriptome-wide mapping of ac4C revealed discretely
acetylated regions that were enriched within coding sequences. Ablation of NAT10 reduced ac4C
detection at the mapped mRNA sites and was globally associated with target mRNA downregulation."]

Base-resolution RedaC:T-seq, 2022, with a position-dependent (bidirectional!) translational effect:
[PMID:35679869 "Although cytidine acetylation (ac4C) within protein-coding sequences stimulates
translation, ac4C within 5' UTRs impacts protein synthesis at the level of initiation."] and
[PMID:35679869 "Acetylation further directly impedes initiation at optimal AUG contexts: ac4C
within AUG-flanking Kozak sequences reduced initiation in base-resolved transcriptome-wide HeLa
results and in vitro utilizing substrates with site-specific ac4C incorporation."]

Note this second result cuts against the simple "positive regulation of translation" framing of
the 2018 paper: within one lab's own data ac4C is stimulatory in CDS and inhibitory at the
start codon.

### Side B — no (Schwartz lab)
Base-resolution ac4C-seq applied across evolution finds abundant ac4C in archaeal mRNA and
essentially none in human mRNA:
[PMID:32555463 "In human and yeast mRNAs, ac4C sites are not detected but can be induced-at a
conserved sequence motif-via the ectopic overexpression of eukaryotic acetyltransferase
complexes."] and
[PMID:32555463 "By contrast, cross-evolutionary profiling revealed unprecedented levels of ac4C
across hundreds of residues in rRNA, tRNA, non-coding RNA and mRNA from hyperthermophilic
archaea."]
The method itself is published as a protocol [PMID:33772246 "Here, we present N4-acetylcytidine
(ac4C) sequencing (ac4C-seq), a protocol for the quantitative single-nucleotide resolution
mapping of cytidine acetylation in RNA."], which also frames human mRNA ac4C as an open
question rather than an established fact [PMID:33772246 "exploring whether ac4C occurs within
mRNA at low stoichiometries in settings marked by Nat10 overexpression such as cancer"].

### The exchange is on the record, back to back in Mol Cell 2024
Schwartz side [PMID:38640895 "We find that mismatch signatures are not reproducible, as C>T
mismatches are nearly exclusively present in only one of two biological replicates. Furthermore,
all mismatch types-not only C>T-are highly enriched in WT samples, inconsistent with an
acetylation signature."]

Oberdoerffer side [PMID:38640896 "Through RedaC:T-seq reanalysis, we establish a low basal error
rate at unmodified nucleotides that is not skewed to any specific mismatch type and a prominent
increase in C:T substitutions as the dominant mismatch type in both treated wild-type
replicates, with a high degree of reproducibility across replicates."] and, on the other
dataset, [PMID:38640896 "we uncover significant data quality issues including insufficient
depth, with one wild-type replicate yielding 2.7 million reads, inconsistencies in reduction
efficiencies between replicates"].

Neither side retracted. As of 2026 the question is open.

### The disease literature does not engage the dispute
A large and growing 2025-2026 disease literature simply assumes NAT10-mediated mRNA ac4C on named
transcripts. Examples reviewed here:
- gastric cancer / DUSP1 [PMID:41956987 "NAT10 binds to DUSP1 mRNA and catalyzes its ac4C
  modification at positions C327, C330, and C331 within the coding sequence (CDS) region, thereby
  enhancing the stability of DUSP1 mRNA and increasing the abundance of DUSP1 protein."]
- aged liver regeneration / Parp10 [PMID:42315153 "Mechanistically, Nat10 installed ac4C on
  Parp10 mRNA to enhance its stability and translational efficiency."]
- renal fibrosis, combining both proposed activities [PMID:42592486 "Mechanistically, nuclear
  NAT10 coordinated with cytoplasmic NAT10 to promote exosome secretion of TEC to induce
  fibroblast activationcombining mRNA ac4C modification and lysine acetylation (Kac)."]

These papers use antibody-based ac4C-RIP and NAT10 knockdown, i.e. exactly the assay class whose
specificity is at issue, and none of them cite or address PMID:38640895. They are therefore
weight-of-numbers, not weight-of-evidence, for the mRNA substrate claim. They do corroborate that
*loss of NAT10 changes the abundance and translation of specific mRNAs* — which is expected on
either model, because NAT10 loss cripples 40S biogenesis.

### Position taken
`GO:0106162 mRNA cytidine N-acetyltransferase activity` is retained (two independent IDAs, and
CLAUDE.md forbids removing an experimental annotation whose full text I have not read) but marked
non-core on every one of its four annotation rows. GOA already carries both the activity and,
implicitly through the rRNA/tRNA terms, the uncontested core. The dispute belongs in `reason`
and the open question in `suggested_questions`.

## Two propagation issues found in the IBA set

1. `GO:0002101 tRNA wobble cytosine modification` (IBA) — WITH/FROM is
   `PANTHER:PTN000100786|UniProtKB:P76562`. P76562 is TMCA_ECOLI, "tRNA(Met) cytidine
   acetyltransferase TmcA" (verified at UniProt). In bacteria the acetylated base *is* the wobble
   base [PMID:25411247 "In bacteria, ac 4 C is present at the wobble position of elongator tRNA
   Met ."], but in eukaryotes the NAT10/THUMPD1 target is C12 in the D-arm of tRNA-Ser and
   tRNA-Leu [PMID:25653167 "Specific eukaryotic tRNAs, including leucine and serine in yeast, are
   acetylated at position 12 (46)."]. The position is different and the term is wrong for human.
   -> MODIFY to `GO:0051391 tRNA acetylation`.

2. `GO:0106162` (IBA) — WITH/FROM is
   `AGI_LocusCode:AT1G10490|PANTHER:PTN000100786|UniProtKB:Q5JHC6|UniProtKB:Q9H0A0`. Q5JHC6 is
   TMCA_THEKO, the *Thermococcus kodakarensis* enzyme (verified at UniProt) — i.e. the archaeal
   case where transcriptome-wide mRNA ac4C is not contested at all. The same paper that
   established archaeal mRNA ac4C failed to detect it in human mRNA. Q9H0A0 appearing in its own
   WITH/FROM is correct and expected (its IDAs are among the descendant evidences behind the
   IBD), *not* circular. No propagation failure asserted; the annotation is simply demoted to
   non-core along with the human IDAs.

## Does NAT10 have a defensible protein-acetyltransferase molecular function?

Claims exist: histones/hTERT (PubMed:14592445), SUN1/mitotic chromosome decondensation
(PubMed:17631499), alpha-tubulin [PMID:19303003 "DNA damage induced increase of NAT10 in the
midbody apparently accompanied by in situ elevation of the level of acetylated alpha-tubulin"],
CCDC84/CENATAC K31 [PMID:31722219 "the acetylation state of CCDC84 at lysine 31 is regulated by
the deacetylase SIRT1 and the acetyltransferase NAT10"], and now histone H3 via a GSDMC scaffold
[PMID:42176271 "In the nucleus, GSDMC functions as a scaffold molecule, recruiting NAT10 to
mediate histone H3 acetylation and recruiting BAZ1B/SMARCA5 to modulate chromatin remodeling and
chromatin accessibility."]

Assessment: **not defensible as a molecular function for this protein, on present evidence.**
UniProt reaches the same conclusion and says why — the in vitro KAT assays were run on truncated
protein:

> "A number of papers have reported some protein lysine acetyltransferase activity in vitro
> (PubMed:14592445, PubMed:17631499, PubMed:19303003, PubMed:26882543, PubMed:27993683,
> PubMed:30165671). However, most experiments have been performed in vitro using a protein
> construct lacking the RNA-binding region at the terminus ... Recent evidence suggests that
> NAT10 mainly acts as a RNA cytidine acetyltransferase in vivo (PubMed:30449621)."

and

> "In addition to RNA acetyltransferase activity, also able to acetylate lysine residues of
> proteins, such as histones, microtubules, p53/TP53 and MDM2, in vitro ... The relevance of the
> protein lysine acetyltransferase activity is however unsure in vivo (PubMed:30449621)."

The primary paper makes the same point directly:
[PMID:25411247 "A truncated recombinant NAT10 (amino acids 164-834) lacking the N-terminal RNA
helicase domain has in vitro lysine acetyltransferase activity toward histones in the presence of
acetyl-CoA; this activity does not require ATP ( 17 ). In this study, we clearly showed that a
full-length Nat10 has RNA acetyltransferase ability that can catalyze formation of ac 4 C1842 in
18 S rRNA in the presence of both acetyl-CoA and ATP; thus, ac 4 C1842 formation requires both
catalytic domains of NAT10."]

Note the construct that is catalytically competent for lysines (164-834) is exactly the one that
has lost the ATPase/RNA-binding module required for the RNA reaction; the reverse control — does
*full-length* NAT10 acetylate a protein substrate? — is the one that has not been done cleanly.
The GSDMC/H3 result (PMID:42176271) is a co-IP-plus-knockdown chromatin study, not an enzymology
experiment, and NAT10 knockdown collapses ribosome biogenesis, so a downstream/indirect route to
altered H3 acetylation is not excluded. GOA's exposure here is only the BP term
`GO:0006473 protein acetylation` (IDA, PMID:31722219) — there is no protein-lysine-KAT *MF* term
on the record, which is the right state of affairs. That BP annotation is kept but non-core.

## Other annotation calls worth recording

- `GO:0005697 telomerase holoenzyme complex` (IDA, PMID:18082603). The paper itself distinguishes
  holoenzyme components from associated NTPases: [PMID:18082603 "All three core H/ACA-motif
  binding proteins are telomerase holoenzyme components essential for RNP accumulation."] while
  NAT10 falls under [PMID:18082603 "two NTPase proteins associate preferentially with active
  enzyme"]. Marked over-annotated, not removed.
- `GO:0032211 negative regulation of telomere maintenance via telomerase` (IMP, PMID:18082603)
  rests on an *overexpression* phenotype: [PMID:18082603 "overexpression of either associated
  hnRNP protein (hnRNP C and hnRNP U) or either NTPase protein (NAT10 and GNL3L) induced telomere
  shortening."] Kept, non-core, caveat recorded.
- `GO:0016020 membrane` (HDA, PMID:19946888, NK-cell membrane proteome) for a nucleolar protein is
  a high-throughput carry-over; marked over-annotated.
- `GO:0045727 positive regulation of translation` (IDA, PMID:30449621) is directionally too
  confident given PMID:35679869's own finding that 5'UTR/Kozak ac4C *inhibits* initiation.
  Modified to `GO:0006417 regulation of translation`.
- All seven bare `GO:0005515 protein binding` rows marked over-annotated per project guidance.

## PMID verification

Every PMID cited above was resolved against PubMed (title/journal/year) via the PubMed MCP, and
each supporting_text used in the YAML is a verbatim substring of the corresponding cached
`publications/PMID_*.md`. P76562 and Q5JHC6 were resolved against the UniProt REST API.
