from blog import Blog


MENU_PROMPT = "Enter 'c' to create a blog, 'l' to list blogs, " \
              "'r' to read one, 'p' to create a post or 'q' " \
              "to quit."

POST_TEMPLATE = """\nTitle: {}\nContent: {}\n"""


blogs = dict()


def menu():
    selection = input(MENU_PROMPT)

    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()

        selection = input(MENU_PROMPT)


def print_blogs():
    # Print available blogs
    for key, blog in blogs.items():
        print(f"{key}: {blog}")


def ask_create_blog():
    title = input('Blog title: ')
    author = input('Author name: ')

    blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input("Blog title to read:")

    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_post():
    blog_name = input("Blog title for the post:")
    title = input("Post title: ")
    content = input("Post content: ")

    blogs[blog_name].create_post(title, content)
