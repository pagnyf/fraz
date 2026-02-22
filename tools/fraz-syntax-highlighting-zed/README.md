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
cd tree-sitter-fraz
tree-sitter parse examples/test.fraz
```

- Test syntax highlighting:
```bash
cd tree-sitter-fraz
tree-sitter highlight examples/test.fraz
```

- Update syntax highlighting for [parser repository `tree-sitter-fraz`](https://github.com/pagnyf/tree-sitter-fraz):
Update `tree-sitter-fraz/queries/highlights.scm` such as:
```scm
(object) @tag
```
where `(object)`is type provided by parser and `@tag` is the highlight key for tree-sitter themes.
Tree sitter themes can be updated in config file:
- `$XDG_CONFIG_HOME/tree-sitter/config.json` or `$HOME/.config/tree-sitter/config.json` on Unix
- `%APPDATA%\tree-sitter\config.json` or `$HOME\AppData\Roaming\tree-sitter\config.json` on Windows


- Update syntax highlighting for [zed extension in repository `fraz`](https://github.com/pagnyf/tree-sitter-fraz):
Update `languages/fraz/highlights.scm` such as:
```scm
(object) @tag
```
Capturing groups (such as `@tag`) supported by Zed are different from tree sitter and listed in [Language Extensions](https://zed.dev/docs/extensions/languages#syntax-highlighting).

## Install as Dev Extension in Zed

In Zed:
- Press `Ctrl+Shit+P` and type `extension`.
- Select `zed: extensions`
- Select `fraz-syntax-highlighting-zed` as folder

Update extension with latest syntax changes:
- Regenerate parser:
```bash
cd tree-sitter-fraz
tree-sitter generate grammar.js
```
- Commit and push [parser repository `tree-sitter-fraz`](https://github.com/pagnyf/tree-sitter-fraz) updates:
```bash
cd tree-sitter-fraz
git push origin main
```
- Update `extension.toml` with latest commit id:
```toml
[grammars.fraz]
repository = "https://github.com/pagnyf/tree-sitter-fraz"
commit = "87836a94d75afe4179c391806661fdf7f5d2d6ae" 
```
- Open Zed extensions, click `Rebuild` next to `Fraz Syntax Highlighting`

## Extension Settings

`fraz-syntax-highlighting` doesn't add custom Zed settings currently.

## Known Issues

N/A

## Release Notes

### 0.0.1

N/A
