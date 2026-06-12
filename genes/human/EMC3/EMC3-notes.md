# EMC3 (human, Q9P0I2) review notes

## Identity / architecture
- EMC3 = ER membrane protein complex subunit 3 (synonym TMEM111). 261 aa, multi-pass ER membrane protein with 3 TM helices (TM1 15-38, TM2 115-130, TM3 169-187; N-terminus lumenal) [file:human/EMC3/EMC3-uniprot.txt TOPO_DOM/TRANSMEM features].
- Oxa1/YidC-superfamily insertase fold; Pfam PF01956 EMC3_TMCO1; distant homolog of Get1/YidC: "EMC3 is a distant homolog of Get1" [PMID:29242231 "EMC3 is a distant homolog of Get1"], both "evolved from an ancestral prokaryotic insertase of the YidC family".
- Belongs to the EMC3 family [file:human/EMC3/EMC3-uniprot.txt "Belongs to the EMC3 family"].

## EMC complex membership
- Identified biochemically in the EMC during ERAD network mapping [PMID:22119785; UniProt "Component of the ER membrane protein complex (EMC)."].
- Strongest verified binary partner is EMC2: UniProt INTERACTION line "Q9P0I2; Q15006: EMC2; NbExp=12" — EMC2 is the cytosolic scaffold that cradles EMC3.

## Function — EMC is a TMD insertase; EMC3 is the catalytic core
- EMC catalyzes energy-independent insertion of newly synthesized membrane proteins into the ER membrane [file:human/EMC3/EMC3-uniprot.txt "(EMC) that enables the energy-independent insertion into endoplasmic"].
- Demonstrated as a transmembrane-domain insertase, reconstituted in liposomes: "EMC is a transmembrane domain insertase, a function" [PMID:29242231]; "EMC as an ER-resident insertase for moderately hydrophobic TMDs" [PMID:29242231].
- Post-translational insertion of tail-anchored (TA) proteins (e.g. SQS/squalene synthase) [PMID:29242231; UniProt "post-translational insertion of tail-anchored/TA proteins in"].
- Cotranslational role for multipass proteins: "EMC binds to and promotes the biogenesis of a range of multipass transmembrane proteins" and "EMC engages clients cotranslationally and immediately following" clusters of charged TMDs [PMID:29809151].
- Initiates accurate topogenesis by inserting the first TMD (N-exo) of GPCRs; cooperates with Sec61: "EMC inserts TMDs co-translationally and cooperates with the Sec61 translocon to ensure accurate topogenesis" [PMID:30415835]; "Sec61 translocon was necessary for insertion of the next TMD" [PMID:30415835]. This = stop-transfer membrane-anchor insertion (GO:0045050).

## EMC3 is the substrate-conducting active site (insertase core)
- Cryo-EM structure: substrate insertion occurs via "an enclosed hydrophilic vestibule within the membrane formed by the subunits EMC3 and EMC6" [PMID:32439656 abstract]; requires "a methionine-rich cytosolic loop".
- Structure-guided MUTAGEN of EMC3 residues R31, M101/M106/M110/M111, R180 (the Met-rich loop and the hydrophilic vestibule): "No effect on EMC assembly but decreased membrane insertion of hydrophobic transmembrane helices-containing proteins by the EMC" [file:human/EMC3/EMC3-uniprot.txt MUTAGEN 31/101/106/110/111/180]. Controls F173 and conservative R->K substitutions had no effect. => EMC3 forms the substrate-conducting insertase active site; activity separable from assembly.
- Hence GO:0032977 membrane insertase activity with qualifier `contributes_to` is the CORE molecular function (EMC3 is the catalytic subunit but acts within the complex).

## Curation decisions (summary)
- CORE: GO:0032977 (insertase activity, contributes_to), GO:0071816 (TA insertion), GO:0045050 (stop-transfer insertion), GO:0072546 (EMC complex), GO:0005789 (ER membrane). All ACCEPT.
- GO:0016020 membrane (generic parent of ER membrane) -> KEEP_AS_NON_CORE.
- GO:0005515 protein binding IPIs (PMID:26496610/32296183/33961781/35271311/40205054, mostly the EMC2 interaction) -> KEEP_AS_NON_CORE (real high-throughput interactions but uninformative bare term).
- No REMOVE/MODIFY/UNDECIDED needed; experimental insertase/process annotations are well supported by full-text and the EMC3-specific mutagenesis.

