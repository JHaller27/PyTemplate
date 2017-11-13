def main():
    data_dir = '..'
    template_names = ['hello.template']
    variables_names = ['hello.vars']
    output_name = '../hello.txt'

    for t_name in template_names:
        for v_name in variables_names:
            t_name = data_dir + '/' + t_name
            v_name = data_dir + '/' + v_name
            generate(output_name, t_name, v_name)


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
