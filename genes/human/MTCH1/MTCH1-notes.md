# MTCH1 (Q9NZJ7) — review notes

Journal for the AI review of human MTCH1 (mitochondrial carrier homolog 1; historical name PSAP,
"presenilin-associated protein"). All assertions carry inline provenance.

## 1. What the protein is

- SLC25 (mitochondrial carrier) fold, six predicted TM helices, two SOLCAR repeats
  (UniProt Q9NZJ7: `DR PROSITE; PS50920; SOLCAR; 2.`, `FT TRANSMEM 94..104 / 156..176 / 210..229 /
  255..279 / 323..342 / 372..389`), but resident in the **outer** mitochondrial membrane, not the
  inner membrane where canonical SLC25 carriers sit
  [PMID:12377771 "PSAP is a mitochondrial resident protein sharing homology with mitochondrial carrier protein"].
- PANTHER family PTHR10780 (MITOCHONDRIAL CARRIER HOMOLOG), subfamily PTHR10780:SF3
  (MITOCHONDRIAL CARRIER HOMOLOG 1). MTCH2 is SF20 of the same family.
- Long and short isoforms exist and were both used in the 2026 structural study
  (Q9NZJ7-1 = MTCH1-L, Q9NZJ7-2 = MTCH1-S)
  [PMID:42308315 "MTCH1 (Q9NZJ7-1 [MTCH1-L] and Q9NZJ7-2 [MTCH1-S] for both long and short isoforms, respectively)"].

## 2. The insertase question — three independent lines, all positive for MTCH1

**(a) Guna et al. 2022 (the MTCH2 paper), PMID:36264797.** The rigorous reconstitution
(purified protein in liposomes) was done for **MTCH2**, not MTCH1. For MTCH1 the paper shows a
knockdown genetic interaction only:
[PMID:36264797 "which is also localized to the mitochondrial outer membrane, had an additive effect to loss of MTCH2 on biogenesis of many mitochondrial TAs"]
and then generalises:
[PMID:36264797 "We therefore propose that MTCH1/2 are the founding members of a unique class of membrane protein insertases that exploit the SLC25 transporter fold"].
So the GOA **IDA** on MTCH1 for GO:0032977 sourced to this paper is, strictly, a proposal plus a
depletion phenotype rather than a direct demonstration on MTCH1. The conclusion turned out to be
right, but the evidence code overstates what this particular paper did for MTCH1. Recorded, not
acted on — the curator had the full text and figures S17, and the claim is now independently
confirmed (below).

**(b) Dimogkioka, Elias & Rapaport 2025, J Cell Sci, PMID:40704594** — heterologous complementation
in yeast. This is the paper that makes MTCH1 insertase activity a direct claim about MTCH1 itself:
[PMID:40704594 "Expression of MTCH1 and MTCH2 in yeast cells lacking Mim1, Mim2 or both revealed that MTCH1, but not MTCH2, could compensate for the growth defects upon deleting the MIM complex."]
[PMID:40704594 "These findings indicate that MTCH1, by itself, has insertase activity and is a functional equivalent for the MIM complex, despite the absence of any evolutionary relation between the mammalian and yeast insertases."]
[PMID:40704594 "In summary, our current findings provide clear evidence for the capacity of the mammalian protein MTCH1 to act as an insertase for mitochondrial outer membrane proteins."]

**(c) Stevens et al. 2026, Sci Adv, PMID:42308315** — rescue in human cells, the cleanest
homologous-system test:
[PMID:42308315 "we observed that MTCH1 could partially rescue loss of MTCH2 for several α-helical OM substrates"].

### Is the "MTCH1 but not MTCH2 rescues yeast" result actually awkward?

Less than it looks. The authors themselves attribute the MTCH2 failure to behaviour of MTCH2 **in
yeast**, not to absence of insertase activity: MTCH2 was toxic and mislocalised to the ER —
[PMID:40704594 "The localization of MTCH2 to the ER in cells lacking Mim1 might be interfering with the import machinery on the ER surface or disturbing the lipid bilayer, causing ER disfunction and leading to impaired growth."]
— and even when a chimeric N-terminal MTCH1 segment redirected it to mitochondria it still did not
complement
[PMID:40704594 "However, even upon redistribution to the mitochondria caused by the addition of the MTCH1 N-terminal region, MTCH2 did not manage to complement the absence of Mim1."].
They offer conformational/substrate-recognition differences as the explanation
[PMID:40704594 "Structural prediction analysis revealed that the α-helices of MTCH2 are more tightly packed compared to those of MTCH1, potentially suggesting that MTCH1 has a conformation better suited for integration into the yeast mitochondrial membrane."].

So the correct reading is **not** "MTCH2 is not an insertase". MTCH2 insertase activity is
established by reconstitution with purified protein in liposomes (PMID:36264797) and by the 2026
cryo-EM structure-function work (PMID:42308315), neither of which this yeast assay touches. What
the yeast result adds is a **positive** claim about MTCH1 and a caution that heterologous
complementation reports on compatibility with the host membrane/substrate set as much as on
catalytic capability. Net effect on curation: it strengthens GO:0032977 on MTCH1; it does not
weaken anything on MTCH2.

## 3. The carrier/transporter question