## Verification pass (2026-06-11)
- All 22 PENDING annotations reviewed and filled; status COMPLETE.
- Verbatim supporting substrings confirmed present: uniprot "Component of the ER membrane protein complex (EMC).", "SUBCELLULAR LOCATION: Endoplasmic reticulum membrane", "Multi-pass membrane protein", "Q9P0I2; Q15006: EMC2", "No effect on EMC assembly but decreased" (EMC3 vestibule/Met-loop mutagenesis), "post-translational insertion of tail-anchored/TA proteins in", "stop-transfer membrane-anchor sequences become ER membrane spanning"; PMID:29242231 "transmembrane domain insertase" / "tail-anchored membrane proteins with moderately hydrophobic transmembrane" / "EMC3 is a distant homolog of Get1"; PMID:32439656 "formed by the subunits EMC3 and EMC6" / "enclosed hydrophilic" / "methionine-rich cytosolic loop"; PMID:30415835 "G protein-coupled receptors".
- IPI partners: PMID:26496610/33961781/35271311/40205054 -> EMC2 (Q15006); PMID:32296183 -> Q13126 (non-EMC, likely incidental/client). All bare protein binding -> KEEP_AS_NON_CORE.
- CORE molecular function GO:0032977 (contributes_to) is the catalytic insertase activity; ACCEPT. No REMOVE/MODIFY/UNDECIDED needed.

## Falcon deep-research findings (incorporated 2026-06)

New recent (2020-2024) papers identified by Falcon deep research and verified against PubMed; added to the review references. EMC3-specific / EMC3-vestibule findings not previously captured:

- EMC3 selectivity filter (EMC3-specific mechanism): two conserved positively charged EMC3 residues, R31 and R180, at the hydrophilic-vestibule entrance form a charge-repulsion filter that rejects mitochondrial tail-anchored proteins and enforces the positive-inside rule; making the vestibule negative increases ER misinsertion [PMID:37199759 "Positively charged residues at the entrance to the vestibule function as a selectivity filter that uses charge-repulsion to reject mitochondrial TA proteins"]. Advances EMC3 from "insertase subunit" to an active client-discrimination/topology-fidelity determinant (added to insertase core_function supported_by).
- Post-translational topology rectification at the EMC3/EMC6 vestibule: EMC inserts C-terminal TMDs of multipass proteins (e.g. SOAT1) after ribosome release; the EMC cytosol-facing hydrophilic vestibule is adjacent to the pre-translocated C-tail; ~250 putative multipass clients [PMID:37957425 "the EMC's cytosol-facing hydrophilic vestibule is adjacent to a pre-translocated C-terminal tail"]. Expands the EMC3 catalytic vestibule's role (added to process core_function supported_by).
- Gating plug regulates the EMC3 vestibule: human EMC cryo-EM (apo vs VDAC-bound) reveals a gating plug inside the hydrophilic vestibule (the substrate-binding pocket); its conformational change suggests the EMC is not insertion-competent in the VDAC1-bound state, i.e. state-dependent regulation of the EMC3/EMC6 insertion pocket [PMID:38517390 "we identified a gating plug located inside the EMC hydrophilic vestibule, the substrate-binding pocket for client insertion"].
- In vivo EMC3 requirement (disease/physiology): emc3 loss in Drosophila causes defective phototransduction and photoreceptor degeneration with reduced rhodopsin (ERAD-independent); conditional Emc3 knockout in mice causes rhodopsin mislocalization and rod/cone photoreceptor death [PMID:31263175 "Conditional knockout of the Emc3 gene in mice led to mislocalization of rhodopsin protein and death of cone and rod photoreceptor cells"]. Conserved in vivo evidence that EMC3 is required for biogenesis of rhodopsin, a multipass GPCR-like client.
- Note (not added to YAML): Falcon also cited Zhu et al. 2020 (PLoS ONE, DOI:10.1371/journal.pone.0238435), a mouse bipolar-cell Emc3 conditional-KO retinal degeneration study; a PMID could not be resolved via PubMed search in this pass, so it is recorded here only by DOI. The closely related, fully PubMed-verified Xiong 2020 paper (PMID:31263175) covers the core EMC3 retina in-vivo finding and was added instead.
