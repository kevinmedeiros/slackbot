# Variáveis
IMAGE_NAME = slackbot
IMAGE_TAG = latest

# Comandos
build:
	@docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

run:
	@docker run -p 3000:3000 $(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: build run