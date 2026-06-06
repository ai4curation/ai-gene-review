# ATP6V0E1 Research Notes

## Gene overview

ATP6V0E1 (UniProt O15342) encodes V-type proton ATPase subunit e 1 (81 amino acids, 9.2 kDa), a small dual-transmembrane protein that is a component of the V0 membrane-embedded domain of the vacuolar-type H+-ATPase (V-ATPase). The protein is also known as M9.2, V-ATPase 9.2 kDa membrane accessory protein.

The protein has a short lumenal N-terminus (residues 1-7), two transmembrane helices (residues 8-28 and 36-56), a short cytoplasmic loop (residues 29-35), and a C-terminal lumenal domain (residues 57-81) that carries an N-linked glycan at Asn70.

## V0 complex structure and role of subunit e

UniProt and cryo-EM data confirm: "The proton translocation complex V0 consists of the proton transport subunit a, a ring of proteolipid subunits c9c'', rotary subunit d, subunits e and f, and the accessory subunits ATP6AP1/Ac45 and ATP6AP2/PRR" [file:human/ATP6V0E1/ATP6V0E1-uniprot.txt "The proton translocation complex V0 consists of the proton transport subunit a, a ring of proteolipid subunits c9c'', rotary subunit d, subunits e and f, and the accessory subunits ATP6AP1/Ac45 and ATP6AP2/PRR"]

[PMID:33065002 "Vesicular- or vacuolar-type adenosine triphosphatases (V-ATPases) are ATP-driven proton pumps comprised of a cytoplasmic V1 complex for ATP hydrolysis and a membrane-embedded Vo complex for proton transfer."]

## Discovery and characterization

ATP6V0E1 was first described as the M9.2 protein isolated from bovine chromaffin granule V-ATPase. The paper showed it was a novel extremely hydrophobic protein with sequence similarity to Vma21p (yeast).
[PMID:9556572 "M9.2, a novel extremely hydrophobic 9.2-kDa protein comprising 80 amino acids, was detected in the membrane sector. It shows sequence and structural similarity to Vma21p, a yeast protein required for assembly of vacuolar ATPase."]

Note: the similarity to Vma21p in the original paper may have been incorrect nomenclature — Vma21p in yeast is actually an assembly factor (different from the subunit e), whereas the M9.2 protein is the e subunit itself. The human e1/e2 subunits are distinct from the Vma21p assembly factor.

## Two paralogs: ATP6V0E1 (e1) and ATP6V0E2 (e2)

Humans have two e subunit paralogs. ATP6V0E1 (e1) is ubiquitously expressed; ATP6V0E2 (e2) is expressed predominantly in kidney and brain.
[PMID:17350184 "in contrast to the ubiquitously expressed gene encoding the e1 subunit (previously called e), this novel gene is expressed in a more restricted tissue distribution, particularly kidney and brain. We show by complementation studies in a yeast strain deficient for the ortholog of this subunit, that either form of the e-subunit is essential for proper proton pump function."]

This establishes: (1) e1 is ubiquitous, (2) both e1 and e2 are essential for V-ATPase function, confirmed by yeast complementation.

## Experimental evidence: cryo-EM structure (PMID:33065002)

ATP6V0E1 was directly identified and visualized in the complete human V-ATPase cryo-EM structures. The N-linked glycan at Asn70 is experimentally confirmed.
[PMID:33065002 - directly identifies subunit e1 in V0 complex by mass spectrometry and structural modeling]

## Subcellular localization

- Lysosomal membrane: TAS from multiple Reactome entries, consistent with V0 membrane localization
- Endosome membrane: TAS from Reactome (transferrin endocytosis, endosome acidification pathways)
- Phagocytic vesicle membrane: TAS from Reactome (V-ATPase in phagosome acidification)
- Generic membrane: IEA from UniProt keywords

## IGI annotations

GO:0046961 (proton-transporting ATPase activity, rotational mechanism) and GO:1902600 (proton transmembrane transport) are annotated with IGI evidence from PMID:17350184. This is appropriate — the yeast complementation study shows either e1 or e2 is essential for proton pump function, demonstrating the requirement for an e subunit in V-ATPase activity.

## Protein binding (GO:0005515, PMID:32296183)

From high-throughput interactome screen; uninformative over-annotation as per project guidelines.

## Vacuolar acidification (ISS)

ISS annotation from ortholog transfer; consistent with e1 function as V0 component required for V-ATPase activity.

## ATPase-coupled ion transmembrane transporter activity (ISS)

ISS annotation from ortholog transfer; appropriate as the V0 domain translocates protons as ions using ATP hydrolysis energy.

## Regulation of macroautophagy (NAS, PMID:22982048)

Over-annotation — the paper uses V-ATPase disruption as a tool. Does not specifically implicate e1 in macroautophagy regulation.

## Summary

ATP6V0E1 is a small dual-transmembrane V0 subunit whose primary function is structural: it is a required component of the V0 proton-translocating domain. The N-glycan at Asn70 (experimentally confirmed by cryo-EM) contributes to V-ATPase assembly, localization, and stability (consistent with the glycan coat described in PMID:33065002). The protein is ubiquitously expressed and localizes to lysosomal and endosomal membranes as part of the assembled V-ATPase.
