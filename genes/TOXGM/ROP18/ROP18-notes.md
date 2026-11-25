# ROP18 (Toxoplasma gondii ME49, TGME49_205250, A0A125YQL1) — curation notes

**Note on provenance of these notes:** automated deep research was *not* available in this
environment (Falcon authentication failed; OpenAI key invalid). No `*-deep-research-*.md`
file was generated. What follows is a **manual literature review** done by reading the
UniProt record, the cached publications in `publications/`, and primary papers fetched with
`ai-gene-review fetch-pmid`. Every assertion below carries an inline citation with a
verbatim quote from a cached source.

## 1. Sequence record and what it does/doesn't say

- UniProt A0A125YQL1 is a TrEMBL entry for the ME49 (type II) allele, annotated only by
  homology: `PE   3: Inferred from homology`, `DE   RecName: Full=Serine/threonine-protein`,
  `EC=2.7.11.1`, protein kinase domain 252–531, ATP-binding residue 281, active-site
  (proton acceptor) residue 409 [file:TOXGM/ROP18/ROP18-uniprot.txt "SIMILARITY: Belongs to the protein kinase superfamily. Ser/Thr protein"].
- The record carries a Phobius-predicted transmembrane helix at 21–40
  [file:TOXGM/ROP18/ROP18-uniprot.txt "Membrane {ECO:0000256|SAM:Phobius}"]. This is the
  N-terminal signal peptide/pro-region of a rhoptry protein, not a bona fide membrane anchor;
  the literature on the ROP2 family explicitly rules out the transmembrane interpretation of
  the conserved hydrophobic stretch [PMID:17305424 "Our recent sequence analysis of all ROP2 family sequences has led us to rule out the transmembrane prediction for this conserved segment [12]."].
