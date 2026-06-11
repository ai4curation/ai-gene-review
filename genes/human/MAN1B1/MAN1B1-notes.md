# MAN1B1 (ER alpha-1,2-mannosidase I / ERManI) research notes

UniProt: Q9UKM7 (MA1B1_HUMAN). HGNC:6823. EC 3.2.1.113. Glycoside hydrolase family 47 (GH47).
699 aa, type II single-pass ER membrane protein (signal-anchor).

## Identity / catalytic activity

MAN1B1 encodes the human Endoplasmic reticulum mannosyl-oligosaccharide 1,2-alpha-mannosidase
(ER alpha-1,2-mannosidase I, ERManI, ERMan1, Man9-mannosidase). It is a true, active glycosidase.

- [file:human/MAN1B1/MAN1B1-uniprot.txt "EC=3.2.1.113"] and CAZy GH47 family membership.
- It "catalyzes the first mannose trimming step in mammalian Asn-linked oligosaccharide biosynthesis"
  [PMID:10409699 "the enzyme that catalyzes the first mannose trimming step in mammalian Asn-linked oligosaccharide biosynthesis"].
- Cleaves a single specific alpha-1,2-mannose at low concentration: the recombinant enzyme "removes a
  single mannose residue from Man9GlcNAc and [1H]-NMR analysis indicates that the only product is
  Man8GlcNAc isomer B, the form lacking the middle-arm terminal alpha 1,2-mannose"
  [PMID:10521544 "The recombinant enzyme removes a single mannose residue from Man9GlcNAc and [1H]-NMR analysis indicates that the only product is Man8GlcNAc isomer B"].
  Thus product = Man8GlcNAc2 isomer B (M8b), lacking the B-branch (middle-arm) terminal mannose.

## Calcium dependence / inhibitor profile (GH47 mechanism)

- "Calcium is required for enzyme activity and both 1-deoxymannojirimycin and kifunensine inhibit the
  human alpha 1,2-mannosidase" [PMID:10521544 "Calcium is required for enzyme activity and both 1-deoxymannojirimycin and kifunensine inhibit the human alpha 1,2-mannosidase"].
- "The mannose cleavage reaction required divalent cations as indicated by inhibition with EDTA or EGTA
  and reversal of the inhibition by the addition of Ca(2+)"
  [PMID:10409699 "The mannose cleavage reaction required divalent cations as indicated by inhibition with EDTA or EGTA and reversal of the inhibition by the addition of Ca(2+)"].
- UniProt: COFACTOR Ca(2+); BINDING 688 Ca(2+). The Ca2+ is structural/catalytic in the GH47 fold; it is
  not an independent "calcium signaling" function. Hence GO:0005509 calcium ion binding is a real but
  subsidiary/structural attribute (KEEP_AS_NON_CORE).
- Inverting hydrolytic mechanism with novel sugar conformations resolved structurally
  [PMID:15713668 "The unusual inverting hydrolytic mechanism catalyzed by members of this family is investigated here"];
  catalytic residues mapped by mutagenesis (E330, D463, H524, E599) — UniProt ACT_SITE 330/463/570/599.

## Broader specificity at high concentration (mannose timer beyond M8b)

The earlier view (strict single-mannose trimming) was revised:
- [PMID:12090241 "The specificity of the yeast and human class I ER alpha 1,2-mannosidases involved in ER quality control is not as strict previously reported"] (title-only cached; UniProt cites it for FUNCTION, CATALYTIC ACTIVITY, SUBSTRATE SPECIFICITY).
- At high enzyme concentration ERManI excises additional residues: "at very high concentrations it can
  excise up to four alpha1,2-linked mannose residues" and "ERManI is required for trimming to
  Man(5-6)GlcNAc(2) and for ERAD in cells in vivo"
  [PMID:18003979 "at very high concentrations it can excise up to four α1,2-linked mannose residues"]
  [PMID:18003979 "ERManI is required for trimming to Man 5–6 GlcNAc 2 and for ERAD in cells in vivo"].
- In vitro it can generate Man6/Man5 and trims misfolded glycoproteins more extensively:
  [PMID:22160784 "the enzyme generated Man(6)GlcNAc(2)-PA and Man(5)GlcNAc(2)-PA"]
  [PMID:22160784 "hERManI could recognize tertiary and/or quaternary structures of glycoproteins and remove more α-1,2 linked mannoses from misfolded glycoproteins"].
  This explains the conformational/misfolding selectivity underlying the ERAD "mannose timer".

## Role in ERAD / glycoprotein quality control ("mannose timer")

- UniProt FUNCTION: "Involved in glycoprotein quality control targeting of misfolded glycoproteins for
  degradation" [file:human/MAN1B1/MAN1B1-uniprot.txt "Involved in glycoprotein quality control targeting of misfolded glycoproteins for degradation"].
