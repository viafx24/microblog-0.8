from app import db
from app.models import User, Citation


#print(Citation.query.all())

#print(Citation.query.get(300))

u = User.query.get(1)

citation = Citation(text='test',SRR=1,TRT=1,author=u)
db.session.add(citation)
db.session.commit()

print(Citation.query.get(301))
#citations=Citation.query.order_by(Citation.number).filter(Citation.number>=64).all()
#print(citations)
