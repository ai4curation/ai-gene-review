# SLC26A4 (Pendrin, O43511) curation notes

## Gene identity and family
- HGNC: SLC26A4 (synonym PDS). UniProt O43511, 780 aa, PE1 (evidence at protein level).
- Belongs to the SLC26A/SulP transporter family (TC 2.A.53); SulP fold with C-terminal
  STAS domain (residues 535-729). [file:human/SLC26A4/SLC26A4-uniprot.txt "Belongs to the SLC26A/SulP transporter (TC 2.A.53) family."]
- InterPro: IPR001902 SLC26A/SulP_fam, IPR011547 SLC26A/SulP_dom, IPR018045 S04_transporter_CS, IPR002645 STAS_dom. PANTHER PTHR11814 (SULFATE TRANSPORTER).

## Molecular function — electroneutral anion exchanger
- Sodium-independent transporter of chloride and iodide. [file:human/SLC26A4/SLC26A4-uniprot.txt "Sodium-independent transporter of chloride and iodide"]
- Mediates electroneutral 1:1 exchange: Cl-/HCO3-, Cl-/I-, Cl-/formate (UniProt CATALYTIC ACTIVITY: Rhea:29823 chloride, 66324 iodide, 72363 Cl/HCO3, 72379 I/Cl, 72267 formate/Cl).
- Cl-/formate exchange shown in Xenopus oocytes [PMID:10644529, UniProt FT]. Cl-/I- mechanism [PMID:15155570].
- IQGAP1 interaction (kidney) enhances Cl-/HCO3- exchange activity.
  [file:human/SLC26A4/SLC26A4-uniprot.txt "Interacts with IQGAP1"]
  [PMID:35601831 "enhanced Cl-/HCO3 - exchanger activity"]

### NOT a sulfate transporter (key point)
- The original cloning paper proposed pendrin as a "putative sulphate transporter" purely on
  homology [PMID:9398842 "closely related to a number of known sulphate transporters"].
- This hypothesis was directly refuted: pendrin expressed in Xenopus oocytes and Sf9 cells
  showed NO sulfate transport, only chloride and iodide.
  [PMID:10192399 "chloride and iodide, but not sulfate"]
- Consequence: all sulfate annotations on SLC26A4 (GO:0008271 IEA/InterPro, GO:0015116 IBA+TAS,
  GO:1902358 IBA+IEA+TAS) are REMOVE. In the PANTHER family review PTHR11814, the sulfate IBD
  nodes (PTN000212046, PTN000929279) are the opisthokont SulP clade where sulfate is ancestral;
  pendrin sits in the metazoan Cl/HCO3 exchanger branch (PTN000929177) that lost sulfate cargo.
  PAINT has NOT yet recorded an IRD/IKR loss on the pendrin lineage (`just paint-losses human
  SLC26A4` → none), and the family review assessed those nodes SOUND without a pendrin
  member_exception. UPSTREAM FOLLOW-UP: a member_exception for O43511 on GO:0015116/GO:1902358
  (and the metazoan exchanger subfamily generally) should be added to the PTHR11814 family
  review so the gene-level REMOVE agrees with it. (I cannot edit that file in this task scope.)

## Subcellular localization — apical plasma membrane
- Apical cell membrane, multi-pass. [file:human/SLC26A4/SLC26A4-uniprot.txt "Apical cell membrane"]
- Kidney: apical surface of non-A (type B / non-A,non-B) intercalated cells of the cortical
  collecting duct. [PMID:11274445 "Labeling was detected on the apical surface of a subpopulation of cells"]
  [PMID:16928804 "in conjunction with apical pendrin and apical RhCG"]
- Thyroid: apical membrane of follicular cells.
  [PMID:12107249 "expressed in the apical membrane of thyroid follicular"]
  [PMID:11932316 "localizes to the apical membrane of thyroid follicular cells"]
- IQGAP1 co-localizes apically. [PMID:35601831 "co-localizes with pendrin on the apical membrane of B-intercalated cells"]
- Detected in urinary exosomes by proteomics [PMID:19056867, PMID:21082674] — expected shed
  apical membrane protein; peripheral (KEEP_AS_NON_CORE).
