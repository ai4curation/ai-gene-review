# dnj-25 (auxilin) curation notes

Scaffold accession: UniProt A0A486WXP9 (TrEMBL, 786-aa isoform W07A8.3d entry;
the module lists the sibling TrEMBL entry D7SFQ5, 458 aa, for the same gene).
PANTHER PTHR23172 AUXILIN/CYCLIN G-ASSOCIATED KINASE-RELATED; single DnaJ domain
at residues 724-784. The single C. elegans auxilin. Module role: auxilin
J-domain co-chaperone in the uncoating tier of
modules/synaptic_vesicle_endocytosis.yaml.

## Primary characterization (Greener et al. 2001, abstract only)

- [PMID:11175756 "In vitro, the molecular chaperone Hsc70 uncoats clathrin-coated vesicles in an ATP-dependent process that requires a specific J-domain protein such as auxilin."]
- [PMID:11175756 "Here we show that C. elegans has a single auxilin homologue that is identical to mammalian auxilin in its in vitro activity."]
- [PMID:11175756 "When RNA-mediated interference (RNAi) is used to inhibit auxilin expression in C. elegans, oocytes show markedly reduced receptor-mediated endocytosis of yolk protein tagged with green fluorescent protein (GFP)."]
- [PMID:11175756 "In addition, most of these worms arrest during larval development, exhibit defective distribution of GFP-clathrin in many cell types, and show a marked change in clathrin dynamics, as determined by fluorescence recovery after photobleaching (FRAP)."]
- [PMID:11175756 "We conclude that auxilin is required for in vivo clathrin-mediated endocytosis and development in C. elegans."]

## Later phenotypes (Joseph et al. 2020, full text; found via deep research)

- [PMID:32069276 "leads to increased clathrin accumulation within the hyp7 epidermis, decreased clathrin mobility (in coelomocytes), and molting defects"]
  (sentence begins "Notably, inhibition of DNJ-25, the C. elegans ortholog of auxilin, ...").
- [PMID:32069276 "Disassembly of the clathrin coat following membrane scission is carried out by the conserved uncoating ATPase Hsc70, together with its co-chaperone(s), auxilin/GAK [29, 71]."]

## Synaptic evidence

- None directly for dnj-25 at synapses in the worm. The synaptic uncoating step
  in C. elegans is documented through unc-26 (coated-vesicle accumulation)
  and inferred for DNJ-25/HSP-1 from the biochemistry and the whole-animal
  clathrin phenotypes; flagged in suggested_questions.

## Review decisions (5 IBA rows)

- All 5 ACCEPT (cytoplasm, vesicle, clathrin binding, clathrin-dependent
  endocytosis, clathrin coat disassembly), each with propagation_review on
  PANTHER:PTN000571055. No NEW rows; core function = clathrin-binding
  J-domain co-chaperone driving clathrin coat disassembly with HSP-1.
- Deep research (falcon) succeeded; it missed Greener 2001 but surfaced
  Joseph 2020, which was cached and used.
