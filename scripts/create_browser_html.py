#!/usr/bin/env python3
"""Create the HTML file for linkml-browser."""

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gene Annotation Review Browser</title>
    <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/linkml-browser@latest/dist/linkml-browser.min.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/linkml-browser@latest/dist/style.css">
    <style>
        body { margin: 0; padding: 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; }
        #app { max-width: 1400px; margin: 0 auto; }
        h1 { color: #333; }
        .stats { background: #f5f5f5; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
        .review-action { padding: 2px 6px; border-radius: 3px; font-size: 12px; font-weight: 600; }
        .action-accept { background: #d4edda; color: #155724; }
        .action-keep { background: #d1ecf1; color: #0c5460; }
        .action-remove { background: #f8d7da; color: #721c24; }
        .action-modify { background: #fff3cd; color: #856404; }
        .action-over { background: #fce4d1; color: #8a4b08; }
        .action-undecided { background: #e2e3e5; color: #383d41; }
    </style>
</head>
<body>
    <div id="app">
        <h1>Gene Annotation Review Browser</h1>
        <div class="stats" v-if="data">
            <strong>Total Annotations:</strong> {{ data.length }} | 
            <strong>Genes:</strong> {{ uniqueGenes }} | 
            <strong>Species:</strong> {{ uniqueSpecies }}
        </div>
        <linkml-browser 
            :schema="schema" 
            :data="data"
            :config="browserConfig">
        </linkml-browser>
    </div>
    
    <script>
    const { createApp } = Vue;
    
    createApp({
        data() {
            return {
                schema: null,
                data: null,
                browserConfig: {
                    title: 'Gene Annotation Reviews',
                    itemsPerPage: 25,
                    enableSearch: true,
                    enableFilter: true,
                    enableSort: true,
                    enableExport: true
                }
            }
        },
        computed: {
            uniqueGenes() {
                if (!this.data) return 0;
                return new Set(this.data.map(d => d.gene_symbol)).size;
            },
            uniqueSpecies() {
                if (!this.data) return 0;
                return new Set(this.data.map(d => d.taxon_label).filter(t => t)).size;
            }
        },
        async mounted() {
            try {
                // Load schema
                const schemaResponse = await fetch('schema.json');
                this.schema = await schemaResponse.json();
                
                // Load data  
                const dataResponse = await fetch('data.json');
                this.data = await dataResponse.json();
            } catch (error) {
                console.error('Error loading data:', error);
            }
        }
    }).mount('#app');
    </script>
</body>
</html>"""

if __name__ == "__main__":
    with open("app/index.html", "w") as f:
        f.write(html_content)
    print("Browser HTML created successfully")
