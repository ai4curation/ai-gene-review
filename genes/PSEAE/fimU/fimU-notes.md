# fimU (PA4550, G3XCZ0) notes

## Identity

- UniProt G3XCZ0, unreviewed (TrEMBL), 168 aa; gene fimU, locus PA4550.
  Recommended name "Type II secretion system protein H" is an ARBA-generated
  name (ECO:0000256|ARBA), not a curated function. Class III signal peptide
  (PROPEP 1..9, PROSITE PRU01070), TM helix 12-30 (Phobius), InterPro
  IPR022346 T2SS_GspH, Pfam PF12019 GspH, PF07963 N_methyl. No PANTHER xref in
  the UniProt entry.
- First gene of the fimU-pilVWXY1Y2E minor pilin operon region; P. aeruginosa
  has its own T2SS GspH (XcpU), so FimU is the type IV pilus paralogue, not
  the Xcp component.

## Literature

- fimU mutants lack fimbriae and twitching; FimT overexpression can replace it
  [PMID:8682785 "Isogenic mutants constructed by allelic exchange demonstrated
  that the fimU gene was required for fimbrial biogenesis and twitching
  motility"; "overexpression of the fimT gene was found to be able to
  functionally replace the lack of a fimU gene product"].
- Minor pilins are processed by PilD and incorporated into pili
  [PMID:20338182 "the minor pilins FimU, PilV, PilW, PilX, and PilE were
  processed by the pre-pilin peptidase PilD and incorporated throughout the
  growing pilus filament"]; FimU promotes assembly [PMID:20338182 "with FimU
  and PilX being implicated as key promoters of pilus assembly on the cell
  surface"].
- FimU is incorporated independently and couples the priming complex to the
  major pilin; crystal structure resembles GspH [PMID:25389296 "FimU is
  incorporated independently of the others and is proposed to couple the
  putative minor pilin-PilY1 complex to the major subunit."; "our 1.4 Å
  crystal structure of FimU revealed striking architectural similarity to its
  T2S ortholog GspH, despite minimal sequence identity"]. The paper also shows
  that Xcp minor pseudopilins can prime T4P assembly, i.e. the T2S proteins
  cross over into T4P, not that FimU acts in T2S.

## PANTHER node PTN008624060

- IBD of GO:0044096 type IV pilus (2026-03-04), WITH UniProtKB:G3XCZ0 only.
- Leaves (7, 6 taxa): P. aeruginosa FimU, Shewanella FimU (Q8EBJ4),
  Xanthomonas FimT x2 (Q8P7W3, Q8P7X0), Neisseria meningitidis Q9JZV4,
  Vibrio VC_0858 (Q9KTP3), Dictyoglomus turgidum Dtur_1183 (B8E2W2, an
  N-methylation-motif protein). All are FimU/FimT-type minor pilins by name or
  domain; type IV pilus as a location suits minor pilins, which are
  incorporated into the fibre.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN008624060 | GO:0044096 type IV pilus | 1 (sole) | 7 (6 taxa) | GO:0044096 type IV pilus, located_in, IDA, PMID:20338182 (PseudoCAP) | SOUND | Antibodies to FimU detect it incorporated throughout sheared pilus fibres; independently confirmed by PMID:25389296. Minor pilins are fibre components, so the term fits the FimU/FimT clade. |

## Decisions summary

- ACCEPT: plasma membrane (IEA); type IV pilus (IBA, IDA); motility (IMP);
  type IV pilus assembly (IMP).
- MODIFY: pilus assembly (IDA) to GO:0043683 type IV pilus assembly.
- REMOVE: type II protein secretion system complex and protein secretion by
  the type II secretion system (IEA from IPR022346 GspH): domain shared with
  T2SS GspH, but FimU is the T4P paralogue; P. aeruginosa has a separate
  Xcp GspH (XcpU).
