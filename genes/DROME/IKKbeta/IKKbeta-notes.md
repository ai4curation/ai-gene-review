# IKKbeta (ird5, DLAK; CG4201; UniProt Q9VEZ5) notes

## Identity
- Drosophila ortholog of mammalian IKKbeta/IKKalpha; Ser/Thr protein kinase, I-kappa-B kinase subfamily (UniProt).
- Forms the Drosophila IKK complex with the regulatory subunit Kenny (key, IKKgamma/NEMO ortholog)
  [PMID:11018014 "identification of a Drosophila IkappaB kinase complex containing DmIKKbeta and DmIKKgamma, homologs of the human IKKbeta and IKKgamma proteins"].

## Imd pathway / Relish activation
- ird5 mutants fail to induce antibacterial peptides, but antifungal Drosomycin induction is unaffected
  [PMID:11156609 "Mutations in ird5 prevent induction of six antibacterial peptide genes in response to infection but do not affect the induction of an antifungal peptide gene"].
- IKK complex is required for Relish cleavage and can phosphorylate Relish in vitro
  [PMID:11018014 "the activated DmIKK complex, as well as recombinant DmIKKbeta, can phosphorylate Relish in vitro"].
- IKK is not needed for Toll-pathway activation of Dif/Dorsal
  [PMID:11018014 "this Drosophila IkappaB kinase complex is not required for the activation of the Rel proteins Dif and Dorsal through the Toll signaling pathway"].
- Two roles: direct phosphorylation of Relish S528/S529 required for RNA Pol II recruitment; noncatalytic support of Dredd-mediated cleavage
  [PMID:19497884 "IKK functions noncatalytically to support Dredd-mediated cleavage of Relish"].
- TAK1 is the IKK-activating kinase [PMID:14519762 "Drosophila TAK1 functions as both the Drosophila IkappaB kinase-activating kinase and the JNK kinase-activating kinase"].
- Early work (DLAK) showed in vitro Cactus binding/phosphorylation in cell lines [PMID:10636911 "DLAK can interact with Cactus, a Drosophila IkappaB and phosphorylate recombinant Cactus, in vitro"];
  in vivo genetics (PMID:11018014, PMID:11156609) indicate the IKK complex is dispensable for Toll/Cactus signalling, so Relish is the physiological substrate.

## Antiviral / STING
- dIKKbeta and Relish required against picorna-like viruses; dSTING acts upstream of dIKKbeta
  [PMID:30119996 "dSTING participated in the control of infection by picorna-like viruses, acting upstream of dIKKβ to regulate expression of Nazo, an antiviral factor"].
- Imd pathway antiviral roles: Sindbis [PMID:19763182], CrPV [PMID:19829691].

## Other contexts
- Hypoxia activates IKK-NF-kB, required for survival [PMID:24993778 "hypoxia activates the IKK-NF-κB [IκB (inhibitor of nuclear factor κB)-NF-κB] pathway and the immune response in Drosophila melanogaster"].

## Deep research
- Falcon deep research was attempted but the run was killed (exit 137, memory pressure on shared host); literature captured here from cached publications instead.

## Review decisions
- Core MF: protein Ser/Thr kinase phosphorylating Relish within the IKK complex (with Kenny).
- generic protein binding rows removed (uninformative); protein catabolic process and TNF-mediated signaling marked over-annotated.
