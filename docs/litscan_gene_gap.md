# Find papers that close gaps in gene function

Every Saturday at 14:00 UTC, LitScan searches Europe PMC for recent primary
papers, measures how much experimental GO evidence exists for each matched gene,
and proposes issues to create or update a gene review. It follows the
[DisMech literature scan](https://github.com/monarch-initiative/dismech/blob/main/.github/workflows/literature-scan.yml)
pattern of deterministic retrieval followed by curator-oriented triage.

## Run a dry scan

```sh
export GITHUB_REPOSITORY=ai4curation/ai-gene-review
bash .github/scripts/litscan-issue-ledger.sh > /tmp/aigr-issue-ledger.json
just litscan-gene-gap --days 30 --ledger /tmp/aigr-issue-ledger.json
just litscan-validate-gene-gap conf/litscan/gene_gap.yaml reports/litscan/gene-gap/*-gene-gap.json
```

A local run writes a JSON packet, a ranked Markdown table and eligible issue
bodies to `reports/litscan/gene-gap/`. A single candidate can be validated as
`GapCandidate` using the [LinkML schema](../src/ai_gene_review/schema/litscan_gene_gap.yaml).
Omit the ledger to explore results without GitHub access. Specify
`--date-from YYYY-MM-DD --date-to YYYY-MM-DD` for a fixed inclusive window.
Manual workflow dispatch defaults to a dry run and uploads the packet artifact.

To try new weights without querying the APIs again, rescore an existing packet
into another directory (the command refuses to overwrite the input packet and its
issue bodies). Each candidate keeps its earlier rank as `previous_rank`. Only the
packet's own candidates are re-ranked, so confirm a change with a fresh scan.
Packets written before the homology and full-text fields were added cannot be
rescored:

```sh
just litscan-rescore-gene-gap reports/litscan/gene-gap/2026-11-26-gene-gap.json --output-dir /tmp/rescore
```

## Read the score

The [configuration](../conf/litscan/gene_gap.yaml) lists the search terms,
recognized model organisms and strains, limits, scoring bands, and weights.
Four capped searches cover unknown function, named uncharacterized proteins,
refutation and biochemical characterization. They use first publication date, exclude reviews and errata,
and can include Europe PMC preprints with `--include-preprints`.

Each ranked row represents one paper and one UniProt accession. The score adds
the matching rules and the issue body shows each contribution.

| Signal | Measurement |
| --- | --- |
| Known function | QuickGO rows by source evidence code. Informative experimental rows plus ISS/ISO/ISA/ISM rows transferred from a homolog, both without bare protein binding. Zero scores +5, compared with −4 above 40. |
| Saturation | More than 40 GO rows of any evidence loses a point, more than 100 loses three. Informative experimental rows already in two GO aspects lose three points, in all three four. |
| Electronic or phylogenetic support only | A nonempty record consisting entirely of IEA and IBA earns +1. A missing informative experimental molecular function earns +2. |
| Unknown protein or family | UniProt protein names, Pfam DUF/UPF domains, and the number of UniProtKB entries with experimental GO cross-references in an assigned PANTHER family. A family with indexed members and zero experimental members earns +3. |
| Subject of the paper | A title mention earns +1, and three or more abstract sentences naming the gene earn +2, so a co-subject reported under a partner's title still counts. |
| New primary evidence | Characterization, functional-experiment, direct molecular assay (binding with partners or residues, enzyme, reporter or reconstitution assays) and rescue or epistasis language must share a sentence with the candidate symbol. A pseudoenzyme class word counts only in the title, because abstracts use it as background. |
| Weak evidence | A sentence naming the gene with a disease or knockout phenotype, in a paper with no direct assay or rescue on the gene, loses three points. Bare "abolished" or "reversed" count as phenotype, not rescue. Framing by an indirect effect or as a therapeutic target loses two. High-throughput, review-like and clinical language subtract points. A paper whose full text Europe PMC does not hold loses a point, and its issue says so. |
| Review impact | An existing review missing the reference earns +2. A reference already used by GOA on this product loses 6 points. |

The weights were recalibrated after curators reviewed the first six filed
issues: only the two papers with a direct assay or a gene without homolog
coverage closed a gap. The packet lists every rule that fired for each row.

These counts describe what the databases currently contain. An absent family
assignment supplies no family score. UniProtKB family coverage and QuickGO
annotation counts have different denominators. A statement about a catalytic
mutant can resemble evidence for a naturally inactive enzyme, so a curator or
the triage step must check the experimental subject.

## From paper to issue

1. Collect identifiers from the titles and bodies of all issues, open and
   closed. Suppress papers already mentioned there and candidates whose gene
   review already cites their PMID, DOI or Europe PMC preprint ID. Filing
   one gene from a multi-gene paper suppresses that paper on later runs. The
   hidden marker records which accession the issue assigned to the curator.
2. Match gene symbols from the title or repeated abstract mentions to UniProt
   entries in the configured species. Drop explicit non-gene acronym expansions. Prefer reviewed entries and allow an
   unreviewed title match if it resolves uniquely. Gene aliases, model species,
   expression hosts and cross-species studies can produce false matches.
3. Rank by score, then by known-function rows, reference and
   accession. By default at most ten candidates qualify for triage, with one
   per paper and a minimum score of six. A dispatch can lower the cap.
4. A read-only triage agent checks the gene, species, experiment and, for an
   update, what the paper would change in the review. It returns eligible rank
   numbers. The publisher validates the selection, refreshes the issue ledger,
   checks the title and body for unwanted notifications, and files the generated bodies. A new-review issue gives the exact UniProt
   accession to fetch. An update issue points to the existing review.

The [workflow](../.github/workflows/litscan-gene-gap.yml) serializes runs.
Network lookups use per-host pacing and bounded retries on transient failures.
Dry runs need only read access. Scheduled publication uses the repository's
ai4c-agent App after triage, with issue-write permission.

The scan samples a configured number of records per query. Papers without a
recognized organism or gene symbol, claims made only in the full text and
papers outside the retrieval vocabulary can be missed.
