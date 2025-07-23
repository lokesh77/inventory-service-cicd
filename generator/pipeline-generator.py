import yaml

def load_blueprint(path='blueprints/blueprint.yml'):
    with open(path) as f:
        return yaml.safe_load(f)

def generate_pipeline(config):
    includes = [
        f"templates/build/{config['language']}.yml",
        f"templates/deploy/{config['deploy_method']}.yml",
        "templates/scan/lint.yml"
    ]
    for test in config.get("test_type", []):
        includes.append(f"templates/test/{test}.yml")

    return {
        "include": [{"local": f} for f in includes],
        "stages": ["lint", "build", "test", "deploy"],
        "variables": {
            "PROJECT_NAME": config["project_name"],
            "DEPLOY_ENVIRONMENTS": ",".join(config["environments"]),
        }
    }

def write_pipeline(pipeline_dict, out_path=".gitlab-ci.yml"):
    with open(out_path, 'w') as f:
        yaml.dump(pipeline_dict, f, sort_keys=False)

if __name__ == "__main__":
    config = load_blueprint()
    pipeline = generate_pipeline(config)
    write_pipeline(pipeline)
    print("✅ Pipeline generated: .gitlab-ci.yml")
