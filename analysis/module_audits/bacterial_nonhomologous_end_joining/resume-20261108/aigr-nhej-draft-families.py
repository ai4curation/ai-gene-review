from pathlib import Path
import yaml

ROOT = Path("analysis/module_audits/bacterial_nonhomologous_end_joining")


def term(i, label):
    return {"id": i, "label": label}


def source(n):
    s = (Path("publications") / f"PMID_{n}.md").read_text()
    return s, yaml.safe_load(s.split("---", 2)[1])


def support(n, q):
    s, _ = source(n)
    assert " ".join(q.split()) in " ".join(s.split()), (n, q)
    return {"reference_id": f"PMID:{n}", "supporting_text": q}


def refs(ns):
    return [dict(id=f"PMID:{n}", title=source(n)[1]["title"]) for n in ns]


def protein(a, label, symbol, org, path):
    return dict(
        id="UniProtKB:" + a,
        label=label,
        gene_symbol=symbol,
        organism=org,
        gene_review=path,
    )


ku_members = [
    protein(
        "Q88HU8",
        "Ku",
        "ku",
        "Pseudomonas putida KT2440",
        "genes/PSEPK/ku/ku-ai-review.yaml",
    ),
    protein(
        "Q9I1W5",
        "Ku",
        "ku",
        "Pseudomonas aeruginosa PAO1",
        "genes/PSEAE/ku/ku-ai-review.yaml",
    ),
    protein(
        "P9WKD9",
        "Ku",
        "mku",
        "Mycobacterium tuberculosis H37Rv",
        "genes/MYCTU/mku/mku-ai-review.yaml",
    ),
    protein(
        "O34859",
        "Ku",
        "ku",
        "Bacillus subtilis 168",
        "genes/BACSU/ku/ku-ai-review.yaml",
    ),
]
lig_members = [
    protein(
        "Q88HU3",
        "LigD",
        "ligD",
        "Pseudomonas putida KT2440",
        "genes/PSEPK/ligD/ligD-ai-review.yaml",
    ),
    protein(
        "Q9I1X7",
        "LigD",
        "ligD",
        "Pseudomonas aeruginosa PAO1",
        "genes/PSEAE/ligD/ligD-ai-review.yaml",
    ),
    protein(
        "P9WNV3",
        "LigD",
        "ligD",
        "Mycobacterium tuberculosis H37Rv",
        "genes/MYCTU/ligD/ligD-ai-review.yaml",
    ),
    protein(
        "O34398",
        "LigD",
        "ligd",
        "Bacillus subtilis 168",
        "genes/BACSU/ligd/ligd-ai-review.yaml",
    ),
]
ku_ev = support(
    "12215643",
    "bacterial Ku specifically recruits DNA ligase to DNA ends and stimulates DNA ligation.",
)
ku_ap = support(
    "25355514",
    "The presence of an AP-lyase activity also in the homolog protein from the distantly related bacterium Pseudomonas aeruginosa",
)
architecture = support(
    "34901162",
    "B. subtilis LigD lacks the PE domain, with only the LIG domain at the N-terminus and the POL domain at the C-terminus",
)
lig_ev = support(
    "16023671",
    "The ligase domain catalysed the sealing of nicked double-stranded DNA designed to mimic a DSB",
)
pol_ev = support(
    "16023671",
    "The polymerase domain can also extend DNA in a template-dependent manner.",
)
prim_ev = support(
    "16023671",
    "The polymerase domain demonstrated DNA-dependent RNA primase activity, catalysing the synthesis of unprimed oligoribonucleotides on single-stranded DNA templates.",
)
pe_ev = support(
    "16046407",
    "the PE domain has a 3'-phosphatase activity on an all-DNA primer-template",
)
ku = {
    "family_id": "PANTHER:PTHR41251",
    "family_name": "NON-HOMOLOGOUS END JOINING PROTEIN KU",
    "preferred_name": "Prokaryotic-type Ku DNA-end-binding proteins",
    "summary": "Ku proteins bind broken duplex DNA ends and assemble end-joining complexes. Bacterial Ku homodimers recruit repair ligases and protect or align DNA ends. Some experimentally characterized Ku proteins additionally process abasic sites, but this chemistry has not been established throughout the family.",
    "functional_coherence": "MOSTLY_COHERENT",
    "coherence_reason": "DNA-end binding is the conserved structural role. C-terminal organization, repair partners and measured AP/5-prime-dRP lyase activities differ in evidential scope; the latter are not granted family-wide. The family contains nonbacterial records, so family membership alone does not establish bacterial taxon context.",
    "reference_protein": ku_members[1],
    "subfamilies": [
        {
            "subfamily_id": "PANTHER:PTHR41251:SF1",
            "label": "NON-HOMOLOGOUS END JOINING PROTEIN KU",
            "description": "Conserved Ku scaffold represented here across Pseudomonadota, Actinomycetota and Bacillota. The sampled tree also contains a plant-labelled leaf; no unsupported contamination or lineage-loss explanation is assigned.",
            "representative_members": ku_members,
            "supported_by": [ku_ev],
        }
    ],
    "node_assessments": [
        {
            "node_id": "PANTHER:PTN002222140",
            "asserted_term": term("GO:0003690", "double-stranded DNA binding"),
            "seeds": [ku_members[2], ku_members[1]],
            "assessment": "SOUND",
            "assessment_reason": "The actual tree places the Bacillus, PAO1 and H37Rv exemplars below this node, and the experimentally characterized Ku scaffold binds duplex ends. The two listed seeds support the conserved activity; their count is not a weakness. KT2440 Q88HU8 is absent from the sampled tree and is not assigned an invented leaf position. The export records a bacterial taxon even though the current tree includes a plant-labelled leaf; this mismatch is retained as a taxonomic provenance question, not evidence that the binding function is lost.",
            "node_taxon": term("NCBITaxon:2", "Bacteria"),
            "evidence": "IBD",
            "negated": False,
            "supported_by": [ku_ev],
        }
    ],
    "term_assessments": [
        {
            "assessed_term": term("GO:0003690", "double-stranded DNA binding"),
            "scope": "FAMILY_WIDE",
            "scope_reason": "Conserved Ku DNA-binding scaffold and the inspected PAINT node support duplex binding. This does not transfer the exact end-protection kinetics of a truncated construct to every member.",
            "supported_by": [ku_ev],
        },
        {
            "assessed_term": term("GO:0045027", "DNA end binding"),
            "scope": "FAMILY_WIDE",
            "scope_reason": "Recognition of duplex termini is the defining Ku role supported by bacterial biochemical reconstitution. This finer claim is not asserted to be the term present on the inspected PAINT node, which carries GO:0003690.",
            "supported_by": [ku_ev],
        },
        {
            "assessed_term": term(
                "GO:0140078",
                "class I DNA-(apurinic or apyrimidinic site) endonuclease activity",
            ),
            "scope": "UNRESOLVED",
            "scope_reason": "AP beta-elimination is measured for Bacillus and Pseudomonas Ku, but no experimentally or phylogenetically justified family-wide catalytic grant or narrower gain/loss node has been established. Retain the positive member evidence without treating every Ku as an AP lyase.",
            "supported_by": [ku_ap],
        },
    ],
    "references": refs(["12215643", "20018881", "25355514", "34901162"]),
    "review_status": "NEEDS_REVIEW",
    "reviewed_by": "codex",
    "review_date": "2026-11-07",
    "notes": "Tree topology and exact leaves are preserved under analysis/module_audits/bacterial_nonhomologous_end_joining/tree-evidence-20261107/PTHR41251-compact.json with its raw export and receipt. PTHR41251-paint.tsv is the assertion source. SF1 is a classification, not an interchangeable PTN identifier. The module additionally imposes bacterial context. No residue-loss claims are made.",
}
node_terms = [
    (
        "GO:0003887",
        "DNA-directed DNA polymerase activity",
        [lig_members[2], lig_members[1]],
        "UNRESOLVED",
        pol_ev,
    ),
    (
        "GO:0003910",
        "DNA ligase (ATP) activity",
        [lig_members[2], lig_members[1]],
        "SOUND",
        lig_ev,
    ),
    (
        "GO:0006269",
        "DNA replication, synthesis of RNA primer",
        [lig_members[2]],
        "UNRESOLVED",
        prim_ev,
    ),
    (
        "GO:0006303",
        "double-strand break repair via nonhomologous end joining",
        [lig_members[2]],
        "UNRESOLVED",
        lig_ev,
    ),
]
nodes = []
for i, label, seeds, verdict, ev in node_terms:
    reason = (
        "ATP-dependent ligation is supported by the characterized LigD ligase domains and is consistent with both the fused-LigD SF2 and ATP-dependent-ligase SF3 classifications in the actual descendant tree."
        if verdict == "SOUND"
        else "The actual PTN001627042 tree includes SF2 fused LigD exemplars and SF3 ATP-dependent ligases. The characterized SF2 proteins support the asserted activity or process, but SF3 domain architecture and participation have not been sufficiently adjudicated to settle the scope over every descendant. This is an unresolved broad-node assessment, not a claim that the SF2 target genes lost the function or that the experimental seeds are weak."
    )
    if i == "GO:0006269":
        reason += " The GO definition includes damage-repair priming; do not reject the term merely because LigD is a repair enzyme or because only one seed is listed. Physiological use and biochemical capacity are distinct."
    nodes.append(
        {
            "node_id": "PANTHER:PTN001627042",
            "asserted_term": term(i, label),
            "seeds": seeds,
            "assessment": verdict,
            "assessment_reason": reason,
            "evidence": "IBD",
            "negated": False,
            "supported_by": [ev],
        }
    )
