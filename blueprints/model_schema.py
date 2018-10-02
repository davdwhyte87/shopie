from blueprints.post.models import Post,Comment,Like
from blueprints.user.models import User
from extensions import ma,db


class UserSchema(ma.ModelSchema):
    class Meta:
        model=User
        fields=('id','name','email','image','phone','bio','uname')
        sqla_session = db.session
class CommentSchema(ma.ModelSchema):
    class Meta:
        model=Comment
        sqla_session=db.session
    user=ma.Nested(UserSchema)
class LikeSchema(ma.ModelSchema):
    class Meta:
        model=Like
        field='user_id'
        sqla_session = db.session
class PostSchema(ma.ModelSchema):
    class Meta:
        model=Post
        sqla_session=db.session
    user=ma.Nested(UserSchema)
    comment=ma.Nested(CommentSchema,many=True)
    likes=ma.Nested(LikeSchema,many=True)
    





