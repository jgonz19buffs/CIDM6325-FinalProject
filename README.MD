# Final Project
For the final project, we will simply complete the last project, E-Learning Platform, from Antonio and add some additional functionality and requirements for it.
Requirements Steps
The Final Project is fairly straightforward.

## Steps
* Complete the E-Learning Platform project (Book chapters 12 to 16)
* Add a student portfolio of work - described below and additional to step 1 above
* Follow and complete the "Going Live" deployment steps in Book chapter 17. 
* Be prepared for follow-on instructions on how your "Going Live" deployment steps can shared as a container image in Docker
* Modify - the best of your ability - all CSS files from Antonio's styles to the use of Bootstrap

## Student Portfolio of Work
While students are able to enroll in courses in the E-Learning Platform, we capture very little about their enrollment as there is no concept of graded work and what not. <br>
So, what we want is for a student to be able to upload representative work - ONLY in the text, Video, PDF or PNG format - so that, for each class, one or more works can be viewed per course. <br>
For implementation you create forms and views, as is done with Chapter 14 AND facilitate the same actions with additional API functions, as is done with Chapter 15. <br>
This means that, in addition to enrollment, once a student is enrolled, we can share the course contents page with an ADDITIONAL section where the student can upload one or work completed works (again limited to PDFs or PNGs) so that they can be associated with a course they are enrolled in. <br>
We will need some view that combines the original course contents page with an additional section below it that shows the students portfolio works. <br>

## Portofolio Rendering
This should be HIGHLY consistent with the four content types  set up in Chapter 14 - text, image, video, and file.  Your limits will be: 
* Text: any text content is fine and can be captured in a form or as an upload
* Image: must be uploaded as a form and is LIMITED to PNG format only
* Video: can be linked or uploaded and should be in the MP4 format only
* File: this is ONLY for PDF files.

## Portfolio Content Rules
Each entry should be given a title, a date, and a link to the content <br>
The link takes the viewer to a detail page for the content where it can be shown - We have already shown PDFs by opening them in previous chapters. <br>
Chapter 14 takes care of the rest. <br>
If a student is logged in, then the portfolio portion of the page should display content ONLY for the logged in student. <br>
If an instructor or administrator is logged in, then the portfolio portion of the page should display content ONLY for all students <br>

## Extras
The Final Project  Rubric will be updated to reflect the required Django and technology content that must be present in your project. <br>
CIDM6325/FinalProjectRubric.MD at FALL2024 · ahuimanu/CIDM6325 <br>
This has been partially updated as of late October 2024 and will be again updated. <br>
However, if you follow the steps in this document, then treat the rubric as a checklist to ensure that your items are there. <br>
Support for this work from me will be ongoing up to the due date for the work. <br>
Some particular items, like a Bootstrap translation, will require more support for me. <br>
I would leave that for the LAST THING you do and I would complete the work first

## Submitting your work
* Provide me with the URL of the GitHub repository that contains your work, please just make this public.
* Download your Repository as a ZIP file and attach that ZIP file here in this dropbox.



## Guide to Book Topics for Final Project (Baseline, Good, Better, Best)

