pipeline {
    agent any
    stages {
        stage ("Cloning code from SCM ") {
            steps {
                git branch: 'dev', url: 'https://github.com/Ankit-dev23/djngo_app.git'
            }
        }

        // Befor Installing requirmenst it required to install virtualenv and create virtual env by below commands
        // install virtualenv --> sudo apt install python3-pip/sudo apt install python3-virtualenv
        // To create virtual env -->  virtualenv --no-site-packages /var/lib/jenkins/envs/medi_app/bin
        // sudo apt install python3-pip -y
        // sudo apt install python3-virtualenv -y
        stage ("Creating Virtual ENV") {
            steps {
                sh """#!/bin/bash
                mkdir /var/lib/jenkins/envs/
		        virtualenv /var/lib/jenkins/envs/${JOB_NAME}
		        """
            }
        }


        stage ("Installing Requirments") {
            steps {
                sh """#!/bin/bash
		        source /var/lib/jenkins/envs/${JOB_NAME}/bin/activate
		        pip install -r requirment.txt
		        """
            }
        }

        stage ("Checking black") {
            steps {
                sh """#!/bin/bash
		        source /var/lib/jenkins/envs/${JOB_NAME}/bin/activate
		        black --check . --color -v
		        """
            }
        }

        stage ("Checking isort") {
            steps {
                sh """#!/bin/bash
		        source /var/lib/jenkins/envs/${JOB_NAME}/bin/activate
		        isort --check .
		        """
            }
        }

        stage ("Checking Django test") {
            steps {
                sh """#!/bin/bash
		        source /var/lib/jenkins/envs/${JOB_NAME}/bin/activate
		        python manage.py test
		        """
            }
        }

        stage ("Checking Coverage") {
            steps {
                sh """#!/bin/bash
		        source /var/lib/jenkins/envs/${JOB_NAME}/bin/activate
		        coverage run manage.py test -v 2 && coverage report --fail-under=90
		        """
            }
        }

        stage ("Building Docker image") {
            steps {
                sh 'docker build -t ishunrzb09/${JOB_NAME}:${BUILD_NUMBER} .' 
            }
        }

        stage ("Login Into Docker Registry") {
            steps {
                sh 'docker login'
            }
        }

        stage ("Publishing Docker Images into Public Registry") {
            steps {
                sh 'docker push ishunrzb09/${JOB_NAME}:${BUILD_NUMBER}'
            }
        }

        // stage ("Removing created images from local system") {
        //     steps {
        //         sh 'docker rmi -f ishunrzb09/${JOB_NAME}:V_${BUILD_NUMBER}'
        //     }
        // }

        // stage ("Pulling created Docker image from remote server") {
        //     steps {
        //         sh 'docker pull ishunrzb09/${JOB_NAME}:${BUILD_NUMBER}'
        //     }
        // }

        // stage ("Removing Old Container") {
        //     steps {
        //         sh 'docker rm -f medical_container'
        //     }
        // }

        // stage ("Spinning Container from downloaded image") {
        //     steps {
        //         sh 'docker run -itd --name=medical_container -p 8000:8000 ishunrzb09/${JOB_NAME}:${BUILD_NUMBER}'
        //     }
        // }
    }
}