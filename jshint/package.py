import textwrap;

if __name__ == '__main__':
    files = [
      'jshint.js',
      'Settings.js',
      'CommandLine.js'
    ]
    body = []
    for file in files:
        body.append(open(file, 'r').read())
    s = '\n'.join(body);
    scriptfile = open('jshint_script.js', 'w');
    scriptfile.write(s);
    scriptfile.close();

    s = s.encode("hex").upper();
    t = "".join(["\\x"+x+y for (x,y) in zip(s[0::2], s[1::2])]);
    arrayfile = open('jshint_script.h', 'w');
    a = "static const char jshint_script[] = \\\n\t\"%s\";"%"\"\\\n\t\"".join(textwrap.wrap(t,80));
    arrayfile.write(a);
    arrayfile.close();
