# fraz-syntax-highlighting README

This is the README for `fraz-syntax-highlighting` extension.

## Features

`fraz-syntax-highlighting` provides syntax color highlighting for `.fraz` files in VS Code.
Current syntax highlighting is based on semantic highlighting to keep compatibility with most themes.

## Requirements

`fraz-syntax-highlighting` only works with file ending with `.fraz`. 

## Extension Settings

`fraz-syntax-highlighting` doesn't add custom VS Code settings currently.

## Known Issues

Semantic highlighting is currently using standard tokens types used by other extensions to optimize for readability (with default themes) instead of semantic correctness (eg. Objects declaration are analyzed as `entity.name.function.fraz` instead of `entity.name.class.fraz`).
This might be improved in the future.

## Release Notes

Users appreciate release notes as you update your extension.

### 0.0.1

First working version.
Provides syntax highlighting for model and query definition of `.fraz` files.

