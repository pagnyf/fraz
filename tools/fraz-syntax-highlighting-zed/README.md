# fraz-syntax-highlighting README

This is the README for `fraz-syntax-highlighting` extension in Zed.

## Features

`fraz-syntax-highlighting` provides syntax color highlighting for `.fraz` files in Zed.
Current syntax highlighting is based on semantic highlighting to keep compatibility with most themes.

## Requirements

`fraz-syntax-highlighting` only works with file ending with `.fraz`. 

## Contributing

This extension is built using `tree-sitter`. Refer to [Tree sitter documentation](https://tree-sitter.github.io) to edit it.

Within `/tree-sitter-fraz` directory, you can run the following snippets to perform basic actions:
- Generate parser
```bash
cd tree-sitter-fraz
tree-sitter generate grammar.js
```

- Parse file into a syntax tree:
```bash
tree-sitter parse tree-sitter-fraz/examples/basic.fraz
```

- Test syntax highlighting:
```bash
tree-sitter highlight tree-sitter-fraz/examples/basic.fraz
```

- Update syntax:
Update `tree-sitter-fraz/queries/highlights.scm` such as:
```scm
(object) @tag
```
where `(object)`is type provided by parser and `@tag` is the highlight type in Zed templates

## Install as Dev Extension in Zed

In Zed:
- Press `Ctrl+Shit+P` and type `extension`.
- Select `zed: extensions`
- Select `fraz-syntax-highlighting-zed` as folder

Update extensions with latest syntax changes:
- Regenerate parser:
```bash
tree-sitter generate tree-sitter-fraz/grammar.js
```
- Commit and push [parser repository `tree-sitter-fraz`](https://github.com/pagnyf/tree-sitter-fraz) updates:
```bash
cd tree-sitter-fraz
git push origin main
```
- Commit and push [`fraz` repository](https://github.com/pagnyf/fraz):
```bash
cd fraz
git push origin main
```
- Open Zed extensions, click `Rebuild` next to `Fraz Syntax Highlighting`

## Extension Settings

`fraz-syntax-highlighting` doesn't add custom Zed settings currently.

## Known Issues

N/A

## Release Notes

### 0.0.1

N/A
