# PyTemplate

The PyTemplate application replaces text in a template file with text set elsewhere in a variables file.
If multiple template or var files are given as arguments, the resultant file structure would contain
the cross-product of templates x vars.

## Features

| Feature | Planned | In development | Current |
|:--------|:--------|:---------------|:--------|
| Configurable via command line arguments | x | | |
| Custom template delimiters (default: "<>") | x | | |
| Search directory for templates/configs | x | | |
| Specify output directory | | | x |
| Multiple files | | | x |

## Example

Running PyTemplate on the following files...

`Hello.template`
```
Hello, <name>!
```

`Hello.var`
```
name=world
```

...would produce...

`Hello.txt`
```
Hello, world!
```
