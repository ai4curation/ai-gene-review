# RP2 (O75695) curation notes

## Deep research status
DR_STATUS_PLACEHOLDER

## Summary of function
- XLRP gene; homologous to tubulin cofactor C [PMID:9697692 "The predicted gene product shows homology with human cofactor C, a protein involved in the ultimate step of beta-tubulin folding."]
- Dual N-terminal acylation targets RP2 to the plasma membrane [PMID:10942419 "Our data suggest that the protein is dually acylated and that the palmitoyl moiety is responsible for targeting of the myristoylated protein from intracellular membranes to the plasma membrane."]
- RP2 is the ARL3 GAP [PMID:18376416 "Biochemical analysis showing a 90,000-fold stimulation of the GTPase reaction together with the structure of an Arl3-GDP-AlF4--RP2 transition state complex showed that RP2 is an efficient GAP for Arl3, with structural features similar to other GAPs."]; patient mutations hit the arginine finger [PMID:18376416 "in particular the mutation of the arginine finger of RP2"].
- Earlier work: RP2 + cofactor D stimulates tubulin GTPase [PMID:11847227 "Here we show that in the presence of cofactor D, RP2 protein also stimulates the GTPase activity of tubulin."]; GOA carries a NOT annotation for post-chaperonin tubulin folding from the same paper.
- Localization: basal body/associated centriole, Golgi, periciliary ridge [PMID:20106869 "localizes to the ciliary apparatus, namely the basal body and the associated centriole at the base of the photoreceptor cilium"]; RP2 depletion disperses Golgi-to-cilium vesicles [PMID:20106869 "Depletion of RP2 and dysregulation of Arl3 resulted in dispersal of vesicles cycling cargo from the Golgi complex to the cilium, including the IFT protein IFT20."]
- RP2 is required for NPHP3 ciliary targeting together with ARL3 and UNC119B [PMID:22085962 "Strikingly, knockdown of ARL3, UNC119b, and RP2 each dramatically reduced the percentage of cilia with localized NPHP3 1–200."]; RP2 confines active ARL3 to cilia [PMID:26455799 "The exclusive localization of active Arl3 inside cilia is guaranteed by the Arl3-specific GTPase-activating protein RP2"].

## Key decisions
- GAP activity rows ACCEPT (core).
- protein binding with ARL3: MODIFY to small GTPase binding (binding papers) or GTPase activator activity (GAP papers); HuRI hit REMOVE.
- magnesium ion binding IDA (PMID:26455799): UNDECIDED; cached full text never mentions Mg2+ binding by RP2 (Mg2+ belongs to ARL3's nucleotide site).
- protein folding TAS (homology only): REMOVE.
- Reactome cilium assembly: MARK_AS_OVER_ANNOTATED.
- NEW protein localization to ciliary membrane (GO:1903441), IMP PMID:22085962, with explicit caveat (RP2 could be modelled as regulator of ARL3 only).

## HPA cilium atlas vs module role
- Module (stage 5): ARL3 GTPase-activating protein (GO:0005096), process protein localization to cilium; connection "RP2 negatively regulates ARL3 cargo release".
- HPA v25: no primary cilium/basal body call; main locations End piece; Mid piece; Plasma membrane; Principal piece. GOA HPA row: plasma membrane (GO_REF:0000052).
- Interpretation: the HPA plasma membrane call matches the known acylation-dependent plasma membrane localization; the sperm flagellar calls are consistent with ciliary-type compartments. Lack of a primary-cilium call agrees with the model that RP2 acts at the ciliary base/periciliary membrane and outside cilia to keep ARL3-GTP confined inside the cilium, rather than inside the axoneme. core_functions agree with the module (GAP activity; locations plasma membrane, basal body, periciliary membrane compartment). The module's GO:0061512 is represented by the more specific NEW GO:1903441.