- Trimming removes the glycoprotein from the calnexin/reglucosylation cycle and commits it to ERAD:
  [PMID:18003979 "trimming by ERManI to the smaller oligosaccharides would remove the glycoprotein from reglucosylation and calnexin binding cycles"].
- Acts as a timer enzyme [PMID:25411339 "acts as a timer enzyme, modifying N-linked sugar chains of glycoproteins with time"].
- Mannose trimming by ERManI is required for handoff to downstream ERAD lectins/E3 ligases:
  [PMID:21062743 "mannose trimming enables delivery of a substrate glycoprotein from EDEM1 to late ERAD steps through association with XTP3-B"]; inhibition (kifunensine) or ERManI knockdown blocks
  substrate association with XTP3-B and the E3 ligases HRD1 and SCF(Fbs2).

## Localization

- ER membrane, type II single-pass: [file:human/MAN1B1/MAN1B1-uniprot.txt "Endoplasmic reticulum membrane"]
  and "Single-pass type II membrane protein"; ER pattern on expression
  [PMID:10409699 "Expression of an epitope-tagged full-length form of the human mannosidase homolog in normal rat kidney cells resulted in an ER pattern of localization"].
- Concentrated in the pericentriolar ER-derived quality control compartment (ERQC):
  [PMID:18003979 "ERManI is strikingly concentrated together with the ERAD substrate in the pericentriolar ER-derived quality control compartment (ERQC)"].
  The high local concentration there enables extensive trimming (timer).
- At steady state, resides in mobile quality-control vesicles (QCVs) of ER-like density that converge to
  the ERQC under stress: [PMID:25411339 "ERManI is located, at the steady state, in quality control vesicles (QCVs) to which ERAD substrates are transported"]. Supports cytoplasmic vesicle (GO:0031410) annotation.
- IMPORTANT for Golgi annotation: PMID:25411339 concludes the Golgi sighting is an artifact:
  [PMID:25411339 "membrane disturbance, as is common in immunofluorescence methods, leads to an artificial appearance of ERManI in a Golgi pattern"]. So the Golgi apparatus (GO:0005794, TAS PMID:22160784) annotation
  is disputed/likely artifactual; keep as non-core rather than core, and do not treat as a genuine site of
  action. (Note PMID:22160784 abstract is an in vitro study and does not itself assert Golgi localization;
  the TAS Golgi annotation traces to the broader controversy.)
- extracellular vesicle (GO:1903561, HDA PMID:24769233, CSF EVs) and membrane (GO:0016020, HDA
  PMID:19946888, NK membrane proteome) are large-scale proteomics detections; real but peripheral.

## Disease

- Biallelic MAN1B1 variants cause autosomal-recessive intellectual disability (Rafiq syndrome / RAFQS;
  MIM:614202), a congenital disorder of glycosylation (MAN1B1-CDG):
  [file:human/MAN1B1/MAN1B1-uniprot.txt "Rafiq syndrome (RAFQS) [MIM:614202]: An autosomal recessive disorder characterized by variably impaired intellectual and motor development"].
  Variant R334C causes ~1300-fold loss of activity; E397K disrupts stable expression (UniProt VARIANTs).
  Serum transferrin isoelectric focusing shows a CDG type 2 pattern.

## Curation reasoning summary

- Core MF: GO:0004571 mannosyl-oligosaccharide 1,2-alpha-mannosidase activity (IDA/EXP/IMP/IBA/TAS) — ACCEPT.
- Core BP: GO:0036503 ERAD pathway; GO:1904380 ER mannose trimming; GO:0140277 ER N-glycan trimming — ACCEPT.
- Core CC: GO:0005789 ER membrane, GO:0005783 ER, GO:0044322 ERQC — ACCEPT.
- GO:0031410 cytoplasmic vesicle (QCV) — ACCEPT (genuine, PMID:25411339).
- GO:0005509 calcium ion binding — KEEP_AS_NON_CORE (structural cofactor of GH47, not independent function).
- Generic IEA terms membrane (GO:0016020), carbohydrate metabolic process (GO:0005975), glycoprotein
  metabolic process (GO:0009100), oligosaccharide metabolic process (GO:0009311) — too general vs the
  specific terms; MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE.
- GO:0005794 Golgi apparatus (TAS) — KEEP_AS_NON_CORE; likely fixation artifact per PMID:25411339.
- GO:1903561 extracellular vesicle (HDA) — KEEP_AS_NON_CORE (proteomics).
- GO:0019082 viral protein processing (Reactome, SARS-CoV-2 spike N-glycan trimming) — KEEP_AS_NON_CORE;
  it is the generic mannosidase activity acting on a viral glycoprotein, not a distinct function.
- GO:0036510 trimming of terminal mannose on C branch (Reactome TAS) — ACCEPT (specific correct sub-step).
- Many redundant Reactome TAS GO:0004571 and GO:0044322 entries — ACCEPT (correct, redundant).
</content>
</invoke>
