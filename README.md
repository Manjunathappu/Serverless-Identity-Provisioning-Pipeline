# 🚀 AWS Serverless HRMS Onboarding System

> A production-style serverless HRMS onboarding solution built on AWS that automates employee identity provisioning, document validation, workflow orchestration, IT provisioning, and onboarding progress tracking.

---

# 📌 Project Overview

Employee onboarding is a critical HR process that often involves multiple manual tasks across HR and IT teams, such as employee registration, identity creation, document verification, software provisioning, policy acknowledgements, and onboarding status tracking. These manual processes can lead to delays, inconsistencies, and increased administrative overhead.

The **AWS Serverless HRMS Onboarding System** addresses these challenges by automating the complete onboarding lifecycle using a scalable, event-driven, serverless architecture on AWS. The application creates employee records, provisions secure user identities, validates onboarding documents, orchestrates onboarding workflows, automates IT provisioning, sends email notifications, and provides real-time visibility into onboarding progress through dedicated employee and HR dashboards.

Built using AWS managed services such as **AWS Lambda, API Gateway, Amazon DynamoDB, Amazon Cognito, AWS Step Functions, Amazon S3, Amazon SES, Amazon SNS, and Amazon CloudFront**, the solution eliminates infrastructure management while ensuring scalability, security, reliability, and cost efficiency.

This project demonstrates practical implementation of serverless application development, RESTful APIs, event-driven workflows, cloud security, identity management, and workflow automation, making it representative of modern cloud-native enterprise applications.

---

# 🎯 Key Features

- Automated employee registration and onboarding
- Identity provisioning using Amazon Cognito
- Secure document upload and validation
- Workflow orchestration using AWS Step Functions
- HR approval workflow
- Automated IT provisioning
- Real-time onboarding progress tracking
- HR administration dashboard
- Employee self-service portal
- Email notifications using Amazon SES
- HR notifications using Amazon SNS
- Secure REST APIs with Amazon API Gateway
- Scalable serverless architecture

---

# 🏗️ Solution Architecture

<p align="center">
<img width="1536" height="1024" alt="Solution Architecture (Identity Pipeline)" src="https://github.com/user-attachments/assets/02434957-61f2-419f-8dc9-5086b691d053" />
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
</p><img width="1385" height="700" alt="architecture_diagram_project_1" src="https://github.com/user-attachments/assets/0e6dc913-9484-4748-bd5f-48993497adf4" />


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
</p><img width="602" height="851" alt="Employee_onboarding_portal" src="https://github.com/user-attachments/assets/0092487c-f891-4b2b-b1cc-a748184df4a7" />


---

## 👨‍💼 HR Dashboard

- View Employees
- Approve Employees
- Track Status
- Monitor Workflow

### 📷 HR Dashboard

<p align="center">
<img src="screenshots/hr-dashboard.png" width="900">
</p><img width="1883" height="249" alt="HR_onboarding_dashboard" src="https://github.com/user-attachments/assets/924e5b08-e01f-4427-9414-303654fc7489" />


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
</p><img width="1250" height="491" alt="Lambda Functions" src="https://github.com/user-attachments/assets/a718f2df-1b18-4e37-9c6f-01ba31b5804b" />


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
</p><img width="856" height="873" alt="Step_function_execution" src="https://github.com/user-attachments/assets/5691e851-75fa-4485-98cf-edfc5d262946" />


---

# 🗄️ Database

Employee data and onboarding progress are stored in Amazon DynamoDB.

### 📷 DynamoDB Tables

<p align="center">
<img src="screenshots/dynamodb.png">
</p><img width="1247" height="412" alt="DynamoDB Tables" src="https://github.com/user-attachments/assets/bedf776b-15d2-4d60-9919-e111136272be" />


---

# 🔐 Authentication

Amazon Cognito manages employee authentication.

### 📷 Cognito User Pool

<p align="center">
<img src="screenshots/cognito.png">
</p><img width="1245" height="216" alt="Cognito User Pool" src="https://github.com/user-attachments/assets/33a899a5-20a6-42e8-b681-a51fa87ca361" />


---

# 🌍 API Layer

Amazon API Gateway exposes backend APIs.

### 📷 API Gateway

<p align="center">
<img src="screenshots/api-gateway.png">
</p><img width="1233" height="552" alt="API Gateway-2" src="https://github.com/user-attachments/assets/b6fb0644-373f-4a07-b897-4b9e0d667332" />


---

# 📂 Document Storage

Amazon S3 securely stores employee documents.

### 📷 Amazon S3 Bucket

<p align="center">
<img src="screenshots/s3-bucket.png">
</p><img width="1530" height="417" alt="S3 Documents bucket" src="https://github.com/user-attachments/assets/7351d16c-47fb-4d62-8e62-ce9550045fa7" />


---

# 📧 Email Notifications

Amazon SES sends

- Welcome Email
- Reminder Email
- HR Notification

---

# 📢 HR Notifications

Amazon SNS notifies HR once onboarding is complete.

### 📷 Amazon SNS

<p align="center">
<img src="screenshots/sns.png">
</p><img width="1242" height="207" alt="SNS Topic" src="https://github.com/user-attachments/assets/2fa40359-918f-4301-a53e-e45974788194" />


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

S Manjunath

AWS Certified Cloud Practitioner
