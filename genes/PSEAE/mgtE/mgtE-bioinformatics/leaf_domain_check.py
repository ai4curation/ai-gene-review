"""For every leaf under a PANTHER node, look up the UniProt entry and report
length, Pfam domains and transmembrane segments.

Usage: python -I leaf_domain_check.py TREE_JSON NODE_ID PFAM_REQUIRED
  TREE_JSON      PANTHER v19 treeinfo JSON (as saved by curl)
  NODE_ID        PTN id whose leaves are checked
  PFAM_REQUIRED  Pfam accession whose presence is reported (e.g. PF01769,
                 the MgtE transmembrane domain)

The UniProt entry is found by searching the leaf's locus tag (the part of
gene_id after the colon, or the UniProt mnemonic for Gene:XXX_YYY ids) and
keeping the first hit whose organism shares the leaf organism's genus.
Leaves that cannot be resolved are reported as UNRESOLVED.
"""

import json
import sys
import urllib.parse
import urllib.request

UP = "https://rest.uniprot.org/uniprotkb/search"


def kids(n):
    c = n.get("children", {}).get("annotation_node", [])
    return c if isinstance(c, list) else [c]


def leaves(n):
    k = kids(n)
    return [n] if not k else [x for c in k for x in leaves(c)]


def find(n, pid):
    if n.get("persistent_id") == pid:
        return n
    for c in kids(n):
        r = find(c, pid)
        if r:
            return r
    return None


def uniprot(query: str) -> list[list[str]]:
    params = {
        "query": query,
        "fields": "accession,organism_name,length,xref_pfam,ft_transmem",
        "format": "tsv",
        "size": "5",
    }
    url = f"{UP}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=120) as r:
        rows = r.read().decode().strip().split("\n")[1:]
    return [x.split("\t") for x in rows if x]


def main() -> None:
    tree_file, node_id, pfam = sys.argv[1:4]
    root = json.load(open(tree_file))["search"]["tree_topology"]["annotation_node"]
    node = find(root, node_id)
    print(f"# Leaves of {node_id}: organism | locus | accession | length | {pfam} | TM segments | Pfam")
    n_with = n_without = n_unres = 0
    for lf in leaves(node):
        org = lf.get("organism", "")
        gid = lf.get("gene_id", "")
        locus = gid.split(":", 1)[-1]
        if gid.startswith("Gene:") and "_" in locus and locus.split("_")[-1].isupper():
            q = f"id:{locus}"
        else:
            q = f"gene:{locus}"
        genus = org.split()[0].lower() if org else ""
        hit = None
        try:
            for row in uniprot(q):
                if genus and genus in row[1].lower():
                    hit = row
                    break
        except Exception as exc:  # network or parse failure is reported, not hidden
            print(f"- {org} | {locus} | ERROR {exc}")
            n_unres += 1
            continue
        if not hit:
            print(f"- {org} | {locus} | UNRESOLVED")
            n_unres += 1
            continue
        acc, _, length, pf, tm = (hit + [""] * 5)[:5]
        has = pfam in pf
        ntm = tm.count("TRANSMEM")
        n_with += has
        n_without += not has
        print(f"- {org} | {locus} | {acc} | {length} | {'yes' if has else 'NO'} | {ntm} | {pf}")
    print(f"\nwith {pfam}: {n_with}; without: {n_without}; unresolved: {n_unres}")


if __name__ == "__main__":
    main()
