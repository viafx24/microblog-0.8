from app import db
from app.models import User, Citation

## technique pour obtenir le nombre max de citation
#Test=Citation.query.order_by(Citation.number.desc()).first()
#print(Test.number)

#print(Citation.query.all())

#print(Citation.query.get(300))








# ajout d'un batch de 10 citations;

u = User.query.get(1)

citation = Citation(text='Dans le monde, il y a toujours des gens qui ne supportent pas la lumière. C’est parce qu’ils sont eux-mêmes remplis d’ombre.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Jamais il ne fait au méchant l’honneur de croire que la raison ait inspiré un seul de ses actes.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Il n’est pas naturel que celui qui a la force désire beaucoup le pouvoir ; et l’on a souvent remarqué que les athlètes sont rarement méchants.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Le guerrier est un métaphysicien. Le guerrier s’est dessiné un dieu, une justice, des maximes, un ordre humain qu’il croit surhumain. Par un retour sur lui-même que tout homme connaît, il honore en lui-même, plus que tout, ce pouvoir de trouver la loi et de la suivre. D’où la pire injure qu’on puisse lui faire c’est de penser autrement que lui, c’est de vivre d’après d’autres maximes que les siennes ; c’est de mépriser ce qu’il honore.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Le courage vraiment sûr est celui qui s’observe beaucoup et longtemps, qui se couvre d’abord et n’avance qu’à pas lents et calculés.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='L’effort excessif peut aussi résulter de l’impatience ou de l’exaltation, deux états qui ne mènent nulle part. De même qu’il faut de la patience pour faire pousser une récolte, il ne sert à rien de tirer sur les plans pour les faire sortir plus vite.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Ce qui est venu par la fatigue s’en va par le repos.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='C’est pourtant bien à notre esprit que nous avons affaire du matin au soir, et c’est lui qui en fin de compte, détermine la qualité de chaque instant de notre existence. Nos pensées détiennent ainsi l’immense pouvoir de conditionner notre manière d’être.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Ce sont les autres, tous les autres, qui fondent la trame de nos vies et forment la matière de nos existences.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Heureux par-dessus tout celui qui sent la trace de son coup de marteau sur le loquet de sa porte.',SRR=1,TRT=1,author=u)
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
