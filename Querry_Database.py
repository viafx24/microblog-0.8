from app import db
from app.models import User, Citation

u = User.query.get(1)
print(u)

#print(Citation.query.all())

print(Citation.query.get(300))


#citations=Citation.query.order_by(Citation.number).filter(Citation.number>=64).all()
#print(citations)