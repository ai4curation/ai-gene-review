# NCU09880 evidence notes

NCU09880 is a canonical SmG protein that binds snRNA in the heptameric Sm ring. SmG-containing U1, U2, U4 and U5 small nuclear ribonucleoproteins assemble into the spliceosome and support pre-mRNA splicing. SmG also participates in the assembly intermediates that build these RNA-protein particles.

## Identity and provenance

The exact current accession is Q7S234; NCU09880 is retained as the current locus identifier. No independently established formal gene-symbol replacement was found. Original claims are preserved in NCU09880-protnlm-source.json from the live API snapshot retrieved 2026-09-09T03:00:51.831347+00:00. The current sequence is not proven to be the prediction-time input, and placeholder API dates do not establish release or training membership.

## Primary evidence and justified transfer

- [PMID:27417296] "A seven-subunit Sm protein ring forms a core scaffold of the U1, U2, U4, and U5
snRNPs that direct pre-mRNA splicing."
- [PMID:27417296] "Tests of pairwise combinations of
SmG, SmE, SmF, SmB, and SmD3 alleles highlighted the inherent redundancies
within the Sm ring, whereby simultaneous mutations of the RNA binding sites of
any two of the Sm subunits are lethal."

The specific domain/family observation used is `DR   InterPro; IPR034098; Sm_G.`. Family membership and characterized relatives establish the inference; ARBA or AI-generated names are not independent functional evidence. PAINT is a curator-reviewed ancestral assertion, not donor-count evidence.

## Unresolved assertions

- 7-methylguanosine cap hypermethylation: Cap hypermethylation is catalyzed by Tgs1 and is coupled to snRNP biogenesis, so a noncatalytic SmG contribution is plausible. The retrieved experiments establish SmG-dependent ring assembly but do not resolve the specific SmG requirement for cap hypermethylation underlying this yeast-to-Neurospora transfer. This is not rejected merely because SmG lacks methyltransferase activity.

## Falcon report appraisal

The actual Falcon report was inspected. It supports canonical SmG rather than Lsm7, cooperative snRNA binding and U1/U2/U4/U5 particle membership, consistent with the characterized yeast SmG mutagenesis paper used here (PMID:27417296). It emphasizes lineage variation in assembly routes, so the budding-yeast Brr1/Lot5 route is not added as a Neurospora-specific pathway. The SMN-Sm row is interpreted as the existing curator-assessed ancestral assembly interaction, supported by the explicit SmG-containing human assembly structure (PMID:21816274), rather than direct target complex purification. The report does not provide a specific Neurospora SmG cap-hypermethylation experiment and does not settle that narrower transfer.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted for this section.

### Identity
- Q7S234 is the only UniProt entry for locus NCU09880 (TrEMBL, PE 3). 85 aa, full-length SmG: Sm domain 3..75 (PROSITE PS52002), SmG-specific signature IPR034098 / CDD cd01719. Not a fragment, isoform or alternative gene model. The snRNA-contact triad (Arg24, Phe36, Asn38) and SmE-bridging Arg62 are conserved (`NCU09880-bioinformatics/RESULTS-rereview.md`).

### Evolutionary grounding
- PANTHER PTHR10553:SF2 (SMALL NUCLEAR RIBONUCLEOPROTEIN G), shared with S. cerevisiae SMX2 (P40204), S. pombe smg1 (O74966) and Drosophila SNRPG (Q9VXE0). Human/mouse SNRPG (P62308/P62309) fall in SF26 "SMALL NUCLEAR RIBONUCLEOPROTEIN G-RELATED" with the human SNRPG pseudogene products — a PANTHER subfamily split within orthologous SmG, not a functional divergence; the PAINT node PTN000058285 spans both (`NCU09880-bioinformatics/RESULTS-assembly-rereview.md`).
- Closest experimentally characterised relative by subfamily: S. cerevisiae SMX2 (P40204), structure-guided mutagenesis in [PMID:27417296 "A seven-subunit Sm protein ring forms a core scaffold of the U1, U2, U4, and U5 snRNPs that direct pre-mRNA splicing."]. No review of SMX2 exists in the repo.

### Changes from the previous review
- GO:0034719 SMN-Sm protein complex (IBA): ACCEPT -> KEEP_AS_NON_CORE. Transient assembly intermediate in which SmG is a client. Neurospora encodes an SMN Gemin2-binding-domain protein (NCU01700, Q7RY22) and a SIP1/Gemin2-family protein (NCU00620, Q7SI32), so the IBA is not outside the lineage that retains the machinery.
- GO:0036261 7-methylguanosine cap hypermethylation (IEA, Compara from yeast): UNDECIDED -> MARK_AS_OVER_ANNOTATED. The yeast source is PMID:9528767, where SmE depletion reduced TMG capping [PMID:9528767 "the efficiency of hypermethylation is around 0.51 to 0.61, indicating that depletion of SmE protein affects the snRNA hypermethylation process."]; SmG was not assayed, Tgs1 performs the methylation [PMID:11983179], and PAINT did not propagate this term from the SmG node while propagating snRNP/splicing terms. Necessity of the Sm core, not SmG participation.
- All other rows retained (ACCEPT; protein-containing complex stays MODIFY -> spliceosomal complex), with row-specific reasons and the subfamily evidence added. Description and core function rewritten.

### Family and modules
- Family review `interpro/panther/PTHR10553/PTHR10553-review.yaml` places NCU09880 in SF2 (SmG branch); agrees. It does not note that vertebrate SNRPG sits in SF26.
- No fungal splicing module exists; `modules/dmel_spliceosome.yaml` models the orthologous Drosophila SNRPG (Q9VXE0, same subfamily) in snRNP assemblies.
