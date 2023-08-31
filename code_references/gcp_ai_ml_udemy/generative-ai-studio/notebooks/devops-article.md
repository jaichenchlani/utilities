title: Devops Tutorial | DevOps with Docker, Kubernetes and Azure DevOps

What is DevOps? How is it different from Agile? What are the popular DevOps Tools? What is the role of Docker, Kubernetes and Azure DevOps in DevOps?

Let's get started with a simple use case.

## You will learn
- What is DevOps?
- Why do we need DevOps?
- How is DevOps different from Agile?
- What are the important DevOps tools?
- How does Docker help DevOps?
- How does Kubernetes help DevOps?
- How does Azure DevOps help DevOps?
- What is Continuous Integration, Continuous Delivery?
- What is Infrastructure as Code?
- How do Terraform and Ansible help DevOps?


## What is DevOps?

As with most buzzwords around software development, there is no accepted definition for DevOps.

Definitions vary from simple ones, like these two, to complex definitions that last a complete page of a book. 

>**DevOps** is the combination of **cultural philosophies, practices, and tools** 
that **increases** an organization’s ability to **deliver applications and services** at **high velocity** - Amazon Web Services(AWS)

> **DevOps** is a **collaborative and multidisciplinary** effort within an organization to **automate continuous delivery** of new software versions, while **guaranteeing** their **correctness and reliability** - A Survey of DevOps Concepts and Challenges - L Leite 


**Instead of trying define DevOps**, let's understand how Software Development evolved to DevOps.

### Waterfall Model

First few decades of software development was centered around the water fall model. 

Waterfall model approached software development the same way that you would approach building a real estate project - for example, building an amazing bridge. 

You will build software in multiple phases that can go on for a period any where between a few weeks to a few months. 

