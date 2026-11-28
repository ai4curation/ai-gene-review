import datetime
import hashlib
import json
import pathlib
import re
import subprocess
import yaml

ROOT = pathlib.Path.cwd()
OUT = (
    ROOT
    / ".cache/module-audit-logs/nitrogen-pts-20261107/triage/annotation-consultation-20261107"
)


def dump(name, data):
    (OUT / name).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


rows = [
    (
        "P37177",
        "ECOLI",
        "ptsP",
        "Escherichia coli K-12",
        "native_relay",
        "PTHR46244:SF1",
        "",
    ),
    (
        "P0A9N0",
        "ECOLI",
        "ptsO",
        "Escherichia coli K-12",
        "native_relay",
        "PTHR33705:SF2",
        "NPr/npr alias",
    ),
    (
        "P69829",
        "ECOLI",
        "ptsN",
        "Escherichia coli K-12",
        "native_relay",
        "PTHR47738:SF1",
        "",
    ),
    (
        "Q88CN5",
        "PSEPK",
        "ptsP",
        "Pseudomonas putida KT2440",
        "native_relay",
        "PTHR46244:SF1",
        "",
    ),
    (
        "Q88PA2",
        "PSEPK",
        "ptsH",
        "Pseudomonas putida KT2440",
        "native_relay",
        "PTHR33705:SF2",
        "PP_0948; literature ptsO; preserve established folder",
    ),
    (
        "Q88PA0",
        "PSEPK",
        "ptsN",
        "Pseudomonas putida KT2440",
        "native_relay",
        "PTHR47738:SF1",
        "",
    ),
    (
        "A0A0H3C823",
        None,
        "ptsP",
        "Caulobacter vibrioides NA1000",
        "native_relay",
        "PTHR46244:SF6",
        "CCNA_00892; PMID27109061 Results and Methods explicit",
    ),
    (
        "A0A0H3C344",
        None,
        "ptsH",
        "Caulobacter vibrioides NA1000",
        "native_relay",
        "PTHR33705:SF2",
        "CCNA_00241; PMID27109061 Results and Methods explicit",
    ),
    (
        "A0A0H3CDT8",
        None,
        "ptsN",
        "Caulobacter vibrioides NA1000",
        "native_relay",
        "PTHR47738:SF1",
        "CCNA_03710; PMID27109061 Results and Methods explicit",
    ),
    (
        "P08839",
        "ECOLI",
        "ptsI",
        "Escherichia coli K-12",
        "selector_control",
        "PTHR46244:SF6",
        "carbohydrate EI; not canonical nitrogen-route entry",
    ),
    (
        "P0AA04",
        "ECOLI",
        "ptsH",
        "Escherichia coli K-12",
        "selector_control",
        "PTHR33705:SF1",
        "canonical HPr comparison; NOT the same-SF2 counterexample",
    ),
    (
        "P08877",
        "BACSU",
        "ptsH",
        "Bacillus subtilis 168",
        "selector_control",
        "PTHR33705:SF2",
        "canonical HPr despite official NPR subfamily label",
    ),
    (
        "Q92MK4",
        None,
        "ptsP",
        "Rhizobium meliloti 1021",
        "optional_measured_entry_comparator",
        "PTHR46244:SF6",
        "SMc02437; experimental locus explicit; exact donor strain not explicit in inspected PMID24633875 methods",
    ),
    (
        "Q92TC0",
        None,
        "hpr",
        "Rhizobium meliloti 1021",
        "optional_measured_entry_comparator",
        "PTHR33705:SF2",
        "SMc02754; recombinant expression host is E. coli; donor strain qualification remains",
    ),
]
pattern = "|".join(r[0] for r in rows)
cmd = [
    "rg",
    "-n",
    pattern,
    "genes",
    "--glob",
    "*-ai-review.yaml",
    "--glob",
    "*-uniprot.txt",
]
r = subprocess.run(cmd, text=True, capture_output=True)
assert r.returncode in (0, 1), (r.returncode, r.stderr)
reviewpaths = list((ROOT / "genes").glob("*/*/*-ai-review.yaml"))
# Accession identity only; do not treat a mention in another review as target identity.
byid = {}
for p in reviewpaths:
    s = p.read_text()
    m = re.search(r"^id:\s*[\'\"]?([^\s\'\"]+)", s, re.M)
    if m and m.group(1) in pattern.split("|"):
        byid.setdefault(m.group(1), []).append(str(p.relative_to(ROOT)))
