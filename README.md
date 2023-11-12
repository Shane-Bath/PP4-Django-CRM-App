## CRM Django App - Clientflow
This is a customer management system for a small business.
This Django app is not designed for mobile devices. It is designed for use in an office on standard size screens only.

### Features
-   You can create a client file
-   Log client details, addresses, phone number and email
-   You can edit clients details
-   Create, edit and delete notes for each client
-   View the list of your clients
-   Log phone call
-   Edit and delete calls
-   Create a task 
-   Delete tasks

## Design
This app was first layed out in Balsamiq. It is has Dashboard from which you navigate to the other apps. 

There is User registration and authentication, 
A User registration form is used with fields like username, email, and password. With User login and logout functionality. I have used AllAuth for this functionality. 

Once the user is registered, they can access the dashboard. From there they can create new clients, make nots on each client. Log calls and keep a task list. 

The Dashboard is the central hub. 

## Testing 
I have manually navigated through different pages and functionalities. I have Verified that all elements (buttons, forms, links) are functioning as expected, and the user interface is rendering correctly.

## Manual Testing
### Registration 

| Objective | Test | Expected result | Passed |
| :---:     | :---:|    :---:        | :---:  |
| Check if registration works | Click on register link, complete the form and click on the Signup button. | Redirects to the homepage with dashboard link | Passed |
| Check if login works | Click on login link, complete the form and click login | Redirects to the homepage with dashboard link | Passed |
| Check if Logout works | Click on logout link, click on confirmation | Redirect to homepage with rgister and login links | Passed |

### Dashboard Functionality 

| Objective | Test | Expected result | Passed |
| :---:     | :---:|    :---:        | :---:  |
| Verify that the Log Call feature correctly records a call with details. | Click on "LOG CALL" button, Fill in the call details in the form, Submit the form | The call is recorded in the database, and the call log is updated with the new entry. | Passed |
| Confirm Delete buttton works Display call | Click the delete button | The call is removed from the database | Passed |
| Ensure that the Add Task feature allows users to add tasks to their to-do list | Click on "ADD TASK" button, Enter task details in the form, Submit the form | The task is added to the user’s to-do list and is visible in the Task List. | Passed |
| Confirm Delete buttton works- Task | Click the delete button | The task is removed from the database | Passed |
| Confirm that the New Client feature works and the new client is added to the database | Click on "ADD CLIENT" button. Complete the form. Submit the form |  The new client information is stored in the database and can be retrieved when searched for. | Passed |
| Test the search functionality to locate existing clients. | Use the search bar. Enter the name of an existing client. Click on the "Search" button | The application returns a list of clients that match the search query | Passed |
| Confirm Delete buttton works - clients | Click the delete button | The client is removed from the database | Passed |
### Clients file

| Objective | Test | Expected result | Passed |
| :---:     | :---:|    :---:        | :---:  |
| Verify that the client details can be updates | Click on "UPDATE" button, fill in the NEW details in the form, Submit the form | The update details is recorded in the database. | Passed |
| Add note to clients file | Click on "ADD NOTE" button, fill in the details in the form, Submit the form | The note is added to the client file | Passed |
| Edit note on client file | Click on "VIEW NOTE" button, click on "EDIT NOTE" button, update note with new details, submit the form | The note is has the updated information | Passed |
| Confirm Delete buttton works - client's note | Click the delete button | The note is removed from the database | Passed |

### Other Test
| Objective | Test | Expected result | Passed |
| :---:     | :---:|    :---:        | :---:  |
| Verify that all forms have proper validation and do not accept invalid input. | Try to submit forms with invalid or incomplete data. Check for mandatory fields and input formats. | The form will not submit and provide error feedback | Passed |
|  Ensure that all navigation links and buttons work correctly. | Click on each menu item and button to navigate to different sections. Check that the URL matches the expected destination. | Each navigation element leads to the correct section without errors. | Passed |


## Validator Testing

### Pep8 Valdator
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Pyton code.

