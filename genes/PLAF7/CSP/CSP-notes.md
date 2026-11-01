# CSP (Q7K740, PF3D7_0304600) — Plasmodium falciparum 3D7 circumsporozoite protein

**Note on provenance:** automated deep research was unavailable in this environment
(no working provider credentials). These notes are a **manual literature review**
based on the cached UniProt record (`CSP-uniprot.txt`), the cached publications in
`publications/` cited by GOA, and the GO ontology (OLS). No
`*-deep-research-*.md` file was generated.

## Protein overview

- 397 aa precursor; signal peptide 1–18; mature chain 19–374; C-terminal propeptide
  375–397 removed on GPI attachment
  [file:PLAF7/CSP/CSP-uniprot.txt "Removed in mature form"].
- Domain architecture: N-terminal region containing the conserved **region I**
  (KLKQP) proteolytic/cleavage motif, a long **central (NANP)n repeat** region
  (31 four-residue repeats annotated from the cryo-EM study PMID:30324137), and a
  C-terminal **thrombospondin type-1 repeat (TSR)** domain carrying the region II-plus
  adhesive motif (Pfam PF00090; PROSITE PS50092; structures 3VDJ/3VDK/3VDL).
- GPI-anchored surface coat protein of the sporozoite
  [PMID:32150583 "PfCSP is GPI-anchored on the sporozoite surface and plays a critical role in sporozoite development, motility and hepatocyte invasion"].
- UniProt summarises the two-conformation model: the N-terminus masks the TSR in the
  non-adhesive state and is cleaved/removed to expose it for productive invasion
  [file:PLAF7/CSP/CSP-uniprot.txt "The TSP type-1 (TSR) domain is required for sporozoite"].

## Function: adhesion to hepatocyte heparan sulfate proteoglycans

Frevert et al. identified the hepatocyte receptor for CSP region II-plus as heparan
sulfate proteoglycan, and showed the interaction is through the glycosaminoglycan
chains:

- [PMID:8478608 "The remarkable target cell specificity of this parasite may be explained by the presence of receptors for the region II-plus of the circumsporozoite protein (CS) on the basolateral domain of the plasma membrane of hepatocytes. We have now identified these receptors as heparan sulfate proteoglycans (HSPG)."]
- [PMID:8478608 "The binding of CS to the receptors is abolished by heparitinase treatment, indicating that the recognition of region II-plus is via the glycosaminoglycan chains."]
- [PMID:8478608 "They have a molecular weight of 400,000-700,000, are tightly associated with the plasma membrane, and are released from the cell surface by very mild trypsinization"]

This underpins both the MF annotations GO:0043395 (heparan sulfate proteoglycan
binding) and GO:0046812 (host cell surface binding): the ligand is a host-cell-surface
proteoglycan, so both terms describe the same, directly demonstrated binding event from
two complementary angles (chemical identity of the ligand; its host-cell-surface
context). Neither is an over-annotation.

