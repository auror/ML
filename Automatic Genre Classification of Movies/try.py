import json
import urllib2
import re

fp = open('movies.txt','r')

lines = fp.readlines()
fp.close()

fp = open('data.txt','w')
data = []

for line in lines:
    res = (line.split('|'))[1]
    res = res.split(' ')
    year = res.pop(-1)
    year = year[1:6]
    res = ' '.join(res)
    res = res.split(',')
    res.reverse()
    res = ' '.join(res)
    res = res.split(' ')
    
    res = '%20'.join(x for x in res if x)

    url = 'http://www.omdbapi.com/?t='+res
    print url

    sock = urllib2.urlopen(url)
    data = json.loads(sock.read())
    sock.close()

    url = 'http://www.imdb.com/title/'+ data['imdbID'] +'/keywords'
    print url

    sock = urllib2.urlopen(url)
    data = sock.read()
    sock.close()

    keywords = re.findall(r'>[a-z]*</a></td>', data)

    for word in keywords:
        temp = word.replace('</a></td>','')
        temp = temp.replace('>','')
        fp.write(temp + ' ')
    fp.write('\n')

fp.close()



"""fp = open('data.txt', 'r')

lines = fp.readlines()
fp.close()

data = []

fp = open('data1.txt', 'w')
for line in lines:
    temp = line.split(' ')
    data = data + temp

print len(data)
data1 = list(set(data))

ind = []
for i in data1:
    if data.count(i) < 3:
        ind.append(i)

for i in ind:
    data1.remove(i)

print len(data1)

for i in data1:
    fp.write(i + ' ')

fp.close()"""



"""import json
import urllib2
import re

fp = open('data1.txt','r')

lines = fp.read()
fp.close()

words = lines.split(' ')

fp = open('movies.txt','r')
data = []

lines = fp.readlines()
fp.close()

fp = open('td.txt','w')


for line in lines:
    temp = line.split('|')
    genres = temp[-19:]
    genres = ' '.join(genres)

    res = temp[1]
    res = res.split(' ')
    year = res.pop(-1)
    year = year[1:6]

    res = '%20'.join(x for x in res if x)
    
    url = 'http://www.omdbapi.com/?t='+res
    print url

    sock = urllib2.urlopen(url)
    data = json.loads(sock.read())
    sock.close()

    url = 'http://www.imdb.com/title/'+ data['imdbID'] +'/synopsis'
    print url

    sock = urllib2.urlopen(url)
    data = sock.read()
    sock.close()

    synopsis = (data.split('<div id="swiki.2.1">\n\n'))[1].split('\n\n</div>')[0]

    synopsis = synopsis.replace('.','')
    synopsis = synopsis.replace(',','')
    synopsis = synopsis.split(' ')

    for word in words:
        cnt = synopsis.count(word)
        fp.write(str(cnt) + ' ')

    fp.write(genres)
    #fp.write('\n')

fp.close()"""


