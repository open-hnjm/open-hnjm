import yaml
from multiprocessing import Process
import subprocess


def load_config(config_path: str) -> dict:
    with open('config/'+config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def start_module(module_name: str, server_mode=None):
    if server_mode:
        subprocess.run(['python', '-m', f'app.{module_name}.server'])
    else:
        subprocess.run(['python', '-m', f'app.{module_name}.main'])


def print_table(enabled_modules, disabled_modules):
    print("-" * 30)
    print(f"{'Module':<20} {'Status':<10}") 
    print("-" * 30)
    for module in enabled_modules:
        print(f"{module:<20} {'Enabled':<10}")
    for module in disabled_modules:
        print(f"{module:<20} {'Disabled':<10}")


def main():
    config = load_config('config.yaml')

    enabled_modules = []
    disabled_modules = []

    processes = []
    for module, settings in config.items():
        if settings.get('enable', False):
            enabled_modules.append(module)
            process = Process(target=start_module, args=(module, settings.get('server_mode'),))
            processes.append(process)
            process.start()
        else:
            disabled_modules.append(module)

    for process in processes:
        process.join()

    print_table(enabled_modules, disabled_modules)


if __name__ == "__main__":
    main()
