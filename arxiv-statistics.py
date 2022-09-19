import codecs
import json

entrada=codecs.open("arxiv-metadata-oai-snapshot.json","r",encoding="utf-8")
cont=0
catall={}
catbil={}
catfinall={}
catfinbil={}
for linia in entrada:
    cont+=1
    #if cont==100000:
    #    break
    linia=linia.rstrip()
    y = json.loads(linia)
    claus=y.keys()
    categories=y["categories"].split(" ")
    for categoryfin in categories:
        category=categoryfin.split(".")[0]
        if not category in catall:
            catall[category]=0
        catall[category]+=1
        if not categoryfin in catfinall:
            catfinall[categoryfin]=0
        catfinall[categoryfin]+=1
    #dict_keys(['id', 'submitter', 'authors', 'title', 'comments', 'journal-ref', 'doi', 'report-no', 'categories', 'license', 'abstract', 'versions', 'update_date', 'authors_parsed'])
    title=y["title"]
           
    abstract=y["abstract"]
    if abstract.find("-----")>-1:
            print(title)
            print(categories)
            print("----")
            print(abstract)
            print("----------------------")
    if "comments" in claus:
        comment=y["comments"]
        if not comment==None and comment.lower().find("french")>-1:
           
           if abstract.find("-----")>-1:
            #print(title)
            #print(categories)
            #print("----")
            #print(abstract)
            #print("----------------------")
            for categoryfin in categories:
                category=categoryfin.split(".")[0]
                if not category in catbil:
                    catbil[category]=0
                catbil[category]+=1
                if not categoryfin in catfinbil:
                    catfinbil[categoryfin]=0
                catfinbil[categoryfin]+=1

sortida=codecs.open("catall.tsv","w",encoding="utf-8")
for ca in catall:
    cadena=ca+"\t"+str(catall[ca])
    sortida.write(cadena+"\n")
sortida.close()

sortida=codecs.open("catfinall.tsv","w",encoding="utf-8")
for ca in catfinall:
    cadena=ca+"\t"+str(catfinall[ca])
    sortida.write(cadena+"\n")

sortida.close()
   
sortida=codecs.open("catbil.tsv","w",encoding="utf-8")
for ca in catbil:
    cadena=ca+"\t"+str(catbil[ca])
    sortida.write(cadena+"\n")
sortida.close()

sortida=codecs.open("catfinbil.tsv","w",encoding="utf-8")
for ca in catfinbil:
    cadena=ca+"\t"+str(catfinbil[ca])
    sortida.write(cadena+"\n")