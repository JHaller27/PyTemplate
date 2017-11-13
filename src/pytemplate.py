def main():
    template_file = open('../hello.template', 'r')
    variables_file = open('../hello.vars', 'r')
    output_file = open('../hello.txt', 'w')

    delimiter_pre = '<'
    delimiter_post = '>'

    # Build replacements dictionary
    replacements = {}
    for line in variables_file:
        (key, value) = line.strip().split('=')
        replacements[delimiter_pre + key + delimiter_post] = value
    variables_file.close()

    # Output filled-in template
    for line in template_file:
        for key in replacements:
            line = line.replace(key, replacements[key])
        output_file.write(line)
    template_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