### Results

### Dashboard
* [Admin.py](static/images/readme/dashboard_admin.png)
* [Forms.py](static/images/readme/dashboard_forms.png)
* [Models.py](static/images/readme/dashboard_models.png)
* [Urls.py](static/images/readme/dashboard_urls.png)

### pp4_crm_app
* [settings.py](static/images/readme/pp4-settings.png)
* [urls.py](static/images/readme/pp4-urls.png)

## LightHouse 
Lighthouse is a Google Dev tool to check permformace and accessibility. I changed the text font from blue to black to improve my accessiblity score. The blue font failed the contrast test againt the light green backgound. The black passed.

* [Accessibility](static/images/readme/accessibility.png)

The perfomance passed.
* [lighthouse](static/images/readme/acc-improve.png)

## W3C Validation
No errors or warnings. I could not find the trailing slash discussed in the INFO meassage. It does not impact the site.
### HTML
* [Index](static/images/readme/html-index.png)
* [Dashboard](static/images/readme/html-dashboard.png)
* [New client](static/images/readme/html-new-client.png)
* [Client list](static/images/readme/html-client-list.png)
* [Dashboard](static/images/readme/html-dashboard.png)
* [Display call](static/images/readme/html-display-call.png)
* [Task](static/images/readme/html-task.png)
* [Task-list](static/images/readme/html-task-list.png)

### CSS
No errors found
* [Dashboard](static/images/readme/dashboard-css.png)
* [task](static/images/readme/task-css.png)
* [Call log](static/images/readme/call-log-css.png)

## Credit

Thank you to Diasy Mcgirr for her guidance.
<details>
<summary>The following is list of resources I referred to.</summary>

model fields
<https://docs.djangoproject.com/en/4.2/ref/models/fields/#textfield>

unique id- how to create a unique id for each client
<https://stackoverflow.com/questions/16925129/generate-unique-id-in-django-from-a-model-field>

autocomplete
<https://django-autocomplete-light.readthedocs.io/en/master/index.html>
Sharing data bewteen models tables
<https://stackoverflow.com/questions/58611631/django-how-i-can-populate-data-in-a-model-from-another-table-model-in-the-same>

testing
<https://docs.djangoproject.com/en/4.2/topics/testing/overview/>
<https://docs.djangoproject.com/en/4.2/intro/tutorial05/>
<https://realpython.com/testing-in-django-part-1-best-practices-and-examples/>

Function versus genric class views
code instititude
<https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/>
<https://stackoverflow.com/questions/66411588/django-transforming-function-based-view-into-class-based-view>

Displaying data
<https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-display/>

Djang CRM examples
<https://github.com/MicroPyramid/Django-CRM/blob/master/leads/models.py>

<https://stackoverflow.com/questions/72671197/how-to-make-a-select-field-using-django-model-forms-using-set-values>

get_object 404
<https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/>

phone number
<https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-a-phone-number-in-django-models>

AttributeError: 'function' object has no attribute 'as_view'
<https://stackoverflow.com/questions/34217400/function-object-has-no-attribute-as-view>

search table / data
<https://stackoverflow.com/questions/66386490/making-search-bar-in-django>
<https://django-filter.readthedocs.io/en/stable/>

making queries
<https://docs.djangoproject.com/en/4.2/topics/db/queries/>

listing data alphabetically
<https://stackoverflow.com/questions/16778819/django-how-to-sort-objects-alphabetically-by-first-letter-of-name-field>

client urls
<https://docs.djangoproject.com/en/4.1/ref/urlresolvers/>
<https://docs.djangoproject.com/en/3.2/topics/http/urls/#how-django-processes-a-request>


migration and edit fields
<https://stackoverflow.com/questions/70970039/django-rename-field-and-create-new-one-with-the-same-name-returns-psycopg2-error>
<https://www.w3schools.com/django/django_update_data.php>
<https://docs.djangoproject.com/en/4.2/ref/migration-operations/>

