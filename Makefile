run-user:
	docker pull mcfly17/utoville-homecare-user:dev
	docker stop user
	docker run -d --rm --name user -p 8000:8000 mcfly17/utoville-homecare-user

run-seller:
	docker pull mcfly17/utoville-homecare-seller:dev
	docker stop seller
	docker run -d --rm --name seller -p 8001:8001 mcfly17/utoville-homecare-seller

run-admin:
	docker pull mcfly17/utoville-homecare-admin:dev
	docker stop admin
	docker run -d --rm --name admin -p 8002:8002 mcfly17/utoville-homecare-admin