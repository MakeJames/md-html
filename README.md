# md-html

Enjoy the simplicity of markdown with the joy of structured html.

Designed to with flexibility in mind `md-html` can work as:

- A file parser: `md-html ./README.md`
- In line: `cat ./README.md | md-html`
- as a library: `from md_html import Markdown, HTML`

## Development

Uses `pdm` for python package management.

- **Lint:** `pdm run lint`
- **Test:** `pdm run test`
- **Format** `pdm run ruff format`

### Snapshots

Unexpected changes to the output of the cli is guarded by
a set of snapshot tests.

To update the snapshots run `pdm run test --snapshot-update`
