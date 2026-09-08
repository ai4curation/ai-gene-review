# RIC7 sequence and primer identity checks

Run `just analyze` in this directory. Python 3.12+ and Biopython 1.85 are specified
in `pyproject.toml`; `uv` resolves the environment. The script reads all targets,
primers and comparisons from data files and writes `results.json` without assuming
which comparisons will succeed. Interpretation is in [RESULTS.md](RESULTS.md).

## Inputs and provenance

`data/sequences.fasta` contains public reference sequences retrieved on 2026-09-07:

- [F4JLB7](https://rest.uniprot.org/uniprotkb/F4JLB7.txt) and
  [Q1G3K8](https://rest.uniprot.org/uniprotkb/Q1G3K8.txt), parsed as UniProt/Swiss-Prot.
- [NP_194585.1](https://www.ncbi.nlm.nih.gov/protein/NP_194585.1),
  [NP_001031740.1](https://www.ncbi.nlm.nih.gov/protein/NP_001031740.1),
  [NM_118998.1](https://www.ncbi.nlm.nih.gov/nuccore/NM_118998.1),
  [NM_001036663.2](https://www.ncbi.nlm.nih.gov/nuccore/NM_001036663.2), and
  [DQ487576.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ487576.1), retrieved through
  NCBI EFetch (`db=nuccore`, versioned `id`, `rettype=gb`, `retmode=text`) and
  parsed with Biopython `SeqIO` using the GenBank format.
- `DQ487576.1_CDS` is the annotated CDS `/translation` from DQ487576.1.
- [NC_003075.7 reverse-strand interval 14116015–14117367](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=NC_003075.7&seq_start=14116015&seq_stop=14117367&strand=2&rettype=fasta&retmode=text),
  and `AT4G28560_genomic_translation`, computed using `Seq.translate(to_stop=True)`
  with the standard genetic code. The FASTA sequence is already in coding orientation.

The FASTA preserves the fetched sequences, so repeating the comparisons does not
depend on mutable database responses. `data/primers.tsv` transcribes the RIC7
primers from Wu et al. (2001), Table 4, and Hong et al. (online 2015/issue 2016),
RT-PCR methods, plus Zhu et al. (2021) qRT-PCR methods; the table includes the DOI URLs. Wu/Hong source passages were inspected in indexed full-text sections, although their local PMID caches are abstract-only. The Zhu paper was read in cached full text.

## Method and scope

Protein identity is direct full-length sequence equality. For each primer and
specified transcript, the script finds the longest exact 3′ suffix of at least
14 bases, permitting removal of a 5′ cloning tail. Reverse primers are searched
as reverse complements. It reports all occurrences of that longest suffix,
including 1-based inclusive coordinates and the number of discarded 5′ bases.
It performs no mismatch-tolerant alignment, genome-wide specificity search,
primer melting-temperature calculation, or inference of experimental construct
sequence beyond what the matches demonstrate.

The positive templates are the AT4G28556 RefSeq transcript and its matching cDNA;
the distinct AT4G28560 transcript is the biological negative comparison. The
matching function was also checked on synthetic inputs for forward/reverse
orientation, 5′ tails, repeated hits, and no-hit behavior.
