# devops-capstone-project

Final Project for the entire course.
Thank you for making me reach to this level.

![Build Status](https://github.com/KavyashreeDalawai/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)


[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](https://shields.io/)

This repository contains the starter code for the project in [**IBM-CD0285EN-SkillsNetwork DevOps Capstone Project**](https://www.coursera.org/learn/devops-capstone-project?specialization=devops-and-software-engineering) which is part of the [**IBM DevOps and Software Engineering Professional Certificate**](https://www.coursera.org/professional-certificates/devops-and-software-engineering)

## Usage

You should use this template to start your DevOps Capstone project. It contains all of the code that you will need to get started.

Do Not fork this code! It is meant to be used by pressing the  <span style=color:white;background:green>**Use this Template**</span> button in GitHub. This will copy the code to your own repository with no connection back to the original repository like a fork would. This is what you want.

## Development Environment

These labs are designed to be executed in the IBM Developer Skills Network Cloud IDE with OpenShift. Please use the links provided in the Coursera Capstone project to access the lab environment.

Once you are in the lab environment, you can initialize it with `bin/setup.sh` by sourcing it. (*Note: DO NOT run this program as a bash script. It sets environment variable and so must be sourced*):

```bash
source bin/setup.sh
```

This will install Python 3.9, make it the default, modify the bash prompt, create a Python virtual environment and activate it.

After sourcing it you prompt should look like this:

```bash
(venv) theia:project$
```

## Useful commands

Under normal circumstances you should not have to run these commands. They are performed automatically at setup but may be useful when things go wrong:

### Activate the Python 3.9 virtual environment

You can activate the Python 3.9 environment with:

```bash
source ~/venv/bin/activate
```

### Installing Python dependencies

These dependencies are installed as part of the setup process but should you need to install them again, first make sure that the Python 3.9 virtual environment is activated and then use the `make install` command:

```bash
make install
```

### Starting the Postgres Docker container

The labs use Postgres running in a Docker container. If for some reason the service is not available you can start it with:

```bash
make db
```

You can use the `docker ps` command to make sure that postgres is up and running.

## Project layout

The code for the microservice is contained in the `service` package. All of the test are in the `tests` folder. The code follows the **Model-View-Controller** pattern with all of the database code and business logic in the model (`models.py`), and all of the RESTful routing on the controller (`routes.py`).

```text
├── service         <- microservice package
│   ├── common/     <- common log and error handlers
│   ├── config.py   <- Flask configuration object
│   ├── models.py   <- code for the persistent model
│   └── routes.py   <- code for the REST API routes
├── setup.cfg       <- tools setup config
└── tests                       <- folder for all of the tests
    ├── factories.py            <- test factories
    ├── test_cli_commands.py    <- CLI tests
    ├── test_models.py          <- model unit tests
    └── test_routes.py          <- route unit tests
```

## Data Model

The Account model contains the following fields:

| Name | Type | Optional |
|------|------|----------|
| id | Integer| False |
| name | String(64) | False |
| email | String(64) | False |
| address | String(256) | False |
| phone_number | String(32) | True |
| date_joined | Date | False |

## Your Task

Complete this microservice by implementing REST API's for `READ`, `UPDATE`, `DELETE`, and `LIST` while maintaining **95%** code coverage. In true **Test Driven Development** fashion, first write tests for the code you "wish you had", and then write the code to make them pass.

## Local Kubernetes Development

This repo can also be used for local Kubernetes development. It is not advised that you run these commands in the Cloud IDE environment. The purpose of these commands are to simulate the Cloud IDE environment locally on your computer. 

At a minimum, you will need [Docker Desktop](https://www.docker.com/products/docker-desktop) installed on your computer. For the full development environment, you will also need [Visual Studio Code](https://code.visualstudio.com) with the [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension from the Visual Studio Marketplace. All of these can be installed manually by clicking on the links above or you can use a package manager like **Homebrew** on Mac of **Chocolatey** on Windows.

Please only use these commands for working stand-alone on your own computer with the VSCode Remote Container environment provided.

1. Bring up a local K3D Kubernetes cluster

    ```bash
    $ make cluster
    ```

2. Install Tekton

    ```bash
    $ make tekton
    ```

3. Install the ClusterTasks that the Cloud IDE has

    ```bash
    $ make clustertasks
    ```
Scenario:
You have been asked by the customer account manager at your company to
develop an account microservice to keep track of the customers
on your e-commerce website. Since it is a microservice, it is expected
to have a well-formed REST API that other microservices can call.
This service initially needs to create, read, update, delete,
and list customers.

You have also been told that someone else has started on this task.
They have already developed the database model and a Python
Flask-based REST API with an endpoint to create a customer account.

Tasks that need to be completed:
- Create and execute sprint plans
- Develop a RESTful Service using Test Driven Development (TDD)
- Add Continuous Integration (CI) and Security to the Repository
- Deploy the application to Kubernetes
- Build an automated CD DevOps Pipeline

Information about the Project
General
Client: Myself
Project Goal: Demonstrate the knowledge gained in the IBM Program DevOps and Software Engineering with a Capstone Project.
Number of Project Participants: 1 (Cloned repository of IBM. Developed the rest on my own)
Time Period: july 2026
Industry / Area: DevOps, Software Engineering
Role: Developer
Languages: English
Result: Successfully built an account microservice. Demonstrated skills and acquired new knowledge.

Tech Stack
With regard to my role:

GitHub (Version Control, Kanban Board, Actions, ...)
IBM Cloud IDE (based on Theia and Container)
Programming Language: Python
Python Webframework: Flask
Python Unittest Framework: nose
Python Linting: Flake8
Containerization: Docker
Container Orchestration: Kubernetes / OpenShift
Image Registry: IBM Cloud Container Registry
CI/CD Tool: Tekton


To accomplish the scenario follow the steps below:
What I have done as Part of the Project?
Task 1 - Creating and executing Sprint Plans
The RESTful microservice is created with the help of an agile plan (Scrum).
This means, the first task is the Sprint 0.

The main goal of Sprint 0 is to set up the team for future delivery by creating the basic project skeleton, defining the vision and preparing the product backlog.

First, a user story template was created (can be found in: .github/ISSUE_TEMPLATE):
Ensure that you have a new folder in your repository with name .github/ISSUE_TEMPLATE. This folder will contain your new user story template named user-story.md.
To create a user story template first go to code page of your repository, click on settings, scroll down and go to features and choose create template, give the name and description , copy paste the above gerkins synatx and save the template . this will create a folder .github/ISSUE_TEMPLATE save the file under this folder as user-story.md.
<img width="1916" height="912" alt="image" src="https://github.com/user-attachments/assets/4c5a965c-1bb2-4a9c-90a2-a9e1687c4407" />

The template provides the basis for the user stories to be created for the sprints.
It uses the Gherkin Syntax.
Gherkin is a simple description language with very few rules for the structured formulation of scenarios in the context of behavior-driven software development according to BDD principles.
<img width="1892" height="903" alt="image" src="https://github.com/user-attachments/assets/18679649-81d6-4341-8f95-ed472188009c" />
<img width="1890" height="903" alt="image" src="https://github.com/user-attachments/assets/8e7c0146-0952-49e8-8153-cccdf9662aa1" />

Next, the user stories were created.
The titles were provided by IBM as part of the project (e.g. Update an account in the service) and I filled them with content.
Two examples (Note: Screenshots were taken later, therefore they are already labeled and assigned to a project):


Step 1: Create a GitHub Kanban board in your repository
In this exercise, you will set up a kanban board using GitHub Projects for the created repository.

Set up your GitHub kanban board by incorporating the seven columns give below:
New issues
Icebox
Product backlog
Sprint backlog
In progress
Review/QA
Done

Create a user story template
In this exercise, you will create a user story template that will help you write well-formatted user stories for your GitHub kanban board.

Steps to be performed
Create a template for your project’s GitHub repository. Ensure the template includes the components listed below. You may want to copy, paste, and then edit this text because it also contains the correct markdown syntax you will need for the template.
**As a** [role]  
**I need** [function]  
**So that** [benefit]  
      
### Details and Assumptions
    * [document what you know]      
### Acceptance Criteria     
    gherkin 
    Given [some context]
    When [certain action is taken]
    Then [the outcome of action is observed]


Assemble your product backlog
In this exercise, you will create user stories based on the customer accounts microservice for the e-commerce capstone project. The accounts service will have basic customer information like names and addresses.

Create seven user stories in your GitHub kanban board, one for each of the following steps of your project:
1. Setup the development environment
2. Read an account from the service
3. Update an account in the service
4. Delete an account from the service
5. List all accounts in the service
6. Containerize your microservice using Docker
7. Deploy your Docker image to Kubernetes

Ensure that all your stories are listed in the New Issues pipeline.
you will begin to conduct Backlog Refinement by inspecting the issues in the New Issues pipeline and moving them to the Product Backlog or Icebox depending on when you plan to work on them. Containerizing with Docker and deploying to Kubernetes is something you will do a few sprints from now, so it is not immediately important.

1. Determine which user stories you will work on immediately and move them from the New Issues pipeline to the Product Backlog pipeline.
    1. Setup the development environment
    2. Read an account from the service
    3. Update an account in the service
    4. Delete an account from the service
    5. List all accounts in the service

2. Move the remaining stories from New Issues into the Ice box as you will work on them later.
    6. Containerize your microservice using Docker
    7. Deploy your Docker image to Kubernetes

Refine your product backlog
    1.Make sure that all the stories in the Product Backlog have sufficient details to be considered “sprint ready.” Pay special attention to the Acceptance Criteria to be sure that you have defined the definition of “done.”

2.Create a label called technical debt with a yellow color code and add it to your repository.

3.Assign labels to your stories. Remember that anything that brings value to the customer is an enhancement, and technical debt can be things that developers need but provide no visible customer value.

4.Rank the stories in the Product Backlog from highest to lowest priority by dragging them higher or lower in the pipeline column, respectively. Think about the order in which you should implement them.


Note: If you have added the labels but cannot see them on the kanban board, please follow these steps:

1. Open the dropdown menu next to the Backlog (highlighted as 1 in the screenshot below).
2. Select the arrow next to the Fields option (highlighted as 2).
3. Drag and drop Labels from the Hidden fields list to the Visible fields list (highlighted as 3).
4. Select Save to save the changes.

<img width="1876" height="863" alt="image" src="https://github.com/user-attachments/assets/c5611b57-86f0-414a-82b3-a02d8f4cc749" />


Build your first sprint from your product backlog
In this exercise, you will populate your first Sprint Backlog from your Product Backlog. Typically, you create a sprint plan with your entire team during the sprint planning meeting. But since you are completing this project by yourself, you will have to simulate that meeting.

Steps to be performed
1. Set up three sprints (Sprint 1, Sprint 2, and Sprint 3) in GitHub and make the sprints one week in duration.

2. Open the first story from the top of the Product Backlog and assign estimated story points to it. For now, use the scale 3, 5, 8, 13 = S, M, L, XL.

3. Assign the current story to Sprint 1.

4. Close the current story and move it from the Product Backlog to the Sprint Backlog, being careful to preserve its ranked order. For example, the story at the top of the Product Backlog would remain the top story in Sprint Backlog.

5. Repeat steps 3–5 for the remaining four stories in the Product Backlog, preserving their ranked order.

* Click here for a checklist.

    1. Ensure each of these stories is "sprint ready" by checking the following:
    
    1.1 Each story has a label
    
    1.2 Each story has an estimate
    
    1.3 Each story is assigned to Sprint 1
The priorities of the issues in the backlog have also been defined.
P0 is the highest priority and is therefore listed at the top.
P2 is the lowest priority and is therefore listed at the bottom.
This completes first Task and now Task 2 can be started.

REST API Guidelines
The REST API guidelines were specified by IBM:
<img width="610" height="815" alt="image" src="https://github.com/user-attachments/assets/debc44a1-76d7-4ad5-9772-9f3e9d609ece" />

<img width="610" height="815" alt="image" src="https://github.com/user-attachments/assets/39ad73a5-9843-4f20-8b1c-e653a60bae16" />
Step 2: Setting up the Development Environment
Something is missing in the set-up of the development environment: Configuring the nosetests command with additional options.
This will save us typing work when carrying out unit tests in the future.

The modified setup.cfg file:
<img width="951" height="830" alt="image" src="https://github.com/user-attachments/assets/021f7f67-8b76-40c0-b246-aa1f32d97bfc" />
This completes the user story for setting up the development environment and the Kanban board is updated:
<img width="1907" height="913" alt="image" src="https://github.com/user-attachments/assets/303f3392-e7cb-4782-89f7-13ccff360155" />
At the same time, the next user story was defined: Read an account from service (see column In Progress).
Implementing API Endpoint - Read an Account
Following the TDD approach, the test cases to be fulfilled were defined first:
<img width="1359" height="843" alt="image" src="https://github.com/user-attachments/assets/7295e6d3-9192-418e-addb-b582605400bf" />
The code was then written to fulfill the tests.
The code coverage is more than 95%.
This means that everything fits.
<img width="1371" height="842" alt="image" src="https://github.com/user-attachments/assets/541d2474-f9f5-4f96-82d1-79619f8f8830" />
At the same time, the next user story was defined: Update an account from service (see column In Progress):
<img width="1900" height="905" alt="image" src="https://github.com/user-attachments/assets/d7f45458-e3ce-420c-bcf9-b8bb08594e60" />

Implementing API Endpoint - Update an Account
Following the TDD approach, the test cases to be fulfilled were defined first:
<img width="1392" height="851" alt="image" src="https://github.com/user-attachments/assets/a9c01716-8be3-4009-9f21-6690282149f2" />
<img width="1395" height="841" alt="image" src="https://github.com/user-attachments/assets/3812e099-7a70-4ae4-b631-3b0b20bbed97" />

The code was then written to fulfill the tests.
The code coverage is more than 95%.
This means that everything fits.
<img width="1393" height="846" alt="image" src="https://github.com/user-attachments/assets/165fec4f-ecbc-4ae1-bc2b-12e733205fe5" />
At the same time, the next user story was defined: Delete an account from service (see column In Progress):
<img width="1903" height="913" alt="image" src="https://github.com/user-attachments/assets/f8d91ea5-6b6a-40cd-8157-d39f9575d3d3" />
Implementing API Endpoint - Delete an Account
Following the TDD approach, the test cases to be fulfilled were defined first:
<img width="1409" height="840" alt="image" src="https://github.com/user-attachments/assets/d5f71696-dee9-43da-ae27-7690e910d9b7" />
The code was then written to fulfill the tests.
The code coverage is more than 95%.
This means that everything fits.
<img width="1361" height="844" alt="image" src="https://github.com/user-attachments/assets/5ec971c4-9c4f-4ea9-9395-7a4cf632c5c9" />
At the same time, the next user story was defined: List all accounts from service (see column In Progress):
<img width="1909" height="915" alt="image" src="https://github.com/user-attachments/assets/814030cc-0afb-4b2f-a976-460d18dcdeaa" />
Implementing API Endpoint - List all Accounts
Following the TDD approach, the test cases to be fulfilled were defined first:
<img width="1398" height="842" alt="image" src="https://github.com/user-attachments/assets/c6486f3d-b24f-4ce0-99ca-bb8095e010cd" />
The code was then written to fulfill the tests.
The code coverage is more than 95%.
This means that everything fits.
<img width="1322" height="852" alt="image" src="https://github.com/user-attachments/assets/64c593ca-8fad-4d91-a7f6-a6037484b117" />
<img width="1911" height="909" alt="image" src="https://github.com/user-attachments/assets/b7c9c28e-b19b-4e3d-be2b-3cf2c6aed5d6" />
Improving Total Code Coverage
The total code coverage is currently below 95 %.
There is a lot of potential for improvement in some areas (e.g. error_handlers.py file):
<img width="628" height="389" alt="image" src="https://github.com/user-attachments/assets/d5b001da-fc7e-4e79-8a79-135dad223e27" />
A new test file was created to test the error handlers: tests/test_error_handlers.py.
The test suite for error handlers was set up (setup and teardown) and the unit tests were written:
<img width="1229" height="850" alt="image" src="https://github.com/user-attachments/assets/23873edf-be99-4328-a8c1-054eb840fe9a" />
The goal was achieved: The total code coverage is now above 95 %.
<img width="1225" height="846" alt="image" src="https://github.com/user-attachments/assets/72dc6736-c8d6-4e31-9ae5-cf5ced1ea8b2" />
Demonstration of the REST API
First, local access to the service is enabled.
The following command is used to refresh the database:
flask db-create
Then use the command below to start the service with the new database:
make run
Terminal output:
<img width="976" height="183" alt="image" src="https://github.com/user-attachments/assets/a0f72f08-3fb4-4962-b38a-8847bd4e4e1a" />
The application is started using the Launch Application function in the IBM Cloud IDE.
A port number is also required to start the application.
<img width="678" height="341" alt="image" src="https://github.com/user-attachments/assets/6ae1d06f-2376-4168-a68a-923d3f062caa" />
According to the terminal, the application listens to port 5000, so port 5000 is entered / required.
The output:
<img width="868" height="147" alt="image" src="https://github.com/user-attachments/assets/4ed1e4ee-71b9-4056-83f8-57c49d33d907" />
The service is now running.
The curl command is used to make REST calls to the implemented endpoints.
The demonstration of Create an Account endpoint using the following command:
curl -i -X POST http://127.0.0.1:5000/accounts \
-H "Content-Type: application/json" \
-d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1212"}'
<img width="916" height="163" alt="image" src="https://github.com/user-attachments/assets/054042f7-fa5a-494e-802f-d45c4d3095fb" />
The demonstration of List all Accounts endpoint using the following command:
curl -i -X GET http://127.0.0.1:5000/accounts
<img width="933" height="122" alt="image" src="https://github.com/user-attachments/assets/91ec12b6-57c2-435e-b137-c24666e72913" />
The demonstration of Read an Account endpoint using the following command:
curl -i -X GET http://127.0.0.1:5000/accounts/1
<img width="915" height="121" alt="image" src="https://github.com/user-attachments/assets/8b118c40-58ef-4d3a-924a-ffff9fe4ef3c" />
The demonstration of Update an Account endpoint using the following command:
curl -i -X PUT http://127.0.0.1:5000/accounts/1 \
-H "Content-Type: application/json" \
-d '{"name":"John Doe","email":"john@doe.com","address":"123 Main St.","phone_number":"555-1111"}'
<img width="918" height="148" alt="image" src="https://github.com/user-attachments/assets/cc258090-3643-4522-a1a4-02446b89a6a1" />
The difference: The phone number ends now with a 1 instead of 2 (555-1112 -> 555-1111).

The demonstration of Delete an Account endpoint using the following command:
curl -i -X DELETE http://127.0.0.1:5000/accounts/1
<img width="524" height="211" alt="image" src="https://github.com/user-attachments/assets/da06d20b-624a-449f-97d5-1ad54e580d2c" />
After deletion, all accounts were displayed to show that the account had actually been deleted.
The list is empty, so the account has been deleted.

The REST API has been finished, Sprint 1 is now complete and the next task can now be started: Task 3 - Add Continuous Integration and Security to the Repository.

Task 3 - Adding Continuous Integration and Security to the Repository
Additional Scenario and Planning Sprint 2
In Task 3, a new scenario was added (defined by IBM):
Management has been looking for ways to increase developer productivity
and has noticed that developers spend a lot of time checking
that all the tests pass before approving each pull request.
Management has decided it is time to automate this task
by implementing continuous integration (CI) using GitHub Actions.

There have also been many stories in the news about security breaches
and exploits, and management is concerned about the security of your microservice.
In an effort to be proactive, they have decided that you need to
add defensive security measures to your microservice in the
form of security headers and cross-origin resource sharing (CORS) policies.

Two new user stories were created to fulfill the requirements.
This time, these were specified by IBM.
As Sprint 1 is complete, Sprint 2 is also planned. The newly created user stories are added here.

The first user story - Need the Ability to Automate Continuous Integration Checks:

<img width="1298" height="895" alt="image" src="https://github.com/user-attachments/assets/0ebab5cb-1977-4a62-8337-625a556e9119" />

The second user story - Need to Add Security Headers and CORS Policies:

<img width="1310" height="845" alt="image" src="https://github.com/user-attachments/assets/d6857baf-1883-40a9-aa2f-7bdf6556e70c" />
The updated Kanban Board / Sprint Plan 2:

<img width="1903" height="894" alt="image" src="https://github.com/user-attachments/assets/c108e21d-036b-473f-b10f-18652d08d944" />
Implementing Continuous Integration Automation
A key practice in DevOps is Continuous Integration (CI), where developers continuously integrate their code into the main branch by making frequent pull requests.
To make life easier for developers, a CI pipeline is now being implemented with the help of GitHub Actions.

I assign the user story in the Kanban board to myself and move it to the In Progress column:
<img width="1903" height="910" alt="image" src="https://github.com/user-attachments/assets/a4837cf6-a3fa-4ba6-8b91-42b3b38fca54" />
The implemented YAML file (.github/workflows/ci-build.yaml) for the Github Actions workflow:
<img width="1495" height="738" alt="image" src="https://github.com/user-attachments/assets/f6d86969-e4e2-4770-bb82-e94d3b026c63" />
<img width="1150" height="607" alt="image" src="https://github.com/user-attachments/assets/ad4e7c68-f749-4e33-aea1-a153d1cc746b" />
<img width="991" height="347" alt="image" src="https://github.com/user-attachments/assets/efa44e8f-e129-4e00-a865-74ab251881d3" />
This completes all the acceptance criteria of the CI user story and the Kanban board can be updated.
The CI user story was moved to the Done column and at the same time the next user story (Need to Add Security Headers and CORS Policies) was moved to the In Progress column:
<img width="1913" height="893" alt="image" src="https://github.com/user-attachments/assets/7392b671-85f1-4345-b3e5-1de0897cbda2" />
Implementing Security Headers and CORS Policies
The next step is to increase the security of the microservice.

First, security headers are implemented with the help of Flask Talisman.
Flask Talisman forces the REST API clients to use the HTTPS protocol.

Following the TDD approach, the test cases to be fulfilled were defined first:
<img width="878" height="444" alt="image" src="https://github.com/user-attachments/assets/ec3c1455-733a-40f0-8f33-5d9228603b0b" />
<img width="807" height="816" alt="image" src="https://github.com/user-attachments/assets/041e1b85-3db8-4a29-919a-b216158df215" />
Regarding the options / values of the headers:
More information can be found in the Flask documentation or here: https://github.com/GoogleCloudPlatform/flask-talisman

To fulfill the tests, Flask Talisman dependency was installed and a Talisman instance was created after the Flask app instantiation.
The result is that all our previous tests fail... at least our newly written security unit test works

<img width="1235" height="827" alt="image" src="https://github.com/user-attachments/assets/6bbd5378-b226-4ed6-9a39-e72d217ec484" />
The reason for the failure is that Talisman enforces HTTPS - this is good in the production system, but not in testing, as HTTP is used here.
Therefore, the HTTPS enforcement is switched off in the test_XXXX.py files.
As a result, all our tests work again (including the newly written security unit test):
<img width="1210" height="840" alt="image" src="https://github.com/user-attachments/assets/59c75bd6-d518-402d-ac18-254446132e91" />
We can test the security headers with the following command:
curl -I localhost:5000
Before the security headers were added:
<img width="999" height="320" alt="image" src="https://github.com/user-attachments/assets/1b6b423a-0103-4311-ab6e-3a937b642f28" />
After the security headers have been added:
<img width="978" height="342" alt="image" src="https://github.com/user-attachments/assets/fd098935-eb0f-4397-ba27-4b75b4beba62" />
The options such as X-Frame-Options or Content-Security-Policy are included - everything works as intended.
The status code is 302 FOUND instead of 200 OK, as the curl command searches for HTTP by default but finds / redirects to HTTPS (see Location in header).

Now the second part of the security user story: Adding CORS policies.

Following the TDD approach, the test cases to be fulfilled were defined first:

<img width="889" height="668" alt="image" src="https://github.com/user-attachments/assets/c41d3a3b-bb07-4f25-9496-e45cfc9dd617" />
To fulfill the tests, Flask CORS dependency was installed and a CORS instance was created after the Flask app instantiation.
The result: All tests were successful:
<img width="1326" height="815" alt="image" src="https://github.com/user-attachments/assets/70524bb2-9ffb-405d-9494-d5c75f728e55" />
We can test the CORS policies with the following command:
curl -I localhost:5000
The CORS policy is now also displayed (see red marking):
<img width="1093" height="292" alt="image" src="https://github.com/user-attachments/assets/b09c6ef7-6211-49e8-9328-89e1987195c3" />
The Security user story in the Kanban Board is moved to the Done column:
<img width="1907" height="890" alt="image" src="https://github.com/user-attachments/assets/859862cf-1bbb-43ec-a629-aa6c196eed17" />
This ends Sprint 2 and we can start with the next task (Deploy the Application to Kubernetes).

Task 4 - Deploying the Application to Kubernetes
Additional Scenario and Planning Sprint 3
In Task 4, a new scenario was added (defined by IBM):

Management has been very pleased with the changes you have been making.
It's now time to create a sprint plan to implement the last two stories in your Product Backlog,
which are "Containerize your microservice using Docker" and "Deploy your Docker image to Kubernetes."

One more thing. There is a new requirement.
You did such a great job automating the CI pipeline with GitHub Actions that all of the
developers seem much happier because of it. Management has decided that if a little automation
is good, then more automation would be better. They would like you to automate the deployment
to Kubernetes using Tekton once you have figured out how to do it manually.

One new user stories were created to fulfill the requirements.
The content was specified by IBM:

<img width="1260" height="832" alt="image" src="https://github.com/user-attachments/assets/e41d904b-ddd4-4b78-bf55-3ee4420a244e" />
As Sprint 2 is complete, Sprint 3 is also planned. The newly created user story is added here.

The updated Kanban Board / Sprint Plan 3:
<img width="1907" height="887" alt="image" src="https://github.com/user-attachments/assets/0dd98d6a-b8ce-4929-868d-23522d6e8b34" />
These stories are now being implemented.
Containerizing the Microservice using Docker
The user story Containerize microservice using Docker was moved to the Progress column and assigned to me.
The updated Kanban board:

<img width="1910" height="884" alt="image" src="https://github.com/user-attachments/assets/af3c9479-828c-4743-8cde-0499af651b71" />
An image is required to create a container.
And to create an image, a Dockerfile is required.
Therefore, the Dockerfile is implemented first:
<img width="718" height="459" alt="image" src="https://github.com/user-attachments/assets/e9ef16d9-a966-4aaf-a82c-d226d0c8f41f" />
The Docker image is then built and the repository is tagged as accounts with the following command:
docker build -t accounts .
Check whether an image has been created with the following command:
docker images
The output which looks good:
<img width="435" height="61" alt="image" src="https://github.com/user-attachments/assets/98a83cd9-ba57-4379-8fe5-440a2ad3defc" />
A container was then created using the image with the following command:
docker run --rm \
    --link postgresql \
    -e DATABASE_URI=postgresql://postgres:postgres@postgresql:5432/postgres \
    -p 8080:8080 \
    accounts

Explanation (see Docker documentation as well):

--rm = Remove container when it exists
--link postgresql = Link to another container (for using PostgreSQL database)
-e DATABASE_URI=postgresql://postgres:postgres@postgresql:5432/postgres = Environment variable
-p 8080:8080 = Publish container's port to host
accounts = Name of container image

The application is started again using the Launch Application function from the IBM Cloud IDE.
The output:
<img width="1021" height="845" alt="image" src="https://github.com/user-attachments/assets/21c44362-fa59-468f-8be3-46ca68bd6a62" />
<img width="800" height="146" alt="image" src="https://github.com/user-attachments/assets/4a88ac5d-bbe9-494c-835c-15e94b7d5d93" />
The image is then tagged and pushed to the IBM Cloud Registry with the following command:
docker tag accounts us.icr.io/$SN_ICR_NAMESPACE/accounts:1
docker push us.icr.io/$SN_ICR_NAMESPACE/accounts:1
$SN_ICR_NAMESPACE is an environment variable already predefined by IBM Cloud IDE and refers to my account:
<img width="441" height="32" alt="image" src="https://github.com/user-attachments/assets/e14cbaee-a017-4972-bc28-c9379276051f" />
The push is then checked with the following command:
ibmcloud cr images
The output:
<img width="822" height="198" alt="image" src="https://github.com/user-attachments/assets/19335c82-753c-4de7-b5c1-3dcc7eb17215" />
The image is there and so everything fits.

The user story (Containerize microservice using Docker) is now fully implemented and the next user story (Deploy your Docker image to Kubernetes) can be tackled.
The updated Kanban board:
<img width="1906" height="883" alt="image" src="https://github.com/user-attachments/assets/0d49ec89-086c-4a56-8904-a107ad29380b" />

Deploying to Kubernetes
Manifests / YAML files must be created for the user story Deploy your Docker image to Kubernetes so that the microservice can be deployed consistently.
For the time being, the microservice is deployed manually.
It will be deployed automatically in Task 5 - Building an automated CD DevOps Pipeline.
The manifests can then be reused.

The PostgreSQL database is needed for the application.
OpenShift provides a number of templates for creating services.
IBM has already predefined the template (file postgresql-ephemeral-template.json).

The resources are created and deployed using the template with the following commands:

oc create -f postgresql-ephemeral-template.json
oc new-app postgresql-ephemeral

With the command oc get all we can see that the Postgres service is running:
<img width="801" height="292" alt="image" src="https://github.com/user-attachments/assets/cd5f2a84-20ab-4cfc-a4df-70379ed8fc91" />
The manifests / YAML files can now be created.
IBM provides the tip that you can write the definition of the deployment in a YAML file with the help of the flags --dry-run=client (= ensures that nothing is actually created) and --output=yaml.
IBM also specifies that the image created earlier should be used in the IBM Cloud Registry and three replicas.

I found more information with the --help command:

<img width="854" height="495" alt="image" src="https://github.com/user-attachments/assets/d0ce7336-2c3c-4ba9-9372-5b2ac6fb5d5a" />
The resulting command:
oc create deployment accounts \
    --dry-run=client \
    --output=yaml > deploy/deployment.yaml \
    --image=us.icr.io/sn-labs-christians21/accounts:1 \
    --replicas=3

The output / YAML-file (deploy/deployment.yaml):

<img width="739" height="591" alt="image" src="https://github.com/user-attachments/assets/b21789d5-5c18-487b-a7cc-8ad1df3f0734" />
After applying the deployment to the cluster:
<img width="549" height="133" alt="image" src="https://github.com/user-attachments/assets/93abbe7f-dc1e-4224-b6ae-01d10ed5b8a3" />
To access the postgres database, according to IBM the following environment variables are needed:

DATABASE_HOST
DATABASE_NAME
DATABASE_USER
DATABASE_PASSWORD
A secret for Postgres was also created using the service template.
It contains the names of the variables that are inserted into deployment.yaml as environment variables.
The command oc describe secret postgresql was used to get the information.
The result:
<img width="762" height="821" alt="image" src="https://github.com/user-attachments/assets/6507da44-4c21-4e1a-b366-913851225d7f" />
The file deployment.yaml was then applied to the cluster again with the command oc create -f deploy/deployment.yaml.

A service object was created in order to be able to use the service from outside.
Here, the definition was also written with a command in a YAML file. The command:
<img width="658" height="846" alt="image" src="https://github.com/user-attachments/assets/9161bcd0-0115-4f72-bfae-36e9e8559630" />
After applying the file deploy/service.yaml to the cluster:
<img width="613" height="221" alt="image" src="https://github.com/user-attachments/assets/da06b1f5-69ad-4d6c-b6b0-585817195be7" />
A route object was created to obtain the URL of the service using the following command:
oc create route edge accounts --service=accounts
The result with the command oc get routes (URL is marked red):
<img width="1001" height="304" alt="image" src="https://github.com/user-attachments/assets/a419969e-2b96-4cb0-9b26-b5bdcbfc0747" />
If you enter the URL in your browser, our service will appear:

<img width="1046" height="146" alt="image" src="https://github.com/user-attachments/assets/d6d1eb66-1ea2-407d-944a-0949892c6cce" />
Everything works.
This means that manual deploying with Kubernetes / OpenShift is done and the Kanban board can be updated.
The next user story can be implemented.
<img width="1906" height="891" alt="image" src="https://github.com/user-attachments/assets/3e55ac4c-0296-4a8c-8b3a-c20684619e33" />
Task 5 - Building an automated CD DevOps Pipeline
The detailed view of the last user story:

<img width="1378" height="823" alt="image" src="https://github.com/user-attachments/assets/8a449523-a8f1-4f4e-997b-896f64531349" />
Here is an overview of the related tasks in the pipeline:
<img width="395" height="246" alt="image" src="https://github.com/user-attachments/assets/a6d64e7e-5057-470f-86a8-734a3b363127" />
First, a storage / workspace (PersistentVolumeClaim, PVC) was set up for the pipeline and the pipeline itself with the following commands:
oc create -f tekton/pvc.yaml
oc apply -f tekton/tasks.yaml
oc apply -f tekton/pipeline.yaml
Verification that everything has been created as intended:

<img width="676" height="135" alt="image" src="https://github.com/user-attachments/assets/33db4eab-6fd9-4f0b-910c-9e49e752b274" />
Part of the pipeline has already been implemented. The following tasks:
init
clone
See screenshot of tekton/pipeline.yaml below as well:
<img width="1111" height="708" alt="image" src="https://github.com/user-attachments/assets/ea31af85-741c-45ab-9d1d-851ef925ae61" />
The task has already been defined in the pipeline: git-clone.
This does not have to be written in tekton/tasks.yaml itself, because a predefined task already exists in the Tekton Hub.
This is installed in the cluster with the following command:
tkn hub install task git-clone
Verification of the installation of task git-clone:

<img width="367" height="67" alt="image" src="https://github.com/user-attachments/assets/65ad82c0-44f1-4ab7-9561-56861f2d4d65" />
The pipeline is now started in order to see the output.
The following command is used:

tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/devops-capstone-project.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    -s pipeline \
    --showlog
Use option -h for more information on passing the values for PVC etc..
The value of branch can be exchanged for test purposes (e. g. cd-pipeline instead of main).
The result: the pipeline succeeded.
<img width="1138" height="588" alt="image" src="https://github.com/user-attachments/assets/fab68bb7-c2b1-43e0-8510-d16b881136af" />
The next task is lint with Flake8.
This does not have to be written in tekton/tasks.yaml itself, because a predefined task already exists in the Tekton Hub.
This is installed in the cluster with the following command:

tkn hub install task flake8
Verification of the installation of task flake8:

<img width="374" height="82" alt="image" src="https://github.com/user-attachments/assets/619b7afd-9c3a-4bf4-911f-63e2f3e687d6" />
The task is built into tekton/pipeline.yaml, applied with the command oc apply -f tekton/pipeline.yaml and the pipeline is restarted with the following command:

tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/devops-capstone-project.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    -s pipeline \
    --showlog

The logs:
<img width="1273" height="813" alt="image" src="https://github.com/user-attachments/assets/295deb4c-23d0-4ca9-b5c4-c8f9657f06c8" />
As you can see, the pipeline failed because I didn't do my linting correctly...
After I fixed my linting problem, the pipeline works:
<img width="1009" height="199" alt="image" src="https://github.com/user-attachments/assets/1d17ce1a-3abb-4bc4-a1a2-14e8eb62602e" />
The next task is tests with nose.
This time there is no predefined task in the Tekton Hub.
We have to create it ourselves.
The definition is in tekton/tasks.yaml. The implemented code:
<img width="751" height="707" alt="image" src="https://github.com/user-attachments/assets/63edf8ff-6201-46bf-91a6-b412e62de8aa" />
The task was then added to the pipeline (tekton/pipeline.yaml):
<img width="693" height="587" alt="image" src="https://github.com/user-attachments/assets/57d7d7a5-6759-4ae2-bd3d-d14d9cbb7cf8" />
The two changes were then added to the cluster:

oc apply -f tekton/tasks.yaml
oc apply -f tekton/pipeline.yaml
Then start the pipeline again to see the results of the tests task:

tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/devops-capstone-project.git" \
    -p branch="main" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    -s pipeline \
    --showlog
  <img width="699" height="494" alt="image" src="https://github.com/user-attachments/assets/f1992465-7106-453d-a596-a15b3c0bd52a" />
  Everything fits. Now the next task in the pipeline: build.
This is required to build the image.
There is a task for this in the Tekton Hub: buildah.

It does not need to be installed separately as it has already been installed as a ClusterTask.
ClusterTasks are not only available to a single pipeline, but to several.

With the command tkn clustertask ls you can see all ClusterTasks and the buildah task is listed:

<img width="537" height="219" alt="image" src="https://github.com/user-attachments/assets/3cf200a2-3f88-45b5-8406-069a22d98ccd" />

The build task (with reference to buildah) was then integrated into the pipeline and the changes applied with command oc apply -f tekton/pipeline.yaml:
<img width="505" height="492" alt="image" src="https://github.com/user-attachments/assets/cfcdffb2-e377-4189-b69b-29aaa288bd92" />
<img width="808" height="471" alt="image" src="https://github.com/user-attachments/assets/0a6c98cb-d116-4d61-bb85-497f91756c52" />
Start the pipeline again - this time with an additional parameter (build-image):

tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/devops-capstone-project.git" \
    -p branch="main" \
    -p build-image="image-registry.openshift-image-registry.svc:5000/$SN_ICR_NAMESPACE/accounts:1" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    -s pipeline \
    --showlog

<img width="1108" height="406" alt="image" src="https://github.com/user-attachments/assets/8f5d3e1d-a2fd-4dd2-9c47-5ad118bf51a1" />

Now comes the last task: deploy.
There is a task for this in the Tekton Hub: openshift-client.
It does not need to be installed separately as it has already been installed as a ClusterTask.
Command tkn clustertask ls:
<img width="558" height="421" alt="image" src="https://github.com/user-attachments/assets/9dc41d60-59cc-4612-bb54-767d37c2e58c" />
The deploy task (with reference to openshift-client) was then integrated into the pipeline and the changes applied with command oc apply -f tekton/pipeline.yaml:

<img width="679" height="542" alt="image" src="https://github.com/user-attachments/assets/7c758f2a-02e6-42ee-b8a0-1b9424c8de71" />
<img width="499" height="541" alt="image" src="https://github.com/user-attachments/assets/edbf1748-4406-422c-a388-895eab6dead0" />

Start the pipeline again:

tkn pipeline start cd-pipeline \
    -p repo-url="https://github.com/christian-schw/devops-capstone-project.git" \
    -p branch="main" \
    -p build-image="image-registry.openshift-image-registry.svc:5000/$SN_ICR_NAMESPACE/accounts:1" \
    -w name=pipeline-workspace,claimName=pipelinerun-pvc \
    -s pipeline \
    --showlog
The logs:
<img width="1186" height="373" alt="image" src="https://github.com/user-attachments/assets/0a3a7dfe-8794-49a3-b539-e0aede6256e6" />
The user story is complete, Sprint 3 is finished and the Kanban board has been updated:
<img width="1906" height="894" alt="image" src="https://github.com/user-attachments/assets/49d16873-6292-4094-831f-fca1d9ceb9ea" />

That completes the project.


