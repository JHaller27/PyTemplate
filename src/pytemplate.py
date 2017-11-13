def main():
    template_file = open('hello.template', 'r')
    variables_file = open('hello.vars', 'r')
    output_file = open('hello.txt', 'w')

    delimiter_pre = '<'
    delimiter_post = '>'

    # Build replacements dictionary
    replacements = {}
    for line in variables_file:
        (key, value) = line.split('=')
        replacements[key] = delimiter_pre + value + delimiter_post
    variables_file.close()

    # Output filled-in template
    for line in template_file:
        for key, value in replacements:
            line.replace(key, value)
        output_file += line
    template_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
