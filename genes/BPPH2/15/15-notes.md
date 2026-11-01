# Bacillus phage phi29 gene 15 (gp15 / p15, endolysin) — curation notes

UniProt: P11187 (ENLYS_BPPH2), 258 aa, EC 3.2.1.17. Host: *Bacillus subtilis*
(NCBI:txid1423). Reviewed for the CACAO project (batch 3, screen 1).

**Deep research was unavailable for this review.** No deep-research API keys
exist in this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file exists. Everything below was gathered by
reading the cached publications, by PubMed E-utilities / web search, and by
live queries to UniProt, InterPro and QuickGO. Both papers cited by the two
CACAO rows are **abstract-only** in the cache (`full_text_available: false`),
and neither is in the PMC open-access subset (EuropePMC `fullTextXML` and the
NCBI BioC endpoint both return nothing for PMC304338 and PMC193017), so no
figure-level reading was possible.

**GONUTS is gone, not offline.** Batches 1 and 2 recorded `gowiki.tamu.edu` as
"temporarily offline while we perform upgrades". Queried again on 2026-11-01 it
now returns **HTTP 410 Gone** with the page "GONUTS, the GO wiki, has been
retired" — "The GO wiki that was at gowiki.tamu.edu is no longer online" —
and a per-protein page (`/wiki/index.php/UniProtKB:P11187`) also returns 410.
The Internet Archive has no snapshot of the phi29 pages. The project's standing
fallback for abstract-only CACAO rows is therefore permanently unavailable, not
pending; this should be recorded in `projects/CACAO.md`.

## What the protein is

