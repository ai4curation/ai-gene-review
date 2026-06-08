# NEMF (Rqc2/Tae2 ortholog) research notes

UniProt: O60524 (NEMF_HUMAN). "Nuclear Export Mediator Factor" / Ribosome quality control
complex subunit NEMF. Mammalian Rqc2/RQC2/Tae2 homolog. NEMF family.

## Core function
NEMF is a key component of the RQC complex. It binds stalled 60S ribosomal subunits by
recognizing the exposed nascent-chain-conjugated (P-site peptidyl) tRNA, recruits/stabilizes
LTN1/Listerin, and mediates CAT tailing — non-templated, mRNA- and 40S-independent C-terminal
elongation of stalled nascent chains using mainly Ala-charged tRNA delivered to the A-site.

- UniProt FUNCTION: "Within the RQC complex, NEMF specifically binds stalled 60S ribosomal
  subunits by recognizing an exposed, nascent chain-conjugated tRNA moiety and promotes the
  recruitment of LTN1 to stalled 60S subunits (PubMed:25578875)."
- UniProt FUNCTION: "NEMF mediates CAT tailing by recruiting alanine-charged tRNA to the A-
  site and directing the elongation of stalled nascent chains independently of mRNA or 40S
  subunits, leading to non-templated C-terminal alanine extensions (CAT tails)."
- [PMID:33406423 "NEMF, a mammalian RQC2 homolog, modifies translation products of nonstop mRNAs ... with a C-terminal tail mainly composed of alanine"]
- [PMID:33909987 "mammalian NEMF has an additional, Listerin-independent proteolytic role, which, as in bacteria, is mediated by tRNA-Ala binding and Ala tailing"]

## Mechanistic role in two RQC branches
- RQC-L (canonical): CAT tailing exposes lysines for LTN1-dependent ubiquitination.
- RQC-C (alternative): Ala tail forms a C-degron recognized by CRL2(KLHDC10) and RCHY1/PIRH2
  C-end-rule E3 ligases.
- [PMID:33909987 "we identify the CRL2KLHDC10 E3 ligase complex and the novel C-end rule E3, Pirh2/Rchy1, as bona fide RQC pathway components that directly bind to Ala-tailed ribosome stalling products"]

## MF annotations
- GO:0000049 tRNA binding (IBA) — supported; NEMF binds peptidyl-tRNA and recruits aminoacyl-tRNA.
- GO:1904678 alpha-aminoacyl-tRNA binding (IDA, PMID:33406423, PMID:33909987) — core; binds
  Ala-charged tRNA for CAT-tailing.
- GO:0043023 ribosomal large subunit binding (IDA/IBA) — core; binds 60S.

## BP annotations
- GO:0140708 CAT tailing (IDA PMID:33406423, PMID:33909987) — CORE, NEMF-defining activity.
- GO:0072344 rescue of stalled cytosolic ribosome — core RQC.
- GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process — core.
- GO:0065003 protein-containing complex assembly (IMP PMID:25578875) — NEMF promotes RQC
  assembly (recruits LTN1); KEEP_AS_NON_CORE (this is the complex-assembly aspect of its role).

## Nuclear export (legacy)
- GO:0051168 nuclear export (IMP PMID:16103875) — older name "nuclear export mediator factor";
  UniProt notes "NEMF may also indirectly play a role in nuclear export (PubMed:16103875)".
  This predates the RQC characterization. PMID:16103875 not cached. Keep as NON_CORE; the
  predominant, well-supported function is cytoplasmic RQC. Treat as minor/contested role.
- Nucleus localization (GO:0005634 IEA, GO_REF:0000044) reflects the legacy "nuclear export"
  role; UniProt lists Nucleus by ECO:0000305|PubMed:16103875. KEEP_AS_NON_CORE — predominant
  localization is cytosol/cytosolic ribosome.

## Complex / localization
- RQC complex (LTN1 + TCF25 + NEMF) on 60S. Cytoplasm, cytosol (PubMed:25578875).
- Disease: biallelic NEMF variants cause IDDSAPN (intellectual disability + axonal neuropathy);
  Listerin/NEMF loss → neurodegeneration in mice. (background)

## Actions summary
- Core MFs: GO:1904678 alpha-aminoacyl-tRNA binding; GO:0000049 tRNA binding; GO:0043023 60S binding.
- Core BPs: GO:0140708 CAT tailing; GO:0072344 rescue; GO:1990116 RQC catabolism.
- nucleus / nuclear export -> KEEP_AS_NON_CORE.
- cytosol IEA/TAS, cytosolic ribosome IDA, RQC complex -> ACCEPT.
- protein-containing complex assembly -> KEEP_AS_NON_CORE.
