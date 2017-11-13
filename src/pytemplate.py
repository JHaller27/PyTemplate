def main():
    data_dir = '..'
    output_dir = '..'
    template_names = ['hello.template', 'ssh.template']
    variables_names = ['hello.vars']

    for t_name in template_names:
        for v_name in variables_names:
            out_name = get_output_file_name(t_name, v_name)

            t_name = data_dir + '/' + t_name
            v_name = data_dir + '/' + v_name
            out_name = output_dir + '/' + out_name
            generate(out_name, t_name, v_name)


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
