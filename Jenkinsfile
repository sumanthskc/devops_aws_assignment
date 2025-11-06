def AWS_CREDENTIALS_ID="78837e91-ad17-4100-b91f-77dde81cdef2"
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