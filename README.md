# FastAPI

is a modern high performance, web framework for building APIs with python. It uses ASGI(Asychronous Server Gateway Interface)
whereas Flask/Django uses WSGI(Web server Gateway Interface).

### ASGI is intended to provide a standard interface between asyc-capable python web servers, frameworks and applications.

1.  WSGI provided a standard for synchronous pytohn apps, ASGI provides one for both asynchronous and synchronous apps with a WSGI backwards-capability implementation and multiple servers and application frameworks. WSGi is used by Flask and Django

2.  WSGI - sychronous; ASGI - asynchronous

### Pydantic is the most widely used data validation library for Python.

############################################

SGI and ASGI are both interfaces that act as middlemen between web servers and Python web applications. They define how data is exchanged between these two components. Here's a breakdown of their key differences:

## Processing Style:

WSGI (Web Server Gateway Interface): WSGI uses synchronous processing. This means the web server handles requests one at a time. A worker thread gets tied up waiting for slow tasks like database calls to finish before moving on to the next request.

ASGI (Asynchronous Server Gateway Interface): ASGI is built for asynchronous programming. This allows the web server to handle multiple requests concurrently. Even if one request is waiting on a slow task, the server can handle others without being blocked.

## Use Cases:

WSGI: A good choice for simpler applications with moderate traffic that don't require fancy features like WebSockets or real-time communication. WSGI frameworks like Django and Flask are well-established and have a vast ecosystem of libraries.

ASGI: Ideal for complex, high-traffic applications that benefit from handling many requests simultaneously. ASGI shines in applications using WebSockets or real-time features. Frameworks like Starlette and Sanic are built for ASGI.

## Compatibility:

WSGI: WSGI has been around for longer and is widely supported by most web servers and hosting environments.

ASGI: ASGI is a newer specification. You might need to use specific web servers like Daphne or uvicorn for ASGI applications.

In summary, WSGI is the traditional way of running Python web applications, while ASGI offers a more performant approach for modern web development needs. The choice between them depends on the complexity and requirements of your application.

#####################################

## similiar to dataGlass

# Uvicorn,

pronounced “you-vee-corn”, stands for “Unicorn serving ASGI”, and it's an application server used to serve Python web applications that adhere to the ASGI specification. It's lightweight, concurrent, and designed to serve fast web applications in the modern age

## `uvicorn main:app --reload`

is a command used to run a Uvicorn server with automatic reloading.

Let's break it down:

1. uvicorn: This is the command to run the Uvicorn server.
2. main:app: This specifies the application module and instance to run. In this case, it's looking for a file main and an instance named app inside it.
3. --reload: This flag enables automatic reloading of the application when changes are detected in the code. Uvicorn will automatically restart the server when it detects changes, making it ideal for development environments.

When you run this command, Uvicorn will:

1. Start the server with the application instance specified in (link unavailable).
2. Monitor the file system for changes to the application code.
3. Automatically restart the server when changes are detected, applying the updates.

This command is particularly useful during development, as it allows you to see the effects of your code changes without manually restarting the server each time.
Note: Make sure your (link unavailable) file has an ASGI-compatible application instance defined, like app = FastAPI() or app = Starlette(), for Uvicorn to work correctly.

#########################################

# Asynchronous programming enables concurrency,

####################################################

# PyDantic: To make sure data is valid and follows certain rules.

It adds data validation, parsing and serialization options

Pydantic allows us to create classes that inherit from BaseModels.
These classes contain fields that define the structure of piece of data

Pydantic's BaseModel class is a powerful tool for defining data structures in Python. Here's a detailed explanation:

## Pydantic BaseModels:

1. BaseModels are classes that inherit from `pydantic.BaseModel`
2. They provide a way to define the schema (structure) of data objects for validation, serialization, and deserialization.
3. Each field in a BaseModel represents a piece of data within the overall structure.

## Defining Fields:

1. You define fields within a BaseModel class using type annotations (similar to static typing in other languages).
2. These annotations specify the expected data type for each field.

# Type annotations are a that provides a way to specify the expected data type for variables, function arguments, and return values

# `*b` unpacks a list into positional arguments

# `**b` unpacks a dictionary into keyword arguments

# Query parameters :Query is a set of key-value pairs after `?` in a URL, separated by `&` characters.

`?` is query separator and not part of query string. passes query string string directly to program i.e. q=19&color=purple

# GenreURLChoices | None: This specifies the expected type and optionality of the parameter.

1. `GenreURLChoices`: This likely refers to a custom enumeration class defined elsewhere in your code. This class presumably defines the allowed valid values for the genre parameter. By using an enumeration, you ensure that only valid genres are accepted by the endpoint.
2. `| None`: The pipe symbol `|` acts as a union operator, indicating that the parameter can either be of type GenreURLChoices or None.
3. `= None`: This sets the default value of the genre parameter to None. If the client doesn't explicitly provide a genre parameter in the request, it will be treated as None.

# POST request:

when you need to send data from a client(browser) to your API, you send it as a request body.

## A request body is data sent by the client to your API.

## A response body is data your API sends to the client.

## API always have to sent a response bosy but clients don't necessary need to send request bodies all the time.

################################################################

# typing.annotated

special typing form to add context specific metadata to an annotation. Metadata added using `Annotaed` can be used by static analysis tools or at runtime.
If a lib or tool encounters an annnotation Annotated[T,x] and has no special logic for the metadata. It should ignore the metadata and simply traeat annotation as T.

` Annotated[<type>,<metadata>]`
Annotated[int,ValueRange(-10,5)]

# Fastapi uses annotation to add metadata to request parameter

# Annotation cant work alone. FastAPI know how to work QUERY type. FastAPI's query is needed for Annotation to work

# Fastapi uses annotation to add metadata to request parameter

# we can use that using Query from FastAPI and Annotated from typing
