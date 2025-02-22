from .base_serializer import BaseSerializer

class DocumentSerializer(BaseSerializer):
    def serialize(self, obj):
        return {
            "id": obj.meta.id,
            "source": obj.to_dict()
        }
