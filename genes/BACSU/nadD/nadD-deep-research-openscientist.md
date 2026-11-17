---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-12T05:20:42.263169'
end_time: '2026-11-12T05:31:23.568007'
duration_seconds: 641.3
template_file: templates/gene_research_go_focused.md
template_variables:
  organism: BACSU
  gene_id: P54455
  gene_symbol: nadD
  uniprot_accession: P54455
  protein_description: 'RecName: Full=Nicotinate-nucleotide adenylyltransferase; EC=2.7.7.18;
    AltName: Full=Deamido-NAD(+) diphosphorylase; AltName: Full=Deamido-NAD(+) pyrophosphorylase;
    AltName: Full=Nicotinate mononucleotide adenylyltransferase; Short=NaMN adenylyltransferase;'
  gene_info: Name=nadD; Synonyms=yqeJ; OrderedLocusNames=BSU25640;
  organism_full: Bacillus subtilis (strain 168).
  protein_family: Belongs to the NadD family. .
  protein_domains: Cyt_trans-like. (IPR004821); NadD/NMNAT. (IPR005248); Rossmann-like_a/b/a_fold.
    (IPR014729); CTP_transf_like (PF01467)
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 9
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: nadD-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: nadD-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Gene Research for Functional Annotation

## ⚠️ CRITICAL: Gene/Protein Identification Context

**BEFORE YOU BEGIN RESEARCH:** You MUST verify you are researching the CORRECT gene/protein. Gene symbols can be ambiguous, especially for less well-characterized genes from non-model organisms.

### Target Gene/Protein Identity (from UniProt):
- **UniProt Accession:** P54455
- **Protein Description:** RecName: Full=Nicotinate-nucleotide adenylyltransferase; EC=2.7.7.18; AltName: Full=Deamido-NAD(+) diphosphorylase; AltName: Full=Deamido-NAD(+) pyrophosphorylase; AltName: Full=Nicotinate mononucleotide adenylyltransferase; Short=NaMN adenylyltransferase;
- **Gene Information:** Name=nadD; Synonyms=yqeJ; OrderedLocusNames=BSU25640;
- **Organism (full):** Bacillus subtilis (strain 168).
- **Protein Family:** Belongs to the NadD family. .
- **Key Domains:** Cyt_trans-like. (IPR004821); NadD/NMNAT. (IPR005248); Rossmann-like_a/b/a_fold. (IPR014729); CTP_transf_like (PF01467)

### MANDATORY VERIFICATION STEPS:

1. **Check if the gene symbol "nadD" matches the protein description above**
2. **Verify the organism is correct:** Bacillus subtilis (strain 168).
3. **Check if protein family/domains align with what you find in literature**
4. **If you find literature for a DIFFERENT gene with the same or similar symbol, STOP**

### If Gene Symbol is Ambiguous or You Cannot Find Relevant Literature:

**DO NOT PROCEED WITH RESEARCH ON A DIFFERENT GENE.** Instead:
- State clearly: "The gene symbol 'nadD' is ambiguous or literature is limited for this specific protein"
- Explain what you found (e.g., "Found extensive literature on a different gene with the same symbol in a different organism")
- Describe the protein based ONLY on the UniProt information provided above
- Suggest that the protein function can be inferred from domain/family information

### Research Target:

Please provide a comprehensive research report on the gene **nadD** (gene ID: P54455, UniProt: P54455) in BACSU.

The research report should be a detailed narrative explaining the function, biological processes, and localization of the gene product. Citations should be given for all claims.

You should prioritize authoritative reviews and primary scientific literature when conducting research. You can supplement
this with annotations you find in gene/protein databases, but these can be outdated or inaccurate.

We are specifically interested in the primary function of the gene - for enzymes, what reaction is catalyzed, and what is the substrate specificity? For transporters, what is the substrate? For structural proteins or adapters, what is the broader structural role? For signaling molecules, what is the role in the pathway.

We are interested in where in or outside the cell the gene product carries out its function.

We are also interested in the signaling or biochemical pathways in which the gene functions. We are less interested in broad pleiotropic effects, except where these elucidate the precise role.

Include evidence where possible. We are interested in both experimental evidence as well as inference from structure, evolution, or bioinformatic analysis. Precise studies should be prioritized over high-throughput, where available.

## Output

# Functional Annotation Report: *nadD* (NaMN Adenylyltransferase) in *Bacillus subtilis*

