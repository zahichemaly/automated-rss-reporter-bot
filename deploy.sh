echo 'Building container image'
pip freeze > requirements.txt
docker build -t ayabot.azurecr.io/worker:v0.1 .

echo 'Login to registry'
docker login ayabot.azurecr.io

echo 'Pushing image to Azure Registry'
docker push ayabot.azurecr.io/worker:v0.1
