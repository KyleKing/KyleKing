A few of my main projects:

<!-- PLANNED:

- https://github.com/KyleKing/dotfiles (chezmoi)
- https://github.com/KyleKing/recipes
- https://github.com/KyleKing/nvim
- https://github.com/KyleKing/karabiner-actions
- https://github.com/KyleKing/yak-shears
-->

## Terminal UI Applications

<details>
<summary><strong>repo-dashboard</strong> (<a href="https://github.com/KyleKing/gh-repo-dashboard">repo</a>) - TUI for viewing linked PRs, git status, stashes, and other information across multiple local git and Jujutsu (jj) repositories</summary>

![demo](https://raw.githubusercontent.com/kyleking/repo-dashboard/main/.github/assets/demo.gif)

**Quickstart**

```bash
gh extension install KyleKing/gh-repo-dashboard
gh repo-dashboard ~/Developer                          # TUI
gh repo-dashboard --cli --filter 'dirty' ~/projects     # scriptable JSON
```

</details>

<details>
<summary><strong>tail-jsonl</strong> (<a href="https://github.com/KyleKing/tail-jsonl">repo</a>) - Tail JSONL logs with pretty formatting and multi-line text like exceptions extracted for easier review</summary>

![demo](https://raw.githubusercontent.com/kyleking/tail-jsonl/main/.github/assets/demo.gif)

**Quickstart**

```bash
echo '{"message": "message", "timestamp": "2023-01-01T01:01:01.0123456Z", "level": "debug", "data": true, "more-data": [null, true, -123.123]}' |& uvx tail-jsonl
```

See the hosted docs, [PyPI package](https://pypi.org/project/tail_jsonl/), or the [repo docs](https://github.com/KyleKing/tail-jsonl/tree/main/docs) for more.

</details>

<details>
<summary><strong>jj-diff</strong> (<a href="https://github.com/KyleKing/jj-diff">repo</a>) - TUI diff tool designed for jj workflows and as a drop-in replacement for scm-diff-editor</summary>

![demo](https://raw.githubusercontent.com/kyleking/jj-diff/main/.github/assets/demo.gif)

<!-- PLANNED: provide brew install command instead and elsewhere -->

**Quickstart**

```bash
go install github.com/KyleKing/jj-diff/cmd/jj-diff@latest
jj-diff                 # browse diffs
jj-diff --interactive   # move/split hunks
```

Can also be wired in as jj's diff editor via `~/.config/jj/config.toml`.

</details>

<details>
<summary><strong>paper-todo-tui</strong> (<a href="https://github.com/KyleKing/paper-todo-tui">repo</a>) - TUI adaption of the minimalist productivity system from <a href="https://gladdendesign.com/products/paper-apps-todo">Paper Apps "TODO"</a></summary>

![demo](https://raw.githubusercontent.com/kyleking/paper-todo-tui/main/.github/assets/demo.gif)

State persists to `~/.local/share/paper-todo/state.json`.

</details>

<details>
<summary><strong>tail-cw</strong> (<a href="https://github.com/KyleKing/tail-cw">repo</a>) - Tail and filter AWS CloudWatch Logs from the terminal, with local Parquet caching and a Textual TUI</summary>

![demo](https://raw.githubusercontent.com/kyleking/tail-cw/main/docs/images/demo.gif)

Needs AWS credentials (profile/region) with CloudWatch Logs read access.

</details>

<details>
<summary><strong>vcr-tui</strong> (<a href="https://github.com/KyleKing/vcr-tui">repo</a>) - TUI for previewing VCR cassette files and other machine-generated fixtures</summary>

**Quickstart**

```bash
uv sync
vcr-tui /path/to/cassettes
vcr-tui preview cassette.yaml --key "interactions[0].response.body.string"
```

</details>

## GitHub CLI Extensions

<details>
<summary><strong>gh-lazydispatch</strong> (<a href="https://github.com/KyleKing/gh-lazydispatch">repo</a>) - Standalone or GitHub CLI extension for dispatching workflows interactively, from history, and more</summary>

![demo](https://raw.githubusercontent.com/kyleking/gh-lazydispatch/main/.github/assets/demo.gif)

**Quickstart**

```bash
gh extension install KyleKing/gh-lazydispatch
# or: brew install KyleKing/tap/gh-lazydispatch
cd your-project && gh lazydispatch
```

</details>

<details>
<summary><strong>gh-star-search</strong> (<a href="https://github.com/KyleKing/gh-star-search">repo</a>) - Indexes your starred repos into a local DuckDB database for fuzzy or semantic (vector) search plus related-repo discovery</summary>

**Quickstart**

```bash
gh extension install KyleKing/gh-star-search
gh star-search sync
gh star-search query "terminal ui library" --mode vector --limit 5
```

Needs `uv` installed (manages the Python environment for summarization/embeddings).

</details>

<details>
<summary><strong>gh-sweep</strong> (<a href="https://github.com/KyleKing/gh-sweep">repo</a>) - TUI for sweeping GitHub repositories: dead branches, unresolved review threads, protection drift, and slow workflows</summary>

<!-- PLANNED: ![demo](https://raw.githubusercontent.com/kyleking/gh-sweep/main/.github/assets/demo.gif) -->

**Quickstart**

```bash
gh extension install KyleKing/gh-sweep   # requires a GitHub Release; see CONTRIBUTING.md for a local install
gh sweep
```

</details>

## Neovim Plugins

<!-- PLANNED: rework examples to align with the new nvim 12 vim.pack syntax -->

<details>
<summary><strong>codanna.nvim</strong> (<a href="https://github.com/KyleKing/codanna.nvim">repo</a>) - Neovim front end for the <code>codanna</code> semantic code search CLI, with Telescope, mini.pick, and snacks.nvim picker support</summary>

**Quickstart**

```lua
{ "KyleKing/codanna.nvim", dependencies = { "folke/snacks.nvim" }, opts = { preferred_picker = "snacks" } }
```

```vim
:CodannaSearch some query
```

Requires the external `codanna` binary and a project indexed via `codanna init && codanna index .`.

</details>

<details>
<summary><strong>spaghetti-comb.nvim</strong> (<a href="https://github.com/KyleKing/spaghetti-comb.nvim">repo</a>) - Records LSP/jumplist navigation into a branching per-project trail, with breadcrumbs, a floating tree view, and bookmark pickers</summary>

**Quickstart**

```lua
add({ source = "KyleKing/spaghetti-comb.nvim" })
require("spaghetti-comb").setup()
```

Then `<leader>sb` for breadcrumbs, `<leader>sh` for the history picker.

</details>

## Mdformat Plugins

A suite of [mdformat](https://github.com/hukkin/mdformat) plugins for extending CommonMark formatting capabilities.

| Plugin                                                                           | Description                                                                                      |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| [mdformat-admon](https://github.com/KyleKing/mdformat-admon)                     | Format python-markdown admonitions                                                               |
| [mdformat-front-matters](https://github.com/KyleKing/mdformat-front-matters)     | Format YAML, TOML, or JSON front matter in markdown files                                        |
| [mdformat-gfm-alerts](https://github.com/KyleKing/mdformat-gfm-alerts)           | Format GitHub's blockquote-based admonitions (alerts)                                            |
| [mdformat-hooks](https://github.com/KyleKing/mdformat-hooks)                     | Run shell commands (like mdsf for code formatting) as post-processing hooks                      |
| [mdformat-mkdocs](https://github.com/KyleKing/mdformat-mkdocs)                   | Format MkDocs-specific markdown including admonitions, content tabs, and Material theme features |
| [mdformat-obsidian](https://github.com/KyleKing/mdformat-obsidian)               | Format Obsidian callouts (admonitions) and wiki-links                                            |
| [mdformat-plugin-template](https://github.com/KyleKing/mdformat-plugin-template) | Opinionated copier template for creating new mdformat plugins with modern Python tooling         |
| [mdformat-slw](https://github.com/KyleKing/mdformat-slw)                         | Better markdown diffs by reducing semantic line breaks                                           |

<details>
<summary>Quickstart</summary>

Each plugin auto-registers with mdformat once installed alongside it:

```bash
uvx --with mdformat-<plugin> mdformat file.md
# or: pipx install mdformat && pipx inject mdformat mdformat-<plugin>
```

`mdformat-plugin-template` is different, it's a copier template rather than a formatting plugin:

```bash
uv tool install copier
copier copy --UNSAFE gh:KyleKing/mdformat-plugin-template dest_folder_name
```

Caveat: don't combine `mdformat-admon` with `mdformat-mkdocs` >= 4.0.0, they're incompatible.

</details>

## Python Development Tools

<details>
<summary><strong>calcipy</strong> (<a href="https://github.com/KyleKing/calcipy">repo</a>) - Python development toolkit with task runners, documentation generators, and quality checks. Use with <strong>calcipy_template</strong> (<a href="https://github.com/KyleKing/calcipy_template">repo</a>) for project scaffolding and <strong>corallium</strong> (<a href="https://github.com/KyleKing/corallium">repo</a>) for shared utilities</summary>

**Quickstart**: see the hosted docs (calcipy.kyleking.me) and PyPI package, no minimal example in the root README today.

For **calcipy_template** scaffolding:

```bash
uvx copier copy --UNSAFE gh:KyleKing/calcipy_template dest_folder_name
```

Per its README, this template is "primarily for my personal use."

</details>

**copier-template-tester** ([repo](https://github.com/KyleKing/copier-template-tester)) - Configurable CLI and pre-commit tool for testing `copier` templates. See the hosted docs (copier-template-tester.kyleking.me), no minimal example in the root README today.

## Project Templates

<details>
<summary><strong>my_go_template</strong> (<a href="https://github.com/KyleKing/my_go_template">repo</a>) - Copier template for Go projects (CLI or library) with linting, hk git hooks, mise tasks, goreleaser, and CI. Sibling to calcipy_template above, opinionated to my own toolchain conventions</summary>

**Quickstart**

```bash
uvx copier copy gh:KyleKing/my_go_template your-project-name
cd your-project-name && mise install && hk install --mise
```

</details>

## Workflow & Testing

<details>
<summary>(<strong>Beta</strong>) <strong>dagtest</strong> (<a href="https://github.com/KyleKing/dagtest">repo</a>) - Complex workflow automation testing. Model and run complex workflow automation testing with Playwright and event listeners</summary>

**Quickstart**

```bash
uv add dagtest
```

```python
from dagtest import test

@test
async def test_root(ctx):
    return {"value": 1}
```

```bash
dagtest run
```

</details>

<!-- PLANNED: **dagster-taskiq-executor-demo** ([repo](https://github.com/KyleKing/dagster-taskiq-executor-demo)) - TaskIQ executor for Dagster. Demo application using TaskIQ instead of Celery to run Dagster jobs -->

<details>
<summary><strong>tlr</strong> (<a href="https://github.com/KyleKing/tlr">repo</a>) - Capacity- and dependency-aware planning board for Linear projects (Deno/TypeScript core, static web front end)</summary>

**Quickstart**

```bash
mise install && deno install && hk install
deno task dev             # serve the board at localhost:8000
deno task issues "Name"   # refresh from Linear
```

Needs Linear, Incident.io, and Google Calendar credentials to refresh data (see SETUP.md), so it's a personal/team tool rather than a drop-in installable app.

</details>

## Utilities & Other Projects

<details>
<summary><strong>doner</strong> (<a href="https://github.com/KyleKing/doner">repo</a>) - Managed pinned versions in Dockerfiles (<code>doner</code>: DOcker maintaiNER)</summary>

**Quickstart**

```bash
go install github.com/KyleKing/doner/cmd/doner@latest
doner check              # dry-run
doner update -f Dockerfile
```

Homebrew tap listed as "coming soon."

</details>

<details>
<summary><strong>diacea</strong> (<a href="https://github.com/KyleKing/diacea">repo</a>) - Universal diagram converter (Excalidraw, TLDraw, SVG, Mermaid) to text formats like Mermaid, PlantUML/C4, GraphViz, and D2</summary>

**Quickstart**

```bash
uvx diacea -i diagram.json -f mermaid -o output.mmd
uvx diacea sync docs/diagrams/*.excalidraw --check   # CI-friendly staleness check
```

</details>

<details>
<summary><strong>app-template</strong> (<a href="https://github.com/KyleKing/app-template">repo</a>) - Minimal Deno, Hono, HTMX template. Referenced by tlr's roadmap as a future pattern to borrow from (Playwright e2e tests, Zod-validated env config)</summary>

<!-- TODO: flesh out this quickstart once the copier rework settles -->

**Quickstart**

```bash
uvx copier copy gh:KyleKing/app-template dest_folder_name
```

</details>

<details>
<summary><strong>djot-fmt</strong> (<a href="https://github.com/KyleKing/djot-fmt">repo</a>) - Formatter for djot markup language</summary>

**Quickstart**

```bash
go install github.com/KyleKing/djot-fmt@latest
djot-fmt -w file.dj
```

</details>

<details>
<summary><strong>mise-postgres-binary</strong> (<a href="https://github.com/KyleKing/mise-postgres-binary">repo</a>) - Mise plugin for installing PostgreSQL binaries</summary>

**Quickstart**

```bash
mise plugin install postgres-binary https://github.com/KyleKing/mise-postgres-binary
mise use postgres-binary:postgres@18.4.0
```

</details>

## Contributions

- [textract](https://github.com/deanmalmgren/textract) - Extract text from any document. I previously maintained textract-py3, but have since merged all of the improvements into textract and continued releasing new features

______________________________________________________________________

[Personal Website](https://kyleking.me) | [PyPI Packages](https://pypi.org/user/kyleking)
