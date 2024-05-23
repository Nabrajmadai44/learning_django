from rest_framework import serializers
from crud.models import Student, ClassRoom


class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)

    
    
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField(max_length=50)
    
class ClassRoomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["id", "name"]
        
class StudentModelSerializer(serializers.ModelSerializer):
    # classroom = ClassRoomModelSerializer()
    class Meta:
        model = Student
        fields = ["id", "name", "age", "email", "address", "classroom"]
        
    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get("request")
        request = self.context.get("request")
        if request and request.method == "GET":
           fields["classroom"] = ClassRoomModelSerializer() 
        return fields