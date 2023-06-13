# **Residence and Work Permit Management System**

This is an easy-to-use web application developed for managing the application, processing and issuing of residence and work permits.

---

## **Introduction**

Residence and Work Permit Management System is accessible through a web browser such as:

* Google Chrome
* Safari 
* Mozilla Firefox
* Internet Explorer etc.

Applicants who visit the site can apply for residence and work permits. To use the system, applicants must first ***sign up*** to create an account that will be used to track the status and progress of their applications.

The system is developed to send email and SMS notifications to appropriate individuals at every stage of the application process. This helps to ensure timely and efficient applications for residence and work permits. 

---

## **Installation**

Residence and Work Permit Management System is built on the [Frappe Framework](https://frappeframework.com/ "Frappe Site"), a full-stack, open source, web development framework written in Python & JavaScript. The framework is ***generic*** and can be used to build database driven apps. ***MariaDB*** is the default database for the framework.

To install the Residence and Work Permit Management System, you will have to install [Frappe-Bench](https://frappeframework.com/docs/v13/user/en/installation "Frappe Bench Installation"), a command-line package and site manager for the Frappe Framework.

>For more details, read the Bench ***README***.

After installing Frappe Bench, you will have to initialise a bench directory with the Frappe Framework using the following command:

```bench
bench init work_residence_permits
```

Next, change the directory to ***work_residence_permits*** and download the Residence and Work Permit Management app with the following commands:

```bench
cd work_residence_permits

bench get-app work_residence_permit_management https://github.com/IoT-Communications/Work-Residence-Permit-Hackathon.git
```

Create a new site to install the app by running the command:

```bench
bench new-site work-resindence.example.com
```

This will create a new folder in your ***/sites*** directory and create a new database for this site.

Next, install the Residence and Work Permit Management app in this site by running the command:

```bench
bench --site work-resindence.example.com install-app work_residence_permit_management
```

To run the app locally, you must start the bench service with the command:

```bench
bench start
```

At this point, the Residence and Work Permit Management app is installed and listening on port 8000. 

You can now fire up your browser by clicking [this link](http://localhost:8000/ "Login Screen") and you should see the login screen. 

Login as Administrator and use the password you set at the time of creating the site ***(work-resindence.example.com)***.

---

## **License**

MIT