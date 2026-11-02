# yjjW (P39409, b4379, YJJW_ECOLI) notes

Deep research was unavailable for this gene (falcon returns 403; asta gave nothing
useful in Phase 1 of the RADICAL_SAM project). Notes built from UniProt, cached primary
papers, PubMed and the shared genome-context analysis
(`genes/ECOLI/pflC/pflC-bioinformatics/RESULTS.md`).

## Identity and family

- 287 aa radical SAM protein, "Putative glycyl-radical enzyme activating enzyme YjjW",
  EC 1.97.1.- {ECO:0000250|UniProtKB:P0A9N4} [file:ECOLI/yjjW/yjjW-uniprot.txt]. PE level 1
  (protein existence at protein level, from the interactome study). Its own NCBIfam family
  is TIGR04041 "YjjW family glycine radical enzyme activase", distinct from the PFLE_PFLC
  family of PflC/YbiY; PANTHER PTHR30352:SF13.
- Unlike PflC/YbiY, UniProt already uses the generic reaction RHEA:61976 (glycyl-[protein])
  and EC 1.97.1.-, not the PFL-specific EC 1.97.1.4. It has two 4Fe-4S ferredoxin-type
  domains and is modelled as binding up to three [4Fe-4S] clusters
  [file:ECOLI/yjjW/yjjW-uniprot.txt "May bind up to 3 [4Fe-4S] clusters"].
- TIGR04041 text: members "are paired with and appear to activate a glycyl radical enzyme
  of unknown function, designated YjjI ... Members of this family may be misannotated as
  pyruvate formate lyase activating enzyme" [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md].

## Partner GRE: YjjI (P37342), a GRE-family protein of unknown function

- yjjW overlaps the 3' end of yjjI by 29 bp, same strand
  [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md]. This is the canonical GRE+activase
  arrangement.
- YjjI (UniProt P37342, 516 aa) is "Uncharacterized protein YjjI"; InterPro IPR016905
  "Glycyl radical enzyme YjjI-like", Pfam PF11230 YjjI-like. It carries an internal
  Gly-loop motif RVTGY (Gly 465), not C-terminal as in classic GREs
  [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md]. YjjI has been noted as a PflB homolog
  but specialised away from PFL (EcoliWiki). Its substrate and reaction are unknown.
- YjjW is only 24-33% identical to any other E. coli activase, and is not closer to PflC
  (24.4%) than to PflA (32.5%). YjjI is ~26-28% identical to all E. coli GREs
  [file:ECOLI/pflC/pflC-bioinformatics/RESULTS.md].

## Protein-binding IPI rows (PMID:24561554)

Three binary Y2H interactions from the proteome-scale E. coli interactome: dpiA (P0AEF4,
a response regulator), galE (P09147, UDP-glucose 4-epimerase), minC (P18196, cell-division
inhibitor). None is a GRE or has any functional link to radical chemistry or
anhydro-sugar metabolism; these look like typical high-throughput Y2H noise. Per Phase 1
convention, generic protein binding (GO:0005515) is REMOVE as uninformative. Removing the
annotation does not assert the interactions are false.

## Assessment

GO:0043364 (general glycyl-radical enzyme activase) is supported by family placement (IBA
and ISS), intact radical SAM motifs, and the yjjW-yjjI coupling. No activity of YjjW has
been shown and the substrate GRE (YjjI) is itself uncharacterised, so I used the
"catalysis not established" branch: GO:0051539 KEEP_AS_NON_CORE, GO:0003824/GO:0016491
MODIFY to GO:0043364, and no SAM-binding NEW row. UniProt already avoids the PFL-specific
EC here, so there is no GO:0043365 over-annotation to correct (unlike pflC/ybiY). The three
protein-binding rows are REMOVE. At time of writing, genes/ECOLI/pflA was still
INITIALIZED, so terms were not aligned with it.
