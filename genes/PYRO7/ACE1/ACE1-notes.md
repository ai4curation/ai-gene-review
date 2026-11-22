# ACE1 (G4MVZ2, MGG_12447) — Pyricularia oryzae 70-15 — curation notes

## Sources
- UniProt G4MVZ2 (Swiss-Prot), deep research `ACE1-deep-research-falcon.md`.
- Cached full text: PMID:15319478 (Boehnert 2004), PMID:17142568 (Fudal 2007), PMID:29142718 (Song 2015).
- Abstract only: PMID:12838393 (Pi33 mapping), PMID:18433432 (cluster), PMID:31644300 (CYP1/CYP3).
- Not cached / not used for quotes: Zhang 2021 (Chem Eur J; ORFZ/ORF3 cross-complementation), Lambou 2024 (PLoS Pathog; BIP1 regulation) — summarized only via the deep-research file.

## Identity and architecture
- Hybrid iterative highly reducing PKS fused to one NRPS module, 4034-4035 aa.
  [PMID:29142718 "fused to a single module of a nonribosomal peptide synthetase (NRPS)"]
  UniProt: "ACE1 has the following architecture: KS-AT-DH-MT-KR-PCP-C-A-T-R."
- Embedded ER domain is inactive (ER0); trans-ER RAP1 supplies enoyl reduction.
  [PMID:29142718 "The biosynthesis of 6 and 7 do not require an enoyl reductase step, consistent with the observation that the ACE1 ER domain is predicted to be inactive."]

## Catalysis (heterologous expression)
- ACE1 alone in A. oryzae / M. oryzae: heptaketide pyrone (magnaporthepyrone) and diols.
  [PMID:29142718 "CC values showed intact acetate incorporations consistent with the heptaketide origin of 6."]
- ACE1 + RAP1: tyrosine-containing nonaketide amide 8 (cytochalasan-like backbone).
  [PMID:29142718 "In this case it appears that tyrosine is used as the amino acid and attached to the polyketide in the same way as observed in the cases of pretenellin A 1 and preaspyridone 3."]
  [PMID:29142718 "the likely ultimate product of the ACE1 pathway will be a member of the tyrosine-derived cytochalasans"]
- None of the isolated products (6, 7, 8) is the Pi33 avirulence signal; native product unknown.

## In planta
- KS active-site Cys183Ala abolishes avirulence on Pi33 rice although the protein is expressed and localized: enzymatic activity, not the protein, is recognized.
  [PMID:15319478 "These results demonstrate that the ace1 C183A : GFP allele is unable to confer avirulence."]
- Ace1-GFP (functional) is cytoplasmic in appressoria, not secreted.
  [PMID:15319478 "Fluorescence of the Ace1-GFP protein was detected exclusively in the cytoplasm of appressoria"]
- Expression restricted to appressoria at the onset of penetration.
  [PMID:17142568 "only expressed in appressoria during fungal penetration into rice and barley"]
- 15-gene infection-specific cluster; SYN2, RAP2 dispensable for avirulence (PMID:18433432 abstract).

## Annotation decisions (summary)
- Fatty acid synthase activity / fatty acid biosynthetic process: IEA family transfers from the shared KS/AT fold; ACE1 is a PKS-NRPS making a polyketide-amino acid hybrid, not fatty acids -> MODIFY to polyketide synthase activity (GO:0016218) / polyketide biosynthetic process (GO:0030639).
- Condensation-domain "catalytic activity" -> MODIFY to non-ribosomal peptide synthetase activity (GO:1904091). Comparator: fungal PKS-NRPS hybrids iccA (A0A482N9V7) and iliA (P0DO30) carry both GO:0016218 and GO:1904091 by IDA in QuickGO, so assigning both to ACE1 follows existing practice.
- No avirulence/host-interaction process term added: ACE1 is an intracellular biosynthetic enzyme; the recognized entity is an unidentified metabolite, and the plant-side response is performed by Pi33 rice. Effector terms (e.g. GO:0080185) would require the gene product (or a defined product) to act on the host. Raised as a suggested question.
