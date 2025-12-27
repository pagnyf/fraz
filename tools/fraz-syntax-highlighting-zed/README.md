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
tree-sitter generate grammar.js
```

- Parse file into a syntax tree:
```bash
tree-sitter parse examples/basic.fraz
```

- Test syntax highlighting:
```bash
tree-sitter highlight examples/basic.fraz
```

## Extension Settings

`fraz-syntax-highlighting` doesn't add custom Zed settings currently.

## Known Issues

N/A

## Release Notes

### 0.0.1

N/A
