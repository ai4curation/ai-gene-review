# RASGEF1A (human, Q8N9B8) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: reviewed as the experimentally characterised reference member of PANTHER
subfamily PTHR23113:SF172 (RAS-GEF DOMAIN-CONTAINING FAMILY MEMBER 1A), for later
transfer to the donkey ortholog (EQUAS A0A9L0J8J4). No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon human RASGEF1A --fallback perplexity-lite` failed: the Edison
(falcon) API returned `403 Forbidden` at `/auth/login`, and the perplexity-lite fallback
then hit its 600 s timeout. No deep-research file exists. The review is based on the two
primary papers (both cached abstract-only), the UniProt record, the Reactome entry and the
cached PANTHER PAINT table. A web search found no further primary functional studies of
RASGEF1A.

### Evolutionary placement

- UniProt: `PANTHER; PTHR23113:SF172; RAS-GEF DOMAIN-CONTAINING FAMILY MEMBER 1A`.
  RASGEF1B (Q0VAM2) is in a separate subfamily, SF197.
- Domain architecture: N-terminal Ras-GEF (REM) domain (41..170) and the CDC25-type Ras-GEF
  catalytic domain (214..461), per PROSITE PS50212/PS50009. No transmembrane segment,
  lipidation motif or other targeting domain is annotated.
- PAINT: the GEF activity IBD (GO:0005085) and the Ras protein signal transduction IBD
  (GO:0007265) both sit at PTN000560991 (taxon:2759, the eukaryotic root of the family).
  Q8N9B8 is itself a seed of the GO:0005085 IBD (from its own IDA rows); RASGEF1B Q0VAM2 is
  also a seed. Q8N9B8 is NOT among the seeds of the GO:0007265 IBD. The plasma-membrane
  IBD is at PTN007734601; Q8N9B8 is not a seed of it.
- PAINT has IRD NOT GO:0007265 at several Euteleostomi nodes (PTN002750093, PTN002750101,
  PTN002750108); RASGEF1A still receives the positive IBA, so its lineage is not under
  those NOT nodes.

### Experimental evidence (human protein)

1. Ura et al. 2006 [PMID:17121879 "RASGEF1A protein has a guanine nucleotide exchange
   activity to K-RAS, H-RAS, and N-RAS proteins in vitro"]; [PMID:17121879 "exogenous
   RASGEF1A expression increased the activity of Ras"]; siRNA knockdown slowed
   cholangiocarcinoma cell growth; overexpression in COS7 cells increased motility
   [PMID:17121879 "COS7 cells expressing exogenous RASGEF1A showed enhanced cellular
   motility in Transwell and wound-healing assays"]. RASGEF1A is overexpressed in
   intrahepatic cholangiocarcinoma.
2. Yaman et al. 2009 (Wittinghofer lab, purified proteins) [PMID:19645719 "RasGEF1A and
   RasGEF1B function as very specific exchange factors for Rap2, a member of the Rap
   subfamily of Ras-like G-proteins"]; [PMID:19645719 "They do not act on Rap1 or other
   members of the Ras subfamily"]. Specificity depends on Rap2 Phe39 in switch I.

Conflict: the two papers disagree on substrate. Both show nucleotide exchange activity,
so GO:0005085 is secure. The substrate is not settled: the Wittinghofer-lab data with
purified proteins favour Rap2 and argue against H/K/N-Ras, while Ura et al. reported Ras
exchange in vitro and Ras activation after overexpression. UniProt reports both ("RAP2A,
KRAS, HRAS, and NRAS (in vitro)"). GO:0017034 (Rap GEF activity) is obsolete in GO, so
GO:0005085 is the most specific MF term available.

### Decisions

- GO:0005085 (IBA, 2x IDA, IEA): ACCEPT. Core.
- GO:0007264 small GTPase-mediated signal transduction (IEA): ACCEPT. This holds whichever
  GTPase is the substrate.
- GO:0007265 Ras protein signal transduction (IBA) and GO:0046579 positive regulation of
  Ras protein signal transduction (IDA): KEEP_AS_NON_CORE, because the Ras substrate is
  disputed by the purified-protein study. I did not propose NEW GO:0032486 Rap protein
  signal transduction: the only evidence is in vitro exchange on Rap2, and there is no
  cellular evidence that RASGEF1A activates Rap2. This is raised as a question instead.
- GO:0016477 cell migration (IDA): KEEP_AS_NON_CORE. The only evidence is an
  overexpression motility phenotype in heterologous COS7 cells.
- GO:0005829 cytosol (Reactome TAS) and GO:0005886 plasma membrane (IBA): KEEP_AS_NON_CORE.
  These are plausible for a soluble Ras-family GEF that acts on membrane-anchored GTPases,
  but there is no localization data for RASGEF1A itself.

For transfer to orthologs: only the GEF activity is experimentally established, and only
in vitro (two human studies). The substrate (Rap2 vs H/K/N-Ras), localization and
cellular process roles are inferred or disputed.