Topic                                       | Baseline  | Good  | Better  | Best
---                                         | ---       | ---   | ---     | ---
***Chapter 1***                             |           |       |         |
Create Project and Apps                     | x         |       |         |
Creating models                             | x         |       |         |
Django Migrations                           | x         |       |         |
Configuring models for the Django Admin     | x         |       |         |
Queries and Querysets                       | x         |       |         |
Function-Based Views and Templates          | x         |       |         |
WOrking with URLs                           | x         |       |         |
***Chapter 2***                             |           |       |         |
Canonical Urls for SEO                      | x         |       |         |
Pagination                                  | x         |       |         |
Class-Based Views                           |           | x     |         |
Sending email (internal in console)         | x         |       |         |
Sending email (with 3rd party)              |           |       | x       |
One-to-Many Model Relationships             | x         |       |         |
***Chapter 3***                             |           |       |         | 
Django Taggit for Categorization            | x         |       |         |
Aggregate model quiries                     | x         |       |         |
Django Template Language                    | x         |       |         |
Custom template tags                        |           | x     |         |
Custom template filters                     |           | x     |         |
Sitemap                                     |           | x     |         |
Site feeds                                  |           | x     |         |
Postgres                                    |           | x     |         |
Postgres Full-text search                   |           |       |         | x
***Chapter 4***                             |           |       |         |
Django authentication framework             | x         |       |         |
Django Admin                                | x         |       |         |
Django Admin manage users                   | x         |       |         | 
Django Auth User Profile                    | x         |       |         | 
Customize Admin interface                   | x         |       |         | 
Customize ModelAdmin classes                | x         |       |         |
Media file uploads                          | x         |       |         |
Authentication decorators                   | x         |       |         |
***Chapter 5***                             |           |       |         |
Messages framework                          |           |       | x       |
Use front-end framework (bootstrap)         |           | x     |         |
Custom auth backend                         |           |       |         | x
Social Authentication                       |           |       |         | x
https                                       | x         |       |         |
***Chapter 6***                             |           |       |         |
Many-to-Many Model Relationships            | x         |       |         |
Django Forms Classes                        | x         |       |         |
Django ModelForm Class                      | x         |       |         |
Form data validation and retreival          | x         |       |         |
Front-end JavaScript (see note A below)     | x         |       |         | 
***Chapter 7***                             |           |       |         |
Activity Streams                            |           |       | x       |
Advanced QuerySet operations                |           | x     |         |
Django Signals                              |           |       | x       |
Django Debug Toolbar                        | x         |       |         | 
Redis                                       |           |       | x       | 
***Chapter 8***                             |           |       |         |
Pillow Image processing                     |           | x     |         |
Django Sessions                             |           | x     |         |
Custom context processors                   |           | x     |         |
Django and RabbitMQ/Celery/Flower           |           |       |         | x
***Chapter 9***                             |           |       |         |
Stripe Payments                             |           |       | x       |
Webhook Handlers                            |           |       | x       |
CSV export                                  |           | x     |         |
Add custom view to admin interface          |           | x     |         |
PDF Generation                              |           |       |         | x
Send PDFs via Email (external)              |           |       |         | x
***Chapter 10***                            |           |       |         |
Recommender Engine with redis               |           |       |         | x
***Chapter 11***                            |           |       |         | 
Internationalization (I18N)                 |           |       | x       |
Code translation                            |           |       | x       |
Template translation                        |           |       | x       |
Rosetta                                     |           |       | x       |
Model translation with `django-parler`      |           |       | x       |
Localization with `django-localflavor`      |           |       | x       |
***Chapter 12***                            |           |       |         |
Fixtures                                    |           | x     |         |
Model Inheritance                           | x         |       |         |
Authentication and Authorization            | x         |       |         |
Custom Model Fields                         |           | x     |         |
***Chapter 13***                            |           |       |         |
Content Management System                   | x         |       |         |
HTML5 drag and drop                         |           |       | x       |
HTML5 sortable                              |           |       | x       |
Neapolitan for CRUD Views                   |           |       |         | x
Django Formset                              | x         |       |         |
Additial CBV Mixins with `django-braces`    |           | x     |         |
***Chapter 14***                            |           |       |         |
Django caching with `memchached/redis`      |           |       |         | x
***Chapter 15***                            |           |       |         |
Django Rest Framework for APIs              | x         |       |         |
***Chapter 16***                            |           |       |         |
Implement Daphne ASGI                       | x         |       |         |
Django Channels                             | x         |       |         |
Web Sockets                                 | x         |       |         |
Python/Django Async programming             | x         |       |         |
***Chapter 17***                            |           |       |         |
Docker Deployment (optional)                | x         |       |         |