Check if user is authenticated
<https://docs.djangoproject.com/en/4.2/topics/auth/default/>
<https://docs.djangoproject.com/en/4.2/ref/utils/>
<https://stackoverflow.com/questions/29673549/method-decorator-with-login-required-and-permission-required>
<https://docs.djangoproject.com/en/4.2/topics/class-based-views/intro/>

context -- fix error code line to long.
<https://docs.djangoproject.com/en/dev/ref/templates/api/#module-django.template>

redirect after submit button is pressed
<https://stackoverflow.com/questions/60952187/how-to-redirect-to-another-page-that-contains-id-in-django>
<https://docs.djangoproject.com/en/4.2/topics/http/shortcuts/>

edit model
<https://www.youtube.com/watch?v=jCM-m_3Ysqk>
<https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/>

<https://docs.djangoproject.com/en/4.2/topics/http/views/#:~:text=A%20view%20function%2C%20or%20view>,.%20.%20or%20anything%2C%20really.

debugging
<https://www.mattlayman.com/understand-django/debugging-tips-techniques/>

listing on date order
<https://stackoverflow.com/questions/9834038/django-order-by-query-set-ascending-and-descending>

edit task mark complete
<https://stackoverflow.com/questions/68113852/how-to-check-whether-the-checkbox-is-checked-in-django>

update view
<https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/>

delete view
<https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/>

add to user
<https://stackoverflow.com/questions/63255598/django-how-to-link-to-specific-user>
noreverse
<https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/>

<https://stackoverflow.com/questions/38390177/what-is-a-noreversematch-error-and-how-do-i-fix-it>

calander
<https://stackoverflow.com/questions/75945489/django-python-calendar-module>
<https://jqueryui.com/datepicker/>
<https://stackoverflow.com/questions/18106454/how-to-use-a-jquery-datepicker-with-the-django-template-language>

Template
<https://docs.djangoproject.com/en/4.2/ref/templates/language/>

SVG

<https://www.svgbackgrounds.com/>

Modal
<https://stackoverflow.com/questions/23648761/how-to-build-django-ajax-modal-popup-forms-with-server-side-forms>
<https://jquerymodal.com/>
<https://django-bstrap-modals.readthedocs.io/en/latest/index.html>

Styling forms
<https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa>

Cripsy forms
<https://github.com/django-crispy-forms/crispy-bootstrap5>
<https://ordinarycoders.com/blog/article/render-a-django-form-with-bootstrap>
<https://stackoverflow.com/questions/13098954/use-crispy-form-with-modelform>
<https://django-crispy-forms.readthedocs.io/en/latest/index.html>
<https://stackoverflow.com/questions/12144475/displaying-multiple-rows-and-columns-in-django-crispy-forms>

Soft delete
<https://dev.to/bikramjeetsingh/soft-deletes-in-django-a9j>

Success message
<https://stackoverflow.com/questions/28723266/django-display-message-after-post-form-submit>

Changing note fnction to class view
<https://docs.djangoproject.com/en/4.2/topics/class-based-views/generic-editing/>

Pagination
Code institue
<https://realpython.com/django-pagination/>
<https://docs.djangoproject.com/en/4.2/topics/pagination/>
<https://realpython.com/django-pagination/#combined-example>

color
<https://colorhunt.co/palette/f6ffdee3f2c1c9dbb2aac8a7>
F6FFDE
E3F2C1
C9DBB2
AAC8A7

Calander
<https://docs.python.org/3/library/calendar.html>

Updateview / edit
<https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#django.views.generic.edit.UpdateView>

success message
<https://getbootstrap.com/docs/5.0/components/toasts/>
<https://dev.to/serhatteker/show-message-in-class-based-views-django-4a4d>
<https://docs.djangoproject.com/en/4.2/ref/contrib/messages/>
<https://docs.djangoproject.com/en/4.2/ref/contrib/messages/#adding-messages-in-class-based-views>
<https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown>


</details>