Gene 15 is the second gene of the phi29 lysis cassette; gene 14, immediately
upstream, is the holin. The pair was sequenced together
[PMID:3027653 "Nucleotide sequence of Bacillus phage phi 29 genes 14 and 15:
homology of gene 15 with other phage lysozymes."], and gp15 is a phage-type
lysozyme: [PMID:3027653 "Gene product 15 (gp15) has considerable homology with
Salmonella phage P22 lysozyme and lesser homology with Escherichia coli phage
T4 lysozyme."].

The activity was established by cloning and purification, not by mutant
analysis: [PMID:3469652 "The overproduced protein has been purified to near
homogeneity and confirmed to be the product of gene 15 by amino acid sequence
analysis of its N terminus."] and [PMID:3469652 "The purified product of gene
15 has a lysozyme activity similar to other phage-type lysozymes: products of
phage T4 gene e and of phage P22 gene 19."]. The same paper notes
[PMID:3469652 "However, to our knowledge phi 29 lysozyme is structurally unique
among the phage-type lysozymes."] — the unusual feature being the two
C-terminal LysM repeats appended to the GH24 catalytic domain
(`file:BPPH2/15/15-uniprot.txt` "LysM domains are thought to be involved in
peptidoglycan binding.", two PF01476/PS51782 matches in the record).

UniProt curates the mechanism as the canonical holin/endolysin sequence:
[`file:BPPH2/15/15-uniprot.txt` "Endolysin with lysozyme activity that degrades
host peptidoglycans and participates with the holin and spanin proteins in the
sequential events which lead to the programmed host cell lysis releasing the
mature viral particles."] and [`file:BPPH2/15/15-uniprot.txt` "The endolysin is
cytoplasmic, but can reach the periplasmic space with the help of the holins
which disrupt the host cell membrane."]. Family placement:
[`file:BPPH2/15/15-uniprot.txt` "Belongs to the glycosyl hydrolase 24 family."],
[`file:BPPH2/15/15-uniprot.txt` "Pfam; PF00959; Phage_lysozyme; 1."].

The holin partner is independently established: [PMID:8432697 "Phage phi 29
gene 14, the product of which is required for efficient lysis of Bacillus
subtilis, was cloned in Escherichia coli."] and [PMID:8432697 "Production of
protein 14 in E. coli resulted in cell death, whereas production of protein 14
concomitantly with the phi 29 lysozyme or unrelated murein-degrading enzymes
led to lysis, suggesting that membrane-bound protein 14 induces a nonspecific
lesion in the cytoplasmic membrane."]. The division of labour is stated flatly
in [PMID:7831803 "The 131-codon gene 14 of Bacillus subtilis phage phi 29
encodes the holin function, whereas the downstream gene 15 codes for a
lysozyme."].

One caution worth noting but not acting on: the entry records
[`file:BPPH2/15/15-uniprot.txt` "Lacks the conserved Asp active site."]. This
is a HAMAP sequence observation; it does not survive as a doubt about activity,
because the purified protein was assayed and is a lysozyme (PMID:3469652).
Only Glu15 is annotated as proton donor/acceptor.

## Screen 1 (adjacent-locus confusion): CONFIRMED on the GO:0044659 CACAO row

The CACAO row `GO:0044659 viral release from host cell by cytolysis`, IMP,
`acts_upstream_of_or_within_positive_effect`, PMID:820555 (2025-02-17) is the
screen's target. PMID:820555 is Carrascosa et al. 1976, a classical
characterization of phi29 gene products by sus mutants. Its abstract offers one
sentence about lysis: [PMID:820555 "A cistron, probably involved in the final
lysis of the infected bacteria, has been found."] and [PMID:820555 "Mutants in
this gene give place, under restrictive conditions, to delayed lysis and
produce, after artificial lysis, a burst size similar or higher than that
obtained after wild-type phage infection."]. The cistron is not named in the
abstract.

Five independent lines say that cistron is **gene 14**, not gene 15:

1. The sus mutant that exists in this region of the phi29 collection is a
   gene-14 mutant: [PMID:3027653 "The g14 open reading frame (ORF) was
   confirmed by sequencing a sus14(1241) mutant."] There is no sus15.
2. Gene 14's product is the one whose loss impairs lysis: [PMID:8432697 "Phage
   phi 29 gene 14, the product of which is required for efficient lysis of
   Bacillus subtilis, was cloned in Escherichia coli."]
3. [PMID:7831803 "The 131-codon gene 14 of Bacillus subtilis phage phi 29
   encodes the holin function, whereas the downstream gene 15 codes for a
   lysozyme."] A holin mutant gives exactly the delayed-lysis-with-normal-burst
   phenotype the 1976 abstract describes, because the endolysin accumulates in
   the cytoplasm but cannot reach the murein.
4. gp15 was not characterized by mutant phenotype at all; it was cloned,
   overproduced and assayed eleven years later (PMID:3469652). A 1976
   mutant-phenotype paper cannot be the source of an IMP on gene 15.
5. The decisive internal evidence: the same CACAO curator made **two** rows from
   that one sentence. `projects/CACAO/data/cacao-quickgo-2026-10-28.tsv` shows
   `GO:0044659` IMP PMID:820555 on P03682 (gene 4, the late-genes transcription
   activator p4, 2025-02-20) as well as on P11187 (gene 15, 2025-02-17). One
   cistron in the paper, two genes annotated, and the actual lysis cistron
   (gene 14, UniProtKB:P11188, `HOLIN_BPPH2`) carries no row at all. At least
   one of the two is misattributed, and neither is gene 14.

A cross-check requested by the batch coordinator, who is also reviewing gene 17
and gene 4: the choice is not between gene 15 and gene 4. Both are wrong, because
the cistron is gene 14. The later phi29 literature attributes the 1976 abstract's
exact phenotype — delayed lysis under restrictive conditions with a normal or
larger burst after artificial lysis — to the named alleles sus14(1241) and
sus14(1242), and Steiner et al. report that phi29-induced lysis in *B. subtilis*
is only delayed when protein 14 is absent. So the gene-4 row and the gene-15 row
are both misattributions of one sentence, and the gene that earned it has no
CACAO row. Confidence is recorded as PROBABLE rather than CONFIRMED only because
the 1976 full text itself could not be read (Eur J Biochem 1976 is not in PMC).

On the qualifier: all ten of phi29's 2025-dated CACAO rows use
`acts_upstream_of_or_within_positive_effect`, so the hedge is a campaign habit
and has to be judged per gene rather than condemned wholesale — on gene 17 it
reportedly fits the evidence better than `involved_in`. It does not fit here:
gp15's lysozyme activity was measured directly on purified protein, and that
activity *is* the cytolytic step of GO:0044659, so `involved_in` is right.

So the shape predicted by screen 1 is **present**. It behaves as it did on T4
gp5.4: the *term* is independently true of gene 15 — gp15 is the endolysin that
performs the peptidoglycan hydrolysis releasing virions, and the UniRule IEA row
in the same GOA file carries GO:0044659 on sound grounds — while the *stated
evidence* belongs to the neighbouring gene. Under the curator-deference rule the
row is kept (ACCEPT, with the defect filed), not removed: the full text was not
readable, and removing it would drop a true claim.

The same row is a second, independent hit on **screen 3**: the qualifier
`acts_upstream_of_or_within_positive_effect` is wrong for gene 15, which
executes the murein-hydrolysis step of lysis rather than acting upstream of it.
(The qualifier fits the *evidence* — a mutant delaying a downstream outcome —
which is itself a sign that the row was written from a gene-14 phenotype.)

The other CACAO row, `GO:0003796 lysozyme activity` IMP PMID:3469652
(2012-11-16), is about the right gene and the right paper; only the evidence
code is wrong. PMID:3469652 assays a purified protein, with no mutant anywhere
in it, so the code should be IDA. Same shape as the SWP7 and T5 D15 rows in
batch 2.

## Endolysin own-process shape: PRESENT, in three places and from two routes

This replicates the PRD1 P15 (`genes/BPPRD/XV`) and phage K LysK
(`genes/BPPGK/lysK`) findings, and extends them.

- `GO:0009253 peptidoglycan catabolic process`, IEA, GO_REF:0000120, from
  `UniRule:UR000433564` + `InterPro:IPR002196`/`IPR034690`. Ancestry checked in
  QuickGO: GO:0009253 sits wholly under `GO:0009987 cellular process` via
  peptidoglycan/aminoglycan/macromolecule catabolism, with no interspecies
  parent. phi29 has no peptidoglycan of its own.
- `GO:0016998 cell wall macromolecule catabolic process`, IEA, GO_REF:0000002,
  from `InterPro:IPR002196`. Ancestry checked in QuickGO: `GO:0044036` →
  `GO:0071554 cell wall organization or biogenesis` → `GO:0009987 cellular
  process`. Same defect, different term — this one was not seen on XV or lysK.
- `GO:0042742 defense response to bacterium`, IEA, GO_REF:0000043, from
  `UniProtKB-KW:KW-0081`. Third instance of the inverted-direction keyword
  mapping after XV and lysK.

Both own-process terms take `GO:0052009 symbiont-mediated disruption of host
cell wall` (QuickGO: under `GO:0098933 symbiont-mediated disruption of host cell
envelope` → `GO:0044419`), the same replacement the two comparator reviews used.

Two things are new relative to the comparators:

- **The rule route, not just InterPro2GO.** `UniRule:UR000433564` is HAMAP
  `MF_04110`, whose name is **ENDOLYSIN_T4** (queried live at
  `rest.uniprot.org/unirule`): a rule whose entire scope is phage endolysins.
  Its GO set is `GO:0003796`, `GO:0044659` **and** `GO:0009253`. Every protein
  the rule fires on is a phage endolysin acting on another organism's wall, so
  the own-process term is wrong for 100% of its targets — a stronger case than
  lysK's, where IPR002502 Amidase_2 is genuinely shared with bacterial
  autolysins whose substrate is their own sacculus.
- **IPR002196 is a phage-lysozyme family.** InterPro's live record for
  IPR002196 ("Glycoside hydrolase, family 24", a family entry) maps it to
  `GO:0003796`, `GO:0009253` **and** `GO:0016998`; 1,570 of its 8,193 UniProt
  members are viral (InterPro API, taxonomy 10239). The two process terms
  mis-direct all 1,570.

- **A keyword-name correction for the earlier reviews.** The XV and lysK reviews
  both describe `KW-0081` as "Antimicrobial". The live UniProt keyword record
  gives `KW-0081` = **Bacteriolytic enzyme** ("Enzyme, e.g. lysozyme or
  endopeptidase, essential for lysis of bacterial cell walls"), a *child* of
  `KW-0929` Antimicrobial. Its GO mapping is `GO:0003824`, `GO:0008152`,
  `GO:0031640` and `GO:0042742`. This sharpens the upstream report rather than
  weakening it: the offending keyword is not the broad antimicrobial one that
  also covers host defence peptides, but the narrow one that means
  "bacteriolytic enzyme", for which `defense response to bacterium` is never
  right, and whose mapping to `GO:0003824 catalytic activity` and
  `GO:0008152 metabolic process` is uninformative root-level noise.

## CACAO row summary

| term | ev | ref | action | why |
|---|---|---|---|---|
| GO:0003796 lysozyme activity | IMP | PMID:3469652 | ACCEPT | right gene, right paper; purified-protein assay, so the code should be IDA (filed as a defect) |
| GO:0044659 viral release by cytolysis | IMP | PMID:820555 | ACCEPT | term true of gp15, but the 1976 mutant is sus14(1241) and the paper's lysis cistron is gene 14 (P11188); qualifier also wrong |

## Open questions

- GO has no "host periplasmic space" cellular-component term (QuickGO search),
  so the compartment where this enzyme actually works cannot be expressed; the
  only CC available is `GO:0030430 host cell cytoplasm`, which is where the
  enzyme sits before the holin acts.
- What the two LysM repeats contribute is unknown. No binding or deletion
  experiment on phi29 gp15 has been published; the UniProt DOMAIN line is
  inference from the domain's general properties.
