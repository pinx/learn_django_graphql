# Django Graphql learning experiment

This is my first encounter with Django. I wanted to check out the Graphene library.

I worked with graphql before, in the context of the Elixir/Phoenix framework.

The primary source of information was the [graphene tutorial](https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/).

## [Today I learned](https://www.urbandictionary.com/define.php?term=TIL)

- In `urls.py`, you reference the graphql endpoint, and optionally/preferably the graphiql page.

- Define models in the `models.py` file. Django takes care of the rest, with `makemigrations` and `migrate`.

- One-to-many works by magic. Django creates an `orderProducts_set` property on the `Order` model.

- In the graphql `schema.py`, you define resolvers: how to fetch the requested data.

- In 'schema.py', you define models and the queries, and possibly mutations and subscriptions.

- In `admin.py` you register the models that you want to make available to the admin tool.

- In `settings.py` you can define logging, to have generated SQL show up in the debug console.