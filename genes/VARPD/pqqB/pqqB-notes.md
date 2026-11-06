# Curation Notes for *Variovorax paradoxus* `pqqB` (`A0A0H2M8Q2`, `VPARA_00950`)

## Overview
- **UniProt Accession:** `A0A0H2M8Q2` (`A0A0H2M8Q2_VARPD`)
- **Ordered Locus Name:** `VPARA_00950` (`pqqB1` / `pqqB`, encoded at the 5' end of the `pqqBCDE` cluster `VPARA_00950`–`VPARA_00920`)
- **Gene Symbol:** `pqqB`
- **Organism:** *Variovorax paradoxus* (`NCBITaxon:34073`, strain TBEA6)
- **Protein Function:** 307-amino-acid metallo-$\beta$-lactamase-fold (`FT DOMAIN 53..274`, `Pfam:PF12706`, `InterPro:IPR011842`, `NCBIfam:TIGR02108`, `PANTHER:PTHR42663:SF7`) non-heme $\text{Fe}^{2+}$-dependent hydroxylase in pyrroloquinoline quinone (PQQ) biosynthesis (`UniProtKB:A0A0H2M8Q2`).

## Resolution of Historical UniProt/HAMAP Annotation Defect
- `UniProtKB:A0A0H2M8Q2` (`HAMAP-Rule:MF_00653`) still carries the legacy comment `CC -!- FUNCTION: May be involved in the transport of PQQ or its precursor to the periplasm.` and keyword `KW Transport`.
- However, biochemical, $^{18}\text{O}_2$-labeling, and crystallographic characterization by Koehn et al. 2019 ([PMID:30811189 Discovery of Hydroxylase Activity for PqqB Provides a Missing Link in the Pyrroloquinoline Quinone Biosynthetic Pathway., "Here we show evidence that the remaining essential biosynthetic enzyme PqqB is an iron-dependent hydroxylase catalyzing oxygen-insertion reactions that are proposed to produce the quinone moiety of the mature PQQ cofactor."]) and reviewed by Zhu & Klinman 2020 ([PMID:32731194 Biogenesis of the peptide-derived redox cofactor pyrroloquinoline quinone., "Detailed kinetic analyses have confirmed that PqqB is a previously unknown iron-dependent hydroxylase, indicating a cross-over between the MBL superfamily and the non-heme iron hydroxylases."]) established that PqqB is a cytosolic non-heme iron-dependent hydroxylase that oxygenates the tyrosine ring of a PqqA-derived cross-linked intermediate to form the hydroxyquinone precursor that cyclizes to AHQQ.
- Sequence inspection of `A0A0H2M8Q2` confirms both the N-terminal structural $\text{Zn}^{2+}$-binding motif (`Cys18-Asn19-Cys20-Pro21-Asn22-Cys23`) and the metallo-$\beta$-lactamase fold (`residues 53–274`).
- Pathway context is modeled in [`MODULE:pqq_biosynthesis`](../../../modules/pqq_biosynthesis.yaml).

## Review of Existing GOA Annotations
- `GO:0018189` (`pyrroloquinoline quinone biosynthetic process`, IEA via `UniProtKB-UniRule:UR000098300`) -> **ACCEPT** (core biological process).

## New Annotations Added
- `GO:0016705` (`oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen`, `ISS` from `PMID:30811189`) — matches `PSEPK/pqqB` and `MODULE:pqq_biosynthesis` (`pqqb_hydroxylase`).
- `GO:0005506` (`iron ion binding`, `ISS` from `PMID:30811189`) — catalytic $\text{Fe}^{2+}$ cofactor required for PqqB hydroxylase activity.
- `GO:0005829` (`cytosol`, `IC`, `located_in`) — soluble 307-residue cytoplasmic enzyme lacking signal peptides or transmembrane helices.
