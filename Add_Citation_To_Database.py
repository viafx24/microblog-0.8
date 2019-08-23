from app import db
from app.models import User, Citation

## technique pour obtenir le nombre max de citation
#Test=Citation.query.order_by(Citation.number.desc()).first()
#print(Test.number)

#print(Citation.query.all())

#print(Citation.query.get(300))








## ajout d'un batch de 10 citations;

#u = User.query.get(1)

#citation = Citation(text='Je sais et je sens que faire du bien est le plus vrai bonheur que le cœur humain puisse goûter.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='L’esprit ressemble à un singe entravé par de nombreux liens, qui ne cesserait de sauter dans tous les sens pour se détacher. Il gesticule tant et si bien qu’il empêche quiconque, y compris lui-même, de défaire un seul nœud. Il faut commencer par le pacifier et le rendre attentif. Calmer le singe ne signifie pas l’immobiliser en le gardant enchainé. Le but est de profiter de ce répit pour lui rendre la liberté.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='Pour celui qui pratique l’amour et la compassion, un ennemi représente l’un des maîtres les plus importants. Sans ennemi, on ne peut pratiquer la patience et la tolérance.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='Il y a une chose dont nous avons toujours besoin : c’est du gardien appelé Attention.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='Et le marin ne rirait-il pas de vous si vous lui disiez que toute la traversée dépend du premier coup de barre ?',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='Le marin en haute mer, le guide de haute montagne, l’artisan consciencieux savent que l’on n’obtient rien de bon en obéissant au caprice du moment.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='L’aspect le plus évident de la vanité est la raideur et la rigidité. On se sent l’esprit raide comme un python qui aurait avalé une proie.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='Une bouffé d’orgueil se dissipe comme une brume matinale chez celui qui sait rester humble.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='L’humilité est la vertu féconde de celui qui mesure tout ce qui lui reste à apprendre et l’étendue du chemin qu’il doit encore parcourir.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citation = Citation(text='Montre-moi plutôt à ne pas exhaler la plainte au milieu de l’adversité.',SRR=1,TRT=1,author=u)
#db.session.add(citation)
#db.session.commit()

#citations=Citation.query.order_by(Citation.number).filter(Citation.number>=299).all()
#print(citations)












## technique pour supprimer une citation et verifier que cela a bien marché
##print(Citation.query.get(302))

#Test=Citation.query.get(302)
#db.session.delete(Test)
#db.session.commit()

#citations=Citation.query.order_by(Citation.number).filter(Citation.number>=299).all()
#print(citations)
