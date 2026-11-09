# actC (Q93P57), *Myxococcus xanthus* — curation notes

## Provenance of this file

No deep-research provider API keys exist in this container, so `just deep-research`
was **not** run and no `-deep-research-<provider>.md` file was created. Everything
below comes from the cached publications in `publications/`, the UniProt flat file,
Europe PMC / PubMed metadata, the UniProt and QuickGO REST APIs, and InterPro/PANTHER
records. Quotes are verbatim from the cited source.

GONUTS (`gowiki.tamu.edu`), the CACAO wiki that holds the student evidence pages, was
re-checked on 2026-11-01 as the CACAO project page asks. It is no longer merely
offline: `https://gowiki.tamu.edu/wiki/index.php/Main_Page` returns **HTTP 410 Gone**
with the page "GONUTS, the GO wiki, has been retired" ("The GO wiki that was at
gowiki.tamu.edu is no longer online."). The Wayback availability API has no snapshot
for `MYXXA:ACTC`, `MYXXA:Q93P57`, or the Gronewold/Kaiser reference page. The
student-evidence check is therefore permanently unavailable, not temporarily so, and
the CACAO rows below are judged from the papers alone under the curator-deference rule.

## What the protein is

Q93P57 is a 437-residue unreviewed (TrEMBL) entry, `PE 4: Predicted;`, with no
functional UniProt comments. Its architecture is two-part:

- residues ~1–270: an NAD(P)-binding Rossmann-like domain (Gene3D 3.40.50.720,
  SUPFAM SSF51735, InterPro IPR036291 / IPR051783 "NAD(P)-dependent oxidoreductase-like").
- residues 273–437: a GNAT (GCN5-related N-acetyltransferase) domain —
  `DOMAIN          273..437` with `/note="N-acetyltransferase"`, plus
  `PROSITE; PS51186; GNAT; 1.`, `Pfam; PF00583; Acetyltransf_1; 1.` and
  `CDD; cd04301; NAT_SF; 1.`

No catalytic activity has ever been assayed for ActC. There is no experimental
molecular-function datum in the literature; the whole experimental record is genetic.

## The act operon and what the cited paper shows for actC

The one paper behind every CACAO row is PMID:11359579 (Gronewold & Kaiser 2001,
*Mol Microbiol*). It is **abstract-only** in our cache (`full_text_available: false`)
and is not open access (Europe PMC: `isOpenAccess: N`, `inEPMC: N`, no PMCID).

The abstract is nonetheless specific about actC:

- [PMID:11359579 "The C-signal is a morphogen that controls the assembly of fruiting bodies and the differentiation of myxospores"]
- [PMID:11359579 "Production of this signal, which is encoded by the csgA gene, is regulated by the act operon of four genes that are co-transcribed from the same start site"]
- [PMID:11359579 "The act C and act D genes regulate the time pattern of CsgA production, while achieving the same maximum level"]
- [PMID:11359579 "An act C null mutant raises CsgA production 15 h earlier than the wild type, whereas an act D null mutant does so 6 h later than wild type"]

Note what the abstract attributes to which gene. The **sporulation** phenotype named in
the abstract is actA's and actB's, not actC's:
[PMID:11359579 "The act A and act B mutants have the same developmental phenotype: both aggregate, neither sporulates, both prolong rippling"].
actC's stated result is a 15 h advance in the timing of CsgA production at an
unchanged maximum level.

Two later papers from the same authors pin down what the 2001 paper showed for actC
and are the basis for judging the two developmental rows:

- PMID:11807078 (2002, abstract-only in cache): mutants in each act gene were
  examined against four reporters.
  [PMID:11807078 "These mutations changed the expression of four gene reporters that are related to aggregation and sporulation and are expressed at 6 h or later in development"]
  and
  [PMID:11807078 "The other act null mutations caused either premature expression to wild-type levels (actC) or delayed expression (actD), which ultimately rose to wild-type levels"].
  So actC shifts the **timing** of aggregation and sporulation gene expression; the
  levels ultimately reached are wild type. Early, C-signal-independent development is
  untouched:
  [PMID:11807078 "Neither the time of first expression nor the rate of expression increase was changed in actA, actB, actC, or actD mutant strains"].
- PMID:17189369 (2007, **full text available**) restates the 2001 paper's actC
  morphological phenotype explicitly, citing it as reference 17:
  [PMID:17189369 "deletion of the actC gene led to the premature formation of many small fruiting bodies"].
  This is the sentence that grounds the fruiting-body row in the cited paper.
  It also states the direction of ActC's effect:
  [PMID:17189369 "Since deletion of actC leads to precocious C-signal-dependent gene expression, actC protein appears to inhibit the rise of csgA expression"]
  and offers a mechanism hypothesis:
  [PMID:17189369 "ActC (MXAN3215) would inhibit csgA expression. ActD caspase could degrade ActC, releasing the inhibition and allowing the expression of csgA to rise at the appropriate time."]

Why the sporulation claim is still defensible, if peripheral:
[PMID:17189369 "The cell-surface-associated, nondiffusible C signal is essential for both fruiting body formation and sporulation"] and
[PMID:17189369 "Sporulation genes have a higher threshold of C-signal intensity than genes for aggregation"].
A gene that sets when C-signal rises therefore does modulate when the sporulation
threshold is crossed — but no actC sporulation-efficiency defect is reported anywhere
we can read, and the 2002 reporters reach wild-type levels.

The operon has five genes, not four: [PMID:17189369 "actE , are expressed together and constitute an operon, because an in-frame deletion of actB decreased expression of actA and actE to the same extent"].
`actE` was described after the 2001 paper, whose abstract says "four genes".

## Which entity performs the step

ActC's own action is on *csgA* expression: it restrains the rise of C-signal
production. Fruiting-body morphogenesis and sporulation are executed by the
C-signalling cascade downstream, not by ActC. The CACAO rows are nonetheless
*regulation of* terms, which is the correct GO device for a regulator that acts
through a signal, so the terms are not a "phenotype read as process" failure. What is
missing from GOA is the direct claim — negative regulation of *csgA* gene expression —
which is proposed as a NEW row.

## Molecular-function rows: domain prediction, and one wrong propagation

`GO:0016747`, `GO:0016407` and `GO:0016740` all trace to the real GNAT match
(InterPro IPR000182, UniRule UR000414522 via PROSITE-ProRule PRU00532). The domain is
specifically an **N**-acetyltransferase signature, which `GO:0008080` states and the
three annotated terms do not.

`GO:0004029 aldehyde dehydrogenase (NAD+) activity` (TreeGrafter, GO_REF:0000118,
PANTHER node PTN005180820) does not fit. NAD+-dependent aldehyde dehydrogenases
(EC 1.2.1.3) are the ALDH superfamily — Pfam PF00171 (Aldedh), SUPFAM SSF53720 — and
Q93P57 matches none of those; its NAD(P)-binding domain is the Rossmann-like
3.40.50.720 / SSF51735 fold used by short-chain dehydrogenases/reductases and
NAD-dependent epimerases/dehydratases. PANTHER itself places the protein in
`PTHR48079` whose name is "PROTEIN YEEZ" (local `interpro/panther/panther.obo`) and
whose InterPro integration IPR051783 is described as a family of ketoreductases,
epimerases and dehydratases, with no aldehyde dehydrogenase among the members listed
in `interpro/panther/PTHR48079/PTHR48079-entries.csv`.

The propagation is not specific to this gene. A QuickGO query on
`withFrom=PANTHER:PTN005180820` (2026-11-01) returns **2,648 annotations**, every one
of them either `GO:0004029` or `GO:0005737`, i.e. ~1,324 proteins receive this
aldehyde-dehydrogenase assertion from that single node. Recorded as a `source_defects`
entry against GO Central / PANTHER.

`just paint-losses MYXXA actC` reports "Q93P57 is not a leaf of this tree; losses not
checked. No IRD or IKR loss on this gene's lineage." (The row is a TreeGrafter graft,
not a PAINT IBA.)

