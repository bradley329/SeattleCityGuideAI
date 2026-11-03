# Azure App Service basic Python Flask sample

This repository contains a minimal Python Flask web application for Azure App
Service. You can run it locally, deploy it with Azure Developer CLI, or use it
as source for an App Service deployment workflow.

## What's included

- `app.py` contains the Flask application.
- `requirements.txt` lists the Python packages installed during deployment.
- `templates/` and `static/` contain the HTML templates and styles.
- `infra/` contains Bicep modules for an App Service plan and Linux web app.
- `azure.yaml` describes the application to Azure Developer CLI.

The Bicep templates deploy a Basic B1 App Service plan and a Python 3.12 Linux
web app. Resource names follow Azure Developer CLI conventions unless you
override the optional name parameters in `infra/main.bicep`.

## Run locally

Install Python 3.12, then clone and start the app:

```shell
git clone https://github.com/microsoft/app-service-basic-sample.git
cd app-service-basic-sample
python -m venv .venv
```

Activate the virtual environment on macOS or Linux:

```shell
. .venv/bin/activate
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the packages and run the development server:

```shell
python -m pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

## Deploy with Azure Developer CLI

After you [install Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd),
sign in and deploy:

```shell
azd auth login
azd up
```

`azd up` creates Azure resources in the subscription and location you select.

## Source and third-party software

This sample is adapted from
[`Azure-Samples/msdocs-python-flask-webapp-quickstart`](https://github.com/Azure-Samples/msdocs-python-flask-webapp-quickstart).
See [NOTICE](NOTICE) for copied third-party software and linked package
dependencies.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). This project follows the
[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

## Security

Report security vulnerabilities privately to the Microsoft Security Response
Center through the [MSRC Researcher Portal](https://msrc.microsoft.com/create-report).
Do not report security vulnerabilities through public GitHub issues. See the
[MSRC reporting FAQ](https://www.microsoft.com/msrc/faqs-report-an-issue) for
more information.

## License

This project is licensed under the MIT License. See [LICENSE.TXT](LICENSE.TXT).

## Trademarks

This project may contain trademarks or logos for projects, products, or
services. Authorized use of Microsoft trademarks or logos is subject to the
[Microsoft Trademark and Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks).
Use of Microsoft trademarks or logos in modified versions of this project must
not cause confusion or imply Microsoft sponsorship. Any use of third-party
trademarks or logos is subject to those third parties' policies.
