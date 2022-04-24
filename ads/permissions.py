from django.http import Http404
from rest_framework import permissions
from ads.models import User, Ads


class AdsPermission(permissions.BasePermission):
    message = 'Changing ad for non admin or non moderator user not allowed.'

    def has_permission(self, request, view):

        if request.user.role in [User.MODERATOR, User.ADMIN]:
            return True

        try:
            entity = Ads.objects.get(pk=view.kwargs["pk"])
        except Ads.DoesNotExist:
            raise Http404

        if entity.author_id_id == request.user.id:
            return True
        return False