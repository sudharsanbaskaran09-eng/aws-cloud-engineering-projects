# AWS CI/CD Pipeline with GitHub, CodeBuild, ECR & ECS

## 📌 Project Overview

This project demonstrates a complete CI/CD pipeline on AWS that automatically builds a Dockerized application and deploys it to Amazon ECS whenever changes are pushed to a GitHub repository.

### CI/CD Flow

```text
Developer
    │
    │ git push
    ▼
GitHub Repository
    │
    ▼
AWS CodePipeline
    │
    ▼
AWS CodeBuild
    │
    ├── Build Docker Image
    ├── Authenticate with Amazon ECR
    └── Push Docker Image
            │
            ▼
       Amazon ECR
            │
            ▼
       Amazon ECS
            │
            ▼
     Running Container
```

---

## 🎯 Objectives

- Implement a complete AWS CI/CD workflow.
- Connect GitHub with AWS CodePipeline.
- Automatically build Docker images using AWS CodeBuild.
- Store container images in Amazon ECR.
- Deploy the application to Amazon ECS.
- Automate application deployment after source-code changes.
- Understand IAM permissions required for AWS CI/CD services.

---

## 🛠️ AWS Services Used

| Service | Purpose |
|---|---|
| **GitHub** | Source-code repository |
| **AWS CodePipeline** | CI/CD orchestration |
| **AWS CodeBuild** | Application and Docker image build |
| **Amazon ECR** | Docker image registry |
| **Amazon ECS** | Container deployment and management |
| **IAM** | Permissions and service roles |

---

## 📂 Project Structure

```text
aws-cicd-project/
│
├── Dockerfile
├── buildspec.yml
├── application/
│   └── application files
│
└── README.md
```

---

# 🔄 CI/CD Workflow

## 1. Developer Push

The developer pushes code to the GitHub repository.

```bash
git add .
git commit -m "Update application"
git push origin main
```

---

## 2. Source Stage

AWS CodePipeline detects the new GitHub commit.

```text
GitHub
   ↓
CodePipeline Source Stage
```

The source artifact is passed to the next stage.

---

## 3. Build Stage

AWS CodeBuild receives the source artifact and executes the commands defined in:

```text
buildspec.yml
```

The build process is:

```text
Source Code
    ↓
Docker Build
    ↓
Docker Image
    ↓
Amazon ECR
```

---

## 4. Amazon ECR

The Docker image is pushed to an Amazon ECR repository.

Example:

```text
Amazon ECR
└── aws-cicd-app
    └── latest
```

ECR acts as the private container image registry.

---

## 5. ECS Deployment

Amazon ECS pulls the updated container image and runs the application using the configured ECS cluster, task definition and service.

```text
ECR
 ↓
ECS Task Definition
 ↓
ECS Service
 ↓
Running Container
```

---

# ⚙️ Build Configuration

The project uses a `buildspec.yml` file to define the CodeBuild process.

Example structure:

```yaml
version: 0.2

phases:

  pre_build:
    commands:
      - echo Logging in to Amazon ECR
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com

  build:
    commands:
      - echo Building Docker image
      - docker build -t $IMAGE_REPO_NAME:$IMAGE_TAG .

  post_build:
    commands:
      - echo Pushing Docker image
      - docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$IMAGE_REPO_NAME:$IMAGE_TAG
```

> Adjust the variables and commands according to the actual `buildspec.yml` used in the project.

---

# 🔐 IAM Configuration

During the project, the CodePipeline execution initially failed because the CodePipeline service role did not have permission to pass the CodeBuild service role.

### Error

```text
not authorized to perform: iam:PassRole
```

### Cause

The CodePipeline service role did not have permission to pass the required CodeBuild service role.

### Solution

Added the required:

```text
iam:PassRole
```

permission to the CodePipeline service role for the CodeBuild service role.

Example role:

```text
codebuild-aws-cicd-build-role
```

