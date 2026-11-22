# C11orf98 / RSMC review notes

## Symbol and ORF situation — read this first

Two things about this gene's identity matter for curation and are easy to get wrong.

**1. The symbol.** HGNC still uses **C11orf98** (HGNC:51238, previous symbol C11orf48).
UniProt has adopted the gene name **RSMC** ("28S rRNA/ribosome and sororin micro-cofactor")
from PMID:41261216, and the GOA file downloaded for this gene already shows `RSMC` in its
SYMBOL column. This repository's directory convention is the HGNC symbol, so the directory
and `gene_symbol` stay `C11orf98`, with `RSMC` recorded as an alias.

**2. The ORF.** The RSMC microprotein is an **alternative ORF**, not a splice isoform:
[PMID:41261216 "Since RSMC/C11ORF98 is an alternative ORF of the LBHD1 gene (Fig."] — the
sentence is truncated by a figure callout, but the claim is unambiguous, and the authors
confirmed that their RSMC siRNAs leave LBHD1 mRNA unchanged. HGNC records `C11orf48` as the
previous symbol of **both** C11orf98 (E9PRG8) and **LBHD1** (HGNC:28351, UniProt Q9BQE6),
which is the fingerprint of an alt-ORF locus that was later split into two gene records.

The practical consequence: **E9PRG8 is itself the alt-ORF product.** The whole 123-residue
UniProt entry is the microprotein, there are no `alternative_products` on the entry, and no
annotation below needs an `isoform:` scope. What must not happen is transfer of any of these
annotations to LBHD1/Q9BQE6, which is a different protein from a different reading frame of
the same locus. That is the ORF-blurring risk here, and it lives between UniProt entries,
not within one.

## What the 2026 paper shows

[PMID:41261216 "During normal S-phase, PARP1 PARylates a microprotein encoded by the
alternative ORF C11ORF98, which we designate RSMC (28S rRNA/ribosome and Sororin
micro-cofactor)."]

The chain of evidence:

- Direct, reconstituted interaction with Sororin/CDCA5: [PMID:41261216 "This indicates a
  direct association between RSMC and Sororin."] from recombinant GST-RSMC and
  6xHis-Flag-Sororin pulldowns.
- Loss of function causes cohesion defects: [PMID:41261216 "RSMC depletion caused cohesion
  defects albeit milder than Sororin knockdown (KD), and its direct association with Sororin
  was indispensable for cohesion."] Knockdown gave ~40% defective cells versus ~80% for
  Sororin, and combined siRNA plus heterozygous knockout reached ~67%.
- Mechanism, part 1 — Sororin recruitment: [PMID:41261216 "Together, these data suggest that
  RSMC enhances the recruitment of Sororin to cohesin on chromatin during S phase in
  cooperation with ESCO1/2-dependent SMC3 acetylation."]
- Mechanism, part 2 — stimulating Sororin's anti-Wapl activity: [PMID:41261216 "Through
  chromatin fractionation and in vitro competitive MST analysis, we showed that RSMC
  stimulates the anti-Wapl activity of Sororin."]
- Regulation: [PMID:41261216 "Intriguingly, this interaction was enhanced by S-phase PARP
  activity via RSMC PARylation, complementing SMC3 acetylation to ensure Sororin's timely
  chromatin recruitment and anti-Wapl function."]
- Localisation: [PMID:41261216 "Immunostaining revealed that RSMC was primarily distributed
  in the nucleus as Sororin (Fig."]

## The other half of the name: ribosome biogenesis

The "R" in RSMC is not from this paper. C11orf98 was independently found as a component of
human nucleoplasmic pre-60S particles: [PMID:37491604 "Two new human nuclear factors, L10K
and C11orf98, were also identified."] UniProt models it in PDB 8INF at 3.0 A in complex with
the pre-60S ribosome and describes it as a possible distal functional ortholog of yeast
Alb1. The cohesion paper acknowledges this and notes a difference from the yeast case:
[PMID:41261216 "Nevertheless, human C11ORF98 binds 28S rRNA but not PA2G4 (Arx1 in yeast)
(Zhang et al, 2023b)."]

The earlier APEX proximity-labelling study is consistent: the top partners were the two
major nucleolar chaperones, [PMID:28589727 "Two of the most robust C11orf98-associated
proteins are nucleolin (NCL) and nucleophosmin (NPM1) (Figure 3C)."], and the microprotein
localises to nucleoli, [PMID:28589727 "Furthermore, the FLAG-tagged C11orf98 microprotein
overlaps entirely with the HA-tagged NPM1 in the nucleoli, providing additional evidence
that NPM1 and the C11orf98 microprotein are likely to interact with each other."]

So this gene has **two** proposed functions from two non-overlapping lines of work: a
nucleolar/pre-60S ribosome assembly factor, and a nucleoplasmic cofactor for Sororin in
sister chromatid cohesion. Unlike SMIM26, these are not topologically incompatible — both
are nuclear, and the protein is small and disordered at both termini (UniProt: residues
1-21 and 82-123 disordered), which is typical of a factor that is recycled between
complexes. But nothing in either paper tests whether the two roles are connected, and the
composite UniProt protein name asserts both.

## Curation position taken

- `GO:0045876` positive regulation of sister chromatid cohesion (IMP) → **ACCEPT**, core.
  It is the best-supported claim in the record: direct binding, knockdown, heterozygous
  knockout, rescue, and an inter-sister-distance assay.
- `GO:0005634` nucleus and `GO:0005730` nucleolus → **ACCEPT** both. They are not in
  conflict; the nucleolar pool is where the pre-60S work puts the protein and the
  nucleoplasmic pool is where the cohesion work puts it.
- `GO:0005515` protein binding (both IPI rows) → **MARK_AS_OVER_ANNOTATED** per project
  guidance. The Sororin row (WITH UniProtKB:Q96FF9) is the most informative interaction this
  gene has and deserves a real molecular function term rather than bare protein binding.
- Proposed as reviewer additions, all single-source and flagged as such:
  `GO:0030674` protein-macromolecule adaptor activity (RSMC brings Sororin to cohesin on
  chromatin), `GO:0120187` positive regulation of protein localization to chromatin (the
  Sororin recruitment result), and `GO:0042273` ribosomal large subunit biogenesis (the
  pre-60S structural identification).

## What is not established

- Whether the ribosome-assembly role and the cohesion role are mechanistically linked, or
  whether the protein simply has two jobs.
- Whether RSMC is *required* for pre-60S maturation. PMID:37491604 identifies it as a
  component of the particle; it does not report a depletion phenotype, and UniProt's
  wording is "may be involved".
- Whether homozygous loss is viable. Only heterozygous knockouts were obtained
  (PMID:41261216), which is suggestive of essentiality but is not stated as such.