## The predicted failure shape: cross-isolate transfer — ABSENT

The screen flagged PMID:11359579 because its CACAO rows span two NCBI taxon ids,
`NCBITaxon:34` (*Myxococcus xanthus*) and `NCBITaxon:246197` (*M. xanthus* strain
DK1622), and the Gag-shaped hypothesis was that one experiment had been annotated onto
entries of a different isolate without re-grounding. It had not. Checked concretely:

1. **Which strain the paper worked in.** DK1622, the standard laboratory strain and the
   reference genome. The 2001 paper's own GenBank submission carries
   `RC   STRAIN=DK1622` on Q93P57, and the follow-up paper states that the submitted
   sequence is the genome sequence: [PMID:17189369 "The entire sequence was verified in the complete sequence of the M. xanthus genome, GenBank accession number CP000113"]
   (CP000113 is the DK1622 genome). DK1622 is also the wild-type comparator throughout
   PMID:17189369.
2. **Which strain Q93P57 is from.** DK1622, as above. The species-level taxon id on the
   entry reflects how the authors deposited AF350253, not a different organism.
3. **Whether the paper assays actC itself.** Yes — the abstract reports the actC null
   mutant's 15 h advance in CsgA production, and PMID:17189369 attributes the actC
   fruiting-body phenotype to this same reference.

