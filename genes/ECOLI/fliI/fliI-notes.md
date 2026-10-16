# fliI (E. coli K-12, P52612, b1941) review notes

## Identity
- UniProt P52612, gene fliI (flaAIII, flaC), b1941/JW1925. RecName "Flagellum-specific ATP synthase", EC 7.1.2.2
  (H+-transporting two-sector ATPase reaction, ProRule-based PRU10106). This name/EC reflects F1-beta homology,
  not function; the appropriate EC for a type III export ATPase is 7.4.2.8. The UniProt FUNCTION comment still
  offers the old alternative "a proton translocase involved in local circuits at the flagellum", for which no
  evidence exists.
- PANTHER PTHR15184:SF81 (FLAGELLUM-SPECIFIC ATP SYNTHASE); InterPro IPR005714 (T3SS FliI/YscN), IPR020005
  (FliI clade 1), IPR000194 (F1/V1/A1 alpha/beta nucleotide-binding domain).

## Direct E. coli K-12 evidence
Very little. GOA experimental rows are three IPI "identical protein binding" rows from yeast two-hybrid screens:
- PMID:24561554 (E. coli binary interactome, Y2H) and PMID:19834901 (Y2H benchmarking; "90 motility-related
  proteins from Escherichia coli were tested in all pairwise combinations") - FliI-FliI self-interaction.
- PMID:8604139 (Marykwas et al. 1996): the abstract describes FliG/FliM/FliN/FliF/H-NS interactions only; the FliI
  self-interaction must be in the full text (not cached). Per project rules, not overruled.
- NAS rows come from the Nakamura & Minamino 2019 review PMID:31337100 ["FliH, FliI and FliJ form the cytoplasmic
  ATPase ring complex with a 12 FliH to 6 FliI to 1 FliJ stoichiometry"; "The FliI6 ring hydrolyzes ATP to
  activate the transmembrane export gate complex, thereby driving H+-coupled flagellar protein export by the
  export gate"]. The review does not claim FliI acts in chemotaxis.
- No purified-P52612 enzymology found (PubMed search FliI + Escherichia coli + ATPase returned Salmonella / EPEC
  EscN papers). Falcon deep research agrees: "No direct 2023-2024 biochemical characterization specifically of
  E. coli K-12 P52612 was identified."

## Ortholog (Salmonella typhimurium FliI, P26465) evidence - flagged as ortholog
- PMID:8491729 (Dreyfus 1993): FliI related to F1 beta; "Site-directed mutagenesis of residues in FliI that
  correspond to catalytically important residues in the F1 beta subunit resulted in loss of flagellation".
- PMID:8943245 (Fan & Macnab 1996): Mg2+-dependent ATPase; "The activity was not affected by inhibitors of the F-,
  V- or P-type ATPases".
- PMID:12054792 (Auvray 2002): FliI/FliH peripheral inner-membrane; FliH2/FliI heterotrimer; phospholipids
  stimulate ATPase.
- PMID:12787361 (Claret 2003): ATP-promoted hexameric ring, positive cooperativity ("oligomerization and enzyme
  activity are coupled"). Supports the FliI-FliI IPI rows biologically.
- PMID:17202259 (Imada 2007): crystal structure; "extensive similarities to the alpha and beta subunits of
  F0F1-ATPsynthase".
- PMID:21278755 (Ibuki 2011): FliJ gamma-like; "FliJ promotes the formation of FliI hexamer rings by binding to
  the center of the ring".
- PMID:18216858 / PMID:18216859: PMF drives export; ATP hydrolysis by FliI is not essential ("the flagellar
  secretion apparatus functions as a proton-driven protein exporter").
- PMID:21934659: "the export gate complex by itself is a proton-protein antiporter".
- PMID:29946050: in vitro reconstitution; "FlhA has an ion channel activity"; "ATP hydrolysis by FliI can drive the
  protein export without bulk PMF".

## ATP synthase-family terms
- GO:0046933 (IBA, contributes_to) and GO:0045259 (IBA, part_of) from PANTHER:PTN008558586. Local PAINT table
  (interpro/panther/PTHR15184/PTHR15184-paint.tsv) shows both IBDs at PTN008558586, seeded only by F1-beta
  proteins (E. coli AtpD P0ABB4, human ATP5F1B P06576, yeast ATP2 S000003882, S. pombe atp2 SPAC222.12c; plus
  plant/rat/bovine F1 subunits for the CC term). projects/TREEGRAFTER/rotary_atpase/node_placement.tsv shows
  PTN008558586 is a DUPLICATION node whose children are PTN000390097 (FliI/SctN clade: SF9, SF62, SF81) and
  PTN008558588 (F1-beta subfamilies). So the IBD sits one node too deep: it spans the FliI/SctN paralog clade,
  none of whose members has any evidence of ATP synthesis or proton transport, and which lacks Fo partners.
  -> REMOVE both; recommend moving the IBD to PTN008558588 (or NOT at PTN000390097).
- GO:0015986 (IEA GO_REF:0000108, inferred from GO:0046933) -> REMOVE with the source.
- FliJ gamma-like / rotary FliI6-FliJ model does not make FliI a proton transporter: the proton flux is through
  the export gate (FlhA) and FliI is a peripheral soluble ATPase.

## Decisions (consistent with CAUVC/fliI)
- ATP binding, ATP hydrolysis activity, cytoplasm, T3SS secretion, T3SS complex, flagellum assembly: ACCEPT.
- bacterial-type flagellum (NAS): MODIFY -> GO:0120102 (also present as its own NAS row, ACCEPT).
- motility: KEEP_AS_NON_CORE (downstream of assembly). chemotaxis: MARK_AS_OVER_ANNOTATED (indirect).
- identical protein binding x3: KEEP_AS_NON_CORE (homohexamer biology real but uninformative MF).
- NEW: GO:0008564 protein-exporting ATPase activity (ISS from Salmonella ortholog).
