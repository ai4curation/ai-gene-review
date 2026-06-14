# P3H1 (LEPRE1 / GROS1 / Leprecan-1) — gene review notes

UniProt: Q32P28 (P3H1_HUMAN), 736 aa precursor. HGNC:19316. Human.
EC 1.14.11.7 (procollagen-proline 3-dioxygenase / prolyl 3-hydroxylase).

## Core identity and function

P3H1 is an ER-lumenal 2-oxoglutarate / Fe(II)-dependent dioxygenase that catalyzes
3-hydroxylation of specific proline residues in procollagen.

- [file:human/P3H1/P3H1-uniprot.txt "Has prolyl 3-hydroxylase activity and catalyzes the post-"] / "translational formation of 3-hydroxyproline in -Xaa-Pro-Gly- sequences in pro-collagen chains, a critical step for the formation of mature collagen trimers (PubMed:39245686)."
- Catalytic reaction (UniProt): "L-prolyl-[collagen] + 2-oxoglutarate + O2 = trans-3-hydroxy-L-prolyl-[collagen] + succinate + CO2 ... EC=1.14.11.7" supported by [PMID:39245686].
- Cofactors: Fe cation; L-ascorbate (vitamin C). UniProt COFACTOR section + keywords "Iron; Metal-binding; ... Vitamin C." Fe(3+) and 2-oxoglutarate binding residues His587, Asp589, His659, Arg669, etc., with mutagenesis (H587A, H659A, R669H = loss of activity).
- Fe2OG dioxygenase domain 564-678; InterPro IPR005123 / IPR006620; member of leprecan family.

The specific physiological substrate residue is alpha1(I)Pro986 (and alpha1(II)Pro986).
- [PMID:17277775 "CRTAP forms a complex with cyclophilin B and prolyl 3-hydroxylase 1, which is encoded by LEPRE1 and hydroxylates one residue in type I collagen, alpha1(I)Pro986."]
- [PMID:22615817 "This complex is responsible for one step in collagen post-translational modification, the prolyl 3-hydroxylation of specific proline residues, specifically α1(I) Pro986. P3H1 provides the enzymatic activity of the complex"]

## The PCP / P3H1-CRTAP-PPIB complex

P3H1 is the catalytic core of the ER collagen prolyl 3-hydroxylation complex
("PCP complex") with CRTAP (O75718) and PPIB / cyclophilin B (P23284), in 1:1:1 stoichiometry.
- [file:human/P3H1/P3H1-uniprot.txt "Forms a ternary complex with PPIB (CYPB) and CRTAP, known as"] / "the PCP complex, in a 1:1:1 stoichiometric ratio; this complex binds unfolded collagen (PubMed:39245686)."
- Cryo-EM structures (8K0E/F/I/M/8K17/8KC9) of the ternary and dual-ternary complex with 2-OG and Fe(3+) and a collagen analog [PMID:39245686].
- [PMID:39245686 "The assembly of the PCP complex initiates with the association between P3H1 and CRTAP, resulting in the formation of the binary complex. Subsequently, PPIB joins the binary complex to form the PCP ternary complex."]
- The active sites of P3H1 and PPIB form a face-to-face bifunctional reaction center: "The active sites of P3H1 and PPIB form a face-to-face bifunctional reaction center, indicating a coupled modification mechanism." [PMID:39245686]
- P3H1 is the only complex component with a KDEL ER-retrieval signal (C-terminal "...KPKDEL", residues 733-736 "Prevents secretion from ER"). KDEL is essential for function in vivo [PMID:22615817].

## Mutual stabilization / chaperone role

CRTAP and P3H1 mutually stabilize each other in the ER; loss of either depletes both (proteasomal degradation of the orphan).
- [PMID:19846465 "These data indicate that CRTAP and P3H1 are mutually stabilized in the collagen prolyl 3-hydroxylation complex."]
- [PMID:19846465 "Proteasomal inhibitors partially rescue P3H1 protein in CRTAP-null cells."]
- The complex also has chaperone activity (inhibits citrate synthase aggregation, assists rhodanese refolding, collagen fibrillogenesis): [PMID:19846465 "the prolyl 3-hydroxylation complex has recently been reported by the Bachinger laboratory to function as a chaperone"]; [PMID:22615817 "the P3H1/CRTAP/CyPB complex has 3 distinct activities: it is a prolyl 3-hydroxylase, a PPIase, and a molecular chaperone"]. This underpins protein folding / protein stabilization GO terms.

