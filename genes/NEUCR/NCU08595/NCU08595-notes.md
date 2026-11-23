# NCU08595 evidence notes

NCU08595 is a Rpf2-family ribosome assembly factor with a Brix RNA-binding domain. By conservation with characterized fungal Rpf2, it associates with Rrs1, binds 5S rRNA and promotes incorporation of the 5S ribonucleoprotein particle into nucleolar large-subunit precursors. This assembly step supports large-subunit rRNA maturation.

## Identity and provenance

The exact current accession is Q7SCN3; NCU08595 is retained as the current locus identifier. No independently established formal gene-symbol replacement was found. Original claims are preserved in NCU08595-protnlm-source.json from the live API snapshot retrieved 2026-09-09T03:00:51.831347+00:00. The current sequence is not proven to be the prediction-time input, and placeholder API dates do not establish release or training membership.

## Primary evidence and justified transfer

- [PMID:25855814] "Proteins Rpf2 and Rrs1 are required for 60S ribosomal subunit maturation."
- [PMID:25855814] "gel shift analysis revealed that the Rpf2-Rrs1 complex binds directly
to 5S rRNA."

The specific domain/family observation used is `DR   InterPro; IPR039770; Rpf2.`. Family membership and characterized relatives establish the inference; ARBA or AI-generated names are not independent functional evidence. PAINT is a curator-reviewed ancestral assertion, not donor-count evidence.

## Unresolved assertions

No unresolved GOA assertion remains at the reviewed level of specificity. Experimental observations on relatives are distinguished from target observations.

## Falcon report appraisal

The actual Falcon report supports a conserved Rpf2-Rrs1 assembly-factor role and correctly distinguishes direct fungal-homolog assays from absent target assays. Its principal additional paper, PMID:26117542, was cached and inspected: the Aspergillus complex structure and biochemical data place it against 5S rRNA, RpL5 and Rsa4. Exact excerpt: "The heterodimer forms
specific contacts with the 5S rRNA, RpL5 and the biogenesis factor Rsa4." This agrees with PMID:25855814 used for the main judgment. Specific residue numbers, essentiality and an autonomous nuclease function are not assigned to NCU08595.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this re-review.

### Identity
- Q7SCN3 is the only UniProt entry for locus NCU08595 (TrEMBL, PE 3, 341 aa, sequence version 1). It is the complete product, not a fragment, isoform or alternative gene model. Its length matches PTHR12728:SF0 members (C. thermophilum G0SF80 350 aa, S. cerevisiae P36160 344 aa, human Q9H7B2 306 aa). The Brix domain (FT 28..249) is complete.
- PANTHER: PTHR12728 (BRIX DOMAIN CONTAINING PROTEIN) / SF0 (RIBOSOME PRODUCTION FACTOR 2 HOMOLOG), per the UniProt DR line. The family review `interpro/panther/PTHR12728/PTHR12728-review.yaml` puts NCU08595 in SF0 as a representative, so the two agree. Q7SCN3 is not among the 11 sampled rows of `PTHR12728-entries.csv`, but that is a sampling gap, not a conflicting placement.

### Evolutionary grounding (new analysis)
- `NCU08595-bioinformatics/rpf2_motif_rereview.py` → `RESULTS-rereview.md`. NCU08595 is 74% identical to C. thermophilum Rpf2 and 46% identical to S. cerevisiae Rpf2. The 5S rRNA loop E-binding KKR loop is at K94-K96 in N. crassa, C. thermophilum and yeast. The residue aligned to yeast R236 (5S rRNA binding, PMID:25855814) is R242 in NCU08595.
- The direct EMSA in [PMID:26117542 "These data show that Rpf2 directly binds the 5S rRNA."] used the C. thermophilum (Sordariales) protein, which is in the same PANTHER subfamily and the same order as Neurospora. This is the best-grounded transfer available.
- PAINT node PTN000296192 propagates rRNA binding, nucleolus and LSU-rRNA maturation. It does not propagate the yeast pre-60S complex CC terms. I read that omission as deliberate and do not add them.

### Changes from the previous review
- GO:0019843 rRNA binding (IBA + IEA): ACCEPT → MODIFY to GO:0008097 5S rRNA binding, which is the specific ligand shown for the ortholog. Core MF changed to match.
- GO:0000470 maturation of LSU-rRNA: ACCEPT → MODIFY to GO:0000463, the descendant already present by IBA (correct-but-general rule).
- GO:0042254 ribosome biogenesis: MODIFY now lists both GO:0000027 and GO:0000463.
- GO:0000027 is now stated to be the primary process. Rpf2-Rrs1 physically recruits and holds the 5S RNP, so it does part of the work of assembly. 27SB processing is downstream, and GO:0000463 is retained under the assembly-factor convention.
- Added PMID:26117542 as a reference and rewrote the description.
- No NEW annotations. NCU08595 itself has no experimental data.

### Relative to review next
- S. cerevisiae RPF2 (P36160, SGD:S000001789) is in the same PANTHER subfamily SF0, is the seed donor of PAINT node PTN000296192, and is the best-characterized ortholog. There is no review in the repo (no genes/yeast/RPF2, no P36160 hit).
- Modules: no module under modules/ covers Rpf2/5S RNP assembly. The grep hits were base64 noise in falcon artifacts.
