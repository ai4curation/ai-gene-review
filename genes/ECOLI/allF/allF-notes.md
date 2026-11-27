# allF (Escherichia coli K-12, UniProtKB:Q47208) review notes

Formerly fdrA; also ylbD, b0518, JW0506. UniProt entry name ALLF_ECOLI, 555 residues.

## 2026-11-18: first review

### Deep research

`just deep-research ECOLI allF --provider perplexity` was run once and failed: the deep-research client reported that the provider is not available in this environment (no credentials). No deep-research file exists for this gene. The literature below was found by PubMed searches and read from the cached publication files.

PubMed searches (2026-11-18), with hit counts and the relevant hits:

- `fdrA[tiab]`: 29 hits; relevant: PMID:38888336, PMID:36384810, PMID:34494882, PMID:7500942. The other hits were not opened one by one.
- `allF[tiab] AND Escherichia coli`: 2 (PMID:41016821, PMID:38888336)
- `allFGH`: 2 (PMID:41081392, PMID:38888336)
- `oxamic transcarbamylase`: 6 (PMID:41081392, PMID:41016821, PMID:38888336, PMID:34494882, and two older papers on the Streptococcus enzyme that were not opened)
- `fdrA AND (Escherichia coli OR Salmonella)`: 4 (the four fdrA papers above)
- `b0518`, `3DMY`, `Q47208`, `yahF Escherichia coli`: 0 each

No paper reports the subcellular location of AllF, a catalytic residue, or a structure of the AllF-AllG-AllH complex.

### What the protein is

AllF is one of three subunits of oxamate carbamoyltransferase (oxamic transcarbamylase, OXTCase, EC 2.1.3.5).

- [PMID:38888336 "This study discovered that allFGH (fdrA, ylbE, and ylbF) are the genes that encode the global orphan enzyme OXTCase."]
- The activity was measured with purified protein: [PMID:38888336 "The OXTCase activity and kinetics were successfully determined with purified recombinant AllF-AllG-AllH (FdrA-YlbE-YlbF)"].
- AllF alone is not active: [PMID:38888336 "However, the activity of OXTCase was not detected when only FdrA was present."] This is why the EcoCyc row uses `contributes_to`.
- All three genes are needed in vivo: [PMID:38888336 "Taken together, these findings indicate that the oxamate-producing step catalyzed by OXTCase involves an enzyme encoded by the three genes allF, allG, and allH."] and [PMID:38888336 "Complementation with all three genes (allFGH) restored the oxamate level of the triple mutant to that of the wild-type strain (Table 3)."]
- The product was identified by mass: [PMID:38888336 "The mass of the new peak was analyzed by LC-MS as 131.0084, which corresponds to the molecular weight of oxalurate (Fig. 2D)."]
- The assay ran in the direction of oxalurate synthesis: [PMID:38888336 "oxalurate could not be used as a standard substance due to its unavailability, and the enzyme reaction was performed in the reverse direction"]. This matches the GO:0050205 definition (carbamoyl phosphate + oxamate = oxalurate + phosphate). The physiological direction is oxalurate + phosphate to oxamate + carbamoyl phosphate.
- Kinetics: [PMID:38888336 "for the substrate CP, KM and Vmax were 1.3 mM and 15.4 U/mg OXTCase, respectively, and for the substrate oxamate, they were 36.9 mM and 27.0 U/mg OXTCase"]. pH optimum 9.0 [PMID:38888336 "No enzyme activity was detected at pH 6.0 and 7.0"]; the assay mix contained oxamate, carbamoyl phosphate, MgCl2 and Tris buffer, with no CoA and no nucleotide.
- The enzyme is unrelated to the classical transcarbamylases: [PMID:38888336 "the OXTCase encoded by the three genes is a novel transcarbamylase that shows no similarity with known enzymes of the transcarbamylase family"].