PPIB/CyPB loss does NOT abolish Pro986 3-hydroxylation [PMID:20089953 "The proband's collagen had normal collagen folding and normal prolyl 3-hydroxylation"], i.e. P3H1 is the catalytic core; CyPB is the PPIase partner.

## Localization

Isoform 1 (736 aa, KDEL) is ER-resident; this is the catalytically relevant location.
- [file:human/P3H1/P3H1-uniprot.txt "SUBCELLULAR LOCATION: [Isoform 1]: Endoplasmic reticulum"]
- ER lumen (Reactome TAS), ER (IDA PMID:19846465, PMID:20089953; EXP PMID:19088120).
- [PMID:19088120 "The affected splice form encodes a 736 amino acid (AA) protein with a \"KDEL\" endoplasmic reticulum retention signal."] — establishes isoform 1 / ER as the functional form.
- Secondary/secreted: as a CSPG, P3H1 (leprecan) can be secreted into ECM. UniProt: "Secreted, extracellular space, extracellular matrix" (by similarity to rat). This and proteomics localizations (exosome, membrane, ECM colocalization) are non-core / context-specific captures.

## Disease

Osteogenesis imperfecta type 8 (OI8; MIM 610915), autosomal recessive, severe/lethal. Null LEPRE1 -> loss of Pro986 3-hydroxylation, collagen overmodification, delayed folding.
- [PMID:17277775 "Prolyl 3-hydroxylase 1 is therefore crucial for bone development and collagen helix formation."]
- W675L variant: loss of catalytic activity (UniProt VARIANT + PMID:39245686).

## "Growth suppressor 1" / proliferation

Original cloning as Gros1, a putative growth suppressor in fibroblasts (NIH3T3 overexpression slowed growth). This predates knowledge of its enzymatic role; NAS, weak/historical.
- [PMID:10951563 "Stable transfection of the mouse cDNA encoding the 85-kDa protein into NIH3T3 cells resulted in their slow growth and reduced colony-forming efficiency."]
- UniProt FUNCTION: "Has growth suppressive activity in fibroblasts." Keep as non-core (over-annotated relative to the well-established collagen-modifying enzyme role).

## Annotation decisions summary

CORE:
- GO:0019797 procollagen-proline 3-dioxygenase activity (MF) — ACCEPT core (IDA PMID:39245686; IBA; ISS; IEA). EC 1.14.11.7.
- GO:0005788 ER lumen / GO:0005783 ER (CC) — ACCEPT (site of action).
- GO:0032963 collagen metabolic process (BP) — ACCEPT/core-ish (its biological role).
- GO:0032991 protein-containing complex part_of — ACCEPT (PCP complex membership).

Cofactor / catalytic-support MF (keep, but not bare core):
- GO:0005506 iron ion binding — ACCEPT (catalytic Fe(II) cofactor; structurally demonstrated).
- GO:0031418 L-ascorbic acid binding — KEEP_AS_NON_CORE / ACCEPT (vitamin C cofactor).
- GO:0016705 oxidoreductase activity (paired donors, O2) — parent of the specific dioxygenase MF; KEEP_AS_NON_CORE (generic; GO:0019797 is the informative term).

BP (complex chaperone / collagen biogenesis):
- GO:0006457 protein folding — ACCEPT/KEEP (complex chaperone function; IMP PMID:17277775, ISS PMID:15044469).
- GO:0050821 protein stabilization — ACCEPT (mutual stabilization, IMP PMID:19846465, PMID:22615817).
- GO:0060348 bone development — KEEP_AS_NON_CORE (downstream physiology; OI phenotype).
- GO:0050708 regulation of protein secretion — KEEP_AS_NON_CORE (collagen secretion delay in nulls).
- GO:1901874 negative regulation of post-translational protein modification — KEEP_AS_NON_CORE. This reflects that loss of P3H1 leads to OVER-modification (lysyl hydroxylation/glycosylation) of the helix; the wild-type complex limits over-modification by speeding folding. Slightly contorted but defensible from the IMP data (overmodification on P3H1 loss).

