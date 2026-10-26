# FCA (At4g16280, UniProt O04425) curation notes

## 2026-10 review session (autonomous pathway module)

- Accession verified: UniProt O04425 FCA_ARATH, At4g16280 (gene_exact search returned a single reviewed entry).
- Deep research (falcon) failed (HTTP 429); review built from cached primary literature.
- FCA: two RRMs + WW domain; nuclear RNA-binding protein [PMID:12805228 "We show that FCA is a nuclear RNA-binding protein and that its WW domain is required for this autoregulation."]
- WW domain binds FY (Pfs2p/WDR33) [PMID:12809608 "We have identified FY as a protein partner for this domain."]
- Autoregulation by proximal polyadenylation in intron 3 [PMID:12805228 "We demonstrate here that FCA negatively regulates its own expression by ultimately promoting cleavage and polyadenylation within intron 3."]
- FLC repression needs FLD (LSD1 homolog) [PMID:17996704 "Here, we show that FCA requires FLOWERING LOCUS D (FLD), a homolog of the human lysine-specific demethylase 1 (LSD1) for FLC downregulation."]
- Proximal antisense (COOLAIR) polyadenylation triggers silencing [PMID:19965720 "A specific RNA-binding protein directs their activity to a proximal antisense polyadenylation site."]
- FCA binds nascent COOLAIR and interacts with CLF [PMID:31032401 "We report that the RNA binding protein FCA interacts with the PRC2 subunit CURLY LEAF (CLF) and binds nascent COOLAIR transcripts to allow deposition of H3K27me3 at FLC."]
- Liquid-like nuclear bodies, FLL2 [PMID:31043738 "We thus conclude that FCA localizes to nuclear bodies with liquid-like properties, suggesting that FCA can undergo liquid-liquid phase separation in vivo."]
- FCA does NOT bind ABA [PMID:19078995 "However, we find that FCA does not bind ABA"].

## Decisions
- NEW: lncRNA binding (GO:0106222, COOLAIR) and mRNA alternative polyadenylation (GO:0110104). FCA does the step (binds RNA and recruits FY/CPSF to the proximal site), so the participation test is met.
- Cytoplasm IBA/ISM and RNP complex IBA (PABP-seeded node) flagged as over-annotation/removal.
- Bare protein-binding rows removed (interactions themselves not disputed).


## 2026-10-26 autonomous-flowering RNA-factor audit

All rows were reviewed, preserving original terms, evidence, references, qualifiers, NOT flags and supporting entities. Falcon/fallback research and gene-publication retrieval ran concurrently under the parent workflow; provider attempts failed and logs remain under `.cache/module-audit-logs/autonomous-flowering-fetch/`. No provider report was fabricated. Primary source caches and curated UniProt evidence were inspected independently. Annotation-reviewer consultation with the chromatin-panel reviewer agreed that nuclear predominance is not organelle exclusion, broad RNP membership does not require PABP identity, and FPA termination reinterpretations are locus-specific.

The authoritative PAINT inspection is reproducible in `genes/ARATH/FCA/FCA-bioinformatics/`. It uses exact existing PTNs and is not a reconstructed family phylogeny. The failed full-family download was not used; only its incomplete .part file was removed after disk exhaustion. Current source retrieval is recorded honestly: PMID18223036 refreshed complete; PMID19439664 cache abstract-only but full web text inspected; 16820865 and19561057 recovered normally; optional16753815 fetch returned429 and was not used to support a new claim.

- Cytoplasm IBA and AtSubP rows are now UNDECIDED: predominantly nuclear FCA:GUS (PMID:12805228) and native nuclear bodies do not prove absence of a cytoplasmic population. PTN000609546 was recovered from authoritative IBD.gaf; no node-placement defect was demonstrated.
- Broad RNP-complex claim now ACCEPT: GO:1990904 requires RNA plus protein, not PABP activity or permanent CPSF membership. PMID:31032401 directly demonstrates FCA–COOLAIR association. PTN002768817 was inspected; prior unsupported PROPAGATION_BAD metadata was replaced.
- PMID:31043738 shows FLL1/FLL3 binding by yeast two-hybrid (Extended Data5d), while FLL2 interaction uses crosslinking/phase separation. The source-specific protein-binding row now cites the actual partners.
- NOT GO:0010427 ABA binding was explicitly audited and retained ACCEPT based on PMID:19078995. No sign inversion or positive ABA-receptor assertion.
- Existing two NEW annotations are retained; no new assertions added. The mRNA-binding IBA remains an inherited biochemical inference, not a claim that autoregulation alone proves direct binding to each mRNA.
