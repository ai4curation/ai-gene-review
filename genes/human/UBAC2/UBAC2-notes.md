# UBAC2 (UBA domain-containing protein 2) review notes

UniProt: Q8NBM4 (UBAC2_HUMAN), 344 aa precursor. Synonym PHGDHL1, PSEC0110. HGNC:20486.
Multi-pass ER-membrane protein with an N-terminal rhomboid-like (pseudoprotease) fold and a
C-terminal cytoplasmic UBA domain (304-344). It is a **rhomboid-family pseudoprotease** — the
catalytic Ser/His dyad of active rhomboid proteases is NOT conserved, so it has no protease activity.

## Core biology
1. **ERAD membrane component (RHBDD1/UBAC2 machinery).** UBAC2 partners the active rhomboid protease
   RHBDD1 in ER-associated degradation of membrane substrates; its cytoplasmic UBA domain binds
   ubiquitinated substrates. (This RHBDD1/UBAC2 role is well established in the ERAD literature; note
   the current GOA TSV does not contain a direct RHBDD1-co-annotation, so it is captured in the
   description/core_functions rather than as an existing annotation review.)
2. **FAF2/UBXD8 ER receptor.** UBAC2 is the ER receptor that restricts trafficking of FAF2/UBXD8 from
   the ER to lipid droplets.
   [PMID:23297223 "association of UBXD8 with the ER-resident rhomboid pseudoprotease UBAC2 specifically restricts trafficking of UBXD8 to LDs"]
   This is the basis of the IDA ER localization and "protein localization to ER" annotations (MGI,
   PMID:23297223), and the IMP "negative regulation of retrograde protein transport ER to cytosol"
   (PMID:25660456).
3. **ER-phagy receptor.** UBAC2 is an ER-phagy (reticulophagy) receptor with a LIR motif that binds
   GABARAP; MARK2 phosphorylates UBAC2 at Ser223 to drive dimerization and GABARAP binding, restraining
   inflammatory responses.
   [PMID:39284914 "we identified ubiquitin-associated domain-containing protein 2 (UBAC2) as a receptor for ER-phagy, while at the same time being a negative regulator of inflammatory responses. UBAC2 harbors a canonical LC3-interacting region (LIR) in its cytoplasmic domain, which binds to autophagosomal GABARAP"]
4. **Wnt regulation.** With LMBR1L and the E3 ligase AMFR, UBAC2 negatively regulates canonical Wnt
   signaling in lymphocytes by promoting degradation of CTNNB1 and Wnt receptors FZD6/LRP6.
   [PMID:31073040 "(UBAC2) attenuated Wnt signaling in lymphocytes by preventing the maturation of"]

## Annotation assessment summary
- **serine-type endopeptidase activity (GO:0004252) IBA**: UBAC2 is a rhomboid **pseudoprotease** lacking
  the catalytic dyad; this IBA is an over-propagation from the active-rhomboid branch of the PANTHER tree
  and is biologically incorrect → REMOVE (IEA/IBA over-propagation, refutable on biological grounds).
- ER membrane (GO:0005789 IEA) / ER (GO:0005783 IDA): core compartment → ACCEPT.
- protein localization to ER (GO:0070972) / negative regulation of retrograde protein transport ER to
  cytosol (GO:1904153): reflect the FAF2/UBXD8 ER-receptor role → ACCEPT.
- reticulophagy (GO:0061709) / negative regulation of inflammatory response (GO:0050728) IMP: ER-phagy
  receptor role → ACCEPT.
- negative regulation of canonical Wnt (GO:0090090) IMP/IEA: LMBR1L/AMFR Wnt role → ACCEPT (non-core
  relative to ERAD/ER-phagy, but experimentally supported).
- protein binding (GO:0005515) IPI: uninformative term → KEEP_AS_NON_CORE.
