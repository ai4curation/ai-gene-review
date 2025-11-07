---
provider: perplexity
model: sonar-pro
cached: false
start_time: '2025-10-19T15:07:59.875485'
end_time: '2025-10-19T15:08:14.654965'
duration_seconds: 14.78
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    reasoning_effort: low
    search_recency_filter: month
    search_domain_filter: []
    return_citations: true
    temperature: 0.1
citation_count: 3
---

## Question

Research the COP1 gene in ARATH, focusing on its molecular function, biological processes, and cellular localization. Include information about protein domains, known interactions, and any disease associations.

## Output

The **COP1 gene in Arabidopsis thaliana (ARATH)** encodes a central regulator of light signaling, acting as a key E3 ubiquitin ligase that controls photomorphogenesis and other developmental processes by targeting specific proteins for degradation[3][6][12].

---

**Molecular Function**

- **E3 ubiquitin ligase activity:** COP1 functions as an E3 ubiquitin-protein ligase, mediating the ubiquitination and subsequent proteasomal degradation of target proteins, most notably the transcription factor HY5, which is a positive regulator of photomorphogenesis[3][6][11].
- **Protein-protein interactions:** COP1 interacts with a variety of substrates and regulatory proteins, including SPA proteins (SUPPRESSOR OF PHYA-105), which modulate its activity, and other transcription factors such as ABI4 and ABI5 involved in abscisic acid (ABA) signaling[11][13].

---

**Biological Processes**

- **Photomorphogenesis:** COP1 is a negative regulator of photomorphogenesis in darkness, repressing light-induced development by targeting positive regulators for degradation. In light, COP1 activity is suppressed, allowing photomorphogenic development[3][12].
- **UV-B response:** COP1 acts as a positive regulator in UV-B signaling, coordinating HY5-dependent and independent pathways for UV-B tolerance[3].
- **Hormone signaling:** COP1 integrates light and ABA signaling, influencing seed germination, seedling establishment, stomatal closure, and abiotic stress responses by modulating the stability of ABA-related transcription factors and co-receptors[11].
- **Root and shoot growth coordination:** COP1 regulates the transcription of PIN1, affecting auxin transport and thus coordinating shoot-to-root growth responses to light[9].

---

**Cellular Localization**

- **Nuclear localization:** COP1 predominantly localizes to the nucleus in darkness, where it represses photomorphogenesis by targeting nuclear proteins for degradation[4][6].
- **Cytoplasmic localization:** In the presence of light, COP1 is exported to the cytoplasm, reducing its nuclear activity and allowing light-responsive gene expression[4][6].
- **Localization signals:** COP1 contains a bipartite nuclear localization signal (NLS) in its core domain and a cytoplasmic localization signal (CLS) overlapping the coiled-coil domain, which regulate its subcellular distribution[4].

---

**Protein Domains**

| Domain                | Location (Amino Acids) | Function                                                                 |
|-----------------------|------------------------|--------------------------------------------------------------------------|
| **RING-finger motif** | N-terminal             | Zinc-binding, essential for E3 ligase activity and protein interactions  |
| **Coiled-coil domain**| Adjacent to RING       | Mediates dimerization and protein-protein interactions                   |
| **Core domain**       | Central                | Contains NLS, essential for nuclear import                               |
| **WD-40 repeats**     | C-terminal             | Protein-protein interactions, substrate recognition                      |

- The modular structure allows COP1 to interact with multiple partners and substrates, conferring its pleiotropic regulatory roles[4][13].

---

**Known Interactions**

- **HY5:** Direct substrate, targeted for degradation to repress photomorphogenesis[3][6].
- **SPA proteins (SPA1–SPA4):** Form complexes with COP1, modulating its activity in light and dark conditions[3][11].
- **ABI4 and ABI5:** Transcription factors in ABA signaling, targeted by COP1 for degradation, integrating light and hormone signaling[11].
- **PIN1:** COP1 regulates its transcription, affecting auxin transport and root-shoot growth coordination[9].
- **CIP1:** COP1-interacting protein, promotes ABA signaling[11].

---

**Disease Associations**

- **No direct human disease associations** are reported for Arabidopsis COP1. However, the mammalian homolog (COP1/ RFWD2) is implicated in cancer and other diseases due to its role in protein degradation and gene regulation[6].
- In Arabidopsis, **mutations in COP1** result in constitutive photomorphogenic phenotypes (de-etiolated seedlings in darkness), seedling lethality in severe alleles, and altered responses to environmental stresses[4][12].

---

**Recent Developments (2023–2024)**

- **Chromatin remodeling:** Recent studies show COP1 controls light-dependent chromatin remodeling, further linking it to epigenetic regulation of gene expression[5].
- **Expanded regulatory network:** New research highlights COP1’s integration of light, hormone, and stress signaling, emphasizing its central role in plant adaptability[11].

---

**Key References**

- UniProt entry for COP1 (P43254): Detailed domain structure, function, and interactions[6].
- Recent reviews and primary research articles (2021–2024) on COP1’s roles in light, hormone, and stress signaling[5][11][12].

---

**Summary Table: COP1 in Arabidopsis thaliana**

| Aspect                | Details                                                                                  |
|-----------------------|------------------------------------------------------------------------------------------|
| **Molecular Function**| E3 ubiquitin ligase, protein-protein interactions                                        |
| **Biological Processes** | Photomorphogenesis, UV-B response, ABA signaling, root-shoot growth coordination      |
| **Cellular Localization** | Nucleus (dark), cytoplasm (light); regulated by NLS and CLS                          |
| **Protein Domains**   | RING-finger, coiled-coil, core (NLS), WD-40 repeats                                     |
| **Known Interactions**| HY5, SPA1–SPA4, ABI4, ABI5, PIN1, CIP1                                                  |
| **Disease Associations** | No direct plant disease; mammalian homolog linked to cancer                           |

**Key URLs and Dates:**
- UniProt: [https://www.uniprot.org/uniprotkb/P43254/entry](https://www.uniprot.org/uniprotkb/P43254/entry) (accessed 2024)
- Frontiers in Plant Science review: [https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.662793/full](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.662793/full) (2021)
- PNAS chromatin remodeling study: [https://www.pnas.org/doi/10.1073/pnas.2312853121](https://www.pnas.org/doi/10.1073/pnas.2312853121) (2024)

## Citations

1. https://www.uniprot.org/uniprotkb/P43254/entry
2. https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2021.662793/full
3. https://www.pnas.org/doi/10.1073/pnas.2312853121