Pathway role. [PMID:38888336 "Escherichia coli uses allantoin as the sole nitrogen source during anaerobic growth."] In the oxamate branch [PMID:38888336 "after oxidation of ureidoglycolate to oxalurate, it is converted to carbamoyl phosphate (CP) with the dead-end product oxamate by an oxamic transcarbamylase (OXTCase)"]. Carbamate kinase AllK then makes ATP and ammonia from the carbamoyl phosphate.

The earlier paper from the same laboratory found the gene through an evolved variant. [PMID:34494882 "Transcription of fdrA was induced under anaerobic allantoin degradation conditions, and FdrA was shown to play a crucial role in oxamate production."] The deletion strain made no oxamate: [PMID:34494882 "the ΔfdrA strain could not produce oxamate in allantoin degradation analysis (Table 4), indicating that fdrA encodes an enzyme producing and not degrading oxamate."] The D296Y variant made more oxamate [PMID:34494882 "The FdrAD296Y variant increased glyoxylate conversion to malate by accelerating oxamate production"]. How D296Y does this (activity, affinity or assembly) was not measured on purified enzyme.

### Not a succinyl-CoA synthetase subunit

AllF is a member of PANTHER PTHR11117 (succinyl-CoA ligase subunit alpha) and carries the Pfam CoA-binding (PF02629) and CoA-ligase (PF00549) domains, so databases long called it a predicted acyl-CoA synthetase. [PMID:38888336 "fdrA had been annotated as a gene encoding a putative acyl-CoA synthetase, oxamate:CoA ligase (Pfam 00549), or multicopy suppressor of dominant negative ftsH mutations"].

The evidence against succinyl-CoA synthetase (SCS) activity:

- Direct, but unpublished data: [PMID:34494882 "We detected no SCS activity from FdrA expressed by pCA245N::fdrA (overexpression) or pNTR-SD::fdrA (complementation) using an SCS activity colorimetric assay kit (Sigma) (data not shown)."] and [PMID:34494882 "indicating that fdrA does not encode an SCS or a succinate-related enzyme."] The assay is "data not shown" and the text does not say whether a beta subunit was considered, so I weight it as supporting and not decisive on its own.
- The oxamate:CoA ligase proposal was also set aside: [PMID:34494882 "Thus, it appears that fdrA does not encode an oxamate:CoA ligase."]
- The partners are wrong for SCS. An SCS alpha subunit works with a beta subunit of PTHR11815 that binds the nucleotide. AllF functions with AllG (P77129) and AllH (P0AAS5) (untagged AllG co-eluted with His-tagged AllF and AllH), which are not in `interpro/panther/PTHR11815/PTHR11815-entries.csv`.
- E. coli has a dedicated SCS, SucCD (see `genes/ECOLI/sucD`).
- The allF operon is expressed anaerobically with allantoin, not under conditions of TCA-cycle activity (see Regulation).

### Complex

The three proteins were co-produced and purified together: [PMID:38888336 "The successful overproduction of 6×His-AllF (62 kDa), AllG (46 kDa), and AllH-6×His (31 kDa) was confirmed by SDS-PAGE"]. Untagged AllG came down with the tagged subunits.

The stoichiometry is assumed, not measured: [PMID:38888336 "the molecular mass of OXTCase was assumed to be 139 kDa, which was calculated considering it as a heterotrimer composed of three monomers"]. The authors say [PMID:38888336 "it is difficult to predict how many dimers or monomers (AllF)2, (AllG)2, or (AllH)1 form the OXTCase"]. The paper's formula for the complex, in the text and in Table 5, reads "[(AllF)2]x[(AllG)2]x[(AllG)]y"; the last term is probably meant to be AllH. I have not corrected it anywhere.

AllF dimer: [PMID:38888336 "Among these subunits, AllF has been determined to be a homodimer through crystallization structure analysis"]. This refers to PDB 3DMY, an unpublished structural-genomics deposit of residues 82-555 with no ligand. Substrate binding was only modelled by docking to each subunit separately. There is no mutagenesis and no site has been assigned to a subunit.

