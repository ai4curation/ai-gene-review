// data.js keeps its public URL and ready event; only the wire format changes.
(() => {
  const url = new URL('data.json.gz', document.currentScript.src);
  window.searchDataLoading = true;
  (async () => {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP ${response.status}: ${url}`);
    const stream = response.body.pipeThrough(new DecompressionStream('gzip'));
    const {columns, rows} = await new Response(stream).json();
    window.searchData = rows.map(values => {
      const row = {};
      values.forEach((value, index) => {
        if (value !== null) Object.defineProperty(row, columns[index], {
          value, enumerable: true, writable: true, configurable: true
        });
      });
      return row;
    });
    window.searchDataLoading = false;
    window.dispatchEvent(new Event('searchDataReady'));
  })().catch(error => {
    window.searchDataLoading = false;
    console.error('Annotation data could not be loaded', error);
    window.dispatchEvent(new CustomEvent('searchDataError', {detail: error.message}));
    const status = document.getElementById('resultsCount');
    if (status) status.textContent = 'Unable to load annotation data. Reload to retry.';
  });
})();
