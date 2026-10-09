# Cul1 (Cullin-1, lin-19) review notes

Accession: Q24311. Module: dmel_scf_slimb_ubiquitin_ligase (Cul1-Roc1a catalytic core).

## Literature journal

- SCF assembly: [PMID:11500045 "We show that putative Drosophila SCF core subunits dSkpA and dRbx1 both interact directly with dCu11 and the F-box protein Slmb."]
- Roc1a binds Cul1-4: [PMID:18698375 "we show that Drosophila Roc proteins bind specific Cullins: Roc1a binds Cul1-4"].
- Neddylation and substrates: [PMID:12231629 "suggesting that the Cul1-based SCF complex requires Nedd8 modification for the degradation processes of Ci, Arm, and CycE in vivo"]; CSN deneddylates Cul1 in oogenesis [PMID:12737805].
- K11 chains on Ci: [PMID:23747190 "We demonstrate that Cul1-Slimb-based E3 ligase, but not Cul3-Rdx-based E3 ligase, modifies Ci by efficient addition of K11-linked ubiquitin chains."]
- Nutcracker SCF in spermatid caspase activation: [PMID:20392747 "Nutcracker interacts through its F-box domain with members of a Cullin-1-based ubiquitin ligase complex (SCF): Cullin-1 and SkpA."]
- Pruning via InR/TOR [PMID:24068890]; SCA3 polyQ solubility [PMID:30685895].

## Decisions

- Core MF GO:0160072 ubiquitin ligase complex scaffold activity (own), contributes_to GO:0061630 ubiquitin protein ligase activity; GO:0019005. Same pattern as SkpA, Cul2, EloB, EloC.
- Protein binding: SkpA and Rca1 partner rows MODIFY to GO:0160072; Minus row REMOVE.
- GO:0031461 CRL complex and GO:0006511/GO:0030163/GO:0016567 generic parents non-core; regulation-of-catabolism rows non-core; pathway outputs non-core for the shared scaffold.
- Cytoplasm EXP (PMID:20392747) accepted without quote (no explicit Cul1 localization sentence found in the cached full text).
