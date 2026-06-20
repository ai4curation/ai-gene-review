# CDK5RAP3 (Q96JB5) review notes

## Identity and synonyms
- HGNC: CDK5RAP3 (HGNC:18673); UniProt Q96JB5 (CK5P3_HUMAN); GeneID 80279.
- Synonyms: C53, LZAP, IC53, NLBP, MST016, OK/SW-cl.114, PP1553, HSF-27. AltName "CDK5 activator-binding protein C53" and "LXXLL/leucine-zipper-containing ARF-binding protein (LZAP)".
- 506 aa, no catalytic domain; **despite its name it is not a kinase** and has no known enzymatic activity [PMID:21283629 "LZAP has no known enzymatic activity, implying that its biological functions are likely mediated by its protein-protein interactions"].
- 4 isoforms. Structure solved by cryo-EM as part of the UREL complex on the 60S ribosome (PDB 8OHD, 8OJ0, 8OJ5, 8QFC, 9GY4).

## Core function: UFMylation pathway substrate adaptor (UREL complex)
CDK5RAP3 is a substrate adaptor/recruiter component of the heterotrimeric **UFM1 ribosome E3 ligase (UREL) complex** = UFL1 (E3) + DDRGK1/UFBP1 (adaptor, ER anchor) + CDK5RAP3 [PMID:36121123, PMID:37595036, PMID:38383785, PMID:38383789]. ComplexPortal CPX-8304.

Mechanistic findings:
- UFL1 is inactive alone; UFL1/UFBP1 form the active scaffold-type E3. CDK5RAP3 binds and forms an integral part of the ligase complex and acts as a **substrate adaptor that directs UFMylation to ribosomal protein RPL26/uL24** [PMID:36121123 "we characterize a second adaptor protein CDK5RAP3 that binds to and forms an integral part of the ligase complex... CDK5RAP3 functions as a substrate adaptor that directs UFMylation to the ribosomal protein RPL26"]. In vitro CDK5RAP3 *inhibits/constrains* UFL1/UFBP1 activity, restricting it to mono-UFMylation of RPL26 at K134 [PMID:36121123].
- CDK5RAP3 acts as the adaptor for ufmylation of RPL26 on the 60S subunit of disomes (ER-RQC) [PMID:37595036 "CDK5RAP3, an adaptor for ufmylation of ribosomal subunit RPL26"].
- Cryo-EM: UREL wraps around 60S forming a C-shaped clamp; required for **release of 60S from SEC61 translocon** and 60S recycling; loss of functional UREL causes accumulation of 60S-SEC61 complexes at the ER [PMID:38383789 "UREL wraps around the 60S subunit to form a C-shaped clamp... UFMylation is necessary for releasing SEC61 from 60S subunits"; PMID:38383785 "UFMylation facilitates the rescue of 60S ribosomal subunits that are released after ribosome-associated quality-control-mediated splitting of ribosomes that stall during co-translational translocation"].
- CDK5RAP3 RPL10a-binding domain (RBD, residues 355-370) anchors UREL onto the ribosome via RPL10a/uL1 (UniProt DOMAIN; PMID:38383789). Mutations E217A/D355A/E359A/E373A/R432A abolish UFL1 interaction [UniProt MUTAGEN; PMID:37595036].

## ER-phagy / reticulophagy and ATG8 binding
- C53/CDK5RAP3 is a cytosolic protein recruited to autophagosomes during ER stress in plant and mammalian cells; interacts with ATG8 via shuffled ATG8-interacting motifs (sAIM, motifs at 267-270, 292-295, 310-313); functions as an ER-phagy receptor maintaining ER homeostasis during stress [PMID:32851973]. Interacts with GABARAP/GABARAPL1/GABARAPL2/MAP1LC3A/MAP1LC3B; W269/W294/W312 required [UniProt; PMID:36543799, PMID:36762703].
- UFM1 system regulates ER-phagy through ufmylation of CYB5R3; CDK5RAP3 is part of the E3 complex; ER membrane localization [PMID:36543799].
- The sAIMs bind both ATG8 and UFM1 (UniProt DOMAIN; PMID:32851973, PMID:36762703).

## Localization
- ER membrane (tethered as part of UREL) [PMID:36543799, PMID:38383785, PMID:38383789]; cytoplasm/cytosol [PMID:15790566, PMID:16173922, PMID:19223857; HPA IDA cytosol]; nucleus [PMID:16173922]; centrosome / cytoskeleton / microtubule (associates with microtubules; colocalizes after caspase cleavage) [PMID:19223857, PMID:23478299].

