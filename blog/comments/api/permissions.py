from rest_framework.permissions import BasePermission
from comments.models import Comment


class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            # traigo el id del comment que se está queriendo editar:
            id_comment = view.kwargs['pk']
            # uso esa id para traer el com entero de la db:
            comment = Comment.objects.get(pk=id_comment)

            # busco id del user que mandó la request
            id_user = request.user.pk
            # y el id del user que creó el comentario
            id_user_comment = comment.user_id

            # y los comparo
            if id_user == id_user_comment:
                return True

            return False

