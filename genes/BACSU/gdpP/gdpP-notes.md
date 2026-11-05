# gdpP functional review

## 2026-11-04 — c-di-AMP degradation audit

Identity: P37484, Bacillus subtilis subsp. subtilis str. 168. The original seeded annotation payloads and both raw source files were preserved. All review actions were judged on the gene-specific biology; no new GO annotations were added.

Actual Falcon research was attempted with `just deep-research-falcon BACSU gdpP` and failed with HTTP 403 authentication. No provider report was manufactured. Manual research used the primary papers and curated source statements cited below.

- [PMID:19901023 YybT is a signaling protein that contains a cyclic dinucleotide phosphodiesterase domain and a GGDEF domain with ATPase activity.] PubMed identity verified; cached abstract explicitly reports B. subtilis YybT enzymology. Detailed kinetic and localization statements are also available in curated UniProt.

- [PMID:21566650 c-di-AMP reports DNA integrity during sporulation in Bacillus subtilis.] The cached PubMed abstract and curated UniProt connect YybT to c-di-AMP turnover during sporulation. The cache is abstract-only; the curated localization account tied to this PMID supports retaining the experimental membrane annotation.

- [PMID:21257773 Unusual heme-binding PAS domain from YybT family proteins.] PubMed identity and abstract verified. The tested proteins are BsYybT and GtYybT; this does not establish universal heme sensing by every GdpP ortholog.

The core is c-di-AMP hydrolysis, not its indirect envelope or stress phenotypes. A generic DHHA1-domain mapping does not establish a distinct nucleic-acid-binding role. Heme inhibition is characterized for Bacillus/Geobacillus proteins; ATPase activity is not generalized to S. aureus. pApA feedback was established for S. aureus GdpP and is not transferred to PgpH.

Module membership: `MODULE:bacterial_c_di_amp_signaling`, `gdpp_pde_activity`.

## 2026-11-05 — PR #5997 evidence follow-up

The hydrolysis evidence supports the catalytic assignment: [PMID:19901023 "The DHH/DHHA1 domain hydrolyzes c-di-AMP and c-di-GMP to generate the linear dinucleotides 5'-pApA and 5'-pGpG."]

Removed the hydrolysis quotation from the nucleic-acid-binding over-annotation judgment. The judgment assesses unsupported extension from DHHA1-domain membership; it is not a negative RNA-binding assay. The catalytic evidence remains on the catalytic assertion and core function.
