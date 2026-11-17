# New MnmA-panel members: independent annotation consultation

This consultation reviews all 93 seeded annotations of eleven proteins. It preserves their ordered source payloads and qualifiers, and adds no annotation rows. The status COMPLETE denotes completed adjudication, including explicit uncertainty; it does not mean that every biological intermediate has been resolved.

## Identity and source boundary

The immutable preflight contains official UniProt identity records, accession/locus checks, source URLs, full-text acquisitions and access failures. `new-seed-baseline.yaml` fixes the actual seeded records. These sources distinguish a reference sequence from the strain or construct in a paper.

| Reference protein | Accession | Positive evidence and limit |
|---|---|---|
| ECOLI TusA | P0A890 | E. coli relay reconstitution, IscS activation, sulfur carriage and Moco sulfur allocation; regulatory Fe-S phenotypes are separate. |
| ECOLI TusB / TusC / TusD | P45530 / P45531 / P45532 | E. coli TusBCD heterohexamer; the implicated transferable cysteine is TusD Cys78. TusB and TusC contribute structure to this complex activity. |
| ECOLI TusE | P0AB18 | Relay activity, TusBCD stimulation and MnmA–tRNA association; direct covalent TusE-to-MnmA loading remains unresolved. |
| ECOLI MnmA | P25745 | Direct ATP-dependent tRNA U34 thiolation; competing E. coli Fe-S mechanisms are not settled by Thermus results. |
| BACSU IscS1/YrvO / MnmA | O34599 / O35020 | The source genes were amplified from PS832, a 168 derivative. Native conditional MnmA evidence and heterologous E. coli complementation are distinct. No universal interchangeability is claimed. |
| THET2 MnmA | Q72GX1, TT_C1727 | Exact HB27 MnmA, not the separate HB8 entry. C-terminally tagged heterologously expressed enzyme; reconstituted [4Fe–4S] form supports U34 thiolation. |
| THET2 IscS / SufS | Q72LH2, TT_C0087 / Q72HV9, TT_C1373 | Named HB27 donors, individually active in purified MnmA reactions after reductant removal. This does not identify the exclusive native donor. Earlier TtuA/TtuB U54 assays are a separate sulfur destination. |

## Source reading and decisions

PMID:16387657 is abstract-only in the protected cache; publisher access failed in the preflight. Its abstract explicitly reports recombinant pathway reconstitution, TusA stimulation of IscS, IscS-to-TusA sulfur transfer, TusE stimulation of TusA-to-TusD transfer, and TusE interaction with MnmA–tRNA. These are positive experimental findings, not deductions from mutant necessity. PMID:16472754 is also abstract-only; it explicitly gives the TusBCD heterohexamer and TusD Cys78 mutant result. The original IBA source nodes are inherited assertions, not donor counts; a target appearing among its descendant evidence is not circular.

Full PMID:39660893 critically distinguishes the established relay from its unproven last covalent handoff: MnmA was barely radiolabeled in the original complete relay. The same review discusses conflicting E. coli Fe-S results. The 2021 full paper PMID:33744947 and the separately acquired 2024 full counterclaim (DOI:10.3390/inorganics12030067) do not justify a universal MnmA cofactor requirement. Thermus C-type MnmA has direct reconstituted cluster and catalytic evidence; the D-/C-type distinction is not a separate PANTHER family classification.

The full PMID:23281480 TusA study supports sulfur allocation toward Moco, but leaves direct donation to MoeB/MoaD versus intervening YnjE unresolved. The full PMID:38916309 study identifies lowered Fur translation, iron accumulation, altered Suf expression and changes to IscS regulation in the TusA phenotype. Accordingly the existing TusA iron-sulfur cluster assembly annotation is MARK_AS_OVER_ANNOTATED: the phenotype is real, but direct incorporation of iron and sulfur into a cluster by TusA is not demonstrated. TusA's existing cysteine-catabolism claim is accepted because it stimulates the actual desulfurase reaction and accepts sulfur, not because a deletion impairs growth.

Bare TusA protein binding rows are removed under the repository policy; IscS binding itself is not denied. Specific sulfur carriage and the IscS–TusA complex remain represented. TusD sulfurtransferase activity is accepted as complex-dependent transfer. Fresh ontology results show that sulfur carrier GO:0097163 is a molecular-carrier function, not a descendant of sulfurtransferase GO:0016783. It therefore cannot be used as a supposedly narrower enzymatic replacement. For MnmA, GO:0103016 is a verified descendant of GO:0016740 and GO:0016783. GO:0002143 descends from both tRNA modification and tRNA processing. These valid refinements target annotations already present; none creates a new row.

PMID:25825430 is abstract-only in the normal cache, but the genuine full publisher source was read in `preflight/25825430-web-result.json` and `25825430-web-results.json`. The native conditional mutant retained trace MnmA expression, so residual thiolation is not proof of an alternate native pathway. The cognate pair restores thiolation in heterologous E. coli tests where individual proteins did not; this is a bounded partner-compatibility result. The in-vitro IscS comparator is Azotobacter vinelandii, not E. coli. YrvO Cys325 and ATP-dependent sulfur acceptance by MnmA have direct support. The generic GO:1990228 complex term is not synonymous with TusBCD. Bacillus MnmA's component annotation remains UNDECIDED because the established partnership does not independently resolve the physical assembly being annotated; absence of Tus proteins is not a disproof.

Full PMID:31801798 gives the HB27 MnmA construct and two cysteine-desulfurase assays, including removal of reductants and the explicit possibility of unknown carriers in vivo. MnmA is the U34 catalyst; the donors are sulfur-mobilizing enzymes. PMID:16547008's accessible abstract explicitly names TTC0087/TTC1373 and reports enhancement of a TtuA/TtuB-dependent U54 reaction; it does not make MnmA a U54 thiouridylase. The donors' whole-cell allocation remains unresolved. PLP binding is accepted as part of SufS catalytic chemistry with specific signature and reaction-context support, not from an unreviewed ARBA label alone.

The original localization studies are treated carefully. PMID:10830496 reports minor cytoplasmic YhhP/TusA. PMID:18304323 is MC4100 cytosolic proteomics; the original MnmA curator assignment is retained without claiming independent peptide-level verification. Soluble protein architecture plus the cytoplasmic tRNA reaction support the other existing compartment claims. No invented target fractionation assay is offered. Full PMID:38466471 reports MnmA/trmU among boric-acid-sensitive central-dogma mutants; this remains a non-core phenotype, not a new acid-catalytic function.

## Completeness and uncertainty

All eleven real Falcon attempts failed with HTTP 403 authentication errors. Per-target command logs and the provider ledger preserve the failures; no provider output was manufactured. Source reading, identity records and manual curation supplied the review evidence.

PAINT lineage checks complete for the eight E. coli/Bacillus proteins with no reported IRD/IKR loss. The three HB27 targets are absent from their cached reference trees, so their lineage losses were **not checked**; the tool's trailing generic “No IRD or IKR” line is not interpreted as a resolved target placement. Direct locus-qualified experimental evidence supports their activities independently.

TusB and TusC have a contributed complex sulfurtransferase function with structural membership, not an autonomous catalytic or sulfur-carrier claim. Existing process annotations are supported by that structural participation. No new process row is proposed merely because it is absent in a donor protein or because knockout changes an endpoint. No unsupported new molecular activity or new family identity is added.
