from rest_framework import serializers

from watchlist.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watchlist', )
        # fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    # platform = StreamPlatformSerializer()
    # platform = serializers.SlugRelatedField(slug_field='name', read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'


# class StreamPlatformSerializer(serializers.ModelSerializer):
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlists = WatchListSerializer(many=True, read_only=True)
    # watchlists = serializers.StringRelatedField(many=True, read_only=True)
    # watchlists = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlists = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-detail')
    
    class Meta:
        model = StreamPlatform
        fields = '__all__'


        extra_kwargs = {
            'url': {'view_name': 'platform-detail',},
            # 'users': {'lookup_field': 'username'}
        }

# class WatchListSerializer(serializers.ModelSerializer):
#     id = serializers.CharField(read_only=True)
#     len_name = serializers.SerializerMethodField() # Extra field
#     # Сколько времени назад было добавлено

#     class Meta:
#         model = Movie
#         fields = '__all__'

#     def get_len_name(self, object):
#         return len(object.name)

#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should be different!')
        
#         return data

#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short!')
        
#         return value

# def name_lenght(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short!')

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_lenght])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validate_data):
#         instance.name = validate_data.get('name', instance.name)
#         instance.description = validate_data.get('description', instance.description)
#         instance.active = validate_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description should be different!')
        
#         return data

    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short!')
        
    #     return value