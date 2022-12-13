node {
	stage('Clean Work Space') {
		cleanWs()
		sh 'pwd'
		sh 'ls'
	}

    stage('Clone repository') {
        checkout scm
    }

    stage('Build image') {
        app = docker.build("mcfly17/utoville-homecare", "--no-cache .")
    }

    stage('Test image') {
        app.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
            app.push("dev")
        }
    }

    stage('SSH docker run') {
        script {
            sshPublisher(
                continueOnError: false, failOnError: true,
                publishers: [
                    sshPublisherDesc(
                        configName: "dev",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "make rerun-homecare")
                        ]
                    )
                ]
            )
        }
    }
}