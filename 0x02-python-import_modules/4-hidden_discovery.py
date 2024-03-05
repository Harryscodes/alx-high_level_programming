#!/usr/bin/python3
if __name__ == '__main__':
    import inspect

    import dis
    import types

    def get_names_from_pyc(pyc_file):
        with open(pyc_file, 'rb') as f:
            code_object = types.CodeType(*dis._unpack_structure(f.read()))

            # Extract names from the code object
            names = set(code_object.co_names)

            # Print names in alphabetical order
            for name in sorted(names):
                # Exclude names starting with '__'
                if not name.startswith('__'):
                    print(name)

            # Replace 'path/to/hidden_4.pyc' with the actual path to your .pyc file
            get_names_from_pyc('../hidden_4.')