**GOA carries no transporter or carrier GO term on MTCH1** (checked every row of
`MTCH1-goa.tsv`: the MF terms present are GO:0032977 membrane insertase activity ×2 and
GO:0005515 protein binding ×2 — nothing in the transmembrane-transporter branch). That is the
right call and there is nothing to remove.

The carrier claim survives only in (i) the gene/protein **name** ("Mitochondrial carrier homolog 1")
and (ii) the UniProt keyword block, which still lists `Transport` (line 316 of
`MTCH1-uniprot.txt`) alongside the family statement
`CC -!- SIMILARITY: Belongs to the mitochondrial carrier (TC 2.A.29) family.` Both are
family-signature inferences from the SLC25 fold, not observations. No transported substrate has
ever been reported for MTCH1 or MTCH2.

The 2026 structural work argues positively against the transporter reading: the MTCH clade has
**lost** the machinery that makes an SLC25 protein a carrier —
[PMID:42308315 "MTCH insertases are conserved across holozoa and have diverged from the solute carrier 25 transporters."]
— and insertase activity arose from loss of a transmembrane helix that opened a lipid-facing groove
[PMID:42308315 "evolution of its insertase activity required loss of a transmembrane helix, which created a lipid-accessible hydrophilic groove stabilized by its unique, structured C terminus"].
Consistent with this, MTCH1 has only two SOLCAR repeats rather than the canonical three.
The UniProt `Transport` keyword is the one thing worth flagging to UniProt; the GO side is clean.

## 4. The old PSAP literature (1999–2002)

MTCH1 was discovered as a presenilin-1 interactor in a yeast two-hybrid screen and mis-assigned a
PDZ-like domain
[PMID:10551805 "we screened a human brain cDNA library for PS-1-interacting proteins using the yeast two-hybrid system and isolated a novel protein containing a PSD-95/Dlg/ZO-1 (PDZ)-like domain"].
The paper's closing speculation is the sole basis for two NAS annotations still in GOA
(GO:0009966 regulation of signal transduction; GO:0045161 neuronal ion channel clustering)
[PMID:10551805 "These data suggest that PS-1 may associate with a PDZ-like domain-containing protein in vivo and thus may participate in receptor or channel clustering and intracellular signaling events in the brain."].
No PDZ domain is annotated in the current UniProt entry (the only domain-level features are the two
SOLCAR repeats and six TM helices), and the protein is a multi-pass mitochondrial outer-membrane
protein, not a cytosolic scaffold. Both NAS terms are marked REMOVE.

The proapoptotic claim is better grounded but is an overexpression phenotype
[PMID:12377771 "overexpression of PSAP caused apoptotic death"],
[PMID:12377771 "The mitochondrial localization and proapoptotic activity of PSAP suggest that it is an important regulator of apoptosis."].
Independent corroboration that expressing MTCH1 kills cells comes, incidentally, from the 2026
methods section
[PMID:42308315 "For generating lentivirus with any MTCH1-encoding plasmids, the pan-caspase inhibitor Q-VD-OPh (MedChemExpress) was added to a final concentration of 25 μM at the time of transfection and 24 after transfection to enable lentivirus generation by preventing apoptosis."].
So the phenotype is real and reproducible, but no mechanism links it to a defined MTCH1 molecular
activity, and an alternative reading — that perturbing OMM protein biogenesis secondarily triggers
apoptosis — is untested. Kept as non-core rather than removed.

## 5. Paralog discipline (explicitly not imported onto MTCH1)

MTCH2 has recently acquired two further asserted functions. Neither has been tested on MTCH1 and
neither is transferred here:
- MTCH2 promotes BAX/BAK self-assembly and apoptotic pore growth [PMID:42056306, Nat Struct Mol Biol 2026].
- MTCH2 modulates CPT1 activity in adipocytes by direct interaction [PMID:41044057, Nat Commun 2025].
Given that MTCH1 has its own (older, weaker) proapoptotic literature, the temptation to merge the
two apoptosis stories is exactly the failure mode to avoid: the MTCH2/BAX work is a distinct
mechanism at a distinct step and says nothing about MTCH1.

## 6. Decisions

| Term | Action | Why |
|---|---|---|
| GO:0032977 membrane insertase activity (IDA, IMP) | ACCEPT | Core MF; three independent lines (PMID:36264797, PMID:40704594, PMID:42308315) |
| GO:0045040 protein insertion into mitochondrial outer membrane (IDA) | ACCEPT | Core BP |
| GO:7770059 alpha helical protein insertion into MOM (IMP) | ACCEPT | Core BP, more specific and correct |
| GO:0005741 mitochondrial outer membrane (IEA) | ACCEPT | Correct, specific location |
| GO:0005739 mitochondrion (IBA, HTP, IMP) | ACCEPT | Correct but less specific than GO:0005741 |
| GO:0016020 membrane (IBA) | MARK_AS_OVER_ANNOTATED | Uninformative root-level CC |
| GO:0043065 positive regulation of apoptotic process (IBA, IEP) | KEEP_AS_NON_CORE | Overexpression phenotype, no mechanism |
| GO:0005515 protein binding (IPI ×2) | MARK_AS_OVER_ANNOTATED | Project guidance |
| GO:0009966 regulation of signal transduction (NAS) | REMOVE | Speculation built on a PDZ-domain assignment that has not survived |
| GO:0045161 neuronal ion channel clustering (NAS) | REMOVE | Same; no PDZ domain, wrong compartment |