GO has no term for the oxamate carbamoyltransferase complex. QuickGO searches for "carbamoyltransferase complex" return only GO:0009347 aspartate carbamoyltransferase complex and its regulator term. Recorded as a proposed new term.

### Operon and regulation

- [PMID:38888336 "The three genes form an operon together with allK (ybcF), encoding catabolic carbamate kinase."]
- [PMID:36384810 "Reverse transcription PCR of total mRNA confirmed that the genes fdrA, ylbE, ylbF, and ybcF are co-transcribed."]
- [PMID:41016821 "High expression of the allF operon under anaerobiosis with allantoin requires the local regulator AllS and the global regulator ArcA."] and [PMID:41016821 "EMSA confirmed the direct binding of AllS and ArcA to the promoter of allF."]
- Aerobically the operon is essentially off: 15 and 19 Miller units of the allF-lacZ fusion aerobically, against 4,007 anaerobically with allantoin and 105 anaerobically with NH4Cl (PMID:41016821, Fig. 2 text).

### Distribution

[PMID:38888336 "Urease-negative enteric bacteria such as E. coli, Salmonella enterica, and Citrobacter freundii have homologous genes encoding OXTCase (AllF, AllG, and AllH) and carbamate kinase (AllK)"]. A metagenomic study reports allFGH and allK homologs in ammonia-oxidizing archaea and comammox bacteria [PMID:41081392 "oxamic transcarbamylase (allFGH), and catabolic carbamate kinase (allK)"]. That is a sequence-based annotation of metagenome-assembled genomes, with no assay.

### The name fdrA

[PMID:7500942 "One of the multicopy suppressor clones contained an N-terminally truncated version of a new gene that was designated fdrA."] The fragment suppressed the phenotypes of dominant-negative FtsH; [PMID:7500942 "The intact fdrA gene (11.9 min on the chromosome) directed the synthesis of a 60 kDa protein in vitro."] Abstract only. This is a multicopy effect of a truncated fragment. It has no GO annotation and should not generate one. It is the source of the Salmonella ortholog's name "Acyl-CoA synthetase, involved in protein transport".

### Swarming row (GO:0071973, IMP, PMID:17122336, EcoCyc 2012)

The cached paper is a Keio-collection screen. [PMID:17122336 "Of the 3,985 nonessential gene mutants, 294 were found to exhibit a strongly repressed-swarming phenotype."] and 216 of them had normal swimming; these are listed in Table 1. The cache has the full narrative but not the body of Table 1, and the strings fdrA, ylbD and b0518 do not occur in it. The PMC full text could not be retrieved (the PubMed MCP returned an empty full text; Europe PMC returned HTTP 500). I therefore could not read the row that the annotation rests on.

What can be said from the text that was read:

- The 78 mutants with a swimming defect are named one by one in the narrative, and fdrA is not among them. If the fdrA mutant is one of the 294 strongly repressed mutants it must be one of the 216 with normal swimming, a swarming-specific phenotype.
- A QuickGO query by reference (2026-11-18) returns 13 annotations from this paper. Twelve other genes (yqaA, yciG, preA, ybiA, yehP, ycdY, ymfA, ydcZ, yneE, yfgJ, pgrR, ydgA) carry GO:0071978 bacterial-type flagellum-dependent swarming motility. allF alone carries the parent GO:0071973. This is a lead for a query to EcoCyc, not proof of an error.
- The screen used LB swarm plates with glucose (0.6% agar, wrapped, 33 C; aeration is not stated in the methods) and single-gene deletions without complementation. The authors note that polar effects may inflate the list. The allF-lacZ fusion is barely expressed aerobically in liquid minimal medium (above); expression on the swarm plates was not measured.

Action: UNDECIDED, because the table was not read.

### PANTHER tree placement (PTHR11117, release 19 treeinfo service, read 2026-11-18)

