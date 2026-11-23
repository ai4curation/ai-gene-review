---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/ARPC4
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: P59998
self_evaluation_pairwise: win
faith_pct: 100.0
n_discoveries: 26
citation_count: 25
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for ARPC4 (human)

## Current model (mechanistic narrative)

ARPC4 (p20-Arc) is a core structural subunit of the seven-protein Arp2/3 complex, the actin nucleator that builds branched filament networks at sites of dynamic polymerization such as lamellipodia and bacterial actin tails [PMID:9230079]. Together with ARPC2, ARPC4 forms the structural core of the complex through long C-terminal alpha helices and similarly folded N-terminal alpha/beta domains [PMID:11721045], and it serves as a subunit-interaction hub contacting ARPC2, ARPC3, and ARPC5 [PMID:11162547]. The ARPC2–ARPC4 interface directly engages the mother actin filament: residues at this surface are required for actin nucleation, Y-branch formation, high-affinity F-actin binding, and branch stability [PMID:20404198, PMID:18381280], and the ARPC1–ARPC4 contact is required to propagate the WASp activation signal [PMID:20071330]. Activation involves global conformational reorganization transmitted to ARPC4 upon ATP and WASp-VCA binding [PMID:19298826], with auto-inhibitory salt bridges at the Arp2–Arp3–ARPC4 interface gating the complex; their disruption yields constitutive nucleation [PMID:22125478]. ARPC4 activity is regulated post-translationally: UFL1, when phosphorylated by Akt, UFMylates ArpC4 to promote lamellipodia formation, migration, and metastasis [PMID:40419786], whereas clostridial binary toxins ADP-ribosylate ARPC4 to inhibit nucleation and collapse F-actin networks [PMID:36429089]. Through this branched-actin function, ARPC4 supports a broad range of cellular and tissue processes — epidermal homeostasis with Nrf2 restraint [PMID:29113991], pancreatic acinar-to-ductal metaplasia downstream of mTORC1/2–Rac1 signaling [PMID:33388318], intestinal epithelial barrier integrity under mechanical stress [PMID:40930096], microglial maturation [PMID:41760937], and cancer cell migration and invasion across tumor types [PMID:23267127, PMID:31190401, PMID:41793310]. A recurrent de novo missense variant (p.Arg158Cys) causes reduced cellular F-actin in patients with microcephaly and speech delay, linking ARPC4 to a neurodevelopmental disorder [PMID:35047857].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0005198 structural molecule activity, GO:0008092 cytoskeletal protein binding
- **localization:** GO:0005856 cytoskeleton, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-1266738 Developmental Biology, R-HSA-1643685 Disease
- **partners:** ARPC2, ARPC3, ARPC5, ARPC1, UFL1
- **complexes:** Arp2/3 complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 1997 | High | ARPC4 (p20-Arc) was identified as one of seven subunits of the human Arp2/3 complex; the complex localizes to lamellipodia of fibroblasts and Listeria actin tails (but not actin bundles), consistent with a role in promoting actin assembly at sites of dynamic polymerization. | PMID:9230079 | The Journal of cell biology |
| 2001 | High | Crystal structure of bovine Arp2/3 complex at 2.0 Å resolution revealed that ARPC4 (p20) and ARPC2 (p34) form the core of the complex through long C-terminal alpha helices and similarly folded N-terminal alpha/beta domains. | PMID:11721045 | Science (New York, N.Y.) |
| 2001 | Medium | Yeast two-hybrid analysis showed that p20-Arc (ARPC4) acts as a hub for subunit interactions within the human Arp2/3 complex, interacting with p21-Arc (ARPC3), p34-Arc (ARPC2), and p16-Arc (ARPC5); p41-Arc only interacted with the p20-Arc/p16-Arc heterodimer. Structural integrity was important for p20-Arc/p21-Arc association, while the N-terminal half of p34-Arc was dispensable for its binding to p20-Arc. | PMID:11162547 | Biochemical and biophysical research communications |
| 2010 | High | Molecular dynamics and protein-protein docking simulations, validated by mutagenesis, defined an actin-filament-binding interface on ARPC2 and ARPC4. Residues at this interface are required for actin nucleation, Y-branching, high-affinity F-actin binding, and Y-branch stability, demonstrating that Arp2/3 complex affinity for F-actin independently modulates branch formation and stability. | PMID:20404198 | Proceedings of the National Academy of Sciences of the United States of America |
| 2010 | Low | Molecular dynamics simulations of Arp2/3 activation showed that one structural block (comprising Arp2, ARPC1, the globular domain of ARPC4, and ARPC5) rotates ~30° around a pivot point in an alpha-helix of ARPC4 (Glu81–Asn100) to bring Arp2 into proximity with Arp3 during activation. | PMID:20959098 | Biophysical journal |
| 2011 | Medium | Phosphorylation of Arp2 destabilizes a network of auto-inhibitory salt-bridge interactions at the interface of Arp2, Arp3, and ARPC4, permitting Arp2 reorientation to an activation-competent state. A gain-of-function ARPC4 mutant predicted to disrupt these interactions showed substantial actin nucleation activity in the absence of NPFs. | PMID:22125478 | PLoS computational biology |
| 2009 | Medium | Hydrogen/deuterium exchange mass spectrometry showed that ATP binding to Arp2/3 complex causes conformational rearrangements in Arp2 and Arp3 that are allosterically transmitted to ARPC4 (and ARPC1, ARPC2, ARPC5); WASp VCA binding further modulates exchange rates in ARPC4, indicating global conformational reorganization involving this subunit upon activation. | PMID:19298826 | Journal of molecular biology |
| 2008 | High | In S. cerevisiae, a contact surface between p35/ARPC2 and p19/ARPC4 was identified as required for actin nucleation and endocytosis; mutations near this interface abolished nucleation without disrupting complex integrity. | PMID:18381280 | The Journal of biological chemistry |
| 2010 | High | In S. cerevisiae, lethal mutations at the p40/ARPC1 contact with p19/ARPC4 specifically impaired WASp-induced nucleation of purified Arp2/3 complex, placing ARPC4 at the interface required for WASp activation signal propagation. | PMID:20071330 | The Journal of biological chemistry |
| 2017 | High | Conditional knockout of Arpc4 in mouse epidermis depleted the Arp2/3 complex and caused a psoriasis-like disease; Arpc4 knockout in cultured keratinocytes was sufficient to induce nuclear accumulation of Nrf2, upregulation of Nrf2 target genes, and decreased F-actin levels. In vitro, Nrf2 was shown to bind to filamentous actin. | PMID:29113991 | Development (Cambridge, England) |
| 2021 | High | Conditional ablation of Arpc4 in mouse pancreatic acinar cells demonstrated that the Arp2/3 complex is required for KrasG12D-driven acinar-to-ductal metaplasia (ADM) in vivo; mTORC1 regulates Arp2/3 complex activity via Rac1/Arp3 translation while mTORC2 promotes Arp2/3 via Akt/Rac1, converging on ARPC4-containing Arp2/3 as a common downstream effector for actin cortex remodeling and ADM. | PMID:33388318 | Gastroenterology |
| 2021 | Medium | A recurrent de novo missense variant in ARPC4 (p.Arg158Cys) found in patients with microcephaly and speech delay was associated with decreased F-actin levels in cells from affected individuals, implicating ARPC4 in actin filament network formation required for neurodevelopment. | PMID:35047857 | HGG advances |
| 2025 | High | UFL1 (UFM1-specific E3 ligase 1) interacts with ArpC4 and catalyzes its UFMylation. Akt phosphorylates UFL1 at T426, which enhances UFL1's interaction with ArpC4 and promotes ArpC4 UFMylation, thereby facilitating lamellipodia formation, cell migration, invasion, and metastasis. | PMID:40419786 | Nature structural & molecular biology |
| 2022 | Medium | Binary clostridial toxins (CDT, C2I, Iota) ADP-ribosylate ARPC4/5 (among other Arp2/3 subunits) in addition to actin and Arp2, and this modification inhibits Arp2/3 complex actin-nucleating activity, causing collapse of lamellipodia and F-actin networks in cells. | PMID:36429089 | Cells |
| 2013 | Medium | siRNA-mediated silencing of ARPC4 significantly reduced cell migration (50–68% decrease) in pancreatic cancer cell lines without affecting other processes, indicating ARPC4 is a key functional subunit for Arp2/3-dependent migration in these cells. | PMID:23267127 | Anticancer research |
| 2019 | Medium | ARPC4 knockdown in T24 bladder cancer cells attenuated migration, invasion, and pseudopodia formation and disrupted actin cytoskeleton structure, demonstrating a direct role of ARPC4 in actin-dependent invasive behavior. | PMID:31190401 | Journal of cellular biochemistry |
| 2016 | Low | Chemical cross-linking/mass spectrometry identified the entire seven-subunit Arp2/3 complex (including ARPC4) as an interaction partner of human PKD2 in both cytosolic and Golgi-enriched fractions, with evidence of a direct protein-protein interaction between PKD2 and Arp2/3. | PMID:27559607 | Journal of proteome research |
| 2013 | Medium | Expression of ARPC4 in Mycobacterium tuberculosis severely impaired bacterial growth (evidenced by TEM showing outer-coat shedding), enhanced bacterial clearance in infected macrophages, impaired phagosome-to-lysosome translocation, and suppressed pro-inflammatory cytokine responses. ARPC4 was shown to interact with the essential mycobacterial secretory protein Rv1626, downregulating its expression ~6-fold; Rv1626 also interacted with mammalian Arp2/3 and enhanced actin polymerization. | PMID:23894563 | PloS one |
| 2016 | Low | Viral protein Ac34 (baculovirus) co-immunoprecipitated with ARPC4 (P20) of Sf9 (insect) cells and induced its nuclear relocation; however, mammalian ARPC4 did not interact with Ac34 and was not relocated, indicating species-specific binding specificity. | PMID:27900558 | Virologica Sinica |
| 2025 | Medium | In cervical cancer cells, Aurora-A overexpression upregulated ARPC4 expression via activation of the NF-κBp65 signaling pathway (increased NF-κBp65 phosphorylation led to elevated ARPC4 levels), and ARPC4 knockdown antagonized Aurora-A-promoted migration, invasion, and EMT. | PMID:40294934 | Nan fang yi ke da xue xue bao |
| 2019 | Medium | A genome-wide CRISPR knockout screen in THP-1 macrophages identified ARPC4 loss-of-function as conferring resistance to Salmonella uptake, placing ARPC4-containing Arp2/3 complex in the actin dynamics pathway required for macrophage phagocytic internalization of bacteria. | PMID:31594818 | mBio |
| 2025 | High | In a gut epithelium-specific inducible Arpc4 knockout mouse, loss of Arp2/3 function led to increased intestinal permeability, disrupted tight junction protein localization, epithelial fracturing, and lethality under mechanical challenge; ex vivo organoid experiments showed defects required mechanical stress and elevated actomyosin contractility to manifest. | PMID:40930096 | Current biology : CB |
| 2026 | Medium | Conditional Arpc4 knockout in myeloid cells showed that Arp2/3 complex loss in Langerhans cells leads to cell decline through DNA damage accumulation associated with aberrant nuclear shapes, lamina reduction, and nuclear envelope rupture, revealing a role for Arp2/3/ARPC4 in nuclear envelope integrity and genome maintenance in tissue-resident immune cells. | — | bioRxiv |
| 2026 | High | Conditional Arpc4 knockout in microglia showed that Arp2/3 depletion prevents the developmental transition of microglia into ramified cells with homeostatic gene profiles and surveillance function, linking ARPC4-dependent actin branching to microglial maturation in the CNS. | PMID:41760937 | EMBO reports |
| 2026 | Medium | CRISPR/Cas9 knockout of Arpc4 in murine PDAC cell lines downregulated all Arp2/3 complex members and significantly impaired PDAC cell migration, disrupted branched tubular structure formation in collagen I, and inhibited invasive front formation in organoid culture; β1 integrin signaling was identified as a key upstream regulator of Arp2/3-dependent migration through collagen-rich matrices. | PMID:41793310 | International journal of cancer |
| 2026 | Medium | ArpC4 knockdown by siRNA in U2OS cells reduced HDR efficiency, but this effect corresponded with decreased transfection efficiency and reduction in S/G2M cell cycle phases rather than a direct role in DNA repair; WASP/N-WASP were found dispensable for HDR. | PMID:41963733 | EMBO reports |

## Citations

- PMID:11162547
- PMID:11721045
- PMID:18381280
- PMID:19298826
- PMID:20071330
- PMID:20404198
- PMID:20959098
- PMID:22125478
- PMID:23267127
- PMID:23894563
- PMID:27559607
- PMID:27900558
- PMID:29113991
- PMID:31190401
- PMID:31594818
- PMID:33388318
- PMID:35047857
- PMID:36429089
- PMID:40294934
- PMID:40419786
- PMID:40930096
- PMID:41760937
- PMID:41793310
- PMID:41963733
- PMID:9230079
