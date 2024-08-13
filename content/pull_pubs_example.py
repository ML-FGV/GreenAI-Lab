from scholarly import scholarly
from scholarly import ProxyGenerator
import datetime

# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session
pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)

### better to run it on colab because google scholar can block your ip
## https://colab.research.google.com/drive/1f0fnXC74AD-YINGSEoxGjIOyJKYcFtsy?usp=sharing - same script on scholar

print(" run this script on scholar https://colab.research.google.com/drive/1f0fnXC74AD-YINGSEoxGjIOyJKYcFtsy?usp=sharing")

exit(0)

def fill_template(pubobj, labdict):
    pub = pubobj['bib']
    title = pub['title'].replace("  "," ").replace('"',"'")
    date = f"{pub['pub_year']}-01-01"
    author = pub['author'].split(" and ")
    labmembers = []
    # check if author name is in labdict
    # add labmembers in another list
    for i, a in enumerate(author):
        count=0
        all_names = a.split(" ")
        first_name=all_names[0]
        last_name=all_names[-1]
        # if first name has more than one letter
        if len(first_name)>1:
            # if first name + lastname is in labdict
            key_test =f"{first_name} {last_name}"
            if key_test in labdict:
                author[i]=labdict[key_test]
                labmembers.append(author[i])
                count+=1
        else:
          # first name has one character -> split keys in labdict and check first letter equal and lastname
          for key in labdict:
            if key[0]==first_name and key.split(" ")[1]==last_name:
              author[i]=labdict[key]
              labmembers.append(author[i])
              count+=1
        if count==0:
          author[i]=f"{first_name} {last_name}"
    
    link =  pubobj['pub_url'] if 'pub_url'in pubobj else pubobj['eprint'] if 'eprint' in pubobj else ""
    abstract = pub['abstract'] if 'abstract' in pub else title
    template =f"""---
title: "{title}"
date: {date}
authors: {author}
labmembers: {labmembers}
---
{abstract}
- [link]({link})"""
    return template


def get_author_scholar_pubs(author_id, labdict, lag_years=2):
  author = scholarly.search_author_id(author_id)
  author = scholarly.fill(author)
  scholarly.pprint(author)
  current_year = datetime.datetime.now().year
  res_pub = []
  for pub in author['publications']:
      if  'pub_year'in pub['bib'] and int(pub['bib']['pub_year'])>=(current_year-lag_years):
          res_pub.append(scholarly.fill(pub))
          content=fill_template(res_pub[-1], labdict)
          fname = pub['bib']['title'] = pub['bib']['title'].replace("  "," ").replace(":","").replace('"',"'").replace(" ","-")
          fname=fname+".md"
          with open(fname, "w+") as f:
              f.write(content)
          scholarly.pprint(pub)
  return res_pub

labdict = {"Tiago Silva": "Tiago da Silva", "Diego Mesquita": "Diego Mesquita", 
           "Dario Oliveira": "Dario Oliveira", "Eliezer Silva":"Eliezer de S. da Silva", 
           "Luiz Carvalho":"Luiz Max Carvalho",
           "Tamara Pereira":"Tamara Arruda Pereira"}

author_ids={"dario":'Nswjaf0AAAAJ', "diego":'6_FDUGEAAAAJ',
            "tiago":'FLBHiI0AAAAJ', "tamara":'OwB9En0AAAAJ',
            "eliezer":'EK_dBqoAAAAJ'}
res_lst = []
for author in author_ids:
  res_lst.append(get_author_scholar_pubs(author_ids[author], labdict))


# create json res_pubs
import json
with open('pubs.json', 'w') as f:
    json.dump(res_lst, f)




