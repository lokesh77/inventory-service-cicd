# 🚀 Modular CI/CD Framework using Blueprint Templates (GitLab CI)

This project demonstrates a **modular, auto-generated CI/CD pipeline** for any tech stack using a **blueprint YAML file**. It supports different languages, build tools, test types, and deployment strategies in a reusable, standardized way.

## 📁 Project Structure

```
inventory-service-cicd/
├── app/                        # Application source code
├── tests/                      # Unit and integration tests
├── Dockerfile                  # Docker image setup
├── blueprints/blueprint.yml   # Blueprint config for pipeline
├── templates/                 # Shared modular CI/CD templates
├── generator/                 # Script to auto-generate pipeline
├── .gitlab-ci.yml             # Auto-generated pipeline (output)
├── requirements.txt, setup.py # Python project files
└── README.md
```

## 🔧 Prerequisites

- Python 3.7+
- GitLab (for GitLab CI)
- GitHub (to host source code)
- Docker (for building containers)

## 🧩 Step 1: Define the Blueprint

Create the file: `blueprints/blueprint.yml`

```yaml
project_name: "inventory-service"
language: "python"
build_tool: "pip"
test_type: ["unit", "integration"]
deploy_method: "docker"
branching: "semantic"
environments:
  - dev
  - staging
  - prod
```

## 🏗️ Step 2: Customize CI Templates

All CI stages are modular:

| Category | File                                          |
|----------|-----------------------------------------------|
| Build    | `templates/build/python.yml`                  |
| Test     | `templates/test/unit.yml`, `integration.yml`  |
| Deploy   | `templates/deploy/docker.yml`                 |
| Scan     | `templates/scan/lint.yml`                     |

## ⚙️ Step 3: Run the Generator Script

Use the generator to auto-assemble `.gitlab-ci.yml` from your blueprint:

```bash
python3 generator/pipeline-generator.py
```

✅ Output:

```
✅ Pipeline generated: .gitlab-ci.yml
```

## 🧾 Generated `.gitlab-ci.yml`

```yaml
include:
  - local: templates/build/python.yml
  - local: templates/deploy/docker.yml
  - local: templates/scan/lint.yml
  - local: templates/test/unit.yml
  - local: templates/test/integration.yml

stages:
  - lint
  - build
  - test
  - deploy

variables:
  PROJECT_NAME: inventory-service
  DEPLOY_ENVIRONMENTS: dev,staging,prod
```

## 🚀 Step 4: Push to GitLab

Once `.gitlab-ci.yml` is generated, push your changes:

```bash
git add .
git commit -m "Generate CI pipeline from blueprint"
git push origin main
```

Then head to **GitLab > CI/CD > Pipelines** to see it in action.

## 🔄 Updating the Pipeline

Modify `blueprint.yml`, then re-run:

```bash
python3 generator/pipeline-generator.py
```

Your `.gitlab-ci.yml` will automatically update with the new configuration.

## 🔌 Supported Features

✅ Multiple languages (Python, Node, Java…)  
✅ Multiple test types (unit, integration, e2e)  
✅ Flexible deploy options (Docker, CDK, Terraform)  
✅ Modular templates  
✅ Reusable across multiple projects  
✅ Instant setup with minimal effort

## 📁 Example App Included

### `app/main.py`

```python
def hello():
    return "Hello, Inventory!"
```

### `tests/test_unit.py`

```python
from app.main import hello

def test_hello():
    assert hello() == "Hello, Inventory!"
```


## To support new languages or deployment methods:

1. Add a new template in `templates/`
2. Adjust `generator/pipeline-generator.py` if needed
3. Test with a new blueprint config

## 📣 Final Tip

Run this once per microservice with its own `blueprint.yml` and never manually write CI/CD YAML again. Keep consistency, reduce errors, and scale your development velocity.
