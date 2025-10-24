import re

text = input()

pattern = r'(<title>.*<\/title>).*(<body>.*<\/body>)'

title_and_content = re.finditer(pattern, text)

for element in title_and_content:
    title = element.group(1)
    title = re.sub(r'<\/.*>|<.*>\b', "", title)

    content = element.group(2)
    content = re.sub(r'<[a-z =".:\/]+>|<\/[a-z]+>|\\n', "", content)
    print(f"Title: {title}\nContent: {content}")
