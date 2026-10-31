# Cgl2304 (cg2530, NCgl2222; Q8NNA0) notes

## Provenance

- LBNL hackathon alpha-glucan batch, 2026-10-30. Dashboard gene NZ_CP025533.1_2296
  (KBase gene-annotate dashboard). Its sequence is identical over the full 363 aa to UniParc
  UPI000003653B, i.e. Q8NNA0 (C. glutamicum ATCC 13032, UP000000582).
- Fetched with `just fetch-gene CORGL Q8NNA0 --alias Cgl2304`. GOA for Q8NNA0 is empty.
- Deep research: falcon and perplexity are unavailable (no API keys), so
  `just deep-research-claude-code CORGL Q8NNA0 --alias Cgl2304` was used.
- No C. glutamicum Fitness Browser (FEBA) data was looked for; `fetch-fitness` returns 403.
- BERIL runs, from `projects/hackathon/`:
  - `20261030T233147Z-cgl2304-mak-comparison` (`Cgl2304-bioinformatics/mak_comparison.py`)
  - `20261030T233251Z-cgl2304-genome-context` (`Cgl2304-bioinformatics/genome_context.py`)

## Dashboard call

"Protein kinase-like family protein associated with trehalose and alpha-glucan metabolism."
(tier B). The page drew no GO terms from it. The trace rejected maltose kinase activity because
"the 100%-identical cg2530 homolog is explicitly uncharacterized". The model's only literature
evidence was a PaperBLAST snippet cut just before the words "maltose kinase". The dashboard's
own "Known before" panel lists eggNOG gene mak, EC 2.7.1.175 and KEGG K16146 maltokinase.

**Verdict: under-called.** Everything the call says is true, but the evidence supports a
specific function, maltokinase (EC 2.7.1.175).

Suggested correction text:

> Maltokinase (Mak/Pep2; maltose + ATP -> maltose 1-phosphate, EC 2.7.1.175), probable, of the
> TreS-Mak-GlgE-GlgB alpha-glucan pathway; encoded downstream of and translationally coupled
> to treS; lacks the Mak N-terminal cap subdomain.

## Evidence