After adding the required permission, the CodeBuild stage completed successfully.

---

# 🚀 Pipeline Stages

The final pipeline contains three stages:

```text
┌──────────────┐
│    Source    │
│    GitHub    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Build     │
│ AWS CodeBuild│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│    Deploy    │
│  Amazon ECS  │
└──────────────┘
```

### Source

**Provider:** GitHub via GitHub App

Purpose:

- Retrieve application source code
- Detect repository changes
- Provide source artifact to CodeBuild

### Build

**Provider:** AWS CodeBuild

Purpose:

- Build the application
- Build Docker image
- Push image to ECR

### Deploy

**Provider:** Amazon ECS

Purpose:

- Deploy the updated application
- Run the Docker container
- Update the ECS service

---

# 🧪 Testing

A separate **Test stage was not required** for this project.

The implemented pipeline is:

```text
GitHub → CodeBuild → ECS
```

Testing can be added later using services such as:

- AWS CodeBuild
- Automated unit tests
- Integration tests
- API testing
- Container testing

---

# 📸 Project Screenshots

The project screenshots document the implementation and troubleshooting process.

```text
screenshots/
│
├── 01-ecr-repository
├── 02-ecs-cluster
├── 03-ecs-task-definition
├── 04-ecs-deployment-failure
├── 05-codebuild-configuration
├── 06-codebuild-ecr-permission
├── 07-buildspec-docker-context-fix
├── 08-codebuild-success
├── 09-ecr-docker-image
└── 10-aws-cicd-pipeline-success
```

### Final Pipeline Result

The final successful pipeline shows:

```text
🟢 Source  → GitHub
🟢 Build   → AWS CodeBuild
🟢 Deploy  → Amazon ECS
```

---

# 🛠️ Problems Encountered & Solutions

## Problem 1 — CodeBuild Permission Failure

### Error

```text
not authorized to perform: iam:PassRole
```

### Cause

The CodePipeline service role did not have permission to pass the CodeBuild service role.

### Solution

Added the required `iam:PassRole` permission to the CodePipeline service role for the CodeBuild role.

---

## Problem 2 — Docker Build Configuration

The Docker build configuration was adjusted to correctly locate the Dockerfile and application build context.

The `buildspec.yml` was updated accordingly.

---

# ✅ Final Result

The project successfully implements an automated AWS CI/CD pipeline:

```text
       GitHub
          │
          │ Push
          ▼
   AWS CodePipeline
          │
          ▼
    AWS CodeBuild
          │
          │ Docker Build
          ▼
      Amazon ECR
          │
          │ Pull Image
          ▼
      Amazon ECS
          │
          ▼
   Running Application
```

A code push to GitHub can trigger the automated build and deployment workflow.

---

# 📚 Key Concepts Learned

- CI/CD
- GitHub integration with AWS
- AWS CodePipeline
- AWS CodeBuild
- Docker image creation
- Amazon ECR
- Amazon ECS
- ECS Task Definitions
- IAM roles and policies
- `iam:PassRole`
- `buildspec.yml`
- Automated container deployment
- Troubleshooting CI/CD pipeline failures

---

# 🔮 Future Improvements

The pipeline can be extended with:

- Automated unit testing
- Security scanning
- Docker image vulnerability scanning
- AWS CodeDeploy
- Blue/Green deployment
- ECS Fargate
- CloudWatch monitoring
- SNS deployment notifications
- Infrastructure as Code using Terraform
- GitHub branch protection
- Manual approval before production deployment

---

## 🏁 Conclusion

This project demonstrates how to build a practical AWS containerized CI/CD pipeline using GitHub, AWS CodePipeline, AWS CodeBuild, Amazon ECR and Amazon ECS.

It provides an automated path from:

**Source Code → Build → Container Image → Deployment**

and forms a strong foundation for more advanced DevOps and cloud deployment architectures.

