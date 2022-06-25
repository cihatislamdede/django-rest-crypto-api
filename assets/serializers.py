from rest_framework import serializers

from assets.models import Asset


#create asset serializer
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id', 'symbol', 'name', 'explorer']

    def create(self, validated_data):
        return Asset.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.symbol = validated_data.get('symbol', instance.symbol)
        instance.name = validated_data.get('name', instance.name)
        instance.explorer = validated_data.get('explorer', instance.explorer)
        instance.save()
        return instance

    
