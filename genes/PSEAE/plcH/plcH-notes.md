# plcH / PA0844 (P06200) review notes

## Summary of the literature

PlcH (PHLC_PSEAE, reviewed) is a 730-residue precursor with a 38-residue signal peptide and a
mature chain 39-730. UniProt: [file:PSEAE/plcH/plcH-uniprot.txt "Hydrolyzes sphingomyelin in
addition to phosphatidylcholine."] and "Predicted to be exported by the Tat system". PANTHER places
it in PTHR31956 (non-specific phospholipase C-related), with the plant NPC enzymes and the
*M. tuberculosis* PlcA-D proteins — the superfamily the 2002 paper names.

Primary data:

1. Stonehouse et al. 2002 [PMID:12410824], abstract read. [PMID:12410824 "In this report we
   describe the 1,500-fold purification and characterization of the haemolytic phospholipase C
   (PLC) of Pseudomonas aeruginosa"]; the enzyme purifies as a 1:1 PlcH-PlcR2 heterodimer;
   [PMID:12410824 "PlcHR2 is only active on choline-containing phospholipids. It is equally
   active on phosphatidylcholine (PC) and sphingomyelin (SM) and is able to hydrolyse
   plasmenylcholine phospholipids (plasmalogens)"]; and on haemolysis, [PMID:12410824 "While
   calcium has no detectable effect on enzymatic activity, it inhibits the haemolytic activity of
   PlcHR2"] — i.e. haemolysis by the purified enzyme was measured.
2. Ostroff, Vasil & Vasil 1990 [PMID:2120196], abstract read: [PMID:2120196 "PLC-H hydrolyzes
   sphingomyelin in addition to phosphatidylcholine"], while PLC-N also acts on
   phosphatidylserine. This is the paper behind the PseudoCAP GO:0016298 lipase row.
3. Luberto et al. 2003 [PMID:12799377], abstract read: SM synthase activity is secreted
   [PMID:12799377 "SM synthase-like activity was found secreted in the culture medium of P.
   aeruginosa"], and [PMID:12799377 "Second, purified PlcH showed SM synthase activity"], lost in
   *plcH* operon knockouts.
4. Voulhoux et al. 2001 [PMID:11726509], abstract read: [PMID:11726509 "two substrates for the
   Pseudomonas aeruginosa secreton, both phospholipases, use the twin-arginine translocation
   (Tat) system"]. PlcH is cargo of the Xcp T2SS.
5. Jackson et al. 2013 [PMID:23667230], **full text cached and read**: [PMID:23667230
   "Pseudomonas aeruginosa hemolytic phospholipase C (PlcH) degrades phosphatidylcholine (PC), an
   abundant lipid in cell membranes and lung surfactant"] and [PMID:23667230 "A ΔplcHR mutant,
   known to be defective in virulence in animal models, was less able to colonize epithelial cell
   monolayers and was defective in biofilm formation on plastic when grown in lung surfactant"].
   PC catabolites choline and glycine betaine activate the Anr regulon. **No haemolysis assay
   appears anywhere in the cached text**, which matters for the GO:0044179 IMP row keyed to it.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001277539 | GO:0004629 C-type glycerophospholipase activity | 9 | 253 (49 taxa) | GO:0034480, IDA, PMID:12410824 (PseudoCAP) | SOUND | Purified, 1,500-fold enriched enzyme, assayed on defined substrates, active only on choline phospholipids. A PC-PLC is by definition a C-type glycerophospholipase, so the node term is a correct generalisation of the seed. | *M. tuberculosis* PlcA/B/C/D (P9WIB5, P9WIB3, P9WIB1, P9WIA9 — IDA GO:0004629 and EXP/IMP GO:0034480) and four Arabidopsis NPC genes (AT2G26870, AT3G48610, AT3G03540, AT3G03530) — UniProt accessions verified by live QuickGO query 2026-11-05 | Yes. Four mycobacterial seeds carry their own IDA/EXP evidence for the same chemistry. **No GO_CENTRAL defect**; the node term fits a clade whose plant members are non-specific PLCs. |
| PTN001277563 | GO:0034480 phosphatidylcholine phospholipase C activity | 5 | 11 (5 taxa) | GO:0034480, IDA, PMID:12410824 (PseudoCAP) | SOUND | Same seed, same direct assay; here the node term is exactly the seed term and the node is small (11 leaf IBAs, 5 taxa) — the bacterial PC-PLC subfamily. | The same four *M. tuberculosis* Plc enzymes, each with EXP GO:0034480 (PMID:20736081) and IMP GO:0034480 (PMID:12100560) | Yes. The IBD would stand on the mycobacterial seeds alone. No GO_CENTRAL defect. |

Both PseudoCAP seed rows are the *same* GOA row (`enables GO:0034480 IDA PMID:12410824`), and it
is sound. The defects filed on this gene concern two other PseudoCAP rows (below).

Consistency with the reviewed PLD genes in this repository: `genes/PSEAE/pldA` and
`genes/PSEAE/PA5089` are D-type phospholipases on a different PANTHER family and share no node
with plcH, so nothing is duplicated there.

## Annotation decisions and defects

- GO:0034480 (IDA, IBA, IEA): ACCEPT. Core function.
- GO:0004629, GO:0016298 (IDA), GO:0016788: TOO_GENERAL — all entailed by GO:0034480.
- GO:0033188 sphingomyelin synthase activity (IDA): **KEEP_AS_NON_CORE**. Real activity of the
  purified protein, genetically tied to *plcH*, but a secreted enzyme does not meet the
  cytoplasmic-leaflet substrate pools of a true SM synthase, and the physiological output is
  hydrolysis. Treated as a genuine secondary activity of the same catalytic machinery
  (`projects/ENZYME_SPECIFICITY.md` tiering), not as noise.
- GO:0015628 protein secretion by the type II secretion system (IDA): MARK_AS_OVER_ANNOTATED
  plus a PSEUDOCAP `WRONG_TERM` defect (PROBABLE). PlcH is Xcp **cargo**; the term belongs to the
  machinery. Identical calls already exist on `genes/PSEAE/lasB` and `genes/PSEAE/lap`, and the
  defect text cross-references them.
- GO:0016042 lipid catabolic process (IEA): MODIFY to GO:0034638 phosphatidylcholine catabolic
  process.
- GO:0044179 hemolysis in another organism: ACCEPT on both rows (consistency), since the claim
  is directly supported by the purified-enzyme haemolysis data. On the **IMP row keyed to
  PMID:23667230** a PSEUDOCAP `WRONG_REFERENCE` defect is filed at PROBABLE: the cached full text
  of that paper reports colonization, biofilm, Anr and mouse-pneumonia phenotypes and no
  haemolysis experiment. Confidence is PROBABLE rather than CONFIRMED because figure panels are
  not captured in the cached extraction.
- NEW GO:0005576 extracellular region (IC): the gene had no cellular component annotation at
  all, and two independent lines agree (activity purified from culture supernatants; Tat signal
  peptide plus Xcp-dependent secretion).