CC bare-binding / proteomics (non-core):
- GO:0005515 protein binding (IPI x3: PMID:30021884, PMID:33961781, PMID:39245686) — KEEP_AS_NON_CORE. Partners O75718=CRTAP and P23284=PPIB (in 39245686) are real complex partners; 30021884 (histone XL-MS) and 33961781 (BioPlex) capture CRTAP. Bare "protein binding" uninformative.
- GO:0005518 collagen binding contributes_to (ISS PMID:15044469) — ACCEPT/KEEP_AS_NON_CORE; the complex binds unfolded/denatured collagen substrate (consistent with structure & enzymology).
- GO:0070062 extracellular exosome (HDA PMID:19056867) — KEEP_AS_NON_CORE (urinary exosome proteomics; not the functional ER site).
- GO:0016020 membrane (HDA PMID:19946888) — KEEP_AS_NON_CORE (NK-cell membrane proteome; original immunoscreen was a "plasma membrane protein"; low-resolution).
- GO:0031012 extracellular matrix colocalizes_with (HDA PMID:28327460) — KEEP_AS_NON_CORE (consistent with secreted CSPG leprecan form; not the catalytic ER role).
- GO:0010976 positive regulation of neuron projection development (ISS GO_REF:0000024 from rat Q9R1J8) — MARK_AS_OVER_ANNOTATED (electronic ISS transfer from rat leprecan; no human evidence; tangential to collagen-modifying role).
- GO:0008285 negative regulation of cell population proliferation (NAS PMID:10951563) — KEEP_AS_NON_CORE (historical Gros1 growth-suppressor assertion; superseded by enzymatic characterization).

## Falcon deep-research findings (incorporated 2026-06)

Falcon report largely corroborated the existing review; the PCP cryo-EM structural paper it foregrounds (Li et al. 2024, Nat Commun, DOI 10.1038/s41467-024-52321-6) is already in the review as PMID:39245686. Two additional verified references were added:

- ER-stress / proteostasis pathophysiology of recessive OI complex defects: in primary fibroblasts from recessive OI patients (including P3H1/LEPRE1 deficiency), intracellular retention of overmodified type I collagen causes ER enlargement, protein aggregates, PERK-branch UPR activation and apoptosis; the chemical chaperone 4-phenylbutyrate (4-PBA) rescues ER proteostasis and cell survival [PMID:31171565 "the intracellular retention of overmodified type I collagen molecules causes ER enlargement associated with the presence of protein aggregates, activation of the PERK branch of the unfolded protein response and apoptotic death"]. Added as a MEDIUM-relevance reference (complex/disease-mechanism level, not P3H1-catalysis-specific). Not in publications cache.
- Clinical/therapeutic cohort: a retrospective study of rare (non-COL1A1/COL1A2) bone-fragility disorders treated with bisphosphonates includes patients with pathogenic P3H1 variants; lumbar-spine BMD increased dose-dependently and fracture rate fell on treatment [PMID:38926541 "all patients showed a significant increase in LS BMD while treated and this increase was dependent on the dose received. The increase in LS BMD also translated in a reduction of fracture rate during treatment"]. Added as a LOW-relevance reference (OI8 disease management context). Not in publications cache.
- Falcon quantitative claims (e.g. PCP ~150 kDa / ~110 Å / 3.17–3.75 Å; bisphosphonate fracture-rate 3.9→1.4, p=0.02; founder splice variant c.1080+1G>T carrier frequencies) were noted but not added to YAML annotations; substrate/complex/localization facts were already fully covered by the existing review (alpha1(I)Pro986; 1:1:1 P3H1/CRTAP/PPIB complex; KDEL ER retention; bifunctional reaction center).
- No `action:` changes made; reviews were already COMPLETE and these papers are downstream disease/mechanism context. Edits are additive (new references only).
