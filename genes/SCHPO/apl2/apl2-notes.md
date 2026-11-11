# apl2 (O43079, SPBC947.02) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: apl2 is the closest experimentally characterised relative (ortholog) of NEUCR/NCU09721 (Q7S2Q5). This
review assesses apl2 in its own right; no ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon SCHPO apl2 --fallback perplexity-lite` failed: falcon returned "Failed to authenticate"
and the perplexity fallback returned HTTP 401 (quota exceeded). No deep-research file exists. Literature was found
by a PubMed E-utilities search for (apl2 OR AP-1 complex OR apm1 OR AP-1 adaptor) AND (pombe OR fission yeast),
and the relevant hits were cached with `just fetch-pmid`.

### Literature (S. pombe experimental)

- PMID:19624755 (Ma et al. 2009, abstract only in cache). Deletion of each AP-1 subunit; Apl2 = beta.
  "the Deltaapm1 and Deltaapl2 mutants displayed similar but more severe phenotypes than those of Deltaaps1 or
  Deltaapl4 mutants" and "In pull-down assay, Apm1 binds Apl2 even in the absence of Aps1 and Apl4". Subunit
  deletion "caused similar endosomal accumulation of v-SNARE synaptobrevin Syb1"; conclusion: "the four subunits are
  all essential for the heterotetrameric complex formation and for the AP-1 function in exit transport from
  endosomes." Source of the PomBase IDA rows (endosome, Golgi, AP-1 complex, endosome-to-Golgi and endosome-to-PM
  transport).
- PMID:23028933 (Sip1 AP-1 accessory protein, full text). GFP-Apl2 dots co-localise with FM4-64 Golgi/endosomes
  ["suggesting that the four adaptin subunits of the AP-1 complex are localized to the Golgi/endosomes"]; in the
  sip1-i4 mutant Apl2 is diffuse. Sip1 binds each AP-1 subunit including Apl2 in GST pull-downs.
- PMID:21304827 (Rho3, full text). Rho3 overexpression suppresses Δapl2 temperature and immunosuppressant
  sensitivity; Rho3 binds each AP-1 subunit including GST-Apl2 in vitro.
- PMID:23840894 (Sip1/Rho3, full text): AP-1 mislocalised in sip1-i4; mostly about Sip1.
- PMID:15047861 (Kita 2004, apm1): defines AP-1 roles in Golgi/endosome trafficking, secretion, vacuole fusion in
  S. pombe, but only for the mu1 subunit. Context only.
- PMID:18257517 (phosphoproteome): Ser675 phosphorylated.

No S. pombe experiment tests clathrin binding by Apl2 directly, nor endocytosis.

### Sequence / evolution

- 683 aa: Adaptin_N trunk + short hinge; no appendage (ear) domain (bioinformatics/RESULTS.md). Retains a clathrin
  box LLDLD 623-627.
- PANTHER PTHR11134, no subfamily in UniProt. PAINT: apl2 itself is a seed of the AP-1 adaptor complex IBD at
  PTN000123672 (with S. cerevisiae APL2 and Dictyostelium ap1b1). The endocytosis and TGN IBAs come from the deeper
  node PTN000123671, above the beta1/beta2 split, whose endocytosis WITH/FROM list is metazoan only (UniProtKB:P63010 human AP2B1, RGD:71048,
  MGI:MGI:1100869, MGI:MGI:1919020, FB:FBgn0003210, WB:WBGene00000160, ZFIN:ZDB-GENE-061025-1); no fungal
  member is among them.
- The NCU09721 re-review tree (genes/NEUCR/NCU09721/NCU09721-bioinformatics/RESULTS-rereview.md) puts S. pombe apl2
  in the fungal AP-1 beta clade and apl1 in a separate fungal AP-2 beta clade. Fungi therefore have a dedicated AP-2
  beta; plasma-membrane endocytosis is the AP-2 role, so the PTN000123671 endocytosis IBA is likely an
  over-propagation onto fungal AP-1 beta. Marked over-annotated rather than removed: no S. pombe experiment excludes
  it.
- UniProt SUBCELLULAR LOCATION "Cell membrane / coated pit" is ECO:0000250 boilerplate from the adaptin family;
  experimental data place Apl2 at Golgi/endosomes, not the plasma membrane. Plasma membrane IEA removed.

### Decisions in brief

Core: AP-1 complex subunit (IDA/IBA/NAS); contributes to clathrin-cargo adaptor activity (IC); retrograde endosome
to Golgi transport and endosome exit (IDA); located at TGN/Golgi and endosomes. Clathrin binding kept on the basis
of the conserved clathrin box plus PomBase IC, but it is inferred, not demonstrated in S. pombe.

Established experimentally in S. pombe: complex membership/assembly (Apm1-Apl2 pull-down), Golgi/endosome
localisation, requirement for endosomal exit of Syb1, genetic and physical links to Sip1 and Rho3.
Inferred only: clathrin binding, cargo-adaptor activity, TGN specificity.
