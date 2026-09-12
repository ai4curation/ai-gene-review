# hsp-3 (C. elegans) — Research Notes

Gene: **hsp-3** / HSP70C / C15H9.6 / WBGene00002007
UniProt: **P27420** (HSP7C_CAEEL), 661 aa precursor
Taxon: NCBITaxon:6239 (Caenorhabditis elegans)

## Identity / one-line summary

hsp-3 is one of the two *C. elegans* endoplasmic-reticulum (ER)-resident HSP70/BiP
(GRP78/KAR2) orthologs; the other is **hsp-4** (F43E2.8, WBGene00002008, P20163). HSP-3 is
an ATP-dependent chaperone of the ER lumen that assists folding/quality control of secretory
and membrane proteins. HSP-3 is generally regarded as the more **constitutively expressed**
BiP paralog, whereas hsp-4 is the strongly **stress-inducible** paralog and the source of the
canonical `hsp-4::GFP` ER-stress reporter.

## KNOWN (well-grounded)

### Molecular architecture / family
- UniProt: `RecName: Full=Heat shock 70 kDa protein C; Flags: Precursor;` — belongs to the
  HSP70 family. Signal peptide 1–17; C-terminal ER-retention motif (residues 658–661,
  `MOTIF ... "Prevents secretion from ER"`; the sequence ends `...DDKDEL`, so the functional
  retention tetrapeptide is **KDEL** — note HSP-4 instead uses HDEL). Canonical HSP70
  nucleotide-binding domain (NBD) + substrate-binding domain (SBD) architecture (InterPro
  BIP_NBD IPR042050; CDD `ASKHA_NBD_HSP70_BiP`). [UniProt:P27420]
- ATP binding / ATP hydrolysis are family-level MFs (UniProt KW ATP-binding, Nucleotide-binding;
  GOA IBA GO:0016887, IEA GO:0005524, ISS GO:0016887 by similarity to yeast KAR2 P16474).

