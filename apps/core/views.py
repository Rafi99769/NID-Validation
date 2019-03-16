from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import serializers, viewsets
from apps.core.models import NID


class NIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = NID
        fields = '__all__'


class NIDViewSet(viewsets.ModelViewSet):
    serializer_class = NIDSerializer
    queryset = NID.objects.all()

    def get_queryset(self):
        nid = self.request.GET.get('nid')
        qs = super().get_queryset()
        qs = qs.filter(number=nid)
        return qs


# @method_decorator(login_required, name='dispatch')
class NIDView(TemplateView):
    template_name = "core/nid.html"
