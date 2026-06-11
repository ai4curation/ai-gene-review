# ERLIN1 (SPFH1 / ER lipid raft-associated protein 1) review notes

UniProt: O75477 (ERLN1_HUMAN), 348 aa. Synonyms SPFH1, KE04, C10orf69. HGNC:16947.
Single-pass type II ER membrane protein with an SPFH/prohibitin (band 7) domain in the ER lumen.
Belongs to the band 7/mec-2 (prohibitin/stomatin/flotillin) family. Associates with lipid-raft-like
ER membrane domains. Disease: autosomal recessive spastic paraplegia SPG62 (variant G50V).

## Core biology
1. **ERLIN1/ERLIN2 complex mediating ERAD of IP3 receptors.** ERLIN1 (SPFH1) and ERLIN2 (SPFH2) form a
   heteromeric ~2 MDa ring-shaped complex that binds IP3R tetramers and mediates their ERAD with the E3
   ligase RNF170.
   [PMID:19240031 "the ER membrane protein SPFH1 and its homolog SPFH2 form a heteromeric approximately 2 MDa complex that binds to IP(3)R tetramers"]
   [PMID:19240031 "RNA interference-mediated depletion of SPFH1 and SPFH2 blocks IP(3)R"]
   ComplexPortal CPX-7121 "ERLIN1-ERLIN2 complex". In complex with ERLIN2, interacts with RNF170.
2. **Cholesterol binding / SREBP regulation.** Erlins bind cholesterol cooperatively and restrict SREBP
   activation, promoting ER retention of the SCAP-SREBP-Insig complex; they regulate cellular cholesterol
   homeostasis and cholesterol/fatty-acid biosynthesis.
   [PMID:24217618 "Erlins bound cholesterol with specificity and strong cooperativity"]
   [PMID:24217618 "define erlins as novel cholesterol-binding proteins that are directly involved in regulating the SREBP machinery"]
   [PMID:24217618 "promote stability of the SREBP-Scap-Insig complex"]
3. **Sterol-accelerated HMGCR ERAD (gp78/AMFR module).** ERLIN1 interacts with the gp78/AMFR and
   SYVN1/HRD1 ER ubiquitin ligases; SPFH2/TMUB1 link gp78 to sterol-accelerated ERAD of HMG-CoA reductase.
   [PMID:21343306 "we identify two ER membrane proteins, SPFH2 and TMUB1, as associated proteins of mammalian gp78"]
4. **Lipid-raft ER domains.** Erlin-1/2 are prohibitin-family proteins that define lipid-raft-like domains
   of the ER.
   [PMID:16835267 "Erlin-1 and erlin-2 are novel members of the prohibitin family of proteins that define lipid-raft-like domains of the ER"]
5. **USP25/cholesterol/virus.** USP25 deubiquitinates and stabilizes ERLIN1; Usp25-Erlin1/2 activity
   limits cholesterol flux to restrict virus infection (PMID:37683630, not cached — referenced via UniProt).

## Annotation assessment summary
- ER membrane (GO:0005789) / ER (GO:0005783): core compartment → ACCEPT (many redundant Reactome TAS CFTR/CD274
  ERAD-machinery annotations → ACCEPT as correct compartment but non-core specifics).
- ERLIN1/2 complex / ERAD of IP3R (GO:0036503 ERAD pathway IDA): core → ACCEPT.
- cholesterol binding (GO:0015485 IDA): core MF → ACCEPT.
- SREBP signaling (GO:0032933), regulation/negative regulation of cholesterol biosynthesis (GO:0045540/45541),
  negative regulation of fatty acid biosynthesis (GO:0045717): SREBP/sterol role → ACCEPT.
- membrane raft (GO:0045121 NAS): lipid-raft ER domains → ACCEPT (non-core).
- ubiquitin protein ligase binding (GO:0031625 IEA InterPro): consistent with AMFR/SYVN1/RNF170 E3 interactions → ACCEPT (informative).
- protein-containing complex (GO:0032991): generic → KEEP_AS_NON_CORE.
- protein binding (GO:0005515) IPI: uninformative → KEEP_AS_NON_CORE.
- Do NOT over-claim catalytic MF: ERLIN1 is a scaffold/lipid-binding SPFH protein, not an enzyme.