## Development (UFMylation-dependent)
- Cdk5rap3 KO mice are embryonic lethal with severe liver hypoplasia (delayed proliferation, compromised differentiation); CDK5RAP3 is "a UFL1 substrate adaptor" crucial for liver development [PMID:30635284]. Liver development / definitive erythrocyte differentiation / ER stress response ISS/IEA from mouse ortholog Q99LM2. These are downstream physiological consequences of the UFMylation pathway role.

## LZAP/C53 "moonlighting" roles (older literature, mostly overexpression/KD)
- NF-kB: LZAP binds RelA, impairs RelA Ser536 phosphorylation, inhibits NF-kB transcriptional activity; proposed tumor suppressor [PMID:17785205]. RCAD/DDRGK1 + CDK5RAP3 stability and NF-kB modulation [PMID:20228063].
- p53/ARF/MDM2: LZAP binds ARF, alters ARF regulation of HDM2/MDM2, activates p53, causes p53-dependent G1 arrest [PMID:16173922]. NOTE: GOA carries two negated (NOT) annotations from this paper (GO:2000060 NOT positive regulation of ubiquitin-dependent protein catabolic process; GO:0005730 NOT nucleolus).
- G2/M checkpoint: C53 modulates G2/M DNA damage checkpoint via Cdk1-cyclin B1 [PMID:15790566]; antagonizes Chk1 to promote Cdk1 activation/mitotic entry; centrosome-localized [PMID:19223857].
- p38 MAPK: LZAP inhibits p38 phosphorylation by facilitating p38 association with Wip1/PPM1D phosphatase [PMID:21283629].
- Apoptosis: caspase-cleaved C53 causes abnormal microtubule bundling and nuclear envelope rupture [PMID:23478299].
- Cell invasion: NLBP (=CDK5RAP3) inhibits cell invasion [PMID:20164180] (this paper is the one that identifies UFL1 interaction in UniProt).
- Proliferation: IC53 stimulates ECV304 proliferation, upregulated in failing heart [PMID:12054757].
- Maxer (DDRGK1) anchors CDK5RAP3 to the ER; loss causes G1 accumulation [PMID:20531390].
- Cdk5 activator binding: original identification as p35nck5a/Cdk5 activator-binding protein C53 [PMID:10721722, PMID:10915792] — basis for the (misleading) gene name; no evidence CDK5RAP3 regulates Cdk5 kinase activity directly; "regulation of neuron differentiation"/"brain development" are NAS speculation from these cloning papers.

These LZAP/C53 roles are largely from overexpression/knockdown in cancer cell lines, predate the UFMylation-centric understanding, and are best treated as non-core (KEEP_AS_NON_CORE) relative to the well-established UFMylation/ER-RQC adaptor function.

## Protein-binding (GO:0005515) IPI annotations
Many bare `protein binding` IPI entries from IntAct/HT interactome screens (PMID:16169070, 25416956, 25910212, 31515488, 32296183, 33961781, 37595036, 40205054, 16173922, 20228063, 20164180). Bare `protein binding` is uninformative → MARK_AS_OVER_ANNOTATED. Where the WITH partner is UFL1 (O94874) or UFC1 (Q9Y3C8), the relationship is captured by more specific terms (ubiquitin-like protein ligase binding, ubiquitin-like ligase-substrate adaptor activity), so still mark the bare term over-annotated.

## Summary of action plan
- ACCEPT core: protein ufmylation, ubiquitin-like ligase-substrate adaptor activity, rescue of stalled (cytosolic) ribosome, ribosome disassembly, positive regulation of reticulophagy, ER membrane (is_active_in), transferase complex / protein-containing complex (UREL), ubiquitin-like protein ligase binding (UFL1).
- KEEP_AS_NON_CORE: NF-kB binding, p53/ARF/MDM2 roles, G2/M checkpoint, p38/MAPK regulation, apoptotic nuclear changes, cyclin binding, liver development, erythrocyte differentiation, ER UPR, cell proliferation, neuron differentiation/brain development (NAS), cytoplasm/nucleus/centrosome/cytoskeleton/membrane localizations.
- MARK_AS_OVER_ANNOTATED: all bare `protein binding`.
- Negated annotations (NOT nucleolus, NOT positive regulation of ubiquitin-dependent protein catabolic process) ACCEPT as informative negatives.
