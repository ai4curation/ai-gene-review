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
  plant/rat/bovine F1 subunits for the CC term). projects/CONSERVED_FUNCTION_RECOVERY/f_type_atp_synthase/node_placement.tsv shows
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

## 2026-11-06 export-panel review

Identity: P52612, Escherichia coli K-12. Frozen local UniProt provides the accession/locus and the independent classification `DR   NCBIfam; TIGR03496; FliI_clade1; 1.`. No direct KT2440 assay is substituted for a Salmonella experiment.

FliI is the ATP-hydrolyzing subunit of the cytoplasmic flagellar type III export apparatus. FliH and FliJ organize its assembly and coupling to the membrane export gate.

Primary PMID21934659 (https://doi.org/10.1038/ncomms1488) examines Salmonella wild-type and FliHI bypass backgrounds: FliJ–FlhA interaction activates efficient export. PMID29946050 (https://doi.org/10.1128/mBio.00988-18) uses Salmonella inverted membrane vesicles, FlhB(N269A) rod/hook-locked preparations and separate wild-type-FlhB hook-length experiments. Added FliHI plus FliJ improves transport; ΔFoF1 vesicles with MgATP still export without bulk PMF. The hydrolysis-defective FliI(E211Q) control loses that activity. Neither result converts FliI into an ATP synthase. The earlier PMID18216858/18216859 bypass observations show ATPase dispensability under particular conditions, not the irrelevance of ATPase-assisted export. Exact native stoichiometry and energetics in KT2440 remain inferred.

GO audit: current QuickGO snapshots in the ignored export-panel cache verify that 0008564 does not descend from 0016887, and 0120102 does not descend from 0030257; preserve those distinct claims. Membrane→plasma membrane and flagellum/basal body→secretion apparatus are genuine refinements. Non-catalytic subunits receive process/location cores rather than invented autonomous ATPase or generic chaperone functions. Motility/chemotaxis consequences of failed export are distinguished from doing the motion/signaling work.

The original detailed PAINT node analysis is retained; `just paint-losses ECOLI fliI` reported no IRD/IKR above the target. Experimental self-interaction rows are accepted as a central assembly property, with incomplete individual interaction-table access explicitly retained; no paper is declared wrong-gene from its abstract. The historical NEW0008564 row payload and NEW action remain unchanged.

Existing provider research was read as context and preserved byte-for-byte. Independent publication/UniProt support replaces reliance on provider assertions wherever the record lacked primary grounding.

Adjudication check: existing GO0071973 motility claims are retained as non-core broad functional participation because same-role FliH/FliJ comparators consistently carry them. Lack of torque production alone is not a sufficient negative argument. Chemotaxis GO0006935 remains UNDECIDED: its definition includes directed locomotion, not only signal transduction, and the available sources do not settle the intended breadth for export factors.


## 2026-11-06 PR6138 round-1 clarification

Retained all three specific self-association ACCEPT decisions and made functional homohexamer formation explicit in the existing catalytic core synthesis. PMID12787361 measures oligomerization and cooperative ATPase activity in Salmonella, not canonical E. coli. The PMID8604139 interaction table remains unverified from its cached abstract; the reference assessment now distinguishes that source limit from independent support for the conserved self-association claim. The entire chemotaxis annotation row is unchanged.

Ontology definitions and ancestor URLs, primary-source scope and reviewer disagreements are recorded in `analysis/module_audits/bacterial_flagellar_assembly_export/round1-consultation.md`.


### Subsequent round-1 chemotaxis adjudication

Following the integration reviewer's evidence-based adjudication, the original GO0006935 NAS row is MARK_AS_OVER_ANNOTATED. PMID31337100 supports export-gate activation and construction but does not establish FliI participation in ongoing propulsion, steering or gradient-dependent motor regulation. Apparatus construction alone is insufficient for this guided-movement claim. This is an evidence-scope judgment, not a demonstration that all possible secondary roles are absent or a restriction of UNDECIDED to inaccessible papers. The exact export quote and complete original payload are preserved; the reference assessment is aligned. This supersedes the preceding note that the chemotaxis row was unchanged during the initial narrower consultation.
