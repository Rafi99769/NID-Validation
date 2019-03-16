from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import serializers, viewsets
from rest_framework.authentication import BasicAuthentication

from apps.core.models import NID


class NIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NID
        fields = '__all__'


class NIDViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    serializer_class = NIDSerializer
    queryset = NID.objects.all()

    def get_queryset(self):
        nid = self.request.GET.get('nid')
        qs = super().get_queryset()
        if nid is not None:
            qs = qs.filter(number=nid)
        return qs


# @method_decorator(login_required, name='dispatch')
class NIDView(TemplateView):
    template_name = "core/nid.html"
