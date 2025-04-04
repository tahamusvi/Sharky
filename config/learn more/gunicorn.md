
# Gunicorn Configuration for Django

This document provides a guide to configure Gunicorn for your Django application.

## Prerequisites

- Ensure you have Python and pip installed.
- Install Gunicorn in your Django project:

```bash
pip install gunicorn
```

## Basic Usage

To run your Django application with Gunicorn, use the following command:

```bash
gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000
```

- Replace `your_project_name` with the name of your Django project.
- smaple: `config`

## Configuring Workers

### Choosing Worker Type

You can specify the worker type using the `--worker-class` option. Common options include:

- `sync`: Default synchronous worker.
- `gevent`: Asynchronous worker for handling multiple requests.

Example:

```bash
gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000 --worker-class gevent
```

### Setting the Number of Workers

It's recommended to set the number of workers based on your CPU cores. A typical formula is:

```
(2 * number_of_cores) + 1
```

To set the number of workers, use the `--workers` option:

```bash
gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000 --workers 3
```

## Logging

To configure access and error logging, use the following options:

```bash
gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000 --access-logfile access.log --error-logfile error.log
```

## Example Command

Here’s a complete example command that includes worker configuration and logging:

```bash
gunicorn your_project_name.wsgi:application --bind 0.0.0.0:8000 --workers 3 --worker-class gevent --access-logfile access.log --error-logfile error.log
```

## Conclusion

With this configuration, you can efficiently run your Django application using Gunicorn, ensuring better performance and scalability.
