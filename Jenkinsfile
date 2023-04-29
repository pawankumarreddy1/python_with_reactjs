pipeline {
    agent any

    stages {
        stage('CI') {
            steps {
                sh 'git clone git@github.com:pawankumarreddy1/reactjswithpython.git . ' 
                sh 'zip -r apache-html-$BUILD_NUMBER.zip . -i *'
                sh 'aws s3 cp apache-html-$BUILD_NUMBER.zip s3://pavanmanchinti1/'
            }
        }
        stage('CD') {
            steps {
                sh 'rm -fr *'
                sh 'aws s3 cp s3://pavanmanchinti1/apache-html-$BUILD_NUMBER.zip .'
                sh 'unzip apache-html-$BUILD_NUMBER.zip'
                sh 'scp index.html root@172.31.82.39:/var/www/html/'
            }
        }
    }
}
