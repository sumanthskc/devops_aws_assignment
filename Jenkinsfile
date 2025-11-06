def AWS_CREDENTIALS_ID="4b45ce94-9f38-4058-b72a-b1241d2b068c"
def BUCKET_NAME="devops-eval-buck-1"
pipeline{

    agent any
    stages{
        stage("checkout repo"){
            steps{
                git url: "https://github.com/sumanthskc/new_devops_test-1.git" , branch: "feature"
            }
        }
        stage("ziping and uploading"){
            steps {
                
                sh "zip lambda_function.zip lambda_function.py"
                withCredentials([aws(credentialsId: AWS_CREDENTIALS_ID, variablePrefix: 'AWS')]) {
                    sh 'aws s3 lambda_function.zip s3://devops-eval-buck-1'
                }
        }
        }
        stage("updating bucket"){
            steps{

                withCredentials([aws(credentialsId: AWS_CREDENTIALS_ID, variablePrefix: 'AWS')]){
                sh "aws lambda update-function-code \
                --function-name lambda_handler \
                --s3-bucket devops-eval-buck-1  \
                --s3-key lambda_function.zip \
                --publish"
                }

            }
        }
    }
}