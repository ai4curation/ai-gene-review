# CG8915 domain-coverage re-review (2026-10-20)

CG8915/Q9VX63 aligns to the R3H domain and both helicase core domains of human YTHDC2, but not to the YTHDC2 ankyrin-repeat insertion or the YTH domain. CG8915 therefore has the R3H plus intact DEAH helicase architecture without the two YTHDC2-specific accessory modules.

This analysis reuses the existing MAFFT alignments (`outputs/local.fasta`, `outputs/global.fasta`, produced by the original `justfile`; not modified). The new script `domain_coverage_rereview.py` maps human YTHDC2 (Q9H6S0) domain ranges, taken from the Q9H6S0 UniProt feature table, onto each other sequence. It reports the fraction of reference residues aligned to a non-gap residue and the identity over those pairs. Outputs are `outputs/domain-coverage-rereview-local.json` and `outputs/domain-coverage-rereview-global.json`.

| YTHDC2 region (Q9H6S0) | CG8915 aligned fraction (L-INS-i / G-INS-i) | CG8915 identity | CG8915 span | Bgcn aligned fraction (L / G) |
|---|---|---|---|---|
| R3H 38-106 | 0.957 / 0.957 | 0.288 | 60-125 | 0.899 / 0.942 |
| Helicase ATP-binding 203-369 | 1.0 / 1.0 | 0.437 | 219-386 | 0.952 / 0.952 |
| ANK repeats 506-571 | 0.212 / 0.121 | n/a (short fragment) | 420-433 / 426-433 | 0.894 / 0.894 |
| Helicase C-terminal 612-784 | 0.971 / 0.971 | 0.429 | 450-617 | 0.977 / 0.977 |
| YTH 1288-1418 | 0.0 / 0.0 | n/a | none | 0.519 / 0.458 |

## Interpretation

- CG8915 lacks the ankyrin-repeat domain (ARD) that, in YTHDC2, sits between the two helicase lobes. The CG8915 linker between its helicase domains (UniProt DOMAIN 219..386 and 449..617) is about 60 residues, compared with about 240 in YTHDC2. CG8915 also ends at residue 976, so no YTH domain is present.
- The helicase lobes of CG8915 are about 43-44% identical to YTHDC2, compared with 26-28% for Bgcn. CG8915 also keeps the canonical motif I and motif II residues (see `RESULTS.md`).
- The Bgcn column is an alignment-coverage control only. The aligned Bgcn residues across the YTHDC2 R3H and YTH ranges do not show that Bgcn has those domains: a forced global alignment of a 1215-residue protein will place residues against them. PMID:29360036 reports that Bgcn lacks the YTH domain and that its R3H region is lost or highly divergent. Bgcn's coverage of the ANK range does agree with its UniProt ANK repeat feature (407..439).

## Consequences for annotation

The retained R3H and DEAH helicase core supports RNA binding, ATP binding, ATP hydrolysis and DEAH-type (3'-to-5') RNA helicase activity. Two YTHDC2 properties cannot be transferred to CG8915 because the domains responsible for them are absent: N6-methyladenosine recognition (YTH domain) and ARD-dependent partner recruitment. CG8915 matches the "second YTHDC2 homolog" that PMID:29360036 describes in non-Drosophila schizophoran flies (YTH-less, with intact R3H and helicase motifs I and II), apart from having no ARD. This may explain why that study, which treated the ARD as diagnostic of the family, reported no such version in Drosophila. This is a hypothesis. A proper phylogeny is still needed to settle it.

## Reproduction

```
uv run python domain_coverage_rereview.py outputs/local.fasta --reference Q9H6S0 \
  --domains R3H:38-106 HelicaseATP:203-369 ANK:506-571 HelicaseC:612-784 YTH:1288-1418 \
  --output outputs/domain-coverage-rereview-local.json
```

The same command was run on `outputs/global.fasta`, with the output written to `outputs/domain-coverage-rereview-global.json`.
