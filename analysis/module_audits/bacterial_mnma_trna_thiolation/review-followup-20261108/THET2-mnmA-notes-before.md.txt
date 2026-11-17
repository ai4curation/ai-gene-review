# THET2 mnmA: source-bounded annotation review

MnmA of Thermus thermophilus HB27 is a C-type ATP-dependent tRNA-uridine 2-sulfurtransferase. Its characterized reconstituted [4Fe–4S] form catalyzes C2 thiolation of tRNA wobble uridine. Purified IscS or SufS can supply cysteine-derived sulfur to this reaction without added reductants; the physiological choice of donor and possible additional carriers remain unresolved.

Reviewed all seeded rows without changing their payloads, order or qualifiers. No NEW rows were added. Broad functions/processes are refined only to existing supported descendants.

A genuine Falcon attempt failed; its command and error are preserved in the new-member-consultation provider ledger and per-gene log. No provider report was fabricated. Manual primary/review reading and official identity records support this review.

The shared evidence and access limits are documented in analysis/module_audits/bacterial_mnma_trna_thiolation/new-member-consultation/evidence.md. The immutable preflight ledger supplies official assay-strain/locus/accession bridges. Target identities are not inferred from a family name alone.

- GO:0002143 (IEA; GO_REF:0000118): ACCEPT. The protein participates in the reconstituted U34 C2-thiolation mechanism, beyond the original necessity phenotype. The target is HB27 TT_C1727, not the distinct HB8 protein. Purified reconstituted MnmA catalyzes the reaction; the donor comparison establishes in-vitro capacity without resolving physiological donor choice. The recorded ancestral source PANTHER:PTN000232485 is assessed as an inherited functional claim, not a pairwise donor count; self-inclusion among descendant evidence is not circular. The lineage-loss check and target-specific source scope are recorded in the consultation.

- GO:0005737 (IEA; GO_REF:0000120): ACCEPT. A cytoplasmic site is consistent with the soluble characterized protein and its intracellular tRNA sulfur-transfer reaction. This is a localization inference from the catalytic/structural context, not a new target-specific fractionation measurement; retain the existing general compartment rather than fabricate a finer localization assay.

- GO:0006400 (IEA; GO_REF:0000104): MODIFY. The general tRNA modification/processing claim is correct, but the supported step is specifically C2 thiolation of wobble uridine, GO:0002143, already present in this review. Refine to that supported descendant. The protein performs catalytic sulfur transfer or supplies the characterized relay structure, rather than merely being a substrate or producing an indirect phenotype.

- GO:0008033 (IEA; GO_REF:0000002): MODIFY. The general tRNA modification/processing claim is correct, but the supported step is specifically C2 thiolation of wobble uridine, GO:0002143, already present in this review. Refine to that supported descendant. The protein performs catalytic sulfur transfer or supplies the characterized relay structure, rather than merely being a substrate or producing an indirect phenotype.

- GO:0016740 (IEA; GO_REF:0000120): MODIFY. The transferase/sulfurtransferase claim is correct but the characterized substrate and position support tRNA-uridine 2-sulfurtransferase activity, GO:0103016, already present in this review. Refine to this specific descendant without inventing a new annotation or assuming one cofactor mechanism for all MnmA homologs.

- GO:0016783 (IEA; GO_REF:0000002): MODIFY. The transferase/sulfurtransferase claim is correct but the characterized substrate and position support tRNA-uridine 2-sulfurtransferase activity, GO:0103016, already present in this review. Refine to this specific descendant without inventing a new annotation or assuming one cofactor mechanism for all MnmA homologs.

- GO:0103016 (IEA; GO_REF:0000120): ACCEPT. The target-specific biochemical evidence establishes ATP-dependent sulfur incorporation at C2 of tRNA U34. Accept the precise catalytic function. The reaction identity does not settle every terminal sulfur-transfer intermediate or imply that the Thermus cluster requirement applies to E. coli or Bacillus MnmA.

## 2026-11-07 — PR6199 source-specific follow-up

PMID:31801798 methods identify HB27 Ttc1727, expressed recombinantly. The U34A substrate control, ATP omission and inactive apoenzyme support ATP-dependent wobble thiolation. Reconstituted iron content was 3.72 ± 0.03 mol per mol protein, with spectroscopic and Cys-mutant support. One authored IDA NEW proposes GO:0051539; it describes measured cluster binding, not native cellular occupancy or a universal D-type requirement. HAMAP MF_00144 supports cytoplasm, with cytosol inferred from the soluble reaction context.