Path from the root to AllF: PTN008961318 (root, 189 leaves) > PTN000122012 (LUCA, 187) > PTN008512606 (Eubacteria, 181) > PTN004231559 (horizontal transfer, 166) > PTN000122099 (Proteobacteria, 16) > PTN000122102 (Gammaproteobacteria, 13) > PTN008512624 (duplication, 6) > PTN001671414 (Enterobacteriaceae, 3 leaves, SF24, branch length 1.587) > PTN000122104 (duplication, 2) > leaf PTN001290262 (Q47208, branch 0.102; PANTHER still calls it "Protein FdrA").

- The sister of PTN001671414 under the duplication PTN008512624 is PTN001671427 (Enterobacteriaceae, 3 leaves: Salmonella Q8ZQU0, Yersinia pestis A0A5P8YEE8 and E. coli SucD P0AGE9; branch length 0.116). The tree therefore draws SF24 as an enterobacterial duplicate of SucD on a branch more than ten times longer than its sister's.
- Inside SF24, Salmonella Q8ZR75 (PTN001671415, branch 0.103) is outside the duplication PTN000122104 that joins YahF P77187 (PTN000122105, branch 0.859) and AllF.
- The node ids PTN008512624, PTN001671427, PTN000122104, PTN000122099, PTN000122102, PTN001290262, PTN001671415 and PTN000122105 are not in `genes/yeast/LSC2/LSC2-bioinformatics/results.yaml` or the family review.

Pairwise alignments (Biopython PairwiseAligner, BLOSUM62, gap open 11, extend 1; run on 2026-11-18, not stored as a committed analysis):

- AllF against Salmonella Q8ZR75, global: 460 identical of 554 aligned pairs.
- AllF against YahF P77187, global: 200 identical of 493 aligned pairs.
- AllF against E. coli SucD P0AGE9, local: AllF 118-290 against SucD 66-238, 37 identical of 169 aligned pairs. The alignment ends before the SucD phosphohistidine loop (GHAGA, His247 of the precursor numbering). Whether AllF keeps an equivalent histidine is unresolved; the sequence GHAGA does not occur in AllF, YahF or Q8ZR75, but a motif search is not an alignment and proves nothing either way.

Reading: Salmonella Q8ZR75 is the close counterpart of AllF (83% identity) and YahF is the divergent paralog. That fits the branch lengths but not the drawn order of events inside SF24 (a Salmonella leaf outside an E. coli YahF + AllF duplication). The placement of SF24 as a recent enterobacterial duplicate of SucD is also doubtful given the very long branch, the extra N-terminal domain (Pfam PF27530, residues 1-98, absent from SucD) and the report of allFGH homologs outside Enterobacteriaceae (PMID:41081392). None of this was tested by a phylogenetic analysis here.

### IBA rows

- GO:0004775, GO:0004776, GO:0006099 and GO:0009361 come from the LUCA node PTN000122012. The node placement is right for succinyl-CoA synthetase alpha subunits; the problem is that the SF24 clade descends from it. Action REMOVE, with a source defect asking for a loss at PTN001671414. This agrees with `interpro/panther/PTHR11117/PTHR11117-review.yaml`, which marks all four NEEDS_PRUNING with SF24 as a branch to prune. The experimental evidence is for AllF only; extending the loss to YahF and Q8ZR75 is an inference from clade membership (strong for Q8ZR75 at 83% identity, weaker for YahF).
- GO:0005829 cytosol comes from the SF24 node PTN001671414, seeded by YahF (P77187), whose EcoCyc IDA cites PMID:17309111. That paper is an analysis of the inner-membrane fraction [PMID:17309111 "to dissolve and analyze the inner membrane fraction of an Escherichia coli K12 cell lysate were compared"], cached as abstract only; how it supports a cytosol annotation for YahF could not be checked. For AllF the term rests on indirect grounds: UniProt records no signal peptide and no transmembrane segment, the recombinant complex is recovered from the supernatant of a cleared lysate [PMID:38888336 "Cell debris was removed by centrifugation (13,000 rpm, 4°C, 20 min), and the supernatant was collected"] (the lysis buffer contained 0.5% Triton X-100, so this does not exclude membrane association), and its substrates and partner enzymes are cytoplasmic. Accepted. Cytosol is not one of the five root organelle terms, so the organelle policy does not apply.

