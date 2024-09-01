# What is Fraz
Fraz is a data modeling and query format aiming to:
- Simplify application data exchange and query
- Ensure better application safety and correctness

Fraz achieves this goal by:
- Making data description format human-readable (even for non technical-savyy users) and thus as close to natural language as possible
- Structuring data in a Relational Object Model, closer to human's mind representation

Fraz is currently in a experimental stage, format may vary between version and not be backward compatible.

# Contributing

As Fraz is currently in a very early stage, contributions are welcomed, but no guarantees can be given on review delay or acceptation into the current code base.

# Developing Syntax Highlighting Extension
## VSCode

1. Open this repository with VSCode.
2. Press **F5**. This will open a new VSCode window with the current extension loaded. Opening a `.fraz` file such as `examples/models/Airlines.fraz` will display the file content with syntax colored.
3. Update syntax highlighting behaviour by editing files located in `tools/fraz-syntax-highlighting` such as `syntaxes\fraz.tmLanguage.json` or `language-configuration.json`
4. Reload extension by pressing **Ctrl+Shift+F5** to see syntax updated according to your changes.
