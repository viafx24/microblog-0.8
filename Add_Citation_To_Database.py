from app import db
from app.models import User, Citation

## technique pour obtenir le nombre max de citation
#Test=Citation.query.order_by(Citation.number.desc()).first()
#print(Test.number)

#print(Citation.query.all())

#print(Citation.query.get(300))

# ajout d'un batch de 10 citations;

u = User.query.get(1)

citation = Citation(text='Je tiens note de ma dépense. Je ne puis me flatter de ne rien perdre ; mais ce que je perds et le pourquoi et le comment, je puis le dire, je puis rendre compte de ma gêne.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Il ne faut pas de leçons pour se résoudre à coucher au besoin sur des roses. Il en faut pour s’endurcir aux tortures et n’y point subordonner sa foi.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Quand on ne va pas bien, on fait de l’archéologie et on finit par déterrer les fragments du passé. Fragments désignés d’emblée comme l’origine du chaos actuel.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='La colère avec sa racine empoisonnée et sa pointe de miel.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Le grand obstacle c’est toujours la représentation et non la réalité.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='En nous résignant à être en permanence la victime de nos pensées, nous ressemblons au chien qui court après chaque pierre qu’on lui lance. Pourtant si nous examinons la situation avec un peu de recul, nous lui trouverons très souvent un aspect comique : en proie aux tourments de l’ego, nous sommes pareils à un gamin qui trépigne de rage parce qu’on a contrarié ses caprices. Alors, nous ne sommes plus le chien courant après chaque pierre, mais le Lion à qui on ne peut en lancer qu’une, car au lieu de la poursuivre, il se retourne vers le lanceur.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Epictète recommandait à ses disciples de s’exercer d’abord dans les petites choses, afin de créer une habitude. Les bonheurs répétés sont souvent le fruit d’une ascèse qui, au sens étymologique, signifie « exercice » en grec.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Il est facile d’être patient quand tout va bien. Ce sont justement les situations difficiles qui nous mettent au défi de renforcer cette vertu cardinale qu’est la patience. Se souvenir d’en faire une pratique régulière.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Le rire soulève une des plus légères affections de l’âme ; il ne voit rien de grand, de sévère ni même de sérieux dans tout notre vain appareil.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()



citations=Citation.query.order_by(Citation.number).filter(Citation.number>=299).all()
print(citations)




## technique pour supprimer une citation et verifier que cela a bien marché
##print(Citation.query.get(302))

#Test=Citation.query.get(302)
#db.session.delete(Test)
#db.session.commit()

#citations=Citation.query.order_by(Citation.number).filter(Citation.number>=299).all()
#print(citations)
