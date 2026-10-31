# smad3b notes (Danio rerio, SMAD family member 3b; UniProt Q8AY16)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 3, random sample)

**Deep research:** not available for this gene (Edison/Falcon returned 402 Payment Required;
the OpenAI key is invalid). Not attempted, per instructions. No `-deep-research-*.md` file
exists. The literature search was done by hand (Europe PMC; same queries as in
`../smad3a/smad3a-notes.md`).

Accession: Q8AY16 (TrEMBL, 423 aa) holds all 19 GOA rows. Its only experimental row is the
Tob1a protein-binding IPI (PMID:16890162). Paralog: smad3a (Q8AY15). Human ortholog SMAD3.
The sequence analysis is shared with smad3a: `../smad3a/smad3a-bioinformatics/RESULTS.md`.

### TGD origin
See smad3a notes. PANTHER `TGD_tree`; synteny and phylogeny in PMID:27703851
[PMID:27703851 "confirmed that smad3a/3b most likely originated from the teleost-specific WGD"].

### Protein
- smad3b vs human SMAD3 93.0%, vs gar SMAD3 93.9%, vs smad3a 94.1%.
- Differences concentrate in the linker (82.3% identical to human, vs 92.7% for smad3a); 2-aa
  linker deletion; S418 (CK1 phosphosite in human) is N. Zn site, K40/K41, T179/S204/S208/S213
  and the SSVS motif are conserved.
- Faster evolution and linker positive selection in teleost smad3b
  [PMID:27703851 "Moreover, the branch length of smad3b cluster was longer than smad3a"]
  [PMID:27703851 "Five candidate positive selected sites were identified, two of which were significantly positively selected (219L**, 221L**, posterior probability > 0.99) in smad3b."]
  (These positions are in flounder numbering; I did not map them to zebrafish.)

### Expression
- First described, with expression and overexpression activity, by Pogoda and Meyer 2002
  [PMID:12112463 "Here, we describe cloning, expression pattern, transcriptional regulation, and functional properties of two novel zebrafish Smad proteins: the TGF-beta agonist Smad3b, and the anti-Smad Smad7."]
- ZFIN rows from that paper: maternal; gastrula margin; lateral mesoderm; tail bud; brain
  regions (diencephalon, epithalamus, pretectum, tegmentum, midbrain, hindbrain, rhombomeres);
  retina; spinal cord; somites (smad3a-bioinformatics/output.txt).
- Whole-embryo expression, strongest in eyes and tail at somitogenesis
  [PMID:21159776 "smad3b expressed in the whole embryonic body but with stronger expression in eyes and tail ( supplemental Fig."]
- Not circadian [PMID:29940038 "In contrast to Smad3a, another zebrafish paralog of Smad3, Smad3b, did not show any time- or light-dependent expression pattern"]
- Bgee top entities: heart, muscle tissue, pharyngeal gill, eye, liver.

### Function
- Overexpression induces mesoderm and organizer genes
  [PMID:12112463 "We show that zebrafish Smad3b, in contrast to the related zebrafish Smad2, can induce mesoderm independently of TGF-beta signaling."]
  [PMID:12112463 "Although mammalian Smad3 was shown to inhibit expression of the organizer-specific genes goosecoid, zebrafish smad3b activates organizer genes such as goosecoid."]
- Weaker than smad3a on myf5 [PMID:21159776 "Although the ability of Smad2 and Smad3a to activate the myf5 promoter requires Smad4 to form a complex and enter the nucleus, Smad3b only plays a minor role in myf5 promoter activation."]
- caSmad3b raises cardiomyocyte proliferation (31%, vs 70% for caSmad3a)
  [PMID:29196619 "whereas both caSmad3a and caSmad3b expression resulted in a 70% (±18% s.e.m.) and 31% (±12% s.e.m.) increase in EdU incorporation, respectively"]
- DN-Smad3b used as a general Smad2/3 blocker in neural induction and cell-competition work
  [PMID:19580801 "by injecting dnsmad3b mRNA encoding a dominant negative Smad3b mutant, inhibits the expression of the early neural markers sox2 and sox3 at the onset of gastrulation"]
  [PMID:39690179 "Inhibiting TGF-β-type Smad signalling by co-expression of Smad3b dominant-negative mutants (Smad3bDN) in unfit cells or injecting smad4a MO37 reduced the apoptosis of unfit cells (Fig."]
  These dominant-negative results show what Smad2/3 signalling does, not what smad3b specifically does.
- Knockdown alters neural differentiation (as for smad3a) [PMID:25286120 "Similarly, smad3a and 3b knock-down alter neural differentiation showing that both paralogues play a positive role in neural differentiation."]
- Double knockout with smad3a: see smad3a notes (PMID:42584512, PMID:40066353).

### Annotation decisions
- All IBA/IEA rows reviewed with the same actions as the matching smad3a rows (conserved protein,
  same PAINT nodes). Protein binding (Tob1a IPI) removed as uninformative on both copies.
- No smad3b-specific experimental process annotation exists in GOA. None was added: the
  overexpression and dominant-negative data act on Smad2/3 signalling generally.
