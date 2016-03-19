# -*- coding: utf-8 -*- 

import markdown
import codecs
import json

def get_settings():
    settings_file = codecs.open('settings.json', 'r', encoding='utf-8')
    settings = json.loads(settings_file.read())
    settings_file.close()
    return settings

settings = get_settings()

md = markdown.Markdown(extensions=['mdx_katex'])

header = u'''
<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>{title}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.css" type="text/css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.js"></script>
  </head>
  <body>
    {body}
  </body>
</html>
'''

mdfile = codecs.open('body.md', 'r', encoding='utf-8')
mdcontent = mdfile.read()
mdfile.close()

html = header.format(body=md.convert(mdcontent), title=settings['title'])

outfile = codecs.open('index.html', 'w', 'utf-8')
outfile.write(html)
outfile.close()
