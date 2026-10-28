# oprB (PA3186, Q51485) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol)

Fetched with `just fetch-gene PSEAE oprB`. Accession Q51485 matches the worklist
(rank 81). Swiss-Prot reviewed entry PORB_PSEAE (PE 1). No deep-research
provider was used.

### Identity and literature

- OprB (outer membrane protein D1, glucose porin) is the glucose-inducible,
  carbohydrate-selective outer-membrane porin; Pfam PF04966 OprB, InterPro
  IPR007049 Carb-sel_porin_OprB, TCDB 1.B.19.1.1, PANTHER PTHR37944 "PORIN B".
  Signal peptide 1-31 confirmed by N-terminal sequencing (UniProt, PMID:8132494).
- Wylie and Worobec 1995 (PMID:7768797; abstract only in the cache; the PubMed
  MCP returned no full text for PMC176988):
  - [PMID:7768797 "Using interposon mutagenesis, we have generated strains of
    Pseudomonas aeruginosa which lack or overexpress the substrate-selective OprB
    porin of this species."]
  - [PMID:7768797 "A marked decrease or increase in the initial uptake of glucose
    by these strains verified the role of OprB in facilitating the diffusion of
    glucose across the outer membrane of P. aeruginosa."]
  - [PMID:7768797 "the loss or overexpression of OprB had a similar effect on the
    uptake of three other sugars able to support the growth of this bacterium
    (mannitol, glycerol, and fructose). This effect was restricted to
    carbohydrate transport; arginine uptake was identical in mutant and
    wild-type strains."]
- UniProt curated function [file:PSEAE/oprB/oprB-uniprot.txt "Involved in the
  transport of glucose, mannitol, fructose and glycerol (sugars able to support
  the growth of P.aeruginosa). Facilitates glucose diffusion across the outer
  membrane."]. UniProt also cites liposome channel specificity work (Trias et al.
  1988, PMID:2450582) and biophysical characterisation (PMID:8132494), neither
  cached.

Evidence type: whole-cell initial uptake in mutant and overexpression strains.
This is IMP, not IDA, though the claim (OprB conducts sugars across the outer
membrane) is sound and OprB does the transport work as the channel.

### Clade check for PTN002209977 (cached PAINT leaf GAF; QuickGO 2026-10-28)

10 leaves in 5 taxa: OprB (Q51485) and PAO1 paralogs PA2291 ("probable
glucose-sensitive porin") and PA4099; Bradyrhizobium bll2003, blr2272, blr3947,
blr8037; Synechocystis slr1163; Xanthomonas campestris RpfN; Rhodopirellula
RB9508 ("carbohydrate-selective porin OprB"). QuickGO shows no experimental
annotations for any leaf other than OprB. All belong to the OprB
carbohydrate-selective porin family, so a carbohydrate transport node term is
a reasonable family-level claim.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002209977 | GO:0008643 carbohydrate transport | 1 (sole) | 10 (5 taxa) | GO:0008643, IDA, PMID:7768797 (PseudoCAP) | SOUND | Uptake of glucose, mannitol, fructose and glycerol (not arginine) tracks OprB loss and overexpression; OprB is the channel. Evidence is better coded IMP. The node term is a general family-level property of OprB-family carbohydrate-selective porins and suits this small clade. |

Defects filed: PSEUDOCAP WRONG_EVIDENCE_CODE (IDA -> IMP, CHECK) on the
experimental row. No GO_CENTRAL defect.

## Decisions summary

- ACCEPT: cell outer membrane (IEA), porin activity (IEA).
- MODIFY: carbohydrate transport (IBA, IDA, IEA) and transmembrane transport
  (IEA) -> D-glucose, mannitol, fructose and glycerol transmembrane transport;
  membrane -> cell outer membrane.
