# sucC (PA1588, P53593) notes

## Literature

No deep-research provider was available. PubMed E-utilities returned HTTP 500
on 2026-11-05. The review rests on the full text of PMID:10671455 (cached) and
the reviewed UniProt entry (HAMAP MF_00558).

- SucC and SucD were purified separately; the mixture is active [PMID:10671455
  "an Scs enzymatic reaction was performed with succinate, CoA, and a mixture
  of purified Scs α and β subunits"].
- Dual ADP/GDP specificity [PMID:10671455 "Scs synthesizes essentially an
  equimolar amount of ATP and GTP"]; can also make UTP and CTP at higher NDP
  concentrations.
- NDK-like phosphate transfer from ATP to GDP without succinyl-CoA [PMID:10671455
  "the Scs complex transferred the terminal phosphate from [γ- 32 P]ATP to GDP
  to form GTP"].
- The phosphorylated protein is the 30-kDa alpha subunit [PMID:10671455
  "stimulated the phosphorylation of the 30-kDa Scs α subunit"].

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000212531 | GO:0042709 succinate-CoA ligase complex | 6 | 208 (130 taxa) | GO:0042709, IDA, PMID:10671455 (PseudoCAP) | SOUND | Full text read: activity assayed with the mixture of purified SucC and SucD (neither subunit was assayed alone for the ligase reaction). The heteromer was not isolated, but it is reconstituted functionally. | E. coli SucC P0A836, human SUCLG2 Q96I99, mouse MGI:1306775/MGI:1306824, rat RGD:1305008 | Yes. The other seeds are characterised SCS beta subunits; the term suits the whole SCS-beta clade. |
| PTN000212531 | GO:0004775 succinate-CoA ligase (ADP-forming) activity | 5 | 164 (126 taxa) | GO:0004775, IDA, PMID:10671455 (PseudoCAP) | SOUND | Full text read: forward and reverse SCS reactions with ATP/ADP on reconstituted enzyme. | E. coli SucC P0A836, human SUCLA2 Q9P2R7, Arabidopsis Q84LB6, rat RGD:1309397 | Yes. The node term is right for the clade, and the GTP-specific SUCLG2 branch is excluded by a NOT at PTN000929335 (checked in leaf.gaf). |

No PSEUDOCAP defect on the seed rows and no GO_CENTRAL defect.

## Other decisions

- GO:0046777 protein autophosphorylation (PseudoCAP IDA): REMOVE. The labelled
  protein is SucD, and the label is the catalytic phosphohistidine. A PSEUDOCAP
  WRONG_TERM defect is recorded (PROBABLE). Not a seed.
- GO:0004550 NDP kinase activity: MARK_AS_OVER_ANNOTATED. The activity is real
  in vitro but of unknown relevance, and a dedicated Ndk exists.
- GO:0009142 NTP biosynthesis: KEEP_AS_NON_CORE.
- GO:0003824 and GO:0046872: TOO_GENERAL.

## Reconciliation with the other bacterial SCS reviews (2026-11-18)

The six bacterial succinyl-CoA synthetase reviews (PSEAE, PSEPK and ECOLI sucC and sucD) were compared. PMID:10671455 was re-read in full. Changes to this review:

- core_functions now use contributes_to_molecular_function, as the PSEPK and ECOLI reviews do. The ligase activity was assayed with the mixture [PMID:10671455 "an Scs enzymatic reaction was performed with succinate, CoA, and a mixture of purified Scs α and β subunits (3 μg each)"]. The second entry now carries cytosol.
- Nucleotide wording. No rates were measured, so "as readily as ATP" and "dual specificity" were replaced. GTP is formed from GDP alone [PMID:10671455 "either ADP or GDP could act as a substrate at the lowest concentration tested (50 μM)"]. The equimolar result is a 10-minute end-point on TLC [PMID:10671455 "At equal concentrations, both GTP and ATP were synthesized in essentially equal amounts."]. Because the same preparation moves phosphate between ATP and GDP, an equimolar end-point cannot rank ADP against GDP; that is this review's inference, not the paper's. GO:0004776 stays ACCEPT and core: unlike E. coli, where GTP use is about a tenth as efficient, the authors report no preference [PMID:10671455 "Both GDP or ADP were equally preferred at lower concentrations"].
- The assayed enzyme was recombinant [PMID:10671455 "Both the constructs pKV153 (encoding the Scs α subunit) and pKV152 (encoding the Scs β subunit) were introduced into E. coli BL21(pLysS) for protein expression."]. Copurification with Ndk is an earlier observation on the native enzyme [PMID:10671455 "The Scs protein was shown to copurify with Ndk in P. aeruginosa"].
- Description. "association with the 12-kDa form of Ndk shifts NTP output towards GTP and UTP" overstated the assay, which measured Ndk output with SCS subunits added [PMID:10671455 "very little CTP (<10%) was generated, suggesting that a complex of 12-kDa Ndk and Scs may modulate Ndk activity"].
- GO:0004550 NDP kinase activity stays MARK_AS_OVER_ANNOTATED. Added: the alpha subunit alone gave GTP in the Ndk-modulation assay [PMID:10671455 "the Scs α subunit alone (lane 3) or a combination α and β subunits (lane 7) generated GTP in presence of GDP, CDP, and UDP"]; per the methods that assay used 50 µM GDP/CDP/UDP with labelled ATP as donor. The authors did consider Ndk contamination, but their control addresses only the phosphate-dependent reaction [PMID:10671455 "When we tested the ability of purified P. aeruginosa Ndk to generate any NTP from a mixture of P i , succinyl-CoA, and ADP-GDP-CDP-UDP, no NTP formation was detected (data not shown)."]. A host (E. coli) contaminant in the His-tagged alpha preparation is therefore not excluded for the ATP-dependent transfer. The row is an IDA and the transfer by the mixed subunits is reported, so it is not removed.
- GO:0046777 protein autophosphorylation stays REMOVE, on subunit grounds only. The earlier reason also said a catalytic phosphohistidine is not an autophosphorylation process; the E. coli sucD review holds that the term fits its definition literally and marks the alpha-subunit row over-annotated. The two reviews now agree: the P. aeruginosa row is removed because it is on the beta subunit, which is not the phosphorylated protein [PMID:10671455 "During enzymatic catalysis, Scs undergoes an intermediate Scs-α subunit phosphorylation."]. Both subunits were present in the phosphorylation reaction and only the 30-kDa alpha band is reported as labelled. The source defect is now WRONG_GENE_PRODUCT (corrected value Q51567, SucD), still DELETE_ROW and PROBABLE. QuickGO by reference (2026-11-18): PseudoCAP made GO:0004550, GO:0004775, GO:0009142 and GO:0042709 on both subunits from this paper, and GO:0046777 on sucC only.
- GO:0046872 metal ion binding stays TOO_GENERAL with a fuller reason and the Mg2+ cofactor quote. The row's own evidence is the ATP-grasp signature IPR011761, which does not identify the metal. The PSEPK and ECOLI sucC rows were changed from MODIFY to TOO_GENERAL to match.
- Cytosol (IBA) now quotes the HAMAP family membership and not the TCA sentence, which says nothing about location.
- A duplicated UniProt entry in references was deleted.
- Seed assessment above: the verdicts on this gene's two seed rows stand. The statement that the term suits the whole SCS-beta clade is superseded by the family review, interpro/panther/PTHR11815/PTHR11815-review.yaml, which sets GO:0042709 and GO:0004775 at PTN000212531 to NEEDS_PRUNING for another leaf (Aquifex aeolicus O67330, a citryl-CoA synthetase subunit ortholog). That does not concern P53593.
- Not done here: the family reviews and modules/tca_cycle.yaml do not yet cite this review; that is outside this change.
