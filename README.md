# Django Webapp Deployment

A simple Django application configured for Docker, Docker Compose, GitHub Actions CI, Docker Hub publishing, and EC2 deployment.

## Tech Stack

- Python 3.12
- Django 6.0
- Gunicorn
- Docker
- Docker Compose
- GitHub Actions
- Docker Hub
- AWS EC2

## Project Structure

```text
.
├── .github/workflows/ci-cd.yml
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── tests.py
│   └── views.py
├── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
├── manage.py
├── requirements.txt
└── README.md
```

## Run Locally

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

## Run Tests

```bash
python manage.py check
python manage.py test
```

## Run With Docker

Build the image:

```bash
docker build -t django-cicd-app .
```

Run the container:

```bash
docker run --rm -p 8000:8000 django-cicd-app
```

Open:

```text
http://localhost:8000
```

## Run With Docker Compose

For local development:

```bash
docker compose up --build
```

Stop containers:

```bash
docker compose down
```

## Production Compose

The production compose file uses a Docker image from Docker Hub and stores SQLite data in a named Docker volume.

Required environment variables:

```text
DOCKER_IMAGE
DJANGO_SECRET_KEY
DJANGO_ALLOWED_HOSTS
```

Example:

```bash
DOCKER_IMAGE=username/django-cicd:latest \
DJANGO_SECRET_KEY=change-this-secret \
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1 \
docker compose -f docker-compose.prod.yml up -d
```

## CI/CD Pipeline

The GitHub Actions workflow is located at:

```text
.github/workflows/ci-cd.yml
```

The pipeline runs on pushes and pull requests to:

```text
main
master
```

### CI Jobs

The CI pipeline:

1. Checks out the code
2. Sets up Python 3.12
3. Installs dependencies
4. Runs Django checks
5. Runs Django tests
6. Validates Docker Compose
7. Builds the Docker image

### CD Jobs

On push to `main` or `master`, the CD pipeline:

1. Builds the Docker image
2. Pushes the image to Docker Hub
3. Connects to EC2 by SSH
4. Pulls the latest Docker image
5. Starts the app with `docker-compose.prod.yml`
6. Runs Django migrations

## GitHub Secrets

Add these secrets in:

```text
GitHub Repository -> Settings -> Secrets and variables -> Actions
```

Required secrets:

```text
DOCKERHUB_USERNAME
DOCKERHUB_TOKEN
EC2_HOST
EC2_USER
EC2_SSH_KEY
DJANGO_SECRET_KEY
DJANGO_ALLOWED_HOSTS
```

Optional secret:

```text
EC2_APP_DIR
```

Example values:

```text
DOCKERHUB_USERNAME=your-dockerhub-username
EC2_HOST=your-ec2-public-ip
EC2_USER=ubuntu
DJANGO_ALLOWED_HOSTS=your-ec2-public-ip,localhost,127.0.0.1
EC2_APP_DIR=/home/ubuntu/django-cicd
```

For Amazon Linux, `EC2_USER` is often:

```text
ec2-user
```

For Ubuntu EC2 images, `EC2_USER` is often:

```text
ubuntu
```

## EC2 Server Requirements

Install these on the EC2 instance:

```text
git
docker
docker compose
```

Make sure the EC2 security group allows inbound traffic on:

```text
22    SSH
8000  Django app
```

After deployment, open:

```text
http://YOUR_EC2_PUBLIC_IP:8000
```

## Useful EC2 Commands

Check running containers:

```bash
docker ps
```

View app logs:

```bash
docker logs django-cicd-web
```

Restart the app:

```bash
docker compose --env-file .env.production -f docker-compose.prod.yml restart
```

Stop the app:

```bash
docker compose --env-file .env.production -f docker-compose.prod.yml down
```

## Troubleshooting

If GitHub Actions tests fail, run locally:

```bash
python manage.py check
python manage.py test
```

If Docker build fails, run:

```bash
docker build -t django-cicd-app .
```

If deployment skips, check that all required GitHub secrets are set.

If the EC2 app is not reachable, check:

- EC2 security group allows port `8000`
- Docker container is running
- `DJANGO_ALLOWED_HOSTS` includes the EC2 public IP
- The app logs with `docker logs django-cicd-web`