- Brush border membrane (GO:0031526, ISS from mouse Q9R155): pendrin's apical location in
  intercalated cells / thyroid follicular cells is not a microvillar brush border (that is a
  proximal-tubule/intestinal structure, where pendrin is not expressed). Treated as
  MARK_AS_OVER_ANNOTATED; apical plasma membrane is the supported term.

## Biological roles (tissue physiology)
- **Thyroid**: apical iodide efflux into the follicle lumen, supplying I- for thyroid hormone
  synthesis. [PMID:12107249 "pendrin is an iodide-specific transporter" / "responsible for iodide efflux in the thyroid"]
  [PMID:11932316 "is thought to enable efflux iodide into the follicle lumen"]
  PDS missense mutants mislocalize (ER-retained) and lose iodide efflux [PMID:11932316
  "The results indicated loss of pendrin iodide"]. R776C retains iodide transport
  [PMID:16684826 "retained its ability to transport iodide in vitro"].
  Participation test for GO:0006590 thyroid hormone generation: pendrin supplies the I-
  substrate to the lumen but performs NO step of hormone (thyroglobulin iodination/coupling)
  synthesis — TPO/DUOX/TG do that chemistry. Pendrin is the Cl-/I- antiporter upstream. It is
  not a scaffold/cofactor/chemistry participant in hormonogenesis itself. GO:0006590 is NOT
  annotated in GOA and should NOT be proposed (fails participation). Iodide transport MF/BP are
  the correct core claims.
- **Kidney**: apical Cl-/HCO3- exchange in B-intercalated cells → renal bicarbonate secretion,
  chloride reabsorption, acid-base and blood-pressure regulation.
  [PMID:11274445 "pendrin is an apical anion transporter in" / "has an essential role in renal bicarbonate"]
  Pds-KO tubules fail to secrete bicarbonate [PMID:11274445 "tubules from alkali-loaded
  Pds-knockout mice failed to secrete bicarbonate"]. Supports a NEW GO:0015701 bicarbonate
  transport row (pendrin directly performs the HCO3- transport step) and GO:0006885 regulation
  of pH (non-core physiological output).
- **Inner ear**: endolymph ion/pH homeostasis required for hearing; loss → sensorineural
  deafness. GO:0007605 sensory perception of sound (TAS) — pendrin provides the required ionic
  milieu but does not transduce sound → KEEP_AS_NON_CORE (necessity, not participation in
  transduction).

## Disease
- Pendred syndrome (PDS, MIM:274600): autosomal recessive sensorineural deafness + goiter +
  enlarged vestibular aqueduct. DFNB4 (MIM:600791): nonsyndromic recessive deafness with EVA.
  [file:human/SLC26A4/SLC26A4-uniprot.txt DISEASE]. SLC26A4 testing in EVA [PMID:24051746].

## Action summary rationale
- CORE MF: GO:0140900 chloride:bicarbonate antiporter activity; GO:0015108 chloride TMT
  activity; GO:0015111 iodide TMT activity. All ACCEPT (IDA/IMP/IBA/TAS converge).
- CORE location: GO:0016324 apical plasma membrane (ACCEPT); GO:0005886 plasma membrane (ACCEPT).
- REMOVE: GO:0005515 protein binding (uninformative; IQGAP1 interaction kept as reason/MF
  antiporter enhancement); all sulfate terms (disproven, see above).
- TOO_GENERAL: GO:0016020 membrane, GO:0055085 transmembrane transport, GO:0015698 inorganic
  anion transport (all entailed by asserted specific terms).
- KEEP_AS_NON_CORE: regulation of pH, sensory perception of sound, oxalate transport/activity,
  extracellular exosome.
- UNDECIDED: GO:0032880 regulation of protein localization (ISS from mouse; basis not verifiable,
  not a characterized pendrin function).
- NEW: GO:0015701 bicarbonate transport (IDA, Royaux 2001 renal HCO3- secretion).

## Oxalate note
- GO:0019531 oxalate TMT activity (IBA, node PTN000929177) / GO:0019532 oxalate transport (IEA):
  the metazoan exchanger node is assessed SOUND in the family review (oxalate documented for
  SLC26A2/A6/A7). Pendrin is in that clade but oxalate transport is not among its experimentally
  characterized substrates (Cl/I/HCO3/formate). No target-specific disproof as for sulfate →
  KEEP_AS_NON_CORE (respect IBA node placement; not a core pendrin activity).
