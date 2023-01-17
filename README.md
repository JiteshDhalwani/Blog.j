### Distinctiveness and Complexity

I have created a platform, named Blog.j, that allows users to read and write blogs. As someone who likes to read, I've always wanted to create a site where users can create their own blogs and share them with other users of the site. After coming accross Google's [blog site](https://blog.google/), I decided to make one for my final project.

Working on the backend was fairly straightforward, thanks to CS50's problem sets. However, working with images at this scale was a challenge that I wanted to undertake. I came across Pillow (Python Imaging Library) and learned a lot about how Django deals with media files.

I also wanted to make my application more secure, therefore, I started using Django's UserCreationForm as it had tougher password requirements and had more checks.

Earlier versions of the project consisted of blogs with a wall of text, which did not look very good. I realized that one way to allow users to add layout and design to their text was to allow support for markdown. Since I wanted my website to feature blogs from various different topics, I figured that the ability to attach links, images, pieces of code, lists, heading, and other features would be important. Therefore, I added the functionality where users can write content in markdown format and the website would render it.

As someone who reads news based on categories (mostly tech), I wanted to ensure that users could easily choose to read blogs from the categories they wanted, and therefore I added support for categories and seperate pages to list blogs based on particular categories. 

Along with that, author of a blog has flexibility to delete their blog if they wish to do so. 

Even before starting the project, I knew that I wanted to add the funtionality of search in my website. I tried different solutions and finally found one that worked for me, and added a search option which would help users find the blog they are looking for. This feature will become even more important when the number of blogs increase.

The biggest challenge, however, was designing the front-end. As someone who mostly worked with Python before, I knew that I needed to improve my front-end skills. So I went, with my knowledge of basic HTML and CSS, and started creating simple pages, trying and testing new features and ideas.

After having a good grip on CSS, I decided to get into Bootstrap. I found learning by creating small simple projects to be an effective method, so I learned Bootstrap 5 by creating a responsive web page for a 'web development crash course' ![site](https://github.com/JiteshDhalwani/bootstrap5_site). Learning about Bootstrap grid and flexbox took the longest, but it also allowed me to design my blog site to my liking. I also used JavaScript to add features like allowing users to scroll back to the top of the page.

This project took me the longest out of the all the project, partly because of the front-end learning curve that I had to endure. I beleive that I have made a good, minimalist and useful site which users will enjoy using.


### What’s contained in each file you created?

1. `create_blog.html` - Presents users with a form to create blogs and attach an image related to it.
2. `index.html` - This is the home page that displays a list of blogs. Users that are signed in can read. Unsigned users will be required to the login page.
3. `layout.html` - Forms a base layout for some pages. Contains recurring sections like navbar, etc.
4. `login.html` - Presents users with a login form.
5. `register.html` - Presents users with a register form.
6. `search.html` - Displays the results of search query.
7. `show_category.html` - Displays blogs belonging to a particular category.
8. `user.html` - Displays posts created by a particular user.
9. `view_blog.html` - This is the reading page that displays blog content to the user.


### How to run your application?

1. Run `pip install -r /path/to/requirements.txt`
2. Run `python3 manage.py runserver`
3. Visit `http://127.0.0.1:8000/` in your web browser