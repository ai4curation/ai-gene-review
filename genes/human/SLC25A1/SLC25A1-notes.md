# SLC25A1 (Tricarboxylate transport protein / mitochondrial citrate carrier, CIC/CTP) review notes

UniProt: P53007 (TXTP_HUMAN). Gene: SLC25A1 (HGNC:10979; synonym SLC20A3). Chromosome 22q11 (DiGeorge/velocardiofacial critical region).

## Identity and family
- RecName "Tricarboxylate transport protein, mitochondrial"; AltNames "Citrate transport protein" (CTP), "Mitochondrial citrate carrier" (CIC), "Solute carrier family 25 member 1", "Tricarboxylate carrier protein" [file:human/SLC25A1/SLC25A1-uniprot.txt "RecName: Full=Tricarboxylate transport protein, mitochondrial"].
- Member of the mitochondrial carrier (SLC25) family, TC 2.A.29 [file:human/SLC25A1/SLC25A1-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family."]. Three Solcar repeats, six predicted transmembrane helices (multi-pass) — canonical SLC25 fold [file:human/SLC25A1/SLC25A1-uniprot.txt "Multi-pass membrane protein"].
- 311 aa precursor with a short cleavable presequence (residues 1–13) that is dispensable for targeting/insertion but keeps the protein import-competent/soluble [file:human/SLC25A1/SLC25A1-uniprot.txt "Possesses a short cleavable presequence, which, however, is found"].

## Molecular function — the citrate carrier
- Mitochondrial electroneutral antiporter that exports citrate from the matrix into the cytosol in exchange for malate [file:human/SLC25A1/SLC25A1-uniprot.txt "Mitochondrial electroneutral antiporter that exports citrate"]. Also exchanges citrate for isocitrate, phosphoenolpyruvate, cis-aconitate and (to a lesser extent) trans-aconitate, maleate and succinate [file:human/SLC25A1/SLC25A1-uniprot.txt "Also able to mediate the exchange of citrate for"].
- Rhea catalytic activities in UniProt encode the antiport half-reactions: (S)-malate(in)+citrate(out)=(S)-malate(out)+citrate(in) (RHEA:72483); D-threo-isocitrate/citrate (RHEA:72471); citrate/succinate (RHEA:28835); cis-aconitate/citrate (RHEA:72475); trans-aconitate/citrate (RHEA:72479); PEP/citrate (RHEA:72487); maleate/citrate (RHEA:72491).
- Km(citrate) = 7.5 uM [file:human/SLC25A1/SLC25A1-uniprot.txt "KM=7.5 uM for citrate"].
- This is a **transporter, not an enzyme** — no catalytic/metabolic MF should be assigned; the "CATALYTIC ACTIVITY" Rhea entries describe transport (antiport) reactions, not chemical transformations.
- Substrate specificity determined in Majd et al. 2018: "the human citrate carrier predominantly transports citrate, isocitrate, cis-aconitate, phosphoenolpyruvate and malate" [PMID:29031613 "the human citrate carrier \npredominantly transports citrate, isocitrate, cis-aconitate, phosphoenolpyruvate and \nmalate"]. Succinate is only a minor/lesser substrate, so the EXP citrate:succinate antiporter (GO:0015515) term names the wrong physiological counter-substrate as primary; malate is the main counter-substrate.
- Mechanism: substrates exchanged consecutively (ping-pong), one transported then dissociating before the second binds [file:human/SLC25A1/SLC25A1-uniprot.txt "Substrate exchange across the membrane occurs consecutively with one substrate"]. SLC25 carriers function as monomers (Cimadamore-Werthein et al. 2024, PMID:38937634) [file:human/SLC25A1/SLC25A1-uniprot.txt "SUBUNIT: Monomer."].

## Biological role
- Supplies cytosolic citrate as the acetyl-CoA source (via ATP-citrate lyase, ACLY) for fatty-acid, sterol, dolichol and ubiquinone synthesis; citrate export "cannot be fully compensated by other pathways, restricting the cytosolic production of acetyl-CoA that is required for the synthesis of lipids, sterols, dolichols and ubiquinone" [PMID:29031613 "restricting the cytosolic production of \nacetyl-CoA that is required for the synthesis of lipids, sterols, dolichols and \nubiquinone"].
- Cytosolic citrate also has roles in fatty acid/sterol synthesis, regulation of glycolysis, and protein acetylation [file:human/SLC25A1/SLC25A1-uniprot.txt "In the cytoplasm, citrate plays important"].
- Part of the citrate–malate shuttle with ACLY (Reactome R-HSA-75849).

## Ferroptosis (PMID:39881208, full text available)
- CRISPR-Cas9 SLC superfamily screen identified SLC25A1 as a critical ferroptosis regulator in cancer cells [PMID:39881208 "identify SLC25A1 as a critical ferroptosis \nregulator in human cancer cells"].
- Mechanism: "SLC25A1 drives citrate export from the mitochondria to the cytosol, where it fuels acetyl-CoA synthesis by ATP citrate lyase (ACLY)"; this acetyl-CoA "sustains FSP1 acetylation and prevents its degradation by the proteasome" [PMID:39881208 "SLC25A1 drives citrate export from the \nmitochondria to the cytosol, where it fuels acetyl-CoA synthesis by ATP citrate \nlyase (ACLY)"]. Net effect: SLC25A1 protects against ferroptosis (negative regulation of ferroptosis, GO:0110076, IMP). This is a downstream/contextual consequence of the core transport function, not the core evolved function.

## Localization
- Mitochondrion inner membrane (multi-pass) [file:human/SLC25A1/SLC25A1-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane"]. GOA has this via ISS (from mouse Q8JZU2) and IEA (SubCell mapping); the mitochondrion (IBA, HTP) and mitochondrial membrane (IMP) terms are true but less specific parents.
- HDA "nucleus" (PMID:21630459, sperm-nucleus proteomics) and HDA "extracellular exosome" (PMID:19056867, urinary-exosome proteomics) are high-throughput proteomics detections in fractions that are not the site of function; these are over-annotations for an inner-membrane citrate carrier.

## Disease
- Combined D-2- and L-2-hydroxyglutaric aciduria (D2L2AD, MIM:615182), autosomal recessive neonatal-onset encephalopathy [file:human/SLC25A1/SLC25A1-uniprot.txt "Combined D-2- and L-2-hydroxyglutaric aciduria (D2L2AD)"]. Many missense variants abolish or severely reduce citrate transport [PMID:29031613 "nine \nmutations abolish transport of citrate completely, whereas the other three \nreduce the transport rate by >70%"].
- Congenital myasthenic syndrome 23, presynaptic (CMS23, MIM:618197) [file:human/SLC25A1/SLC25A1-uniprot.txt "Myasthenic syndrome, congenital, 23, presynaptic (CMS23)"].

## Annotation review summary
- Core MF: **GO:0071913 citrate secondary active transmembrane transporter activity** (IDA PMID:29031613; also IBA) — most specific MF that captures the secondary-active antiport mechanism; parent of GO:0015137/GO:0015142. GO does not currently have a "citrate:malate antiporter activity" term.
- GO:0015137 (citrate transmembrane transporter activity, TAS PMID:8666394) and GO:0015142 (tricarboxylic acid transmembrane transporter activity, IDA/TAS) are correct broader parents — ACCEPT / KEEP_AS_NON_CORE.
- GO:0015515 (citrate:succinate antiporter activity, EXP) — MODIFY toward GO:0071913: succinate is only a minor substrate; malate is the primary physiological counter-substrate.
- Core BP: **GO:0006843 mitochondrial citrate transmembrane transport** (IDA PMID:29031613; IBA).
- Core CC: **GO:0005743 mitochondrial inner membrane** (ISS/IEA).
- Over-annotations: nucleus, extracellular exosome (HDA proteomics); mitochondrion / mitochondrial membrane are true-but-broad parents of the inner-membrane location.
- IEA GO:0071422 succinate transmembrane transport (inferred from GO:0015515) — over-annotation because succinate is a minor substrate; MARK_AS_OVER_ANNOTATED.
- negative regulation of ferroptosis (IMP) — real but downstream/contextual; KEEP_AS_NON_CORE.
