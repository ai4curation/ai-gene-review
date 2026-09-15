# SERINC2 manual deep-research synthesis

## Scope and provenance

This manual synthesis was prepared after the required automated deep-research attempt failed: Falcon returned HTTP 402 (payment required), and the Perplexity-lite fallback returned HTTP 401 (insufficient quota). No failed provider-named output was retained. Evidence was assembled from reviewed human UniProtKB Q96SA4, all nine GOA rows, and the locally cached primary publications.

## Molecular function and location

SERINC2 is a multipass plasma-membrane phospholipid scramblase. Reviewed UniProt places the human protein at the cell membrane and records non-ATP-dependent bidirectional lipid movement for phosphatidylserine, phosphatidylcholine, and phosphatidylethanolamine. The directly SERINC2-specific purified-protein comparison in PMID:37474505 used NBD-PC proteoliposomes: "each hSERINC flips the NBD-PC lipids" and "hSERINC2 flips at an intermediate rate" [PMID:37474505]. The broader PS/PE/PC substrate statement in the same paper's abstract is clearest for purified hSERINC3 and for the SERINC-family conclusion, while UniProt has curated those catalytic activities for SERINC2.

The direct activity supports GO:0017128 phospholipid scramblase activity. Generic membrane annotations are correct but less informative than GO:0005886 plasma membrane. GO:0017121 plasma membrane phospholipid scrambling is too cellular/process-specific for SERINC2 because available virion assays show that SERINC2 incorporation does not disrupt PS asymmetry.

## Lipid-metabolism and transferred annotations

The older mammalian Serinc-family study reported that Serinc proteins facilitate synthesis of serine-derived membrane lipids [PMID:16120614, "facilitates the synthesis of two serine-derived lipids, phosphatidylserine and sphingolipids."]. That supports retaining phosphatidylserine metabolic process as a broad, non-core consequence, while the direct human evidence defines scrambling rather than biosynthesis as SERINC2's proximal molecular activity.

The acetyltransferase activator activity row was transferred electronically from rat Serinc2. The source paper concerns serine incorporation and membrane-lipid synthesis, and its accessible abstract contains no acetyltransferase assay, direct enzyme-activation assay, or Nat-complex role. The current enzyme activator GO term is defined for direct activation of an enzyme, so a generic replacement would still overstate the accessible evidence. Together with the directly established scramblase function and multipass topology, this makes GO:0010698 a biologically unsupported transfer rather than a second SERINC2 molecular function.

## Antiviral boundary and peripheral localization

SERINC2 should not be assigned the antiviral role established for SERINC3 and SERINC5. In the direct comparison, "hSERINC2 lacks antiviral activity" [PMID:37474505], even though purified SERINC2 retained lipid-flipping activity. The later HIV-1 virion study used SERINC2 as a negative-control paralog and reported robust virion incorporation without restriction or PS-asymmetry disruption [PMID:38785977]. This separation is informative: phospholipid scrambling measured in proteoliposomes is not sufficient for retroviral restriction in the tested system.

The urinary-exosome HDA annotation is supported as non-core high-throughput localization evidence. PMID:19056867 reports an LC-MS/MS inventory of normal human urinary exosomes and states that the proteomic data are publicly accessible. The linked NHLBI urinary-exosome database lists SERINC2/NP_849196 with one peptide under reference 2. This supports retaining the localization as non-core; it does not define SERINC2's molecular activity.

## Open questions

The endogenous regulation and non-viral physiological consequences of SERINC2 scrambling are unknown. Reviewed UniProt lists four isoforms, but the cited functional work does not resolve isoform-specific topology, trafficking, substrate preferences, or activity.
