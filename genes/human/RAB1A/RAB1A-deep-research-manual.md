# Manual deep research for RAB1A

## Summary

RAB1A is a prenylated Rab-family small GTPase that alternates between cytosolic GDP-bound and membrane-associated GTP-bound states. Its best-established function is at the ER, ERGIC, and Golgi, where Rab1 cycling supports anterograde carrier delivery and Golgi integrity. Direct human evidence comes from TBC1D20-mediated Rab1 inactivation, which blocks secretory cargo delivery from the ER [PMID:17684057], and from bacterial GAPs such as VirA and EspG, which inactivate Rab1 and disrupt ER-to-Golgi trafficking [PMID:22939626].

The autophagy literature identifies a second conserved early role. Bacterial Rab1 inactivation perturbs autophagy-mediated defense [PMID:22939626], and C9orf72 binds Rab1a and the ULK1 complex to help move ULK1 to the phagophore during autophagosome initiation [PMID:27334615].

Several annotations describe peripheral RAB1A uses that are real but not core: RAB1A on early endocytic vesicles recruits Kifc1 for minus-end-directed motility [PMID:21303926], RAB1A supports integrin beta1 recycling to lipid rafts during cell migration [PMID:20639577], and HSV-1 relies on Rab1a/b-dependent ER export of viral glycoproteins for efficient secondary envelopment [PMID:21680502].

In the RNF115/TLR GO-CAM, RAB1A supplies the ER-to-Golgi leg of TLR transport. RNF115 catalyzes K11-linked ubiquitination of RAB1A, reducing GDI1 recruitment and RAB recycling; RAB13 then acts on the later Golgi-to-cell-surface leg for a subset of TLR cargoes [PMID:35343654].

## Curation decisions

- Accepted Rab GTPase activity, G protein activity, ER and Golgi localization, ER-to-Golgi transport, Golgi organization, autophagosome assembly/autophagy, and transport-vesicle membrane rows.
- Kept cytosol, early endosome, endocytosis, cell migration, HSV-1 virion assembly, melanosome, defense-response, neuronal-cell-body, and microtubule vesicle-transport rows as non-core secondary contexts.
- Marked growth hormone secretion, positive regulation of IL-8 production, cadherin binding, extracellular exosome, COPII cargo loading, and positive regulation of glycoprotein metabolism as over-annotations.
- Marked `endomembrane system`, `membrane`, `intracellular protein transport`, and `vesicle-mediated transport` as too general because the same review accepts specific ER, Golgi, transport-vesicle, early-endosome, ER-to-Golgi, and autophagy terms.
- Removed all bare `GO:0005515` protein-binding rows under the generic protein-binding policy while preserving the RAB1A interaction evidence in review support.
