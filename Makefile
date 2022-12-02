run:
	docker pull mcfly17/utoville-homecare-user:dev
	docker stop user
	docker run -d --rm --name user -p 8000:8000 mcfly17/utoville-homecare-user