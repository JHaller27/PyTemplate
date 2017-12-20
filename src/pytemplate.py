import argparse
import os


# Pseudo-constants
TEMPLATE_EXTENSION = '.template'
VARIABLE_EXTENSION = '.vars'


def main():
    # ArgParse setup
    parser = argparse.ArgumentParser(description='Template-based file generator')
    parser.add_argument('-i', '--input', default='./',
                        help='Directory to search for template and variable files')
    parser.add_argument('-o', '--output', default='./out/',
                        help='Directory to write output files to')
    parser.add_argument('-t', '--templates', nargs='*',
                        help='Template files. If omitted, will search for .template files')
    parser.add_argument('-v', '--variables', nargs='*',
                        help='Variable files. If omitted, will search for .vars files')
    parser.add_argument('-e', '--outputext', default='.txt',
                        help='Output file extension')
    parser.add_argument('-d', '--delim', nargs=2, default=['<', '>'],
                        help='Variables in the template file must be of the form "<DELIM><VAR><DELIM>"')
    parser.add_argument('--root', default='./',
                        help='Root directory')
    args = parser.parse_args()

    data_dir = args.root + args.input
    output_dir = args.root + args.output

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Find files if name list is empty
    template_names = args.templates if (args.templates is not None)\
        else (search_for_files(data_dir, TEMPLATE_EXTENSION))
    variables_names = args.variables if (args.variables is not None)\
        else (search_for_files(data_dir, VARIABLE_EXTENSION))

    # Create output files from cross-product of other files
    for t_name in template_names:
        for v_name in variables_names:
            out_name = get_output_file_name(t_name, v_name, args.outputext)
            generate(output_dir + out_name, data_dir + t_name, data_dir + v_name, args.delim[0], args.delim[1])


def get_output_file_name(t_name: str, v_name: str, output_extension='.txt') -> str:
    # Get bare template file name
    if '/' in t_name:
        t_name = t_name.rsplit('/')[-1]
    t_name = t_name.rsplit('.')[0]

    # Get bare variables file name
    if '/' in v_name:
        v_name = v_name.rsplit('/')[-1]
    v_name = v_name.rsplit('.')[0]

    # Generate output file name
    out_name = t_name
    if t_name != v_name:
        out_name += '-' + v_name
    out_name += output_extension

    return out_name


def search_for_files(directory: str, extension: str):
    files = []
    print("Searching '%s' for %s files..." % (directory, extension))
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file)
            print("  Found '%s'" % file)
    print()
    return files


def generate(output_name: str, template_name: str, variables_name, delimiter_pre='<', delimiter_post='>') -> None:
    print("Generating '%s'" % output_name)
    with open(template_name, 'r') as template_file:

        # Build replacements dictionary
        replacements = {}
        with open(variables_name, 'r') as variables_file:
            for line in variables_file:
                key = line[0:line.index('=')].strip()
                value = line[line.index('=')+1:].strip()
                replacements[delimiter_pre + key + delimiter_post] = value

        # Output filled-in template
        with open(output_name, 'w') as output_file:
            for line in template_file:
                for key in replacements:
                    line = line.replace(key, replacements[key])
                output_file.write(line)


if __name__ == '__main__':
    main()