### Other rows

- GO:0003824 catalytic activity (InterPro IPR005811): TOO_GENERAL, as in the eleven succinyl-CoA synthetase subunit reviews. The signature supports nothing deeper, so MODIFY is not available.
- GO:0050205 `enables` IEA from the EC number: the term is right; the qualifier is stronger than the evidence, since AllF alone is inactive. Accepted for consistency with the IDA row and noted in the reason.

### Open questions for the bench

1. Which subunit holds the active site, and what each of AllF, AllG and AllH contributes.
2. Whether AllF keeps any of the chemistry of its succinyl-CoA synthetase alpha ancestry (a phosphohistidine intermediate, CoA binding). The assay needs no CoA, but a phosphoenzyme was not tested.
3. Stoichiometry and architecture of the complex.
4. How D296Y increases oxamate production.
5. How a truncated FdrA fragment suppresses dominant-negative FtsH.

Not knowledge gaps, recorded here as curation notes: the subcellular location has not been measured (a fractionation would settle it); YahF and Salmonella Q8ZR75 have no review; the family review's UNRESOLVED verdict for the cytosol IBD at PTN001671414 can now cite this review.

## 2026-11-22: what informatics does and does not settle about the catalytic histidine

Two OpenScientist reports were run on the open questions (provider output, not edited, not literature):
`allF-hypotheses/carbamoyltransferase-site-not-in-allf/openscientist.md` (run 1) and
`allF-hypotheses/sca-alpha-phosphohistidine-retained/openscientist.md` (run 2). They disagree on which AllF
residue stands at the SucD catalytic histidine (His247 in UniProt P0AGE9 numbering, His246 in the crystal
structures): run 1 says Val293, run 2 says Gln467. Three independent checks (sequence, structure, family) were
made of their claims, and the reproducible parts are now a committed analysis,
`allF-bioinformatics/catalytic_his_mapping.py` with `results.yaml` and `RESULTS.md`, which I re-ran twice on
2026-11-22 with identical output. This supersedes the 2026-11-18 statement above that "Whether AllF keeps an
equivalent histidine is unresolved".

Established (file:ECOLI/allF/allF-bioinformatics/RESULTS.md):

- AllF has no histidine at the catalytic position. [file:ECOLI/allF/allF-bioinformatics/RESULTS.md "AllF has no histidine at the position of the SucD catalytic histidine."]
- Run 1's Val293 is wrong. Residue 293 is valine, but it lies outside the PF00549 domain and 26 A from the superposed histidine.
- Run 2's Gln467 is what the Pfam PF00549 profile gives (column 102; Gln466 in Salmonella FdrA, Gln483 in YahF), but it is not the structural equivalent. On PDB 3DMY the SucD segment 242-251 has no AllF counterpart; AllF 462-476 pairs with SucD 257-271, and Gln467 superposes on SucD Lys262, 18 A from the histidine. The loop is absent, not substituted GHAGA to QQIAT.
- The checks did not agree with each other at first: the sequence and family checks confirmed Gln467 from the profile and said they had not looked at a structure; the structure check refuted it. Both are reproduced in the script. I follow the structure for the question "which residue is there", and report the profile column as a profile column. One of several unstable pairwise alignments in the sequence check paired SucD ALEAAGV with AllF LEDAGI, which is the register the superposition gives for that segment; that alignment put His247 on Tyr449 and is not evidence for either mapping. The superposition uses one program (tmtools TM-align) and one AllF structure.
- AllF has two SucD-like lobes (174-299, 300-502). The histidine loop is missing from both. Met391 fills the place of the histidine side chain in lobe 2; His389, in an insert that SucD lacks, is the nearest histidine (closest atom 4.5-5.0 A, CA 9.0-9.4 A, in the frame where the SucD C-terminal domain is superposed on lobe 2; 9.5-9.8 A and 15.1-15.4 A in the dimer frame, where lobe 1 of the other chain takes the alpha role). Within a chain its side chain is 3.2-3.4 A from the Thr338 carbonyl oxygen and 5.3-6.2 A from the Gly339 and Gly340 backbone nitrogens, the N-terminus of the lobe 2 phosphate-binding helix.
- The N-terminus of the phosphate-binding helix is kept in both lobes (Ser202-Gly203-Thr204; Gly339-Gly340-Thr341).
- In the 3DMY dimer, lobe 1 of one chain with lobe 2 of the other resembles the alpha-C plus beta-C pair of succinyl-CoA synthetase; the two lobes of one chain do not.
- All 53 reviewed succinyl-CoA synthetase alpha entries (IPR005810) have histidine at the profile column. Of 951 AllF-family entries (IPR061301), 764 have glutamine and 7 have histidine (not in a GHAGA context; not examined further). The G[KR]PHPM motif of His389 is in 884 of 951 and in none of the 53.
- 150 UniProtKB entries carry the AllG domain with the AllF CoA-ligase domain in one chain (848-1039 residues); one carries AllG with AllH. Run 1's counts reproduce exactly.

