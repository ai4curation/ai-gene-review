---
provider: affinage
model: Affinage (Claude Sonnet reading pass + Opus synthesis pass)
source_url: https://affinage.wi.mit.edu/api/gene/BABAM1
affinage_run_date: 2026-06-09T22:02:44
uniprot_accession: Q9NWV8
self_evaluation_pairwise: win
faith_pct: 83.33333333333333
n_discoveries: 13
citation_count: 13
note: >-
  Verbatim machine-fetched record from the Affinage API (Cheeseman Lab),
  reproduced as-is as an external deep-research source (like a
  falcon/perplexity report). It is Affinage-authored, LLM-generated, and
  human-only. Curatorial assessment of this record — relevance, correctness,
  trust gates, whether to import its GO grounding — is the reviewer's and
  belongs in the gene review's references[].reference_review, not in this file.
---

# Affinage mechanistic annotation for BABAM1 (human)

## Current model (mechanistic narrative)

BABAM1 (NBA1/MERIT40) is a core structural subunit of the BRCA1-A complex that organizes ubiquitin-directed DNA double-strand break (DSB) signaling and links it to homologous recombination and the broader DNA damage response [PMID:19261749, PMID:19261746]. It is incorporated into the RAP80/Abraxas/BRCC36/BRE-containing complex through a direct C-terminal interaction with BRE/BRCC45 and through contacts with the adaptor ABRAXAS, where it functions as a scaffolding/bridging element that stabilizes the assembly and maintains the protein abundance of BRE and Abraxas [PMID:19261748, PMID:21282113, PMID:24125081, PMID:24667604]. By preserving complex integrity, BABAM1 is required for RAP80-directed retention of BRCA1 at DSBs, for the Lys63-deubiquitinase activity of BRCC36, and for the G2/M checkpoint and ionizing-radiation resistance [PMID:19261749, PMID:19261746]; the same C-terminal BRE-binding motif also sustains the cytoplasmic ABRO1-BRCC36 complex [PMID:21282113]. Beyond DSB repair, BABAM1 acts upstream of FANCD2 in interstrand cross-link repair, where Merit40-null cells show delayed ICL unhooking, reduced end resection, and reduced recombination [PMID:26338419], and it recruits Tankyrase1 to DSBs via an N-terminal RXXPEG/tankyrase-binding motif to promote homologous recombination and proper mitotic spindle assembly, an activity restrained by WWOX [PMID:30533199, PMID:30571846, PMID:37248434]. Its repair function is tuned by phosphorylation: Akt phosphorylates BABAM1 to promote BRCA1-A complex assembly after genotoxic stress, and mTORC2 controls BABAM1 Ser29 phosphorylation to sustain nuclear DNA repair activity [PMID:26027929, PMID:36315652]. Independently of DSB repair, BABAM1 is a subunit of an Lnk-associated Lys63-deubiquitinating complex that attenuates hematopoietic stem cell expansion through a Tpo/Mpl signaling axis [PMID:25636339].

## Affinage mechanism profile (Affinage's own GO/Reactome grounding)

- **molecular_activity:** GO:0060090 molecular adaptor activity, GO:0005198 structural molecule activity
- **localization:** GO:0005634 nucleus, GO:0005829 cytosol
- **pathway (Reactome):** R-HSA-73894 DNA Repair, R-HSA-1640170 Cell Cycle
- **partners:** BRE, ABRAXAS, RAP80, BRCC36, BRCA1, TNKS1, WWOX
- **complexes:** BRCA1-A complex, Abraxas-BRCC36 complex, ABRO1-BRCC36 complex, Lnk-associated K63-deubiquitinating complex

## Dated findings (citation-anchored)

