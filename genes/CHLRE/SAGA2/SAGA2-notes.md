# SAGA2 (Chlamydomonas reinhardtii) curation notes

UniProt A0A2K3DEH1 (TrEMBL, "CBM20 domain-containing protein"); locus Cre09.g394621
(CHLRE_09g394621v5); 1,816 aa, 189.5 kDa predicted.

**Second UniProt entry.** A0A2K3DEF8 (TrEMBL, 1,748 aa, "CBM20 domain-containing
protein") carries the same ORF name CHLRE_09g394621v5 and EMBL CM008970 (checked by
UniProt REST query on 2026-10-04). The two entries are alternative gene-model products of
one gene. This review uses A0A2K3DEH1, the entry that carries the GOA annotations. Which
model is correct is unresolved.

## Deep research

Deep research was not run. The falcon provider returns HTTP 402 and perplexity is
unavailable in this environment, so the wrapper was skipped on instruction. No
`-deep-research-*.md` file exists for this gene. The review rests on the cached primary
literature below.

## Sequence features (UniProt record)

- Two consecutive CBM20 starch-binding domains, residues 96-206 and 221-343 (PROSITE PS51166; Pfam PF00686; InterPro IPR002044).
- Coiled-coil regions 714-1244; extensive disordered, low-complexity regions (Pro-, Gln-rich) including the C-terminal 1403-1816.
- No predicted transmembrane segment.
- PANTHER PTHR15048:SF0 (STARCH-BINDING DOMAIN-CONTAINING PROTEIN 1), the STBD1 family. The two IBA rows come from this family.
- Four Rubisco-binding motifs [PMID:38241434 "SAGA2 is a ~190-kDa protein that is 30% identical to SAGA1 and has four RBMs and a CBM20 domain"].

## Literature summary

### Meyer et al. 2020 (PMID:33177094): naming, motif, localization
- Named here [PMID:33177094 "The protein we named SAGA2 (Cre09.g394621)"]; it co-precipitated with the anti-SAGA1 antibody because it carries the same Rubisco-binding motif.
- Rubisco bound SAGA2 internal motif peptides on arrays [PMID:33177094 "Rubisco bound to all predicted internal motif sites when we incubated purified Rubisco with arrays of peptides tiling across the full-length proteins"].
- SAGA2-Venus at the matrix-starch interface [PMID:33177094 "We observed that SAGA2 also localized to that interface but appeared to cover the surface of the matrix more homogeneously than SAGA1."].

### Atkinson/Chan et al. 2024 (PMID:38241434): Arabidopsis proto-pyrenoid
- SAGA2 transit peptide targets chloroplast stroma [PMID:38241434 "the native SAGA2 transit peptide could target SAGA2::mNeon to the chloroplast stroma"].
- Y2H with Rubisco LSU/SSU and EPYC1 helices [PMID:38241434 "Similar to SAGA1, SAGA2 interacted with both CrRbcS and the Chlamydomonas large subunit of Rubisco (CrRbcL)"].
- Recruits starch to the condensate, and binds starch outside it as well [PMID:38241434 "Together, our imaging data suggested that SAGA2 interacts differently with the condensate compared to SAGA1 but is also able to recruit starch to the matrix."].
- Note: this paper calls the CBM20 C-terminal; UniProt puts both CBM20s at the N terminus.

### Hennacy et al. 2024 (PMID:39548241)
- SAGA2 excluded from tubule biogenesis [PMID:39548241 "but it is unlikely to contribute to matrix-traversing membrane biogenesis based on the growth phenotypes of the saga2 mutant"].

### Crans et al. 2026 (PNAS PMID:42090253): primary SAGA2 genetics and biochemistry
- Direct starch binding by the purified two-CBM20 construct [PMID:42090253 "We observed that both the 10×His-mVenus-2×SAGA1-CBM20 and the 10×His-mVenus-SAGA2-2×CBM20 proteins, but not a 10×His-mVenus control protein, bound to starch"], competed by beta-cyclodextrin and maltoheptaose.
- SAGA2 is depleted from tubule entry sites, where SAGA1 is enriched [PMID:42090253 "Our results indicate that whereas SAGA1 is enriched at the starch–tubule–matrix junctions of the pyrenoid, SAGA2 is depleted from these regions"].
- saga2 grows normally, has a single pyrenoid and normal tubules [PMID:42090253 "These observations indicate that SAGA2 is not necessary for pyrenoid tubule formation."].
- saga2 has reduced starch coverage at 3 h of low CO2 (33% vs WT), rescued by SAGA2-Venus, normal by 21 h [PMID:42090253 "Taken together, these results indicate that SAGA2 is necessary for normal matrix–starch sheath coverage early during pyrenoid formation."].
- Double mutant has no sheath; starch in the stroma; either gene rescues [PMID:42090253 "suggesting that SAGA1 and SAGA2 function redundantly to localize starch sheaths to the pyrenoid"].
- Starch granule initiation is proposed as a model only; not annotated.

## Decisions

1. **IBA vacuolar transport and membrane (PTN000386078, STBD1 family): REMOVE.** The
   node is seeded by mammalian STBD1 (ER-anchored, glycophagy). SAGA2 shares only the CBM20,
   has no membrane anchor, is chloroplast-targeted and acts at the matrix-starch interface,
   away from membranes. Target-specific evidence of divergence, recorded in propagation_review.
2. **IEA carbohydrate binding, starch binding: ACCEPT.** Confirmed by the direct binding
   assay (domain-level). Consistent with SAGA1.
3. **NEW pyrenoid (GO:1990732) IDA** from SAGA2-Venus localization.
4. **No process term.** GO has no starch sheath assembly/localization term. GO:0033037
   polysaccharide localization exists but QuickGO shows only 2 annotations (Chst11,
   glycosaminoglycan), so it is not an established home for starch tethers. Raised as a
   suggested question, consistent with the SAGA1 review. Tubule terms (GO:0160223,
   GO:0010027) are explicitly not applicable to SAGA2.

## Module (pyrenoid_ccm, starch_sheath_barrier)

SAGA2 is not a participant yet. Proposed annoton, mirroring saga1_matrix_starch_linker:
participant UniProtKB:A0A2K3DEH1; function GO:2001070 starch binding; location GO:1990732
pyrenoid; no process.
