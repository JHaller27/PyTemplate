import argparse
import os


def main():
    # Defaults
    template_names = []
    variables_names = []

    # ArgParse setup
    parser = argparse.ArgumentParser(description='Template-based file generator')
    parser.add_argument('-i', '--input', default='./',
                        help='Directory to search for template and variable files')
    parser.add_argument('-o', '--output', default='./',
                        help='Directory to write output files to')
    parser.add_argument('-t', '--template', dest='template_names', action='append',
                        help='Template files. If omitted, will search for .template files')
    parser.add_argument('-v', '--variable', dest='variables_names', action='append',
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
    if len(template_names) == 0:
        template_names = search_for_files(data_dir, '.template')

    if len(variables_names) == 0:
        variables_names = search_for_files(data_dir, '.vars')

    # Create output files from cross-product of other files
    for t_name in template_names:
        for v_name in variables_names:
            out_name = get_output_file_name(t_name, v_name, args.outputext)

            t_name = data_dir + '/' + t_name
            v_name = data_dir + '/' + v_name
            out_name = output_dir + '/' + out_name
            generate(out_name, t_name, v_name, args.delim[0], args.delim[1])


def get_output_file_name(t_name: str, v_name: str, output_extension='.txt') -> str:
    # Get bare template file name
    if '/' in t_name:
        t_name = t_name.rsplit('/')[1]
    t_name = t_name.rsplit('.')[0]

    # Get bare variables file name
    if '/' in v_name:
        v_name = v_name.rsplit('/')[1]
    v_name = v_name.rsplit('.')[0]

    # Generate output file name
    out_name = t_name
    if t_name != v_name:
        out_name += '-' + v_name
    out_name += output_extension

    return out_name


def search_for_files(directory: str, extension: str):
    files = []
    for file in os.listdir(directory):
        if file.endswith(extension):
            files.append(file)
    return files


def generate(output_name: str, template_name: str, variables_name, delimiter_pre='<', delimiter_post='>') -> None:
    with open(template_name, 'r') as template_file:

        # Build replacements dictionary
        replacements = {}
        with open(variables_name, 'r') as variables_file:
            for line in variables_file:
                (key, value) = line.strip().split('=')
                replacements[delimiter_pre + key + delimiter_post] = value

        # Output filled-in template
        with open(output_name, 'w') as output_file:
            for line in template_file:
                for key in replacements:
                    line = line.replace(key, replacements[key])
                output_file.write(line)


if __name__ == '__main__':
    main()