So the two taxon ids denote one organism and one locus, exactly the alternative the
screen design anticipated. **No cross-isolate transfer; the shape is absent.**

## What is there instead: redundant UniProt entries fragmenting one operon's annotations

The taxon span is real but its cause is entry redundancy, and it has a consequence
worth recording. Each act gene exists **twice** in UniProtKB — once from the 2001
paper's own AF350253 submission at taxon 34, and once from the DK1622 genome
(CP000113) at taxon 246197:

| gene | taxon 34 entry (AF350253) | taxon 246197 entry (DK1622 proteome) | CACAO rows landed on |
|---|---|---|---|
| actA | Q93P59 (342 aa, `GN actA`) | Q1D7F9 (342 aa, `GN actA MXAN_3213`) | Q93P59 |
| actB | Q93P58 (553 aa, `GN actB`) | Q1D7F8 (553 aa, `GN actB MXAN_3214`) | **Q1D7F8** |
| actC | Q93P57 (437 aa, `GN actC`) | Q1D7F7 (437 aa, **no gene name**, `MXAN_3215`) | Q93P57 |
| actD | Q93P56 | MXAN_3216 | — |
| actE | Q93P55 | MXAN_3217 | — |

Verified by fetching both sequences: Q93P57 and Q1D7F7 are byte-identical (437 aa,
same md5 of the sequence) and share the same RefSeq protein `WP_011553262.1`. They are
the same protein of the same strain under two accessions and two taxon ids.

Three consequences:

- The three CACAO rows for one paper are split across both entry sets — actA and actC
  on the taxon-34 entries, actB on the DK1622 entry. Nothing was transferred between
  organisms; the curators simply reached whichever entry carried the gene symbol
  (`actB` is a gene name only on the DK1622 entry; `actC` is a gene name only on the
  taxon-34 entry, since Q1D7F7 has no `GN Name`).
- The experimental annotations sit on the entry that is **not** in the reference
  proteome. Q1D7F7 carries `DR Proteomes; UP000002402`; Q93P57 carries none. So
  `Q1D7F7` — the ActC that appears in the DK1622 proteome, in STRING, KEGG and
  EnsemblBacteria — has only the three IEA rows (`GO:0005737`, `GO:0016747`,
  `GO:0004029`, checked 2026-11-01) and none of the experimental developmental
  annotations.
- The defect is UniProt's, not CACAO's: an obsolete-style redundant pair that should be
  merged. Recorded as a `source_defects` entry against UniProt on the
  `GO:0031155` row.

## Summary of judgements

| term | code | action | one-line reason |
|---|---|---|---|
| GO:0031155 regulation of reproductive fruiting body development | IMP | ACCEPT | ΔactC gives premature formation of many small fruiting bodies, attributed to this paper by PMID:17189369 |
| GO:0009966 regulation of signal transduction | IMP | MODIFY → GO:0009968 | sign is known: ActC restrains the rise of C-signal production |
| GO:0043937 regulation of sporulation | IMP | KEEP_AS_NON_CORE | real but downstream and timing-only; the abstract's sporulation phenotypes are actA's and actB's |
| GO:0004029 aldehyde dehydrogenase (NAD+) activity | IEA | REMOVE | wrong fold; over-propagated from PTN005180820 to ~1,300 proteins |
| GO:0005737 cytoplasm | IEA | ACCEPT | soluble protein, no TM or signal peptide; right granularity for a bacterium |
| GO:0016407 acetyltransferase activity | IEA | MODIFY → GO:0008080 | GNAT domain is an N-acetyltransferase signature |
| GO:0016747 acyltransferase activity, transferring... | IEA | MODIFY → GO:0008080 | same domain, same refinement |
| GO:0016740 transferase activity | IEA | TOO_GENERAL | near-root term entailed by GO:0008080 |
| GO:0010629 negative regulation of gene expression | IMP | NEW | ActC's own action: it inhibits the rise of csgA expression |
