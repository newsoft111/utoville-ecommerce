node {
    stage('Checkout') {
		checkout changelog: false, poll: false, scm: [
			$class: 'GitSCM',
			branches: [[
				name: "*/main"
			]],
			doGenerateSubmoduleConfigurations: false,
			extensions: [[
				$class: "WipeWorkspace"
			], [
				$class: "CleanBeforeCheckout"
			]],
			submoduleCfg: [],
		]
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