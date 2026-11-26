# RASGEF1A (horse, Equus caballus) — A0A9L0R5H6

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New review (no prior review existed for this horse accession). ProtNLM2 predictions were not
consulted.

### Identity and gene model

- A0A9L0R5H6 (TrEMBL, PE 4, 529 aa; Ensembl ENSECAP00000056991.1, horse chromosome 1) is the
  horse RASGEF1A ortholog. PANTHER places it in PTHR23113:SF172 (RAS-GEF DOMAIN-CONTAINING
  FAMILY MEMBER 1A), the same subfamily as human RASGEF1A Q8N9B8 (481 aa, Swiss-Prot) and
  Xenopus rasgef1a A0JM95 (interpro/panther/PTHR23113/PTHR23113-entries.csv).
- Global alignment to human (file:HORSE/RASGEF1A/RASGEF1A-bioinformatics/RESULTS.md): 96.25%
  identity over 480 aligned pairs; human Met1 = horse Met6 (5-residue N-terminal extension
  MWEET); a 44-residue insertion (horse 112-155) inside the human REM domain boundary, absent
  from the human canonical isoform. REM 130/130 covered (94.6% identical), catalytic CDC25 domain
  248/248 covered (98.0% identical). C-terminus complete.
- Conclusion: full-length ortholog, not a fragment. The gene model differs from human by the
  N-terminal extension and the internal insertion; whether the insertion is a real horse exon or a
  gene-model artefact is not determinable here. No domain or catalytic region is missing.

### Deep research

`just deep-research-falcon HORSE RASGEF1A --fallback perplexity-lite` failed: falcon
"Failed to authenticate"; perplexity-lite fallback HTTP 401 insufficient quota. No deep-research
file was produced. Review uses the cached primary literature below and the human Swiss-Prot entry.

### Literature (human RASGEF1A; both cached abstract-only)

- [PMID:17121879 "RASGEF1A protein has a guanine nucleotide exchange activity to K-RAS, H-RAS, and N-RAS proteins in vitro"]
  Ura et al. 2006: identified as up-regulated in intrahepatic cholangiocarcinoma; exogenous
  expression raised Ras activity; siRNA slowed ICC cell growth; COS7 overexpression enhanced
  motility in Transwell/wound-healing.
- [PMID:19645719 "RasGEF1A and RasGEF1B function as very specific exchange factors for Rap2 ... They do not act on Rap1 or other members of the Ras subfamily."]
  Yaman et al. 2009 (Wittinghofer lab), purified proteins: Rap2-specific exchange; Phe39 of the
  Rap2 switch I is the specificity determinant.
- These two findings conflict over Ras subfamily substrates. The purified-protein study is the
  more rigorous biochemical test, but both are abstract-only here, so the Ras-activity finding is
  recorded as DISPUTED, not overturned.

### Evolutionary grounding (PAINT, PTHR23113)

- Horse IBA rows come from PTN000560991 (family root, eukaryote-wide: GEF activity, Ras protein
  signal transduction) and PTN007734601 (plasma membrane, broad node seeded by SOS, RasGRP,
  RapGEF and other members). No RASGEF1-clade node carries a term.
- Rap protein signal transduction (GO:0032486) was placed by PAINT only at nodes seeded by
  RAPGEF2/6 (PTN001896698), C3G/RAPGEF1 (PTN004608122) and EPAC (PTN000561159); RASGEF1A is
  not inside those clades and did not inherit it. Several Rap-GEF clades carry IRD NOT Ras
  protein signal transduction; the RASGEF1 clade carries no such negation.

### Decisions

- GEF activity (GO:0005085): ACCEPT (IBA + IEA); core.
- Plasma membrane (IBA is_active_in): KEEP_AS_NON_CORE; family-level inference, no direct data.
- Small GTPase-mediated signal transduction (GO:0007264): ACCEPT. Given the Rap2-vs-Ras
  substrate conflict, this is as specific as the evidence firmly allows (it covers both Ras
  and Rap signalling).
- Ras protein signal transduction (IBA) and positive regulation of Ras protein signal transduction
  (IEA from human IDA): KEEP_AS_NON_CORE; rest on Ura 2006 and the family-root IBD, contested by
  Yaman 2009.
- Cell migration (IEA from human IDA): KEEP_AS_NON_CORE; overexpression motility phenotype.
- No NEW annotations. Rap protein signal transduction was not added: PAINT did not propagate it
  to this clade, and the only support is in vitro exchange on purified Rap2.

### Relative to review next

Human RASGEF1A (Q8N9B8), same PANTHER subfamily SF172, Swiss-Prot with the experimental data;
no review exists in the repo (only genes/EQUAS/RASGEF1A, the donkey ortholog).

### Modules / PANTHER family review

- No family review YAML exists for PTHR23113 under interpro/panther/ (only metadata, entries and
  PAINT tables); no subfamily-placement disagreement to report.
- grep of modules/ for RASGEF1/Rap2/PTHR23113 matched only modules/t_cell_receptor_signaling.yaml,
  and only via the unrelated adaptor GRAP2; no module contains RASGEF1A or a Rap2 pathway.
