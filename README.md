# 🚀 AWS Serverless HRMS Onboarding System

> A production-style serverless HRMS onboarding solution built on AWS that automates employee identity provisioning, document validation, workflow orchestration, IT provisioning, and onboarding progress tracking.

---

# 📌 Project Overview

(Project Description)

---

# 🏗️ Solution Architecture

<p align="center">
<img src="architecture/architecture-diagram.png" width="1000">
</p>

---

# ☁️ AWS Architecture

### AWS Services Used

| Service | Purpose |
|----------|----------|
| Amazon S3 | Static Website Hosting & Document Storage |
| Lambda | Backend Processing |
| API Gateway | REST APIs |
| DynamoDB | Database |
| Cognito | Authentication |
| Step Functions | Workflow |
| SES | Emails |
| SNS | Notifications |
| CloudFront | CDN |

### 📷 AWS Console Architecture

<p align="center">
<img src="screenshots/aws-architecture.png">
</p>

---

# 🌐 Frontend

## 👨‍💼 Employee Portal

- Employee Registration
- Upload Documents
- Track Progress
- Policy Sign-off

### 📷 Employee Portal

<p align="center">
<img src="screenshots/employee-portal.png" width="900">
</p>

---

## 👨‍💼 HR Dashboard

- View Employees
- Approve Employees
- Track Status
- Monitor Workflow

### 📷 HR Dashboard

<p align="center">
<img src="screenshots/hr-dashboard.png" width="900">
</p>

---

# ⚙️ Backend

## Lambda Functions

The backend consists of seven Lambda functions.

| Function | Purpose |
|----------|----------|
| CreateEmployee | Creates employee |
| GetEmployees | Fetch employee data |
| DocumentValidation | Validates uploaded files |
| ITProvisioning | Simulates IT provisioning |
| PolicySignOff | Policy acceptance |
| ManagerIntro | Sends introduction |
| ApproveEmployees | Final HR approval |

### 📷 Lambda Functions

<p align="center">
<img src="screenshots/lambda-functions.png">
</p>

---

# 🔄 Workflow Automation

AWS Step Functions orchestrate the onboarding workflow.

Workflow

- Employee Registration
- Document Upload
- Validation
- IT Provisioning
- Policy Sign-off
- Manager Introduction
- HR Approval

### 📷 Step Functions Workflow

<p align="center">
<img src="screenshots/step-functions.png">
</p>

---

# 🗄️ Database

Employee data and onboarding progress are stored in Amazon DynamoDB.

### 📷 DynamoDB Tables

<p align="center">
<img src="screenshots/dynamodb.png">
</p>

---

# 🔐 Authentication

Amazon Cognito manages employee authentication.

### 📷 Cognito User Pool

<p align="center">
<img src="screenshots/cognito.png">
</p>

---

# 🌍 API Layer

Amazon API Gateway exposes backend APIs.

### 📷 API Gateway

<p align="center">
<img src="screenshots/api-gateway.png">
</p>

---

# 📂 Document Storage

Amazon S3 securely stores employee documents.

### 📷 Amazon S3 Bucket

<p align="center">
<img src="screenshots/s3-bucket.png">
</p>

---

# 📧 Email Notifications

Amazon SES sends

- Welcome Email
- Reminder Email
- HR Notification

### 📷 Amazon SES

<p align="center">
<img src="screenshots/ses.png">
</p>

---

# 📢 HR Notifications

Amazon SNS notifies HR once onboarding is complete.

### 📷 Amazon SNS

<p align="center">
<img src="screenshots/sns.png">
</p>

---

# 🚀 Content Delivery

The frontend is distributed globally using Amazon CloudFront.

### 📷 CloudFront Distribution

<p align="center">
<img src="screenshots/cloudfront.png">
</p>

---

# 🔄 Application Workflow

```text
Employee Registration
        │
        ▼
Create Employee
        │
        ▼
Amazon Cognito
        │
        ▼
Welcome Email
        │
        ▼
Upload Documents
        │
        ▼
Document Validation
        │
        ▼
Step Functions
        │
        ▼
IT Provisioning
        │
        ▼
Policy Sign-off
        │
        ▼
Manager Introduction
        │
        ▼
HR Approval
        │
        ▼
Employee Ready
```

---

# 📂 Project Structure

```text
aws-serverless-hrms-onboarding-system/
│
├── frontend/
├── backend/
├── architecture/
├── screenshots/
└── README.md
```

---

# 🚀 Future Enhancements

- OCR-based document verification
- AI document validation
- MFA Authentication
- GitHub Actions CI/CD
- Terraform/CDK
- CloudWatch Monitoring
- Slack Integration

---

# 👨‍💻 Author

Manjunath S

AWS Certified Cloud Practitioner

Electronics & Communication Engineering (2026)
