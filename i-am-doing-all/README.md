# Wife's To-Do List for Me

This project is a Flask-based web application that allows my wife to create and manage a to-do list for me. It uses MongoDB for data storage, Nginx as a reverse proxy, and Docker for containerization.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Features

- Create, read, update, and delete tasks (CRUD operations)
- Modern, responsive frontend using Bootstrap
- RESTful API for task management
- Docker containerization for easy deployment
- Nginx reverse proxy for improved performance and security
- MongoDB for persistent data storage

## Prerequisites

- Docker
- Docker Compose
- Git

## Project Structure
project_root/
├── app/
│   └── app.py
├── static/
│   ├── styles.css
│   └── script.js
├── templates/
│   └── index.html
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── requirements.txt
├── .env
└── README.md


## Setup and Installation

1. Clone the repository:
`git clone https://gitlab.com/your-username/wifes-todo-list.git
cd wifes-todo-list`

2. Create a `.env` file in the project root and add the following environment variables:

``MONGO_URI=mongodb://${MONGO_ROOT_USERNAME}:${MONGO_ROOT_PASSWORD}@mongodb:27017/${DB_NAME}?authSource=admin
DB_NAME=wife_todo_list
MONGO_ROOT_USERNAME=admin
MONGO_ROOT_PASSWORD=your_secure_password_here``

Replace `your_secure_password_here` with a strong password.

3. Build and start the Docker containers:
`docker-compose up --build -d`

## Running the Application

After setup, the application will be available at `http://localhost`. You can interact with it through your web browser.

To stop the application:
`docker-compose down`

## API Endpoints

- `GET /mission`: Retrieve all mission IDs
- `GET /mission/{id}`: Retrieve a specific mission
- `POST /mission`: Create a new mission
- `PUT /mission/{id}`: Update an existing mission
- `DELETE /mission/{id}`: Delete a mission
- `GET /metrics`: (Placeholder for future metrics implementation)

## Environment Variables

- `MONGO_URI`: MongoDB connection string
- `DB_NAME`: Name of the MongoDB database
- `MONGO_ROOT_USERNAME`: MongoDB root username
- `MONGO_ROOT_PASSWORD`: MongoDB root password

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a merge request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.