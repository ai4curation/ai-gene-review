# Curation Notes for *Variovorax paradoxus* S110 `iadD` (`C5CSP6`, `Vapar_1493`)

## Overview
- **UniProt Accession:** `C5CSP6` (`C5CSP6_VARPS`)
- **Ordered Locus Name:** `Vapar_1493`
- **Gene Symbol:** `iadD`
- **Organism:** *Variovorax paradoxus* S110 (`NCBITaxon:543728`)
- **Protein Function:** Catalytic alpha subunit (`IadD`, 439 aa) of the heterohexameric ($\alpha_3\beta_3$) indole-3-acetic acid (IAA) Rieske non-heme iron aromatic-ring-hydroxylating dioxygenase complex (`IadD/IadE`).

## Literature & Structural Evidence
1. **Discovery of the *Variovorax* `iad` Auxin-Degradation Locus (`PMID:32999461`):**
   - Finkel et al. (2020) *Nature* 587:103–108 demonstrated that a single bacterial genus, *Variovorax*, is necessary and sufficient within a 185-member synthetic root community to revert severe root-growth inhibition (RGI) induced by auxin-producing commensals or exogenous indole-3-acetic acid (IAA) [PMID:32999461, "Here we show that a single bacterial genus, Variovorax, which is taxonomically and metabolically diverse, is able to maintain the developmental programme of the root within a complex community context."].
   - Comparative genomics and RNA-seq under IAA induction identified hotspot 33, a conserved syntenic gene cluster present across all 26 RGI-reverting *Variovorax* genomes that degrades auxin and is required in vivo to maintain stereotypic root growth [PMID:32999461, "Guided by bulk and single-strain inoculations and comparative genomics, we identified a single auxin-degradation operon that is conserved in all available genomes of Variovorax and is necessary and sufficient for the reversion of root growth inhibition."].

2. **Genetic Dissection and Metabolomic Pathway (`PMID:36266335`):**
   - Conway et al. (2022) *Nature Microbiology* 7:1817–1832 genetically dissected the *Variovorax* `iad` operon (`iadR-iadA-iadB-iadC-iadD-iadE-...`) in *Variovorax* sp. CL14 and *Variovorax paradoxus* S110.
   - Heterologous expression in *E. coli* established that `iadD` and `iadE` (`iadDE`, encoding the large and small subunits of the aromatic-ring-hydroxylating dioxygenase) are the minimal gene set sufficient for IAA conversion, and inclusion of the ferredoxin reductase `iadC` (`iadCDE`) boosts IAA degradation efficiency in vitro and is required in vivo in *Variovorax* to achieve the rapid IAA degradation rate needed to revert *Arthrobacter* CL28-induced RGI [PMID:36266335, "Incorporation of IadC (Ferredoxin reductase) to IadD/IadE enhanced transformation of IAA to oxIAA in vitro, although IadC was not essential for the whole-cell degradation in E. coli."].
   - Metabolomic profiling showed that *Variovorax* degrades IAA aerobically via 2-oxindole-3-acetic acid (oxIAA) and dioxindole-3-acetic acid (DOAA) to isatin and anthranilic acid [PMID:36266335].

3. **Crystal/Cryo-EM Structures and Biochemical Mechanism (`PMID:37459330`):**
   - Ma et al. (2023) *PLoS Biology* 21:e3002189 solved the high-resolution crystal structures of apo `IadD/IadE` (PDB `7YLS`) and IAA-bound `IadD/IadE` (PDB `8H2T`) from *Variovorax paradoxus* S110 (`C5CSP6` / `C5CSP7`).
   - `IadD` (large $\alpha$ subunit) and `IadE` (small $\beta$ subunit) assemble into a mushroom-shaped heterohexamer ($\alpha_3\beta_3$) where a trimer of `IadD` forms the catalytic cap and a trimer of `IadE` forms the structural stem [PMID:37459330, "IadD/IadE exhibits a mushroom-shaped quaternary structure handling a 3-fold symmetry axis, with the trimeric α subunits (IadD) functioning as the catalytic 'cap' strategy and the β subunits (IadE) forming the 'stem' base"].
   - Each `IadD` monomer contains:
     - **N-terminal Rieske `[2Fe-2S]` domain (residues 44–160):** Coordinates the `[2Fe-2S]` cluster via Cys85, His87, Cys106, and His109.
     - **C-terminal catalytic non-heme mononuclear iron domain (residues 1–43 and 161–437):** Coordinates the active-site $\text{Fe}^{2+}$ ion via His216, His221, and Asp377 (2-His-1-carboxylate facial triad).
   - Due to the 43.3 Å intrasuubunit distance vs. 11.9 Å intersubunit distance between the Rieske `[2Fe-2S]` cluster and the mononuclear iron center, electrons are transferred **across adjacent `IadD` subunits** via the bridging conserved Asp213 residue (`His109 -> Asp213 -> His216`).
   - Isothermal titration calorimetry (ITC) confirmed direct IAA binding to `IadD` ($K_d = 17.0 \pm 1.9\text{ }\mu\text{M}$ for `IadD/IadE`; $24.1 \pm 3.0\text{ }\mu\text{M}$ for `IadD` alone), and site-directed mutagenesis of active-site residues (`H216A`, `H221A`, `F251A`, `H311A`, `R329A`, `Y362A`) abolished or severely reduced IAA conversion to oxIAA [PMID:37459330].
   - In vivo, `IadD/IadE` shows high substrate specificity for IAA and sluggish/negligible activity toward 2,4-D, IBA, or IPA, explaining why *Variovorax* selectively buffers IAA in the rhizosphere without degrading synthetic auxins such as 2,4-D [PMID:37459330].

## Review of Existing GOA Annotations
- `GO:0005506` (`iron ion binding`, IEA) -> **ACCEPT** (directly supported by structural coordination of catalytic mononuclear $\text{Fe}^{2+}$ by His216, His221, and Asp377 in PDB `7YLS`/`8H2T`, `PMID:37459330`).
- `GO:0051537` (`2 iron, 2 sulfur cluster binding`, IEA) -> **ACCEPT** (directly supported by Rieske `[2Fe-2S]` coordination by Cys85, His87, Cys106, and His109 in PDB `7YLS`/`8H2T`, `PMID:37459330`).

## Proposed New Annotations
- `GO:0016708` (`oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of two atoms of oxygen into one donor`) or `GO:0051213` (`dioxygenase activity`) — `enables`, supported by `PMID:37459330` and `PMID:36266335`.
- `GO:0042437` (`indoleacetic acid catabolic process`) — `involved_in`, supported by `PMID:32999461`, `PMID:36266335`, and `PMID:37459330`.
- `GO:0046982` (`protein heterodimerization activity`) / complex assembly with `IadE` (`C5CSP7`) and homooligomerization in the $\alpha_3\beta_3$ heterohexamer, localized to `GO:0005829` (`cytosol`).
