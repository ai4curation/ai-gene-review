# S0EDH7 (FFUJ_06423) bioinformatics results (2026-10-21 full re-review)

Independent of any ProtNLM output. Files in this folder:

- `S0EDH7.fasta` - query sequence (342 aa, from S0EDH7-uniprot.txt).
- `hmmscan_S0EDH7_summary.txt` - local hmmscan (HMMER3) of S0EDH7 against a panel of 14
  kinase-like Pfam HMMs downloaded from the InterPro API (PF00069, PF07714, PF01636,
  PF17667, PF06293, PF01633, PF02958, PF12260, PF06176, PF14531, PF10707, PF01163,
  PF03109, PF05445).
- `kinase_motif_analysis.py` / `kinase_motif_analysis.out` - maps the residues aligned to
  the PF00069 catalytic loop (HrDlKpeN) and DFG motif for S0EDH7 and four homologs.
- `blast_uniprotkb_top.txt`, `blast_swissprot_top.txt` - EBI NCBI-BLAST hit tables.

## Findings

1. InterPro (API, 2026-10-21) lists only fold-level matches for S0EDH7: IPR011009 and
   SSF56112 (residues 180-311) and Gene3D 1.10.510.10 (258-320). No Pfam, PROSITE or
   PANTHER family is assigned.
2. Against the kinase-like panel, the best hit is Pkinase (PF00069), 29.5 bits, i-Evalue
   3.6e-10, HMM positions 43-143 aligned to residues 194-309. This is below the PF00069
   gathering threshold (31.7 bits), which explains the absence of a Pfam match. Kdo
   (15.2 bits) and APH (10.1 bits) score lower.
3. The alignment covers only the C-lobe (from about the alphaC helix onward). HMM
   positions 1-42, which contain the glycine-rich loop and the beta3 lysine, are not
   aligned in S0EDH7 or in any of the four homologs tested.
4. Catalytic-loop and Mg-binding motifs are retained: the PF00069 HrDlKpeN position aligns
   to W286-G287-D288-G289-K290-A291-S292-N293 (catalytic Asp D288, Lys K290, Asn N293)
   and the DFG motif to D307-F308-G309. The variant WGDGK..N loop is conserved in
   Fusarium (A0A1L7VSC9), Verticillium (G2WYF2), Sclerotinia (A7ERU3, WGDGKPHN) and
   Cordyceps (A0A162MTB1) homologs, suggesting a family-specific catalytic loop.
5. BLAST against UniProtKB: all strong hits (E < 1e-80) are uncharacterized
   Pezizomycotina proteins (Fusarium, Verticillium, Sclerotinia, Metarhizium, Cordyceps,
   Akanthomyces, etc.), several in multidomain contexts (e.g. a HET-domain fusion,
   A0A3M2RMT5, classified PANTHER PTHR33112). Against Swiss-Prot the best hits are weak
   and scattered across unrelated Ser/Thr kinase families (PIM2_DANRE E=0.002, PKH1_YEAST
   E=0.007, PKH2_YEAST E=0.07), i.e. there is no characterized ortholog.

## Interpretation

S0EDH7 is a member of an uncharacterized, Pezizomycotina-restricted family with a
divergent C-lobe of the protein kinase-like fold. Retention of the catalytic Asp, Lys
and Asn of the catalytic loop and of the DFG Asp is consistent with an active
phosphotransferase, but the N-lobe ATP-binding elements could not be detected and the
phosphoacceptor class (protein versus small molecule) cannot be inferred: the closest
profile is the eukaryotic protein kinase, but sub-threshold, and Kdo/APH small-molecule
kinase profiles also align to the same catalytic segment. No function can be transferred
from a characterized relative because none was found in a phylogenetically defined
group (no PANTHER subfamily, no PAINT node).
