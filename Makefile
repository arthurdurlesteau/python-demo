export appName=python_demo_app

default: build push deploy clean
build:
	docker build ./ -t 'artur98/${appName}:latest'
push:
		docker push 'artur98/${appName}:latest'
compose:
	docker-compose up; cd manifests; kompose convert -f ../docker-compose.yml
deploy:
	kubectl apply -f ./manifests --recursive
destroy:
	kubectl delete -f ./manifests --recursive
clean:
	docker image prune -f;
	rm -rf manifests/*