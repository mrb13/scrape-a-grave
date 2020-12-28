import sys
import os.path
import urllib.request
import sqlite3 as sql
from bs4 import BeautifulSoup, SoupStrainer

from db import makeGraveDatabase, addRowToDatabase, extractBirth, extractDeath

problemchilds = []
CONNECT = True

#if CONNECT:
#    if not os.path.isfile('./graves.db'):
#        makeGraveDatabase()


def findagravecitation(graveid):
    grave = {}
    grave['id'] = graveid

    #url = 'http://www.findagrave.com/cgi-bin/fg.cgi?page=gr&GRid='
    url = ' '
    url += str(graveid)
    print("url:", url)
    grave['url'] = url

    with urllib.request.urlopen(url) as html:
            print("t1:")
            #soup = BeautifulSoup(html.read(), "lxml")
            soup = BeautifulSoup(html.read(), "html.parser")
           # print("t2:", soup)

    text = 'Find A Grave Memorial #'
    text += str(graveid) + '\nName: '
        #name = soup.table.tr.td.find_next_siblings('td')[1].table.tr.get_text()

##########################################################
graveids = []
numcites = 0
numids = 0

# # read from gedcom
# with open('tree.ged', encoding='utf8') as ged:
#     for line in ged.readlines():
#         numcites+=1
#         if '_LINK ' in line and 'findagrave.com' in line:
#             for unit in line.split('&'):
#                 if 'GRid=' in unit:
#                     if unit[5:-1] not in graveids:
#                         graveids.append(unit[5:-1])
#                         #print(graveids[numids])
#                         numids+=1

# read from text file
with open('input-sites.txt', encoding='utf8') as txt:
    urlsz=[]

    for line in txt.readlines():
        numcites+=1
        #print("hiiit2:")

        with urllib.request.urlopen(line) as html:
            only_tags_with_id_cemNumberLabel = SoupStrainer(id="cemNumberLabel")
            only_tags_with_id_ipdescr = SoupStrainer(id="partBio")
            #print("linee:",line)
            # soup = BeautifulSoup(html.read(), "lxml")
            #addrs = []
            soup = BeautifulSoup(html.read(), "html.parser")
            sent_str = ""
            def has_content_and_itemprop(tag):
                #return tag.has_attr('class') and not tag.has_attr('id')
                return tag.has_attr('itemprop') and  tag.has_attr('content')

            for h1_tag in  soup.find_all("h1"):
                #print("h1_tag:", h1_tag)
                for cemetery_name in h1_tag.find_all("span"):
                   # print( "cemetery_name:", cemetery_name.string )
                    for address_tag in  soup.find_all("address"):
                    #print("address_tag:", address_tag)
                     for addr_span_tag in address_tag.find_all("span"):
                        #addrs.append(addr_span_tag.attrs['itemprop'])
                        #sent_str = str(addr_span_tag.string)
                        sent_str += str(addr_span_tag.string)+ ' '
                        #print("cemetery_name:", cemetery_name.string, "; addr_span_tag:", sent_str  )
            for directions in soup.find_all(attrs={"class": "bio-min hidden"}):
                dirz=directions.string
                #print("directions:", dirz)
            for m_tag in soup.find_all("p"):
                #latitude = ""
                #longitude = ""
                for s1 in m_tag.find_all("span"):
                    for s_lat in s1.find_all(attrs={"title": "Latitude"}):
                        latitude = s_lat.string
                        #print("latitude:", latitude   )
                    for span_long in s1.find_all(attrs={"title": "Longitude"}):
                        longitude = span_long.string
                        #print("longitude:", longitude   )

            for a_tag in  soup.find_all("td"):
                #<span id="cemNumberLabel" class="info">2579222</span>
                #for id_tag2 in a_tag.find_all("span"):
                #    print("id_tag2:", id_tag2)
                # f1 = id_tag2.select('span[id$="cemNumberLabel"]')
                #print("id_tag22:", f1.string)

                for ahref_tag in a_tag.find_all("a"):
                    #print("cemetery_name:", cemetery_name.string, "; addr_span_tag:", sent_str , "; ahref_tag:", ahref_tag.string, )
                    print(cemetery_name.string, ";", sent_str, ";", ahref_tag.string , ";" , dirz , ";" , latitude, ";" , longitude, ";" ,line)
                    #for show_maps in ahref_tag.find_all(attrs={"target": "_blank"}):
                    #print(ahref_tag.has_attr('target'))
                    #print(ahref_tag.target)


#[<h1 class="bio-name" itemprop="name"><span itemprop="name">Dublin Grove FWB Church Cemetery</span> </h1>]

parsed = 0
failedids = []
for i,gid in enumerate(graveids):
    try:
        print(str(i+1) + ' of ' + str(numids))
        print(findagravecitation(gid)+'\n\n')
        parsed += 1
    except:
        print('Unable to parse Memorial #'+str(gid)+'!\n\n')
        print("Error:", sys.exc_info()[0])
        failedids.append(gid)

out = 'Successfully parsed ' + str(parsed) + ' of '
out += str(len(graveids))
print(out)
if len(problemchilds)>0:
    print('\nProblem child were:', problemchilds)

# with open('results.txt', 'w') as f:
#     f.write(out + '\n')
#     f.write('\nProblem childz were:\n')
#     f.write('\n'.join(problemchilds))
#     f.write('\nUnable to parse:\n')
#     f.write('\n'.join(failedids))
