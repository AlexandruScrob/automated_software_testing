blogs = dict()


def menu():
    print_blogs()


def print_blogs():
    # Print available blogs
    for key, blog in blogs.items():
        print(f"{key}: {blog}")