lig = {
    "family_id": "PANTHER:PTHR42705",
    "family_name": "BIFUNCTIONAL NON-HOMOLOGOUS END JOINING PROTEIN LIGD",
    "preferred_name": "LigD-related ATP-dependent ligases with variable processing domains",
    "summary": "This family contains ATP-dependent DNA ligases, including fused LigD proteins that combine end sealing with polymerase activity and, in some lineages, a phosphoesterase module. Domain content and order vary: Bacillus subtilis LigD lacks the phosphoesterase domain found in the characterized Pseudomonas and mycobacterial proteins. Abasic-site processing and nucleotide-addition reactions depend on the protein and substrate context.",
    "functional_coherence": "MOSTLY_COHERENT",
    "coherence_reason": "ATP-dependent ligation is the common activity. The actual tree contains fused-LigD SF2 and ATP-dependent-ligase SF3 members; even SF2 is heterogeneous for phosphoesterase architecture. Family or SF2 membership alone cannot establish every processing activity.",
    "reference_protein": lig_members[1],
    "subfamilies": [
        {
            "subfamily_id": "PANTHER:PTHR42705:SF2",
            "label": "BIFUNCTIONAL NON-HOMOLOGOUS END JOINING PROTEIN LIGD",
            "description": "Characterized fused POL/LIG proteins from three bacterial phyla; PE is present in the characterized Pseudomonas and mycobacterial proteins but absent in Bacillus LigD. Retain the official subfamily label rather than substituting a domain-count description.",
            "representative_members": lig_members,
            "supported_by": [architecture, pol_ev, lig_ev],
        }
    ],
    "node_assessments": nodes,
    "term_assessments": [
        {
            "assessed_term": term("GO:0003910", "DNA ligase (ATP) activity"),
            "scope": "FAMILY_WIDE",
            "scope_reason": "ATP-dependent DNA sealing is the common ligase activity and the inspected IBD assertion; variable processing domains do not negate ligation.",
            "supported_by": [lig_ev],
        },
        {
            "assessed_term": term("GO:0003887", "DNA-directed DNA polymerase activity"),
            "scope": "SUBFAMILY_ONLY",
            "applicable_subfamilies": [
                term(
                    "PANTHER:PTHR42705:SF2",
                    "BIFUNCTIONAL NON-HOMOLOGOUS END JOINING PROTEIN LIGD",
                )
            ],
            "scope_reason": "Fused POL/LIG architecture and DNA synthesis are supported in the characterized SF2 proteins across three phyla. Do not extend this processing activity to SF3 merely because the broad IBD node spans it. The module requires an independently supported POL role in addition to classification.",
            "supported_by": [pol_ev, architecture],
        },
        {
            "assessed_term": term(
                "GO:0046403", "polynucleotide 3'-phosphatase activity"
            ),
            "scope": "UNRESOLVED",
            "scope_reason": "This activity is established for the Pseudomonas PE domain, including an all-DNA substrate, but SF2 includes Bacillus LigD without PE. A function- and domain-qualified subset is required; no SF2-wide grant, arbitrary residue rule or invented ancestral loss is asserted.",
            "supported_by": [pe_ev, architecture],
        },
        {
            "assessed_term": term(
                "GO:0140078",
                "class I DNA-(apurinic or apyrimidinic site) endonuclease activity",
            ),
            "scope": "UNRESOLVED",
            "scope_reason": "Bacillus LigD POL catalyzes substrate-dependent AP beta-elimination. Its gain or conservation across all LigD homologs has not been established, so preserve the measured exemplar without a family-wide grant.",
            "supported_by": [
                support(
                    "30976810",
                    "a robust AP lyase activity in the polymerization domain of Bacillus subtilis LigD",
                )
            ],
        },
    ],
    "references": refs(
        [
            "16023671",
            "16046407",
            "20018881",
            "26826709",
            "30976810",
            "34901162",
            "41957403",
        ]
    ),
    "review_status": "NEEDS_REVIEW",
    "reviewed_by": "codex",
    "review_date": "2026-11-07",
    "notes": "The current tree is preserved under analysis/module_audits/bacterial_nonhomologous_end_joining/tree-evidence-20261107/PTHR42705-compact.json with its raw export and receipt; PTHR42705-paint.tsv supplies the four actual assertions. Do not equate PTN001627042 with SF2: its descendants also include SF3 and nonbacterial leaves. Q88HU3 is not an exact leaf in this sample. No PE or AP-lyase IBD occurs in the export. SF3 is observed but not independently reviewed here; the associated broad-node questions remain unresolved rather than fabricated losses. The 2026 mycobacterial LigD construct P9WNV2 differs from the H37Rv representative P9WNV3 and is not substituted for it.",
}
for fam, doc in [("PTHR41251", ku), ("PTHR42705", lig)]:
    p = Path("interpro/panther") / fam / (fam + "-review.yaml")
    assert not p.exists()
    p.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100))
    print(p)
