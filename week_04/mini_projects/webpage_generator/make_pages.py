import os

#fetching a list of all our raw text

raw_files = os.listdir("raw")

for rf in raw_files:
    with open(f"raw/{rf}","r",encoding="utf-8") as fin:
        title = fin.readline().rstrip()        #grabbing the first line as out title
        content = ""
        for line in fin.readlines():
            content += f"<p>{''.join(line.rstrip())}<p>"
        # creating a basic html structure with text input

        page = f"""<!DOCTYPE html>
<html>
<head>
        <title>{title}</title>
</head>

<body>
        <h1>{title}</h1>
        {content}
</body>
        </html>"""

#then write the content in an HTML file
        dirname = "pages"
        filename = f"pages/{rf[:-4]}.html"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write(page)