The host-side relationship also motivates the BP term **GO:0044650 adhesion of symbiont
to host cell** ("The attachment of a symbiont to a host cell via adhesion molecules,
general stickiness etc., either directly or indirectly.", OLS): CSP is the adhesin
itself, so it performs the work of the adhesion step rather than merely being required
for it. This term is currently absent from GOA for Q7K740. Comparator check within P. falciparum: RH5
(Q8IFM5) carries GO:0044650 (IEA, propagated from GO:0046789 host cell surface receptor
binding), while AMA1 does not — the term is applied inconsistently to invasion adhesins
rather than systematically withheld.

## Function: sporozoite motility and invasion (region II, region I)

Tewari et al. replaced the endogenous *P. berghei* CSP with PfCSP and with
region-deleted versions:

- [PMID:12244064 "Disruption of region II abolished sporozoite motility and dramatically impaired their ability to invade mosquito salivary glands and infect the vertebrate host."]
- [PMID:12244064 "Region I-deficient sporozoites showed no impairment of motility or infectivity in either vector or vertebrate host."]
- [PMID:12244064 "We show here that P. falciparum circumsporozoite protein functions in rodent parasite and that P. berghei sporozoites carrying the P. falciparum CS gene develop normally, are motile, invade mosquito salivary glands, and infect the vertebrate host."]

Two points follow. (i) The region II (TSR) adhesive motif is required for **gliding
motility** of the sporozoite, a substrate-dependent, adhesin-driven form of cell
motility — matching GO:0071976 cell gliding ("Cell motility that results in the smooth
movement of a cell along a solid surface.", OLS). CSP is a surface adhesin that engages
the substrate during this movement, so it contributes directly; loss of region II
abolishes the motility outright. (ii) The same experiment supports entry into both the
**vector** (salivary gland) and the **vertebrate host**, which is why the broad term
GO:0044409 (symbiont entry into host) carries content that the hepatocyte-specific
GO:0085017 does not entail at the level of the evidence.

Caveat recorded: these experiments were performed on PfCSP expressed in a *P. berghei*
background, not on *P. falciparum* sporozoites directly. That is a legitimate
transgenic-complementation design and the paper explicitly demonstrates PfCSP functions
in the rodent parasite, so it supports annotation of PfCSP.

## Function: hepatocyte invasion / liver infection (antibody-neutralisation genetics)

Both GO:0085017 IMP annotations come from antibody studies:

- [PMID:29554084 "which coats the PfSPZ surface and plays a key role in parasite migration out of the skin, entry into the liver parenchyma and invasion of hepatocytes"]
- [PMID:29554084 "we tested a panel of IgG antibodies in vitro for their capacity to inhibit PfSPZ traversal and invasion of a human hepatocyte cell line"]
- [PMID:29554084 "The increased potency of the dual-specific antibodies could be due to the proximity of the N-terminal junction to region I (KLKQP) of PfCSP, which is involved in the cleavage of the N-terminus to allow PfSPZ invasion of hepatocytes"]
- [PMID:32150583 "Both antibodies are potent, especially at high concentrations (300 and 600 μg/mouse) with >90% reduction in liver burden load as compared to naïve infected mice"]

Passive immunisation / antibody-blockade is a perturbation of the protein's function
and is routinely treated as IMP-like evidence by UniProt curators. The hepatocyte
invasion event forms a parasitophorous vacuole, so GO:0085017 ("entry into host cell by
a symbiont-containing vacuole", OLS) is the correct, parasite-appropriate specific term
— it is not an animal-centric or plant-centric mis-transfer.

Note that PMID:32150583 did its in vivo protection work with transgenic *P. berghei*
sporozoites expressing the PfCSP epitope (chimeric challenge model), so the in vivo
evidence for PfCSP itself is indirect; the in vitro inhibition in PMID:29554084 used
*P. falciparum* sporozoites and human hepatoma cells.

## Localisation

- **Plasma membrane (GO:0005886)** — CSP is the GPI-anchored surface coat of the
  sporozoite [PMID:32150583 "PfCSP is GPI-anchored on the sporozoite surface"];
  UniProt: [file:PLAF7/CSP/CSP-uniprot.txt "Cell membrane {ECO:0000250|UniProtKB:P19597}; Lipid-anchor, GPI-anchor"].
- **Cell surface (GO:0009986)** — correct and well supported for a surface coat
  protein; the InterPro2GO source (IPR003067, circumsporozoite protein) is an
  appropriate mapping for this family.
- **Cytoplasm (GO:0005737)** — the IEA/ISS pair derive from the *P. berghei* ortholog
  P23093, where CSP is cytoplasmic in developing oocysts before redistributing to the
  surface: [file:PLAF7/CSP/CSP-uniprot.txt "Localizes to the cytoplasm and the"]
  (continuing "cell membrane in oocysts at day 6 post infection and then gradually
  distributes over the entire cell surface of the sporoblast and the budding
  sporozoites"). This is a transient biosynthetic/developmental localisation, not the
  functional site of the protein — correct to keep, but non-core.

The IDA plasma-membrane annotation cites PMID:16603573, a GPI-anchored proteome study
that explicitly focuses on the blood stage
[PMID:16603573 "Focusing on the clinically relevant blood stage of the life cycle"] and
whose 11 proteomically validated GPI proteins are merozoite surface proteins, not CSP;
CSP appears via the GPI-HMM prediction. The *conclusion* (CSP is a GPI-anchored plasma
membrane protein) is nevertheless firmly correct from other sources, so this is kept
rather than removed — the per-CLAUDE.md rule is not to overrule a curator's experimental
call from an abstract alone, and in any case the location is right.

## Protist-specific checks performed

- No animal- or plant-specific terms transferred electronically (no e.g. extracellular
  matrix, immune-system, chloroplast/apicoplast mis-assignments).
- No organelle mismatch: the annotated compartments (plasma membrane, cell surface,
  cytoplasm) are all genuine for a GPI-anchored sporozoite coat protein; no apicoplast,
  rhoptry, microneme or digestive-vacuole claim is made (CSP is not a secretory-organelle
  protein — it is surface-displayed, though it transits the secretory pathway).
- Host-vs-symbiont direction correct: GO:0046812 (host cell surface binding),
  GO:0044409, GO:0085017 and proposed GO:0044650 are all symbiont-perspective terms
  applied to a parasite protein acting on the host, which is the intended use.
- No paralog-family over-annotation: CSP is a single-copy, family-defining gene
  (InterPro IPR003067 is CSP-specific); the PANTHER assignment PTHR44826 "SPORE COAT
  PROTEIN SP85" is a loose TSR-domain-driven grouping and contributes no GO annotation
  here.

## Curation decisions (summary)

| Term | Evidence | Action |
|---|---|---|
| GO:0005737 cytoplasm (IEA, ISS) | GO_REF:0000044 / GO_REF:0000024 (P23093) | KEEP_AS_NON_CORE ×2 |
| GO:0005886 plasma membrane (IDA, IEA, ISS) | PMID:16603573 / GO_REF:0000044 / GO_REF:0000024 | ACCEPT ×3 |
| GO:0009986 cell surface (IEA) | GO_REF:0000002, IPR003067 | ACCEPT |
| GO:0043395 heparan sulfate proteoglycan binding (IDA) | PMID:8478608 | ACCEPT |
| GO:0046812 host cell surface binding (IDA) | PMID:8478608 | ACCEPT |
| GO:0044409 symbiont entry into host (IDA) | PMID:12244064 | ACCEPT |
| GO:0085017 entry into host cell by symbiont-containing vacuole (IMP ×2) | PMID:29554084, PMID:32150583 | ACCEPT ×2 |
| GO:0044650 adhesion of symbiont to host cell | PMID:8478608 (+PMID:12244064) | NEW |
| GO:0071976 cell gliding | PMID:12244064 | NEW |

No REMOVE or MODIFY actions were warranted: every existing annotation is biologically
correct for this protein, and the GOA set is unusually clean for a protist entry.