Established with a limit: CoA carried rigidly from SucD into 3DMY clashes (14-16 of 48 atoms within 2.2 A), and the Rossmann-like domain of AllF has a permuted chain order. That is a blocked pose in a ligand-free crystal, not proof that CoA cannot bind.

Not established by any of this, and still for the bench: whether any phosphoenzyme or carbamoyl-enzyme forms; which subunit binds carbamoyl phosphate, oxamate and magnesium; whether His389 or the helix N-termini do anything; where AllG and AllH sit; the stoichiometry. Nothing here bears on the FtsH-suppression question.

Leads from the reports that were not checked and are not in the review:

- Run 1: Foldseek finds no carbamoyltransferase or carbamate kinase fold in AllG or AllH; an invariant D170-D171 loop in AllH as a metal or anion site; STRING fusion score 0.899 for AllF-AllG; "PF02629 phosphate loop intact" in AllF.
- Run 2: individual CoA-contact substitutions in AllF; conservation percentages of the helix residues (from 125 sequences); Gln467 as a substrate contact. Run 2 itself labels the His389 model a lead.

Decisions:

- The four REMOVE rows keep their action and gain the residue-level reason, two quotes from the analysis and a `residue_claims` entry (LOST, anchor SucD His247, no target because nothing in AllF corresponds). The four GO_CENTRAL defects mention it, with YahF and Q8ZR75 glutamine at the profile column as clade-level support.
- Knowledge gaps narrowed, none closed. The phosphohistidine question is now "is there any covalent intermediate, and does the inherited scaffold bind a ligand".
- Suggested experiments: His389 and Thr341 variants (with Ser202 and Thr204), and assay of a natural AllG-AllF fusion. I did not add Gln467 mutagenesis: by superposition it is 16-18 A from the site, and its conservation at a profile column whose register is off in this family is not a reason to mutate it. I did not add AllH loop mutagenesis: that lead was not checked.
- The wrong statements in the reports are recorded as `finding_review` on the reference entries (OVERTURNED for Val293, DISPUTED for the GHAGA to QQIAT reading) and in `review_notes`. `source_defects` was not used: there is no upstream record of a one-off run to correct.
- PTHR11117 family review: the SF24 sentence "Whether the phosphohistidine chemistry ... is not known" was replaced by the residue-level result.

2026-11-24, after PR review: the statement that His389 is the nearest histidine to the position of the SucD catalytic histidine had not been computed. The script now measures every histidine of both chains of 3DMY in both frames (RESULTS.md result 7). It holds: in the lobe 2 frame His389 is 4.5-5.0 A away by closest atom and the next histidine (His364) is 15.3-15.6 A; in the dimer frame His389 of the other chain is nearest by closest atom (9.5-9.8 A against 11.8-12.0 A for His362), though His362 is nearer by CA.
