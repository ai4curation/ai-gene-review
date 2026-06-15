# Curation: PANTHER PTHR35730 — "Kinetochore protein SPC24 homolog-related"

**Family:** PANTHER **PTHR35730** (integrated InterPro entry **IPR044951**,
"Kinetochore protein SPC24-like"); Gene3D 3.30.160.570 ("Ncd80 complex, Spc24
subunit").
**Members:** 696 proteins across 344 proteomes / 981 taxa; 552 AlphaFold models.
Subfamilies: PTHR35730:SF2 (our genes) and SF3; **SF1 was deleted 2019-02-22**.
**Reviewed (Swiss-Prot) members:** exactly **one** — *Arabidopsis thaliana*
SPC24/MUN (**Q67XT3**, At3g08880).
**Curated:** 2026-06-15. Provenance: InterPro REST API, UniProt, and the two
member gene reviews in this repo (SORBI/SORBI_3003G204000, ARATH/SPC24).

> Note: the standard deep-research harness could not be run in this environment
> (the `falcon` provider hits a template-variable bug and times out; `perplexity`
> is not configured; the PANTHER website is behind a CAPTCHA). This curation is
> therefore manual, grounded in the InterPro API and the member gene reviews. It
> is intentionally **not** named `-deep-research-<provider>.md`.

## What this family is

SPC24 is one of the four subunits of the **NDC80 (NDC80–NUF2–SPC24–SPC25)
outer-kinetochore complex**, the principal end-on attachment site coupling
spindle microtubules to centromeres. Within the complex, the NDC80–NUF2 pair
forms the microtubule-binding "head", while the **SPC24–SPC25 pair forms the
coiled-coil/RWD-domain "foot" that anchors the complex to the inner kinetochore**
(MIND/Mis12 complex). The complex is required for accurate chromosome
segregation and for spindle-assembly-checkpoint signaling.

Members are short proteins (~180–210 aa) with an N-terminal/central coiled-coil
and a C-terminal RWD-like globular domain — the SPC24 architecture.

## Key curatorial finding: PTHR35730/IPR044951 is the *plant-lineage* SPC24 family

SPC24 is notoriously **sequence-divergent across eukaryotes**, and PANTHER/InterPro
split it by lineage:

| | Plant SPC24 | Metazoan/general SPC24 |
|---|---|---|
| PANTHER | **PTHR35730** | PTHR22142 |
| InterPro | **IPR044951** "Kinetochore protein SPC24-like" | IPR013252 "Kinetochore-Ndc80 subunit Spc24" |
| InterPro2GO | **GO:0051983** (regulation of chromosome segregation) | *(no GO mapping)* |
| Example member | *A. thaliana* SPC24/MUN (Q67XT3) | *H. sapiens* SPC24 (Q8NBT2) → PTHR22142 |

- A 30-member sample of PTHR35730 is **entirely Viridiplantae** (Brassica,
  Gossypium, Citrus, Cucumis, Arabis, Theobroma, Jatropha, Coffea, Erythranthe,
  Oryza, Leersia, …). I found no metazoan/fungal members in the sample.
- Human SPC24 (Q8NBT2) is **not** in PTHR35730 — it is in **PTHR22142**, which
  integrates into the separate InterPro entry **IPR013252**.
- The two InterPro entries are functional/structural counterparts (both are the
  SPC24 subunit of the NDC80 complex) but are kept distinct because the sequence
  is too divergent for a single signature.

Consequence: **PTHR35730/IPR044951 is reliable for what it contains (plant SPC24
orthologs) but is not the universal SPC24 family.** Completeness (catching all
eukaryotic SPC24s in one signature), not correctness, is the limitation.

## Assessment of the family-level GO mapping (IPR044951 → GO:0051983)

- **Direction: correct, low over-propagation risk.** Unlike functionally
  heterogeneous families, the SPC24 family is mono-functional: every bona-fide
  member is a structural subunit of the NDC80 kinetochore complex. The single
  experimentally characterized member, Arabidopsis SPC24/MUN, is a validated
  kinetochore/NDC80-complex protein whose loss causes chromosome-segregation
  defects, aneuploidy and embryonic lethality [PMID:29356153]; the partner plant
  subunit NUF2 corroborates the complex's mitotic role [PMID:33993566]. So
  propagating "involvement in (regulation of) chromosome segregation" to family
  members by IEA is sound, including to the otherwise-uncharacterized sorghum
  member C5XPJ5.
- **The mapping is, however, narrow and slightly indirect.** SPC24 is a
  *structural* kinetochore subunit; the most informative family-level
  annotations would also include:
  - **CC** GO:0031262 *Ndc80 complex* and GO:0000776 *kinetochore* (the defining
    localization; experimentally supported for the reviewed plant member and for
    the metazoan ortholog).
  - **BP** GO:0007059 *chromosome segregation* (the process the complex executes),
    of which GO:0051983 *regulation of chromosome segregation* is a defensible
    but more oblique framing (justified by the NDC80 complex's contribution to
    spindle-checkpoint control of the metaphase→anaphase transition).
- **Notable asymmetry:** the well-studied metazoan SPC24 entry **IPR013252 has no
  InterPro2GO mapping at all**, while the plant-specific IPR044951 carries one.
  A consistent curation would give both entries the same SPC24/NDC80-complex GO
  terms (CC: NDC80 complex/kinetochore; BP: chromosome segregation), rather than
  leaving the canonical family unannotated and the plant family mapped only to a
  single regulation term.

## Recommendations

1. **Keep** the IPR044951 → GO:0051983 IEA mapping (correct, conservative).
2. **Consider adding** to the family-level mapping the cellular-component terms
   GO:0031262 (Ndc80 complex) and/or GO:0000776 (kinetochore), and the
   biological-process term GO:0007059 (chromosome segregation) — all supported by
   the experimentally characterized Arabidopsis SPC24/MUN and the conserved
   structural role.
3. **Cross-entry consistency:** flag for InterPro that the sibling SPC24 entry
   IPR013252 (metazoan SPC24, PTHR22142) lacks any GO mapping and should receive
   the same SPC24/NDC80-complex terms.
4. **Members:** annotations transferred within PTHR35730 should be restricted to
   the plant lineage; do not assume PTHR35730 captures non-plant SPC24 (use
   PTHR22142/IPR013252 for those).

## Member gene reviews in this repository
- *Sorghum bicolor* **SORBI_3003G204000** (C5XPJ5), PTHR35730:SF2 — uncharacterized;
  single IEA annotation reviewed/ACCEPTED on the basis of this family assignment.
- *Arabidopsis thaliana* **SPC24/MUN** (Q67XT3), PTHR35730:SF2 — the sole reviewed
  member; experimentally validated kinetochore/NDC80-complex subunit
  [PMID:29356153].

## References
- [PMID:29356153] Shin et al. 2018, Plant J — Arabidopsis SPC24/MUN, NDC80
  complex, chromosome segregation, embryonic lethality.
- [PMID:33993566] Li et al. 2021, Plant J — AtNUF2, NDC80-complex subunit,
  spindle/chromosome segregation in mitosis.
- InterPro IPR044951 (SPC24-like; → GO:0051983), IPR013252 (Kinetochore-Ndc80
  subunit Spc24); PANTHER PTHR35730 (plant), PTHR22142 (metazoan).
