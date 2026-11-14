# ECOLI tusA: source-bounded annotation review

TusA is a small cytosolic sulfur-carrier protein that accepts persulfide sulfur from the cysteine desulfurase IscS and supplies the TusBCD/TusE relay for C2 thiolation of tRNA wobble uridine. Binding of TusA stimulates IscS activity. TusA also helps direct sulfur toward molybdenum-cofactor biosynthesis; its effects on iron-sulfur cluster abundance and iron homeostasis include indirect changes in Fur translation and sulfur-mobilization regulation.

Reviewed all seeded rows without changing their payloads, order or qualifiers. No NEW rows were added. Broad functions/processes are refined only to existing supported descendants.

A genuine Falcon attempt failed; its command and error are preserved in the new-member-consultation provider ledger and per-gene log. No provider report was fabricated. Manual primary/review reading and official identity records support this review.

The shared evidence and access limits are documented in analysis/module_audits/bacterial_mnma_trna_thiolation/new-member-consultation/evidence.md. The immutable preflight ledger supplies official assay-strain/locus/accession bridges. Target identities are not inferred from a family name alone.

- GO:0002143 (IDA; PMID:16387657): ACCEPT. The protein participates in the reconstituted U34 C2-thiolation mechanism, beyond the original necessity phenotype. The catalytic or sulfur-carrier role is supported by biochemistry as well as genetics; the mechanistic limits of terminal sulfur delivery do not invalidate process participation.

- GO:0002143 (IEA; GO_REF:0000002): ACCEPT. The protein participates in the reconstituted U34 C2-thiolation mechanism, beyond the original necessity phenotype. The catalytic or sulfur-carrier role is supported by biochemistry as well as genetics; the mechanistic limits of terminal sulfur delivery do not invalidate process participation.

- GO:0002143 (IMP; PMID:16387657): ACCEPT. The protein participates in the reconstituted U34 C2-thiolation mechanism, beyond the original necessity phenotype. The catalytic or sulfur-carrier role is supported by biochemistry as well as genetics; the mechanistic limits of terminal sulfur delivery do not invalidate process participation.

- GO:0005515 (IPI; PMID:15690043): REMOVE. The IscS interaction reported by PMID:15690043 is biologically relevant, but bare protein binding does not describe TusA's sulfur-carrier mechanism. Remove this uninformative term under the protein-binding policy, not as a denial of interaction or a duplicate-row deletion. The specific carrier and IscS–TusA complex annotations are retained.

- GO:0005515 (IPI; PMID:16387657): REMOVE. The IscS interaction reported by PMID:16387657 is biologically relevant, but bare protein binding does not describe TusA's sulfur-carrier mechanism. Remove this uninformative term under the protein-binding policy, not as a denial of interaction or a duplicate-row deletion. The specific carrier and IscS–TusA complex annotations are retained.

- GO:0005515 (IPI; PMID:16606699): REMOVE. The IscS interaction reported by PMID:16606699 is biologically relevant, but bare protein binding does not describe TusA's sulfur-carrier mechanism. Remove this uninformative term under the protein-binding policy, not as a denial of interaction or a duplicate-row deletion. The specific carrier and IscS–TusA complex annotations are retained.

- GO:0005515 (IPI; PMID:24561554): REMOVE. The IscS interaction reported by PMID:24561554 is biologically relevant, but bare protein binding does not describe TusA's sulfur-carrier mechanism. Remove this uninformative term under the protein-binding policy, not as a denial of interaction or a duplicate-row deletion. The specific carrier and IscS–TusA complex annotations are retained.

- GO:0005737 (EXP; PMID:10830496): MODIFY. Cytoplasmic localization is correct; the soluble cytosolic sulfur relay and tRNA substrate context support the more specific cytosol term already carried by this gene. This refinement does not assert a newly measured fractionation experiment: the original localization evidence, characterized soluble protein and intracellular tRNA reaction are considered together.

