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