| Year | Confidence | Finding | PMIDs | Journal |
|------|-----------|---------|-------|---------|
| 2009 | High | NBA1/MERIT40 is a component of the BRCA1 A complex (containing BRCA1/BARD1, Abraxas, RAP80, BRCC36, and BRE), is required for resistance to ionizing radiation, localizes to DNA damage sites, maintains BRE and Abraxas protein abundance, and is required for recruitment of BRCA1 to DNA damage sites. Four members of the BRCA1-A complex possess polyubiquitin chain-binding capability. | PMID:19261749 | Genes & development |
| 2009 | High | MERIT40 directly interacts with BRE/BRCC45 and is assembled into the RAP80/Abraxas-containing BRCA1 complex via this interaction. MERIT40 regulates BRCA1 retention at DNA breaks and checkpoint function primarily by maintaining the stability of BRE and the five-subunit complex. | PMID:19261748 | Genes & development |
| 2009 | High | MERIT40 is essential for BRCA1-Rap80 complex protein interactions, stability, and DSB targeting. MERIT40 is required for Rap80-associated Lys63-ubiquitin deubiquitinase (BRCC36 DUB) activity, and for G2 checkpoint and viability responses to ionizing radiation. | PMID:19261746 | Genes & development |
| 2011 | High | NBA1/MERIT40 interacts with BRE through a C-terminal conserved motif of NBA1 and the C-terminal UEV domain of BRE, and this interaction is critical for maintaining the integrity of both the nuclear Abraxas-BRCC36 complex and the cytoplasmic ABRO1-BRCC36 complex. Knockdown of NBA1 decreases protein levels of components in both complexes and impairs BRCA1 recruitment to damage sites. | PMID:21282113 | The Journal of biological chemistry |
| 2015 | Medium | MERIT40 is phosphorylated by Akt following doxorubicin-induced DNA damage. This Akt-mediated phosphorylation of MERIT40 facilitates assembly of the BRCA1-A complex in response to DNA damage and contributes to DNA repair and cell survival. | PMID:26027929 | Cell reports |
| 2015 | High | MERIT40 is required for ICL (interstrand cross-link) repair: Merit40-null mice show hypersensitivity to ICLs but not whole-body irradiation. MERIT40 is recruited to ICL lesions prior to FANCD2, and Merit40-null cells exhibit delayed ICL unhooking, reduced end resection, and reduced homologous recombination at ICL damage. Merit40 mutation exacerbated ICL-induced chromosome instability with Brca2 deficiency but not with Fancd2 mutation, defining its epistatic relationship within the FA-BRCA network. | PMID:26338419 | Genes & development |
| 2015 | High | MERIT40 is a core subunit of an Lnk-associated Lys63 deubiquitinating complex that attenuates HSC expansion. Loss of MERIT40 increases HSC pool size, enhances resistance to cytoablative stress, and increases repopulating ability and self-renewal. M40-null HSCs show hypersensitivity to thrombopoietin (Tpo) stimulation, and HSC phenotypes are abrogated on a Tpo receptor (Mpl)-null background. | PMID:25636339 | Blood |
| 2018 | Medium | MERIT40 directly binds Tankyrase (PARP family) via a tankyrase-binding consensus motif, and recruits tankyrase to DNA double-strand break sites following X-ray irradiation. Cells expressing a tankyrase-binding-deficient MERIT40 mutant fail to rescue the IR-sensitivity phenotype of MERIT40 knockdown cells. | PMID:30533199 | Oncotarget |
| 2019 | Medium | The RXXPEG motif of MERIT40 mediates direct interaction with the ARC-V domain of Tankyrase1 (TNKS1). Mutation of RXXPEG (R28A) disrupts MERIT40-TNKS1 interaction and causes aberrant spindle assembly and chromosome misalignment, demonstrating a role for MERIT40 in spindle structure/function through TNKS1. | PMID:30571846 | Cell biology international |
| 2022 | Medium | BABAM1 phosphorylation at Ser29 is regulated by mTORC2 in glioblastoma cells. Inhibition of mTORC2 reduces pBABAM1(Ser29), decreases DNA repair activity in the nucleus, and promotes apoptosis. mTORC2 also controls γH2AX levels. These findings place BABAM1 as an mTORC2 downstream effector in the DNA damage response. | PMID:36315652 | Journal of proteome research |
| 2013 | Medium | MERIT40 forms a dimer in a concentration-independent manner and contains a stable central domain with structural similarity to vWA-like regions. MERIT40 interacts with ABRAXAS (the adaptor molecule of the BRCA1 complex), helping to bridge and stabilize the complex. | PMID:24125081 | Journal of biomolecular structure & dynamics |
| 2014 | Medium | MERIT40 interacts with ABRAXAS in a non-phosphorylation-dependent manner via the BRCA1-BRCT domain region, acting as an adapter molecule that generates a scaffold among complex members to stabilize the BRCA1-A complex. | PMID:24667604 | Biochemical and biophysical research communications |
| 2023 | Medium | WWOX physically interacts with MERIT40 and inhibits excessive homologous recombination (HR) activity induced by MERIT40 overexpression. WWOX impairs the MERIT40-Tankyrase interaction, preventing the MERIT40-Tankyrase complex from promoting HR at DSBs. | PMID:37248434 | Cancer gene therapy |

## Citations

- PMID:19261746
- PMID:19261748
- PMID:19261749
- PMID:21282113
- PMID:24125081
- PMID:24667604
- PMID:25636339
- PMID:26027929
- PMID:26338419
- PMID:30533199
- PMID:30571846
- PMID:36315652
- PMID:37248434
