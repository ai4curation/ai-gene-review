# TLR1 (human, Q15399) review notes

Sources: UniProt Q15399, GOA (80 seeded rows; the GOA tsv has 81 lines, two IDA
GO:0035354 rows from PMID:16880211 collapse into one), cached publications, and
`TLR1-deep-research-falcon.md` (Falcon, completed during this review; consistent with
the primary literature below and used only as background).

## Core biology

- TLR1 is the triacyl-lipopeptide-selecting partner of TLR2. Structure:
  [PMID:17889651 "the two ester-bound lipid chains are inserted into a pocket in TLR2, while the amide-bound lipid chain is inserted into a hydrophobic channel in TLR1"];
  [PMID:17889651 "Binding of the tri-acylated lipopeptide, Pam(3)CSK(4), induced the formation of an \"m\" shaped heterodimer of the TLR1 and TLR2 ectodomains"].
- Partner choice sets TLR2 specificity: [PMID:19931471 "Its ligand specificity is controlled by whether it heterodimerizes with TLR1 or TLR6"].
- Genetic requirement (mouse): [PMID:12077222 "Macrophages from TLR1-deficient (TLR1(-/-)) mice showed impaired proinflammatory cytokine production in response to the 19-kDa lipoprotein and a synthetic triacylated lipopeptide"].
- Cell surface heterodimer, raft recruitment, Golgi trafficking:
  [PMID:16880211 "Our data show that TLR2 forms heterodimers with TLR1 and TLR6 and that these heterodimer pre-exist and are not induced by the ligand"];
  [PMID:16880211 "Activation occurs at the cell surface, and the observed trafficking is independent of signaling"].
- TIR domain: [PMID:11081518 "Here we report the crystal structures of the TIR domains of human TLR1 and TLR2"]; TLR1 BB-loop mutants reduce signaling [PMID:16893894 "in vitro functional studies involving TLR1 G676A and TLR1 G676L resulted in reduced PAM(3)CSK(4) mediated NF-kappaB activation"].
- Phagosome recruitment: [PMID:11095740 "Finally, we show that TLR6, TLR2, and TLR1 are recruited to macrophage phagosomes"].

## Key curation decisions

1. GO:0001875 lipopolysaccharide immune receptor activity (IDA, contributes_to,
   PMID:16880211) -> MODIFY to GO:0038187 pattern recognition receptor activity.
   The definition requires combining with LPS; TLR1:TLR2 binds triacyl lipopeptide.
   The same term is used in GO-CAM 5fb9cc0600000727 (TLR1-TLR2 complex); flagged as a
   suggested question rather than edited.
2. GO:0031663 LPS-mediated signaling pathway (IEA, GO_REF:0000108, inferred from the
   GO:0001875 row) -> REMOVE; it is an artefact of the mis-fitting MF term.
3. protein binding rows: TLR2 partners -> MODIFY to GO:0035663 Toll-like receptor 2
   binding; TLR10 (co-IP, PMID:15728506) -> MODIFY to GO:0035325 Toll-like receptor
   binding; isolated-TMD (E. coli ToxR) partners TLR6/TLR10 and BioPlex TLR6 -> REMOVE.
4. Cytokine-production regulation terms (IL-6, IL-8, TNF; ISS/IEA/IGI) and positive
   regulation of TLR2 signaling (IGI, PMID:22198949) -> KEEP_AS_NON_CORE (downstream
   outcomes / co-receptor role). Microglial cell activation (rat IEA) and macrophage
   activation (NAS citing an IFN-induction expression paper) -> MARK_AS_OVER_ANNOTATED.
5. Core functions: contributes_to GO:0038187 in GO:0035354 at the plasma membrane,
   directly in GO:0038123 and GO:0042495; plus GO:0042497 triacyl lipopeptide binding
   (structure-based; recorded as a core function, not as a NEW annotation, since
   GO:0071723 lipopeptide binding is already accepted).

## Relevance to project questions

- There is no TLR-specific MF term; the existing TLR1 MF annotation borrowed the LPS
  term. GO:0038187 is the right existing term; a lipopeptide immune receptor term
  would be the parallel to GO:0001875 if GO wants ligand-specific MF.
