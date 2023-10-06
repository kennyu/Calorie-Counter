import clarifai_grpc
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

# Initialize Clarifai API client
stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

# Get the Food model ID
food_model = stub.GetModel(
    service_pb2.GetModelRequest(model_id='bd367be194cf45149e75f01d59f77ba7'))

# Set up the image
with open('food.jpg', 'rb') as f:
    file_data = f.read()

image = resources_pb2.Image(base64=file_data)

# Make the prediction
response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id='bd367be194cf45149e75f01d59f77ba7',
        inputs=[resources_pb2.Input(data=image)]))

if response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Request failed: " + response.status.description)

# Get the first predicted concept and print the name
concept = response.outputs[0].data.concepts[0]
print(concept.name)
