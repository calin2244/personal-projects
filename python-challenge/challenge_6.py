import zipfile
from re import compile

archive = zipfile.ZipFile("channel.zip", 'r')

comments = []

#with archive as zipf:
    #for name in zipf.namelist():
        #data = zipf.read(name)
        #comments.append(archive.getinfo(name).comment.decode('utf-8'))
        #print(name, len(data), repr(data[::]))
name = '90052'
pattern = compile("Next nothing is (\d+)")

while True:
    content = archive.read(name+'.txt').decode('utf-8')
    comments.append(archive.getinfo(name+'.txt').comment.decode('utf-8'))
    match = pattern.search(content)
    if match == None:
        break
    name = match.group(1)

print(''.join(comments))