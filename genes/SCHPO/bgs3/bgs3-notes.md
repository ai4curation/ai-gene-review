# bgs3 (SPAC19B12.03 / Q9P377) review notes

## 2026-11-01 initial review

Sources: UniProt Q9P377, GOA (19 rows), PMID:12582133 (abstract only; PMC full
text returned 403), PMID:16823372 and PMID:27974503 (abstract only), and
PMID:42786154 (full text, PMC13612389). No deep-research provider file: no
SCHPO MOD-description provider is configured, and a Perplexity run was not
attempted in this session.

### Key new paper: Willet, Jacob et al. 2026 Nat Commun (PMID:42786154)

- Ghs2 (GH16 single-pass TM protein; Kre6-related) is an obligate partner of Bgs3:
  "Ghs2 is specifically required for the proper subcellular localization of Bgs3,
  but not other glucan synthases" [PMID:42786154]. In the new ts allele bgs3-1 at
  36 °C, GFP-Ghs2 is "almost entirely cytoplasmic" [PMID:42786154].
- Co-IP: "HA3-Ghs2 and GFP-Bgs3 co-immunoprecipitated (Fig. 3b), whereas GFP-Ghs2
  and RFP-Bgs4 did not" [PMID:42786154].
- AF3: GH16 domain "proximal to the predicted β-1,3-glucan extrusion pore of
  Bgs3" [PMID:42786154]. Interface mutant bgs3-5A fails to complement bgs3-1.
- bgs3-1 and ghs2-2 both have thick walls with deposits of up to ~600 nm. Solid-state NMR:
  bgs3-1 reduces mobile branched (β-1,3,6) glucan by ~58% and β-1,6-glucan by ~45%;
  mobile β-1,3-glucan rises ~8-fold [PMID:42786154].
- Model: "Bgs3 synthesizes linear β-1,3-glucan and Ghs2 subsequently introduces
  β-1,6-linked branch points onto the nascent polymer" [PMID:42786154].

### Curation decisions

- MF 1,3-beta-D-glucan synthase activity: ACCEPT (IBA/IEA/ISS). There is no direct assay of
  Bgs3 itself; the activity rests on GT48 family inheritance.
- I did NOT add β-1,6-glucan biosynthesis or glucan branching terms to Bgs3. Ghs2 is
  the entity proposed to perform branching, and the authors interpret the β-1,6-glucan
  loss as downstream. bgs3-1 data show necessity, not participation in that step.
- General process rows (GO:0006075, GO:0051274, GO:0051278) are MODIFIED to
  GO:0071970, which the gene already carries (TAS). Membrane is MODIFIED to plasma membrane.
- Fungal-type cell wall (keyword NAS): REMOVE, because the enzyme is an integral PM protein.
- Cytoplasm HDA (ORFeome): MARK_AS_OVER_ANNOTATED. This is likely secretory or endosomal
  transit; internal puncta were seen in PMID:42786154.
- A GO CC term for the Bgs3-Ghs2 (and analogous Bgs1-Sbg1) synthase-remodeler
  assembly does not exist. This is raised as a suggested question, not proposed.