### Localization
- ER lumen. UniProt: `SUBCELLULAR LOCATION: Endoplasmic reticulum lumen`. Directly stated for
  HSP-3 in the FIC-1 paper: [PMID:27138431 "HSP-1 is predominantly cytosolic, whereas HSP-3 is
  retained within the ER lumen."]. The signal peptide + `DDKDEL` retention motif are consistent.
- The pan-HSP70 IBA also propagated `cytoplasm`, `nucleus`, and `membrane` to HSP-3. These are
  ancestral/aspecific localizations of the broad HSP70 family (which includes cytosolic and
  nuclear members); for a dedicated ER-lumenal BiP with a cleaved signal peptide and DDKDEL
  motif, these are over-propagations, not the functional site.

### Function — ER protein folding chaperone
- UniProt FUNCTION (by similarity): `Probably plays a role in facilitating the assembly of
  multimeric protein complexes inside the ER.` [UniProt:P27420]
- The two worm BiPs are treated as chaperones that cross-compensate:
  [PMID:27138431 "elegans encodes two Grp78/BiP homologues, hsp-3 and hsp-4, assumed to
  cross-compensate for each other in their roles as ER-residing protein chaperones"].
- GOA: `protein folding chaperone` (GO:0044183, IBA), `protein refolding` (GO:0042026, IBA),
  `ATP hydrolysis activity` (GO:0016887), `heat shock protein binding` (GO:0031072, co-chaperone
  interactions), `endoplasmic reticulum chaperone complex` (GO:0034663), `ERAD pathway`
  (GO:0036503, IBA).

### Function — UPR / ER stress
- HSP-3 (with HSP-4) is part of the BiP-type repressive brake on the three UPR sensors:
  [PMID:27138431 "HSP-3—together with its close homolog, HSP-4—form a complex with IRE-1, ATF-6
  and PEK-1, to preclude activation of UPR-related signaling events by preventing either
  oligomerization of IRE-1 and PEK-1 or proteolytic processing of ATF-6 in the golgi [23]"].
- hsp-3 is itself an ER-stress/UPR target. In the Urano et al. genome-wide microarray, the gene
  **C15H9.6 (= hsp-3)** appears in Table I (genes whose tunicamycin induction is attenuated in
  `xbp-1(zc12)` mutants): induction in N2 = 1.32 ± 0.06 (log2), reduced to 0.68 ± 0.05 in the
  xbp-1 mutant — i.e. hsp-3 IS ER-stress-inducible and xbp-1/ire-1-dependent, though more
  modestly than hsp-4 (F43E2.8; 1.92 → 0.44) and the sHSPs. [PMID:12186849 — Table I lists
  `C15H9.6 ... 1.32 ± 0.06 ... 0.68 ± 0.05`; general framing: "in C. elegans, the ire-1 and
  xbp-1 pathway has retained its essential role in upregulating expression of many UPR target
  genes that are similarly upregulated by the homologous pathway in yeast"].
  NOTE (paralog caution): the extracted Urano Table I places the display label "HSP-4" next to
  cosmid C15H9.6, but C15H9.6 is unambiguously **hsp-3** per WormBase/UniProt ORFName; the GOA
  IEP/HEP annotation of hsp-3 to UPR is therefore based on the gene actually assayed, not a
  mislabel.
- GOA IEP GO:0030968 / GO:0036498 from Shen et al. 2001 [PMID:11779465] (abstract-only in cache;
  curator read full text — the foundational C. elegans UPR paper that established
  ire-1/xbp-1-dependent UPR-target transcription). Defer to curator.

### PTM
- HSP-3 is a direct substrate of the FIC-1 AMPylase (covalent AMP addition). UniProt: `PTM:
  AMPylated by fic-1. {ECO:0000269|PubMed:27138431}`. Direct MS evidence:
  [PMID:27138431 "two classes of proteins over-represented amongst the AMPylated fraction of
  proteins: HSP 70 proteins (HSP-1, HSP-3) as well as translation elongation factors ..."].

### Physiology (hsp-3-specific)
- HSP-3 contributes to tolerance of chronic ER stress and innate immunity:
  [PMID:27138431 "hsp-3 nematodes were very sensitive to P. aeruginosa exposure during early
  development and only few reached adulthood, highlighting a role for HSP-3 in the tolerance of
  chronic ER stress and innate immunity."].
- Recent paralog-resolved work (Urban et al. 2025, Nat Commun 10.1038/s41467-025-65998-0; bioRxiv
  2025.01.14.633073) shows the two BiPs are **functionally diversified**: HSP-3 carries the more
  canonical ER-folding role while HSP-4 is specialized for interorganellar signaling / ER-phagy
  (Sec-62/C18E9.2) and ER-stress mitigation, together controlling body growth, reproduction,
  stress resistance, aging, and autophagy. (DOI-level; not in local PMID cache.)

## NOT known / gaps

- The molecular basis of the hsp-3 vs hsp-4 **division of labor** — differential client
  repertoire, tissue programs, and signaling interfaces — is unresolved; the paralogs are still
  largely "assumed to cross-compensate" [PMID:27138431]. Which clients specifically require
  HSP-3 (vs HSP-4) is not established.
- The functional consequence of HSP-3 **AMPylation** by FIC-1 (does it inhibit/tune HSP-3
  chaperone/ATPase activity in vivo, and under what conditions?) is unknown:
  [PMID:27138431 "Whether AMPylation of different—or even multiple—sites on Heat shock 70 family
  proteins results in diverse changes of their activities remains to be studied."]; and
  [PMID:27138431 "it remains to be tested which proteins may represent the primary in vivo
  targets of FIC-1"].
- Whether the classic BiP→UPR-sensor repression mechanism is exerted specifically by HSP-3 (vs
  HSP-4, or requiring both) in worms is inferred from mammalian precedent (ref [23] in the FIC-1
  paper) rather than shown directly for HSP-3.

## Annotation-review plan (21 GOA annotations)

MF/biology core (ACCEPT): GO:0005788 ER lumen (IBA+IEA); GO:0016887 ATP hydrolysis (IBA/IEA/ISS);
GO:0005524 ATP binding (IEA); GO:0044183 protein folding chaperone (IBA); GO:0042026 protein
refolding (IBA); GO:0031072 heat shock protein binding (IBA); GO:0034663 ER chaperone complex
(IBA+ISS).

UPR (ACCEPT, hsp-3 assayed/part of machinery): GO:0030968 ER UPR (IBA/IEA/IEP×1/HEP×1);
GO:0036498 IRE1-mediated UPR (IEP+HEP).

Non-core (KEEP_AS_NON_CORE): GO:0036503 ERAD pathway (IBA — genuine BiP QC role but no
hsp-3-specific evidence, peripheral to the constitutive folding role).

Over-propagations from pan-HSP70 IBA (MARK_AS_OVER_ANNOTATED): GO:0005737 cytoplasm; GO:0005634
nucleus; GO:0016020 membrane — HSP-3 is a soluble ER-lumen protein (signal peptide + DDKDEL).

## Additional findings surfaced by falcon deep research (hsp-3-deep-research-falcon.md)

The falcon report (real output, 28 citations; verified against primary sources where cached)
corroborates and extends the above. Notable additional, literature-grounded points (cited to
the report's own sources — not all are in the local PMID cache, so treated as context, not as
GOA-annotation evidence):
- AMPylation site mapped to **Thr176** in the NBD; consequences for HSP-3 chaperone activity
  "remain to be fully elucidated"; FIC-1 selectively AMPylates HSP-3 (not HSP-4)
  (truttmann2016; camara2022). Reinforces knowledge-gap 2.
- HSP-3 is ~5-fold more abundant than HSP-4 basally and only ~2-fold DTT-inducible (vs ~9-fold
  for hsp-4); **IRE-1 is required for hsp-3 basal expression** (urban2025; shen2001).
  Confirms hsp-3 = the constitutive paralog.
- **UPR-independent, infection-specific immune role**: Couillault et al. 2012 place HSP-3
  downstream of NIPI-3 / upstream of TPA-1 in epidermal nlp-29 antimicrobial-peptide control
  during *Drechmeria coniospora* fungal infection — not shared with HSP-4, not via canonical
  UPR. (Not in GOA; noted for completeness.)
- **BiP as a temperature sensor** (Shi et al. 2024): at 30°C, folding demand sequesters BiP
  (hsp-3/hsp-4), lowering free BiP and driving ERAD-dependent degradation of TRA-2 to promote
  male germline fate. Provides worm-specific ERAD context (kept hsp-3 ERAD as non-core since
  attributed to BiP collectively).
- Germline-specific hsp-3 ablation shortens lifespan; intestine-specific loss does not
  (urban2025) — tissue-specific physiology.

## Provenance index (cached publications used)
- PMID:27138431 — FIC-1 AMPylase paper (full text). HSP-3-specific: ER-lumen localization,
  AMPylation, UPR-sensor complex, ER-stress/immunity role. HIGH relevance.
- PMID:12186849 — Urano et al. 2002, JCB (full text). Microarray; C15H9.6/hsp-3 is an
  xbp-1-dependent UPR target (Table I). HIGH relevance.
- PMID:11779465 — Shen et al. 2001, Cell (abstract-only). Foundational C. elegans UPR paper;
  source of IEP UPR annotations. MEDIUM–HIGH relevance.
- PMID:2225768 — Heschl & Baillie 1990, review (abstract-only). HSP70 multigene family; ISS
  source for ATP hydrolysis. LOW–MEDIUM relevance.
</content>
</invoke>