- GO:0005737 (IEA; GO_REF:0000120): MODIFY. Cytoplasmic localization is correct; the soluble cytosolic sulfur relay and tRNA substrate context support the more specific cytosol term already carried by this gene. This refinement does not assert a newly measured fractionation experiment: the original localization evidence, characterized soluble protein and intracellular tRNA reaction are considered together.

- GO:0005829 (IDA; PMID:10830496): ACCEPT. Retain the curated cytosolic assignment, consistent with the soluble protein and its tRNA sulfur-transfer reaction. For the proteomic/localization sources this preserves the original curator's target assignment rather than claiming a target peptide was independently reidentified; for the inherited TusD row it is a conserved compartment inference, not a donor-count argument.

- GO:0006400 (IEA; GO_REF:0000104): MODIFY. The general tRNA modification/processing claim is correct, but the supported step is specifically C2 thiolation of wobble uridine, GO:0002143, already present in this review. Refine to that supported descendant. The protein performs catalytic sulfur transfer or supplies the characterized relay structure, rather than merely being a substrate or producing an indirect phenotype.

- GO:0006777 (IMP; PMID:23281480): ACCEPT. TusA has a supported sulfur-distribution role in molybdenum-cofactor biosynthesis, supported by MPT/cPMP and molybdoenzyme phenotypes together with its IscS sulfur-carrier chemistry. The full PMID:23281480 study explicitly leaves direct donation to MoeB/MoaD versus an intervening carrier unresolved; it does not establish an obligatory TusA-only route. The later iron-regulatory effects do not negate the supported sulfur-distribution role.

- GO:0016226 (IMP; PMID:38916309): MARK_AS_OVER_ANNOTATED. The full PMID:38916309 study establishes effects of TusA loss on Fe-S abundance and iron homeostasis, but traces them through reduced Fur translation, iron accumulation and changes in sulfur-mobilization regulation. GO:0016226 describes incorporation of iron and sulfur into a cluster. A pleiotropic requirement and modulation of IscS availability do not establish that TusA performs that incorporation step. This is an overextended process assignment, not a claim that the experimental phenotype is false or that TusA can never affect assembly.

- GO:0019448 (IDA; PMID:16387657): ACCEPT. TusA contributes directly to the sulfur-mobilizing breakdown of L-cysteine by stimulating IscS and accepting the released sulfur, as explicitly reported in PMID:16387657 and supported by the full PMID:23281480 activity study. This is a cofactor/acceptor contribution to the reaction, not an assertion that TusA itself has cysteine desulfurase activity or a conclusion from knockout necessity alone.

- GO:0097163 (IDA; PMID:16387657): ACCEPT. TusA covalently accepts persulfide sulfur from IscS and supplies the downstream relay, directly matching the sulfur-carrier definition. Independent biochemistry supports the electronic mapping as well as the experimental row.

- GO:0097163 (IEA; GO_REF:0000120): ACCEPT. TusA covalently accepts persulfide sulfur from IscS and supplies the downstream relay, directly matching the sulfur-carrier definition. Independent biochemistry supports the electronic mapping as well as the experimental row.

- GO:1990329 (IPI; PMID:16387657): ACCEPT. TusA binds IscS in the sulfur-mobilizing complex and stimulates its catalytic activity; this is the mechanistically informative complex annotation corresponding to the nonspecific interaction rows. No generalized protein-binding function is needed to capture this role.

## 2026-11-07 — PR6199 source-specific follow-up

The E. coli relay supports a soluble cytosolic tRNA reaction. Cytosol refinements use the same functional/structural inference for MnmA and TusA/B/C/D/E; no new fractionation measurement is claimed. PMID:16387657 reconstitutes the pathway with recombinant components; PMID:16472754 resolves the TusBCD heterohexamer. Core reaction roles and original annotation payloads are preserved. The frozen seed has 17 rows whereas raw GOA has 18: two GO:0005515/IPI/PMID:16387657 records share the same represented claim and WITH/FROM but differ in assigned-by/date (IntAct versus EcoCyc). This pre-existing seed collapse is documented, not repaired by manufacturing an authored NEW or changing row order.
