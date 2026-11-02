# glo (Q9VGH5) curation notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full-length Glorund product (586 aa; isoforms A/B/D), FlyBase FBgn0259139. The sibling
folder `genes/DROME/glo/` reviews Q8INJ6 (isoform C, 179 aa, identical over residues 1-168).
No ProtNLM2 file or prediction-evidence folder was opened.

### Setup / provenance
- `just fetch-gene DROME Q9VGH5 --alias glo__Q9VGH5` gave 17 GOA rows (4 IBA, 2 IEA, 11 FlyBase
  experimental/ISS rows, which are the same as those on Q8INJ6).
- `just deep-research-falcon DROME Q9VGH5 --alias glo__Q9VGH5 --fallback perplexity-lite` FAILED:
  Edison returned 403 Forbidden at auth/login, and the Perplexity fallback returned 401 insufficient_quota.
  No deep-research file was written for this folder. The review is based on cached primary papers
  read directly (PMIDs below).

### Evolutionary grounding (glo__Q9VGH5-bioinformatics/RESULTS.md)
- PANTHER 19.0: Q9VGH5 is in PTHR13976:SF76 (named "AT27789P"). Every experimentally
  characterised relative is in a different subfamily: HNRNPH1 SF60, HNRNPF SF32, HNRNPH2 SF33,
  HNRNPH3 SF36, GRSF1 SF42, ESRP1 SF37, ESRP2 SF30, fly fus SF25. No subfamily-level transfer from
  mammalian hnRNP F/H proteins is warranted.
- PAINT: PTN000360053 (hnRNP F/H + GRSF1 + ESRP node) carries only RNA binding, nucleoplasm and
  regulation of RNA splicing. PTN000359854 carries ribonucleoprotein complex. Specific splicing or
  G-quadruplex terms were not propagated, and I treat that as deliberate.

### Experimental evidence on Glo itself (Drosophila)
- Binds nanos TCE stem-loop III; repression in vivo tracks binding [PMID:16516833 "We establish that the ability of the TCE to repress translation in vivo reflects its ability to bind Glorund in vitro."]
- Direct 3'UTR interaction [PMID:19013444 "through a direct interaction with its 3' untranslated region"]
- Each qRRM binds G-tract RNA; crystal structures of qRRM1-3 [PMID:28380354 "Each qRRM domain bound independently to G-tract RNA (Figure 2)"]
- Any two qRRMs suffice for nos repression [PMID:37427795 "In vivo experiments further indicated that any two qRRMs are sufficient to repress nos translation."]
- Post-initiation repression; polysome co-sedimentation [PMID:21460235 "provide evidence that Glo mediates this event"]
- dFMRP recruitment via qRRM2 [PMID:35699205 "Glo's qRRM2 domain specifically and directly interacts with dFMRP"]
- Direct Hrp48 and Hfp binding; nuclear + cytoplasmic; otu-104 rescue; direct test of otu splicing inconclusive [PMID:19013444 "whereas Glo and Hrp48 are both nuclear and cytoplasmic"; "proved inconclusive"]
- G-tract mode alone suffices for chromosome dispersion and D/V functions [PMID:28380354 "Our finding that the G-tract binding mode alone is required for Glo function in dorsal-ventral patterning and chromosome dispersion supports this idea."]
- RNAi lipid phenotypes (PMID:33537463, PMID:41837177) and overexpression testis phenotype
  (PMID:39092172): not used for process annotation (indirect, RNAi-only or gain-of-function).

### Established vs inferred (for downstream transfer)
- Established in fly: mRNA binding (TCE and G-tract), translation repressor activity via
  binding a regulatory element, negative regulation of nanos translation, nuclear + cytoplasmic
  localization, RNP membership, direct Hrp48/Hfp/dFMRP association.
- Inferred only: regulation of RNA splicing (PAINT deep node, partner identity and genetic rescue;
  no direct splicing readout).
- Developmental IMP rows (D/V axis, osk/grk localization, nurse-cell chromosome organization)
  were kept as non-core, since they are probably indirect via otu. Wound healing (screen HMP) was
  marked over-annotated. Bare protein binding rows were removed per policy.
- Isoform C (Q8INJ6) lacks qRRM3 and most of qRRM2, so functions that need two intact qRRMs
  should not be assumed for it.