- PANTHER places the protein in PTHR44167 ("OVARIAN-SPECIFIC SERINE/THREONINE-PROTEIN KINASE
  LOK-RELATED"), i.e. an animal STE20/LOK-like family. This is the source of the TreeGrafter
  IEAs for `nucleus` and `mitotic DNA damage checkpoint signaling`, which are metazoan
  functions with no counterpart in a secreted apicomplexan rhoptry kinase (see §5).

## 2. ROP18 is a rhoptry kinase secreted onto the parasitophorous vacuole membrane

- ROP18 belongs to the ROP2 family of rhoptry bulb proteins and relocalises to the PVM during
  invasion [PMID:17305424 "We show here that ROP18, a member of the ROP2 family, is located in the rhoptries and re-localises at the parasitophorous vacuole membrane during invasion."].
- The protein is a genuinely active kinase discharged at the host–parasite interface
  [PMID:17305424 "We therefore demonstrate that rhoptries can discharge active kinases at the parasite–host cell interface upon cell invasion."].
- Overexpression increases intravacuolar replication, and this depends on catalytic activity
  [PMID:17305424 "In addition, overexpression of ROP18 in tachyzoites led to a dramatic stimulating effect on intracellular parasite multiplication, strongly suggesting that this protein plays a role in the control of parasite proliferation and may therefore be involved in T."].
- After secretion the protein is tethered to the cytosolic face of the PVM
  [PMID:22906355 "Following secretion into the host cell, ROP18 traffics to the parasitophorous vacuole membrane (PVM) where it is tethered to the cytosolic face of this host-pathogen interface."],
  via an arginine-rich amphipathic helical region upstream of the kinase domain
  [PMID:22906355 "In this report, we show that ROP18 mutants altered in an arginine-rich domain upstream of the kinase domain fail to associate to the PVM following secretion from rhoptries."].
- PVM targeting is *functionally required*: targeting mutants retain intrinsic kinase activity
  but cannot phosphorylate host substrates or confer virulence
  [PMID:22906355 "Vacuole-targeting mutants of ROP18 failed to phosphorylate Irga6 and were unable to divert IRGs from the PVM, despite retaining intrinsic kinase activity. As a consequence, these mutants were avirulent in a mouse model of acute toxoplasmosis."].

## 3. Virulence factor identified by genetic mapping

- ROP18 was positionally cloned as a type I acute-virulence QTL and is secreted into the host
  cell during invasion; the phenotype requires kinase activity
  [PMID:17170305 "Positional cloning identified the candidate virulence gene ROP18, a highly polymorphic serine-threonine kinase that was secreted into the host cell during parasite invasion."],
  [PMID:17170305 "These attributes of ROP18 required kinase activity, which revealed that secretion of effectors is a major component of parasite virulence."].
- The companion mapping study framed ROP kinases generally as key virulence factors
  [PMID:17170306 "Polymorphic secreted kinases are key virulence factors in toxoplasmosis."].

## 4. Molecular mechanism: phosphorylation of host IFN-inducible GTPases (IRGs)

- ROP18 binds and phosphorylates host immunity-related GTPases, blocking the IRG-dependent
  clearance machinery
  [PMID:21147463 "Consistent with this, expression of ROP18 was both necessary and sufficient to block recruitment of Irgb6, which was in turn required for parasite destruction."].
- The reaction is a direct, catalysis-dependent phospho-transfer; kinase-dead protein traps the
  substrate
  [PMID:21147463 "When ROP18 and Irgb6 were each separately immunoprecipitated and incubated in vitro in a hot kinase reaction, both auto-phosphorylation of several forms of ROP18 and labeling of Irgb6 were readily detected by the active ROP18 but not the kinase-dead form (Figure 4B)."],
  [PMID:21147463 "The strength of this interaction was increased by 3-fold, as shown by phosphorimager analysis, in parasites expressing the kinase-dead ROP18 D/A (Figure 4A), consistent with it being trapped with its substrate when unable to complete the phospho-transfer reaction."].
- The modified residues are **threonines** in switch region I of the GTPase domain
  [PMID:21203588 "We show that the parasite kinase phosphorylates host Irga6 at two threonines in the nucleotide-binding domain, biochemically inactivating the GTPase and inhibiting its accumulation and action at the T."],
  [PMID:21203588 "We show here that the ROP18 kinase from highly virulent strains targets Irga6, phosphorylating two threonines in the switch I loop."]
  — i.e. Thr102 and Thr108 [PMID:22906355 "To determine if Irga6 accumulation was associated with an inability to phosphorylate this substrate, we took advantage of previously characterized antibodies that recognize the phosphorylated Thr102 and Thr108 residues that are targeted by ROP18 (Steinfeldt et al., 2010a)."].
  This matters for GO: the RHEA-derived IEA asserts *serine* kinase activity, whereas the
  direct experimental substrate chemistry is threonine phosphorylation; the correct term is
  the dual `protein serine/threonine kinase activity`.
- ROP18 acts as part of a complex with the pseudokinase ROP5 and the dense granule protein GRA7
  [PMID:26247512 "In this study, we confirmed the dense granule protein GRA7 as an additional component of the ROP5/ROP18 kinase complex and identified GRA7 association with the PVM by direct binding to ROP5."],
  and ROP5 allele identity gates ROP18 function
  [PMID:22761577 "Here we report that ROP18 can only inhibit accumulation of the IRGs on the PVM of strains that also express virulent ROP5 alleles."].
- Substrate scope among IRGs is narrower than first thought
  [PMID:26247512 "We show that the only specific target of ROP18 among IRG proteins is in fact Irga6."].

## 5. A second host target: ER-bound ATF6β

- A yeast two-hybrid screen with the N-terminal extension identified host ATF6β
  [PMID:21670204 "In this study, we show that ROP18 targets the host endoplasmic reticulum-bound transcription factor ATF6β. Disruption of the ROP18 gene severely impairs acute toxoplasmosis by the type I RH strain."],
  and the kinase activity is required for its destruction
  [PMID:21670204 "The kinase activity of ROP18 is essential for proteasome-dependent degradation of ATF6β and for parasite virulence."],
  [PMID:21670204 "The N-terminal extension of ROP18 contributes to ATF6β-dependent pathogenicity by interacting with ATF6β and destabilizing it."].
  Direct phosphorylation of ATF6β by ROP18 is *not* demonstrated in that paper (the effect is
  attributed to binding plus kinase-dependent proteasomal degradation), so no substrate-specific
  MF term is warranted for this interaction.

## 6. Strain / host context relevant to the ME49 entry being reviewed

- The entry under review is the **type II ME49** allele. Type II ROP18 is expressed and is an
  active, functional allele
  [PMID:22761577 "ROP18 is highly expressed in types I and II strains but an insertion in the promoter prevents expression in type III strains."],
  [PMID:22761577 "Indeed, transgenic expression in the type III strain CEP of either ROP18I or ROP18II decreased the average number of vacuoles coated with Irgb6 from 45% to 23% (P = 0.001) for ROP18I or 29% (P = 0.003) for ROP18II (Figure 1B)."].
  The reduced acute virulence of type II strains comes from the ROP5 allele context, not from
  loss of ROP18 function
  [PMID:22761577 "This suggests that either ROP18 cannot function independently of ROP5, or that ROP18 is inhibited in the type II background."].
  So the IRG-evasion function is appropriate to annotate to the ME49 protein, while the extreme
  acute-virulence phenotype is a type I property.
- The IRG arm of the mechanism is **mouse-specific**; humans lack the expanded IRG family
  [PMID:22761577 "However, neither ROP18 nor ROP5 markedly affect survival in IFNγ-activated human cells, which lack the multitude of IRGs present in murine cells."].
  GO process terms should therefore be the generic symbiont/host terms, not anything implying a
  universal host range.

## 7. Curation calls arising from the above

- `GO:0004674 protein serine/threonine kinase activity` — core; experimentally supported
  (autophosphorylation, Irga6/Irgb6 phosphorylation, kinase-dead controls).
- `GO:0106310 protein serine kinase activity` (RHEA IEA) — the characterized chemistry is
  threonine phosphorylation in Irga6 switch I, so the serine-only child is the wrong level;
  MODIFY to `GO:0004674`.
- `GO:0005524 ATP binding` — accept (kinase with annotated ATP-binding residue).
- `GO:0000166`, `GO:0004672`, `GO:0016301`, `GO:0016740` — true but entailed by `GO:0004674`
  / `GO:0005524`: TOO_GENERAL.
- `GO:0005634 nucleus` (TreeGrafter, PTHR44167) — wrong compartment. ROP18 is a rhoptry protein
  secreted onto the cytosolic face of the PVM; the term comes from metazoan LOK/STK20-family
  grafting. REMOVE.
- `GO:0044773 mitotic DNA damage checkpoint signaling` (TreeGrafter) — a metazoan checkpoint
  function with no support in any ROP18 study; the protein is an exported effector, not a
  nuclear checkpoint kinase. REMOVE.
- Missing from GOA and proposed as NEW: `GO:0020008 rhoptry`,
  `GO:0020005 symbiont-containing vacuole membrane` (the GO term used for the T. gondii PVM;
  cf. MAF1b1 A0A140H546 annotated IDA to GO:0020005 in QuickGO),
  `GO:0052170 symbiont-mediated suppression of host innate immune response`.
