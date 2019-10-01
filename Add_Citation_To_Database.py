from app import db
from app.models import User, Citation

## technique pour obtenir le nombre max de citation
#Test=Citation.query.order_by(Citation.number.desc()).first()
#print(Test.number)

#print(Citation.query.all())

#print(Citation.query.get(300))

# ajout d'un batch de 10 citations;

u = User.query.get(1)

citation = Citation(text='Bizarre qu’au sein de ce pitoyable spectacle, je n’ai éprouvé nulle haine, bien que les individus de cette espèce m’aient empoisonné la vie douze année durant.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Pourquoi l’individu a-t-il les vices de la société ? La société les lui donne. On est entrainé dans le faux par des parents, par des voisins. On apprend le mal, ensuite on l’enseigne et on arrive à ce comble de dépravation qui concentre dans un seul cœur la science perverse de tous.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Le pire qui puisse advenir est de se mettre dans son tort par rapport aux canailles ; on se fait alors chapitrer par eux, et il n’est juge plus impitoyable que celui qui, premièrement, est dans son droit et deuxièmement, est un coquin.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Chacun sera sot autant qu’il est roi. Exactement autant qu’il fera faire, au lieu de faire.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Il faut une sagesse supérieure pour ne rien supposer jamais des intentions et des pensées d’un homme.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Les êtres se comportent de façon nuisible parce qu’ils sont sous l’emprise de l’ignorance et des poisons mentaux que celle-ci engendre.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='L’ignorance est la cause de tous les maux.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='L’homme réellement fort se sent également responsable de son ennemi.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='La tendance à nuire, à blâmer et à dénigrer est une forme de vanité.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Il faut savoir étiqueter une pensée ou un état d’esprit en « lamentation ».',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Quand rien ne va plus dedans, rien ne va plus dehors. La paix de l’âme est si importante qu’il faut savoir renoncer à ce que l’on entreprend pour ne pas la perdre.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Du seul fait de rester assis à observer à quelle vitesse et avec quel illogisme, mes pensées et mes émotions allaient et venaient, je commençais à voir qu’elles n’étaient pas aussi solides et réelles qu’elles en avaient l’air. Alors, je commençais à lâcher prise sur ma croyance à l’histoire qu’elles avaient l’air de me raconter.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Le mal qui nous afflige puise généralement sa force dans le rétrécissement de notre univers mental. Les pensées ne cessent alors de rebondir contre les parois de cette prison intérieure. Elles s’accélèrent et s’amplifient, chaque rebond nous infligeant de nouvelles meurtrissures. Il faut donc élargir notre horizon intérieur, au point que l’émotion n’ai plus de murs où ricocher sans trêve. Alors les projectiles du malheur vont se perdre dans le vaste espace de la liberté intérieure.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Si parfois je veux m’amuser d’un fou, je n’ai pas loin à chercher, c’est de moi que je rie.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Pendant l’hiver, le gel fige les lacs et les rivières. Avec le printemps, la terre et les eaux se réchauffent : c’est le dégel. Que reste-il alors de la dureté de la glace ? L’eau est douce et fluide, la glace dure et coupante. On ne peut pas dire qu’elles soient identiques ni non plus qu’elles soient différentes, car la glace n’est que de l’eau solidifiée et l’eau de la glace fondue. Il en est de même de nos perceptions du monde extérieur.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Je vous souhaite la bonne humeur. Voilà ce qu’il faudrait offrir et recevoir. Voilà la vraie politesse qui enrichit tout le monde et d’abord celui qui donne. Voilà le trésor qui se multiplie par l’échange. On peut la semer le long des rues, dans les tramways, dans les kiosques à journaux, il ne s’en perdra pas un atome. Elle poussera et fleurira partout où vous l’aurez jeté.',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

citation = Citation(text='Fais que je ne cherche pas tant à être consolé que de consoler, d’être compris que de comprendre, d’être aimé que d’aimer. Parce que c’est en donnant que l’on reçoit. C’est en s’oubliant soi-même qu’on se retrouve.',SRR=1,TRT=1,author=u)
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