**Gene:** *nadD* (synonyms: *yqeJ*; ordered locus BSU25640)
**Protein:** Nicotinate-nucleotide adenylyltransferase (NaMN adenylyltransferase)
**UniProt:** [P54455](https://www.uniprot.org/uniprotkb/P54455/) · **EC:** 2.7.7.18
**Organism:** *Bacillus subtilis* (strain 168)

---

## Summary

The gene *nadD* of *Bacillus subtilis* strain 168 (synonym *yqeJ*; locus BSU25640; UniProt P54455) encodes **nicotinate mononucleotide (NaMN) adenylyltransferase** (NaMNAT; EC 2.7.7.18), a soluble cytoplasmic enzyme that catalyzes the **penultimate, essential step of NAD⁺ biosynthesis**. The enzyme transfers the adenylyl (AMP) moiety of ATP to nicotinic acid mononucleotide (NaMN), producing nicotinic acid adenine dinucleotide (NaAD, also called deamido-NAD) and inorganic pyrophosphate in a reversible, Mg²⁺-dependent reaction. The product NaAD is then amidated by NAD synthetase (NadE) to yield the mature redox cofactor NAD⁺. This identity is firmly established: the *B. subtilis* gene was directly identified and its product biochemically and structurally characterized by Olland and colleagues ([PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/)). There is no gene-symbol ambiguity — the UniProt description, EC number, protein family (NadD family), and domain architecture (Cyt_trans-like/CTP_transf_like, Rossmann-like α/β fold) all align exactly with the experimental literature.

Mechanistically, NadD occupies the **metabolic convergence point of all NAD⁺ biosynthetic routes**. NaMN is the common intermediate generated both by the *de novo* pathway (from aspartate via NadA/NadB/NadC) and by the nicotinate salvage pathway (via PncA/PncB). Because every route funnels through NaMN and then through NadD → NadE, NadD is one of only two indispensable downstream enzymes in bacterial NAD⁺ synthesis and cannot be bypassed. The enzyme is distinguished from the related nicotinamide mononucleotide adenylyltransferases (NMNATs) by its **substrate specificity for the deamidated (nicotinate) form, NaMN**, a preference whose structural basis — recognition of the nicotinate carboxylate by backbone amides — was resolved crystallographically.

Structurally, *B. subtilis* NadD adopts the Rossmann-like α/β fold of the **nucleotidyltransferase/α-β-phosphodiesterase superfamily**, and uses the conserved **(T/H)XGH** catalytic motif for ATP binding and adenylyl transfer. Direct inspection of the 189-residue P54455 sequence locates this motif as **HNGH at residues 15–18**, embedded in an N-terminal glycine-rich phosphate-binding loop — confirming the annotation at the primary-sequence level. Unusually for this enzyme family, the *B. subtilis* protein is a **homodimer**. Because NadD is essential and broadly conserved across bacteria yet structurally divergent from the human enzyme, it is a **validated, druggable broad-spectrum antibacterial target**, a conclusion supported by structure-based inhibitor campaigns against close relatives (*Bacillus anthracis*, *E. coli*) and by genetic depletion studies in *M. tuberculosis*.

---

## Key Findings

### Finding 1 — *nadD* (BSU25640/*yqeJ*) encodes the NaMN adenylyltransferase of NAD⁺ biosynthesis

The central identity of the gene is established by direct experimental work on *B. subtilis*. Olland et al. (2002) identified the *B. subtilis nadD* gene (synonym *yqeJ*) by sequence homology to other bacterial *nadD* genes and confirmed its function by biochemical characterization of the gene product. They state explicitly: *"The nadD gene, encoding the enzyme nicotinic acid mononucleotide (NaMN) adenylyltransferase (AT), is essential for the synthesis of NAD and subsequent viability of the cell. The nadD gene in Bacillus subtilis (yqeJ) was identified by sequence homology with other bacterial nadD genes and by biochemical characterization of the gene product"* ([PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/)).

The reaction catalyzed is the adenylyl transfer:

> **ATP + nicotinate β-D-ribonucleotide (NaMN) ⇌ diphosphate + nicotinate adenine dinucleotide (NaAD / deamido-NAD)**

This is a reversible, Mg²⁺-dependent nucleotidyl transfer that produces the immediate precursor to NAD⁺. The reaction is the **penultimate step** of NAD⁺ biosynthesis, immediately preceding the amidation of NaAD to NAD⁺ by NAD synthetase (NadE). This finding anchors the entire annotation: the gene symbol, EC number (2.7.7.18), and organism all match the UniProt target identity, and the function was determined by precise, low-throughput biochemistry rather than inference alone.

### Finding 2 — Substrate specificity: NadD prefers the deamidated nicotinate substrate (NaMN over NMN)

A defining biochemical feature of the NadD family — and of the *B. subtilis* enzyme in particular — is its specificity for the **nicotinate (deamidated)** mononucleotide, NaMN, rather than the amidated nicotinamide mononucleotide (NMN). Olland et al. found that the enzyme *"catalyzes the reversible adenylation of both NaMN and the nicotinamide mononucleotide (NMN) but shows specificity for the nicotinate"* ([PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/)). While the enzyme is catalytically capable of acting on both substrates, its physiological and kinetic preference is clearly for NaMN.

The structural basis for this preference was resolved in the same study: *"Interactions of the nicotinic acid with backbone atoms indicate the structural basis for specificity"* ([PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/)). The nicotinate carboxylate group is recognized through hydrogen bonds to main-chain amide atoms in the substrate pocket. This specificity is functionally important: it channels the deamidated route of NAD⁺ synthesis (where amidation occurs late, at the NadE step) and distinguishes bacterial NadD from the nicotinamide-preferring NMNATs that operate in the non-deamidating salvage routes of other organisms. Corroborating structural evidence from the related *Staphylococcus aureus* enzyme shows the same principle — *"the nicotinate carboxylates of NaAD are recognized by interaction with the main-chain amides of Thr85 and Tyr117, a positive helix dipole and two bridged-water molecules"* ([PMID: 16784754](https://pubmed.ncbi.nlm.nih.gov/16784754/)).

### Finding 3 — Quaternary structure and fold: a homodimer with a Rossmann-like α/β nucleotidyltransferase fold

Olland et al. determined crystal structures of *B. subtilis* NadD in both the apo state (2.1 Å) and a product-bound state (3.2 Å). The monomer adopts *"a monomer fold common to members of the nucleotidyl-transferase alpha/beta phosphodiesterase superfamily"* ([PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/)) — i.e., a Rossmann-like dinucleotide-binding fold. This matches the domain annotations for P54455 (InterPro IPR004821 Cyt_trans-like; IPR005248 NadD/NMNAT; IPR014729 Rossmann-like α/β/α fold; Pfam PF01467 CTP_transf_like).

A notable and unusual feature is the **oligomeric state**: whereas most characterized NMN/NaMN adenylyltransferases are monomeric, *"In contrast to other known NMN ATs, biophysical characterizations reveal it to be a dimer"* ([PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/)). A consistent "functional" dimer was observed across both crystal forms, suggesting the dimer is biologically meaningful rather than a crystallization artifact. Catalysis relies on the superfamily-conserved **(T/H)XGH** motif for ATP binding, a hallmark first defined in the founding NMNAT structural work: *"A strictly conserved HXGH motif (in single-letter amino acid code) is involved in ATP binding and recognition"* ([PMID: 10986466](https://pubmed.ncbi.nlm.nih.gov/10986466/)).

### Finding 4 — NadD is essential and a validated broad-spectrum antibacterial drug target

Because NadD catalyzes a non-redundant, essential step, loss of its activity is lethal to bacteria. This essentiality combined with broad conservation and structural divergence from human NMNATs makes NadD an attractive antibacterial target. Sorci et al. selected it explicitly for inhibitor development: *"Nicotinate mononucleotide adenylyltransferase of the NadD family, an essential enzyme of NAD biosynthesis in most bacteria, was selected as a target for structure-based inhibitor development"* ([PMID: 19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/)). Structure-based inhibitors against *E. coli* and *Bacillus anthracis* NadD (the latter a close genus-level relative of *B. subtilis*) selectively inhibited the bacterial enzymes without affecting the human counterparts and showed on-target antibacterial activity.

Genetic validation comes from *Mycobacterium tuberculosis*, where controlled depletion of NadD confirmed the metabolic consequence of blocking this step: *"Induced degradation of either target enzyme showed a strong bactericidal effect which coincided with anticipated changes in relative levels of NaMN and NaAD intermediates (substrates of NadD and NadE, respectively) and ultimate depletion of the NAD(H) pool"* ([PMID: 24549842](https://pubmed.ncbi.nlm.nih.gov/24549842/)). The accumulation of NaMN (NadD's substrate) and depletion of NAD(H) upon NadD loss directly demonstrates that NadD is the committed enzyme converting NaMN to NaAD, and that this conversion is indispensable for viability.

### Finding 5 — NadD acts at the convergence of *de novo* and salvage NAD routes; its upstream supply is NiaR-regulated in *B. subtilis*

NaMN is the universal node of bacterial NAD⁺ metabolism: it is produced by the *de novo* pathway (NadA/NadB/NadC, from aspartate via quinolinate) and by the nicotinate salvage pathway (PncA/PncB). From NaMN onward, there is a single two-enzyme funnel — NadD then NadE — through which all routes must pass. As Sorci et al. articulated for group A streptococci, *"the redundancy of functional upstream salvage pathways in GAS species narrows the choice of potential drug targets to the two indispensable downstream enzymes of NAD synthesis, nicotinate adenylyltransferase (NadD family) and NAD synthetase (NadE family)"* ([PMID: 23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/)). This places NadD squarely at the non-redundant bottleneck of the pathway.

In *B. subtilis* specifically, the enzymes that supply NadD's substrate are under coordinated transcriptional control by the niacin-responsive repressor **NiaR (YrxA)**. Rodionov et al. showed that *"In addition to transcriptional control of the nadABC genes, the NiaR regulon in some species extends to niacin salvage (the pncAB genes) and includes uncharacterized membrane proteins possibly involved in niacin transport"* ([PMID: 18276644](https://pubmed.ncbi.nlm.nih.gov/18276644/)). Thus NadD's inputs — both *de novo* synthesis and salvage uptake of niacin via the NiaP (YceI) transporter — are modulated by NiaR in response to niacin availability, while NadD itself sits downstream as the constitutive, essential committed step.

### Finding 6 — Conserved, druggable active-site architecture across *Bacillus* species

Structural studies of *Bacillus anthracis* NadD — a close relative of *B. subtilis* within the same genus — reinforce both the central metabolic role and the druggability of the active site. Huang et al. solved crystal structures of *B. anthracis* NadD in complex with three distinct inhibitors, revealing a common inhibitor-binding site adjacent to the substrate pocket and showing that subtle ligand modifications alter the binding mode. They affirm: *"Bacterial nicotinate mononucleotide adenylyltransferase encoded by the essential gene nadD plays a central role in the synthesis of the redox cofactor NAD(+)"* ([PMID: 20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/)). The conservation of active-site chemistry across *Bacillus* species supports transferring mechanistic and inhibitor insights to the *B. subtilis* enzyme.

### Finding 7 — Primary-sequence confirmation of the catalytic (H)XGH motif in P54455

Direct analysis of the 189-residue *B. subtilis* NadD sequence (UniProt P54455) locates the conserved catalytic motif **HNGH at residues 15–18**, embedded in the N-terminal glycine-rich phosphate-binding loop (…GIFGGTFDPPHNGHLL…, residues ~6–19). This matches the (T/H)XGH ATP-binding/adenylyl-transfer motif that is diagnostic of the nucleotidyltransferase α/β phosphodiesterase superfamily, as defined by D'Angelo et al.: *"A strictly conserved HXGH motif (in single-letter amino acid code) is involved in ATP binding and recognition"* ([PMID: 10986466](https://pubmed.ncbi.nlm.nih.gov/10986466/)). The presence of this motif at the sequence level, together with the N-terminal Rossmann-like dinucleotide-binding fold annotated for P54455 (InterPro IPR014729, IPR005248; Pfam PF01467), confirms the enzyme's catalytic identity independently of the crystal structure.

---

## Mechanistic Model and Interpretation

### The reaction and its place in the pathway

NadD catalyzes the adenylyl transfer that converts NaMN into deamido-NAD:

```
            NadD (EC 2.7.7.18), Mg2+
  NaMN  +  ATP  ================================>  NaAD (deamido-NAD)  +  PPi
  (nicotinate mononucleotide)                       (nicotinate adenine dinucleotide)
```

The product NaAD is then amidated by NadE (NAD synthetase) using glutamine or ammonia to form the mature cofactor:

```
            NadE (NAD synthetase)
  NaAD  +  ATP + NH3/Gln  ===================>  NAD+  +  AMP + PPi (+ Glu)
```

### Pathway convergence — why NadD is a bottleneck

All biosynthetic routes to NAD⁺ in *B. subtilis* funnel through NaMN, then through the obligatory NadD → NadE pair:

```
  DE NOVO (from aspartate)                 SALVAGE (from niacin/nicotinate)
  Asp --NadB--> ... --NadA--> quinolinate   nicotinamide --PncA--> nicotinate
       --NadC--> NaMN                        nicotinate   --PncB--> NaMN
                      \                              /
                       \                            /
                        v                          v
                 ====================  NaMN  ====================
                                        |
                                        |  NadD   (ESSENTIAL, non-redundant)
                                        v
                                       NaAD (deamido-NAD)
                                        |
                                        |  NadE   (ESSENTIAL, non-redundant)
                                        v
                                       NAD+  --> (NadK) --> NADP+
```

Everything upstream of NaMN is potentially redundant (de novo vs. salvage) and is regulated by **NiaR (YrxA)** in response to niacin availability. Everything from NaMN onward is a single, non-redundant funnel. This topology is precisely why NadD (and NadE) are the two indispensable "choke-point" enzymes and why they are favored antibacterial targets.

### Substrate discrimination — the deamidation logic

| Property | NadD (NaMNAT) | NMNAT |
|---|---|---|
| Preferred substrate | NaMN (deamidated / nicotinate) | NMN (amidated / nicotinamide) |
| Product | NaAD (deamido-NAD) | NAD⁺ directly |
| Amidation step | Late (at NadE) | Not required |
| *B. subtilis* enzyme | **Yes — P54455 is NadD** | — |
| Recognition basis | Nicotinate carboxylate ↔ backbone amides | Amide recognition |

*B. subtilis* NadD prefers the nicotinate form, committing the cell to the **deamidated route** in which amidation is deferred to the final NadE step. The specificity is encoded by backbone-amide recognition of the nicotinate carboxylate in the substrate pocket.

### Structure–function synthesis

| Feature | Observation | Evidence |
|---|---|---|
| Fold | Rossmann-like α/β; nucleotidyltransferase/phosphodiesterase superfamily | [PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/) |
| Catalytic motif | (H)XGH = **HNGH at residues 15–18** of P54455 | [PMID: 10986466](https://pubmed.ncbi.nlm.nih.gov/10986466/); sequence analysis |
| ATP binding | HXGH motif binds/positions ATP for adenylyl transfer | [PMID: 10986466](https://pubmed.ncbi.nlm.nih.gov/10986466/) |
| Substrate specificity | Nicotinate carboxylate recognized by backbone amides | [PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/) |
| Oligomeric state | Homodimer (unusual for the family) | [PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/) |
| Metal dependence | Mg²⁺-dependent | EC 2.7.7.18 / family biochemistry |

### Subcellular localization

NadD is a **soluble, cytoplasmic enzyme**. It carries no signal peptide, transmembrane segment, or lipidation signal, and its substrates (NaMN, ATP) and product (NaAD) are cytoplasmic metabolites of central metabolism. Its function — the reversible adenylyl transfer producing deamido-NAD — is therefore executed entirely in the cytosol, consistent with the general cytoplasmic localization of the NAD⁺ biosynthetic machinery. This is an inference from the protein's physicochemical properties and the location of its substrates/products, which is strongly supported but not the subject of a dedicated localization study.

---

## Evidence Base

| PMID | Title (abbrev.) | Relevance to annotation |
|---|---|---|
| [11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/) | *Identification, characterization, and crystal structure of B. subtilis NaMN adenylyltransferase* | **Primary, definitive**: identifies *B. subtilis nadD* (*yqeJ*), biochemically confirms NaMN AT activity, demonstrates nicotinate specificity, solves apo (2.1 Å) and product-bound (3.2 Å) structures, and shows the enzyme is a dimer. Underpins Findings 1–3. |
| [10986466](https://pubmed.ncbi.nlm.nih.gov/10986466/) | *Structure of NMN adenylyltransferase: a key enzyme in NAD⁺ biosynthesis* | Defines the conserved **HXGH** ATP-binding/catalytic motif of this adenylyltransferase family. Supports Findings 3 and 7. |
| [19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/) | *Targeting NAD biosynthesis: structure-based NadD inhibitors* | Establishes NadD as essential and a validated, selective drug target (incl. *B. anthracis*, *E. coli*); inhibitors spare human enzymes. Supports Finding 4. |
| [24549842](https://pubmed.ncbi.nlm.nih.gov/24549842/) | *Metabolic/bactericidal effects of NadD/NadE suppression in mycobacteria* | Genetic depletion of NadD is bactericidal and causes NaMN accumulation + NAD(H) depletion — direct proof of NadD's committed, essential metabolic role. Supports Finding 4. |
| [23204464](https://pubmed.ncbi.nlm.nih.gov/23204464/) | *Quinolinate salvage and NAD biosynthesis targeting in GAS* | Frames NadD and NadE as the two indispensable downstream enzymes at which redundant upstream routes converge. Supports Finding 5. |
| [18276644](https://pubmed.ncbi.nlm.nih.gov/18276644/) | *Transcriptional regulation of NAD metabolism: NiaR (YrxA) regulon* | Describes NiaR control of *nadABC*, *pncAB*, and niacin transport in *B. subtilis* — the regulated supply of NadD's substrate. Supports Finding 5. |
| [20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/) | *Complexes of bacterial NadD with inhibitors* | *B. anthracis* NadD–inhibitor structures; conserved, druggable active site in a close *Bacillus* relative. Supports Finding 6. |
| [16784754](https://pubmed.ncbi.nlm.nih.gov/16784754/) | *Crystal structure of S. aureus NaMNAT* | Independent structural confirmation of nicotinate-carboxylate recognition by backbone amides and of functional dimerization in a NadD-subfamily enzyme. Corroborates Findings 2–3. |
| [25631047](https://pubmed.ncbi.nlm.nih.gov/25631047/) | *Mycobacterial NadD: structure, mechanism, drug discovery* | Details the ordered kinetic mechanism (ATP binds first) and conformational control of catalysis in a NadD enzyme; context for mechanism. |
| [20926389](https://pubmed.ncbi.nlm.nih.gov/20926389/) | *Acinetobacter NAD metabolism* | Shows NadD can be functionally replaced by NadM in some bacteria — context on conservation; *B. subtilis* retains canonical NadD. |
| [16585762](https://pubmed.ncbi.nlm.nih.gov/16585762/) | *Comparative genomics of NAD biosynthesis in cyanobacteria* | Demonstrates a NadD ortholog (NaMN-preferring) is essential and cannot be complemented by an NMN-preferring AT — reinforces substrate-specificity logic (Finding 2). |
| [28986923](https://pubmed.ncbi.nlm.nih.gov/28986923/) | *HldC adenylyltransferase from B. pseudomallei* | Illustrates the shared Rossmann-like α/β fold and T/HXGH motif across the broader nucleotidyltransferase superfamily — structural context for Finding 3. |
| [17195474](https://pubmed.ncbi.nlm.nih.gov/17195474/) | *Subsystems-based drug-target identification* | Methodological framework placing NadD within an essential, druggable NAD subsystem. Context for Findings 4–5. |

**Convergence of evidence.** The annotation rests on an unusually strong and self-consistent evidence base: direct biochemistry and crystallography on the *B. subtilis* enzyme itself ([PMID: 11704676](https://pubmed.ncbi.nlm.nih.gov/11704676/)), primary-sequence confirmation of the catalytic motif in P54455, independent structural studies on genus relatives (*B. anthracis*) and other bacteria (*S. aureus*, *M. tuberculosis*), genetic essentiality/depletion data, and comparative-genomics pathway reconstruction. No conflicting evidence was found; all lines converge on the same functional assignment.

---

## Limitations and Knowledge Gaps

1. **Gene-symbol verification — resolved, no ambiguity.** The mandatory identity check is fully satisfied: the symbol *nadD* (and synonym *yqeJ*/BSU25640), EC 2.7.7.18, the NadD protein family, and the Cyt_trans-like/Rossmann-fold domains all match the experimentally characterized *B. subtilis* enzyme. There is no competing gene with the same symbol confounding the literature.

2. **Localization is inferred, not directly measured.** Cytoplasmic localization is inferred from the absence of targeting/membrane signals and from the cytosolic nature of substrates and products. No dedicated experimental localization study (e.g., fluorescent fusion, fractionation) for *B. subtilis* NadD was identified. The inference is strong but not experimentally proven for this specific protein.

3. **Detailed steady-state kinetics for the *B. subtilis* enzyme are incomplete.** While substrate preference (NaMN over NMN) is established, quantitative kinetic constants (kcat, Km for NaMN, NMN, ATP) and the ordered binding mechanism have been characterized in detail primarily for orthologs (e.g., *M. tuberculosis* NadD, where ATP binds first; [PMID: 25631047](https://pubmed.ncbi.nlm.nih.gov/25631047/)). Transfer of this mechanism to *B. subtilis* is plausible but not directly demonstrated.

4. **Functional significance of dimerization is unresolved.** The *B. subtilis* enzyme is a dimer, unusual within the family. Whether dimerization is required for activity, regulation, or stability — versus being incidental — has not been functionally dissected.

5. **Regulation at the protein level is uncharacterized.** Upstream substrate supply is NiaR-regulated transcriptionally, but post-translational regulation of NadD itself (allostery, feedback inhibition by NAD⁺/NADH, conformational gating under energy stress as seen in mycobacteria) has not been studied in *B. subtilis*.

6. **The analysis is literature/bioinformatics-based.** No new wet-lab data were generated; conclusions rest on published primary studies, structural data, and direct sequence analysis of P54455.

---

## Proposed Follow-up Experiments and Actions

1. **Quantitative enzymology of *B. subtilis* NadD.** Determine steady-state kinetic parameters (kcat, Km for NaMN, NMN, ATP; Mg²⁺ dependence) and establish the kinetic mechanism (ordered vs. random), testing whether the ATP-first ordered mechanism reported for mycobacterial NadD holds here.

2. **Direct localization confirmation.** Construct a functional NadD–fluorescent protein fusion or perform subcellular fractionation + immunoblotting in *B. subtilis* 168 to experimentally verify cytoplasmic localization.

3. **Dimer-interface mutagenesis.** Identify and mutate dimer-interface residues to generate monomeric variants and test effects on activity, stability, and in vivo complementation of a conditional *nadD* knockdown — resolving whether dimerization is functionally required.

4. **Conditional essentiality and metabolomics in *B. subtilis*.** Build a CRISPRi/degron-based conditional *nadD* strain and measure, by targeted metabolomics, the predicted NaMN accumulation and NAD(H) depletion upon depletion — directly reproducing in *B. subtilis* the causal chain demonstrated in *M. tuberculosis* ([PMID: 24549842](https://pubmed.ncbi.nlm.nih.gov/24549842/)).

5. **Feedback/allostery testing.** Assay NadD activity in the presence of NAD⁺, NADH, and NaAD to detect product/end-product inhibition and any energy-charge-dependent conformational regulation.

6. **Structure-guided inhibitor profiling.** Test the selective NadD inhibitors developed against *B. anthracis*/*E. coli* ([PMID: 19716475](https://pubmed.ncbi.nlm.nih.gov/19716475/), [PMID: 20578699](https://pubmed.ncbi.nlm.nih.gov/20578699/)) against purified *B. subtilis* NadD and whole cells to confirm on-target antibacterial activity in this species.

---

## Conclusion

*B. subtilis nadD* (P54455; *yqeJ*; BSU25640) encodes **nicotinate mononucleotide adenylyltransferase** (EC 2.7.7.18), a soluble cytoplasmic homodimer that catalyzes the essential, reversible, Mg²⁺-dependent transfer of the adenylyl group from ATP to NaMN, producing deamido-NAD (NaAD) plus pyrophosphate — the penultimate step of NAD⁺ biosynthesis. It is specific for the deamidated nicotinate substrate (NaMN over NMN), uses a Rossmann-like α/β fold with the catalytic (H)XGH motif present at residues 15–18 of its sequence, and sits at the non-redundant convergence point of the *de novo* and salvage pathways immediately upstream of NadE. Because there is no metabolic bypass, NadD is essential for viability and a validated broad-spectrum antibacterial drug target. The annotation is supported by direct biochemistry and crystallography of the *B. subtilis* enzyme, corroborated by structural, genetic, and comparative-genomic studies across related bacteria, with no conflicting evidence.


## Artifacts

- [OpenScientist final report](nadD-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](nadD-deep-research-openscientist_artifacts/final_report.pdf)

## Citations

1. PMID:11704676
2. PMID:16784754
3. PMID:10986466
4. PMID:19716475
5. PMID:24549842
6. PMID:23204464
7. PMID:18276644
8. PMID:20578699
9. PMID:25631047