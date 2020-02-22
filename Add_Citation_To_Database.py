from app import db
from app.models import User, Citation

## technique pour obtenir le nombre max de citation
#Test=Citation.query.order_by(Citation.number.desc()).first()
#print(Test.number)

#print(Citation.query.all())

#print(Citation.query.get(300))

# ajout d'un batch de 10 citations;

u = User.query.get(1)

citation = Citation(text='Hâtons-nous de suivre le conseil de Nietzsche pour qui le meilleur moyen de bien inaugurer la journée consiste à se demander, dès son réveil, si aujourd’hui l’on peut faire plaisir à « au moins un homme ». Tout commence par le prochain.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Quelle que soit la personne que tu regardes, sache qu’elle a déjà plusieurs fois traversé l’enfer.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Les mots de Spinoza disent l’essentiel et me servent de programme : « bien faire et se tenir en joie ».',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='On progresse beaucoup plus en écoutant qu’en parlant. Le proverbe dit : « tu as 2 oreilles et une bouche, ce qui veut dire que tu dois écouter 2 fois plus que tu ne dois parler ».',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Il faut que l’ego s’use comme une vieille chaussure, voyageant de la souffrance à la libération.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='On ne peut être vraiment paisible si l’on ne porte en soi la qualité invincible de la paix.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Vivre c’est être utile à plusieurs.',SRR=1,TRT=1,author=u)
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
