# Streaming Application with Spring Boot, FastAPI and React

This project demonstrates how to create a streaming application using Spring Boot, FastAPI, and React. The application streams a message letter by letter from the backend (Spring Boot) to the frontend (React)


## Introduction

This project integrates Spring Boot, FastAPI, and React.

**FastAPI** handles the API endpoints for sending messages. It is responsible for receiving the messages from the user and forwarding them to the Spring Boot application.

**Spring Boot** manages the message streaming process. Upon receiving messages from FastAPI, it processes them and streams the output to the frontend application using Server-Sent Events (SSE).

**React** powers the frontend application, displaying the streamed messages in real-time. The application listens for incoming messages from the Spring Boot backend and updates the user interface dynamically.


## Features

Stream messages letter by letter from the backend to the frontend.

Display the streamed messages in a React application.

Simple and intuitive user interface.


## Architecture

The project consists of three main components:

**Spring Boot**: Backend service to handle message streaming.

**FastAPI**: API service to send messages to the Spring Boot application.

**React**: Frontend application to display the streamed messages.


## Usage

To send messages to the backend (Spring Boot) via FastAPI, use the following curl command in a seperate terminal after running Fastapi and Springboot:

    curl -X POST http://localhost:8000/send-message

After sending the message, run react app to start the application.


## Prerequisites

Java 11 or higher

Python 3.8 or higher

Node.js and npm

Maven


## Technologies Used

**Spring Boot**: Backend service for message streaming.

**FastAPI**: API service for sending messages.

**React**: Frontend application for displaying messages.

**Axios**: HTTP client for making API requests from React.

**JavaScript (React)**: Frontend development.

**Java**: Backend development with Spring Boot.

**Python**: API development with FastAPI.


## License

This project is licensed under the MIT License.
