# GCDH (Q92947) review notes

Deep research (`GCDH-deep-research-falcon.md`) did NOT appear within the 8-minute poll window,
so this review is grounded in the UniProt record (`GCDH-uniprot.txt`), the seeded GOA
(`GCDH-goa.tsv`), the cached Reactome entry, and cached publications. No deep-research file
was fabricated.

## Verified core biology

- GCDH is the mitochondrial-matrix, FAD-dependent **glutaryl-CoA dehydrogenase** (EC 1.3.8.6),
  a member of the acyl-CoA dehydrogenase family. It catalyses the **oxidative decarboxylation
  of glutaryl-CoA to crotonyl-CoA + CO2**, transferring electrons via FAD to the
  electron-transfer flavoprotein (ETF → ETFDH → respiratory chain).
  [file:UniProt FUNCTION: "Catalyzes the oxidative decarboxylation of glutaryl-CoA to crotonyl-CoA and CO(2) in the degradative pathway of L-lysine, L-hydroxylysine, and L-tryptophan metabolism. It uses electron transfer flavoprotein as its electron acceptor."]
- Acts in the **degradative pathway of L-lysine, L-hydroxylysine and L-tryptophan** metabolism.
  UniProt PATHWAY: lysine degradation; tryptophan metabolism.
- **Homotetramer**, mitochondrion matrix. Precursor with a 44-residue N-terminal mitochondrial
  transit peptide cleaved on import (mature chain 45-438). [UniProt SUBUNIT/SUBCELLULAR LOCATION;
  Reactome R-HSA-71046]
- Isoform Short (Q92947-2) is **inactive** (alternative C-terminus replacing the FAD/substrate
  C-terminal helix region). [PMID:8541831 abstract; UniProt]
- Deficiency causes **glutaric aciduria type 1 (GA1, MIM:231670)** — progressive dystonia/
  athetosis, striatal (basal ganglia) degeneration, macrocephaly, encephalopathic crises.
  Extensive GA1 missense variant catalogue in UniProt.

## Evidence for specific annotations

- **GO:0004361 glutaryl-CoA dehydrogenase activity** (IDA PMID:8541831, IBA, IEA): core MF.
  Cloned/expressed human enzyme with kinetic constants; disease mutant <1% activity. ACCEPT.
- **GO:0050660 FAD binding** (IBA/IEA): cofactor is FAD; multiple FAD-binding residues in
  UniProt features; crystal structures 1SIQ etc. with FAD. ACCEPT.
- **GO:0005759 mitochondrial matrix** (TAS Reactome, IEA): matrix localization. ACCEPT.
- **GO:0005739 mitochondrion** (IDA PMID:37198486, IDA HPA, HTP PMID:34800366, TAS): ACCEPT.
- **GO:0019477 L-lysine catabolic process** (IMP PMID:37198486, IEA): core BP.
  PMID:37198486 shows GCDH is the crotonyl-CoA-producing enzyme in lysine catabolism; GCDH
  depletion abolishes lysine-induced crotonylation. ACCEPT.
- **GO:0005634 nucleus** (IDA PMID:37198486): a moonlighting/context-specific pool.
  "GCDH most frequently co-localized with the mitochondrial marker COX IV, but >20% of total
  GCDH localized to nuclei in GSCs" — nuclear GCDH-CBP complex crotonylates histones. This is a
  cancer-cell (glioblastoma stem cell) context, not the canonical mitochondrial-matrix function.
  KEEP_AS_NON_CORE.
- **GO:0033539 fatty acid beta-oxidation using acyl-CoA dehydrogenase** (IDA PMID:25416781, IBA):
  MISLEADING for GCDH. GCDH acts in amino-acid (lysine/Trp) catabolism, NOT fatty-acid
  beta-oxidation. PMID:25416781 (METTL20/ETFβ) only uses GCDH as an ETFβ electron-acceptor test
  case ("reduced its ability to receive electrons from the medium chain acyl-CoA dehydrogenase
  and the glutaryl-CoA dehydrogenase"); it does not assay GCDH in fatty-acid beta-oxidation.
  This is family-level over-propagation. MARK_AS_OVER_ANNOTATED (IDA; do not REMOVE experimental)
  and REMOVE for the IBA (electronic phylo inference on a clearly wrong branch for GCDH).
- **GO:0000062 fatty-acyl-CoA binding** (IBA/IEA): GCDH binds glutaryl-CoA (a dicarboxylyl-CoA),
  not a fatty-acyl-CoA. Family-level term; loosely defensible as CoA-thioester binding but
  imprecise. MARK_AS_OVER_ANNOTATED.
- **GO:0046949 fatty-acyl-CoA biosynthetic process** (IBA/IEA): WRONG — GCDH is catabolic
  (produces crotonyl-CoA by decarboxylation) and does not biosynthesise fatty-acyl-CoA. The
  product crotonyl-CoA is a short-chain enoyl-CoA, not a fatty-acyl-CoA, and the direction is
  catabolic. REMOVE the IEA; MARK_AS_OVER_ANNOTATED the IBA (defer to phylo review, but flag).
- **GO:0003995 acyl-CoA dehydrogenase activity** (IEA): parent/family MF, correct but less
  precise than GO:0004361. MODIFY → GO:0004361.
- **GO:0016627 oxidoreductase activity, acting on the CH-CH group of donors** (IEA InterPro):
  correct broad parent of the dehydrogenase activity. ACCEPT (broad IEA OK).
- **GO:0006637 acyl-CoA metabolic process** (IEA): broad but correct (glutaryl-CoA is an
  acyl-CoA). ACCEPT as non-core / broad.
- **GO:0009063 amino acid catabolic process** (IEA): correct broad parent (lysine/Trp
  catabolism). ACCEPT.
- **GO:0019395 fatty acid oxidation** (IEA): WRONG branch — GCDH is amino-acid catabolism, not
  fatty-acid oxidation. Electronic Ensembl-ortholog transfer of a family-level term. REMOVE.

## Notes on references
- PMID:25416781 title/abstract are about METTL20/ETFβ; it is genuinely relevant to GCDH only as
  showing GCDH donates electrons to ETFβ. It does NOT support the fatty-acid beta-oxidation term.
- PMID:34800366 is a large mitochondrial-proteome dataset (HTP); GCDH identity is in supplementary
  data, consistent with mitochondrial localization.
