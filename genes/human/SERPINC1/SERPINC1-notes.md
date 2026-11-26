# SERPINC1 (antithrombin-III, P01008) review notes

## 2026-11-26 session

### Deep research
- `just deep-research human SERPINC1 --provider asta` ran (exit 0), but the
  retrieval returned 20 off-target papers (IgAN prognosis protocol, grey seal
  influenza, OMA orthology primer, PhosphoSitePlus, etc.) with no antithrombin
  content. The output was discarded rather than committed; these notes are a
  manual literature review instead.

### PubMed queries run (PubMed MCP, 2026-11-26)
- `antithrombin heparin pentasaccharide crystal structure thrombin ternary complex` -> 0 hits (too many terms)
- `antithrombin heparin template thrombin structure Li Huntington 2004` -> PMID:15311269
- `antithrombin factor Xa heparin structure Michaelis complex` -> PMID:16619025 (among 7)
- `heparin pentasaccharide antithrombin conformational activation mechanism Jin Carrell` -> PMID:10966821
- `Olson antithrombin-heparin regulation blood clotting proteinases paradigm` -> PMID:20685328 (review, full text)
- `Antiangiogenic activity of the cleaved conformation of the serpin antithrombin` -> PMID:10489375, PMID:18000792
- `antithrombin deficiency mice embryonic lethal Ishiguro` -> PMID:11018075
- Metadata lookup of the UniProt FUNCTION citation PMID:15140129.

### Core biology
- Antithrombin is the principal plasma serpin controlling coagulation proteases:
  [PMID:15311269 "The maintenance of normal blood flow depends completely on the inhibition of thrombin by antithrombin, a member of the serpin family."]
- Targets: thrombin, FIXa, FXa, FXIa, and TMPRSS7 per UniProt
  [file:human/SERPINC1/SERPINC1-uniprot.txt "AT-III inhibits thrombin, matriptase-3/TMPRSS7, as well as factors IXa, Xa and XIa"].
  In vitro also KLK6 [PMID:12878203 "Inhibition of hK6 was achieved via binding to different serpins, among which antithrombin III was the most efficient."].
- Heparin/HS activation, two mechanisms:
  [PMID:16619025 "Inhibition of several coagulation proteases is accelerated by up to 10,000-fold by heparin, either through bridging AT and the protease or by inducing allosteric changes in the properties of AT."]
  Pentasaccharide is allosteric and selective for FXa/FIXa; bridging (template) is needed for thrombin
  [PMID:20685328 "the bridging effect of full-length glycosaminoglycan chains augments antithrombin reactivity with factors Xa and IXa and is solely responsible for upregulating antithrombin reactivity with another important target proteinase, thrombin"].
  Structural basis: [PMID:15311269 "The structure reveals a template mechanism with antithrombin and thrombin bound to the same heparin chain."];
  [PMID:10966821 "the rearrangement of the reactive centre loop that occurs upon activation is part of a widespread conformational change"].
- Physiological activators are endothelial-surface heparan sulfate proteoglycans
  (Reactome R-HSA-9823290). Heparin binding is the obvious missing MF annotation
  (GOA has none for human; mouse P32261 carries GO:0008201 only by ISO).
- Physiology: human deficiency -> thrombophilia (UniProt DISEASE AT3D;
  [PMID:15140129 "We identified two families with significant reduction of circulating antithrombin displaying early and severe venous thrombosis"]).
  Mouse knockout embryonic lethal with fibrin deposition
  [PMID:11018075 "These findings suggest that antithrombin is essential for embryonic survival and that it plays an important role in regulation of blood coagulation in the myocardium and liver."].
- Anti-angiogenic activity of cleaved/latent forms in mouse models
  [PMID:10489375 "Here it is shown that the cleaved conformation of antithrombin has potent antiangiogenic and antitumor activity in mouse models."];
  [PMID:18000792 "The intact native molecule does not have this effect."].
  Mechanism undefined; not proposed as a GO annotation (see below).

### Annotation decisions (summary)
- serpin inhibitor activity rows (IBA/IEA/TAS/NAS): ACCEPT.
- KLK6 protein-binding IPI: MODIFY to GO:0004867; FAM20C protein-binding IPI: REMOVE (kinase-substrate, uninformative).
- identical protein binding (domain-swapped dimer, PMID:18923394): MARK_AS_OVER_ANNOTATED; polymerisation is a pathological serpinopathy conformation.
- blood coagulation TAS: MODIFY to negative regulation of blood coagulation (sign correction, as for PROS1).
- regulation of blood coagulation IEA (IPR033829, antithrombin-specific entry): MODIFY to negative regulation.
- plasma membrane TAS (Reactome, HS-bound on endothelial surface): MODIFY to external side of plasma membrane (as PROS1/F5).
- ER lumen TAS (FAM20C reaction): transit only -> MARK_AS_OVER_ANNOTATED.
- extracellular region rows: ACCEPT. GO:0005615 extracellular space is now obsolete in QuickGO, so no refinement proposed.
- ECM, exosome, blood microparticle HDA: KEEP_AS_NON_CORE.

### NEW-term checks
- GO:0030195 negative regulation of blood coagulation: AT itself performs the
  step (covalent trapping of the proteases). Comparator check by term id via
  QuickGO (exact): TFPI P10646 IDA, PROC P04070 IDA/TAS/IEA, THBD P07204
  IDA/NAS/TAS all carry it (positive control works); SERPIND1 P05546 does not
  (0 hits); SERPINC1 P01008 0 hits. Proposed NEW.
- GO:0008201 heparin binding: MF, direct crystallographic evidence. Proposed NEW.
- GO:0016525 negative regulation of angiogenesis: 0 hits for human P01008 and
  mouse P32261; activity is of non-native conformers in xenograft models with an
  undefined mechanism. Not proposed; recorded as a question/knowledge gap.