1. **Homology.** Cgl2304 is 40-44% identical over 91-99% of its length to six characterised
   maltokinases [file:CORGL/Cgl2304/Cgl2304-bioinformatics/RESULTS.md "Cgl2304 is about 40-44%
   identical to all six characterised maltokinases over 91-99% of its length."]:
   - Mvan A1TH50: 43.5%
   - Mtb O07177 and M. bovis Q7U2S7: 42.9%
   - M. smegmatis A0R6D9: 39.5%
   - Actinoplanes Q7WUM3: 42.0%
   - S. coelicolor Pep2A Q7AKG7: 40.7%

   C. glutamicum TreS, as a control, is 28.7% identical.
2. **Catalytic residues are conserved** (mapped onto the M. vanbaalenii Mak structure;
   PMID:25619172 "the catalytic loop (303HGD305) and the 322DFE324 motif that contain the
   putative catalytic base (Asp305) and the magnesium-binding Asp322, respectively"):
   - P-loop: E89, Q90, S91, N92
   - ATP lysine: K105
   - catalytic loop HGDLHLGQ at 246-253, identical in all six references
   - DFE motif: D265, F266, E267
   - R277
   - maltose-binding triad: K335, Y338, Y342

   All four residues mutated in Mtb Mak are conserved, including D339 (D339N is inactive),
   which maps to Asp265. The only change is Arg342 to Lys285.
3. **Brenner motif.** The strict HxDxxxxN pattern matches none of the seven maltokinase
   sequences. Maltokinases put a Gln (Mg1 ligand Gln310) where the Asn would be, and the query
   has the equivalent Gln253. This is a family feature, not a defect.
4. **N-terminal cap subdomain.** The Pfam Mak_N_cap HMM (PF18085) hits all six references but
   not Cgl2304, and the first ~88 query residues align only patchily to the cap. This accounts
   for the length difference: 363 aa versus 437-464 aa for the references. The cap is
   cystatin-like and is proposed to regulate the enzyme and dock it onto TreS (PMID:25619172).
   Its loss could change regulation; this has not been tested.
5. **The gene model is not truncated.**
   - The reading frame runs only 5 codons upstream of the ATG before an in-frame stop.
   - treS (NCgl2221, same strand) ends 4 nt inside the Cgl2304 start, an ATGA
     translational-coupling overlap.
   - Corynebacterial orthologs are all short: C. efficiens 362 aa, C. callunae 365 aa,
     C. durum 361 aa. All 25 Corynebacterium COG3281 entries in UniProt are 400 aa or shorter.
6. **Pathway context.**
   - treS (cg2529) is immediately upstream, the same contiguous arrangement as in mycobacteria
     (PMID:25619172 "In mycobacteria, Mak and TreS are independent enzymes encoded, with very
     few exceptions, by contiguous genes").
   - The genome encodes GlgE (cg1382, Q8NR39) and GlgB (cg1381, Q8NR40).
   - The pathway from trehalose to alpha-glucan was defined by Kalscheuer et al.
     (PMID:20305657).
7. **C. glutamicum literature.**
   - Woo et al. 2010 (PMID:20802079) is the only peer-reviewed mention. It reports homology
     only, citing unpublished data: "maltose formed from trehalose by TreS is incorporated into
     glycogen by the consecutive action of the maltose kinase Pep1 and the maltosyltransferase
     GlgE ... Genes encoding homologs of Pep1 (cg2530) and GlgE (cg1382) were also identified
     in C. glutamicum".
   - **Naming confusion.** The mycobacterial maltokinase is Pep2 (Rv0127; PMID:20305657,
     PMID:15378530). In S. coelicolor, pep1A/pep1B are glgE1/glgE2 (UniProt Q9L1K2, Q9KY04). Woo
     et al.'s "maltose kinase Pep1" is a naming slip, but it means the maltokinase.
   - Henrich, PhD thesis, Universität zu Köln, 2011
     (https://kups.ub.uni-koeln.de/4163/1/Dissertation_Alexander_Henrich.pdf, section 3.3.3). I
     checked these quotes against the PDF text myself:
     - The thesis names cg2530 "treX" and reports 37% identity to pep2 (rv0127).
     - An insertion in cg2530 in a ΔmalQ background abolished growth on trehalose: "C.
       glutamicum ΔmalQ IM treX did not seem to be able to utilize trehalose for growth". The
       same strain also failed to use maltose (final OD 22 versus 36 for wild type).
     - The insertion alone had no phenotype on glucose plus trehalose.
     - The thesis concludes that the earlier ΔtreS deletion was polar on cg2530.
     - Caveats: the thesis is not peer reviewed; the evidence is genetic only; and "treX" here
       is not the GH13 TreX debranching enzyme.
     - The thesis name "treX" is deliberately not carried as an alias in the review YAML.
       TreX/GlgX is the established name of the GH13 glycogen debranching enzyme in this same
       trehalose/alpha-glucan pathway, and aliases are machine-readable (PR #5763 review).
   - Wolf et al. 2003 (PMID:12890033) and Tzvetkov et al. 2003 (PMID:12855718) characterise
     treS and the trehalose and glycogen routes but do not study cg2530.

## Annotation decisions

GOA is empty, so all rows are NEW, with ISS evidence.

- **GO:0019200 carbohydrate kinase activity.** GO has no maltokinase activity term, so a
  "maltokinase activity" term is proposed under proposed_new_terms, with parent GO:0019200.
  RHEA:31915 / EC 2.7.1.175 match no GO term in the local GO database or QuickGO search.
- **GO:0046835 carbohydrate phosphorylation.** This is the direct process; the Actinoplanes
  Mak1 carries it by IDA.
- **GO:0030979 alpha-glucan biosynthetic process.**
  - Chosen over GO:0005978 glycogen biosynthetic process, which is not a subclass of
    GO:0030979 in GO.
  - GlgE-pathway flux to glycogen is unproven in C. glutamicum, where glycogen is also made by
    GlgC/GlgA.
  - Comparators: Mtb and M. smegmatis GlgE carry GO:0030979 (IEA); reviewed mycobacterial Mak
    proteins carry GO:0005978 (IEA).
- **Not added.**
  - Trehalose catabolic process: Mak acts on maltose, and TreS does the trehalose step.
  - Cytoplasm: one line of evidence only (DeepTMHMM globular, no signal peptide).
- **Names to fix upstream.** The RefSeq product name "trehalose synthase" for WP_011015024.1 and
  the UniProt submitter name "probably involved in trehalose biosynthesis" come from the COG3281
  label ("Predicted trehalose synthase"). They are wrong for this protein, which is the kinase,
  not TreS.

## QC

- `just validate CORGL Cgl2304`: passed.
- `just validate-references`: passed (0 issues).
- `just validate-terms`: passed.
- `just render`: passed.
- `just validate-predictions` on `Cgl2304-dashboard-predictions-review.yaml`: 0 errors,
  0 warnings.
