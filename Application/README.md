
# HPDF Week-1 Assignment

Solution Application containing all the mentioned functionalities in the Assignment questions.

## **Installing / Getting started**
<h4>**prerequisite**</h4>
 - Python 3.4.3<br>
**Python Libraries**
 - Flask
 - Requests
 - wtforms

### **Deploying / Publishing**
```shell
git clone https://github.com/your/awesome-project.git
cd awesome-project/
python app.py
```
Application will start running in the port 5000.

## **Features**

 1. At http://localhost:5000/ displays  "Hello World - Thanveer".
 2. At http://localhost:5000/authors fetches list of authors from https://jsonplaceholder.typicode.com/users and list of posts from https://jsonplaceholder.typicode.com/posts and displays Authors names with no posts by each author.
 3. At  http://localhost:5000/setcookie , Sets a cookie with name=thanveer and age=23.
 4. At http://localhost:5000/getcookies fetches the cookies that has been already set and displays it's values.(If cookies are not present displays "No Cookies Found".
 5. At http://localhost:5000/deny displays a message as "Request Denies".
 6. At  http://localhost:5000/html displays a simple HTML Page.
 7. At http://localhost:5000/input displays a text input with a submit button. On Submission the input will be displayed in the *stdout*.
 


