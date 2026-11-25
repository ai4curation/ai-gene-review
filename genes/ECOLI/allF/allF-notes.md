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
