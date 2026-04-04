# ppk34 / ckk2 (SPCC1919.01) - Research Notes

## Gene Identity

- UniProt: Q9UU87
- PomBase: SPCC1919.01
- Current PomBase name: **ckk2** (calcium/calmodulin-dependent protein kinase kinase Ckk2)
- Former name: ppk34 (putative protein kinase 34, from systematic kinase deletion analysis)
- ORF names: SPCC1919.01, SPCC830.12
- 354 amino acids, serine/threonine kinase domain (residues 40-331)

## Nomenclature History

ppk34 was the systematic name assigned by Bimbo et al. 2005 [PMID:15821139] in their "Systematic deletion analysis of fission yeast protein kinases." Cisneros-Barroso et al. 2014 [PMID:25081204] renamed the gene **ckk2** after identifying it as a CaMKK2 homolog: "In addition to Ssp1, we found a second sequence homologous to mammalian CaMKK: SPC1919.01, named Ppk34 for the uncharacterised putative protein kinase 34 in a systematic deletion analysis of fission yeast kinases. Due to its homology to the CaMKK proteins, we have renamed it Ckk2." PomBase now uses ckk2 as the primary gene name.

## Domain Architecture

- CDD: cd14008 (STKc_LKB1_CaMKK) - classifies it in the LKB1/CaMKK subfamily
- PANTHER: PTHR43895 (Calcium/calmodulin-dependent protein kinase kinase-related)
- PANTHER subfamily: PTHR43895:SF150 (Serine/threonine-protein kinase STK11) - note this STK11/LKB1 subfamily assignment may be imprecise
- InterPro: IPR000719 (Protein kinase domain), IPR008271 (Ser/Thr kinase active site)
- Pfam: PF00069 (Pkinase)

## Homology to Mammalian CaMKKs

From PMID:25081204: "Ckk2 is most homologous to mammalian CaMKK2 (34%), followed by Ssp1 (32%) and CaMKK1 (28%)."

S. pombe has two CaMKK-like kinases:
1. **Ssp1** - the primary CaMKK ortholog, constitutively required for AMPK (Ssp2) T-loop phosphorylation
2. **Ckk2/ppk34** - a second CaMKK, with specific roles in calcium and nitrogen stress signaling

## Core Functions (Experimentally Demonstrated)

### Function 1: Activation of Cmk1 in calcium signaling (PMID:25081204)
- Ckk2 phosphorylates and activates the CaM-dependent kinase Cmk1 in response to Ca2+ stress
- Active Cmk1 then phosphorylates and inactivates the Prz1 transcription factor (calcineurin/NFAT homolog)
- This constitutes a negative feedback loop: Ca2+ activates both calcineurin (which activates Prz1) and the Ckk2/Cmk1 cascade (which inactivates Prz1)
- "Ckk2 counteracts calcineurin function by negatively regulating Prz1 activity" [PMID:25081204]
- Delta-ckk2 cells show phenotypes similar to delta-cmk1: Cdc25 fails to accumulate during Ca2+ response

Supporting text from PMID:25081204: "we have identified a second CaMKK in fission yeast, the Ckk2 kinase, which is involved in the activation of Cmk1 in response to Ca2+"

### Function 2: Activation of AMPK (Ssp2) in nitrogen stress (PMID:25639242)
- Ppk34/Ckk2 is specifically required for nitrogen-stress-induced activation of AMPKalpha (Ssp2)
- This is distinct from Ssp1, which is constitutively required for Ssp2 T-loop phosphorylation
- Active AMPK then inhibits TORC1 signaling via the Tsc1/2-Rhb1 axis
- "CaMKKPpk34 is required to induce AMPKalphaSsp2 activation following nitrogen stress" [PMID:25639242]
- Overexpression of Ppk34 induces growth arrest dependent on nutrient environment

Supporting text from PMID:25639242: "a second homolog CaMKK(Ppk34) is specifically required to stimulate AMPKalpha(Ssp2) activation in response to nitrogen stress"

### Signaling pathway summary:
```
Ca2+ stress: Ca2+/CaM -> Ckk2 -> Cmk1 -> phospho-Prz1 (inactive) = negative regulation of calcineurin signaling
N stress:    N stress -> Ckk2 -> Ssp2/AMPK -> Tsc1/2 -> Rhb1 -> TORC1 inhibition
```

## Subcellular Localization (PMID:16823372)
- Cytosol and nucleus (HDA evidence from large-scale GFP localization study by Matsuyama et al. 2006)

## Viability (PMID:15821139)
- ppk34 deletion is viable under standard growth conditions (Bimbo et al. 2005)

## Reactome Pathways (Projected from Human)
- R-SPO-111932: CaMK IV-mediated phosphorylation of CREB (projected from R-HSA-111932)
- R-SPO-442729: CREB1 phosphorylation through CaMKII/CaMKK/CaMKIV cascade (projected from R-HSA-442729)
- R-SPO-9619229: Activation of RAC1 downstream of NMDARs (projected from R-HSA-9619229)
- NOTE: These are all orthologue projections from human. S. pombe does not have CREB, CaMKIV, or NMDARs. These Reactome annotations are misleading for this gene.

## Key Interaction Partners
- **Cmk1** (SPCC74.03c) - direct substrate, phosphorylated by Ckk2 in Ca2+ signaling
- **Ssp2** (SPAC23C4.18c) - direct substrate (AMPKalpha), phosphorylated by Ckk2 at T189 in nitrogen stress
- **Ssp1** (SPCC1259.13) - the other CaMKK, cooperates with Ckk2 in AMPK regulation
- **Prz1** - indirect target (phosphorylated by Cmk1, not directly by Ckk2)
- **Ppb1** (calcineurin) - the phosphatase whose signaling is counteracted by the Ckk2/Cmk1 axis

## Verification of BioReason Claims

### What BioReason got right:
1. Ser/Thr kinase activity - correct
2. Negative regulation of calcineurin-mediated signaling - correct
3. Negative regulation of TORC1 signaling - correct, but mechanism is indirect (via AMPK/Ssp2)
4. Cellular response to calcium ion - correct
5. Cytosol and nucleus localization - correct

### What BioReason got wrong or exaggerated:
1. **"Chronological aging"** - BioReason mentions "chronological aging" and "lifespan traits" but there is NO published evidence for ppk34/ckk2 directly regulating aging. This appears to be an extrapolation from TORC1 inhibition (which CAN affect aging in other contexts) but no such data exists for this gene.
2. **"Phosphorylates calcineurin's regulatory subunit"** - Incorrect. Ckk2 does NOT phosphorylate calcineurin directly. It phosphorylates Cmk1, which then phosphorylates Prz1 (the calcineurin target). The BioReason model confuses the indirect pathway.
3. **"14-3-3 proteins that read phospho-motifs"** as likely interaction partners - While Rad24/Rad25 (14-3-3 proteins) are involved in Prz1 regulation, there is no evidence they directly interact with Ckk2/ppk34.
4. **"PP2A-family phosphatases"** as interaction partners - Speculative; while PP2C phosphatases regulate Ssp2 phosphorylation state, they are not demonstrated Ckk2 interactors.
5. The Reactome pathway annotations are projected from human and do not reflect actual S. pombe biology.
6. The **UniProt Summary** ("Involved in chronological aging and growth control") is fabricated by BioReason and is NOT from UniProt -- UniProt does not contain this text.

### Empty GO predictions:
The BioReason GO Term Predictions sections (MF, BP, CC) are all empty, which is notable.