panel = []
for acc, sp, gene, org, role, fam, note in rows:
    actual = byid.get(acc, [])
    panel.append(
        dict(
            accession=acc,
            organism=org,
            gene=gene,
            role=role,
            panther_subfamily=fam,
            existing_review_paths=actual,
            intended_review_path=f"genes/{sp}/{gene}/{gene}-ai-review.yaml"
            if sp
            else None,
            status="EXISTING_DRAFT" if actual else "MISSING",
            identity_note=note,
        )
    )
dump(
    "panel.json",
    {
        "recommended_count": 12,
        "native_relay_count": 9,
        "selector_control_count": 3,
        "optional_count": 2,
        "recommended_existing_reviews": 3,
        "recommended_missing_reviews": 9,
        "organism_folder_rule": "Resolve exact UniProt species code during normal fetch; never substitute CB15 for NA1000.",
        "members": panel,
    },
)
inventory = {
    "command": cmd,
    "exit_code": r.returncode,
    "matches": r.stdout.splitlines(),
    "target_accession_review_matches": byid,
    "gene_snapshots": [],
    "family_review_status": {},
}
for gene in ["ptsP", "ptsH", "ptsN"]:
    p = ROOT / f"genes/PSEPK/{gene}/{gene}-ai-review.yaml"
    d = yaml.safe_load(p.read_text())
    ann = d["existing_annotations"]
    machine = [
        {k: v for k, v in a.items() if k != "review"}
        for a in ann
        if a.get("review", {}).get("action") != "NEW"
    ]
    inventory["gene_snapshots"].append(
        {
            "path": str(p.relative_to(ROOT)),
            "sha256": sha(p),
            "id": d["id"],
            "status": d.get("status"),
            "rows": len(ann),
            "active_historical_NEW": sum(
                a.get("review", {}).get("action") == "NEW" for a in ann
            ),
            "non_NEW_row_count": len(machine),
            "ordered_non_NEW_payload_sha256": hashlib.sha256(
                json.dumps(machine, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest(),
            "raw_files": {
                f"genes/PSEPK/{gene}/{gene}-{suf}": sha(
                    ROOT / f"genes/PSEPK/{gene}/{gene}-{suf}"
                )
                for suf in ["uniprot.txt", "goa.tsv"]
            },
        }
    )
for fam in ["PTHR46244", "PTHR33705", "PTHR47738"]:
    p = ROOT / f"interpro/panther/{fam}/{fam}-review.yaml"
    inventory["family_review_status"][str(p.relative_to(ROOT))] = (
        "PRESENT" if p.exists() else "MISSING"
    )
dump("repository-inventory.json", inventory)
controls = []
for fam, accs in [
    ("PTHR46244", ["P08839", "P37177"]),
    ("PTHR33705", ["P08877", "P0AA04", "P0A9N0"]),
]:
    p = ROOT / f"interpro/panther/{fam}/{fam}-entries.csv"
    for line in p.read_text().splitlines():
        if line.split(",")[0] in accs:
            controls.append(
                {
                    "path": str(p.relative_to(ROOT)),
                    "source_sha256": sha(p),
                    "literal_csv_row": line,
                }
            )
obo = (ROOT / "interpro/panther/panther.obo").read_text()
labels = {}
for ident in [
    "PTHR46244:SF1",
    "PTHR46244:SF6",
    "PTHR33705:SF1",
    "PTHR33705:SF2",
    "PTHR47738:SF1",
]:
    m = re.search(r"^id: PANTHER:" + re.escape(ident) + r"\nname: ([^\n]+)", obo, re.M)
    assert m, ident
    labels[ident] = m.group(1)
dump(
    "family-controls.json",
    {
        "official_labels": labels,
        "label_source": "interpro/panther/panther.obo",
        "label_source_sha256": sha(ROOT / "interpro/panther/panther.obo"),
        "member_controls": controls,
        "scope": "Membership counterexamples, not a family-wide evolutionary adjudication; alpha memberships derive from existing candidate-identities-20261107.json.",
    },
)
E = []


def ev(id, url, access, quote, claim, limit, sections):
    E.append(
        dict(
            id=id,
            url=url,
            access=access,
            short_exact_quote=quote,
            claim=claim,
            limits=limit,
            inspected_sections=sections,
        )
    )


ev(
    "PMID:10473571",
    "https://pubmed.ncbi.nlm.nih.gov/10473571/",
    "abstract",
    "EI(Ntr) phosphorylated NPr but not HPr",
    "Purified E. coli EI(Ntr) transfers phosphate from PEP to NPr; assay distinguishes HPr.",
    "Do not convert assay specificity into universal insulation, or assert detailed strain/kinetics without full text.",
    "Abstract",
)
ev(
    "PMID:7876255",
    "https://pubmed.ncbi.nlm.nih.gov/7876255/",
    "abstract",
    "Purified IIANtr and NPr exchange phosphate appropriately",
    "Original purified partner phosphotransfer/exchange evidence in E. coli.",
    "Assays include carbohydrate components; native physiological routing is a distinct question.",
    "Abstract",
)
ev(
    "PMID:15741344",
    "https://pubmed.ncbi.nlm.nih.gov/15741344/",
    "abstract lead",
    None,
    "Primary NMR study of E. coli PtsN/NPr interface.",
    "Not mined beyond title/abstract search; no assay-specific new claim.",
    "Search result",
)
ev(
    "PMID:23517463",
    "https://pmc.ncbi.nlm.nih.gov/articles/pmid/23517463/",
    "full-text request blocked by CAPTCHA",
    None,
    "Primary glutamine/alpha-ketoglutarate regulation lead for E. coli.",
    "No detailed source finding asserted; retrieve normally before use.",
    "Search title and access failure",
)
ev(
    "PMID:18296519",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC2347394/",
    "local partial text despite full_text_available true",
    "the primary flow of phosphate through the N/C-sensing PTS proceeds from PEP to EI(Ntr) to NPr to EIIA(Ntr)",
    "KT2440 native mutant/phosphostate evidence for relay and fructose/FruB bypass.",
    "Local Abstract/Discussion only; not purified pairwise reconstitution.",
    "publications/PMID_18296519.md",
)
ev(
    "PMID:17416664",
    "https://pubmed.ncbi.nlm.nih.gov/17416664/",
    "local abstract",
    "act in concert to control the intracellular accumulation of polyhydroxyalkanoates",
    "KT2440 PTS-linked PHA phenotype.",
    "No direct effector/enzymatic target inferred from this phenotype.",
    "publications/PMID_17416664.md",
)
ev(
    "PMID:19400808",
    "https://pubmed.ncbi.nlm.nih.gov/19400808/",
    "local abstract",
    "IIA(Ntr) interacts with sensor kinase KdpD and stimulates kinase\nactivity",
    "E. coli unphosphorylated PtsN stimulates KdpD kinase, increasing KdpE phosphorylation.",
    "Do not transfer catalytic direction to Pseudomonas from conserved names.",
    "publications/PMID_19400808.md",
)
ev(
    "PMID:21236318",
    "https://pubmed.ncbi.nlm.nih.gov/21236318/",
    "local abstract",
    "the enzyme activity was measured in\nextracts of isogenic ptsN(+)/ptsN(-)P. putida strains",
    "KT2440 AceE association, cytoplasmic colocalization and extract PDH downregulation.",
    "Not purified binary binding/inhibition reconstitution.",
    "publications/PMID_21236318.md",
)
ev(
    "PMID:26224366",
    "https://pubmed.ncbi.nlm.nih.gov/26224366/",
    "local abstract",
    "PtsN is responsible for repression of kdpFABC transcription",
    "P. putida KdpD interaction and condition/phosphostate-dependent promoter repression.",
    "Direct kinase inhibition/activation direction not independently established by available abstract.",
    "publications/PMID_26224366.md",
)
ev(
    "PMID:24633875",
    "https://gage.mcb.uconn.edu/downloads/2014_goodwin_jbact.pdf",
    "full author-hosted PDF",
    "hpr (smc02754) and ptsP (smc02437), respectively, were amplified",
    "Purified S. meliloti EI→HPr; glutamine binding to GAF and inhibition; no corresponding alphaKG effect under tested conditions.",
    "Native donor strain not explicitly stated in inspected methods; expression hosts are E. coli.",
    "PDF pp1–2 abstract and construct/purification methods",
)
ev(
    "PMID:27109061",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC4848567/",
    "full primary HTML and publisher PDF",
    "we found a unique HPr homologue (ptsH, CCNA_00241)",
    "NA1000 locus bridge for PtsP/CCNA00892, HPr/CCNA00241, PtsN/CCNA03710; native phosphostate and SpoT response.",
    "EI autophosphorylation uses containing fractions; PtsN-SpoT BACTH vs indirect HPr effect; not a purified three-protein flux measurement.",
    "Results gene identification; Methods strains/fractions/autophosphorylation; Fig6",
)
ev(
    "PMID:39742999",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC11808508/",
    "full primary HTML",
    "All bacterial strains used in this study are derivatives of E. coli K-12",
    "PtsN-YcgO phosphostate-dependent copurification; YcgO antiport in everted vesicles and native genetic support.",
    "B derivatives used for some protein expression; detailed CorC/RCK mechanism remains proposed.",
    "Abstract; Results; Experimental procedures",
)
ev(
    "PMID:37074168",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC10210985/",
    "full primary HTML",
    "FruB, the fructose EI, can substitute for PtsP in PtsN phosphorylation but only in the absence of PtsO",
    "PA14 native PtsN-H68 phosphostate and alternative upstream contribution.",
    "No automatic PAO1 identity; genetic/phosphostate support does not prove purified direct bypass edge.",
    "Abstract; Results; Methods",
)
ev(
    "PMID:40748077",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC12369347/",
    "full published primary HTML",
    "PtsO and PtsN as independent effectors in the PTS",
    "PA14 quorum reporter/perturbation/transcriptome work separates upstream and terminal outputs.",
    "Use published PMID not preprint39975224; direct PtsN-LasR interaction not established; GAF dispensable for some outputs.",
    "Abstract; Results; Bacterial strains and strain construction",
)
ev(
    "PMID:32341157",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC7229655/",
    "full primary HTML",
    None,
    "Rlv3841 separates PtsN/ABC-transport/ChvI outputs from ManX carbon effects; HprK/Ser48 branch.",
    "Exact panel accession mapping pending; no arbitrary ManX/PtsN replacement or direct central-enzyme binding inference.",
    "Results; Discussion; Materials and Methods",
)
ev(
    "DOI:10.1128/aem.01073-26",
    "https://journals.asm.org/doi/full/10.1128/aem.01073-26",
    "full primary HTML; publication2026-09-30",
    "BACTH assays did not detect a direct protein interaction between Rlv3841 ManX and MDH or between ManX and SucA",
    "Native Rlv3841 metabolic/polymer physiology; ManXH9A and HprK effects; binding assay limitations explicit.",
    "Crude-extract enzymology and inconclusive protein purification; assay negative not universal proof of no interaction.",
    "Abstract; Results around Fig2; Discussion; Methods",
)
ev(
    "PMID:24515609",
    "https://pubmed.ncbi.nlm.nih.gov/24515609/",
    "abstract inspected in prior triage",
    None,
    "H16 PtsN/SpoT1 interaction; unphosphorylated preference; no native KdpD interaction detected.",
    "Full-text assay details remain open; do not universalize negative interaction or evolutionary claim.",
    "Existing research-notes.md prior read-only triage",
)
ev(
    "PMID:21478317",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC3127587/",
    "full text table inspected in prior triage",
    None,
    "H16 PtsI/HPr/PtsN architecture differs from GAF-PtsP/NPr.",
    "Not a canonical-route positive from PtsN identity alone; exact accession panel not resolved here.",
    "Table1; prior research-notes.md",
)
ev(
    "PMID:41870250",
    "https://pmc.ncbi.nlm.nih.gov/articles/PMC13104625/",
    "full minireview",
    None,
    "Comparative discovery map for PTSNtr mechanisms and newer primary sources.",
    "Secondary source; individual homolog distributions do not establish intact functional relay.",
    "Introduction; distribution; outputs; reference list",
)
for evidence in E:
    if evidence["id"].startswith("PMID:"):
        cache = ROOT / ("publications/PMID_" + evidence["id"].split(":", 1)[1] + ".md")
        evidence["canonical_cache_path"] = str(cache.relative_to(ROOT))
        evidence["canonical_cache_exists"] = cache.exists()
        if cache.exists():
            evidence["canonical_cache_sha256"] = sha(cache)
dump(
    "evidence-ledger.json",
    {
        "observed_date": "2026-11-07",
        "retrieval_method": "Read-only web tool for external sources, file reads for five named local publications; no publication caches modified.",
        "entries": E,
    },
)
protected = json.loads((OUT / "protected-inputs.json").read_text())
changed = []
for rel, old in protected.items():
    p = ROOT / rel
    now = (
        {"sha256": sha(p), "mode": oct(p.stat().st_mode & 0o777)}
        if p.exists()
        else None
    )
    if now != old:
        changed.append({"path": rel, "before": old, "after": now})
assert not changed, changed
assert sum(x["rows"] for x in inventory["gene_snapshots"]) == 18
assert sum(x["active_historical_NEW"] for x in inventory["gene_snapshots"]) == 7
assert sum(x["non_NEW_row_count"] for x in inventory["gene_snapshots"]) == 11
assert len(byid) == 3, byid
assert all(not pathlib.Path(p).exists() for p in inventory["family_review_status"])
dump(
    "preservation-proof.json",
    {
        "result": "PASS_READ_ONLY",
        "protected_preexisting_files": len(protected),
        "changed": changed,
        "rows": 18,
        "machine_rows": 11,
        "active_historical_NEW": 7,
        "raw_files": 6,
        "scope": "Exact byte/mode check for enumerated local inputs, not corpus validation; no validators run.",
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    },
)
paths = sorted(
    str(p.relative_to(ROOT))
    for p in OUT.iterdir()
    if p.is_file() and p.name not in ["handoff.json", "artifact-hashes.json"]
)
dump("artifact-hashes.json", {p: sha(ROOT / p) for p in paths})
dump(
    "handoff.json",
    {
        "status": "CONSULTATION_COMPLETE_NO_CURATED_EDITS",
        "report": str((OUT / "report.md").relative_to(ROOT)),
        "recommended_panel": 12,
        "optional_panel_total": 14,
        "existing_reviews": 3,
        "missing_recommended_reviews": 9,
        "newest_verified_primary": "DOI:10.1128/aem.01073-26 (2026-09-30)",
        "blockers_for_later_curation": [
            "Family role selectors must exclude canonical PtsI/HPr while allowing verified alpha relay proteins",
            "Terminal kinase-regulator MF cannot define every PtsN output",
            "PA14 direct experiments must not be assigned as native PAO1 assays",
            "Complete missing source retrieval and gene review before capacity/publication claims",
        ],
        "artifacts": paths
        + [
            ".cache/module-audit-logs/nitrogen-pts-20261107/triage/annotation-consultation-20261107/artifact-hashes.json"
        ],
        "protected_input_count": len(protected),
        "preservation": "PASS",
        "failed_small_retrievals": 3,
        "source_cache_mutations": 0,
        "validation_runs": 0,
        "git_mutations": 0,
    },
)
print(
    json.dumps(
        {
            "recommended_panel": 12,
            "optional_total": 14,
            "existing": len(byid),
            "protected": len(protected),
            "evidence_sources": len(E),
            "artifacts": len(paths) + 2,
        },
        indent=2,
    )
)
