# PyTemplate

The PyTemplate application replaces text in template files with text set elsewhere in variables file.
If multiple template or var files are given as arguments, the resultant file structure would contain
the cross-product of {the set of `.template` files} x {the set of `.vars` files}.

## Examples

### Example 1

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
### Example 2

Help text

```
$ ./pytemplate.py -h
usage: pytemplate.py [-h] [-i INPUT] [-o OUTPUT]
                     [-t [TEMPLATES [TEMPLATES ...]]]
                     [-v [VARIABLES [VARIABLES ...]]] [-e OUTPUTEXT]
                     [-d DELIM DELIM] [-r ROOT]

Template-based file generator

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Directory to search for template andvariable files.
                        (default: )
  -o OUTPUT, --output OUTPUT
                        Output directory. (default: out/)
  -t [TEMPLATES [TEMPLATES ...]], --templates [TEMPLATES [TEMPLATES ...]]
                        Template files. If omitted, will search for
                        all'.template' files in the root. (default: None)
  -v [VARIABLES [VARIABLES ...]], --variables [VARIABLES [VARIABLES ...]]
                        Variable files. If omitted, will search for all'.vars'
                        files in the root. (default: None)
  -e OUTPUTEXT, --outputext OUTPUTEXT
                        Output file extension (default: .txt)
  -d DELIM DELIM, --delim DELIM DELIM
                        Specify the left and right delimiters. Textinside
                        these delimiters will be interpreted asvariables to be
                        replaced. (default: ['<', '>'])
  -r ROOT, --root ROOT  Root directory (default: ./)
```

### Example 3

Using the `sample/` directory included in this project...

```
$ ./pytemplate.py -r ../sample/ -i data/ -o out/
Searching '../sample/data/' for .template files...
  Found 'ssh.template'
  Found 'hello.template'

Searching '../sample/data/' for .vars files...
  Found 'hello.vars'

Generating '../sample/out/ssh-hello.txt'
Generating '../sample/out/hello.txt'
```
