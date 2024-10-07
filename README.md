# BlackMole Media Hub

Welcome to **BlackMole Media Hub**, a Python (Flask) web application built and deployed using Azure App Service. This project powers the website [www.blackmolecaptures.com](http://www.blackmolecaptures.com), a platform showcasing stunning photography, multimedia content, and creative work.

## Table of Contents

- [Project Overview](#project-overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Installation](#installation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

BlackMole Media Hub is a scalable, cloud-based platform designed to host and manage the photography portfolio and media services offered through the **Black Mole Captures** brand. Leveraging the Flask framework and deployed using Azure App Service, this project ensures high availability, secure hosting, and seamless content delivery.

## Tech Stack

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (can be upgraded to Azure SQL or any RDBMS)
- **Cloud Hosting**: Azure App Service
- **Version Control**: Git, Azure DevOps Repos
- **CI/CD Pipeline**: Azure Pipelines

## Features

- **Responsive Web Design**: Optimized for various devices including desktops, tablets, and smartphones.
- **Dynamic Content**: Integration of a dynamic portfolio showcasing high-resolution images and videos.
- **Scalable Architecture**: Hosted on Azure App Service for reliability and scalability.
- **Continuous Integration & Delivery**: Automated deployment using Azure Pipelines for seamless updates.
- **Secure**: HTTPS enabled with integrated Azure Key Vault for secrets management.

## Installation

To run the project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://dev.azure.com/<your-organization>/blackmole-media-hub/_git/blackmole-media-hub
    cd blackmole-media-hub
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:

    ```bash
    flask run
    ```

5. Visit `http://127.0.0.1:5000/` to see the site locally.

## Deployment

This project is deployed using **Azure App Service**. To deploy any new changes:

1. **Push changes to your Azure DevOps repository**.
2. **Azure Pipelines** will automatically trigger a CI/CD pipeline that builds, tests, and deploys the updated Flask app to Azure App Service.

### Setting up Azure App Service:

- Create an Azure App Service instance.
- Configure the deployment center to connect your Azure DevOps repo.
- Set up application settings such as `FLASK_ENV`, `SECRET_KEY`, etc. in the Azure portal.

## Usage

You can access the live website at: [www.blackmolecaptures.com](http://www.blackmolecaptures.com).

The platform allows users to:

- Browse the photography portfolio
- View high-quality image galleries
- Contact for booking and collaborations

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