[![Image](https://www.springboottutorial.com/images/devops-01-waterfall.png "Waterfall Model")](https://links.in28minutes.com/DevOps-SBT)

In most waterfall projects, it would be months before the business sees a working version of an application. 

### Key Elements to Build Great Software

While working in the waterfall model for a few decades, we understood a few key elements around developing great software:
- Communication
- Feedback
- Automation

#### Importance of Communication

Software Development is a multi disciplinary effort involving a variety of skills. 


Communication between people is essential for the success of a software project. 

In the waterfall model, we tried to enhance communication by trying to prepare 1000 page documents on Requirements, Design, Architecture and Deployment. 

But, over a period of time, we understood that 
- The best way to enhance communication within the team, is to get the team together. Get a variety of skills in the same team. 
- Cross functional teams - with wide range of skills - work great.

#### Importance of Early Feedback

Getting Feedback Quickly is important. Building great software is all about getting quick feedback.

> Are we building an application which meets the business expections? 

You cannot wait for months to get feedback. You would want to know quickly. 

> Will your application have problems if it is deployed to production? 

You don't want to know it after a few months. You want to find it out as early as possible.

The earlier we find a problem, the easier it is to fix it.

We found that the best software teams are structured to enable quick feedback. Anything I'm working on, I would like to know if I'm doing the right thing as early as possible . 


#### Importance of Automation

Automation is critical. Software Development involves a wide range of activities. Doing things manually is slow and error prone. We understood that it's essential to always look for opportunities to introduce Automation.



Having understood the key elements to develop great software, lets look at how we evolved to Agile and DevOps.

### Evolution to Agile


Agile was the first step in evolution towards implementing our learnings with enhanced communication between teams, getting feedback and bringing in automation.


Agile brought the business and development teams together into one team which works to build great software in small iterations called sprints. 



Instead of spending weeks or months on each phase of development, agile focuses on taking small requirements called user stories through the development cycle within a few days, sometimes within the same day.


#### How did Agile enhance communication between teams? 

Agile brought the business and development teams together. 
- Business is responsible for defining what to build? What are the requirements? 
- Development is responsible for building a product that meets the requirements. Development includes everybody involved in Design, Coding, Testing and Packaging of your software. 

In Agile, a representative from Business, called a Product Owner, is always present with the team, the team understands the business objectives clearly. 

When the development team does not understand the requirements well and is going in a wrong path, Product Owner helps them do course correction and stay on the correct path. 

> Result : The final product the team builds is something that the business wants.

Another important factor is that Agile Teams have cross functional skills - coding skills - front end, api and databases, testing skills and business skills. This enhances communication between people that have to work together to build great software.



#### Agile and Automation

What are the Automation areas where Agile Teams focused on? 

Software Products can have a variety of defects. 
- Functional Defects mean the product does not work as expected. 
- Technical Defects make the maintainence of the software difficult. For example, code quality problems. 

In general, agile teams were focused on using automation to find technical and functional defects as early as possible.

Agile teams focused on automation tests. Writing great unit tests to test your methods and classes. Writing great integration tests to test your modules and applications. Agile teams also focused extensively on code quality. Tools like SONAR were used to assess the code quality of applications. 


Is it sufficient if you have great automation tests and great code quality checks? You would want to run them as often as possible. Agile Teams focused on Continuous Integration. You make a commit to version control. Your Unit Tests, Automation Tests and Code Quality Checks were automatically executed in a Continuous Integration Pipeline. Most popular CI/CD tool during the early agile time period was Jenkins.

#### How did Agile promote immediate feedback? 

Most important factor is that Business does not need to wait for months to see the final product.  At the end of every sprint, the product is demoed to all stakeholders including Architecture and Business Teams. All feedback is taken in while prioritizing user stories for the next sprint. Result : The final product the team builds is something that the business wants. 

Another important factor that enables immediate feedback is continuous integration. Let's say I commit some code into version control. Within 30 minutes, I get feedback if my code causes a unit test failure or a integration test failure. I will get feedback if my code does not meet code quality standards or does not have enough code coverage in the unit tests.

Was agile successful? Yes. For sure. By focusing on improving the communication between business and development teams, and focusing on finding a variety of defects early, Agile took software development to the next level. 

I, personally, had a wonderful experience working with some amazing teams in the Agile model. Software Engineering, which for me represents all the efforts in building software from requirements to taking applications live, for the first time, was as enjoyable as programming.

But, does evolution stop? Nope.

New challenges emerged.

### Evolution of Microservices Architectures

We started moving towards a microservices architecture and we started building a number of small api's instead of building large monolith applications. 

What was the new challenge? 

Operations becomes more important. Instead of doing 1 monolith release a month, you are doing hundreds of small microservice releases every week. Debugging problems across microservices and getting visibility into what's happening with the microservices became important. 


It was time for a new buzzword in software development. DevOps.


### Emergence of DevOps

What was the focus of DevOps? 

Focus of DevOps was on enhancing the communication between the Development and the Operations Team. 
- How do we make deployments easier? 
- How do we make the work operations team does more visible to the development team?


#### How did DevOps enhance communication between teams? 

DevOps brought Operations Teams closer to the Development Teams. 
- In more mature enterprises, Development and Operations Teams worked as one Team. They started sharing common goals and both teams started to understand the challenges the other team faces. 
- In enterprises in the early stages of devops evolution, a representative from the operations team can be involved in the sprints - standups and retrospectives.



#### What are the Automation areas where DevOps Teams focused on? 

In addition to the focus areas of agile - Continuous Integration and Test Automation, the DevOps teams were focused on helping automate several of the Operation Teams Activities - Provisioning Servers, Configuring Software on Servers, Deploying Applications and Monitoring Production Environments. A few key terminology are Continuous Deployment, Continuous Delivery and Infrastructure as Code. 

Continuous Deployment is all about continuously deploying new version of software on Test Environments. In even more mature organizations like Google, Facebook, Continuous Delivery helps in continuously deploying software to production - maybe hundreds of production deployments per day. 


Infrastructure as Code is all about treating your Infrastructure like you treat your application code. You create your infrastructure - servers, load balancers and database - in an automated way using configuration. You would version control your infrastructure - so that you can track your infrastructure changes over a period of time. 



#### How did DevOps promote immediate feedback? 

DevOps brings Operations and Development Teams Together. Because Operations and Development are part of the same team, the entire team understands the challenges associated with Operations and Development. 
- Any operational problems get quick attention of the developers. 
- Any challenges in taking software live get early attention of operations team.

DevOps encouraged Continuous Integration, Continuous Delivery and Infrastructure as Code.
- Because of Continous Delivery, If I make a code change or a configuration change that might break a test or a staging environment, I would know it within a few hours.
- Because of Infrastructure As Code, Developers can self provision environments, deploy code and find problems on their own, without any help from operations team. 

While we talk as if agile and devops are two different things to make things simple, in reality, there is no accepted definition for what devops means. 

I see agile and devops as two phases that helped us improve how build great software. They don't compete against each other but together they help us build amazing software products.

As far as iam concerned the objective of Agile and DevOps together is to do things that 
- Promote Communication and Feedback between Business, Development and Operations Teams
- Ease the painpoints with Automation. We will discuss about Unit Tests, Integration Tests, Code Quality Checks, Continuous Integration, Continuous Delivery, Infrastructure as Code and Standardization through Containerization during this amazing journey in this course.

## A DevOps Story

Here's an amazing story:

You are the star developer in a team and you would need to make a quick fix. You go to a github repository! 

You quickly checkout the project. 

You quickly create your local environment. 

You make a change. You test it. You update the unit and automation tests.

You commit it.


You get an email saying it is deployed to QA. 

A few integration tests are automatically run.

Your QA team gets an email asking for approval. They do a manual test and approve.

Your code is live in production in a few minutes.

You might think this is an ideal scenario. But, do you know that this is what is happening in innovative enterprises like Netflix, Amazon and Google day in and day out!

This is the story of DevOps. 


### DevOps = Development + Operations

DevOps is a Natural Evolution of Software Development. DevOps is NOT JUST a tool, a framework or just automation. It is a combination of all these. 

DevOps focuses on People, Process and Products. People aspects of DevOps are all about Culture and Create a Great Mindset. A culture which promotes open communication and values quick feedback. A culture that value high quality software. 

Agile helped in bridging the gap between the business and development teams. Development Teams understood the priorities of the business and worked with the business to deliver the stories providing most value first. However, the Dev and Ops teams were not aligned.

They had different goals.

> The goal of Dev team is to take as many new features to production as possible.

> The goal of Ops team was to keep the production environment as stable as possible.

As you can see, if taking things to production is difficult, dev and ops are unaligned.

> DevOps aims to align the Dev and Ops teams with shared goals. 

Dev team works with the Ops team to understand and solve operational challenges. Ops team is part of the scrum team and understands the features under development.

> How can we make this possible?

> Break down the wall between Dev and Ops! 

#### Getting Dev and Ops Together - Option 1

In matured Dev Ops enterprises, Dev and Ops work as part of the same scrum team and share each other responsibilities. 

#### Getting Dev and Ops Together - Option 2

However, if you are in the early stages of devops evolution, how can you get Dev and Ops have common objectives and work together?

Here are some of the things you can do:
- One of the things you can start with is to have the development team share some of the responsibilities of the operation team. For example, the dev team can take the responsibility of new release for the first week after production deployment. This helps the development team understand the challenges faced by operations in taking new releases live and help them come together and find better solutions.
- Other thing you can do is to involve a representative of the operations team in the Scrum activities. Involve them in Stand ups and Retrospectives of the team.
- The next thing you can do is to make the challenges faced by Operations team more visible to the Development team. When you face any challenges in operations, make development teams part of the teams working on solutions.

Which way you take, find ways of breaking the wall and get the Development and Operations team together.

Another interesting option emerges because of automation. By using Infrastructure as Code and enabling Self Provisioning for Developers, You can create common language that operations and development teams understand - code. More about this in the next couple of steps.

### A DevOps Use Case

Consider the picture below:


This picture show cases two simple workflows
- No 1 : Infrastructure as Code using Terraform and Azure DevOps to provision Kubernetes Clusters
- No 2 : Continuous Deployment of Microservices using Azure DevOps to build and deploy Docker images for microservices into Kubernetes Clusters

Does this sound complex?

Let's break it down and try and understand them.

Let's start with No 2 - Continuous Deployment first.

#### No 2 : DevOps Continuous Deployment with Azure DevOps and Jenkins

What is the use of having great tests and code quality checks if you don't run them often?

What is the use of deployment automation if you don't deploy software often enough?

As soon as a developer commits code into the version control system, the following steps are executed:
- Unit Tests 
- Code Quality Checks 
- Integration Tests 
- Application Packaging - Building a deployable version of application. Tools - Maven, Gradle, Docker
- Application Deployment - Putting new applications or new versions of application live.
- An email to the testing team to test the application.

As soon as there is an approval from the test team, the app is immediately deployed to the  Next Environment.

This is called Continuous Deployment. If you continuously deploy upto production, it is called Continuous Delivery.

The most popular CI CD Tools are Azure DevOps and Jenkins

#### No 1 : DevOps Infrastructure as Code with Terraform

In older days, we used to create environments and deploy applications manually.


Everytime you create a server, this needs to be done manually. 
- What if Java version needs to be updated? 
- A security patch needs to be applied?

You do it manually.

What is the result of this?
- High Chance of Errors.
- Replication environments is difficult.


#### Infrastructure as Code

Infrastructure as Code - Treat Infrastructure the same way as application code

Here are some of the important things to understand with Infrastructure as Code
- Infra team focuses on value added work (instead of routine work)
- Less Errors and Quick Recovery from Failures
- Servers are Consistent (Avoids Configuration Drift)


The most popular IaC tools are Ansible and Terraform.

Typically these are the steps in IaC
- Provision Servers(Enabled by Cloud) from a Template
- Install Software 
- Configure Software

##### Server Provisioning

Typically Provisioning Tools are used to provision servers and get new server ready with networking capabilities. The most popular provisioning tools are CloudFormation and Terraform. 

Using Terraform, you can provision servers and rest of your infrastructure, like load balancers, databases, networking configuration, etc. You can create servers using pre created images created using tools like Packer and AMI (Amazon Machine Image).

##### Configuration Management

Configuration Management tools are used to 
- Install Software 
- Configure Software

Popular Configuration management tools are Chef, Puppet, Ansible, and SaltStack. These are designed to install and manage software on existing servers.

### Role of Docker and Kubernetes in DevOps

What is the role of Docker and Kubernetes in DevOps?


In the microservices world, a few microservices might be built with Java, a few with Python and a few with JavaScript.

Different microservices will have different ways of building applications and deploying them to servers.

This makes operations team's job difficult.

How can we have similar way of deploying multiple types of applications? Enter Containers and Docker.

Using Docker you can build images of microservices - irrespective of their language - Java, Python or JavaScript. You can run these images the same way on any infrastructure.

This simplifies operations.

Kubernetes adds on to this by helping to orchestrate different types of containers and deploying them to clusters.


Kubernetes also provides
- Service Discovery
- Load Balancing
- Centralized Configuration

Docker and Kubernetes make DevOps easy.



### Important DevOps Metrics

Following are some of the important DevOps metrics you can track and improve over a period of time.
- Deployment Frequency - How often are applications deployed to production?
- Time To Market - How long do you need to take a feature from coding to production?
- Failure Rate of New Releases - How many of your releases fail?
- Lead Time to Fixes - How long do you need to make a production fix and release it to production?
- Mean Time to Recovery  - How long do you take to recover your production environment from a major issue?

### DevOps Best Practices

Following are some of the best practices with DevOps
- Standardization 
- Teams with Cross Function Skills 
- Focus on Culture 
- Automate, Automate and ..  
- Immutable Infrastructure 
- Dev Prod Parity 
- Version Control Everything 
- Self Provisioning 

### DevOps Maturity Signals

How do you measure the maturity of your DevOps Implementations. Here are some of the important questions to ask.

#### Development
- Does every commit trigger automated tests and automated code quality checks?
- Is your code continuously delivered to production?
- Do you use pair programming?
- Do you use TDD and BDD? 
- Do you have a lot of re-usable modules?
- Can development teams self provision environments?
- How long does it take to deliver a quick fix to production?

#### Test
- Are your tests full automated with high quality production like test data?
- Does your builds fail when your automated tests fail?
- Are your testing cycles small?
- Do you have automated NFR tests?

#### Deployment
- Do you have Dev Prod Parity?
- Do you use A/B Testing?
- Do you use canary deployments?
- Can you deploy at the click of a button?
- Can you rollback at the click of a button?
- Can you provision and release infrastructure at the click of a button?
- Do you use IAC and version control your infrastructure?

#### Monitoring
- Does the team use a centralized monitoring system?
- Can development team get access to logs at the click of a button?
- Does the team get an automated alert if something goes wrong in production?

#### Teams and Processes
- Is the team looking to continuously improve?
- Does the team have all the skills it needs from Business, Development and Operations?
- Does the team track the key devops metrics and improve on them?
- Do you have the culture of take Local Discoveries and using them to make Global Improvements?

### DevOps Transformation Best Practices
- Leadership Buy-in is Critical 
- Involves Upfront Costs
- Setup COEs to help teams
- Choose the right application and team
- Start Small 
- Sharing Learnings (Newsletters, Communication, COEs) 
- Encourage People with Exploration and Automation Mindset 
- Recognize DevOps Teams
